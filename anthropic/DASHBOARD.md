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
  plot: "#ffffff"
  tint: "#e4edf8"
  ink: "#141413"
  ink-2: "#30302e"
  body: "#3d3d3a"
  text-2: "#5e5d59"
  text-3: "#73726c"
  muted: "#87867f"
  cloud: "#b0aea5"
  hair: "#e8e6dc"
  hair-2: "#dedcd1"
  on-dark: "#faf9f5"
  on-dark-2: "#9c9a92"
  accent: "#d97757"
  accent-deep: "#c6613f"
  good: "#4e7a30"
  bad: "#b0453b"
  focus: "#2c84db"
data:
  categorical: ["#4f86c4", "#b8456e", "#a8862a"]
  other: "#8f8d86"
  comparison: "#b0aea5"
  categorical_text: ["#2e6cae", "#a63c62", "#80661a"]
  sequential: ["#8ab5e6", "#5b97db", "#367ac2", "#215e9d", "#1d446e"]
  diverging: ["#225994", "#5078a7", "#7b97b9", "#b8b5aa", "#bf8091", "#ac5571", "#972552"]
  good: "#4e7a30"
  bad: "#b0453b"
typography:
  serif: { en: "Source Serif 4", ko: "Noto Serif KR" }
  sans: { en: "Inter", ko: "Noto Sans KR" }
  mono: "JetBrains Mono"
radius: {card: "16px", plot: "12px", button: "10px", pill: "999px", tooltip: "8px", badge: "4px"}
spacing: {page: "32px", gap: "16px", card: "28px", row: "10px 0", footer: "26px 32px 28px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: anthropic.tps, powerbi: powerbi-theme.json, prompts: prompt.md}
---

# Anthropic style — DASHBOARD.md

**Ivory, Editorial, Quiet** · 아이보리, 에디토리얼, 고요함

A dashboard design spec read from the public design of anthropic.com and claude.com — the measured tokens of the sites, and the way Anthropic itself presents data in its research posts and model announcements — extended with everything a dashboard needs that a website spec does not: validated data colors, the anatomy of each component, chart rules, number and date formats in English and Korean, density, filters, accessibility, and the settings that carry it into Tableau, Power BI and the web. Give this file to an AI coding agent (keep it in the repository root as `DASHBOARD.md`) or hand it to whoever builds your dashboards, and the screens come out looking like the live sample.

- Live sample: https://styles.vizney.com/anthropic/ (add `?lang=ko` for Korean)
- Raw file for your repository: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/anthropic/DASHBOARD.md
- Files in the same folder: [tokens.json](tokens.json) (source of every value here), [tokens.css](tokens.css), [anthropic.tps](anthropic.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.html)
- Catalog: https://styles.vizney.com · Vizney Styles 01

Not an official Anthropic design, and not affiliated with or endorsed by Anthropic. This is an independent reading of publicly visible design; it carries no logo, wordmark, typeface, image or data of theirs, and the sample's publisher and numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A warm ivory page that reads like a research post, not a cockpit. Anthropic presents data the way its research team does: a bold lead sentence that runs into serif prose, a short list of key findings, figures whose titles state the finding and whose captions start with *Note:*, tables ruled with thin ink lines, and footnotes. The dashboard keeps that grammar. Surfaces are flat ivory cards with no borders or shadows; depth is a ladder of warm grays; the serif appears in one statement and the findings, everything else is a clean sans at 600–700 for titles. Charts sit on a white plot panel inside the card, lines end in written labels, and the brand's clay appears only as a marker — never as a data series. The impression is editorial and calm: a report you would read.

Measured on the sites (October 2026): header 84px; container 1400px with 32px margins; cards `#f5f4ed`, 16px radius, 32px padding; primary button ink with ivory text, 10px radius, 36px tall; nav items as 28px pills; body gray ladder `#faf9f5 → #f5f4ed → #f0eee6 → #e8e6dc → #dedcd1 … #141413`; the serif reserved for the hero sentence (sans 600 for the first sentence, serif 400 for the rest), sans 600–700 for every heading; research figures captioned `**Finding sentence.** Note: method`, with a small `FIGURE 2` label in the margin; benchmark tables ruled with 1px ink lines, the subject column tinted with a colored top rule, `—` for missing values.


## Color Palette & Roles

Surfaces and text are the site's warm gray ladder. There is one brand accent, clay, and it is kept away from data. Green and red exist only as change text.

| Token | Hex | Role |
|---|---|---|
| canvas | `#faf9f5` | page background |
| card | `#f5f4ed` | cards, pills, tertiary buttons; no border, no shadow |
| card-2 | `#f0eee6` | secondary panels, segmented-control tracks |
| plot | `#ffffff` | the white plot panel inside a figure card |
| tint | `#e4edf8` | the subject column of a table (light periwinkle) |
| ink / ink-2 | `#141413` / `#30302e` | titles, figures, table rules, primary button, footer, tooltips / card descriptions |
| body | `#3d3d3a` | running text; primary button hover |
| text-2 | `#5e5d59` | labels, captions, notes, meta values, end-label values (6.0:1 on card) |
| muted | `#87867f` | figure labels, axis ticks, report id (3.3:1 on card; never for body text) |
| cloud | `#b0aea5` | dashed reference and comparison lines |
| hair / hair-2 | `#e8e6dc` / `#dedcd1` | dividers, pill borders, secondary button fill, gridlines / key–value rules, crosshair |
| on-dark / on-dark-2 | `#faf9f5` / `#9c9a92` | text on ink / secondary text on ink |
| accent / accent-deep | `#d97757` / `#c6613f` | clay: the "New" badge and markers / badge text, a clay button if one is ever needed |
| good / bad | `#4e7a30` / `#b0453b` | favourable / unfavourable change, text only (4.6:1 / 5.1:1 on card) |
| focus | `#2c84db` | focus ring (the site's `--color-focus`) |

Rules:
- No cool grays. The only pure white is the plot panel.
- Clay is a brand mark, not a data color. One clay element per screen is plenty: the badge on a new item, a marker, or the one clay button a page may have.
- Text may wear a series color only as a line's end label (the darker *text* step of that color), never for values or body text.


## Data Colors

Anthropic's own research charts lead with a sky blue and a fig pink, add olive, clay and amber for further series, label every line at its end in the series color, and draw reference lines dashed gray. This palette follows that family but uses deeper values that pass an OKLab validator for color-vision-deficiency separation, normal-vision separation and contrast on the white plot panel and the card. Use them exactly as listed; do not generate tints.

**Categorical** (identity on one mark), in fixed order, never cycled:

| Slot | Name | Line / fill | Label text |
|---|---|---|---|
| 1 | sky | `#4f86c4` | `#2e6cae` |
| 2 | fig | `#b8456e` | `#a63c62` |
| 3 | amber | `#a8862a` | `#80661a` |
| Other | gray | `#8f8d86` | `#5e5d59` |

All checks pass on both surfaces: worst all-pairs ΔE 12.5 under CVD (amber↔fig, deutan), 20.1 normal vision; every color ≥ 3:1 on the plot. Lines are still always end-labeled. A fourth real category folds into Other, or the chart becomes small multiples. Color follows the entity, not its rank: when a filter removes a category, the survivors keep their colors (in the sample Fiction is always sky, Nonfiction fig, Children's amber).

**Comparison series** (prior year, all-imprints total, benchmark): `#b0aea5`, dashed 2px (7 on, 5 off), labeled at its end in ink. It is gray and dashed on purpose: context, not a category. Separation from the three hues: ΔE 16.0 / 18.5 / 14.8 under CVD, 18.7 / 24.7 / 15.3 normal vision. **Reference line** (target, parity): the same gray, 1px dashed 4/4, with its label written just above it at the left (`Target 12%`).

**Sequential** (magnitude, one hue, light → dark): `#8ab5e6` `#5b97db` `#367ac2` `#215e9d` `#1d446e`. Sky hue, monotone lightness, every step ≥ 0.06 ΔL apart, light end 2.14:1 on white.

**Diverging** (polarity around a baseline): `#225994` `#5078a7` `#7b97b9` — `#b8b5aa` — `#bf8091` `#ac5571` `#972552`. Sky below, fig above, a neutral warm gray in the middle. Each arm passes the ordinal checks; the poles are ΔE 11.9 apart under CVD, 21.7 normal.

**Status:** good `#4e7a30`, bad `#b0453b`, neutral `#87867f`. Status colors are reserved for change text; they never color a series.


## Typography Rules

One serif, one sans and one mono, with a Korean counterpart for the first two. A screen loads only the fonts of its language. The Korean sans is Noto Sans KR because that is what the brand's own Korean pages use.

| Role | English | Korean | Weights |
|---|---|---|---|
| Sans (everything) | Inter | Noto Sans KR | 400, 500, 600, 700 |
| Serif (statement, findings) | Source Serif 4 | Noto Serif KR | 400, 500 |
| Mono (figure/table labels, section numbers, ids) | JetBrains Mono | JetBrains Mono | 400, 500 |

- **The statement runs in:** the first sentence in sans 600, the rest of the paragraph in serif 400, both at `clamp(23px, 2.6vw, 36px)` / 1.28 with −0.01em tracking. This is the site's hero pattern and the only large serif on the page. Item titles inside it are italic in English (『 』 in Korean).
- **Headings are sans and heavy:** section and card titles 19–21px / 700; figure titles 17px / 600 and written as a finding ("Children's returns rose while fiction and nonfiction eased."). The serif is never bold.
- **Key findings** are serif 16px / 1.5 bullets under a sans 700 heading.
- **Figures** in key–value rows are sans 600 at 17px (14px / 500 inside cards), `tabular-nums`; units (억, 만, 부, %, ₩, M) sit next to the number at 12.5px in text-2.
- **Labels:** figure and table labels (`FIGURE 1`, `TABLE 1`, `18 TITLES`, `REPORT ID`) are mono 11px uppercase with 0.1em tracking in muted; meta rows (Published · Team · Period) 13px with the label in ink and the value in text-2; body 14px; table 13.5px; captions 12.5px; axis ticks 11px; end labels 12px / 600.
- Korean text breaks between words (`word-break: keep-all`); a money figure never breaks.


## Numbers, Dates & Units

- **Currency:** English `₩423M`, `₩4,375M`, `₩16,800` (whole won below a million); Korean `4.23억` in figures, `4억 2,300만 원` in sentences, `16,800원`. Axis ticks `350M` / `3.5억`. Never mix the two systems.
- **Counts:** thousands separators always (`27,300`). Korean adds the counter at the unit size (`27,300부`); English puts the noun in the label.
- **Percentages:** one decimal (`11.5%`). Differences between percentages are points: `−0.6 pts` in English, `−0.6%p` in Korean.
- **Change:** signed with a true minus (`−`, U+2212), one decimal, then the comparison (`+10.4% vs Oct 2025` · `+10.4% 전년 동월 대비`). The color follows whether the move is good for that metric: a falling return rate is green.
- **Multiples and missing values**, as on the site: `5.1×` with the multiplication sign; `—` (em dash) for a value that does not exist, with the reason in the note (`— marks an October release with no September sales`).
- **Qualifiers** go in parentheses after the value or in the axis title: `Cost per attempt (USD, log scale)`, `OSWorld 2.1 (offline subset)`.
- **Dates:** `Oct 31, 2026` / `2026년 10월 31일` in meta rows; `Oct 2026` / `2026년 10월` in prose; month ticks `Nov … Oct` / `11월 … 10월`, the current month in ink; `2026-08-19` only in mono table cells.
- **Alignment:** numbers right-aligned in tables (the site's launch tables left-align them; a dashboard is read down a column), `tabular-nums` everywhere numbers line up.


## Layout Principles

The page is laid out like one of the brand's research posts, with the parts of a dashboard taking the places of the post's parts.

- One column on the canvas, at most 1400px wide, 32px side padding (24px up to 1359px, 16px below 640px). No sidebar, no app chrome.
- **Header** (84px): the company name (16px / 600) and the report name beside it; on the right a period pill, the language toggle, a tertiary button (`Read in PDF`) and the one primary button (`Copy as markdown`). No logo.
- **Filter row** between two hairlines: 28px pills on the left, a basis note on the right. The selected pill is ink. The pills scope every figure, table and card below; cards never carry their own filters.
- **Title block:** meta row (`Published · Team · Period`) → the run-in statement → a section nav written `(1) Revenue (2) Titles (3) Imprints (4) Returns` with the report id in mono at the right. The numbered sections are real anchors.
- **Key findings card:** three or four serif bullets (left, 7 of 12 columns) beside the key figures as hairline key–value rows (right, 5 columns): label, figure, change. This replaces a row of KPI tiles.
- **Figure + table row:** Figure 1 (7 columns) beside Table 1 (5 columns); 6/6 between 1024 and 1199px; stacked below.
- **Entity cards:** one card per imprint (or region, product line…), three across, each with the site's card anatomy (below).
- **Figure + notes row:** Figure 2 (7) beside the Notes card (5): numbered method notes, sources, update time.
- **Footer:** the site's ink footer carries the catalog line, the sample note and the disclaimer.
- **Density:** laptop first. At 1440 × 900 the statement, the key findings and the top of Figure 1 are above the fold; at 1366 × 768 the statement and the findings are.
- Reading order: statement → findings and figures → figure 1 and table → entities → figure 2 and notes. Keep it; don't lead with a chart.


## Component Stylings

- **Card:** `card` fill, 16px radius, 28px padding (24 below 1360, 20 below 640), no border, no shadow, no hover change.
- **Figure card:** a mono label row (`FIGURE 1` left, the measure and unit right, e.g. `MONTHLY REVENUE · ₩`) → the title as a finding sentence (17px / 600) → the white plot panel (12px radius, 250px minimum) → a caption that starts with `Note:` in 12.5px text-2.
- **Table card:** the same label row (`TABLE 1` left, a count such as `18 TITLES` right) → a plain title → the table → a note that defines the measure and explains `—`.
- **Table:** 13.5px sans; every row ruled below with a 1px **ink** line (the site's launch tables), header 600 in ink; the subject column (this month) on the `tint` background with a 2px sky rule on top of its header; group label rows (`Fiction · top 2 of 6`) in 12px text-2 above a hair-2 rule; item rows show the title in ink with the author or owner on a second 12px line; a `New` badge (18px, 4px radius, 1px clay border, clay-deep text) marks items added this period; a progress cell is a 56 × 5px ink bar on a hair track with the percentage. No zebra striping, no hover tint.
- **Entity card** (the site's announcement card): eyebrow with an 8px dot in the entity's series color and `Imprint · October 2026` (13px text-2) → title 21px / 700 → one descriptive sentence (14px ink-2) → hairline key–value rows (13.5px label, 14px / 500 value, change beside it) → a full-width secondary button with an arrow (`Open imprint report →`). The selected entity gets a 3px top rule in its color, and its button becomes primary (`Back to all imprints`).
- **Key–value row:** label left, value right, change after the value; 1px hair-2 rules between rows, 10px vertical padding. The site uses it under every card title (`Model Details — Haiku →`).
- **Buttons** (measured on the site): 36px tall, 10px radius, 14px / 500, an icon after the label when it acts (arrow, download, copy). Primary: ink fill, ivory text, hover `body`. Secondary: hair fill, hair-2 border, ink-2 text. Tertiary: card fill, hair border, body text. Hover changes background only; nothing lifts.
- **Pills:** 28px, 999px radius, 13px, card fill with a hair border — the site's nav items. Used for filters (selected: ink fill, ivory text) and the period. The language toggle is a 28px segmented pill whose selected side is ink.
- **Badges:** 18px, 4px radius, 1px border, 11px / 500 (`New`).
- **Tooltip:** the app's: ink fill, ivory text, 8px radius, shadow `0 4px 16px rgba(20,20,19,.12)`, the only shadow on the page. An 11px title in on-dark-2, then one row per series: a line key (dashed for the comparison), the value in 600, the series name. It sits above, left, right or below the point, whichever fits the card, with its arrow on the point.
- **Toast:** the same ink box at the bottom centre, 2.2 seconds (`Report copied as markdown`).
- **Notes card:** `Notes` 19px / 700, a numbered list in 13px text-2, then `Sources:` and the update time at the bottom.
- **Footer:** ink, full bleed, 26 × 32px padding, 12.5px on-dark-2 text with the catalog line in ivory.


## Charts

Follow the brand's figure grammar before any chart library default.

- **Title says the finding**, caption says the method (`Note: …`), the measure and unit stand in the label row. A chart is never titled with its measure alone.
- **Choose by the question.** Change over time → line, 2.5px, no smoothing, at most three series plus a dashed comparison. Entity vs entity over time → one line per entity in its fixed color (Figure 2). Magnitude across categories → horizontal bars, one hue. Part of whole → one stacked bar with ≤ 3 colors plus Other. Ranking → the ruled table, not a chart. A single number → a key–value row or the statement.
- **One axis.** Never a dual axis. Two measures of different scale become two charts or an index.
- **Axes:** light gridlines (`hair`, 1px) at four or five nice ticks; tick labels 11px muted at the left; the bottom gridline in hair-2; five month ticks, the current month in ink (three ticks below 430px of plot width).
- **End labels instead of legends:** every line ends in a hollow 4px marker and a label `Name value` — the name in the series' text color at 12px / 600, the value in text-2. Labels push apart by 16px when they collide. Below 430px of plot width only the value is written.
- **Reference lines** (target, parity, an event date) are dashed cloud gray with their label written on the line.
- **Hover and keyboard** add a hairline crosshair, a 4.5px hollow dot on every series and the ink tooltip.
- **Don'ts:** no pie or donut, no 3D, no gradients, no area fills, no rainbow categories, no legend when end labels fit, no smoothing that overshoots the data, no clay series.


## Depth & Elevation

Flat. Cards have no border and no shadow; the page's depth is the ladder canvas → card → plot (white) and the ink footer. The tooltip and the toast are the only elements with a shadow. Nothing lifts on hover.


## Interaction & Motion

- On load the lines draw in (1.1s, `cubic-bezier(.165,.84,.44,1)` — the site's ease-out-quart); markers, end labels, findings, table rows and entity cards fade in with a short stagger. Changing a filter rewrites the statement, the findings, every figure title and every card the same way.
- Every chart has a hover tooltip, a keyboard mode (arrow keys step, Home and End jump, Esc clears, values announced through a live region) and a screen-reader table. Filter pills move with the arrow keys. Tables are real tables.
- `Copy as markdown` copies the whole report (statement, findings, key figures, tables, notes) as Markdown — the brand's own "Copy as markdown" utility — and confirms with a toast. `Read in PDF` prints.
- Button hovers change the background in 0.22s. On touch screens a tap picks a point and a tap elsewhere clears it.
- `prefers-reduced-motion` turns all motion off.


## Accessibility

- Text contrast: body and labels ≥ 4.5:1 on their surface (text-2 6.0:1 on card, good 4.6:1, bad 5.1:1, series label colors ≥ 4.9:1); muted (3.3:1) only for 11px labels and ticks.
- Marks: every categorical color is ≥ 3:1 on the plot; the comparison line (2.0:1) is always dashed and labeled, and every chart has a table.
- Identity is never color alone: end labels name every line; the comparison differs by dash; status is text with a sign.
- Focus ring `#2c84db`, 2px, 2px offset. Tab order: header controls → filter pills → sections in reading order.
- Live region for chart navigation; tables with `scope` on headers and on group label rows.


## Responsive Behavior

- ≥ 1360: the layout above. 1200–1359: 24px padding, 14px gap, 24px card padding.
- 1024–1199: figure and table (and figure and notes) share the row 6/6.
- 900–1023: figures, tables and notes stack full width; the three entity cards stay in one row.
- 640–899: entity cards stack; the header drops the report name and `Read in PDF`; the findings card stacks its two halves.
- < 640: 16px padding; the period pill and `Copy as markdown` leave the header; key–value rows put the change on a second line; the table hides the change column and wraps titles; charts write only values at line ends and three month ticks.
- Embedded in a post (`?embed=1`): the footer hides and the page reports its height to the host.


## Tool Mapping

**Web / AI coding agents.** Load `tokens.css` (or copy the `colors` block from the front matter). Fonts come from Google Fonts:
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+KR:wght@400;500;600;700&family=Noto+Serif+KR:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;1,8..60,400&display=swap`

**Tableau.** Import `anthropic.tps`: paste its `<color-palette>` elements into `My Tableau Repository/Preferences.tps` inside `<preferences>` and restart Tableau Desktop. Then: dashboard background `#faf9f5`; containers for cards with background `#f5f4ed` and 24–28px inner padding, no borders (Tableau has no radius); each chart worksheet on a white (`#ffffff`) background inside its card; worksheet titles bold 15–17px written as the finding, the method in the caption; marks: line size 2–2.5, markers off except the last point; axis ticks `#87867f` at 11px, gridlines `#e8e6dc`; the prior year as a dashed gray (`#b0aea5`) reference line or dual line; a dashed reference line for the target with its label; label the line ends ("Mark labels: Line ends"), legends off; number formats `₩#,##0,,M` / `#,##0.0%` / custom `+0.0%;−0.0%`. Fonts: Tableau Book for text, Source Serif 4 only when it is installed on every viewing machine and the server.

**Power BI.** Import `powerbi-theme.json` (View → Themes → Browse for themes). It sets data colors (use only the first four for categories), the ivory page, the card background with a white plot area, bold visual titles, text classes and axis colors. Install Inter on authoring and viewing machines or let it fall back to Segoe UI. Title each visual with the finding and put the method in the subtitle; turn legends off and label line ends with data labels on the last point; show key figures as a table or a multi-row card with hairlines rather than big-number tiles; use the good/bad colors only in conditional formatting of change measures.

**Datawrapper / Flourish / chart libraries.** Categorical `#4f86c4, #b8456e, #a8862a, #8f8d86` (labels `#2e6cae, #a63c62, #80661a`); comparison `#b0aea5` dashed; plot background `#ffffff` on a `#f5f4ed` card; text `#141413` / `#5e5d59`; gridlines `#e8e6dc`.


## Do's and Don'ts

- Do start the screen with the result in words — a bold sentence running into serif prose — and a short list of key findings. Don't lead with a chart or a row of KPI tiles.
- Do title every figure with its finding and caption it with `Note:`. Don't title a chart with the name of its measure.
- Do label line ends and drop the legend. Don't label every point.
- Do keep the brand's sky–fig–amber family for series and dashed gray for comparisons. Don't put clay on a data series, and never more than three colored categories plus Other.
- Do rule tables with thin ink lines and tint the subject column. Don't zebra-stripe or box cells.
- Do use the card anatomy (eyebrow → title → sentence → key–value rows → full-width button) for entities. Don't stack cards inside cards.
- Do keep headings sans and heavy, the serif regular. Don't use a bold serif or a serif for card titles.
- Don't use pies, donuts, dual axes, area fills, gradients, cool grays, pure-white cards, shadows, or a logo in the header.
- Don't invent tints: every color on a mark comes from the Data Colors section.


## Agent Prompt Guide

Put this file in the project root as `DASHBOARD.md` and keep `tokens.css` next to it. Then prompt, for example:

```
Build a monthly sales dashboard in the Anthropic style defined in DASHBOARD.md, laid out like a research post.
Open with a meta row (Published · Team · Period) and one run-in statement: a bold sans sentence with the month's revenue
and its change vs last year, then a serif sentence with the driver and the return rate. Add a section nav "(1) … (4)".
Then a Key findings card (serif bullets beside hairline key–value rows for revenue, copies, return rate, digital share),
Figure 1 (12-month revenue, prior year dashed, title as a finding, Note caption) beside Table 1 (top items, ink rules,
subject column tinted, group rows), one card per imprint with the card anatomy, Figure 2 (return rate by imprint with
the target as a dashed reference) beside a Notes card, and the ink footer. One filter row at the top applies to everything.
Use only the colors in Data Colors, the formats in Numbers, Dates & Units, the components in Component Stylings and the
breakpoints in Responsive Behavior. Korean and English in one file, switched with ?lang=ko|en; English by default.
Every chart needs a hover tooltip, keyboard control and a screen-reader table.
```

Checklist the agent should pass before it is done: statement first and run-in; findings in serif; every figure titled with a finding and captioned with `Note:`; line ends labeled, no legend; comparison and target dashed gray; no clay on data; tables ruled in ink with the subject column tinted; change color by good/bad; `tabular-nums`; keyboard and screen-reader support; nothing bold in the serif.
