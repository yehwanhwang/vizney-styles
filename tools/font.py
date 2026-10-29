"""Build VZ Sans for the site pages (index.html, 404.html), the same font as on Vizney Blocks.

VZ Sans is Spoqa Han Sans Neo cut down to the characters the site pages use. SIL OFL 1.1: a modified
(subset) font must not keep the original family name, and the copyright notice stays (OFL.txt).

Usage: python3 tools/font.py <font-dir>    (pip install fonttools)

<font-dir> is Original/SpoqaHanSansNeo of github.com/spoqa/spoqa-han-sans (v3.3.0). The fonts in its
Subset folder (the ones the Spoqa CDN serves) leave out kerning (GPOS) and a few signs (© – −), and turn
off USE_TYPO_METRICS: Windows then lays lines out with the taller win metrics (1100/310) instead of the
typo metrics (970/282) that macOS and the installed font use, and every line of text sits 1-3px lower.
The flag is set again below whatever the source, so VZ Sans keeps the original's line metrics everywhere.

Writes assets/fonts/vz-sans-{300,400,500,700}.woff and puts the fonts' hash in the ?v= of the font URLs
in both pages. Run it again whenever the text of those pages changes. Sample screens load their own fonts.
"""
import hashlib
import html
import re
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
PAGES = [ROOT / 'index.html', ROOT / '404.html']
OUT = ROOT / 'assets' / 'fonts'
SIGNS = '0123456789.,+-−–%()[]/:·×…→←↑↓↗₩© '
# Weight 300 only draws the step numbers (.steps li::before), so it carries digits alone.
WEIGHTS = (('Light', 300), ('Regular', 400), ('Medium', 500), ('Bold', 700))

if len(sys.argv) != 2:
    sys.exit(__doc__)
font_dir = Path(sys.argv[1])

# Every character a page can render: its markup, its strings (STR, both languages) and any \u escapes.
chars = set(SIGNS) | {chr(c) for c in range(0x20, 0x7f)}
for page in PAGES:
    raw = page.read_text(encoding='utf-8')
    raw = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), raw)
    chars |= set(html.unescape(raw))
text = ''.join(sorted(c for c in chars if c >= ' '))
digits = '0123456789'

OUT.mkdir(parents=True, exist_ok=True)
built = []
for style, weight in WEIGHTS:
    want = digits if weight == 300 else text
    # recalcTimestamp=False keeps the output byte-identical when the text has not changed.
    font = TTFont(font_dir / f'SpoqaHanSansNeo-{style}.ttf', recalcTimestamp=False)
    cmap = font.getBestCmap()
    missing = ''.join(c for c in want if ord(c) not in cmap and not c.isspace())
    if missing:
        print(f'warning: SpoqaHanSansNeo-{style}.ttf has no glyph for {missing}; '
              'these fall back to the next font. Use the Original folder.', file=sys.stderr)
    options = subset.Options()
    options.layout_features = ['*']
    options.hinting = False
    options.desubroutinize = True
    options.name_IDs = ['*']
    sub = subset.Subsetter(options)
    sub.populate(text=want)
    sub.subset(font)

    name = font['name']
    copyright_ = (name.getDebugName(0) or 'Copyright 2020 Spoqa').replace('\\', '')
    values = {
        0: f'{copyright_}. Modified (subset and renamed) from Spoqa Han Sans Neo.',
        1: 'VZ Sans' if style in ('Regular', 'Bold') else f'VZ Sans {style}',
        2: 'Bold' if style == 'Bold' else 'Regular',
        3: f'VZ Sans {style}; subset of Spoqa Han Sans Neo 1.100',
        4: f'VZ Sans {style}',
        6: f'VZSans-{style}',
        16: 'VZ Sans',
        17: style,
    }
    # Drop every record that still carries the original family name, then write ours.
    name.names = [r for r in name.names if r.nameID not in (1, 2, 3, 4, 6, 7, 16, 17, 18, 21, 22)]
    for nid, value in values.items():
        name.setName(value, nid, 3, 1, 0x409)
        name.setName(value, nid, 1, 0, 0)

    # Line metrics: USE_TYPO_METRICS (fsSelection bit 7, OS/2 version 4 and up) makes Windows use the
    # typo values, which equal hhea here, so lines sit the same on Windows, macOS and the installed font.
    os2 = font['OS/2']
    os2.version = max(os2.version, 4)
    os2.fsSelection |= 1 << 7
    hhea = font['hhea']
    if (os2.sTypoAscender, os2.sTypoDescender, os2.sTypoLineGap) != (hhea.ascent, hhea.descent, hhea.lineGap):
        print(f'warning: typo and hhea metrics differ in SpoqaHanSansNeo-{style}.ttf', file=sys.stderr)

    font.flavor = 'woff'
    out = OUT / f'vz-sans-{weight}.woff'
    font.save(out)
    built.append(out.read_bytes())
    print(f'{out.name}: {out.stat().st_size // 1024} KB, {len(font.getGlyphOrder())} glyphs, '
          f'kerning {"yes" if "GPOS" in font else "no"}')

# Cache busting: the URLs change only when the fonts do.
version = hashlib.sha1(b''.join(built)).hexdigest()[:10]
for page in PAGES:
    src = page.read_text(encoding='utf-8')
    new, n = re.subn(r'(/assets/fonts/vz-sans-\d{3}\.woff\?v=)[0-9a-z_]+', rf'\g<1>{version}', src)
    if n == 0:
        sys.exit(f'{page.name}: no /assets/fonts/vz-sans-*.woff?v= URL to update')
    if new != src:
        page.write_text(new, encoding='utf-8')
    print(f'{page.name}: {n} font URLs at v={version}')
