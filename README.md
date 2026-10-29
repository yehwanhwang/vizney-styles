# Vizney Styles

Named dashboard styles from [Vizney](https://www.vizney.com). Each style is one screen and a short spec (`style.md`), so it can be rebuilt by name: share the spec and ask for "the Chalk style". The same screen is the live sample, the 4:5 poster for social posts and the 16:9 cover.

Served at **https://styles.vizney.com** (GitHub Pages, `main` branch). Everything pushed to `main` is published immediately, so keep work in progress off `main`. The home page is `index.html`: the style gallery and an introduction to company styles. Every page opens in English; add `?lang=ko` for Korean.


## Styles

A style is a look and feel, not a dataset. The sample data only shows the style at work.

Styles come in two series. **Texture styles** (Chalk, Glass, Tile) are named after a material and show a look of our own. **Brand styles** (Anthropic) are named after the company whose public website the look was read from, the way [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) catalogs DESIGN.md files: they are independent readings of publicly visible design, not official designs, and they are not affiliated with or endorsed by the companies. A brand style never carries the company's logo, wordmark, typefaces, images or data; the sample screen uses a fictional business and fictional numbers, and the sample, the spec and the blog post all say so. If a company asks for its style to be taken down, it comes down. Trademarks belong to their owners.

| Style | Feel | Sample | Spec | Blog posts |
|---|---|---|---|---|
| Chalk (초크) | Pastel, calm, clean. | [Live sample](https://styles.vizney.com/chalk/) · online store orders (fictional) | [style.md](chalk/style.md) | [KO](https://kr.vizney.com/style-chalk/) · [EN](https://www.vizney.com/style-chalk/) |
| Glass (글래스) | Pastel gradient, frosted glass cards | [Live sample](https://styles.vizney.com/glass/) · online store sales (fictional) | [style.md](glass/style.md) | [KO](https://kr.vizney.com/style-glass/) · [EN](https://www.vizney.com/style-glass/) |
| Tile (타일) | Airy white cards, blue–mint rings | [Live sample](https://styles.vizney.com/tile/) · hotel operations (fictional) | [style.md](tile/style.md) | [KO](https://kr.vizney.com/style-tile/) · [EN](https://www.vizney.com/style-tile/) |
| Anthropic (앤트로픽) | Warm ivory, editorial serif, hairline rows | [Live sample](https://styles.vizney.com/anthropic/) · publisher sales (fictional) | [style.md](anthropic/style.md) | [KO](https://kr.vizney.com/style-anthropic/) · [EN](https://www.vizney.com/style-anthropic/) |


## Adding a style

The full production checklist used with Claude is in [CLAUDE.md](https://github.com/yehwanhwang/vizney-styles/blob/main/CLAUDE.md).

1. Name a texture style with one evocative material or texture word (Chalk, Glass, Linen …) and a brand style with the company's name (Anthropic), and use the name on its own: Vizney Styles is the collection, not part of the name. The folder is the name in lowercase, at the root: `chalk/`. Never name a folder after its sample data.
2. Give it three words ("Pastel, calm, clean." · "파스텔톤, 차분함, 깔끔함."). The name is for remembering; the three words carry the feel at a glance. Make one or two of them words people actually search for (pastel, clean, minimal, dark …) and at least one that no other style uses. The one-sentence intro in the spec and the post excerpt describe what the style looks like.
3. Put these files in the folder:
   - `index.html`: the one screen, self-contained (data included), English and Korean in one file: English by default, Korean with `?lang=ko`. It opens with the series line (`VIZNEY STYLES · 01`, numbered in release order), the name in capitals and the three words, and it fits in one 1080×1350 screen. Colors, fonts and photos go inside data cards, not in separate swatch panels.
   - `style.md`: layout, colors, type, components, motion and don'ts, detailed enough to rebuild the style from its name. It is published at `<name>/style.html`.
   - A photo, if the style uses one (`chalk/chalk.jpg`): your own, or one you are clearly allowed to publish.
4. Add these lines to the page's `<head>`, with the style's own font links (the ones below are Chalk's: Inter for English, Pretendard for Korean, Space Grotesk for the name):

   ```html
   <meta name="robots" content="noindex">
   <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Space+Grotesk:wght@700&display=swap">
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
   <script src="/lib/embed.js" defer></script>
   ```

   `noindex` keeps search traffic on the blog post instead of the bare screen.
5. In embed mode `<html>` gets the class `vz-embed`. Reset any viewport-height layout there and hide page-only notes. With `?shot=1` the page gets `vz-shot`: it hides the language toggle and the footer note and stretches the last row to the bottom of the screen, for captures.
6. Capture from `?shot=1` at 2×: `poster-ko.png` / `poster-en.png` (1080×1350) for Instagram and LinkedIn, and `cover-ko.png` / `cover-en.png` (1440×810) for the post's feature image, the home card and link previews.
7. Publish the blog post at `style-<name>` (for example `/style-chalk/`) on both sites.
8. Update in place; Git history keeps the old versions. Add a row to the Styles table and a card to the home page (`index.html`), then rebuild the site font (below).

Glass, Tile and Anthropic still use the earlier format (a 16:9 app screen and a subtitle that describes the look). They move to the one-screen format in turn.


## Site font

The home page and the 404 page use VZ Sans, the same font as [Vizney Blocks](https://blocks.vizney.com): Spoqa Han Sans Neo cut down to the characters those two pages use and renamed, as the SIL Open Font License asks of a modified font ([OFL.txt](OFL.txt)). It is built from the `Original/SpoqaHanSansNeo` folder of [spoqa-han-sans](https://github.com/spoqa/spoqa-han-sans), not from `Subset` (the files the Spoqa CDN serves), which lacks kerning and a few signs and draws text 1–3px lower on Windows. After changing the text of either page, rebuild it:

```bash
pip install fonttools
python3 tools/font.py /path/to/spoqa-han-sans/Original/SpoqaHanSansNeo
```

The script writes `assets/fonts/` and updates the `?v=` of the font URLs in both pages. Sample screens load their own fonts from a CDN, as their specs say.


## Embedding in a Ghost post

Paste into an HTML card and change the style, language and title. Always set `lang` in the URL rather than relying on the default:

```html
<figure class="kg-card kg-embed-card kg-width-wide">
  <iframe data-vizney-embed src="https://styles.vizney.com/chalk/?lang=ko&amp;embed=1" title="Chalk 스타일 대시보드" loading="lazy" style="display:block;width:100%;height:820px;border:1px solid #e6e6e6;border-radius:12px"></iframe>
  <figcaption><a href="https://styles.vizney.com/chalk/?lang=ko" target="_blank" rel="noopener">전체 화면으로 보기 ↗</a></figcaption>
</figure>
<script src="https://styles.vizney.com/lib/embed-host.js" defer></script>
```

`lib/embed-host.js` resizes the iframe to the height the page reports through `lib/embed.js`, so the whole screen shows without an inner scrollbar. Without it, the iframe keeps its fixed height and scrolls.
