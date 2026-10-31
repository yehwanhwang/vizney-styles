---
name: Anthropic style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 1
tagline: Ivory, Editorial, Quiet
tagline_ko: 아이보리, 에디토리얼, 고요함
source: https://www.anthropic.com, https://claude.com
sample: https://styles.vizney.com/anthropic/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#faf9f5"
  card: "#f5f4ed"
  plot: "#ffffff"
  ink: "#141413"
  ink-2: "#30302e"
  body: "#3d3d3a"
  text-2: "#5e5d59"
  muted: "#73726c"
  mark: "#87867f"
  rule: "#d1cfc5"
  hair: "#e8e6dc"
  hair-2: "#dedcd1"
  subject-tint: "#f4e5d9"
  rival-best: "#e9e6dc"
  on-dark: "#faf9f5"
  on-dark-2: "#b0aea5"
  accent: "#d97757"
  good: "#4a7b00"
  bad: "#b0453b"
  focus: "#2c84db"
data:
  categorical: ["#eb6834", "#1baf7a", "#6150d3"]
  other: "#87867f"
  comparison: "#b0aea5"
  categorical_text: ["#b94a1c", "#008056", "#6150d3"]
  reference: ["#73726c", "#c2c0b6"]
  pair: {before: "#6150d3", after: "#4a7b00", track: "#dad9d1"}
  sequential: ["#7db2f0", "#4f90dc", "#2f74c2", "#1a5ba0", "#16416f"]
  diverging: ["#aa4518", "#dc6c40", "#eb9574", "#d1cfc5", "#7db2f0", "#4f90dc", "#1a64b0"]
  good: "#4a7b00"
  bad: "#b0453b"
typography:
  serif: { en: "Source Serif 4", ko: "Noto Serif KR" }
  sans: { en: "Inter", ko: "Noto Sans KR" }
  mono: "JetBrains Mono"
radius: {card: "16px", card-phone: "12px", window: "16px", button: "10px", button-sm: "8px", pill: "999px", tooltip: "6px", chip: "6px"}
spacing: {page: "32px", gap: "16px", section: "64px", card: "22px 24px 18px", card-head: "0 0 16px", card-foot: "14px 0 0", cell: "9px 10px", footer: "28px 32px 32px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: anthropic.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: orders.csv}
---

# Anthropic style — DASHBOARD.md

**Ivory, Editorial, Quiet** · 아이보리, 에디토리얼, 고요함

A dashboard design spec read from the public design of anthropic.com and claude.com. It takes the sites' measured tokens and the way Anthropic publishes data (the cost-and-score figures and benchmark tables of its model launches, the step charts, error bars, dumbbells and dot-unit surveys of its research posts) and turns them into one card and one chart grammar that a whole dashboard can follow. It then adds what a website spec leaves out and a dashboard needs: validated data colors, card anatomy, chart rules, number and date formats in English and Korean, density, filters, accessibility, and settings for Tableau, Power BI and the web. Put it in your project folder as `DASHBOARD.md` (with `tokens.css`) and point your agent to it, or hand it to whoever builds your dashboards. The live sample was built from it.

- Live sample: https://styles.vizney.com/anthropic/?lang=en (Korean `?lang=ko`; one region `&region=texas`)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/anthropic/DASHBOARD.md
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [anthropic.tps](anthropic.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [orders.csv](orders.csv) (the data behind the sample's Figure 2)
- Catalog: https://styles.vizney.com · Vizney Styles 01

Not an official Anthropic design, and not affiliated with or endorsed by Anthropic. A reference style read from the publicly visible design of anthropic.com and claude.com; it carries no logo, typeface or data of theirs. The sample's company, Vizney Logistics, and all its numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A warm ivory page that reads like a launch post with a research appendix, set in one grammar from top to bottom. It opens with the result in one bold sentence, a serif paragraph that names what drove it, and four key figures. Below that, numbered sections (`01 Overview`, `02 Operations`, `03 How it's built`) hold tiles of the same card: a warm gray card with a 16px radius, a mono figure label, a title that states the finding, a subtitle that names the measure, a one-line key, the chart or table, and a note that starts with `Note:`.

The chart forms are the ones Anthropic publishes: cost against score on a log axis, a benchmark table with the subject's column marked, a step line of the best result over many attempts, bars with 95% error bars, before-and-after dumbbells, and one dot per person for a survey. They share one look: the subject is orange everywhere, everyone else is gray, every filled mark has a 1px ink outline, gridlines are faint and axes are ink.

Clay, the brand accent, stays in the logo and marketing; it does not appear on the dashboard. Nothing has a shadow except the workbench window, the tooltip and the toast. The mood is calm and editorial: a report you would read to the end.

Measured on the sites (October 2026): header 84px; container 1400px with 32px margins; buttons 36px tall with a 10px radius; nav items as 28px pills; surfaces `#faf9f5` (gray-050) and `#f5f4ed` (gray-100); text `#141413`, `#3d3d3a`, `#5e5d59`; launch-chart markers r5 with a 1px ink stroke and 3px lines; research figures with a centered finding and a `Figure n` caption; tooltip an ink box with a 6px radius.


## Color Palette & Roles

Surfaces and text are the site's warm gray ladder.

| Token | Hex | Role |
|---|---|---|
| canvas | `#faf9f5` | page |
| card | `#f5f4ed` | every figure and table card; pills, chips, tertiary buttons |
| plot | `#ffffff` | the workbench window only |
| ink / ink-2 / body | `#141413` / `#30302e` / `#3d3d3a` | titles, axes, mark outlines, table header rules, selected controls, primary button, tooltip, footer / code / running text |
| text-2 | `#5e5d59` | subtitles, notes, ticks, figure labels (6.0:1 on card) |
| muted | `#73726c` | large or decorative text on canvas only (4.4:1 on card) |
| mark | `#87867f` | gray marks that are not text |
| rule / hair / hair-2 | `#d1cfc5` / `#e8e6dc` / `#dedcd1` | key-figure top rules, crosshair / dividers, pill borders / card gridlines, table row rules |
| subject-tint | `#f4e5d9` | the subject's column in a table; header text `#aa4518` (4.8:1) under a 3px orange bar |
| rival-best | `#e9e6dc` | a table cell where a rival is best |
| on-dark / on-dark-2 | `#faf9f5` / `#b0aea5` | text on ink / tooltip labels |
| accent | `#d97757` | clay: logos and marketing only. Never a data mark, never UI on a dashboard |
| good / bad | `#4a7b00` / `#b0453b` | favourable / unfavourable change, text only (4.6:1 / 5.1:1 on card) |
| focus | `#2c84db` | focus ring |

Rules:
- No cool grays and no white cards. White appears only inside the workbench window.
- Small text on a card uses text-2, never muted.
- Text takes a data color only through its text step (orange → `#b94a1c`, aqua → `#008056`) or when the color clears 4.5:1 on its surface (violet `#6150d3`, green `#4a7b00`, the survey's darkest steps `#aa4518` and `#1a64b0`).


## Data Colors

Anthropic's launch charts paint the subject orange, its previous version aqua and every other model gray, each marker outlined in ink. Its research figures add a violet–green pair for before and after, and orange and blue ramps for opinion scales. The palette keeps those roles. Every value passed an OKLab validator (color-vision-deficiency separation, normal-vision separation, contrast) on the card `#f5f4ed`, where every chart sits. Use them exactly; do not generate tints.

| Role | Mark | Label text | Use |
|---|---|---|---|
| Subject | `#eb6834` | `#b94a1c` | the company, the current year, the option the report is about |
| Own past | `#1baf7a` | `#008056` | the subject a year ago, when it sits among rivals |
| Third category | `#6150d3` | `#6150d3` | only when a third real category exists |
| References | `#73726c`, `#c2c0b6` | text-2 | rivals and benchmarks: gray on purpose |
| Other | `#87867f` | text-2 | the rest; also the "by hand" bar beside the subject's bar |
| Comparison line | `#b0aea5`, dashed 2px (6 on, 4 off) | ink | last year, when it is the only comparison |
| Before → after | `#6150d3` → `#4a7b00` on a `#dad9d1` track | the same colors | dumbbells |
| Opinion scale | `#aa4518` `#dc6c40` `#eb9574` · `#d1cfc5` · `#7db2f0` `#4f90dc` `#1a64b0` | each arm's darkest | dot units and stacked scales, diverging around a neutral |
| Sequential | `#7db2f0` `#4f90dc` `#2f74c2` `#1a5ba0` `#16416f` | — | magnitude, light → dark |
| Attempt marks | tried `#a2a09c` dots, rejected `#8e8c88` × | — | step charts of attempts |
| Bullet | track `#e6e3d9`, value subject orange, target ink, last year `#8e8c88` tick | — | a rate against a target in a table |
| Status | good `#4a7b00`, bad `#b0453b`, neutral `#87867f` | — | change text only |

Validation (from `tokens.json`, on the card):
- Orange, aqua and violet pass every check. The worst pair under color-vision deficiency is aqua↔orange at ΔE 9.2 (deutan); tritan 18.2; normal vision 27.6.
- Orange is 2.9:1 and aqua 2.74:1 on the card, so every filled mark (points, bars, dots) carries a 1px `#141413` outline, and every chart has labels or a table.
- The rival grays are neutral by design. With orange and aqua the all-pairs floor stays 9.2 (CVD) and 18.1 (normal). The light gray is 1.78:1 and always carries the outline.
- Comparison `#b0aea5` against orange: 13.0 / 18.6. At 2.2:1 it is always dashed and labeled at its end.
- Subject vs by-hand bars: 9.5 / 17.8, both ≥ 3:1. Orange line vs tried dots: 12.0 / 17.4; rejected attempts also differ by shape.
- Before/after pair: 28.7 / 32.9, both ≥ 4.5:1, so each labels its own values.
- Opinion-scale arms each pass the ordinal checks (monotone lightness, ΔL ≥ 0.06, light ends 2.10:1 and 2.15:1, one hue); the poles are 22.3 / 27.3 apart.
- Good and bad pass as text but do not separate for deutan vision (ΔE 2.8). Status is never color alone: the value keeps its sign and its comparison words.

Rules:
- At most three hues plus gray in one chart. A fourth real category folds into Other or becomes small multiples.
- Color follows the entity, not its rank: the subject is orange in every figure, every table and under every filter.
- Never put a yellow or amber series beside orange; they collapse under color-vision deficiency.
- Clay is not a data color.


## Typography Rules

| Role | English | Korean | Weights |
|---|---|---|---|
| Sans (everything else) | Inter | Noto Sans KR | 400, 500, 600, 700 |
| Serif (lede, section intros, build intro) | Source Serif 4 | Noto Serif KR | 400 |
| Mono (eyebrow, figure labels, section numbers, chips, file names, code) | JetBrains Mono | JetBrains Mono, then Noto Sans KR for Hangul | 400, 500 |

A screen loads only the fonts of its language. The Korean sans is Noto Sans KR because the brand's own Korean pages use it.

| Element | Size / weight | Notes |
|---|---|---|
| Headline | `clamp(28px, 3vw, 42px)` / 700, line-height 1.1, −0.022em | one sentence that states the result; `text-wrap: balance` |
| Key figure value | 42px / 600, −0.03em | units at 0.42em in text-2 (`96.2 %`, `$ 7.85`, `186 만 건`) |
| Section title | 26px / 700 | after a mono number (`01`) and under a 1px ink rule |
| Section intro, lede | 17px, 18px serif / 400 (Korean 17px, line-height 1.65) | text-2; never bold |
| Card title | 19px / 600, line-height 1.32 | the finding; `text-wrap: balance` |
| Card subtitle | 13px text-2 | the measure, the unit, the period |
| Figure label | mono 11px uppercase, 0.06em, text-2 | `FIGURE 2 · ORDERS`, `TABLE 1 · RIVALS` |
| Key | 12.5px / 500 ink | an 18 × 12 swatch drawn like the mark |
| Body · table · table header | 14px · 13.5px · 12.5px / 600 | values ink, `tabular-nums` |
| Note | 12.5px text-2, line-height 1.5 | starts with `Note:` / `주:` |
| Axis title / ticks / point labels | 12px · 11px text-2 · 10.5px ink | |
| Eyebrow | mono 11px uppercase, 0.1em | `OPERATIONS ANALYTICS · OCT 31, 2026` |
| Code | mono 12.5px, line-height 1.62 | |

Headings are sans and heavy; the serif is regular and only for prose. Korean text breaks between words (`word-break: keep-all`), and a number stays on the same line as the particle after it (`97%에`, `54건에서`).


## Numbers, Dates & Units

| | English | Korean |
|---|---|---|
| Money per order | `$7.85` | `7.85달러` |
| Large money | `$4.2M`, `$1.3B` | `420만 달러`, `13억 달러` |
| Money axis | `$4 $6 $10 $15 $25` | `4 6 10 15 25`, the unit in the axis title |
| Counts | `1.86M` (key figure), `320K` (table) | `186만 건`, `32만` |
| Rates | `96.2%`; two decimals when the spread is tiny (`99.58%`); whole numbers for survey shares (`60%`) | the same |
| Points | `+1.6 pts` | `+1.6%p` |
| Per thousand | `38 per 1,000 orders` | `주문 1,000건당 38건` |
| Hours | `10.1 h` | `10.1시간` |
| Change | `+8.4% vs Oct 2025` | `+8.4% 전년 동월 대비` |
| Dates | `Oct 31, 2026`; period `October 2026`; ticks `Nov … Oct` | `2026년 10월 31일`; `2026년 10월`; `11월 … 10월` |

- Money is in the company's own currency; the sample's company is American, so US dollars to the cent.
- Signs use the true minus (`−`, U+2212). One decimal for change.
- The change color follows whether the move is good for that metric: cost per order `−6.9%` is green.
- Units and suffixes are smaller than the digits.
- `—` marks a value that does not exist (a rival without that service); the reason is in a numbered note. Footnote markers are superscripts (`CSAT¹`) linked to the notes.
- Scale qualifiers go in the axis title: `Cost per order ($, log scale)`.
- The current month's tick is ink, the others text-2.


## Layout Principles

One column on the canvas, at most 1400px wide, 32px side padding (24px up to 1359px, 16px below 640px), a 16px gap between cards and 64px between sections. No sidebar, no app chrome, no logo.

1. **Header** (84px): company name (16px / 700) and report name (13px text-2). On the right: a period pill, the EN/KO toggle, a tertiary `Read in PDF` and the one primary button, `Copy as markdown`.
2. **Filter row** between two hairlines: 28px pills on the left, the basis (`As of October 31, 2026 · vs October 2025`) on the right. The pills scope every card, and the URL keeps the choice (`?region=texas`).
3. **Headline block**, 7 of 12 columns: mono eyebrow → headline → serif lede that names the drivers → a section nav (`01 Overview  02 Operations  03 How it's built`). The four key figures sit on the right in 5 columns, 2 × 2, bottom-aligned with the nav.
4. **Sections.** Each opens with a 1px ink rule, a mono number, a 26px title and a one-line serif intro, then rows of cards on a 12-column grid. Cards in one row share a subgrid, so their heads, bodies and notes line up and side-by-side charts start and end on the same lines.
   - `01 Overview`: Figure 1 service tiers (7) · Table 1 rivals (5); Figure 2 orders (5) · Table 2 hubs (7).
   - `02 Operations`: Figure 3 routing changes (8) · Figure 4 dispatch (4), one y scale; Figure 5 suggested routes (7) · Figure 6 driver survey (5).
5. **`03 How it's built`**: a serif paragraph with two buttons (`Read DASHBOARD.md`, `Get one for your company ↗`), three numbered steps, then the workbench window and a caption.
6. **Notes + related reports**, 7 / 5, in the same card.
7. **Ink footer**, full bleed.

At most seven views on one screen: the key figures and four cards in Overview, four cards in Operations. Every view is a standard form an agent or a BI tool can rebuild from a template. A chart's body fills its card, so a chart beside a longer table grows to the table's height. Density: at 1440 × 900 the header, filter row, headline and the four key figures are on the first screen, with the top of Overview below them. Reading order follows the list; never lead with a chart.


## Component Stylings

- **Card**: `#f5f4ed`, 16px radius, 22px 24px 18px padding, no border, no shadow. Three parts on a subgrid: head (figure label row with any tabs on the right → title → subtitle → keys, 16px below), body (the chart or table), foot (`Note:` 12.5px text-2, 14px above). Never a card inside a card.
- **Buttons** (measured): 36px tall, 10px radius, 14px / 500, icon after the label. Primary: ink fill, ivory text, hover `body`. Secondary: hair fill, hair-2 border, ink-2 text. Tertiary: card fill, hair border, body text. Small: 30px, 8px radius, 13px. Icon-only: 30 × 30. Hover changes the background only.
- **Pills**: 28px, 999px radius, 13px, card fill, hair border; selected is ink with ivory text.
- **Segmented control** (figure tabs, the EN/KO toggle, `Without a spec / With DASHBOARD.md`): a canvas track with a hair-2 border, 24px segments, 12px / 500; the selected segment is ink. `role="tablist"`, arrow keys move.
- **Key figure**: 1px `#d1cfc5` rule on top, 14px padding; label 14px / 500 ink → value → change line (13px text-2, the change in 600 status color, then `vs Oct 2025`). Two text sizes besides the value.
- **Keys**: a row above the chart, each an 18 × 12 swatch drawn like its mark (an outlined dot, a line, a dashed line, ×, a bar, a tick, an error bar) and a 12.5px / 500 label. In Figure 1 the keys are buttons that hide a series (`aria-pressed`, 0.4 opacity when off; the last visible series stays).
- **Table**: 13.5px, cells 9px 10px, a 1px ink rule under the header, hair-2 rules between rows, no vertical rules, no zebra. Row headers: category 600 ink over the metric 12px text-2, footnote superscripts. The subject's column: `#f4e5d9` with a 3px orange bar on its header and header text `#aa4518`. The best value per row is bold; when a rival is best its cell is `#e9e6dc` (lower is better for speed and cost). A reference column (the subject a year ago) sits apart in text-2 with a two-line header (`2025` / `For reference`).
- **Bullet in a table**: 150px (112px from 1359px, 88px on phones), an 8px track from 90%, the value in orange with an ink outline, the target as a 1.5px ink line, last year as a gray tick; the value follows as text.
- **Workbench window**: white, 16px radius, 1px hair border, shadow `0 1px 2px rgba(20,20,19,.04), 0 12px 32px rgba(20,20,19,.07)`. Three panes: a 232px package list (`#fbfaf7`, file names in mono 11.5px with a one-line description), the figure (a segmented `Without a spec / With DASHBOARD.md`, a mono chip with the filter value, title, plot, note, then **Checks · DASHBOARD.md** with icons and `All 6 passed` or `0 of 6 passed`), and the code (tabs `Prompt · plan.md · figure-2.js · Tableau · Power BI`, an icon copy button and a primary `Run again`, line-numbered code, a status bar `● Built from DASHBOARD.md · 24 lines`). Syntax colors: comment `#6b6a64`, string `#3f7d1a`, number `#1a64b0`, keyword `#ad502d`, function `#6150d3`, property `#30302e` 500; hex values show a small swatch. Settings show as two columns (name 14ch, value).
- **Notes**: a numbered list 13px text-2 in a card, then sources and the update time.
- **Related reports**: date 12.5px text-2 over a 15px ink title, hair-2 rules between items, an arrow on the right.
- **Tooltip**: ink fill, ivory text, 6px radius, shadow `0 4px 16px rgba(20,20,19,.14)`; a 12px title in `#b0aea5`, then rows of key (dot, or line for line series, dashed for the comparison), value 600, label. It takes the first side that fits inside the card: above, left, right, below.
- **Toast**: the same ink box, bottom center, 2.2s.
- **Footer**: ink, full bleed, 12.5px `#b0aea5`; the catalog line in ivory.


## Charts

- **Choose by the question.**
  - Quality against cost across options → connected scatter on a log cost axis, one line per company, three measures as tabs (Figure 1).
  - The subject against rivals on many measures → a table with the subject's column marked (Table 1).
  - A trend against last year → a line with last year dashed gray and both line ends labeled (Figure 2).
  - Many entities against one target → a table with a bullet per row, sorted by the value (Table 2).
  - Progress over many attempts → a step line of the best result so far over every attempt (dots without gain, × rejected), the target as a dotted line and `↓ Better` in the corner (Figure 3).
  - Two groups with uncertainty → two bars with 95% error bars, on the same scale as the chart beside them (Figure 4).
  - Before and after per category → a dumbbell with a difference column (Figure 5).
  - An opinion scale → dot units, one dot per person, grouped by answer with brackets and counts, the two sides diverging from a center rule (Figure 6).
- **Titles.** The card title is the finding (`Orders grew on last year in 11 of 12 months`), recomputed when the filter changes. The subtitle names the measure and period; the note explains the method, the sample and the uncertainty.
- **Marks.** Connected-scatter lines 3px with r5 points; other lines 2.5px; dumbbell dots r7 on an 8px round track; dot units up to 20px at 1.22 × pitch; bars up to 72px wide. Every filled mark has a 1px `#141413` outline.
- **Axes.** Ink axis lines and baseline; gridlines `#dedcd1` (rows only); ticks 11px text-2, axis titles 12px. Four or five nice ticks. Charts side by side share one y scale and one baseline, and each keeps its tick labels.
- **Labels.** The subject's points carry their names (10.5px) with a card-colored halo. Line ends carry `Name value` instead of a legend. The latest best result gets a star and its value in the subject's text color.
- **Keys** only where labels cannot do the job, as a one-line row in the card head.
- **One axis.** Never a dual axis. A synchronized second axis that only layers marks of the same measure (a Tableau dumbbell) is fine.
- **Never:** pie, donut, 3D, gradients, area fills, rainbow categories, smoothing, clay series, a fourth hue.
- Every chart has a hover tooltip, keyboard control and a screen-reader table.


## Depth & Elevation

Flat. Cards are set apart by color, not by lines or shadows, and never lift on hover. Shadows exist only on the workbench window, the tooltip and the toast.


## Interaction & Motion

- **Filter**: one row of pills scopes everything; changing it rewrites the headline, lede, key figures, card titles and notes, and redraws every chart. The URL keeps the region.
- **Figure tabs** switch the measure of Figure 1 and rewrite its title and note. **Key buttons** hide a series.
- **Hover** shows the tooltip and an ink ring or crosshair on the nearest mark; touch taps pick and a tap elsewhere clears.
- **Keyboard**: every chart is focusable; arrow keys step (up and down switch series in Figure 1), Home and End jump, Esc clears, and a live region reads the value. Tabs, segments and filter pills move with arrow keys.
- **Workbench**: the first time it scrolls into view, the code types itself (55ms a line, 380ms between steps) and each step draws its layer of the figure (frame → comparison line → subject line → end labels → title and note) and ticks its checks. Hovering a line of code spotlights the layer it draws; hovering the chart highlights its code. `Without a spec` shows a typical first draft and fails all six checks. Changing the filter rewrites the `region` value and flashes that line. `Run again` replays; the copy button copies the current tab.
- `Copy as markdown` copies the whole report as Markdown with a toast; `Read in PDF` prints.
- Motion: lines draw in 0.7s, labels fade in 0.3s, `cubic-bezier(.165,.84,.44,1)`; buttons change background in 0.22s. `prefers-reduced-motion` turns all motion off and shows the workbench finished.


## Accessibility

- Text ≥ 4.5:1 on its surface: on the card text-2 6.0:1, good 4.6:1, bad 5.1:1, orange text 4.7:1, aqua text 4.5:1, violet 5.3:1; the subject's header `#aa4518` 4.8:1 on its tint; code token colors ≥ 4.5:1 on white.
- Marks below 3:1 (orange 2.9:1, aqua 2.74:1, light gray 1.78:1, comparison 2.2:1, tried 2.54:1) always have a second cue: an ink outline, a dash, a label or a table.
- Identity is never color alone: names on points and line ends, dashes for comparisons, shapes for rejected attempts, signs on every change.
- Focus ring `#2c84db`, 2px, 2px offset. Tab order: header → filter → sections in reading order.
- Real tables with `scope`; every chart has a hidden data table and an `aria-label` that states what it shows.


## Responsive Behavior

- ≥ 1360: as laid out above.
- 1200–1359: 24px padding, 14px gap; table cells 9px 8px; the bullet is 112px; the workbench moves its file list above the figure and the code.
- 1024–1199: the same rows; Table 1 drops the reference column and Table 2 drops the note column; code lines wrap.
- 900–1023: cards stack one per row (the dropped columns come back); the headline block stacks and the four key figures run in one row; the workbench is one column.
- 640–899: key figures 2 × 2; the report name and `Read in PDF` leave the header; steps stack; code up to 440px tall.
- < 640: 16px padding, 12px card radius; the period pill and `Copy as markdown` leave the header; tables drop the reference, note and orders columns and let names wrap; the dumbbell puts names above each row and keeps the difference column; dot units stack the two sides; code lines wrap.
- Embedded in a post (`?embed=1`): the footer hides and the page reports its height to the host page.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` (or copy the `colors` block from the front matter) and these fonts:
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+KR:wght@400;500;600;700&family=Noto+Serif+KR:wght@400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;1,8..60,400&display=swap`

**Tableau.** Paste the `<color-palette>` elements of `anthropic.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette runs orange, aqua, violet, the two rival grays, Other and the comparison gray; assign the subject first.
- Dashboard background `#faf9f5`; each sheet in a container with background `#f5f4ed` and 22/24px inner padding (Tableau has no radius). Worksheet shading `#f5f4ed`.
- The card head: a text object with the figure label (Tableau Book 9, `#5e5d59`, uppercase), the finding as the sheet title (bold, 13–14pt, ink) and the measure as a subtitle line; the method in the caption, starting with `Note:`.
- Marks: Color → Effects → Border `#141413` on every filled mark; line size 3 for the cost scatter, 2.5 elsewhere; Edit Axis → Logarithmic for cost.
- Gridlines `#dedcd1` (rows only), zero line and axis rulers ink, ticks Tableau Book 9 in `#5e5d59`.
- Step chart: a step line of a running MIN over an attempt index, a circle layer of every attempt, a dotted reference line for the target. Error bars: a reference band or a Gantt bar of the interval. Dumbbell: a synchronized dual axis of the same measure (line + circles), the difference as a text column. Bullet: a bar with a reference line at the target and a reference line per cell for last year.
- Comparison table: a text table with row dividers `#dedcd1`, a header divider in ink, the subject's column shaded `#f4e5d9`, a calculation that bolds the best value and shades a rival's best `#e9e6dc`.
- Formats `$#,##0.00`, `0.0%`, `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0.00"달러"` and `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Inter and Source Serif 4 are installed on every viewing machine and on the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json`. It sets the data colors (the three hues in order, then the two rival grays, then Other), the ivory page, card-colored visuals without borders, axis and gridline colors and text classes. Install Inter on authoring and viewing machines or accept Segoe UI.
- Title each visual with the finding; put the measure in the subtitle and the method in a text box starting with `Note:`.
- Markers on; error bars from the analytics pane for intervals; a dumbbell as a line chart with markers on two series and the line color `#dad9d1`; legends off where data labels on the last point can name the series.
- Key figures as cards with a top border `#d1cfc5` and no background; change measures with conditional formatting in `#4a7b00` / `#b0453b` only.

**Chart libraries (D3, Observable Plot, Vega-Lite, matplotlib, Datawrapper).** Subject `#eb6834` (labels `#b94a1c`), own past `#1baf7a` (`#008056`), rivals `#73726c` / `#c2c0b6`, `stroke: #141413` on every filled mark, comparison `#b0aea5` dashed `6 4`, gridlines `#dedcd1`, ticks `#5e5d59` at 11px, plot background `#f5f4ed`. The sample's Figure 2 in five forms is in the workbench of the live sample; `orders.csv` is its data.


## Do's and Don'ts

- Do start with the result in one sentence, the drivers in a serif lede, and four key figures. Don't lead with a chart or a dozen KPI tiles.
- Do put every view on the same card with the same head and foot. Don't mix frames, mats and panels from different publications.
- Do choose the form by the question (cost scatter, marked table, step line, error bars, dumbbell, dot units). Don't fall back to the same bar chart in every card.
- Do paint the subject orange and everyone else gray, with ink outlines on filled marks. Don't use clay, yellow or a fourth hue on data.
- Do title each card with its finding and explain the method in the note. Don't title a chart with its measure alone.
- Do give side-by-side charts one scale. Don't use a dual axis.
- Do rule tables lightly and tint only the subject's column. Don't zebra-stripe or tint whole rows.
- Do label points and line ends. Don't keep a legend that labels could replace.
- Do keep headings sans and heavy and the serif regular. Don't use a bold serif.
- Do keep seven views or fewer on one screen. Don't add a card only to show a token.
- Don't put a logo, a wordmark or a photo anywhere.


## Agent Prompt Guide

Put this file in the project folder as `DASHBOARD.md`, with `tokens.css` beside it, and add one line to your agent's instructions file (for example `CLAUDE.md`): `Build every dashboard to DASHBOARD.md and run its checks before you finish.` Then prompt, for example:

```
Read DASHBOARD.md and follow it exactly. Build our monthly operations dashboard as one self-contained HTML file
with fictional data, in English and Korean (?lang=en|ko, English by default).
Top: header with the period pill, EN/KO toggle, Read in PDF and Copy as markdown; one filter row of pills that scopes every card.
Then a mono eyebrow, a headline that states this month's result, a serif lede with the drivers, a section nav,
and four key figures 2 × 2 with changes vs last year.
01 Overview: cost against satisfaction by service tier (tabs for three measures) beside a rivals table; orders against
last year beside a hubs table with bullets against the SLA.
02 Operations: a step chart of routing changes beside dispatch bars with 95% error bars on the same scale; a dumbbell
of on-time rate before and after per order type beside a dot-unit driver survey.
Every view on the same card: figure label, finding title, subtitle, keys, chart, "Note:". At most seven views per screen.
Use only the values in Data Colors, the formats in Numbers, Dates & Units and the components in Component Stylings.
Every chart needs a hover tooltip, keyboard control and a screen-reader table.
```

Before it is done, the agent checks:
- [ ] The headline states the result; the lede names the drivers; key figures carry signed changes colored by good or bad.
- [ ] Every view sits on the same card; every card title states a finding; every note starts with `Note:` and explains the method.
- [ ] The subject is `#eb6834` everywhere; rivals gray; comparison dashed `#b0aea5`; every filled mark outlined in ink; no clay, yellow or fourth hue on data.
- [ ] Points and line ends are labeled; keys only where labels cannot work.
- [ ] Side-by-side charts share a scale; no dual axis, pie or donut.
- [ ] Tables use light rules and the tinted subject column; the best value per row is bold.
- [ ] Text ≥ 4.5:1 on its surface; marks below 3:1 have a second cue.
- [ ] Every chart has a tooltip, keyboard control and a data table; the filter changes every card; at most seven views per screen; nothing breaks at 390px.
