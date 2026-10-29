"""Capture a style's covers from its sample screen.

Usage: python3 tools/shots.py <name> [--review DIR] [--offline-fonts DIR]

Serves the repository root on a local port, opens <name>/?lang=en|ko in headless Chromium (Playwright,
with reduced motion so animations never land in a capture) and writes into <name>/:

    cover-en.png, cover-ko.png    1440 × 810 at 2×    home card, post feature image, link previews

It exits with an error if a page throws.

--review DIR         also writes full-page captures at 1440, 1200, 1024 and 390px, in both languages,
                     to DIR (outside the repository) for the visual check, and flags horizontal overflow.
--offline-fonts DIR  for sandboxes that cannot reach the font CDNs. Font requests are answered from
                     partial clones in DIR, made with git on first use:
                       cdn.jsdelivr.net/gh/<owner>/<repo>@<ref>/…  from DIR/<repo> (e.g. Pretendard, Spoqa)
                       fonts.googleapis.com/css2?family=…          from DIR/font-files (fontsource; its variable
                                                                   font when an axis such as opsz is a range)

Needs Playwright with Chromium: pip install playwright && python3 -m playwright install chromium.
"""
import argparse
import functools
import posixpath
import re
import subprocess
import sys
import threading
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COVER = (1440, 810)
REVIEW_WIDTHS = (1440, 1200, 1024, 390)
LANGS = ('en', 'ko')

JSDELIVR = re.compile(r'https://cdn\.jsdelivr\.net/gh/([^/]+)/([^/@]+)@([^/]+)/([^?#]+)')
GSTATIC = 'https://fonts.gstatic.com/vz-offline/'


def serve(root):
    class Quiet(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass
    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=str(root)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def git(*args):
    subprocess.run(['git', *args], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def sparse_clone(url, dest, ref=None):
    if (dest / '.git').exists():
        return
    cmd = ['clone', '--depth', '1', '--filter=blob:none', '--sparse']
    if ref:
        cmd += ['--branch', ref]
    git(*cmd, url, str(dest))


def sparse_add(dest, *paths):
    if paths:
        git('-C', str(dest), 'sparse-checkout', 'add', *paths)


def local_css(path):
    """jsDelivr minifies on the fly: a .min.css that is not in the repository is its .css."""
    if path.name.endswith('.min.css') and not path.exists():
        return path.with_name(path.name[:-len('.min.css')] + '.css')
    return path


class OfflineFonts:
    """Answers the page's font requests from partial git clones instead of the CDNs."""

    def __init__(self, base, page_html):
        self.base = Path(base).resolve()
        self.base.mkdir(parents=True, exist_ok=True)
        links = re.findall(r'<link[^>]+href="([^"]+)"', page_html)
        for link in links:
            m = JSDELIVR.match(link)
            if m:
                self._prepare_jsdelivr(*m.groups())
        families = []
        for link in links:
            if link.startswith('https://fonts.googleapis.com/css2?'):
                families += self._parse_google(link)
        if families:
            dest = self.base / 'font-files'
            sparse_clone('https://github.com/fontsource/font-files', dest)
            sparse_add(dest, *sorted({f'fonts/{"variable" if ranged else "google"}/{slug}'
                                      for _, slug, ranged, _ in families}))

    def _prepare_jsdelivr(self, owner, repo, ref, path):
        dest = self.base / repo
        sparse_clone(f'https://github.com/{owner}/{repo}', dest, ref)
        sparse_add(dest, posixpath.dirname(path))
        css = local_css(dest / path)
        if css.exists():
            refs = re.findall(r'url\(["\']?([^"\')]+)["\']?\)', css.read_text(encoding='utf-8'))
            dirs = {posixpath.dirname(posixpath.normpath(posixpath.join(posixpath.dirname(path), r)))
                    for r in refs if not r.startswith(('http:', 'https:', 'data:'))}
            sparse_add(dest, *sorted(d for d in dirs if d and not d.startswith('..')))

    @staticmethod
    def _parse_google(url):
        """'Source Serif 4:ital,opsz,wght@0,8..60,400;1,8..60,400'
        → [('Source Serif 4', 'source-serif-4', True, [('400', False), ('400', True)])]: the family, its
        fontsource folder, whether an axis other than weight is a range (then Google serves the variable
        font, e.g. with optical sizes), and the weights and styles asked for."""
        out = []
        for spec in urllib.parse.parse_qs(urllib.parse.urlsplit(url).query).get('family', []):
            name, _, axes = spec.partition(':')
            slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
            styles, ranged = [], False
            if not axes:
                styles.append(('400', False))
            else:
                keys, _, tuples = axes.partition('@')
                keys = keys.split(',')
                for t in tuples.split(';'):
                    values = dict(zip(keys, t.split(',')))
                    ranged = ranged or any('..' in v for k, v in values.items() if k != 'wght')
                    weight = values.get('wght', '400')
                    italic = values.get('ital', '0') == '1'
                    if '..' in weight:   # a variable range: every static weight inside it
                        lo, hi = (int(x) for x in weight.split('..'))
                        styles += [(str(w), italic) for w in range(100, 1000, 100) if lo <= w <= hi]
                    else:
                        styles.append((weight, italic))
            out.append((name, slug, ranged, styles))
        return out

    def attach(self, context):
        context.route('https://cdn.jsdelivr.net/**', self._jsdelivr)
        context.route('https://fonts.googleapis.com/**', self._google_css)
        context.route('https://fonts.gstatic.com/**', self._google_file)

    @staticmethod
    def _content_type(path):
        return {'.css': 'text/css', '.woff2': 'font/woff2', '.woff': 'font/woff',
                '.ttf': 'font/ttf', '.otf': 'font/otf'}.get(path.suffix, 'application/octet-stream')

    def _send(self, route, path):
        if not path.is_file():
            print(f'offline font missing: {path}', file=sys.stderr)
            return route.abort()
        return route.fulfill(status=200, content_type=self._content_type(path), body=path.read_bytes())

    def _jsdelivr(self, route, request):
        m = JSDELIVR.match(request.url)
        if not m:
            return route.abort()
        _, repo, _, path = m.groups()
        return self._send(route, local_css(self.base / repo / path))

    def _google_css(self, route, request):
        css = []
        fonts = self.base / 'font-files' / 'fonts'
        for name, slug, ranged, styles in self._parse_google(request.url):
            if ranged:   # the variable font with all its axes; fontsource names the family '<name> Variable'
                files = [(fonts / 'variable' / slug / f'standard{"-italic" if italic else ""}.css', f'variable/{slug}')
                         for italic in sorted({italic for _, italic in styles})]
            else:
                files = [(fonts / 'google' / slug / f'{weight}{"-italic" if italic else ""}.css', f'google/{slug}')
                         for weight, italic in styles]
            for path, folder in files:
                if not path.is_file():
                    print(f'offline font missing: {path}', file=sys.stderr)
                    continue
                text = path.read_text(encoding='utf-8').replace('url(./files/', f'url({GSTATIC}{folder}/files/')
                css.append(text.replace(f"font-family: '{name} Variable'", f"font-family: '{name}'"))
        return route.fulfill(status=200, content_type='text/css', body='\n'.join(css))

    def _google_file(self, route, request):
        if not request.url.startswith(GSTATIC):
            return route.abort()
        rel = request.url[len(GSTATIC):].split('?')[0]
        return self._send(route, self.base / 'font-files' / 'fonts' / rel)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('name', help='style folder, e.g. anthropic')
    ap.add_argument('--review', metavar='DIR', help='also write full-page captures at four widths to DIR')
    ap.add_argument('--offline-fonts', metavar='DIR', help='answer font requests from partial clones in DIR')
    args = ap.parse_args()

    folder = ROOT / args.name
    page_html = (folder / 'index.html').read_text(encoding='utf-8')
    fonts = OfflineFonts(args.offline_fonts, page_html) if args.offline_fonts else None
    review = Path(args.review).resolve() if args.review else None
    if review:
        review.mkdir(parents=True, exist_ok=True)

    from playwright.sync_api import sync_playwright

    server = serve(ROOT)
    base = f'http://127.0.0.1:{server.server_address[1]}/{args.name}/'
    problems = []
    with sync_playwright() as p:
        browser = p.chromium.launch()

        def open_page(width, height, scale, url):
            context = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=scale,
                                          reduced_motion='reduce')
            if fonts:
                fonts.attach(context)
            page = context.new_page()
            page.on('pageerror', lambda e: problems.append(f'{url}: {e}'))
            page.goto(url, wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            page.wait_for_timeout(500)   # let charts redraw once the fonts are in
            return context, page

        for lang in LANGS:
            context, page = open_page(*COVER, 2, f'{base}?lang={lang}')
            page.screenshot(path=str(folder / f'cover-{lang}.png'))
            context.close()
            print(f'{args.name}/cover-{lang}.png')

            if review:
                for width in REVIEW_WIDTHS:
                    context, page = open_page(width, 900, 1, f'{base}?lang={lang}')
                    scroll = page.evaluate('document.documentElement.scrollWidth')
                    if scroll > width:
                        problems.append(f'{width}px {lang}: the page is {scroll}px wide')
                    page.screenshot(path=str(review / f'{args.name}-{width}-{lang}.png'), full_page=True)
                    context.close()
                print(f'review captures for {lang} in {review}')
        browser.close()
    server.shutdown()

    if problems:
        sys.exit('\n'.join(problems))


if __name__ == '__main__':
    main()
