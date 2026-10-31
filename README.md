# Vizney Styles

Dashboard design specs that AI coding agents, Tableau and Power BI can follow. Each entry in the catalog is a company's look, read from its public website and worked out for dashboards: `DASHBOARD.md`, a live sample screen with fictional data, validated data colors, and the tool files. The same package is made privately for your own company.

Served at **https://styles.vizney.com** (GitHub Pages, `main` branch). Everything pushed to `main` is published immediately, so keep work in progress off `main`. Every page opens in English; add `?lang=ko` for Korean.

Made by [Vizney](https://www.vizney.com), a BI consulting studio in Seoul.


## Catalog

| No. | Style | Feel | Sample | Spec | Files | Post |
|---|---|---|---|---|---|---|
| 01 | Anthropic | Ivory, Editorial, Quiet | [Live sample](https://styles.vizney.com/anthropic/) · the monthly operations report of Vizney Logistics (fictional), drawn in one card and chart grammar from the figures Anthropic publishes in launches and research posts, with a build workbench | [DASHBOARD.md](anthropic/DASHBOARD.md) | [anthropic/](anthropic/) | [KO](https://kr.vizney.com/style-anthropic/) · [EN](https://www.vizney.com/style-anthropic/) |

Styles are independent readings of publicly visible design, the way [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) catalogs `DESIGN.md` files. They are not official designs, and they are not affiliated with or endorsed by the companies. A style never carries the company's logo, wordmark, typefaces, images or data; the sample screen uses a fictional business and fictional numbers, and the sample, the spec and the post all say so. If a company asks for its style to be taken down, it comes down. BI vendors (Tableau, Microsoft, Google, Qlik …) are out of scope. Trademarks belong to their owners.

**Request a brand:** open an issue with the [request template](https://github.com/yehwanhwang/vizney-styles/issues/new?template=request.yml). Public requests are picked by 👍 votes, one or two a month. For your own company, [contact us](https://www.vizney.com/contact-us/): the package is private by default.


## What is in a style folder

```
anthropic/
  DASHBOARD.md        the spec: YAML front matter with the tokens, then the rules
  index.html          the live sample, one self-contained file, English and Korean
  tokens.json         the single source of every token; tools/package.py builds the files below from it
  tokens.css          CSS custom properties for web dashboards
  anthropic.tps       Tableau color palettes (categorical, sequential, diverging)
  powerbi-theme.json  Power BI report theme
  prompt.md           prompts for new builds, restyles, reviews and one reproducible figure, plus Tableau and Power BI notes
  orders.csv          sample data for the figure the sample's workbench draws (optional per style)
  cover-en.png        1440×810 at 2×: home card, post feature image, link previews
  cover-ko.png
```

### DASHBOARD.md

The file follows the `DESIGN.md` convention (front matter tokens, then prose sections an agent can read) and adds the sections a dashboard needs. Consumers that know `DESIGN.md` can ignore the extra sections; agents use all of them.

1. Visual Theme & Atmosphere
2. Color Palette & Roles
3. Data Colors — categorical, comparison, sequential, diverging and status colors, each validated for color-vision deficiency, normal-vision separation and contrast
4. Typography Rules — one serif, one sans and one mono, with Korean counterparts
5. Numbers, Dates & Units — English and Korean formats, change notation, rounding
6. Layout Principles — grid, reading order, density
7. Component Stylings — KPI card, pills and tabs, trend card, ranked list, bar list, composition, band, tooltip, legends, status pills
8. Charts — chart choice, one axis, marks, labels, forbidden forms
9. Depth & Elevation
10. Interaction & Motion
11. Accessibility
12. Responsive Behavior
13. Tool Mapping — web, Tableau, Power BI, chart tools
14. Do's and Don'ts
15. Agent Prompt Guide

### Using it

- **AI coding agents:** copy `DASHBOARD.md` (and `tokens.css`) into the repository root and ask for the style by name; `prompt.md` has tested prompts.
- **Tableau:** paste the `<color-palette>` elements of the `.tps` file into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The Tool Mapping section lists the formatting settings.
- **Power BI:** View → Themes → Browse for themes → `powerbi-theme.json`.


## Adding a style

The full production checklist used with Claude is in [CLAUDE.md](CLAUDE.md). In short:

1. Read the real CSS tokens of the company's public website (colors, type, spacing, radius) with a browser. Real values beat estimates.
2. Write a pattern inventory: the compositions and components the company actually uses — header, button variants, card anatomy, tables, number and date notation, list-page controls — and, if the company publishes charts (research, IR, blog), its chart grammar. The sample is composed from this inventory, not from a template.
3. Design the data colors from the family the brand uses in its own charts (or its accent and secondary swatches) and validate them with the dataviz skill's `validate_palette.js`; the brand accent itself is never a data color. Write them into `tokens.json`.
4. Build one landscape sample screen (`index.html`): a real business report on a fictional company, English and Korean in one file, filters that apply to every card, tooltips, keyboard control and screen-reader tables.
5. Write `DASHBOARD.md` and `prompt.md`; run `python3 tools/package.py <name>` to build the tool files and the front matter.
6. Capture the covers with `python3 tools/shots.py <name>`, add the card to `index.html` and the row above, rebuild the site font (below), open a PR.
7. Publish the blog post at `style-<name>` on both sites.


## Tools

```bash
pip install playwright && python3 -m playwright install chromium
python3 tools/package.py anthropic                     # tokens.css, anthropic.tps, powerbi-theme.json, DASHBOARD.md front matter
python3 tools/shots.py anthropic                       # cover-en.png, cover-ko.png
python3 tools/shots.py anthropic --review /tmp/review  # also full pages at 1440, 1200, 1024 and 390px
python3 tools/shots.py anthropic --offline-fonts /tmp/fonts   # no CDN access: fonts from partial git clones
```

With `--offline-fonts`, font requests are answered from partial clones made on first use: jsDelivr GitHub fonts (Pretendard, when a style uses it) from their repositories, Google Fonts from [fontsource/font-files](https://github.com/fontsource/font-files), using the variable font when a link asks for an axis range such as optical size.

### Site font

The home page and the 404 page use VZ Sans, the same font as [Vizney Blocks](https://blocks.vizney.com): Spoqa Han Sans Neo cut down to the characters those two pages use and renamed, as the SIL Open Font License asks of a modified font ([OFL.txt](OFL.txt)). After changing the text of either page, rebuild it from the `Original/SpoqaHanSansNeo` folder of [spoqa-han-sans](https://github.com/spoqa/spoqa-han-sans):

```bash
pip install fonttools
python3 tools/font.py /path/to/spoqa-han-sans/Original/SpoqaHanSansNeo
```

Sample screens load their own fonts from Google Fonts and jsDelivr, as their specs say.


## Embedding a sample in a Ghost post

Paste into an HTML card and change the style, language and title. Always set `lang` in the URL rather than relying on the default:

```html
<figure class="kg-card kg-embed-card kg-width-wide">
  <iframe data-vizney-embed src="https://styles.vizney.com/anthropic/?lang=ko&amp;embed=1" title="Anthropic 스타일 대시보드" loading="lazy" style="display:block;width:100%;height:820px;border:1px solid #e6e6e6;border-radius:12px"></iframe>
  <figcaption><a href="https://styles.vizney.com/anthropic/?lang=ko" target="_blank" rel="noopener">전체 화면으로 보기 ↗</a></figcaption>
</figure>
<script src="https://styles.vizney.com/lib/embed-host.js" defer></script>
```

`lib/embed-host.js` resizes the iframe to the height the page reports through `lib/embed.js`, so the whole screen shows without an inner scrollbar. Without it, the iframe keeps its fixed height and scrolls.
