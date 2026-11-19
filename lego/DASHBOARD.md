---
name: LEGO® style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 8
tagline: Colorful, Stacked, Playful
tagline_ko: 알록달록, 쌓기, 즐거움
source: https://www.lego.com/en-us, https://www.lego.com/en-us/categories/sales-and-deals, https://www.lego.com/en-us/black-friday, https://www.lego.com/en-us/insiders-weekend-deals, https://www.lego.com/en-us/product/venetian-neighborhood-11388, https://www.lego.com/cdn/cs/aboutus/assets/blt1587fc5fdc823ffb/2025_Performance_Highlights.pdf, https://www.lego.com/en-us/legal/notices-and-policies/fair-play/
sample: https://styles.vizney.com/lego/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#ffffff"
  header: "#ffd502"
  line: "#d9d9d9"
  hair: "#ececec"
  rule: "#2c2c2c"
  ink: "#2c2c2c"
  body: "#3d3d3d"
  text-2: "#636363"
  muted: "#636363"
  pill: "#f2f2f2"
  button: "#f47d20"
  button-text: "#141414"
  side: "#f4f4f4"
  baseplate: "#c9c9c9"
  focus: "#141414"
  sale: "#dd0000"
  sale-text: "#bd0000"
  near: "#fff1b0"
data:
  categorical: ["#1e5aa8", "#e05a00", "#f7c600"]
  other: "#a3a3a3"
  comparison: "#8a8a8a"
  categorical_text: ["#1e5aa8", "#b04f00", "#2c2c2c"]
  sequential: ["#89b5f2", "#6f9edf", "#5587cd", "#3a70ba", "#1e5aa8"]
  diverging: ["#e05a00", "#ea7f4e", "#f3a07d", "#e8e8e8", "#89b5f2", "#5587cd", "#1e5aa8"]
  good: "#1e5aa8"
  bad: "#bd0000"
typography:
  sans: { en: "Gantari", ko: "Noto Sans KR" }
  mono: "Roboto Mono"
radius: {card: "8px", pill: "999px", badge: "4px", chip: "2px", age: "4px", tooltip: "8px", brick: "2px", stud: "1px", cell: "2px (heatmap tiles)"}
spacing: {page: "32px (24px under 1360px, 16px under 640px)", gap: "16px (12px under 640px)", section: "56px (44px under 640px)", card: "16px 20px 14px", kpi: "12px 18px 13px", cell: "9px 10px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: lego.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: event.csv}
---

# LEGO® style — DASHBOARD.md

**Colorful, Stacked, Playful** · 알록달록, 쌓기, 즐거움

A dashboard design spec read from the way LEGO® shows a number to a shopper and from the bricks themselves: results drawn as columns of stacked bricks, the yellow header band and the badges of lego.com, the red % OFF tag beside a struck-out price, the box line `18+ | set | pieces`, and the gifts with purchase that step up with the basket at Black Friday. It turns those parts into a bright, working event plan on a white page, with the values, rules and checks an AI coding agent, Tableau or Power BI needs to rebuild it.

```
npx @vizney/styles@latest add lego
# or, without Node:
curl -fsSL https://styles.vizney.com/install.sh | sh -s -- lego
```

That puts `DASHBOARD.md` in the project root and the `dashboard-style` agent skill (build, restyle, review) in `.claude/skills/dashboard-style/`, together with `tokens.css`, `tokens.json`, `lego.tps`, `powerbi-theme.json` and `prompt.md`. Coding agents that read skills pick it up whenever a task touches a dashboard or a chart; any other agent can be told to follow `DASHBOARD.md`.

- Live sample: https://styles.vizney.com/lego/?lang=en (Korean `?lang=ko`; one channel `&channel=online` or `&channel=stores`)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/lego/DASHBOARD.md
- Package: [lego-dashboard-style.zip](lego-dashboard-style.zip) (unzip in your project root) · the skill: [skill/SKILL.md](skill/SKILL.md)
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [lego.tps](lego.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [event.csv](event.csv) (the data behind the sample's Figure 1)
- Blog post: [English](https://www.vizney.com/style-lego/) · [한국어](https://kr.vizney.com/style-lego/)
- Catalog: VIZNEY STYLES · 08 · https://styles.vizney.com (Vizney Styles is a line of [Vizney](https://www.vizney.com))

Not an official LEGO® design, and not affiliated with or endorsed by the LEGO Group. A reference style read from the publicly visible design of lego.com and public touchpoints such as the bricks, LEGO® stores, the Black Friday offers and annual reports; it carries no logo, typeface, photo or data of theirs. LEGO® is a trademark of the LEGO Group of companies which does not sponsor, authorize or endorse this site. The sample's company, Vizney Toys, its sets, offers and all its numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A toy shop on its biggest weekend. The page is white, the header is the lego.com yellow, the boxes are white with a 1px `#d9d9d9` line and 8px corners, and the numbers are big: KPI values in 52px, the plan in 30px over its tower. Colour is brick colour, given by job and used generously inside the figures: **blue** for shoppers, **orange** for offers, **yellow** for sets, **grey** for past events. Red is lego.com's sale red and appears only on % OFF badges and shortfalls.

Three devices carry the report, and each holds data:

- **Stack — brick towers (Figure 1).** What each event added over the year before, as towers of flat grey bricks on a grey baseplate at 0, a full brick a fixed number of sets. This year's plan is then built one brick per driver, each brick starting where the last one ended, with a dashed brick for what a driver takes off, and finished as a wide tower of clear bricks with the total in a yellow badge. The towers read like the LEGO Group's results drawn as columns of bricks.
- **Sale tags (Figure 2, the KPI row, Table 1).** The lego.com shop's tags become labels and number formats: an offer's badge (yellow Gift with purchase, red 20% OFF) names its row, and its effect is a long flat brick with one stud per 5 sets; the offer cost in the KPI row is written like a price, this year's value big with last year's struck out beside it; hero sets carry the badge, the red sale price and the struck-out price.
- **Gift ladder (Figure 3).** Gifts with purchase at set basket values: last year's orders as $10 basket bars, coloured darker orange the more gift steps they reach, a yellow badge flag on each step with the share of orders that reach it, and a pale yellow band under the $20 below each step.

Two plainer views finish the plan: orders by hour over the six event days with this year's actions as numbered yellow badges (Figure 4), and the hero sets by stock against demand (Table 1). The rest stays calm so the devices stand out: no shadows, no gradients, no photos, no minifigures, no lettering on studs.

Measured in a browser on November 14–15 and 18, 2026 on lego.com (US home, product pages, the Sale page, the Black Friday 2026 page, the Insiders Weekend page) and in the LEGO Group's performance highlights: header band `#ffd502` (60px on the site) with `#2c2c2c` text; product tiles white with a 1px `#d9d9d9` line and 8px corners; badges 24px high with 4px corners and a 1px white edge, yellow `#ffd502` with `#141414` text (New, Exclusives, Retiring soon) and red `#dd0000` with white 700 text (20% OFF); the sale price `#bd0000` 16px/700 beside the struck-out price in `#141414`; Add to Bag `#f47d20` with `#141414` text; Filter and Sort pills `#f2f2f2`; element IDs 12px `#636363`. The site's typeface Cera Pro is not used (Gantari stands in; Korean uses Noto Sans KR, as lego.com/ko-kr does). The Sale page's dark red and the Black Friday page's black-and-red brick lettering are not used.


## Color Palette & Roles

| Token | Hex | Role |
|---|---|---|
| canvas | `#ffffff` | Page, boxes and the plot |
| header | `#ffd502` | The 56px header band, the date badge, the plan badge in Figure 1, the gift-step flags in Figure 3, the numbered plan badges in Figure 4. Only ink on it (`#141414` 13.0:1) |
| line | `#d9d9d9` | 1px box outlines; no shadows on boxes |
| hair | `#ececec` | Gridlines and table row rules |
| rule | `#2c2c2c` | 1.5px rule under table heads |
| ink | `#2c2c2c` | Titles, values, the selected pill (white text 14.0:1), step lines in Figure 3, the plan's edge in Figure 1, plan outlines in Figure 4 |
| body | `#3d3d3d` | Body text (10.9:1) |
| text-2 | `#636363` | Labels, table heads and keys (6.0:1) |
| muted | `#636363` | Subtitles, notes, axis ticks, set numbers (6.0:1) |
| pill | `#f2f2f2` | Filter pills and secondary buttons, 999px corners |
| button | `#f47d20` | The one primary pill (Get one made), text `#141414` 6.8:1 |
| baseplate | `#c9c9c9` | The 4px baseplate under Figure 1: the zero line |
| sale | `#dd0000` | % OFF badges and shortfall badges, white 700 text (5.2:1) |
| sale-text | `#bd0000` | Sale prices and shortfalls in text (6.6:1) |
| near | `#fff1b0` | The band under the $20 before each gift step in Figure 3; never under text |
| focus | `#141414` | Focus ring, 2px with a 2px offset |


## Data Colors

Validated with the dataviz `validate_palette.js` (OKLab, `--mode light`) on `#ffffff`, where every chart sits.

| Job | Values | Text step (≥ 4.5:1) |
|---|---|---|
| Categorical (brick colours by job) | shoppers `#1e5aa8` · offers `#e05a00` · sets `#f7c600` (edge `#b38f00`) · past events `#a3a3a3` | `#1e5aa8` · `#b04f00` · `#2c2c2c` · `#636363` |
| Gift steps (Figure 3) | no gift `#a3a3a3` · gift 1 `#f3a07d` · gift 2 `#ea7f4e` · gift 3 `#e05a00` | — |
| Sequential (Figure 4) | under 0.1% `#f2f2f2`, then `#89b5f2` `#6f9edf` `#5587cd` `#3a70ba` `#1e5aa8` | — |
| Diverging (for tools) | `#e05a00` `#ea7f4e` `#f3a07d` · `#e8e8e8` · `#89b5f2` `#5587cd` `#1e5aa8` | — |
| Status | good `#1e5aa8` · bad `#bd0000` · neutral `#a3a3a3` | `#1e5aa8` · `#bd0000` |

- The four categorical colours with `--pairs all`: worst colour-vision ΔE 15.1 (grey and orange, deutan), worst normal-vision ΔE 20.2. Yellow sits above the lightness band on purpose (L 0.85) and grey has no chroma on purpose: yellow bricks always carry a 1px `#b38f00` edge and a value, and grey means past events only.
- The blue ramp and the gift steps pass `--ordinal` (one hue, monotone, every step ΔL ≥ 0.06, light end 2.0:1 on white). The diverging arms pass `--ordinal` separately and their mirrored steps differ by ΔE 16.4, 19.9 and 24.4 under colour-vision deficiency.
- One meaning per colour across the page. Blue is also the colour of a good change (▲ 17%, ▼ 2.8 pts cost); a bad change is red with its sign. Orange text uses `#b04f00`. Values and labels stay in ink; a coloured mark beside them carries the meaning.
- Red is not a data colour: it is the sale badge and the shortfall (a dashed red brick in the coverage bar, red text, a red badge in the KPI row).


## Typography Rules

| Role | English | Korean |
|---|---|---|
| Every word and number | Gantari 400–800 | Noto Sans KR 400–800 |
| Code and file names | Roboto Mono 400/500 | Roboto Mono |

One body face per language, never mixed on one screen. Numerals are tabular in KPIs, tables and axes.

| Size | Value |
|---|---|
| Headline | 30px/800, line-height 1.22 (Korean 28px/700); 24px under 640px |
| KPI value | 52px/800 tabular (Korean 700); 46px under 1360px (42px at 1200–1279px), 34px under 640px; unit 22px/700 beside it; label 14px/600 above; change 13.5px under |
| Card title | 19px/700 (Korean 18px); the figure number above it 12.5px/700 muted |
| Figure 1 values | drivers 14.5px/800, past events 13px (the last year 700), the plan 30px/800 under a 24px badge; names 12.5px on up to two lines |
| Figure 2 | badges 12.5px in 24px; where the offer applies 12.5px muted; values 26px/800 with `sets` 13px muted on the first row |
| Figure 3 | flags 12px/700 in 22px badges; the share that reaches each step 20px/800 with `reach it` 12.5px muted |
| Table | name 15px/700; box line 12.5px (age 11.5px/700 in a 1.5px outlined box with 4px corners); numbers 16px/700; prices 15px/700 |
| Body | 15px/400 (Korean 14.5px) |
| Notes | 12.5px/400 |

Load the fonts as in Tool Mapping. Never Cera Pro, the LEGO wordmark or any lettering made of bricks.


## Numbers, Dates & Units

| What | English | Korean |
|---|---|---|
| Sets | `70K` · `2.90M` | `7만` · `290만`; under 10K in 천: `9천` |
| Added or taken off | `+150K` · `−200K` | `+15만` · `−20만` |
| Money, large | `$149M` | `1.49억 달러`; under 100M `9,912만 달러` |
| Prices | `$249.99`, sale `$103.99` with `$129.99` struck out | `249.99달러`, `103.99달러` |
| Percent | titles and changes whole: `17%`; shares and cost one decimal: `6.4%` | same |
| Points of a share | `▼ 2.8 pts` | `▼ 2.8%p` |
| Orders | `110.9K` | `11.1만` |
| Basket bins | `$90–99` · `$300 and over` | `90~99달러` · `300달러 이상` |
| Hours | axis `12a 3a 6a … 9p`; in text `7 am` | axis `0시 3시 …`; in text `오전 7시`, `자정` |
| Event days | `Members' Sat` · `Black Friday` · `Cyber Monday` | `회원 토요일` · `블랙프라이데이` · `사이버먼데이` |
| Dates | `Nov 21–22` · `Plan · Nov 9` | `11월 21~22일` · `11월 9일 기준` |
| Box line | `18+ | V3104 | 3,412 pcs` | `18+ | V3104 | 부품 3,412개` |

- ▲ ▼ before every change, a true minus (−), the unit never wrapping away from the number (no-break space). Korean glues a number to the word after it with a word joiner.


## Layout Principles

- Page 1400px wide at most, 32px side padding (24px under 1360px, 16px under 640px), 16px between boxes, 56px between sections.
- Header: a 56px yellow band with the company in 19px/800 and the report name in 17px/500 on the left, the EN/KO pill in white on the right.
- Under it, one line: a strip with the yellow `Plan · Nov 9` badge and the event dates divided by thin rules, and the channel filter on the right (`All channels | Online | Brand stores`, pills on `#f2f2f2`, the selected one ink with white text). The filter changes every card and is kept in the URL (`?channel=online`).
- Then the result in one sentence, then the KPI row: four white boxes (Black Friday target, revenue target, offer cost with last year struck out, hero sets ready with a red shortfall badge).
- First screen (1440 × 810): Figure 1, the brick towers | Figure 2, the sale tags (560px). Bottoms on one line.
- `Running the event`: Figure 3, the gift ladder | Figure 4, orders by hour with the plan; then Table 1, the hero sets, least covered first, eight rows and the rest on demand.
- Every figure and table is one box with one anatomy: figure number → the finding as the title → a subtitle with the method → keys → the view → a note.


## Component Stylings

**Header and strip.** The band is `#ffd502` with ink text only. Badges are 24px high, 4px corners, 1px white edge, 12.5px text, 12px side padding: yellow with `#141414` 600, red `#dd0000` with white 700, white with a 1px ink edge (points), `#f2f2f2` (shipping).

**KPI boxes.** White, 1px `#d9d9d9`, 8px corners, 12px 18px 13px padding: the label, the value with its unit, the change (`▲ 17% vs 2025` in the good blue, 700). A cost that falls is written like a sale price: `6.4%` big and `9.2%` struck out in 22px/700 `#141414` beside it. A shortfall is a red badge (`3 short`) followed by its words.

**Brick towers (Figure 1).**
- A 4px `#c9c9c9` baseplate at 0 under the whole plot; row gridlines `#ececec` with signed ticks (`+200K`) on the left.
- Columns: the last three events (two under 600px), the six drivers, then the plan, 1.8 columns wide.
- A past event is a tower of grey `#a3a3a3` bricks: a full brick is 100K sets for all channels and online, 50K for stores (one unit chosen so the tallest tower has at most seven bricks); bricks 2px apart, 2px corners; a top brick smaller than 35% of a full one joins the brick below.
- A driver is one brick, starting where the last driver ended: shoppers `#1e5aa8`, offers `#e05a00`, new sets `#f7c600` with a 1px `#b38f00` edge. A driver that takes sets off is a white brick with a 2px `#e05a00` dashed edge (`5 3`) and dashed studs, its value under it.
- The plan is a tower of white bricks with a 2px `#2c2c2c` edge and four studs, its value (`+420K`) in 30px/800 over it and a yellow badge above with the total (`2.90M in total`). When the value would cross a neighbouring column, it rises above that column's bricks and value.
- Studs: two flat ones on each column's top brick (four on the plan), as wide as a quarter of the column up to 12px, 4px high, 1px corners, overlapping the brick by 1px.
- Connectors: 1px `#8a8a8a` dashed (`2 2`) lines at the running total between drivers and on to the plan.
- A value over every column, signed; a later value that would sit on another rises above it. Names under the axis: years, driver names on up to two lines (11px or a short name when they would be cut; at an angle under 400px), the plan in bold.

**Sale tags (Figure 2).** One row per offer, in order of effect: the lego.com badge with the offer's name, where it applies under it in 12.5px muted, then a flat brick as long as the extra sets per $1,000 of offer cost with one stud per 5 complete sets (studs at most 14px wide, 5px high), orange `#e05a00` when the offer is in the plan and grey `#a3a3a3` when it is dropped, and the value at its end in 26px/800. Keys: `In the plan` and `Dropped`. The note says what a stud is.

**Gift ladder (Figure 3).** $10 basket bars with 2px gaps and 2px corners on a 1px ink baseline, coloured by the gift step reached; the open last bin (`$300+`) half a bar apart. A `#fff1b0` band behind the two bins below each step. Each step is a 1.5px ink line from the baseline to a yellow badge flag at the top (`Gift 1 · $40`, or `$40` alone when the next step is too close) with the share of orders that reach it under the flag (`80%` 20px/800 + `reach it`). Row gridlines `#ececec`; the x axis every $50.

**Hours and plan (Figure 4).** Six rows (the event days, Black Friday in bold) by 24 hours; 1×1 tiles with 2px gaps and 2px corners filled by the share of event orders in that hour (cuts 0.1 · 0.4 · 0.8 · 1.2 · 1.8%). Each action in the plan outlines its tile or tiles in 2px `#141414` with a numbered 17px yellow circle at the top-right corner; the numbered list sits under the grid. The legend is the six tiles with the cuts under their borders.

**Hero sets (Table 1).** Head 12.5px/700 muted over a 1.5px ink rule; rows 9px 10px with `#ececec` rules. Set: the name, then the box line (age box | set | pieces). Offer: its badge, then the price (a red sale price with the struck-out price for a % OFF set). Demand and stock + inbound right-aligned. Covered: a 10px bar to 120% with a 1.5px ink tick at 100%, filled `#f7c600` with a `#b38f00` edge; a shortfall is a red `#bd0000` dashed outline from the fill to 100%, the share in red and `14K short` under it; otherwise `Ready` muted. Least covered first; eight rows and `Show all 12 sets`.

**Tooltip.** White, 1px `#bdbdbd`, 8px corners, a soft shadow (`0 6px 18px` at 14%), 9px 12px 10px padding; a bold head, a muted sub line, rows of swatch, value and label. It adds detail and is never the only copy of a number.

**Buttons.** Pills 40px with 999px corners: the one primary `#f47d20` with `#141414` text; secondary `#f2f2f2`. Code windows on `#f7f7f7` in Roboto Mono 12.5px (keyword `#901f76`, string `#007133`, number `#9c4f12`, function `#bd0000`, property `#1e5aa8`, highlight `#fff3b0`).


## Charts

- **Choose by the question.**
  - How big is the plan and is it ready → the result sentence and the KPI row (target and revenue against last year, offer cost against last year, hero sets ready).
  - How does the plan get there, and is it bigger than past events → the brick towers (Figure 1).
  - Which offers to run → the sale tags, extra sets per $1,000 (Figure 2).
  - Where to set the gift steps and which add-ons to push → the gift ladder (Figure 3).
  - When to open deals, send emails and staff the stores → orders by hour with the plan (Figure 4).
  - Which sets to restock → hero sets, least covered first (Table 1).
- **Titles.** The finding, recomputed for each channel: `The plan adds 420K sets, 2.5 times last year's 170K; gifts add the most`; `Gifts bring 46 extra sets per $1,000, 4.2 times as many as 30% off`; `36% of orders reach the $100 gift; 30% sit within $20 of a step`; `3 of 12 hero sets fall short of event demand; Clockwork Tower needs 14K more`.
- **Marks.** Bricks are flat: one fill, 2px apart, 2px corners, flat studs; no bevel, no highlight line, no shadow. Bars start at zero. A brick for a part of the plan never carries a different colour rule from the legend.
- **Axes.** Row gridlines `#ececec`, no axis lines except the baseplate and the histogram baseline; ticks 12px muted, signed where the chart shows change.
- **Labels.** A value on every brick column, on every offer, on every gift step. The heatmap has no numbers in its tiles; the tooltip and table give them.
- **One axis.** Never a dual axis. Sets and money are separate figures.
- **Never:** pie, donut, 3D, gradients, bevelled or shiny bricks, minifigures, the LEGO logo or lettering on studs, real sets, prices or gifts, the Black Friday page's black-and-red art, photos, or decoration that carries no number.
- Every figure and the table have a tooltip, keyboard control and a screen-reader table.


## Depth & Elevation

Flat. White boxes with a 1px `#d9d9d9` line on a white page; the yellow header is the only band of colour outside the data. The tooltip is the only element with a shadow.


## Interaction & Motion

- The channel pills filter every card; the URL keeps `?lang=` and `?channel=`. Language switches in place and only the language's own font is used.
- Every view responds to hover and to the keyboard: Tab to focus, arrow keys to move (columns, offers, $10 bins, hours, rows), Home and End, Esc to close; a polite live region reads the focused item.
- Motion (`cubic-bezier(.4,0,.2,1)`): bricks drop 0.34s from 14px above with a small settle, past towers brick by brick (70ms a column, 55ms a brick), the drivers after them, the plan last, then the values and badge fade in; Figure 2's bricks grow from the left 90ms apart; Figure 3's bars drop 18ms apart; Figure 4's tiles fade in by hour and day. With `prefers-reduced-motion` everything appears complete.


## Accessibility

- Text ≥ 4.5:1 on white: ink 14.0, body 10.9, muted 6.0, blue 6.8, orange text `#b04f00` 5.3, sale red `#bd0000` 6.6; white on `#dd0000` 5.2; `#141414` on `#ffd502` 13.0 and on `#f47d20` 6.8.
- Light marks (yellow `#f7c600` 1.6:1, grey `#a3a3a3` 2.5:1, the light heat and gift steps 2.0:1) always carry an edge, a value or a table view.
- Changes and shortfalls never rely on colour alone: ▲ ▼, signs, words (`3 short`, `14K short`, `Ready`), the dashed outline.
- Every view has a screen-reader table; the focus ring is 2px `#141414` with a 2px offset; targets at least 32px high.


## Responsive Behavior

- ≥ 1360px: as described.
- 1200–1359px: 24px padding; the first screen 1fr | 520px; Figure 1 keeps the last two events and short names when its plot is narrower than 600px.
- Under 1200px: Figures 1 and 2, then 3 and 4, stack across the page; Figure 2 is as tall as its rows.
- Under 1024px: the KPI row 2 × 2.
- Under 900px: Table 1 drops stock + inbound.
- Under 640px: one column; the channel filter in three equal pills; Figure 1's names at an angle under 400px; Figure 2 drops the line under each badge; Table 1 keeps set, offer and covered, and prices wrap.
- Captured and checked at 1440, 1280, 1200, 1024, 640 and 390px in both languages, with no horizontal scroll and no text over text.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` (installed in `.claude/skills/dashboard-style/`; or copy the `colors` block from the front matter) and the fonts:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gantari:wght@400;500;600;700;800&family=Noto+Sans+KR:wght@400;500;600;700;800&family=Roboto+Mono:wght@400;500&display=swap">
```

Each figure is one SVG drawn over its box so the drawing never pushes the box taller. Bricks are `<rect>`s: a tower's bricks from `pieces(value, unit)`, inset 1px top and bottom for the 2px gap; studs are small `<rect>`s on the top brick. Badges are a `<rect>` with 4px corners and centred text sized from the measured label.

**Tableau.** Paste the `<color-palette>` elements of `lego.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette runs shoppers, offers, sets, then grey.
- Dashboard background `#ffffff`, a 56px `#ffd502` text object for the header, each sheet on white with a 1px `#d9d9d9` border, row gridlines `#ececec`, text `#3d3d3d`, headers `#636363`. Title each sheet with the finding.
- Brick towers: a Gantt bar from `event.csv` (`running_start`, size `added_k_sets`, colour `group`), past events and the plan from 0; fake the brick gaps with a reference line every 100K in `#ffffff` 2px; the plan with no fill and a 2px `#2c2c2c` border; the taken-off driver with a dashed border. Studs need a second shape mark and are optional.
- Sale tags: horizontal bars with the badge text as the row label; studs optional.
- Gift ladder: a histogram of basket value with $10 bins, colour by the step reached, reference lines at $40, $100 and $200 labelled with the share that reaches each.
- Hours: a highlight table (day × hour) on the blue palette; plan actions as a second, outlined mark.
- Formats: `0.00,,"M"`, `+0,"K";−0,"K"`, `$0.00`, `0.0%`; Korean workbooks `0,"만"`. Fonts: Tableau Book unless Gantari is installed on every viewing machine and the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json`. It sets the data colours (shoppers, offers, sets, then grey), white visuals with a 1px `#d9d9d9` border and 8px corners, axis and gridline colours and text classes. Install Gantari on authoring and viewing machines or accept Segoe UI.
- Brick towers: a waterfall chart (category `bar`, Y `added_k_sets`) with increase colours by group and the total as a white column with an ink border, beside a column chart for past events in `#a3a3a3`. Studs are not available; leave them out.
- Sale tags: a bar chart with conditional colour (in the plan / dropped) and data labels; badges as a text column with conditional background.
- Gift ladder: a column chart by $10 bin with conditional colour by step and constant lines at the steps; hours: a matrix with conditional background on the blue steps.
- Title each visual with the finding; the method in the subtitle.

**Chart libraries (D3, Observable Plot, Vega-Lite, matplotlib).** Background `#ffffff`; shoppers `#1e5aa8`, offers `#e05a00`, sets `#f7c600` with a `#b38f00` edge, past `#a3a3a3`; gridlines `#ececec`; text `#3d3d3d`, ticks `#636363`; gift steps `#a3a3a3 #f3a07d #ea7f4e #e05a00`; sequential `#89b5f2 #6f9edf #5587cd #3a70ba #1e5aa8`; good `#1e5aa8`, bad `#bd0000`.


## Do's and Don'ts

| Do | Don't |
|---|---|
| Give each brick colour one job (blue shoppers, orange offers, yellow sets, grey past) | Paint bars in the header yellow or cycle brick colours by rank |
| Build a total brick by brick, each brick from where the last ended | Stack bricks that do not add up, or draw thin slivers on a total's axis |
| Keep bricks flat: one fill, 2px gaps, flat studs | Add bevels, shine, shadows or lettering on studs |
| Use the lego.com badge and price formats (yellow badge, red % OFF, struck-out price) | Use red for anything but sale badges and shortfalls |
| Put a value on every brick column and every offer | Make the reader count bricks or studs to get a number |
| Make the numbers big and the boxes white | Fill the page with colour outside the data |
| Use the LEGO® name only to say where the look was read from, with the notice | Use the logo, minifigures, Cera Pro, real sets, prices or gifts |


## Agent Prompt Guide

Install the style (`npx @vizney/styles@latest add lego`, `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- lego`, or unzip the package in the project root). Agents that read skills load `dashboard-style` on their own and work in one of three modes: **Build**, **Restyle** and **Review**. Other agents can be given this prompt:

```
Read DASHBOARD.md and follow it exactly. Build our Black Friday plan dashboard as one self-contained HTML file with
fictional data, in English and Korean (?lang=en|ko, English by default), on the white page the spec describes.
Header: a 56px #ffd502 band with the company and report name and the EN/KO pill. Under it the strip (a yellow
"Plan · Nov 9" badge and the event dates) and the channel pills (All channels | Online | Brand stores, the filter for
every card, kept in the URL). Then the result in one sentence and four KPI boxes with 52px values: target, revenue,
offer cost with last year struck out, hero sets ready with a red shortfall badge.
First screen: Figure 1, brick towers of the sets each event added over the year before, then this year's drivers brick
by brick (shoppers #1e5aa8, offers #e05a00, new sets #f7c600, a dashed brick for what is taken off) and a wide clear
plan tower with its value in 30px under a yellow badge with the total; beside it Figure 2, the offers as lego.com sale
tags with a brick of extra sets per $1,000, one stud per 5 sets, orange in the plan and grey dropped.
Running the event: Figure 3, last year's baskets in $10 bars coloured by the gift step reached, with yellow badge
flags and the share that reaches each step; Figure 4, orders by hour over the six days in five blues with the plan as
numbered yellow badges; Table 1, the hero sets with the box line, offer badge, price, demand, stock and coverage.
Every view in the same box: figure number, finding title, subtitle, keys, view, note. Use only the values in Data
Colors, the formats in Numbers, Dates & Units and the components in Component Stylings. Every view needs a tooltip,
keyboard control and a screen-reader table.
```

Before it is done, the agent checks:
- [ ] The headline and every title state the finding and change with the channel filter.
- [ ] KPI values are 52px with ▲ ▼ changes in blue when good and red when bad; a falling cost shows last year struck out.
- [ ] Figure 1 starts at a grey baseplate at 0; past towers are grey bricks of one unit; each driver starts where the last ended; the plan is clear with a 2px ink edge, a 30px value and a yellow total badge.
- [ ] Bricks are flat, 2px apart, with two flat studs on top; a brick taken off is a dashed outline.
- [ ] Figure 2's bricks are as long as their values with one stud per 5 sets; every row has its lego.com badge.
- [ ] Figure 3's bars are coloured by the gift step reached, with flags, shares and the $20 bands.
- [ ] Red appears only on % OFF badges and shortfalls; yellow marks carry a `#b38f00` edge or a value.
- [ ] Boxes side by side end on one line at 1440 and 1280px; nothing breaks or overlaps at 390px.
- [ ] Text ≥ 4.5:1; every view has a tooltip, keyboard control and a data table.
- [ ] No logo, Cera Pro, minifigure, photo, real set, price or gift, and the LEGO® notice is on the screen.
