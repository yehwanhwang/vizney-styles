# Vizney Styles

Dashboard design specs that AI coding agents, Tableau and Power BI can follow. Each entry in the catalog is a company's look, read from its public website and worked out for dashboards: `DASHBOARD.md`, a live sample screen with fictional data, validated data colors, and the tool files. The same package is made privately for your own company.

Served at **https://styles.vizney.com** (GitHub Pages, `main` branch). Everything pushed to `main` is published immediately, so keep work in progress off `main`. Every page opens in English; add `?lang=ko` for Korean.

Vizney Styles is a line of [Vizney](https://www.vizney.com), a BI consulting studio in Seoul; the brand is Vizney, and each style carries the series line `VIZNEY STYLES · 01`. Install a style with `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- <style>` or `npx @vizney/styles@latest add <style>` ([npm](https://www.npmjs.com/package/@vizney/styles)).


## Catalog

| No. | Style | Feel | Sample | Spec | Files | Post |
|---|---|---|---|---|---|---|
| 01 | Anthropic | Ivory, Editorial, Quiet | [Live sample](https://styles.vizney.com/anthropic/) · the monthly operations report of Vizney Logistics (fictional), drawn in one card and chart grammar from the figures Anthropic publishes in launches and research posts, with a build workbench | [DASHBOARD.md](anthropic/DASHBOARD.md) | [anthropic/](anthropic/) | [KO](https://kr.vizney.com/style-anthropic/) · [EN](https://www.vizney.com/style-anthropic/) |
| 02 | Notion | Monochrome, Blocks, Tidy | [Live sample](https://styles.vizney.com/notion/) · the monthly store operations report of Vizney Coffee (fictional), built from the blocks of a Notion page and its database views (chart, table and board, calendar, tags and status pills) in one card and chart grammar, with a build workbench | [DASHBOARD.md](notion/DASHBOARD.md) | [notion/](notion/) | [KO](https://kr.vizney.com/style-notion/) · [EN](https://www.vizney.com/style-notion/) |
| 03 | Netflix | Dark, Cinematic, Bold | [Live sample](https://styles.vizney.com/netflix/) · the weekly ticket sales report of Vizney Live (fictional), built from the parts Netflix ranks and shows progress with instead of charts (the billboard, the Top 10 row of outlined numerals, weeks in the Top 10, the episode list with progress bars, the Top 10 table, the hover card, the FAQ accordion) in one card and chart grammar on a dark page, with a build workbench | [DASHBOARD.md](netflix/DASHBOARD.md) | [netflix/](netflix/) | [KO](https://kr.vizney.com/style-netflix/) · [EN](https://www.vizney.com/style-netflix/) |
| 04 | Costco | Warehouse, Receipt, No-Frills | [Live sample](https://styles.vizney.com/costco/) · the weekly warehouse report of Vizney Wholesale (fictional), built from the way Costco shows its numbers in the real world (the warehouse price sign as key figures; the register receipt as the department table, with barcode bars and transactions by hour where its barcode sits; the Warehouse Savings coupon book; the sales-release sentence), with a warehouse board against plan and the holiday buy stacked as pallet racks, under costco.com's blue bands and charcoal ruled sections, with a build workbench | [DASHBOARD.md](costco/DASHBOARD.md) | [costco/](costco/) | [KO](https://kr.vizney.com/style-costco/) · [EN](https://www.vizney.com/style-costco/) |
| 05 | Singapore Airlines | Premium, Boarding Pass, Courteous | [Live sample](https://styles.vizney.com/singapore-airlines/) · the monthly operating statistics of Vizney Air (fictional), built from the way Singapore Airlines shows its numbers in the real world (the boarding pass as key figures, with passengers by day where its barcode sits and the load factor on the stub; the seat map as cabin load; the monthly release and its operating statistics table), with a route map of where capacity went, routes against breakeven and the hub's departures by hour, under singaporeair.com's navy booking tabs and orange hairlines, with a build workbench | [DASHBOARD.md](singapore-airlines/DASHBOARD.md) | [singapore-airlines/](singapore-airlines/) | [KO](https://kr.vizney.com/style-singapore-airlines/) · [EN](https://www.vizney.com/style-singapore-airlines/) |
| 06 | Shell | Energy, Forecourt, Confident | [Live sample](https://styles.vizney.com/shell/) · the weekly mobility report of Vizney Energy (fictional), built from the way Shell shows its numbers on the forecourt and in its results (the price sign as a pillar of key figures, the results deck's compare boxes, key price markers and earnings bridge, the annual report's tables and `[A]` footnotes), with ruled exception lists for sites, tanks and charge points and a schematic corridor operations map whose sites are small price-sign pins, zooming into one site's 2-mile street with competitors' prices and what to do, under a canopy band with the red bar and yellow rules, with a build workbench | [DASHBOARD.md](shell/DASHBOARD.md) | [shell/](shell/) | [KO](https://kr.vizney.com/style-shell/) · [EN](https://www.vizney.com/style-shell/) |
| 07 | F1 | Racing, Telemetry, Precise | [Live sample](https://styles.vizney.com/f1/) · the race debrief of Vizney Racing (fictional), built from the way a race shows its numbers on the timing screens (the onboard display as key figures, with shift lights for the last 15 laps against the winner, dials with target and plan ticks and the finishing position as the gear readout; the circuit map coloured mini-sector by mini-sector; the timing tower with tyre stints), with the gap to the winner lap by lap, a speed trace with the running gap, pit stops against target and season points against plan, on a black page in purple, green and yellow timing colours, with a build workbench | [DASHBOARD.md](f1/DASHBOARD.md) | [f1/](f1/) | [KO](https://kr.vizney.com/style-f1/) · [EN](https://www.vizney.com/style-f1/) |

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
  skill/SKILL.md      the dashboard-style agent skill (build, restyle, review), generated from tools/skill.md
  anthropic-dashboard-style.zip
                      DASHBOARD.md and .claude/skills/dashboard-style/ with the tool files, to unzip in a project root
  orders.csv          sample data for the figure the sample's workbench draws (optional per style)
  cover-en.png        1440×810 at 2×: home card, post feature image, link previews
  cover-ko.png
```

### DASHBOARD.md

The file follows the `DESIGN.md` convention (front matter tokens, then prose sections an agent can read) and adds the sections a dashboard needs. Consumers that know `DESIGN.md` can ignore the extra sections; agents use all of them.

1. Visual Theme & Atmosphere
2. Color Palette & Roles
3. Data Colors — categorical, comparison, sequential, diverging and status colors, each validated for color-vision deficiency, normal-vision separation and contrast
4. Typography Rules — the sans, a serif where the brand uses one, and a mono, with Korean counterparts
5. Numbers, Dates & Units — English and Korean formats, change notation, rounding
6. Layout Principles — grid, reading order, density
7. Component Stylings — the card, key figures, buttons and filters, tables, tooltips, keys, and the brand's own parts (Notion's tags, status pills and board, for example)
8. Charts — chart choice, one axis, marks, labels, forbidden forms
9. Depth & Elevation
10. Interaction & Motion
11. Accessibility
12. Responsive Behavior
13. Tool Mapping — web, Tableau, Power BI, chart tools
14. Do's and Don'ts
15. Agent Prompt Guide

### Using it

- **Install in a project** (run in the project folder):

  ```bash
  npx @vizney/styles@latest add anthropic                      # Node 18+
  curl -fsSL https://styles.vizney.com/install.sh | sh -s -- anthropic   # macOS, Linux
  ```

  It writes `DASHBOARD.md` to the project root and the `dashboard-style` skill with `tokens.css`, `tokens.json`, the `.tps`, `powerbi-theme.json` and `prompt.md` to `.claude/skills/dashboard-style/`, and touches nothing else (`FORCE=1` replaces an earlier install). Without a terminal, unzip `<style>-dashboard-style.zip` from the style's page in the project root.
- **AI coding agents:** agents that read skills load `dashboard-style` whenever a task makes, changes or reviews a dashboard or chart. Others: start the prompt with `Read DASHBOARD.md and follow it exactly.`; `prompt.md` has tested prompts.
- **Tableau:** paste the `<color-palette>` elements of the `.tps` file into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The Tool Mapping section lists the formatting settings.
- **Power BI:** View → Themes → Browse for themes → `powerbi-theme.json`.


### npm CLI

`npm/` holds the `@vizney/styles` package (command `vizney-styles`), which places the same files as `install.sh`:

```bash
npx @vizney/styles@latest add anthropic     # --force to replace, --dir <path> for another folder
npx @vizney/styles@latest list              # the styles in catalog.json
```

It reads the files from this repository's `main` branch, so a new or changed style needs no new npm release; `tools/package.py` keeps `catalog.json` up to date. Release the CLI itself by raising `version` in `npm/package.json` and running the **Publish npm package** workflow (Actions → Run workflow, or push a tag `npm-v<version>`). The `@vizney` scope is the `vizney` npm account. npm stages a release before it goes live: approve it on npmjs.com under **Staged Packages** (2FA) after the workflow finishes. The first release needs the repository secret `NPM_TOKEN` (a granular access token that can publish to the `@vizney` scope); after it, set up Trusted Publishing for `@vizney/styles` on npmjs.com (GitHub Actions, repository `yehwanhwang/vizney-styles`, workflow `npm-publish.yml`) and delete the token. The workflow tests the CLI against the live catalog, skips a version that is already published and publishes with provenance.


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
python3 tools/package.py anthropic                     # tokens.css, anthropic.tps, powerbi-theme.json, DASHBOARD.md front matter, skill/SKILL.md, the zip
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
