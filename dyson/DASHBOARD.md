---
name: Dyson style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 10
tagline: Technical, Exploded View, Clean
tagline_ko: 테크니컬, 분해도, 말끔함
source: https://www.dyson.com/, https://www.dyson.co.kr/
sample: https://styles.vizney.com/dyson/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#ffffff"
  panel: "#f7f7f7"
  header: "#000000"
  header-text: "#ffffff"
  header-sub: "#b9b9b9"
  screen: "#000000"
  screen-text: "#ffffff"
  screen-sub: "#b9b9b9"
  ink: "#333333"
  body: "#404040"
  muted: "#555555"
  faint: "#919191"
  hair: "#dadada"
  line: "#dcdcdc"
  soft: "#ebebeb"
  nickel: "#d9dbdd"
  nickel-edge: "#7d8083"
  link: "#0066cc"
  accent: "#79b928"
  accent-text: "#000000"
  focus: "#0066cc"
  text-2: "#555555"
data:
  categorical: ["#6b46c1", "#1a8a6e", "#c26a12"]
  other: "#d9dbdd"
  comparison: "#555555"
  categorical_text: ["#5a3fb0", "#176f59", "#9a520c"]
  sequential: ["#b3a0e9", "#977cdb", "#7d5fcf", "#6b46c1", "#4b2d91"]
  diverging: ["#2a64b0", "#5b8bd4", "#8fb0e4", "#e3e3e3", "#ec9aa1", "#d9555f", "#a8142c"]
  good: "#1d7a43"
  bad: "#d0273b"
typography:
  sans: { en: "Jost", ko: "Noto Sans KR" }
  display: { en: "Jost", ko: "Noto Sans KR" }
  mono: "Roboto Mono"
radius: {screen: "50%", part: "5px", balloon: "50%", bar: "0", button: "4px", tooltip: "4px", window: "8px", panel: "0"}
spacing: {page: "32px", gap: "32px", section: "76px", panel: "20px 24px 18px", cell: "8px 10px", footer: "24px 0 40px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: dyson.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: parts.csv}
---

# Dyson style — DASHBOARD.md

**Technical, Exploded View, Clean** · 테크니컬, 분해도, 말끔함

A dashboard design spec read from the way Dyson shows what is inside a machine: the round screen on its cordless vacuums (the power mode by name in its colour, the run time left, a battery), the exploded views it uses to explain its technology, the green light on the cleaner head that shows the dust a floor still holds, and the Specifications panel of dyson.com. It turns those parts into a prototype test review on white with black screens, with the values, rules and checks an AI coding agent needs to rebuild it.

```
npx @vizney/styles@latest add dyson
# or, without Node:
curl -fsSL https://styles.vizney.com/install.sh | sh -s -- dyson
```

That puts `DASHBOARD.md` in the project root and the `dashboard-style` agent skill (build, restyle, review) in `.claude/skills/dashboard-style/`, together with `tokens.css`, `tokens.json`, `dyson.tps`, `powerbi-theme.json` and `prompt.md`. Coding agents that read skills pick it up whenever a task touches a dashboard or a chart; any other agent can be told to follow `DASHBOARD.md`.

- Live sample: https://styles.vizney.com/dyson/?lang=en (Korean `?lang=ko`; one model `&model=c45` or `&model=c90`, C60 by default)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/dyson/DASHBOARD.md
- Package: [dyson-dashboard-style.zip](dyson-dashboard-style.zip) (unzip in your project root) · the skill: [skill/SKILL.md](skill/SKILL.md)
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [dyson.tps](dyson.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [parts.csv](parts.csv) (the data behind the sample's Figure 1)
- Blog post: [English](https://www.vizney.com/style-dyson/) · [한국어](https://kr.vizney.com/style-dyson/)
- Catalog: VIZNEY STYLES · 10 · https://styles.vizney.com (Vizney Styles is a line of [Vizney](https://www.vizney.com))

Not an official Dyson design, and not affiliated with or endorsed by Dyson. A reference style read from the publicly visible design of dyson.com and dyson.co.kr and from public touchpoints such as the machines' screens and Dyson's exploded technology views; it carries no Dyson logo, typeface, photo, product name or data. Trademarks belong to their owners. The sample's company, Vizney Appliances, its models, parts, tests and all its numbers are fictional.


## Visual Theme & Atmosphere

An engineering review on a clean bench. The page is white `#ffffff` under a black header; the one panel is the light grey `#f7f7f7` of the dyson.com Specifications panel; text is the site's soft ink `#333333`, never pure black. Everything that measures sits on black: the round screens, the laser floor strips and the graph screens are `#000000` with white Light numerals, exactly like the displays on the machines. Colour is rare and always carries one meaning:

- Mode colours (Eco `#3fd24a`, Auto `#2aa3ef`, Boost `#f0403a`) only on the round screens, always beside the mode's name.
- Purple `#6b46c1` for a part changed since the last design review, with its numbered balloon.
- Red `#d0273b` (text `#b0122f`, `#f0403a` on black) for anything that misses a target or a budget, always with ✗ or the word.
- Laser green `#5fe04a` only for dust on the laser floor.

Three devices carry the report, and each holds data:

- **Round screen (the KPIs).** One black circle per power mode: the mode's name in its colour, the run time left in minutes and seconds in Light, a battery filled by run time ÷ the MIN, 'MIN 60:00' under it, and a ring in the mode colour. Under each screen, the gap to the MIN (red when short, ✓ when not) and the last build's value.
- **Exploded view (Figure 1).** The machine's parts pulled apart along one dash-dot axis from the floor to the hand, at even gaps, each part as long as it is heavy; a budget bracket on the other side; a red tip for the grams over budget; purple for a part changed since the review; numbered balloons ① to ⑧ on leader lines to the name, weight and gap. Under it the assembled weight as one bar against the MAX.
- **Laser floor (Figure 2).** A black strip per build with one green dot for every 0.05% of the dust laid down that is still on the floor after one pass along a wall, wall on the left. Build 37 against build 41 shows the new head at a glance.

The Specifications panel grammar gives the spec rows beside the screens (label → large Light value with a small unit → ✓ or ✗ → hairline), and the figure labels read like a patent drawing: 'FIG. 1'. The later sections put their charts on the same black screens the machines have: wide graph screens with bars from a white dash-dot target line (Figure 3) and a test timeline (Figure 4), white for what passes, grey for what is left, red for what misses. No product photos, renders, drawings of cyclones or loops, screen icons, product or technology names.

Measured in a browser on November 23–24, 2026 at 1440×900 on dyson.com (home, the cordless vacuum list, a product page with Specifications open, a support guide on the screen and power modes), dyson.co.kr and the terms of use: header `#000000` with a 16px Light white menu; text `#333333`, labels `#555555`, tertiary `#919191`, bullets `#404040`; hairlines `#dadada` under spec values, card borders `#dcdcdc`; panels `#fbfbfb` (the sample uses `#f7f7f7` so the panel holds against white on more screens); price blue `#0066cc`; deal button green `#79b928` with black text; Specifications label 16/24 500 `#555555` → value 36/44 Light 300 `#333333` with the unit 24/32 400 → 1px `#dadada`.


## Color Palette & Roles

| Token | Hex | Role |
|---|---|---|
| canvas | `#ffffff` | The page |
| panel | `#f7f7f7` | The one panel (Figure 1), the build 41 column band in Table 1, row hover, the code background |
| header | `#000000` | The header (two lines), with white text and `#b9b9b9` secondary text |
| screen | `#000000` | Round screens, laser floor strips, graph screens; white text, `#b9b9b9` secondary |
| ink | `#333333` | Titles, values, the selected tab's underline, table head rule, balloons |
| body | `#404040` | Body text and part names |
| muted | `#555555` | Labels, subtitles, keys, captions, limits (7.5:1; 6.96:1 on the panel) |
| faint | `#919191` | Only large section numbers and dashes for missing values |
| hair | `#dadada` | Table rules and the hairline under a spec value |
| line | `#dcdcdc` | Card and window borders |
| nickel | `#d9dbdd` | A part's fill, with a `#7d8083` edge (3.71:1 on the panel) |
| link · focus | `#0066cc` | Links and the 2px focus ring |
| accent | `#79b928` | One primary button only ("Ask for your company's style"), black text |


## Data Colors

| Use | Values |
|---|---|
| Part states (Figure 1) | changed `#6b46c1` (text `#5a3fb0`), over budget `#d0273b` (text `#b0122f`), otherwise nickel `#d9dbdd` with a `#7d8083` edge |
| Power modes (round screens only, on black) | Eco `#3fd24a`, Auto `#2aa3ef`, Boost `#f0403a`, always with the mode's name |
| Laser floor | dust `#5fe04a` on `#000000` (12.3:1); the count of dots is the data |
| Graph screens (on black) | met `#ffffff`, missed `#f0403a`, to go `#5c5c5c`; target line `#ffffff` dash-dot 10 3 2 3; change balloons white with a `#5a3fb0` number |
| Categorical (for your own charts) | purple `#6b46c1`, green `#1a8a6e`, copper `#c26a12`, then other in nickel `#d9dbdd`; text steps `#5a3fb0`, `#176f59`, `#9a520c` |
| Sequential | `#b3a0e9` `#977cdb` `#7d5fcf` `#6b46c1` `#4b2d91` |
| Diverging | `#2a64b0` `#5b8bd4` `#8fb0e4` `#e3e3e3` `#ec9aa1` `#d9555f` `#a8142c` |
| Status text | good `#1d7a43`, bad `#b0122f` |

Rules:

- The subject of a title takes purple; everything else stays nickel or grey. Red is never a series colour; it only marks a miss.
- On white, a miss is a red value with ✗; a table cell is never filled with colour. On black, a miss is a red bar or a red end, and the side of the target line plus ✓ or ✗ say the same thing.
- Mode colours never leave the round screens. A graph screen uses white, grey and one red.
- Checked with the dataviz `validate_palette.js` (OKLab) on `#ffffff` and `#f7f7f7`, screen colours on `#000000`: categorical passes every check with `--pairs all` (worst CVD pair copper↔green ΔE 9.6, normal vision 21.3); changed purple against over red ΔE 22.2 (CVD) and 27.6; modes ΔE 11.2 and 29.0, all ≥ 3:1 (Eco and Auto sit above the lightness band on purpose, as on the product, and always come with the mode's name); white against red on black ΔE 36.7 and 42.4; sequential and both diverging arms pass `--ordinal`. Text: ink 12.6:1, muted 7.5:1, red text 7.1:1, good 5.4:1.


## Typography Rules

- **One geometric sans.** dyson.com sets a geometric sans in Light 300, Book 400 and Medium 500; the stand-in is **Jost** (SIL OFL) for English and **Noto Sans KR** for Korean, the face dyson.co.kr sets beside it. Code only in **Roboto Mono**. Numbers stay in the sans with tabular figures.
- Light 300 is the voice of a measurement: the result sentence, section names, the run times on the round screens (Jost in both languages, like a product screen), spec values, part weights, the dust left, and the large build 41 value on a graph screen.
- Medium 500 for labels, titles, tabs, buttons and the figure number; 400 for text.

| Role | Size and weight |
|---|---|
| Result sentence | 34px/300 (Korean 30px), line-height 1.22, two sentences on two lines: what the build did, then what it costs |
| Kicker | 14px/500 `#555555`: model · build · targets met, the count in red (green at 7 of 7) |
| Round screen | 164px circle (150 under 1360px, 142 under 1200px, a third of the width on phones): the mode at 9% of the width in 500, the run time at 27% in 300, 'MIN 60:00' at 7.2% in `#b9b9b9`; under it the gap 15.5px/500 and the last build 13px |
| Spec row | label 14px/500 with its limit 12.5px `#555555` → value 25px/300 with the unit 14px → ✓ or ✗ → 1px `#dadada` hairline |
| Figure number | 'FIG. 1' 12.5px/500 `#555555`, letter-spaced .06em (Korean '그림 1') |
| Card title | 19px/500 (Korean 17.5px), the finding as a sentence; subtitle 14px `#555555` |
| Section | 30px/300 with its number in `#919191` ('01  By build') and a 15px kicker |
| Part label | name 14px/500 above the weight 21px/300 with 'g' 12.5px; the gap 12.5px (500 red when over) |
| Balloon | 19–21px circle, 1px `#333333` (purple for a changed part), the number 11–12px/500 Jost |
| Graph screen | measure name 14px/500 white with its limit 12.5px `#b9b9b9`; build numbers 11.5px `#b9b9b9` (review and now white); the build 41 value 40px/300 white with a small unit, its gap 13px/500 |
| Table | 14.5px rows, 1px `#dadada` rules, a 1px `#333333` rule under the head, group rows 12.5px/500 letter-spaced |
| Body | 16px/400 (Korean 15px) |


## Numbers, Dates & Units

| Measure | English | Korean |
|---|---|---|
| Run time | `56:40` (minutes:seconds, the same on screens in both languages) | `56:40`; in text `3분 20초` |
| Gap to a run-time MIN | `3:20 short` · `+1:10` | `3분 20초 부족` · `1분 10초 여유` |
| Weight of a machine | `2.94 kg`, the MAX `2.90 kg` | `2.94 kg` |
| Weight of a part, a gap | `610 g`, `+50 g`, `40 g over`, `30 g under` | `610 g`, `50 g 초과`, `30 g 여유` |
| Suction | `253 AW` | `253 AW` |
| Noise | `79.2 dB(A)` | `79.2 dB(A)` |
| Edge and carpet pick-up | `98.1%`, a change `+1.1 pts` | `98.1%`, `+1.1%p` |
| Dust left | `1.9%` | `1.9%` |
| Bin | `0.60 L` | `0.60 L` |
| Date | `Nov 21`, with weekday `Fri, Dec 11` | `11월 21일`, `12월 11일(금)` |
| Build and week | `Build 41 · Week 47, Nov 16–22, 2026` | `빌드 41 · 47주차, 2026년 11월 16~22일` |
| Targets met | `5 of 7` · `5 / 7` | `7개 중 5개` · `5 / 7` |
| Pass, miss | ✓ · ✗ next to the value, never alone | same |

Minus is the true minus sign `−`. Numbers are tabular. Missing values are an em dash `—` in `#919191`. A limit is written as the word and the value: `MIN 60:00`, `MAX 2.90 kg` (Korean `최소`, `최대`).


## Layout Principles

- Width up to 1400px, 32px page padding, 32px gaps, 76px between sections, a 12-column grid. At most four views on one screen.
- **Header, black, two lines (104px).** Line one: business and report name, the build and week, EN/KO. Line two: the model tabs (C45 Compact · C60 Standard · C90 Large) set like the dyson.com menu row (16px Light white, the selected one Medium with a 2px white underline), and the test date and design freeze on the right.
- **First screen (1fr | 478px).** Left: the kicker, the result in two Light sentences, the three round screens beside the four spec rows (suction, noise, edge pick-up, weight), then Figure 2 laser floor at the foot of the column. Right: Figure 1 exploded view on the `#f7f7f7` panel with the assembled bar against the MAX. Figure 2 sits at the bottom of its row so both captions end on one line.
- **01 By build (1fr | 1fr, subgrid).** Figure 3, three black graph screens stacked (edge pick-up, Eco run time, weight) | Table 1, the other measures from build 37 (review) to 41 (now), so nothing in Figure 3 is repeated.
- **02 Tests and what is left (7fr | 5fr).** Table 2, the issues, on the left | Figure 4, durability tests on a graph screen, on the right, so the black screens zigzag down the page. Stacked layouts put the figure first.
- **03 Build it yourself** (the workbench) and **04 How we count** (definitions in two columns).
- Side-by-side cards share a subgrid so their title, body and caption rows line up and their bottoms end on one line.
- Every card: figure number → finding title → subtitle → keys → view → caption. No card exists only to show a colour or a typeface.


## Component Stylings

**Round screen.** A black circle; a ring at 45.4% of the diameter, 1.85% thick, in the mode colour, drawn round from the top; the mode's name above, the run time in the middle (Light, white), a white battery outline 40% wide filled in the mode colour by run time ÷ MIN (full at or above the MIN) with a small terminal, 'MIN 60:00' under it in `#b9b9b9`. Below the circle, outside it: the gap to the MIN (15.5px/500, red with the word 'short' when under, ✓ and 'spare' when not) and the last build's value (13px `#555555`).

**Spec row.** Label and limit on the left, the value and unit on the right, ✓ or ✗ after the unit, a 1px `#dadada` hairline under it. A miss turns the limit and the value red `#b0122f`. Four rows beside the screens; under 1280px they move under the screens in a 2×2 grid, under 640px one column.

**Exploded view (Figure 1).** On the `#f7f7f7` panel. A vertical dash-dot axis (`#7d8083`, 14 4 2 4). Parts stacked from the floor (cleaner head) to the hand (battery) at even gaps, centred on the axis, each a rounded rectangle (5px) as long as its weight on one shared scale: nickel `#d9dbdd` with a `#7d8083` edge; purple `#6b46c1` when changed since build 37; the grams over budget as a red `#d0273b` cap at the top of the part. A 1px `#555555` budget bracket on the opposite side of each part. Numbered balloons ① to ⑧ on leader lines; the label shows the name, the weight and the gap to budget (red when over; purple 'changed in build 38' when changed). Under the stack, the assembled weight as one bar, each part a segment in stack order, with the MAX as a dotted line and the total and gap at the right. When the panel is narrower than 420px, labels gather on one side; when it is short, labels go to one line.

**Laser floor (Figure 2).** A black strip per build (56px tall, the full width of the column), the wall on the left; green dots, one per 0.05% of the dust laid down that is still on the floor, denser towards the wall. Each strip has its label (build and head) on the left and the share left on the right in 28px Light with '% left behind' under it. A green sweep crosses the strip as the dots light up.

**Graph screen (Figures 3 and 4).** `#000000` with 8px corners, the only rounded rectangles on the page besides buttons and the code window. Measure name and limit at top left, 'BUILD 41' at top right in letter-spaced `#b9b9b9` capitals. Square-ended bars from a white dash-dot target line (10 3 2 3): white when the target is met, `#f0403a` when missed. The gap printed (12px/500) only on build 37 and the builds that changed a part; those builds also carry a white balloon with the part number in purple and a dotted `#6b6b6b` line down through the bars. Build numbers along the bottom. The build 41 value sits at the right in 40px Light white with a small unit, its gap below in the bar's colour with ✓ or ✗. On a test timeline (Figure 4): done white, to go `#5c5c5c`, past design freeze `#f0403a`; a solid white TODAY line and a white dash-dot DESIGN FREEZE line; month lines `#333333`; test names white and amounts `#b9b9b9`.

**Tables.** No vertical rules, no zebra, no filled cells. Head 13.5px/500 `#555555` with a 1px ink rule under it; group rows in letter-spaced 12.5px/500; rows 14.5px with 1px `#dadada` rules. The current build's column on a `#f7f7f7` band with its value in 500. A miss is a red value with ✗. Parts are named by their balloon and name; the issue table puts the number that matters in red inside the sentence ('50 g over budget') and the fix's effect in the fix column ('−45 g').

**Balloon.** A 19–21px circle with a 1px ink border and the number in Jost 500; purple when the part changed. The same number means the same part on every view.

**Tooltip.** White, 1px `#eeeeee` border, 4px corners, a soft shadow; head 14.5px/500, a grey sub-line (the week), then rows of value (15px/500) and label (`#555555`), a miss in red 500, a change in purple 500.

**Buttons.** 4px corners, 40px tall; the one primary button `#79b928` with black 500 text; secondary buttons a 1px `#333333` border on white. Focus is a 2px `#0066cc` ring.

**Header tabs.** As the dyson.com menu row: no boxes, 16px Light white, the selected tab 500 with a 2px white underline 9px above the line's foot; arrow keys move between tabs.


## Charts

| Question | View |
|---|---|
| Does each power mode last long enough? | Round screens with the gap to the MIN |
| Which targets block the review? | Spec rows with ✓ or ✗ |
| Where does the weight go, part by part? | Exploded view against budgets, the assembled bar against the MAX |
| Does the new part change what the machine leaves behind? | Laser floor, review build against now |
| How did a measure move against its target, build by build? | A graph screen of bars from the target line |
| Every other measure, review to now | Table with the current column on the panel band |
| Will the tests finish before freeze? | A test timeline on a graph screen |
| Who fixes what, by when? | Issue table, biggest first |

- A title states the finding ('The new cleaner head clears the edge but leaves Eco 3:20 short'), never the chart type.
- Bars grow from a meaningful line: zero, or the target when the question is the gap to the target. Never a dual axis, pie, donut, gauge or 3D.
- The exploded view is honest about scale: one length scale for every part. Because small weight changes are hard to see as length, every part carries its weight and gap in numbers, and the assembled bar holds the total.
- A part changed since the review is purple everywhere it appears, with the same balloon number.
- Do not repeat the same numbers in a chart and the table beside it: a table holds what the charts do not.


## Depth & Elevation

Flat. No card shadows, no gradients, no glow. Depth comes from the black screens on white and the one grey panel. The tooltip is the only element with a shadow. Rules are 1px; the only 2px lines are the selected tab, the focus ring and the hover outline on a graph screen.


## Interaction & Motion

- One filter: the model tabs (C45 · C60 · C90), kept in the URL (`?model=`), with `?lang=en|ko`. Every card follows the model.
- Every view has a tooltip on hover and focus, arrow-key and Home/End control with Esc to leave, a polite live region that reads the item, and a visually hidden data table.
- Motion, eased `cubic-bezier(.4,0,.2,1)`, all of it under 1.2s and none of it repeating:
  - Exploded view: the parts start assembled and slide apart along the axis to their even gaps (0.9s, 40ms a part); brackets fade in at 0.65s, balloons and labels at 0.75s.
  - Round screens: each ring draws round (0.9s, 120ms apart); the battery fills from the left 0.25s later.
  - Laser floor: a green line sweeps each strip (1.1s) and the dust lights up behind it.
  - Graph screens: bars grow from the target line, 35ms apart; test bars grow from the left, 70ms apart.
- `prefers-reduced-motion` shows the final state at once.


## Accessibility

- Text ≥ 4.5:1: ink 12.6:1, muted 7.5:1 (6.96:1 on the panel), red text 7.1:1, good 5.4:1; on black, white 21:1, `#b9b9b9` 10.4:1, red `#f0403a` 5.5:1. `#919191` only for large section numbers and dashes.
- Pass and miss are never colour alone: ✓ and ✗, the words 'short', 'over', 'spare', and the side of the target line.
- Mode colours always come with the mode's name; the dust count is also written as a percentage.
- Balloon numbers tie parts across views without colour.
- Each view's container is focusable with a label that states the finding; the hidden table carries the same values.


## Responsive Behavior

| Width | Layout |
|---|---|
| ≥ 1360px | First screen 1fr \| 478px |
| 1280–1359px | Right column 430px |
| 1200–1279px | Spec rows move under the round screens (2×2) |
| 1024–1199px | Right column 390px; sections 01 and 02 stack |
| 900–1023px | One column; the first screen stacks |
| 640–899px | Table 1 drops builds 38 and 39 |
| < 640px | Round screens a third of the width each, spec rows in one column, Table 1 shows builds 37 and 41 only, Table 2's due date goes under the fix, graph screens put the build 41 value at top right in 26px |

Nothing overflows or overlaps at 390px; long labels shorten ('DESIGN FREEZE' → 'FREEZE', one-line part labels).


## Tool Mapping

**Tableau.** Paste the palettes from `dyson.tps` into `Preferences.tps`. Dashboard `#ffffff`, sheets on white, the exploded view on a `#f7f7f7` container. Round screens: a dual-mark sheet is not needed; use a BAN (big number) on a black container with the mode name in its colour above it. Exploded view: a Gantt bar on one axis, `[Start] = running sum of weights + gap`, size = weight, colour by state (changed, over, other). Graph screens: a black worksheet shading, bars of `[Value] − [Target]` from a zero reference line drawn white dash-dot, colour by met/missed. Laser floor: a scatter of dust points on a black sheet. Fonts: Tableau Book unless Jost and Noto Sans KR are installed on every viewing machine and the server.

**Power BI.** Import `powerbi-theme.json` (white visuals, no border, square corners, Jost with Segoe UI fallback). Graph screens: a column chart of the gap to target on a `#000000` plot area with a white constant line at zero, conditional colour white/`#f0403a`. Exploded view: a stacked bar of parts with a transparent spacer series, or a custom visual. Misses: conditional font colour `#b0122f` with ✗ in the value.

**Web.** `tokens.css` gives every value as CSS variables. Draw with SVG; keep numbers as text, not baked into images.


## Do's and Don'ts

**Do**

- Put every measurement on black, like the machine's own screens, and keep the page white.
- Use Light numerals for measurements and Medium for labels; tabular figures.
- Say pass and miss with ✓ and ✗ next to the value.
- Keep one panel colour `#f7f7f7`; leave the rest white.
- Number parts with balloons and keep the numbers across views.
- Write the finding as the title.

**Don't**

- Don't fill table cells or chart backgrounds with green or red zones; a page of pastel zones reads as clutter.
- Don't use mode colours (Eco green, Auto blue, Boost red) outside the round screens, or as series colours.
- Don't repeat the first screen's devices (round screens, exploded view, laser floor) in smaller copies further down; later sections use graph screens and tables.
- Don't show the same numbers twice in a chart and the table beside it.
- Don't use the Dyson logo or typeface, photos, renders, drawings of cyclones or loops, screen icons, product or technology names, or real specifications.
- No dual axes, pies, donuts, gauges, gradients, glow or shadows on cards.


## Agent Prompt Guide

Start from the prompts in `prompt.md`. Before you finish, check:

1. The header is black in two lines with model (or product) tabs set like a menu row, and the page is white with one `#f7f7f7` panel.
2. KPIs are round screens (or spec rows) with the gap to the limit and ✓ or ✗.
3. Every chart that measures sits on a `#000000` screen with white Light values; colours there are white, grey `#5c5c5c` and red `#f0403a` only, except mode colours on round screens.
4. A changed part is purple with its balloon number on every view; red only marks a miss.
5. Titles state findings; captions say how it was measured.
6. No table cell or plot background is filled with a status colour; no numbers are repeated between a chart and its neighbouring table.
7. Text contrast ≥ 4.5:1; pass and miss never rely on colour alone.
8. Every view has a tooltip, keyboard control and a hidden data table; nothing overlaps at 390px.
9. No Dyson logo, typeface, photo, render, product or technology name, or real number.
