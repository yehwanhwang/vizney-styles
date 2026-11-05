---
name: Shell style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 6
tagline: Energy, Forecourt, Confident
tagline_ko: 에너지, 포코트, 당당함
source: https://www.shell.com, https://www.shell.us
sample: https://styles.vizney.com/shell/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#ffffff"
  panel: "#ffffff"
  plot: "#ffffff"
  soft: "#f7f7f7"
  band: "#f2f2f2"
  line: "#e4e4e4"
  hair: "#e4e4e4"
  rule: "#d9d9d9"
  edge: "#bfbfbf"
  ink: "#404040"
  body: "#4a4a4a"
  text-2: "#595959"
  muted: "#707070"
  yellow: "#fbce07"
  yellow-ui: "#ffc800"
  yellow-hover: "#e6b400"
  red: "#dd1d21"
  zone: "#262626"
  zone-2: "#3a3a3a"
  zone-muted: "#bdbdbd"
  gray-band: "#595959"
data:
  categorical: ["#e03a35", "#2f6aae", "#b08500"]
  other: "#a3a3a3"
  comparison: "#7b7b7b"
  categorical_text: ["#c4161c", "#2f6aae", "#8a6800"]
  sequential: ["#96b6e4", "#709ad6", "#4c7ec3", "#3063a9", "#1e4a85"]
  diverging: ["#b32322", "#dd574e", "#ea988f", "#e4e4e4", "#93b3e1", "#5a87c8", "#2d5da0"]
  good: "#007a3d"
  bad: "#c4161c"
typography:
  sans: { en: "Jost", ko: "Pretendard" }
  mono: "Roboto Mono"
radius: {card: "0", sign: "0", box: "0", button: "8px", toggle: "8px", tooltip: "4px", bar: "0"}
spacing: {page: "32px", gap: "16px", section: "44px", card: "16px 20px 0", note: "8px 20px 9px", kpi: "12px 14px 11px", signRow: "9px 16px 10px", footer: "22px 32px 34px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: shell.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: bridge.csv}
---

# Shell style — DASHBOARD.md

**Energy, Forecourt, Confident** · 에너지, 포코트, 당당함

A dashboard design spec read from the public design of shell.com and shell.us, Shell's quarterly results presentations and annual report, and the place most people meet the company: the forecourt, with its price sign, canopy band and gray base band. Shell publishes its numbers on slides — a kicker, a yellow rule, red chart titles, compare boxes, earnings bridges with gray totals — and on the forecourt it shows them on a white sign with a yellow head and a dark price zone. This spec turns those into dashboard parts — the price sign as a pillar of key figures, the results deck's compare boxes and key price markers, its earnings bridge, ruled exception lists, and a schematic corridor map with the sites as small price-sign pins — and adds what a website spec leaves out and a dashboard needs: validated data colors, card anatomy, chart rules, number and date formats in English and Korean, density, filters, accessibility, and settings for Tableau, Power BI and the web. Add it to a project with one command (or the zip on the sample page), or hand it to whoever builds your dashboards. The live sample was built from it.

```
npx @vizney/styles@latest add shell
# or, without Node:
curl -fsSL https://styles.vizney.com/install.sh | sh -s -- shell
```

That puts `DASHBOARD.md` in the project root and the `dashboard-style` agent skill (build, restyle, review) in `.claude/skills/dashboard-style/`, together with `tokens.css`, `tokens.json`, `shell.tps`, `powerbi-theme.json` and `prompt.md`. Coding agents that read skills pick it up whenever a task touches a dashboard or a chart; any other agent can be told to follow `DASHBOARD.md`.

- Live sample: https://styles.vizney.com/shell/?lang=en (Korean `?lang=ko`; one corridor `&corridor=i5`)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/shell/DASHBOARD.md
- Package: [shell-dashboard-style.zip](shell-dashboard-style.zip) (unzip in your project root) · the skill: [skill/SKILL.md](skill/SKILL.md)
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [shell.tps](shell.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [bridge.csv](bridge.csv) (the data behind the sample's Figure 2)
- Catalog: VIZNEY STYLES · 06 · https://styles.vizney.com (Vizney Styles is a line of [Vizney](https://www.vizney.com))

Not an official Shell design, and not affiliated with or endorsed by Shell. A reference style read from the publicly visible design of shell.com and shell.us and its public touchpoints such as forecourts and reports; it carries no logo, typeface, photo or data of theirs. The sample's company, Vizney Energy, and all its numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A forecourt that reports like a results slide. The page is white and flat. The header is a white canopy band — `Vizney Energy |` in red with the period in ink, the way Shell's slides end in `Shell plc |` — over a 6px red bar across the page, the canopy's red band; under it the corridor menu, set like shell.com's navigation with a 4px yellow underline on the selected item. Every section opens like a slide: a small kicker with the section number in red, the heading in ink, a 2px Shell-yellow rule across the width.

Three devices carry the report, and each is built to be read before it is admired. The **price sign** is the key figure: a white cabinet with a yellow head that holds the one big number (the main grade against the street), a 5px red bar, a dark price zone with one row per grade and the posted price to a tenth of a cent, and a gray base band with the site count and the posting time. The **key price markers** of the results deck become Figure 1: three small multiples with red chart titles, the subject line in red, the comparison in gray, the current week shaded, and compare boxes under each plot. The **earnings bridge** is Figure 2: plan to actual in lever steps, gray totals cut at a break, green increases, red decreases, negatives in parentheses. Around them sit ruled exception lists (sites, tanks, charge points), busy hours as bars, a schematic corridor operations map whose sites are small price-sign pins, and a results table from the annual report, collapsed to corridor totals.

Confident and plain: no shadows, no rounded cards, no gradients, no photos. Yellow and red belong to the frame — the rules, the sign's head, the canopy bar, the chart titles — and the data speaks in one red for the subject and gray for the rest, as Shell's own charts do. Every number answers a question someone acts on: price against the street, margin and volume against plan, which sites missed it and why, when to staff, which tank to fill, which charger to fix.

Measured in a browser on November 4, 2026 (shell.com and shell.us signed out, shell.co.kr for the Korean face; the third quarter 2026 results presentation of October 29, 2026; Annual Report 2025; the retail visual identity drawings): shell.com's body is white, headings `#404040`, secondary text `#595959`; primary buttons are 48px high with an 8px radius and 14px bold text, yellow `#ffc800` with dark text or dark `#4a4a4a` with yellow text; navigation items are 14px with a 4px yellow underline under the current item; tooltips and inputs have a 4px radius; there are no card shadows. The results slides put a kicker above each title and a 2pt yellow rule under it, set chart titles in bold red with the unit, put key figures in compare boxes `#f7f7f7` with a yellow bottom rule (`Q3 2026 vs Q2 2026`), shade the current period `#f2f2f2`, draw earnings bridges with gray totals, green increases, red decreases and negatives in parentheses, and end in a red footer line. The annual report marks non-GAAP measures with `[A]`, writes `(2024: x)` after a figure and puts units in parentheses after the measure. The forecourt's prime sign is white with a yellow head and a dark price zone of grades, under a canopy with a red band, over a 12-inch Shell Gray base band; Fuel Rewards copy says `¢/gal` and `main grade`. shell.co.kr declares the Shell face and falls back to Arial and system fonts — no Hangul web font. Photos and drawings were looked at only.


## Color Palette & Roles

Surfaces and text are shell.com's grays; yellow and red frame the page; the price zone is the sign's.

| Token | Hex | Role |
|---|---|---|
| canvas · panel · plot | `#ffffff` | page background, figure panels, the sign's cabinet; a chart sits on its panel |
| soft | `#f7f7f7` | compare boxes (the KPIs, Figure 1's boxes, the build steps), the corridor map's bands, the footer |
| band | `#f2f2f2` | the current week (Figure 1's column, Table 1's week 44 columns), the note band under every figure, hovered rows |
| line · hair | `#e4e4e4` | panel edges and chart gridlines |
| rule | `#d9d9d9` | row rules in lists and tables, the sign's edge, the tooltip border, toggles |
| edge | `#bfbfbf` | dashed thresholds (−3% of plan, 2 days of supply, 97% uptime) |
| ink | `#404040` | titles, key figures, table values (10.4:1) |
| body | `#4a4a4a` | running text; the dark button (shell.com) |
| text-2 | `#595959` | kickers, subtitles, notes (7.0:1) |
| muted | `#707070` | figure labels, axis ticks, units, `(Wk 43: x)` (4.95:1) |
| yellow | `#fbce07` | Shell yellow: the 2px rule under every heading, the compare boxes' bottom rule, the sign's head, the footer rule. Never data |
| yellow-ui · hover | `#ffc800` · `#e6b400` | buttons, the menu underline, the map pins' heads, the selected site · button hover |
| red | `#dd1d21` | Shell red: the canopy bar, chart titles, section numbers, the company name, `[A]` markers. Never data |
| zone · zone-2 · zone-muted | `#262626` · `#3a3a3a` · `#bdbdbd` | the sign's price zone · rules between grades and the hovered grade · grade names and small figures (8.1:1) |
| gray-band | `#595959` | the sign's base band with white text (7.0:1) |

Rules:
- Panels are white with a 1px `#e4e4e4` edge; no radius on panels, boxes or the sign; 8px on buttons and toggles, 4px on the tooltip; no shadows except the tooltip and the toast.
- Yellow is a rule or a head, never a fill behind running text and never data. Red is the frame (the canopy bar, chart titles, numbers of sections), never a series; the data's red is its own step `#e03a35`.
- The price zone `#262626` belongs to the sign and to the map's pins; never fill a panel with it.


## Data Colors

Shell's results charts put the subject in red and everything else in gray, so this style does the same: red is the subject, gray the rest, with Shell's blue and yellow as data steps for a rare second and third series. Every value passed an OKLab validator (color-vision-deficiency separation, normal-vision separation, contrast) on the panel `#ffffff` and the compare boxes `#f7f7f7`. Use them exactly; do not generate tints.

| Role | Mark | Label text | Use |
|---|---|---|---|
| Subject | `#e03a35` | `#c4161c` | what the title names: the posted price, actual margin and volume, the sites more than 3% below plan, the busiest hours, the tanks and charge points past their threshold |
| Second series | `#2f6aae` | `#2f6aae` | a second measure beside the subject, rare |
| Third series | `#b08500` | `#8a6800` | only on lines and bars with direct labels, never next to red |
| Other | `#a3a3a3` | text-2 | everything else: rows inside the threshold, other hours |
| Comparison | `#7b7b7b`, solid 2px for a second measure (laid-in cost), dashed 2px (5 on, 4 off) for plan | ink | always labeled at its end |
| Bridge | totals `#818181`, increase `#008443`, decrease `#e03a35` | ink | Figure 2 |
| Thresholds and lines | zero `#404040`, threshold `#bfbfbf` dashed, baseline `#9a9a9a`, grid `#e4e4e4`, current week `#f2f2f2` | — | |
| Sequential | `#96b6e4` `#709ad6` `#4c7ec3` `#3063a9` `#1e4a85` | ink on the two lightest, white on the rest | color by value; blue, so magnitude never reads as bad |
| Diverging | `#b32322` `#dd574e` `#ea988f` · `#e4e4e4` · `#93b3e1` `#5a87c8` `#2d5da0` | each arm's darkest | above and below a midpoint |
| Status | good `#007a3d`, bad `#c4161c`, neutral `#7b7b7b` | — | change text and status words only |

Validation (from `tokens.json`, light mode, on `#ffffff` and `#f7f7f7`):
- Red `#e03a35` sits one step lighter than the brand red `#dd1d21`, which stays on titles and the canopy bar. Adjacent order red → blue → ochre → gray: lightness inside 0.43–0.77, chroma ≥ 0.10, CVD ΔE 18.5 (protan, red↔blue), normal vision 28.1, contrast ≥ 3:1 on both surfaces; with Other last, the worst adjacent pair is ochre↔gray at 14.7 (CVD) and 15.1 (normal). Across all pairs red↔ochre is 4.0 (deutan), so three series only on lines and bars with direct labels, and scatter plots and maps use red and blue only.
- Other `#a3a3a3` is neutral by design (the lightness band and chroma floor do not apply). At 2.52:1 it always has a second cue: value labels, the grid and tooltips, a table view.
- Comparison `#7b7b7b` against red: CVD 11.1 (protan), normal 20.4, 4.23:1 on white.
- Bridge: increase↔decrease is CVD 7.6 (protan), inside the 6–8 floor band, so the bridge always carries its second encoding: direction from the running total, parentheses on negatives and a value on every bar.
- The sequential ramp is one blue hue, monotone, every gap ≥ 0.06, the light end 2.08:1. The diverging arms pass the ordinal checks (light ends 2.24 and 2.15:1); the poles are 19.6 (CVD) and 27.4 (normal) apart; the midpoint is the grid gray.
- Text: red labels `#c4161c` 6.04:1 (5.39:1 on the `#f2f2f2` column), ochre labels `#8a6800` 5.17:1, good `#007a3d` 5.45:1 (5.09:1 on `#f7f7f7`), bad 6.04:1 (5.63:1). Good↔bad is 5.1 under deuteranopia, so status is never color alone.

Rules:
- Red only for what the title names; the rest gray. A card that is mostly red has highlighted nothing.
- A red mark means the subject or a shortfall, never both in one view: where red marks the rows past a threshold (Figures 3, 5, 6), the subject is those rows.
- Status is never color alone: `▲` / `▼`, the sign or parentheses and words (`below plan`) always come with it.
- Never the brand red `#dd1d21` or Shell yellow on data.


## Typography Rules

| Role | English | Korean | Weights |
|---|---|---|---|
| Sans (everything) | Jost | Pretendard | 300–800 |
| Mono (code in How it's built only) | Roboto Mono | Roboto Mono, then Pretendard for Hangul | 400, 500 |

Jost, a geometric sans after Futura, stands in for the Shell typeface, which is not open; its round O and single-storey figures read close to the forecourt's numerals, and its tabular figures keep columns aligned. shell.co.kr loads no Hangul web font, so Korean uses Pretendard. Numbers on the screen stay in the sans with tabular figures; there is no serif.

| Element | Size / weight | Notes |
|---|---|---|
| Company line · report name | 13.5px: `Vizney Energy` red 500, `|` red 300, the period in body · 28px / 700, line-height 1.15 (Korean 26px) | `Vizney Energy | Wk 44 · 26 Oct – 1 Nov 2026` |
| Kicker | 14px / 400 text-2 | `Mobility results · Week 44`; in sections the number in red 500 |
| Headline | `clamp(24px, 2.05vw, 29px)` / 600, line-height 1.26 | the finding in one sentence; figures in it at 700 in ink (red stays for titles and data) |
| Lede | 15.5px / 400, line-height 1.5 | |
| Section heading | 24px / 700 ink, then a 2px `#fbce07` rule 12px below | |
| Sign label · big number | 12px / 700 caps, 0.08em · 26px / 500 tabular | `POSTED PRICE · WK 44`, `Main grade vs the street +0.2¢` |
| Sign grade · price · margin | 12px / 600 caps `#bdbdbd` · 42px / 500 white, the tenth of a cent at 0.42em superscript, the unit 12px · 17px / 500 white over `margin` 12.5px | 38px under 1360px, 32px on the horizontal board |
| KPI (compare box) | measure 13px with the unit in parentheses · figure 38px / 500, −0.015em · change 13px / 600 status · `(Wk 43: x)` 12.5px muted | four rows on a subgrid |
| Figure label | 12px / 600 caps, 0.07em, muted | `FIGURE 1 · PRICE MARKERS` (Korean 13px, no caps: `그림 1 · 시세`) |
| Card title | 18.5px / 600, line-height 1.32, `text-wrap: balance` | the finding |
| Chart title | 14px / 700 red `#dd1d21`, the unit after it 13px muted | the results deck's red chart titles |
| Key · labels | 12.5px / 500 | |
| Note band | 12px on 17px text-2 on `#f2f2f2` | starts with `Note:` / `주:` where it is a note; `[A]` notes start with the marker |
| Axis ticks · value labels | 12px muted · 12.5px / 600 ink | |
| Body | 14px / 400, line-height 1.5 | |

Korean breaks between words (`word-break: keep-all`), and a number stays on the line with the particle after it.


## Numbers, Dates & Units

| | English | Korean |
|---|---|---|
| Pump price | `$3.55⁶/gal` (the tenth of a cent as a superscript, as on the sign) | `3.55⁶달러/갤런` |
| Price in text · tables | `$3.556`, `$0.606/kWh` | `3.556달러`, `0.606달러/kWh` |
| Price differences · margin | `+5.7¢`, `46.0¢ a gallon`, `¢/gal` | `+5.7센트`, `갤런당 46.0센트` |
| Volume | `1.48` (million gal) in KPIs, `1,482` thousand gal in charts, `60.9` K gal in lists | `148.2`(만 갤런), `148만 2천 갤런`; lists `천 갤런` |
| Money | `$1.12` million in KPIs, `$2.5K` in sentences, `1,099.5` ($ thousand) in the bridge | `112.3`(만 달러), `2,500달러`, `1,099.5`(천 달러) |
| Energy | `175` MWh | `175` MWh |
| Rates · points | `14.2%`, `−0.8 pts`, `71.4%` uptime | `14.2%`, `−0.8%p` |
| Change against plan | `▼ 1.2% below plan`, `▲ 1.0¢ above plan`, `▼ 0.8 pts below the 15% target` | `▼ 계획보다 1.2% 적음`, `▲ 계획보다 1.0센트 높음`, `▼ 목표 15%보다 0.8%p 낮음` |
| Last period | `(Wk 43: 1.49)`, after the change | `(43주: 148.9)` |
| Negatives in tables and bridges | `(9.0)`, `(3.0)` | the same |
| Dates and weeks | `Wk 44 · 26 Oct – 1 Nov 2026`, `Wk 32` on axes, `6 am Mon 2 Nov`, `Tue 3 Nov` | `44주 · 2026년 10월 26일~11월 1일`, `32주`, `11/2(월) 오전 6시`, `11/3(화)` |
| Hours | `4–7 pm`, `12 am`, `6 pm` on axes | `16~19시`, `0시`, `18시` |
| Sites · equipment | `I-5 Exit 188`, `CP-3`, `Station A` | `I-5 188번 출구`, `CP-3`, `경쟁 주유소 A` |
| Distance | `0.8 mi`, `100 mi` | `0.8마일`, `100마일` |
| Missing | `—` (no charge points) | `—` |

- Money is in the company's currency; the sample's company is American, so US dollars and gallons. Sites are named by interstate and exit; the exits, prices and competitors are made up.
- Signs use the true minus (`−`, U+2212); one decimal for change, a tenth of a cent for pump prices.
- Change colors follow whether the move is good for that metric (a price above the street on a site that missed plan is bad).
- Units go in parentheses after the measure (`Fuel margin (¢/gal)`), as in the annual report, so the figure stands alone.
- A table that is rounded still adds up: round each line, then hand the leftover units to the lines with the largest remainders (sites to corridors, corridors to the total; the bridge's steps to the actual). The exact value is in the tooltip.
- Weeks run Monday to Sunday; prices are posted at 6 am and the report is published 6 am Monday.


## Layout Principles

One column on a white page, at most 1400px wide, 32px side padding (24px up to 1359px, 16px below 640px), a 16px gap, 44px above each section. No sidebar, no logo, no photo.

1. **Canopy band** (white, 80px): `Vizney Energy |` and the period; the report name; on the right EN/KO, `Export PDF` (dark) and `Copy as Markdown` (yellow).
2. **Red bar** (`#dd1d21`, 6px) across the page.
3. **Corridor menu** (52px, 1px `#e4e4e4` below): `All corridors (24) · I-5 (8) · I-10 (8) · I-95 (8)`, the selected one 700 with a 4px `#ffc800` underline; `Against plan and week 43` on the right. It is the filter: it scopes every card, and the URL keeps it (`?corridor=i5`).
4. **This week** (from 1200px): the price sign as a pillar on the left (304px, 272px under 1360px); on the right the kicker, the finding headline, the lede, a yellow rule, five compare-box KPIs on a subgrid and Figure 1 (three price markers). The two columns end on one line: the sign's grade rows and Figure 1's plots take the extra height.
5. **02 Against plan:** Figure 2 the gross margin bridge (5 of 12 columns) · Figure 3 sites against plan (7 of 12).
6. **03 Forecourt operations:** Figure 4 busy hours · Figure 5 tanks · Figure 6 charge points, a row of three.
7. **04 Sites:** Figure 7 the corridor operations map across the page (the map and, beside it, the selected site zoomed to its 2-mile street with what to do), then Table 1 results by site, collapsed to corridor totals.
8. **05 How it's built:** an intro with two buttons, three compare-box steps, the workbench window.
9. **06 Method and sources:** footnotes in two columns, `[A]` in red.
10. **Footer** (`#f7f7f7` over a 2px yellow rule): the catalog line, the sample note, the notice and the way back.

At most seven views in a section, and every view a standard form an agent or a BI tool can rebuild. Density: at 1440 × 810 the frame, the price sign, the headline, the five KPIs and the top of Figure 1 are on the first screen. Reading order follows the list; never lead with a chart.


## Component Stylings

- **Panel** (every figure and table): white, 1px `#e4e4e4`, no radius, no shadow, 16px 20px 0. Head: figure label → finding title → a 2px `#fbce07` rule → red chart title with the unit → keys; then the plot; then the note band (`#f2f2f2`, 8px 20px 9px, bleeding to the panel's edges). Never a card inside a card.
- **Section head**: the kicker (`02` in red 500, then `Against plan` in 14px text-2), the heading 24px / 700 ink, a 2px yellow rule across the width.
- **Price sign** (the KPI pillar): a white cabinet with a 1px `#d9d9d9` edge. The head on `#fbce07`, 14px 16px 13px: `POSTED PRICE · WK 44` (12px / 700 caps), `Average across sites, vs week 43` (13px), then above a 1px rule the one big number: `Main grade vs the street` and `+0.2¢` (26px / 500). A 5px `#dd1d21` bar. The price zone on `#262626`, one row per grade (Regular, Mid-grade, Premium, Diesel, EV fast charge), at least 74px each, 1px `#3a3a3a` between: the grade (12px / 600 caps `#bdbdbd`) and the change against last week at the top right (12.5px `#bdbdbd`); the posted price (42px / 500 white, `$3.55⁶`, the unit `/gal` 12px); the margin at the right (17px / 500 white over `margin`). The base band on `#595959` (12.5px white): `Volume-weighted across 24 sites · posted 6 am Sun 1 Nov`. Rows hover to `#3a3a3a` and step with the arrow keys. From 1199px down the sign lies down as a horizontal price board under the headline: the yellow head on the left, the five grades side by side with a 5px red edge, the base band under them.
- **Compare box** (KPI): `#f7f7f7`, a 2px `#fbce07` bottom rule, 12px 14px 11px; four rows on a subgrid so the figures line up: the measure with its unit in parentheses (`Fuel volume (million gal)`), the figure (38px / 500), the change against plan or target (`▼ 1.2% below plan`, 13px / 600 in good or bad), then `(Wk 43: 1.49)` in muted.
- **Price markers** (Figure 1): three small multiples side by side. Each: the red chart title and the unit line (`Main grade price` · `$ a gallon, 13 weeks`), a key, the plot (the subject in red 2.5px, the comparison 2px gray — solid for laid-in cost, dashed for plan — gridlines on rows, the current week as a `#f2f2f2` column that holds both end labels), then two compare boxes under it (`#f7f7f7`, a 1.5px yellow bottom rule): `Posted · Wk 44 · $3.556 · vs Wk 43 −3.5¢`.
- **Bridge** (Figure 2): bars for `Plan · Volume · Margin · Mix · Shop · EV · Actual`; totals `#818181` cut at a white double break near the axis floor (the axis starts at 1,080, and the note says so); steps float from the running total, increases `#008443`, decreases `#e03a35`; dotted 1px connectors at the running total; values above or below the bars in ink, negatives in parentheses; the step names under the axis on two lines when needed; rounded to $0.1K so the steps add up.
- **Exception list** (Figures 3, 5, 6): ruled rows (1px `#d9d9d9`, 30px) under a header line in ink (11.5px / 600 caps muted). Name (the site in 600, the grade or charge point in text-2), a bar from a zero line (1px ink) with a dashed `#bfbfbf` threshold, the value at the bar end, then one or two columns (`K gal`, `vs street`; `Delivery`; `Uptime`, `Lost`). Rows past the threshold are red `#e03a35` with the value in `#c4161c` / 700; the rest `#a3a3a3`. Figure 3 numbers the rows (`1`–`8`); Figure 5 writes `Not booked` in bad; Figure 6 draws hours down of 168 with the target `97% (5 h down)`.
- **Busy hours** (Figure 4): 24 bars, the busiest three hours red and labeled, the rest `#a3a3a3`, ticks every 6 hours, a note that says what to do with the quiet hours.
- **Corridor operations map** (Figure 7): one schematic interstate per corridor in its own `#f7f7f7` band (a white 6px road over an 11px `#cfcfcf` casing; the bends are invented, the distance along the road follows the exit numbers, which are mile markers, with a small mark every 100 mi). Each site is a small price-sign pin on a stem, alternately above and below the road: a `#ffc800` head with the exit number (11px / 700) and a body with the change against plan (12px / 700 white) on `#262626`, or `#c4161c` when more than 3% below plan. Problems hang beside the pin as 8px red badges with white glyphs — a drop for a tank under 2 days with no delivery booked, a bolt for a charge point under 97% — and a site with two problems at once gets a pale red halo with a `#e03a35` ring on the road. The corridor name (18px / 700), its site count and its change against plan sit at the left. A click or the arrow keys select a site (a 3px `#ffc800` outline); the most urgent site (most problems, then the largest shortfall) is selected first.
- **Zoom** (beside the map, 400px; below it under 1200px): `ZOOMED IN · 2-MILE RADIUS` (12px / 600 caps muted), the site (21px / 700), `−6.5% vs plan · +5.7¢ vs the street`. A schematic interchange on `#f7f7f7`: the highway, a cross road and four ramps in the map's road style, a dashed `#bfbfbf` circle of 2 miles (the radius that defines the street price) and a 1-mile scale bar. Our posted main-grade price stands on a pin (`POSTED` on yellow, the price on `#262626` or red); each competitor is a white dot with a gray ring and a tag (`$4.49⁹`, `B · 1.3 mi`) joined by a 1px leader; a competitor that opened or cut its price in week 41 gets a red ring and a red head (`NEW · WK 41`, `CUT · WK 41`). Pins, tags and place names take free spots and never cover a dot or each other; a place name with no room is dropped. Under the map, `What to do`: one line per problem with a red badge — `Review the posted price`, `Book a delivery`, `Send a technician` — each with the numbers behind it (`Fuel volume is 6.5% below plan, and the posted $4.529 is 5.7¢ above the street. Station A, 0.8 mi away, opened in week 41 at $4.399.`); a calm site says `No alerts this week`. Then four figures: Volume, Margin, vs street, Uptime.
- **Results table** (Table 1), from the annual report's tables: group heads with the unit on a second line (`Fuel volume` / `thousand gal`), the week 44 columns shaded `#f2f2f2`, corridor rows in bold with a chevron that opens their sites (furthest below plan first), `Show all sites` / `Hide sites` above the table, a total row over a 1.5px ink rule, negatives in parentheses and red when they are shortfalls, `—` for sites without chargers, a small gray bar beside each site's volume. The all-corridors view starts collapsed; a single corridor starts open.
- **Buttons** (measured): 40px, 8px radius, 14px / 600, 0 14px. Yellow `#ffc800` with ink text (hover `#e6b400`); dark `#4a4a4a` with yellow text (hover `#404040`); outlined white with a 1px `#4a4a4a` border. Small: 32px, 6px radius, 13px.
- **Corridor menu**: 15px / 500 items padded 4px 10px, the selected one 700 ink with a 4px `#ffc800` underline, the count after it 13px muted, hover `rgba(74,74,74,.06)`; `role="tablist"`, arrow keys move. The EN/KO toggle is a 40px box with a 1px `#d9d9d9` edge and 8px radius, two 32px cells, the selected one `#4a4a4a` with yellow text.
- **Tooltip**: white, 1px `#d9d9d9`, 4px radius, shadow `0 2px 10px rgba(0,0,0,.14)`; a 13px / 700 head, an optional 12px muted line, then rows of key (a 9px square or a 14px line, dashed for plan), value 600 ink and label text-2. It takes the first side that fits inside its panel.
- **Workbench window**: 1px `#e4e4e4`, white. A package panel on `#f7f7f7` (file tree in mono, install commands with copy buttons, `Download .zip`), the figure pane (the `Without a spec / With DASHBOARD.md` toggle, a chip `corridor = all`, Figure 2, then **Checks · DASHBOARD.md**), and the code pane (tabs `Prompt · plan.md · figure-2.js · Tableau · Power BI` with a 4px yellow underline, `Run again`, line-numbered code, a red caret while typing). Syntax: comment `#707070`, string `#007a3d`, number `#9c5b00`, keyword `#2f6aae`, function `#c4161c`, property `#404040`, the highlighted line `#fff4c2`.
- **Footnotes** (Method and sources): two columns 40px apart, 12.5px, line-height 1.65; terms bold; `[A]` in red before the defined measure.
- **Footer**: `#f7f7f7` over a 2px `#fbce07` rule, 13px text-2; the catalog line in 600 ink, the series in 12px / 700 with 0.08em tracking; the way back underlined in yellow.


## Charts

- **Choose by the question.** Shell shows its numbers on the sign and on results slides; start with those parts and draw a chart only where they cannot answer.
  - How did the week do → the finding headline, the price sign (posted price by grade, the main grade against the street) and five compare boxes, each against plan or target with last week in parentheses.
  - What moved prices and margin → key price markers: three small lines with the subject red and the comparison gray, both ends labeled in the shaded current week (Figure 1).
  - Why profit differs from plan → the bridge, plan to actual by lever (Figure 2).
  - Which sites missed plan, and why → a ranked exception list with the threshold and the price against the street beside it (Figure 3).
  - When to staff and when to deliver → busy hours, the busiest three red (Figure 4).
  - Which tank to fill, which charger to fix → exception lists against 2 days of supply and 97% uptime (Figures 5, 6).
  - Where the problems sit, and what to do at one site → the corridor operations map with a zoom on the selected site (Figure 7).
  - The detail by site → the results table, collapsed to corridor totals (Table 1).
- **Titles.** The card title is the finding (`5 sites missed fuel plan by more than 3%, all priced 3.5–6.0¢ above the street`; `3 sites carry two problems at once: I-5 Exit 76, I-5 Exit 188 and I-95 Exit 41`), recomputed when the filter changes. The red chart title names the measure and the unit; the note band explains the method.
- **Marks.** Lines 2.5px for the subject and 2px for the comparison, with a hollow end marker. Bars square-ended, list bars 10px, bridge bars up to 44px with 2px gaps. Map pins 46 × 36px.
- **Axes.** `#e4e4e4` gridlines on rows only, no vertical axis line; ticks 12px muted, four to six nice ticks (steps of 1, 2, 5 or 10); weeks `Wk 32`, the current week shaded `#f2f2f2`. A cut axis gets white double break marks and a sentence in the note.
- **Labels.** Line ends carry the value in the series' text step inside the shaded column; values on bars 12.5px / 600 in ink, negatives in parentheses. The tooltip adds detail; it is never the only copy of a number.
- **Keys** as one row under the chart title (a 14 × 10 square, a line, a dashed line, a tick, a badge).
- **Rounding.** Tables and bridges round to a readable unit and still add up; the exact value is in the tooltip.
- **One axis.** Never a dual axis.
- **Never:** pie, donut, 3D, gauges, gradients on data, smoothed lines, the brand red or Shell yellow on data, a real map, terrain, city names or route shields, photos or logos, decoration that carries no number.
- Every chart, list and the map have a tooltip, keyboard control and a screen-reader table.


## Depth & Elevation

Flat and white. Panels are set apart by a 1px `#e4e4e4` edge, compare boxes by `#f7f7f7` and a yellow rule, never by shadows, and never lift on hover. Only the tooltip and the toast have a shadow. The price sign's depth is its three zones — yellow head, dark price zone, gray base band — not a bevel or a glow.


## Interaction & Motion

- **Filter**: the corridor menu scopes everything. Changing it rewrites the headline, the lede, the sign, the KPIs, every title and note, redraws every view, shows one corridor on the map (and moves the zoom to its most urgent site), and opens that corridor in Table 1. The URL keeps the corridor.
- **Hover** shows a crosshair and hollow dots on lines, a `#f2f2f2` band behind a bar, a row or an hour, `#3a3a3a` behind a grade in the sign, and the tooltip; a tap picks on touch screens.
- **Map**: hovering a pin shows its tooltip; a click selects it and redraws the zoom; arrow keys step through the sites in exit order, Home and End jump, Esc clears the tooltip; focus stays on the map while it redraws.
- **Keyboard**: every chart, list, the sign, the map and the table are focusable; arrow keys step, Home and End jump, Esc clears, and a live region reads the value. Menus move with arrow keys.
- **Workbench**: the first time it scrolls into view, the code types itself (55ms a line, 380ms between steps) and each step draws its layer of Figure 2 (frame → totals → steps → values → title and note) and ticks its checks. Hovering a line of code spotlights its layer. `Without a spec` shows a typical first draft and fails all six checks. Changing the corridor rewrites the `corridor` value and flashes that line.
- `Copy as Markdown` copies the whole report (the sign, the KPIs, every figure's rows, the map's sites and problems, the table and the notes) with a toast; `Export PDF` prints the page.
- Motion: lines draw in 0.7s; bars grow in 0.45s, one after another; pins and rows fade in 0.3s; buttons change in 0.15s; `cubic-bezier(.4,0,.2,1)`. `prefers-reduced-motion` turns all motion off and shows the workbench finished.


## Accessibility

- Text ≥ 4.5:1: ink 10.4:1, text-2 7.0:1 and muted 4.95:1 on white; red labels 6.04:1, ochre 5.17:1, good 5.45:1, bad 6.04:1; white on `#262626` 15.1:1, `#bdbdbd` on `#262626` 8.1:1, ink on `#fbce07` 6.9:1, white on `#595959` 7.0:1.
- Marks below 3:1 (Other `#a3a3a3` at 2.52:1, the current-week band) always have a second cue: a value label, the grid, a table.
- Identity is never color alone: values at line ends, `▲` / `▼` and words on every change, parentheses on negatives, glyphs inside the map's badges, the halo's ring, dashes for plan.
- Focus ring 2px `#404040` with a 2px offset.
- Real tables with `scope` (Table 1 is a table; its toggles are buttons with `aria-expanded`); every chart and the map have a hidden data table and an `aria-label` that says what they show and how to move.


## Responsive Behavior

Each step keeps what the wider steps changed.

- ≥ 1360: as laid out above.
- 1200–1359: 24px padding; the sign 272px with 38px prices; compare boxes 11px 12px 10px.
- 1024–1199: the sign lies down as a horizontal price board under the headline (the yellow head on the left, five grades side by side with a 5px red edge, the base band under them), then the KPIs and Figure 1 across. Figure 4 runs across above Figures 5 and 6. Figure 7's zoom moves under the map and splits into the map on the left and what to do on the right; the map's bands are 158px each.
- 900–1023: Figures 2 and 3 stack; the board's prices 30px; the workbench and the footnotes in one column.
- 640–899: the header wraps; `Export PDF` and the menu's right-hand line hide; KPIs and the board's grades in a 3 + 2 grid; Figure 1's markers one per row; Figures 4–6 one per row; Table 1 drops the week 43 columns (under 900px of table width).
- < 640: 16px padding; KPIs 2 × 2 with the fifth across (figures 28px); the board's grades 2 × 2 with the fifth across (28px); Figure 7 becomes a route list in exit order (station, exit, badges, a bar from the plan line, the value, a halo on two-problem sites) and a row selects; the zoom stacks head, map and what to do; Table 1 keeps volume, against plan, margin and uptime.
- Embedded in a post (`?embed=1`): the footer hides and the page reports its height to the host page.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` (installed in `.claude/skills/dashboard-style/`; or copy the `colors` block from the front matter) and these fonts (the second for Korean).

<!--email_off-->

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600;700;800&family=Roboto+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
```

<!--/email_off-->

The sign is a flex column (head, red bar, a grid of grade rows that grows to fill, base band); prices are spans with the tenth of a cent in a `<sup>` at 0.42em. Compare boxes use `grid-template-rows: subgrid` so the figures line up. The map is one SVG: each road a Catmull-Rom curve through seven points with sites placed by arc length; the zoom places our pin, then the competitor tags, then place names in the first free spot from a list of candidates. Give a device's parts a prefix (`ps-`, `mp-`, `mz-`) so shared classes never leak into them.

**Tableau.** Paste the `<color-palette>` elements of `shell.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette runs red, blue, ochre and Other; assign the subject first.
- Dashboard background `#ffffff`. The header as a text object (`Vizney Energy |` in red); a 6px blank object filled `#dd1d21` across; the corridor filter as a single-value list; section heads as text objects with a 2px `#fbce07` blank object under them.
- Each sheet in a container with a 1px `#e4e4e4` border and 16/20px inner padding; the finding as the sheet title, the red chart title (`#dd1d21`, bold) as a subtitle line; the note in a text object on `#f2f2f2`.
- Price sign: a container with a `#fbce07` text object on top (the big number), a 5px red blank, a text table on a `#262626` sheet (white text, the price at 28pt; Tableau cannot raise the tenth of a cent, so write `$3.556`) and a `#595959` text object at the foot.
- Compare boxes: text sheets on `#f7f7f7` with a 2px yellow blank object under each; the change in `#007a3d` or `#c4161c` with ▲ or ▼; `(Wk 43: x)` in a small line.
- Price markers: three line sheets with a reference band on the last week (`#f2f2f2`); plan dashed.
- Bridge: Gantt bars on `RUNNING_SUM(SUM([usd]))` with size `−SUM([usd])`, Color by kind (`#818181`, `#008443`, `#e03a35`); fix the axis start at the break and say so in the caption. Number format `#,##0.0;(#,##0.0)`.
- Exception lists: bars sorted by value with a reference line at the threshold (dashed `#bfbfbf`) and Color by `past threshold` (`#e03a35` / `#a3a3a3`); extra columns as Measure Names text.
- Corridor map: a dual-mark sheet on a scaffold of road points (X, Y from the curve) with the sites as shapes at their exit's position, labels for the exit and the change, and a second sheet for the selected site's zoom driven by a parameter action; or, simpler, the route list (sites in exit order, a bar from the plan line, badges as shapes).
- Results table: a text table with the current week columns shaded by a calculated `#f2f2f2` band, corridors as a hierarchy that drills down to sites, negatives as `(0.0)`.
- Formats: `"$"#,##0.000` (pump prices) · `0.0"¢"` · `#,##0.0` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0.000"달러"`, `0.0"센트"` and `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Jost is installed on every viewing machine and on the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json`. It sets the data colors (red, blue, ochre, then Other), the white page, white visuals with a 1px `#e4e4e4` border and no radius, axis and gridline colors and text classes. Install Jost on authoring and viewing machines or accept Segoe UI.
- Title each visual with the finding; put the red chart title in the subtitle and the method in a text box on `#f2f2f2` that starts with `Note:`.
- Price sign: a yellow card for the big number over a table visual with a `#262626` background and white text; a shape `#dd1d21` between them.
- Compare boxes: card visuals on `#f7f7f7` with a yellow bottom border, the change as a measure with conditional formatting in `#007a3d` / `#c4161c`, always with a sign.
- Bridge: the waterfall visual with sentiment colors increase `#008443`, decrease `#e03a35`, total `#818181`; data labels in thousands with one decimal, negatives in parentheses.
- Exception lists: bar charts with a constant line at the threshold and conditional colors; the map as the route list or a shape map of the schematic roads, with a drillthrough page as the zoom.

**Chart libraries (D3, Observable Plot, Vega-Lite, matplotlib, Datawrapper).** Subject `#e03a35` (labels `#c4161c`), second `#2f6aae`, third `#b08500` (`#8a6800`), Other `#a3a3a3`, comparison `#7b7b7b` (dashed `5 4` for plan), bridge totals `#818181`, increase `#008443`, gridlines `#e4e4e4` on rows only, the current week `#f2f2f2`, ticks `#707070` at 12px, plot background `#ffffff`, square bar ends. The sample's Figure 2 in five forms is in the workbench of the live sample; `bridge.csv` is its data.


## Do's and Don'ts

- Do open with the finding sentence, the price sign and five compare boxes against plan with last week in parentheses. Don't lead with a chart or a dozen KPI tiles.
- Do make every device readable first: write pump prices to a tenth of a cent but round everything else to a readable unit that adds up, put a bar beside every size that is compared, and turn the sign's parts into data (the head carries the main grade against the street, the base band the site count and posting time). Don't keep a device that reads worse than a plain bar or table.
- Do compare against plan as well as last week, rank the shortfalls with their likely cause beside them, and say what to do (staff, fill, fix, reprice). Don't report change alone.
- Do frame the page with the canopy's red bar and the slides' yellow rules, red chart titles and compare boxes. Don't add shadows, gradients, rounded cards or photos.
- Do keep red for what the title names and everything else gray; let the bridge carry green and red with parentheses. Don't put the brand red or Shell yellow on data.
- Do draw the corridor map as a schematic: invented bends, distances from the exit numbers, no terrain or city names, and say so in the note. Don't use a real map, a route shield or a real station.
- Do end panels in one row on one line. Don't stretch a chart to an odd height to get there; change the layout instead.
- Do title each panel with its finding and explain the method in the note band and the footnotes (`[A]`). Don't title a chart with its measure alone.
- Do write money, units and dates the Shell way (`$3.55⁶/gal`, `¢/gal`, `main grade`, `(Wk 43: x)`). Don't use the pecten, the Shell typeface, a real site or a real price.
- Do keep at most seven views in a section. Don't add a card only to show a token.


## Agent Prompt Guide

Install the style (`npx @vizney/styles@latest add shell`, `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- shell`, or unzip the package in the project root). Agents that read skills load `dashboard-style` on their own and work in one of three modes: **Build** (plan the views, then draw them to this file), **Restyle** (move an existing screen onto this file without changing its data) and **Review** (a table of rule, finding, severity and fix). For an agent without skills, start the prompt with `Read DASHBOARD.md and follow it exactly.` For example:

```
Read DASHBOARD.md and follow it exactly. Build our weekly mobility report as one self-contained HTML file with
fictional data, in English and Korean (?lang=en|ko, English by default), on the white page the spec describes.
Top: a white canopy band with "Vizney Energy |" in red, the period and the report name, the EN/KO toggle, a dark
Export PDF and a yellow Copy as Markdown; a 6px red bar; the corridor menu as the filter for every view, kept in the URL.
This week: the price sign as a pillar (yellow head with the main grade against the street, a red bar, a dark price zone
with one row per grade and the posted price to a tenth of a cent, a gray base band), then the finding headline, a lede,
a yellow rule, five compare boxes against plan with "(Wk 43: x)", and three key price markers. Both columns end on one line.
Against plan: the gross margin bridge (gray totals cut at a break, green and red steps, negatives in parentheses) and
the sites against plan as a ranked exception list with the price against the street beside it.
Forecourt operations: busy hours, tanks under 2 days of supply, charge points under 97% uptime.
Sites: a schematic corridor map with the sites as small price-sign pins and alert badges, a zoom on the selected site's
2-mile street with competitors' prices and what to do; then the results table collapsed to corridor totals.
Every view on the same panel: figure label, finding title, yellow rule, red chart title with the unit, keys, view,
note band. At most seven views per section. Use only the values in Data Colors, the formats in Numbers, Dates & Units
and the components in Component Stylings. Every chart, list and the map need a tooltip, keyboard control and a
screen-reader table.
```

Before it is done, the agent checks:
- [ ] The headline is the finding; the price sign shows every grade to a tenth of a cent with its change and margin; the five compare boxes carry a signed change against plan or target in good (`#007a3d`) or bad (`#c4161c`) and last week in parentheses.
- [ ] Every view sits on a white panel (1px `#e4e4e4`) with a yellow rule under the title, a red chart title with the unit and a note band; every card title states a finding.
- [ ] Red `#e03a35` only for what each title names and the rest gray; the bridge in gray, green and red with parentheses; no `#dd1d21` or yellow on data.
- [ ] Plan appears where it matters (the KPIs, Figure 1, the bridge, the sites, the table), and the shortfalls are ranked and named with their likely cause and the action.
- [ ] The map is schematic and says so; pins, tags and labels never overlap; the zoom's numbers match the table.
- [ ] Gridlines on rows only; line ends labeled; no dual axis, pie, donut, gauge, gradient or photo.
- [ ] Numbers, dates, hours and money follow the formats in both languages; tables and bridges add up.
- [ ] Panels side by side end on one line at 1440, 1280 and 1024px without a stretched chart; nothing breaks at 390px.
- [ ] Text ≥ 4.5:1; marks below 3:1 have a second cue; every view has a tooltip, keyboard control and a data table; the filter changes every card.
