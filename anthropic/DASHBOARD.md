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
  card-2: "#f0eee6"
  card-3: "#ebe9e0"
  mat: "#e7e7db"
  panel: "#fbf9f5"
  plot: "#ffffff"
  cloud: "#c5d3e0"
  ink: "#141413"
  ink-2: "#30302e"
  body: "#3d3d3a"
  text-2: "#5e5d59"
  muted: "#73726c"
  mark: "#87867f"
  grid: "#d1cfc5"
  hair: "#e8e6dc"
  hair-2: "#dedcd1"
  on-dark: "#faf9f5"
  on-dark-2: "#b0aea5"
  accent: "#d97757"
  accent-deep: "#c6613f"
  peach: "#ebc9b7"
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
radius: {figure: "0", mat: "8px", panel: "16px", card: "16px", window: "12px", button: "10px", button-sm: "8px", pill: "999px", tooltip: "6px", chip: "6px"}
spacing: {page: "32px", gap: "16px", row: "44px", figure: "16px 18px", mat: "26px 28px 28px", panel: "22px 24px 18px", cell: "10px 12px", footer: "28px 32px 32px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: anthropic.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: orders.csv}
---

# Anthropic style — DASHBOARD.md

**Ivory, Editorial, Quiet** · 아이보리, 에디토리얼, 고요함

A dashboard design spec read from the public design of anthropic.com and claude.com. It takes the sites' measured tokens and, above all, the way Anthropic publishes data: the tabbed cost-and-score figures and benchmark tables of its model launches, the matted figures of its research posts (step charts, error bars, dumbbells, dot-unit survey charts), the card carousels of its research index and the code workbench of its product pages. It then adds what a website spec leaves out and a dashboard needs: validated data colors, component anatomy, chart rules, number and date formats in English and Korean, density, filters, accessibility, and settings for Tableau, Power BI and the web. Put it in your repository root as `DASHBOARD.md` (with `tokens.css`) or hand it to whoever builds your dashboards. The live sample was built from it.

- Live sample: https://styles.vizney.com/anthropic/?lang=en (Korean `?lang=ko`; one region `&region=busan`)
- Raw file for your repository: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/anthropic/DASHBOARD.md
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [anthropic.tps](anthropic.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [orders.csv](orders.csv) (the data behind the sample's Figure 5)
- Catalog: https://styles.vizney.com · Vizney Styles 01

Not an official Anthropic design, and not affiliated with or endorsed by Anthropic. A reference style read from the publicly visible design of anthropic.com and claude.com; it carries no logo, typeface or data of theirs, and the sample's company and numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A warm ivory page that reads like a launch post with a research appendix. The screen opens with the result in one bold sentence, a serif paragraph that says what drove it, and four key figures. Below it, every figure is one Anthropic already publishes:

1. **The launch figure.** Text tabs above a paper panel framed in 1px ink. A legend made of toggle buttons. Lines with ink-outlined markers, the subject's points labeled with their names, a log cost axis, and a centered caption under the frame.
2. **The benchmark table.** Thin ink rules on every cell. The subject column outlined in 3px clay. The best value per row on peach, or on gray when a rival wins. A detached "For reference" column for the subject's own past.
3. **The research mat.** A gray-green mat with a centered bold title that states the finding, a soft panel inside it, and a caption outside that starts with a mono `FIGURE 2` label and a bold lead sentence.
4. **The card carousel.** Hairline-topped cards with a small ink glyph, a 21px title, a count line and one sentence, paged with `← 01 / 02 →`.
5. **The workbench.** A white window on a pale blue mat: a file list, a figure, and code that draws it.

Clay stays a UI accent: it outlines the subject column of the table. On data, the subject is the orange that the brand's own charts give to the model being launched. Everyone else is gray. Nothing has a shadow except the workbench window, the tooltip and the toast. The mood is calm and editorial: a report you would read to the end.

Measured on the sites (October 2026): header 84px; container 1400px with 32px margins; buttons 36px tall with a 10px radius; nav items as 28px pills; launch figure panel `#faf9f5` with a 1px `#141413` border and no radius, 16px padding, title 17px/600, subtitle 15px `#5e5d59`, legend 13px/600 toggles at 0.4 opacity when off, markers r5 with a 1px ink stroke, 3px lines, ticks 11px, axis titles 12px, caption 14px centered; figure tabs 15px/600, selected ink, others gray; benchmark table 14px, cells 10×12px, 1px ink rules, subject column outlined in 3px `#d97757`, wins on `#ebc9b7`, rival wins on `#d1cfc5`; research mat `#e7e7db` (8px radius) around a `#fbf9f5` panel (16px radius); tooltip an ink box with a 6px radius.


## Color Palette & Roles

Surfaces and text are the site's warm gray ladder. Clay is the one brand accent, and it stays in the interface.

| Token | Hex | Role |
|---|---|---|
| canvas | `#faf9f5` | page; also the paper inside a launch figure |
| card / card-2 / card-3 | `#f5f4ed` / `#f0eee6` / `#ebe9e0` | pills, tertiary buttons, chips / the table's "For reference" column / related-report cards |
| mat / panel | `#e7e7db` / `#fbf9f5` | research figure mat / the panel inside it |
| plot / cloud | `#ffffff` / `#c5d3e0` | the workbench window / the mat behind it. The only pure white on the page is inside that window |
| ink / ink-2 / body | `#141413` / `#30302e` / `#3d3d3a` | titles, figure frames, axes, table rules, primary button, footer, tooltip / code, secondary button text / running text |
| text-2 | `#5e5d59` | subtitles, captions, ticks, notes (6.3:1 on canvas) |
| muted | `#73726c` | the smallest text: section numbers, unselected tabs, mono labels (4.6:1) |
| mark | `#87867f` | gray marks that are not text |
| grid / hair / hair-2 | `#d1cfc5` / `#e8e6dc` / `#dedcd1` | gridlines in framed figures, rival-win cells / dividers, pill borders, the selected filter pill / card top rules, button borders |
| on-dark / on-dark-2 | `#faf9f5` / `#b0aea5` | text on ink / secondary text on ink, tooltip labels |
| accent / accent-deep | `#d97757` / `#c6613f` | clay: the 3px outline of the subject column / clay text if ever needed |
| peach | `#ebc9b7` | table cells where the subject wins |
| good / bad | `#4a7b00` / `#b0453b` | favourable / unfavourable change, text only (4.8:1 / 5.3:1) |
| focus | `#2c84db` | focus ring |

Rules:
- No cool grays, no pure-white cards.
- Clay never colors a data mark. The subject's data color is orange `#eb6834`, a different color with a different job.
- Text takes a data color only through its text step (orange → `#b94a1c`, aqua → `#008056`) or when the color itself clears 4.5:1 (violet `#6150d3`, green `#4a7b00`).


## Data Colors

Anthropic's launch charts paint the subject orange, its previous version aqua and every other model gray, with an ink outline on each marker. Its research figures add a violet–green pair for before and after, and clay and blue ramps for opinion scales. The palette keeps those roles. Every value below passed an OKLab validator (color-vision-deficiency separation, normal-vision separation, contrast) on the surface it is drawn on. Use them exactly; do not generate tints.

| Role | Mark | Label text | Use |
|---|---|---|---|
| Subject | `#eb6834` | `#b94a1c` | the company, the current year, the option the report is about |
| Own past | `#1baf7a` | `#008056` | the subject a year ago, when it sits among rivals |
| Third category | `#6150d3` | `#6150d3` | only when a third real category exists |
| References | `#73726c`, `#c2c0b6` | text-2 | rivals and benchmarks: gray on purpose, markers outlined in 1px ink |
| Other | `#87867f` | text-2 | the rest; also the "by hand" bar beside the subject's bar |
| Comparison line | `#b0aea5`, dashed 2px (6 on, 4 off) | ink | last year, when it is the only comparison |
| Before → after | `#6150d3` → `#4a7b00` on a `#dad9d1` track | the same colors | dumbbells |
| Opinion scale | `#aa4518` `#dc6c40` `#eb9574` · `#d1cfc5` · `#7db2f0` `#4f90dc` `#1a64b0` | each arm's darkest | dot-unit and stacked scales, diverging around a neutral |
| Sequential | `#7db2f0` `#4f90dc` `#2f74c2` `#1a5ba0` `#16416f` | — | magnitude, light → dark |
| Attempt marks | tried `#a2a09c` dots, rejected `#8e8c88` × | — | step charts of attempts |
| Status | good `#4a7b00`, bad `#b0453b`, neutral `#87867f` | — | change text only |

Validation (from `tokens.json`):
- Orange, aqua and violet pass every check on paper and on white. The worst pair under color-vision deficiency is aqua↔orange at ΔE 9.2 (deutan); normal vision 27.6. Aqua is 2.67:1 on paper, so its markers keep the ink outline and every chart has labels or a table.
- The rival grays are neutral by design. With orange and aqua the all-pairs floor stays 9.2 (CVD) and 18.1 (normal). The light gray is 1.73:1, so its markers always carry the outline.
- Comparison `#b0aea5` against orange on white: 13.0 / 18.6. At 2.2:1 it is always dashed and labeled at its end.
- Subject vs by-hand bars (`#eb6834` / `#87867f`): 9.5 / 17.8, both ≥ 3:1 on the panel. Orange line vs tried dots: 12.0 / 17.4; rejected attempts also differ by shape.
- Before/after pair: 28.7 / 32.9, both ≥ 4.5:1, so each labels its own values.
- Opinion-scale arms each pass the ordinal checks (monotone lightness, ΔL ≥ 0.06, light end ≥ 2:1); the poles are 22.3 / 27.3 apart.
- Sequential: one blue hue, monotone, every step ≥ 0.06 ΔL, light end ≥ 2:1 on paper and white.
- Good and bad pass as text (4.8:1, 5.3:1) but do not separate for deutan vision (ΔE 2.8). Status is never color alone: the value keeps its sign and its comparison words.

Rules:
- At most three hues plus gray in one chart. A fourth real category folds into Other or becomes small multiples.
- Color follows the entity, not its rank: the subject is orange in every figure and under every filter.
- Never put a yellow or amber series beside orange; they collapse under color-vision deficiency.
- Clay is not a data color.


## Typography Rules

| Role | English | Korean | Weights |
|---|---|---|---|
| Sans (everything else) | Inter | Noto Sans KR | 400, 500, 600, 700 |
| Serif (lede and section intros) | Source Serif 4 | Noto Serif KR | 400 |
| Mono (eyebrow, figure labels, pager, chips, file names, code) | JetBrains Mono | JetBrains Mono, then Noto Sans KR for Hangul | 400, 500 |

A screen loads only the fonts of its language. The Korean sans is Noto Sans KR because the brand's own Korean pages use it.

| Element | Size / weight | Notes |
|---|---|---|
| Headline | `clamp(28px, 3vw, 42px)` / 700, line-height 1.1, −0.022em | one sentence that states the result; `text-wrap: balance` |
| KPI value | 42px / 600, −0.03em | units at 0.42em in text-2 (`96.2 %`, `₩ 3,923`, `186 만 건`) |
| Section title | 32px / 700, −0.02em | |
| Mat title | 27px / 700, centered (22px in a half-width mat) | the finding |
| Card title | 21px / 700 | |
| Lede, section intro | 18px serif / 400, line-height 1.5 (Korean 17px / 1.65) | text-2; never bold |
| Launch panel title / subtitle | 17px / 600 · 15px / 400 text-2 | `Customer satisfaction` · `Satisfaction vs Cost` |
| Figure tabs | 15px / 600 | selected ink, others muted |
| Body, table | 14px / 400 | table values ink, `tabular-nums` |
| Caption | 13px, line-height 1.55 (launch caption 14px centered) | text-2; the lead sentence bold in ink |
| Legend | 13px / 600 | |
| Axis title / ticks / point labels | 12px ink · 11px text-2 · 10.5px ink | |
| Eyebrow / figure label | mono 11px uppercase, 0.1em / 0.018em | `OPERATIONS ANALYTICS · OCT 31, 2026`, `FIGURE 2` |
| Code | mono 12.5px, line-height 1.62 | |

Headings are sans and heavy; the serif is regular and only for prose. Korean text breaks between words (`word-break: keep-all`), and a number stays on the same line as the particle after it (`97%에`, `54건에서`).


## Numbers, Dates & Units

| | English | Korean |
|---|---|---|
| Money per order | `₩3,923` | `3,923원` |
| Large money | `₩4,375M`, `₩1.2B` | `43.75억`, `4억 3,750만 원` in sentences |
| Money axis | `₩2K ₩3K ₩5K ₩10K` | `2,000 3,000 5,000 10,000` |
| Counts | `1.86M` (KPI), `320K orders` (cards) | `186만 건`, `32만 건` |
| Rates | `96.2%`; two decimals when the spread is tiny (`99.58%`); whole numbers for survey shares (`60%`) | the same |
| Points | `+1.6 pts` | `+1.6%p` |
| Per thousand | `38 per 1,000 orders` | `주문 1,000건당 38건` |
| Hours | `10.1 h` | `10.1시간` |
| Change | `+8.4% vs Oct 2025` | `+8.4% 전년 동월 대비` |
| Dates | `Oct 31, 2026`; period `October 2026`; ticks `Nov … Oct` | `2026년 10월 31일`; `2026년 10월`; `11월 … 10월` |

- Signs use the true minus (`−`, U+2212). One decimal for change.
- The change color follows whether the move is good for that metric: cost per order `−6.9%` is green.
- Units and suffixes are smaller than the digits.
- `—` marks a value that does not exist (a rival without that service); the reason is in a numbered note. Footnote markers are superscripts (`CSAT¹`) linked to the notes.
- Scale qualifiers go in the axis title: `Cost per order (₩, log scale)`.
- The current month's tick is ink, the others text-2.


## Layout Principles

One column on the canvas, at most 1400px wide, 32px side padding (24px up to 1359px, 16px below 640px), 44px between rows. No sidebar, no app chrome, no logo.

1. **Header** (84px): company name (16px / 700) and report name (13px text-2). On the right: a period pill, the KO/EN toggle, a tertiary `Read in PDF` and the one primary button, `Copy as markdown`.
2. **Filter row** between two hairlines: 28px pills on the left, the basis (`As of October 31, 2026 · vs October 2025`) on the right. The pills scope every figure, table and card, and the URL keeps the choice (`?region=busan`).
3. **Headline block**, 7 of 12 columns: mono eyebrow → headline → serif lede that names the drivers → a section nav `(1) Service tiers (2) Rivals … (6) How it's built` whose numbers are mono. The four key figures sit at the right in 5 columns, 2 × 2, bottom-aligned with the nav.
4. **Launch figure + benchmark table**, 7 / 5.
5. **Card carousel** of entities (hubs, stores, products), four per page.
6. **One research mat, full width**: a finding title over two charts that share a y scale (1.9 : 1).
7. **Two research mats**, 7 / 5, on a subgrid so the mats and their captions line up.
8. **Workbench**: section title, serif intro, two buttons (`Read DASHBOARD.md`, `Get one for your company ↗`), then the window.
9. **Notes + related reports**, 7 / 5.
10. **Ink footer**, full bleed.

Density: at 1440 × 900 the header, filter row, headline, the four key figures and the top of Figure 1 are on the first screen; at 1366 × 768 the headline and the key figures are. Reading order follows the list; never lead with a chart.


## Component Stylings

- **Buttons** (measured): 36px tall, 10px radius, 14px / 500, icon after the label. Primary: ink fill, ivory text, hover `body`. Secondary: hair fill, hair-2 border, ink-2 text. Tertiary: card fill, hair border, body text. Small: 30px, 8px radius, 13px. Icon-only: 30 × 30. Hover changes the background only.
- **Pills**: 28px, 999px radius, 13px, card fill, hair border. Selected filter: hair fill, hair-2 border, ink 500. The language toggle is a segmented pill whose selected side is ink.
- **Key figure**: 1px `#d1cfc5` rule on top, 14px padding; label 14px / 500 ink → value → change line (13px text-2, the change in 600 status color, then `vs Oct 2025`). Two text sizes in the card besides the value.
- **Figure tabs**: plain text buttons, 15px / 600, 16px apart, 16px above the panel; `role="tablist"`.
- **Launch panel**: paper, 1px ink border, no radius, 16px 18px padding. Title left, subtitle right on the same baseline; legend right-aligned below them: buttons with a 14px circle swatch (1px ink stroke) and the series name, `aria-pressed`, 0.4 opacity when off; the last visible series cannot be turned off. Caption centered below the frame, 14px text-2, at most 640px wide.
- **Benchmark table**: `border-collapse: separate`, 14px, cells 10px 12px, 1px ink left and bottom borders, ink top border on the header, right border on the last column of each block. Row headers: category 600 ink over the metric name 13px text-2, footnote superscripts; sticky on the left when the table scrolls. Subject column: a 3px clay outline drawn with `::after` (sides on every cell, top on the header, bottom on the last row). Best of each row: peach + 600 when the subject wins, `#d1cfc5` + 600 when a rival wins (lower is better for speed and cost). A 10px gap, then the reference column on `card-2` with a two-line header (`2025` / `For reference`). A note under the table explains the shading and the panel.
- **Entity card**: 1px hair-2 rule on top, 18px padding above; a 30px ink glyph (simple original geometry, never a logo) beside the 21px / 700 title; a count line (`320K orders`, 13px text-2); one sentence (14px text-2); a status line (`On-time 96.9% +1.6 pts`). Four per page at ≥ 1100px of width, three, two, one; 24px gutters.
- **Pager**: 32px square buttons (8px radius, card fill, hair-2 border, arrow icons) around a mono counter `01 / 02`; disabled at the ends at 0.4 opacity.
- **Research mat**: `mat` fill, 8px radius, 26px 28px 28px padding; centered title; `panel` inside with a 16px radius and 22px 24px 18px padding. Caption outside: a 68px mono label column (`FIGURE 2`) and the text, the first sentence bold.
- **Boxed legend** (for marks that need a key, as in the research step chart): bottom-right inside the plot, 1px `#b0aea5` border, 2px radius, 12px text-2 rows with an 18px swatch.
- **Workbench window**: white, 12px radius, shadow `0 1px 2px rgba(20,20,19,.05), 0 12px 32px rgba(20,20,19,.10)`, on the cloud mat (8px radius, 36px padding, faint white curves). Three panes: a 208px package list (`#fafaf8`, file names in mono 11.5px with a one-line description), the figure (mono chips for the file and the filter value, title, plot, note, then a **Checks** list from this file with green check icons and `All 6 passed`), and the code (tabs `figure-5.js · figure_5.py · Tableau · Power BI · Prompt`, icon copy button and a primary `Run again`, line-numbered code, a status bar `● Built from DASHBOARD.md · 24 lines`). Syntax colors: comment `#6b6a64`, string `#3f7d1a`, number `#1a64b0`, keyword `#ad502d`, function `#6150d3`, property `#30302e` 500; hex values show a small swatch. Settings for Tableau show as two columns (name 14ch, value).
- **Notes**: 21px / 700 title, a numbered list 13.5px text-2, then sources and the update time.
- **Related reports**: an original node-and-link illustration (circles in the chart palette with ink strokes), the 21px title, cards on `card-3` with a 16px radius (date 13px text-2, title 16px ink), and a small tertiary `View more →`.
- **Tooltip**: ink fill, ivory text, 6px radius, shadow `0 4px 16px rgba(20,20,19,.14)`; a 12px title in `#b0aea5`, then rows of key (dot, or line for line series, dashed for the comparison), value 600, label. It takes the first side that fits inside the figure: above, left, right, below.
- **Toast**: the same ink box, bottom center, 2.2s.
- **Footer**: ink, full bleed, 12.5px `#b0aea5`; the catalog line in ivory.


## Charts

- **Choose by the question.** Quality against cost across options → connected scatter on a log cost axis, one line per company (the launch figure). Progress over many attempts → a step line of the best result so far over every attempt (dots kept or without gain, × rejected), with the target as a dotted reference line and `↓ Better` in the corner. Two groups with uncertainty → two bars with 95% error bars. Before and after per category → a dumbbell with a difference column. An opinion scale → dot units, one dot per person, grouped by answer with brackets and counts, the two sides diverging from a center rule. A trend against last year → a line with the comparison dashed gray.
- **Titles.** In a mat, the title is the finding (`Each kept routing change cut late deliveries`). In a launch panel, the title names the measure and the caption under the frame states the finding. The caption explains the method, the sample and the uncertainty.
- **Marks.** Launch figure lines 3px with r5 markers and a 1px ink stroke; other lines 2.5px; dumbbell dots r7.5 on an 8px round track; dot units up to 20px at 1.22 × pitch; bars about 64px wide.
- **Axes.** Framed figures: ink axis lines, gridlines `#e5e3dc`. Mats: text-2 axis lines and ticks, vertical gridlines `#e3e2d8` for dumbbells. Ticks 11px text-2, axis titles 12px. Four or five nice ticks. Side-by-side charts share one y scale and one baseline.
- **Labels.** The subject's points carry their names (10.5px) with a paper halo. Line ends carry `Name value` instead of a legend. The latest best result gets a star and its value in the subject's text color.
- **Legends** only where labels cannot do the job: series toggles in the launch figure, a boxed key for the marks of a step chart, a one-line key above a dumbbell.
- **One axis.** Never a dual axis. A synchronized second axis that only layers marks of the same measure (a Tableau dumbbell) is fine.
- **Never:** pie, donut, 3D, gradients, area fills, rainbow categories, smoothing, clay series, a fourth hue.
- Every chart has a hover tooltip, keyboard control and a screen-reader table.


## Depth & Elevation

Flat. Figures are framed by a line (launch) or set on a mat (research), never lifted. Shadows exist only on the workbench window, the tooltip and the toast. Nothing moves up on hover.


## Interaction & Motion

- **Filter**: one row of pills scopes everything; changing it rewrites the headline, lede, key figures, captions and titles, and redraws every figure. The URL keeps the region.
- **Figure tabs** switch the measure of the launch figure and rewrite its caption. **Legend toggles** hide a series.
- **Hover** shows the tooltip and an ink ring on the nearest mark; touch taps pick and a tap elsewhere clears.
- **Keyboard**: every chart is focusable; arrow keys step (up and down switch series in the launch figure), Home and End jump, Esc clears, and a live region reads the value. Tabs and filter pills move with arrow keys.
- **Carousel** pages with the pager; hidden cards are inert.
- **Workbench**: the first time it scrolls into view, the code types itself (55ms a line, 380ms between steps) and each step draws its layer of the figure (frame → comparison line → subject line → end labels → title and note) and ticks its check. Hovering a line of code spotlights the layer it draws; hovering a line of the chart highlights its code. Changing the filter rewrites the `region` value and flashes that line. `Run again` replays; the tabs show the same figure as Python, Tableau settings, Power BI settings and an agent prompt; the copy button copies the current tab.
- `Copy as markdown` copies the whole report as Markdown with a toast; `Read in PDF` prints.
- Motion: lines draw in 0.7s, labels fade in 0.3s, `cubic-bezier(.165,.84,.44,1)`; buttons change background in 0.22s. `prefers-reduced-motion` turns all motion off and shows the workbench finished.


## Accessibility

- Text ≥ 4.5:1 on its surface: text-2 6.3:1, muted 4.6:1, good 4.8:1, bad 5.3:1, orange text 4.9:1, aqua text 4.7:1, violet 5.5:1; code token colors ≥ 4.5:1 on white.
- Marks below 3:1 (aqua 2.67:1, light gray 1.73:1, comparison 2.2:1) always have a second cue: an ink outline, a dash, a label or a table.
- Identity is never color alone: names on points and line ends, dashes for comparisons, shapes for rejected attempts, signs on every change.
- Focus ring `#2c84db`, 2px, 2px offset. Tab order: header → filter → sections in reading order.
- Real tables with `scope`; every chart has a hidden data table and an `aria-label` that states what it shows.


## Responsive Behavior

- ≥ 1360: as laid out above.
- 1200–1359: 24px padding, 14px gap; table cells 10px; the workbench moves its file list above the figure and the code.
- 1024–1199: the launch figure and the table stack; the two mats stack; the workbench is one column (figure, then code up to 540px tall).
- 900–1023: the headline block stacks and the four key figures run in one row.
- 640–899: key figures 2 × 2; the report name and `Read in PDF` leave the header; Figure 2's bars move under the step chart; notes and related reports stack; code up to 440px.
- < 640: 16px padding; the period pill and `Copy as markdown` leave the header; the table drops the reference column and wraps row headers; the dumbbell puts names above each row and keeps the difference column; the step chart's key moves above the plot; dot units stack the two sides; code lines wrap. Cards page one at a time.
- Embedded in a post (`?embed=1`): the footer hides and the page reports its height to the host page.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` (or copy the `colors` block from the front matter) and these fonts:
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+KR:wght@400;500;600;700&family=Noto+Serif+KR:wght@400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;1,8..60,400&display=swap`

**Tableau.** Paste the `<color-palette>` elements of `anthropic.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette runs orange, aqua, violet, the two rival grays, Other and the comparison gray; assign the subject first.
- Dashboard background `#faf9f5`. A launch figure is a container with a 1px `#141413` border, no fill change, 16px inner padding; the tabs are a parameter (or navigation buttons) that swaps sheets.
- Marks: Color → Effects → Border `#141413` for every marker; markers on (all points for the launch figure, the last point for trends); line size 3 for the launch figure, 2.5 elsewhere. Edit Axis → Logarithmic for cost.
- Gridlines `#e5e3dc` (rows only), axis rulers ink, ticks Tableau Book 9 in `#5e5d59`.
- Research mats: an outer container `#e7e7db`, an inner one `#fbf9f5` (Tableau has no radius; keep the padding: 26/28px outside, 22/24px inside). The step chart is a step line of a running MIN over an attempt index, a circle layer of every attempt, and a dotted reference line for the target. Error bars are a reference band or a Gantt bar of the interval. A dumbbell is a synchronized dual axis of the same measure (line + circles); the difference column is a text sheet.
- The comparison table is a text table: borders 1px ink on rows and columns, a highlight calculation that colors the best value `#ebc9b7` (subject) or `#d1cfc5` (rival); outline the subject column with a floating 3px `#d97757` border object.
- Titles: the finding, bold; the method in the caption. Formats `₩#,##0`, `0.0%`, `+0.0" pts";−0.0" pts"`; Korean workbooks use `#,##0"원"` and `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Source Serif 4 and Inter are installed on every viewing machine and the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json`. It sets the data colors (the first three hues in order, then the two rival grays, then Other), the paper page, paper visuals with a 1px ink border, axis and gridline colors and text classes. Install Inter on authoring and viewing machines or accept Segoe UI.
- Title each visual with the measure or the finding; put the method in the subtitle. Turn legends off where data labels on the last point can name the series.
- Line and scatter markers on; error bars from the analytics pane for intervals; a dumbbell as a line chart with markers on two series and the line color set to `#dad9d1`.
- Key figures as cards with a top border `#d1cfc5` and no background; change measures with conditional formatting in `#4a7b00` / `#b0453b` only.

**Chart libraries (D3, Observable Plot, Vega-Lite, matplotlib, Datawrapper).** Subject `#eb6834` (labels `#b94a1c`), own past `#1baf7a` (`#008056`), rivals `#73726c` / `#c2c0b6` with `stroke: #141413` on markers, comparison `#b0aea5` dashed `6 4`, gridlines `#e5e3dc`, ticks `#5e5d59` at 11px. The sample's Figure 5 code in all five forms is in the workbench of the live sample; `orders.csv` is its data.


## Do's and Don'ts

- Do start with the result in one sentence, the drivers in a serif lede, and four key figures. Don't lead with a chart or a dozen KPI tiles.
- Do borrow the brand's own figure forms: the tabbed launch panel, the benchmark table, research mats with `FIGURE n` captions, card carousels. Don't fall back to generic cards with a chart in each.
- Do paint the subject orange and everyone else gray with ink-outlined markers. Don't use clay, yellow or a fourth hue on data.
- Do state the finding in the mat title or the caption, and the method and uncertainty in the caption. Don't title a chart with its measure alone and stop there.
- Do give side-by-side charts one scale. Don't use a dual axis.
- Do rule tables in thin ink and outline the subject column in clay. Don't zebra-stripe or tint whole rows.
- Do label points and line ends. Don't keep a legend that labels could replace.
- Do keep headings sans and heavy and the serif regular. Don't use a bold serif.
- Do show how the report is built when the reader is choosing a tool or a vendor. Don't put a logo, a wordmark or a photo anywhere.


## Agent Prompt Guide

Put this file in the project root as `DASHBOARD.md`, with `tokens.css` beside it. Then prompt, for example:

```
Read DASHBOARD.md and follow it exactly. Build a monthly operations dashboard for <company> as one self-contained HTML file
with fictional data, in English and Korean (?lang=en|ko, English by default).
Top: header with the period pill, language toggle, Read in PDF and Copy as markdown; one filter row of pills that scopes everything.
Then a mono eyebrow, a headline that states this month's result, a serif lede with the drivers, a numbered section nav,
and four key figures 2 × 2 with changes vs last year.
Then: a launch figure (tabs for three measures, a bordered paper panel, legend toggles, subject orange, our last year aqua,
rivals gray with ink-outlined markers, cost on a log axis, centered caption) beside a benchmark table (ink rules, the subject
column outlined in clay, wins in peach or gray, a "For reference" column); a carousel of entity cards; a full-width research mat
with a step chart and bars with 95% error bars on one scale; two research mats with a dumbbell and a dot-unit survey;
a workbench that shows one figure, its checks and its code; notes; the ink footer.
Use only the values in Data Colors, the formats in Numbers, Dates & Units and the components in Component Stylings.
Every chart needs a hover tooltip, keyboard control and a screen-reader table.
```

Before it is done, the agent checks:
- [ ] The headline states the result; the lede names the drivers; key figures carry signed changes colored by good or bad.
- [ ] Every mat title or caption states a finding; captions explain the method and the uncertainty.
- [ ] The subject is `#eb6834` everywhere; rivals gray with ink-outlined markers; comparison dashed `#b0aea5`; no clay, yellow or fourth hue on data.
- [ ] Points and line ends are labeled; legends only where labels cannot work.
- [ ] Side-by-side charts share a scale; no dual axis, pie or donut.
- [ ] Tables use ink rules and the clay-outlined subject column.
- [ ] Text ≥ 4.5:1; marks below 3:1 have a second cue.
- [ ] Every chart has a tooltip, keyboard control and a data table; the filter changes every card; nothing breaks at 390px.
