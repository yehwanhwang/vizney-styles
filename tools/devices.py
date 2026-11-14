"""Crop the home page's three device examples from the live samples, in both languages.

Usage: python3 tools/devices.py [--offline-fonts DIR] [name ...]

The home page's section 'a style is a reading, not a theme' shows one device from each of three samples:
F1's onboard display, Costco's register receipt and Singapore Airlines' boarding pass. This opens each sample
at 1440px (2x, reduced motion), places a 16:10 window around the device and writes
assets/home/device-<name>-<lang>.webp. Run it again when one of those samples changes. To show another device,
add its sample and window below and change the home page's .devs list and STR (dev1t … dev3p).

--offline-fonts DIR  as in tools/shots.py, for sandboxes that cannot reach the font CDNs.
Needs Playwright with Chromium and Pillow.
"""
import argparse
import io

from PIL import Image
from playwright.sync_api import sync_playwright

from shots import ROOT, OfflineFonts, serve

OUT = ROOT / 'assets' / 'home'
# A 16:10 window around each device, in CSS pixels of the 1440px page.
CLIPS = {
    'f1': '''() => { const r = document.getElementById('cluster').getBoundingClientRect();
        const w = r.width + 40, h = w / 1.6; return {x: r.left - 20, y: r.top + r.height / 2 - h / 2 + scrollY, width: w, height: h}; }''',
    'costco': '''() => { const p = document.getElementById('t1').getBoundingClientRect(), b = document.getElementById('t1Body').getBoundingClientRect();
        const w = p.width + 40, h = w / 1.6; return {x: p.left - 20, y: b.top - 14 + scrollY, width: w, height: h}; }''',
    'singapore-airlines': '''() => { const r = document.getElementById('bp').getBoundingClientRect();
        const h = r.height + 20, w = h * 1.6; return {x: r.left - 20, y: r.top - 14 + scrollY, width: w, height: h}; }''',
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('names', nargs='*')
    ap.add_argument('--offline-fonts')
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    server = serve(ROOT)
    url = f'http://127.0.0.1:{server.server_port}'
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, js in CLIPS.items():
            if args.names and name not in args.names:
                continue
            fonts = OfflineFonts(args.offline_fonts, (ROOT / name / 'index.html').read_text(encoding='utf-8')) if args.offline_fonts else None
            for lang in ('ko', 'en'):
                ctx = browser.new_context(viewport={'width': 1440, 'height': 900}, device_scale_factor=2, reduced_motion='reduce')
                if fonts:
                    fonts.attach(ctx)
                page = ctx.new_page()
                page.goto(f'{url}/{name}/?lang={lang}', wait_until='load')
                page.evaluate('document.fonts.ready')
                page.wait_for_timeout(1200)
                im = Image.open(io.BytesIO(page.screenshot(clip=page.evaluate(js)))).convert('RGB')
                out = OUT / f'device-{name}-{lang}.webp'
                im.save(out, 'WEBP', quality=88, method=6)
                print(f'{out.relative_to(ROOT)}  {im.size[0]}x{im.size[1]}  {out.stat().st_size // 1024} KB')
                ctx.close()
        browser.close()
    server.shutdown()


if __name__ == '__main__':
    main()
