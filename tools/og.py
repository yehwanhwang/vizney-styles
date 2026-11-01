"""Make the site's link-preview image, og.png (1200 × 630), in the blog's post-image format.

Usage: python3 tools/og.py

The blog (kr.vizney.com · www.vizney.com) gives every post image the same frame: a black background
(#1b1b1b), one yellow point (#ffcc00) and the white 'Vizney' wordmark at the bottom centre. og.png uses that
frame so a shared styles.vizney.com link looks like the rest of Vizney: the line name and the headline on the
left (DASHBOARD.md in yellow), the newest style's cover on the right in a yellow frame, the wordmark below.

The newest style is the last entry of catalog.json; its cover-en.png is cropped above the cover's own wordmark
band. Text is English and set in VZ Sans from assets/fonts. Run it again whenever the catalog or the home page's
first-screen copy changes, and bump ?v= on the og:image meta in index.html.
Needs Playwright with Chromium.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from shots import ROOT, serve  # noqa: E402

SIZE = (1200, 630)
HEADLINE = ("<em>DASHBOARD.md</em> for your company's dashboards")
LEDE = ("A company's look, worked out for dashboards: a spec your AI agents follow, "
        "a live sample, and Tableau and Power BI files.")

PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:'VZ Sans';font-weight:400;src:url(/assets/fonts/vz-sans-400.woff) format('woff')}
@font-face{font-family:'VZ Sans';font-weight:500;src:url(/assets/fonts/vz-sans-500.woff) format('woff')}
@font-face{font-family:'VZ Sans';font-weight:700;src:url(/assets/fonts/vz-sans-700.woff) format('woff')}
*{box-sizing:border-box;margin:0}
html,body{width:1200px;height:630px;overflow:hidden}
body{position:relative;background:#1b1b1b;color:#fff;font-family:'VZ Sans',sans-serif;-webkit-font-smoothing:antialiased}
.copy{position:absolute;left:64px;top:84px;width:500px}
.line{font-size:15px;font-weight:700;letter-spacing:.16em;color:#ffcc00}
h1{margin-top:22px;font-size:52px;line-height:1.12;font-weight:700;letter-spacing:-.03em}
h1 em{font-style:normal;color:#ffcc00}
p{margin-top:24px;font-size:20px;line-height:1.55;color:rgba(255,255,255,.72)}
.shot{position:absolute;right:56px;top:84px;width:536px}
.frame{border:3px solid #ffcc00;border-radius:12px;overflow:hidden;aspect-ratio:1440/726;background:#2a2a2a}
.frame img{display:block;width:100%;height:auto}
.cap{margin-top:14px;font-size:15px;line-height:1.4;color:rgba(255,255,255,.72)}
.cap b{font-weight:500;color:#fff}
.wm{position:absolute;left:50%;bottom:34px;width:106px;height:40px;margin-left:-53px}
</style></head><body>
<div class="copy"><div class="line">VIZNEY STYLES</div><h1>__HEADLINE__</h1><p>__LEDE__</p></div>
<figure class="shot" style="margin:0"><div class="frame"><img src="/__SLUG__/cover-en.png" alt=""></div>
<figcaption class="cap"><b>Newest · __NUM__ __NAME__</b> · __WORDS__</figcaption></figure>
<img class="wm" src="/assets/brand/vizney-wordmark-white.png" alt="">
</body></html>"""


def main():
    newest = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))['styles'][-1]
    html = (PAGE.replace('__HEADLINE__', HEADLINE).replace('__LEDE__', LEDE)
            .replace('__SLUG__', newest['slug']).replace('__NUM__', f"{newest['number']:02d}")
            .replace('__NAME__', newest['name']).replace('__WORDS__', newest['words']))

    from playwright.sync_api import sync_playwright

    server = serve(ROOT)
    base = f'http://127.0.0.1:{server.server_address[1]}/'
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': SIZE[0], 'height': SIZE[1]})
        page.route(base + '__og__.html', lambda route: route.fulfill(body=html, content_type='text/html'))
        page.goto(base + '__og__.html', wait_until='networkidle')
        page.evaluate('document.fonts.ready')
        page.screenshot(path=str(ROOT / 'og.png'))
        browser.close()
    server.shutdown()
    print('og.png')


if __name__ == '__main__':
    main()
