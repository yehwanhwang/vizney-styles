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
  card: "#f0eee6"
  card-strong: "#e8e6dc"
  pill: "#f5f4ed"
  band: "#141413"
  band-hover: "#1f1e1d"
  ink: "#141413"
  ink-2: "#30302e"
  body: "#3d3d3a"
  text-2: "#5e5d59"
  text-3: "#73726c"
  muted: "#87867f"
  on-dark: "#faf9f5"
  on-dark-2: "#9c9a92"
  hair: "#e8e6dc"
  hair-2: "#dedcd1"
  hair-dark: "#30302e"
  accent: "#d97757"
  accent-deep: "#c46849"
  good: "#2c6e4f"
  bad: "#a33d34"
  focus: "#2c84db"
data:
  categorical: ["#d97757", "#6953a0", "#0d9298"]
  other: "#8f8d86"
  comparison: "#73726c"
  sequential: ["#e79176", "#d47150", "#ba5432", "#9b3d1d", "#782d12"]
  diverging: ["#00636a", "#00797f", "#469094", "#9f9b93", "#b26e58", "#a14e33", "#8f2c01"]
  good: "#2c6e4f"
  bad: "#a33d34"
typography:
  serif: { en: "Source Serif 4", ko: "Noto Serif KR" }
  sans: { en: "Inter", ko: "Pretendard" }
  mono: "JetBrains Mono"
radius: {card: "16px", pill: "999px", button: "10px", tooltip: "8px", cover: "2px 4px 4px 2px"}
spacing: {page: "32px", gap: "16px", card: "24px", row: "8px 0", bandPadding: "26px 32px 22px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: anthropic.tps, powerbi: powerbi-theme.json, prompts: prompt.md}
---

# Anthropic style — DASHBOARD.md

**Ivory, Editorial, Quiet** · 아이보리, 에디토리얼, 고요함

A dashboard design spec read from the public design of anthropic.com and claude.com, extended with everything a dashboard needs that a website spec does not: validated data colors, KPI anatomy, chart rules, number and date formats in English and Korean, density, filters, accessibility, and the settings that carry it into Tableau, Power BI and the web. Give this file to an AI coding agent (keep it in the repository root as `DASHBOARD.md`) or hand it to whoever builds your dashboards, and the screens come out looking like the live sample.

- Live sample: https://styles.vizney.com/anthropic/ (add `?lang=ko` for Korean)
- Raw file for your repository: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/anthropic/DASHBOARD.md
- Files in the same folder: [tokens.json](tokens.json) (source of every value here), [tokens.css](tokens.css), [anthropic.tps](anthropic.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.html)
- Catalog: https://styles.vizney.com · Vizney Styles 01

Not an official Anthropic design, and not affiliated with or endorsed by Anthropic. This is an independent reading of publicly visible design; it carries no logo, wordmark, typeface, image or data of theirs, and the sample's publisher and numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A warm ivory page that reads like a well-set book. The screen opens by saying the month's result in one serif sentence, then supports it quietly: ivory cards with no borders or shadows, lists divided by hairlines, one clay accent, and a single ink-black band for the detail table. Depth comes from color steps, not from elevation. Figures stay regular weight; size and placement do the ranking, so nothing shouts. The overall impression is editorial and calm: a report you would read, not a cockpit you would watch.


## Color Palette & Roles

Surfaces and text are a warm gray ladder: `canvas` → `card` → `card-strong` → `band`. There is one accent, `accent` (clay), used for the main data series, outlined pills and the single primary control. Green and red exist only as change text.

| Token | Hex | Role |
|---|---|---|
| canvas | `#faf9f5` | page background, tooltips, hollow markers |
| card | `#f0eee6` | cards; no border, no shadow |
| card-strong | `#e8e6dc` | active tab, secondary button, bar tracks |
| pill | `#f5f4ed` | pills and the language toggle |
| band / band-hover | `#141413` / `#1f1e1d` | the one dark surface and its row hover |
| ink / ink-2 | `#141413` / `#30302e` | figures, titles, primary control / its hover |
| body | `#3d3d3a` | running text |
| text-2 | `#5e5d59` | labels, captions, legends, the statement's words (5.7:1 on card) |
| text-3 | `#73726c` | axis ticks and the comparison series (4.2:1 on card) |
| muted | `#87867f` | rank numbers, small captions (3.1:1 on card; never for body text) |
| on-dark / on-dark-2 | `#faf9f5` / `#9c9a92` | text on the band / its captions (6.5:1) |
| hair / hair-2 / hair-dark | `#e8e6dc` / `#dedcd1` / `#30302e` | dividers on cards / chart baseline and tooltip border / dividers on the band |
| accent / accent-deep | `#d97757` / `#c46849` | the clay accent / its hover and bars on the band |
| good / bad | `#2c6e4f` / `#a33d34` | favourable / unfavourable change, text only (5.2:1 / 5.5:1 on card) |
| focus | `#2c84db` | focus ring |

Rules:
- No pure white and no cool grays. Every gray on this screen is warm.
- Text never wears a data color. Values, labels and legends stay ink or text-2; a colored mark beside them carries identity.
- The accent is the only saturated color on the page unless a chart needs categories (next section).


## Data Colors

All data colors were checked with an OKLab validator for color-vision deficiency separation, normal-vision separation and contrast against the card surface (`#f0eee6`). Use them exactly as listed; do not generate tints.

**Single series:** the accent `#d97757`. It is 2.7:1 on the card, below the 3:1 floor for unlabeled marks, so a clay line or bar is always named in a legend or a row and its end value is written on the chart.

**Comparison series** (prior year, target, benchmark): `#73726c`, dotted (2px, round dots 5px apart). It is gray on purpose: the comparison is context, not a category. Separation from clay: ΔE 8.8 under CVD, 17.5 normal vision.

**Categorical** (identity on one mark), in fixed order, never cycled:

| Slot | Name | Hex |
|---|---|---|
| 1 | clay | `#d97757` |
| 2 | plum | `#6953a0` |
| 3 | teal | `#0d9298` |
| Other | gray | `#8f8d86` |

Worst adjacent pair: ΔE 12.5 under CVD, 19.1 normal vision. A fourth real category folds into Other, or the chart becomes small multiples. Color follows the entity, not its rank: when a filter removes a category, the survivors keep their colors.

**Sequential** (magnitude, one hue, light → dark): `#e79176` `#d47150` `#ba5432` `#9b3d1d` `#782d12`. Monotone lightness, every step at least 0.06 ΔL apart, light end 2.1:1 on the card.

**Diverging** (polarity around a baseline): `#00636a` `#00797f` `#469094` — `#9f9b93` — `#b26e58` `#a14e33` `#8f2c01`. Teal is below, clay is above, the midpoint is a neutral warm gray. Each arm passes the sequential checks; the poles are ΔE 13.0 apart under CVD.

**Status:** good `#2c6e4f`, bad `#a33d34`, neutral `#73726c`. Status colors are reserved for change text and status pills; they never color a series.


## Typography Rules

One serif, one sans and one mono, with a Korean counterpart for the first two. A screen loads only the fonts of its language.

| Role | English | Korean | Weights |
|---|---|---|---|
| Serif (display) | Source Serif 4 | Noto Serif KR | 400, 500 |
| Sans (text, figures) | Inter | Pretendard | 400, 500, 600 |
| Mono (table numbers, dates, ranks, codes) | JetBrains Mono | JetBrains Mono | 400, 500 |

- The serif sets the statement, item titles (books, products, accounts), the band heading and the company name. Weight 400, with 500 only for the numbers inside the statement. The serif is never bold. In English, item titles are italic.
- Figures are sans, regular weight, 34px with −0.02em tracking (30px on phones), `tabular-nums`. Units and suffixes (억, 만, 부, %, ₩, M) sit next to the number at 13px in text-2.
- Scale: statement `clamp(26px, 2.9vw, 40px)` / 1.28; card titles 15px medium with a 12.5px note; body 14px; labels 13px; captions 12.5px; axis ticks 11px; table headers 11.5px uppercase with 0.06em tracking (0.02em in Korean); mono cells 13px.
- A KPI card uses two sizes only: the figure and everything else. Weight and color do the rest.
- Korean text breaks between words (`word-break: keep-all`); a money figure never breaks.


## Numbers, Dates & Units

- **Currency:** English `₩423M`, `₩4,375M`, `₩16,800` (whole won below a million); Korean `4.23억`, `4억 2,300만 원` in sentences, `16,800원`. Use M (millions) and K in English; 억 and 만 in Korean. Never mix.
- **Counts:** thousands separators always (`27,300`). Korean adds the counter after the number at the unit size (`27,300부`, `12,480건`); English adds the noun in the label, not the figure.
- **Percentages:** one decimal (`11.5%`). Differences between percentages are points: `−0.6 pts` in English, `−0.6%p` in Korean.
- **Change:** signed with a true minus (`−`, U+2212), one decimal, then the comparison (`+10.4% vs Oct 2025` · `+10.4% 전년 동월 대비`). The color follows whether the move is good for that metric: a falling return rate is green.
- **Dates:** `2026-08-19` in tables and mono; `Oct 2026` / `2026년 10월` in prose; month ticks `Nov … Oct` / `11월 … 10월`, the current month in ink.
- **Rounding:** figures round to three significant digits on cards; tables keep whole numbers.
- **Alignment:** numbers right-aligned in tables, `tabular-nums` everywhere numbers line up.


## Layout Principles

- One column on the canvas, at most 1400px wide, with 32px side padding (24px up to 1359px, 16px below 640px). No sidebar, no app chrome: the page reads top to bottom like an article.
- **Header** (84px): the company name in serif with a small uppercase caption; on the right a period pill, the language toggle and one ink pill that jumps to the detail band. Nothing else, no logo.
- **Filter row** under a hairline: pill tabs on the left, a basis note on the right. The tabs scope every card below; cards never carry their own filters.
- **Statement:** the headline result as one serif sentence with the numbers in ink, then a one-line lead naming the top item. A dashboard in this style starts by saying the result in words.
- **12-column grid, 16px gap.** Row 1: four KPI cards (3 columns each). Row 2: the trend (7) beside a ranked list (5). Row 3: three cards of 4 columns. Then a full-width ink band with the detail table.
- **Density:** laptop first. The sample fits a 1440 × 900 window to the end of row 2 without scrolling; at 1366 × 768 the statement and the KPI row are above the fold.
- Order of reading: statement → KPIs → trend and list → detail. Keep it; don't lead with a chart.


## Component Stylings

- **Card:** card color, 16px radius, 20 × 24px padding, no border, no shadow, no hover change. Title 15px medium in ink with a 12.5px note in text-2 on the same baseline.
- **KPI card:** label on top, figure 8px below, change line 12px below the figure. The three rows share a subgrid so figures align across the row even when a label wraps. The change line is the signed change in weight 600 (good or bad) followed by the comparison in text-2. A share card shows its split instead (`E-book 17.3% · Audio 5.0%`).
- **Pills and tabs:** 32px tall, 999px radius, 13px text, 1px hair border on the pill tint. The active tab is card-strong with a hair-2 border, ink text, medium weight. The language toggle's selected side turns ink with ivory text. The ink pill is the only primary control, and there is one of it.
- **Trend card:** the plot runs edge to edge across the card. Current series 2px monotone curve in clay; comparison 2px dotted in text-3; a hair-2 baseline; no gridlines; five month ticks, the last in ink. The last point is a hollow dot (canvas fill, 2px clay ring), and the last values of both lines are written at the right end in ink and text-2 so the chart reads without hovering. Hover or focus adds a hairline crosshair, a 13px clay halo at 18%, a canvas dot with a 2.5px ink ring, and the tooltip.
- **Ranked list:** rows divided by 1px hair lines, 8px vertical padding: a two-digit rank in mono muted, the item title in the 15px serif with the author or owner in 12.5px text-2, the value in medium weight with a small unit, and the change as text with a diagonal arrow in good or bad. No chips, no tinted backgrounds. The author drops out when the card is narrower than 420px.
- **Bar list** (single hue): a 6px clay bar on a card-strong track, the name on the left, value and share on the right. Hovering a row dims the others.
- **Composition** (part of whole): a 10px stacked bar with 2px canvas gaps and round ends in the categorical colors, then rows with an 8px dot, name, value and share. No donuts.
- **Ink band:** full width, 16px radius, 26 × 32px padding; a 22px serif heading in ivory beside a caption in on-dark-2; a real table with sans uppercase headers, serif titles, mono numbers and dates right-aligned, hair-dark dividers. A progress cell holds an 88 × 6px bar in accent-deep on a hair-dark track with the percentage; a 22px status pill is outlined in clay when true and in hair-dark when not. Rows tint to band-hover on hover. The band appears once per screen.
- **Tooltip:** canvas fill, 1px hair-2 border, 8px radius, shadow `0 8px 22px rgba(20,20,19,.10)`, the only shadow on the page. An 11px title, then one row per series: a line key or dot, the value in medium, the series name. It sits above, left, right or below the point, whichever fits the card, with its arrow on the point.
- **Legends:** line keys for lines (dotted for the comparison), solid dots for categories. One series needs no legend; its title names it.
- **Status pills:** 22px, 999px radius, 11.5px text, outlined, never filled.
- **Style-carrying cards** in the sample: key colors appear as the cloths of a clothbound edition (name, hex, count), fonts as the typesetting of the next book, and the photo slot as a color-block book cover. Replace them with cards from your own business; keep the rule that colors, fonts and images live inside data cards, never in swatch panels.


## Charts

- **Choose by the question.** Change over time → line (monotone curve, at most two series: current and comparison). Magnitude across categories → horizontal bar list, one hue. Part of whole → one stacked bar with ≤ 3 colors plus Other. Ranking → the hairline list, not a chart. A single number → a KPI card or the statement.
- **One axis.** Never a dual axis. Two measures of different scale become two charts or an index.
- **No gridlines on the trend**; the baseline and the written end values carry the scale. Bar charts may use hair-2 gridlines.
- **Marks:** 2px lines, round caps; bars 6–10px with round ends on a track; ≥ 8px markers with a 2px canvas ring where marks overlap.
- **Labels:** write the end values of every line and the share next to every bar; never a number on every point.
- **Don'ts:** no pie or donut, no 3D, no gradients, no rainbow categories, no dashed lines other than the dotted comparison, no color on text.


## Depth & Elevation

Flat. Cards have no border and no shadow; the page's depth is the ladder canvas → card → card-strong → band. The tooltip is the only element with a shadow. Nothing lifts on hover; rows tint instead.


## Interaction & Motion

- On load the trend line draws in (1.2s, `cubic-bezier(.165,.84,.44,1)`); the comparison, end values, list rows and band rows fade in with a short stagger. Changing a filter rewrites the statement and every card the same way.
- Every chart has a hover tooltip, a keyboard mode (arrow keys step, Home and End jump, Esc clears, values announced through a live region) and a screen-reader table. Tabs move with the arrow keys. The band is a real table and needs no extra one.
- On touch screens a tap picks a point and a tap elsewhere clears it.
- `prefers-reduced-motion` turns all motion off.


## Accessibility

- Text contrast: body and labels ≥ 4.5:1 on their surface (text-2 5.7:1, on-dark-2 6.5:1); muted (3.1:1) only for ranks and short captions.
- Marks below 3:1 (clay on card) are always labeled and listed in a table.
- Identity is never color alone: legends plus direct labels; the comparison series differs by line style; status pills carry words.
- Focus ring `#2c84db`, 2px, 2px offset. Tab order: header controls → filter tabs → cards in reading order.
- Live region for chart navigation; tables with `scope` on headers.


## Responsive Behavior

- ≥ 1360: the 12-column layout above. 1024–1359: same layout with 24px padding and a 14px gap.
- 900–1023: the trend and the list stack full width; the three style cards become two beside one.
- 640–899: two columns; KPI cards 2 × 2; the header drops the caption and the period pill; the table drops the date column and wraps titles.
- < 640: one column with KPI cards still 2 × 2 (28px figures); the ink pill leaves the header; the table keeps title, progress and status.
- Embedded in a post (`?embed=1`): the footer hides and the page reports its height to the host.


## Tool Mapping

**Web / AI coding agents.** Load `tokens.css` (or copy the `colors` block from the front matter). Fonts come from Google Fonts and jsDelivr:
`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Serif+KR:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;1,8..60,400&display=swap`
`https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css`

**Tableau.** Import `anthropic.tps`: paste its `<color-palette>` elements into `My Tableau Repository/Preferences.tps` inside `<preferences>` and restart Tableau Desktop. Then: dashboard background `#faf9f5`; containers for cards with background `#f0eee6`, 16px… Tableau has no radius, so use 0 and keep the inner padding at 24px; no borders; worksheet titles 15px medium; marks: line size 2, markers off except the last point; axis ticks `#73726c` at 11px with gridlines off on line charts; reference line for the prior year as a dotted gray line; number formats `₩#,##0,,M` / `#,##0.0%` / custom `+0.0%;−0.0%`. Fonts: Tableau Book for text, Source Serif 4 only when it is installed on every viewing machine and the server; otherwise Tableau Book throughout and the serif stays in the title.

**Power BI.** Import `powerbi-theme.json` (View → Themes → Browse for themes). It sets data colors (use only the first four for categories), the ivory page and card backgrounds, text classes and axis colors. Install Inter on authoring and viewing machines or let it fall back to Segoe UI. Set KPI cards to card visuals with the callout at 28px and the category label in text-2; use the "good/bad" colors only on conditional formatting of change measures.

**Datawrapper / Flourish / chart libraries.** Categorical `#d97757, #6953a0, #0d9298, #8f8d86`; comparison `#73726c` dotted; background `#faf9f5`; text `#141413` / `#5e5d59`.


## Do's and Don'ts

- Do start the screen with the result in words. Don't lead with a chart or a wall of KPIs.
- Do keep one accent. Don't spread clay over several series, and never more than three colored categories plus Other.
- Do write end values and shares on the marks. Don't label every point.
- Do use regular-weight figures and a never-bold serif. Weight goes to labels, change text and small controls only.
- Do keep cards flat and warm. No borders, shadows, hover lifts, pure white or cool grays, and no card inside a card.
- Don't use pies, donuts, dual axes, gridlines on the trend, dashed lines other than the dotted comparison, or tinted chips for change.
- Don't put a logo, wordmark or illustration in the header; the company name set in serif is the brand. Photos are replaced by color blocks in this reference.
- Don't invent tints: every color on a mark comes from the Data Colors section.


## Agent Prompt Guide

Put this file in the project root as `DASHBOARD.md` and keep `tokens.css` next to it. Then prompt, for example:

```
Build a monthly revenue dashboard in the Anthropic style defined in DASHBOARD.md.
Open with one serif sentence that states the month's revenue and its change vs last year,
then four KPI cards (revenue, orders, return rate, digital share), a 12-month trend with the prior year dotted,
a top-5 list with hairline rows, and a detail table in an ink band. One filter row at the top applies to every card.
Use only the colors in the Data Colors section, the number formats in Numbers, Dates & Units, and the responsive rules.
Korean and English in one file, switched with ?lang=ko|en; English by default.
```

Checklist the agent should pass before it is done: statement first; one accent; comparison dotted gray; end values written; figures regular weight; no gridlines on the trend; change color by good/bad; `tabular-nums`; keyboard and screen-reader support; nothing bold in the serif.
