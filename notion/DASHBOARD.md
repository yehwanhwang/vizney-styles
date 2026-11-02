---
name: Notion style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 2
tagline: Monochrome, Blocks, Tidy
tagline_ko: 모노톤, 블록, 단정함
source: https://www.notion.com, https://notion.site
sample: https://styles.vizney.com/notion/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#ffffff"
  card: "#ffffff"
  surface: "#f6f5f4"
  surface-2: "#f9f9f8"
  callout: "#f9f8f7"
  tab: "#f4f4f3"
  ink: "#191918"
  body: "#31302e"
  text-2: "#615d59"
  muted: "#78736f"
  mark: "#a39e98"
  rule: "#dfdcd9"
  hair: "#e6e5e3"
  hair-2: "#f0efed"
  accent: "#0075de"
  accent-hover: "#005bab"
  accent-soft: "#e6f3fe"
  good: "#14832b"
  bad: "#b01601"
  focus: "#0075de"
data:
  categorical: ["#2783de", "#dd5b00", "#46a171"]
  other: "#c7c6c4"
  comparison: "#a39e98"
  categorical_text: ["#1f6fc5", "#ab4a00", "#14832b"]
  sequential: ["#7db1ea", "#5196e2", "#2271c4", "#1c5aa3", "#1d4677"]
  diverging: ["#ab4a00", "#dd5b00", "#ff8a33", "#dfdcd9", "#7db1ea", "#2271c4", "#1d4677"]
  good: "#14832b"
  bad: "#b01601"
typography:
  sans: { en: "Inter", ko: "Pretendard" }
  mono: "IBM Plex Mono"
radius: {card: "12px", callout: "10px", board: "10px", tooltip: "10px", button: "8px", button-lg: "10px", tag: "4px", status: "10px", view-tab: "20px", segment: "24px", chip: "4px", bar: "2px"}
spacing: {page: "32px", gap: "24px", section: "64px", card: "20px 24px 18px", card-head: "0 0 16px", card-foot: "14px 0 0", cell: "8px 10px", callout: "14px 16px", footer: "28px 32px 32px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: notion.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: sales.csv}
---

# Notion style — DASHBOARD.md

**Monochrome, Blocks, Tidy** · 모노톤, 블록, 단정함

A dashboard design spec read from the public design of notion.com and public Notion pages. It takes the site's measured design-system tokens and the way Notion shows data inside a page — the page head (icon, title, properties, callout), toggle headings and database views: the chart view, table and board, calendar, tags and status pills, number bars — and turns them into one card and one chart grammar that a whole dashboard can follow. It then adds what a website spec leaves out and a dashboard needs: validated data colors, card anatomy, chart rules, number and date formats in English and Korean, density, filters, accessibility, and settings for Tableau, Power BI and the web. Add it to a project with one command (or the zip on the sample page), or hand it to whoever builds your dashboards. The live sample was built from it.

```
npx @vizney/styles@latest add notion
# or, without Node:
curl -fsSL https://styles.vizney.com/install.sh | sh -s -- notion
```

That puts `DASHBOARD.md` in the project root and the `dashboard-style` agent skill (build, restyle, review) in `.claude/skills/dashboard-style/`, together with `tokens.css`, `tokens.json`, `notion.tps`, `powerbi-theme.json` and `prompt.md`. Coding agents that read skills pick it up whenever a task touches a dashboard or a chart; any other agent can be told to follow `DASHBOARD.md`.

- Live sample: https://styles.vizney.com/notion/?lang=en (Korean `?lang=ko`; one region `&region=texas`)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/notion/DASHBOARD.md
- Package: [notion-dashboard-style.zip](notion-dashboard-style.zip) (unzip in your project root) · the skill: [skill/SKILL.md](skill/SKILL.md)
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [notion.tps](notion.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [sales.csv](sales.csv) (the data behind the sample's Figure 1)
- Catalog: VIZNEY STYLES · 02 · https://styles.vizney.com (Vizney Styles is a line of [Vizney](https://www.vizney.com))

Not an official Notion design, and not affiliated with or endorsed by Notion. A reference style read from the publicly visible design of notion.com and public Notion pages; it carries no logo, typeface or data of theirs. The sample's company, Vizney Coffee, and all its numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A white page that reads like a Notion page turned into a report. It opens the way a Notion page does: a line icon, a bold title that states the result, three properties (scope, comparison, status) and a gray callout that names the drivers, with four number widgets beside the title. Below that, toggle headings (`Sales`, `Operations`, `How it's built`) hold database views on one card: white, a 1px hair border, a 12px radius, no shadow. Each card opens with a small view label (an icon and `Figure 1 · Net sales`), a bold title that states the finding, a gray subtitle that names the measure, then the view and a note that starts with `Note:`.

The views are the ones a Notion page uses for data: a chart view (lines and bars on dotted gridlines), a database table with tags, status pills, number bars and a calculation row, the same rows as a board grouped by status, and a month calendar in Notion Calendar's style, with values as text and events as all-day bars. It is mostly black, white and warm gray. Color appears only in the data — Notion blue for the subject, orange and gray when channels are compared — and in Notion's pastel tags and status pills. The data blue `#2783de` is the product's blue, a step apart from the button and link blue `#0075de`.

The mood is tidy and quiet: a team page you keep open, where every block lines up and nothing shouts.

Measured on the sites (November 2026): global navigation 64px; page width 78.25rem on a 12-column grid; buttons 38px (medium) and 28px (small) with an 8px radius, 16px/500 and 14px/500; primary `#0075de` (hover `#005bab`), secondary `#e6f3fe` with `#005bab` text, tertiary white with a `rgba(0,0,0,.1)` border; cards white with a `rgba(0,0,0,.1)` border and a 12px radius; the pricing toggle a `#f6f5f4` track with a 4px border, 24px radius and a white selected pill; text `rgba(0,0,0,.95)` and grays `#f9f9f8 #f6f5f4 #dfdcd9 #a39e98 #78736f #615d59 #494744 #31302e #191918`; card titles 22px/700 at −0.25px, stats 42px/700, headings 54px/700 at −1.875px. In public Notion pages: tags with a 4px radius, status pills with a 10px radius and an 8px dot, table rows 37px with `rgba(42,28,0,.07)` rules, board columns tinted by group with white 10px cards, view tabs as `rgba(33,27,23,.05)` pills, callouts `#f9f8f7` with a 10px radius, and chart views with dotted `#e6e5e3` gridlines, 12px `#7d7a75` ticks, 12px/600 value labels and bars rounded 2px at the top.


## Color Palette & Roles

Surfaces and text are notion.com's warm gray ladder; the rules are the product's.

| Token | Hex | Role |
|---|---|---|
| canvas · card | `#ffffff` · `#ffffff` | page · every figure, table and number widget (with a hair border) |
| surface | `#f6f5f4` | segmented-control track, period pill, hover band behind a bar or row |
| surface-2 | `#f9f9f8` | workbench side panel, calendar days outside the month |
| callout | `#f9f8f7` | the callout block |
| tab | `#f4f4f3` | the selected view tab (`rgba(33,27,23,.05)` on white) |
| ink / body | `#191918` / `#31302e` | titles, key figures, table values, the target line / running text, code |
| text-2 | `#615d59` | subtitles, notes, figure labels, values beside end labels (6.5:1) |
| muted | `#78736f` | property names, table headers, axis ticks, unselected tabs (4.7:1: the lightest gray for small text) |
| mark | `#a39e98` | gray marks that are not text: the comparison line, other regions' lines |
| rule / hair / hair-2 | `#dfdcd9` / `#e6e5e3` / `#f0efed` | crosshair / card borders, dividers, dotted gridlines, baselines / table rules, empty bar tracks |
| accent · accent-hover · accent-soft | `#0075de` · `#005bab` · `#e6f3fe` | buttons, links, focus. Data uses its own blue step, `#2783de` |
| good / bad | `#14832b` / `#b01601` | favourable / unfavourable change and missed targets, text only (4.9:1 / 7.1:1 on white) |
| focus | `#0075de` | focus ring, 2px, 2px offset |

Rules:
- White cards with a hair border; no shadows on cards and no gray cards. Gray fills are for controls, the callout and hover only.
- Small text on white uses muted or darker; on a gray or tinted surface (the segmented track, the callout, the package panel, board columns) it uses text-2 or darker, because muted falls just under 4.5:1 there. `#a39e98` and lighter are never text.
- Blue is Notion's key color in both places, with two steps: `#0075de` for buttons, links and focus, `#2783de` for data. Never swap them, and never put a second blue series next to the subject.


## Data Colors

Notion's chart view paints each series in a mid tone of the same palette its tags use, leading with blue (blue, purple, green, red, gray …), and the dashboards drawn on notion.com lead with blue bars and lines too. This spec keeps that palette and gives it roles: blue is the subject everywhere, orange and green are the other real categories, the product's chart gray is Other, and a darker step of each hue carries text. Every value passed an OKLab validator (color-vision-deficiency separation, normal-vision separation, contrast) on the white card `#ffffff`, where every chart sits. Use them exactly; do not generate tints.

| Role | Mark | Label text | Use |
|---|---|---|---|
| Subject | `#2783de` | `#1f6fc5` | the scope the report is about: this year, the selected region, the channel the story is about |
| Second category | `#dd5b00` | `#ab4a00` | a second real category (drive-thru) |
| Third category | `#46a171` | `#14832b` | only when a third real category exists |
| Other | `#c7c6c4` | text-2 | the rest (in-store), behind 2px white gaps |
| Comparison | `#a39e98`, dashed 2px (6 on, 4 off) | ink | last year; also other regions as 1.5px solid lines |
| Target | `#191918`, dashed 1.2px (4 on, 3 off) | ink | a goal on an axis (`Target 4:00`); a 2px ink tick on bars |
| Sequential | `#7db1ea` `#5196e2` `#2271c4` `#1c5aa3` `#1d4677` | ink on the first two, white on the last three | color by value when a heat map is the only form that works; use sparingly, never for a whole month of cells |
| Diverging | `#ab4a00` `#dd5b00` `#ff8a33` · `#dfdcd9` · `#7db1ea` `#2271c4` `#1d4677` | each arm's darkest | above and below a midpoint |
| Status | good `#14832b`, bad `#b01601`, neutral `#a39e98` | — | change text only |

Tags and status pills are not data marks; they are Notion's select and status properties, a pastel background with dark text:

| Tag | Background | Text | Dot (status) |
|---|---|---|---|
| gray | `#e6e5e3` | `#494846` | `#8e8b86` |
| orange | `#f3ddcb` | `#6a4222` | `#d5803b` |
| green | `#d7e6dd` | `#2a533c` | `#46a171` |
| yellow | `#f2e3b7` | `#655121` | `#d8a32f` |
| red | `#f7d9d5` | `#6d3531` | `#e56458` |
| purple | `#e8dbf2` | `#553b69` | `#b577d6` |
| blue | `#cee3f7` | `#264a72` | `#2783de` |

Validation (from `tokens.json`, on white):
- Blue, orange and green pass every check, all pairs. The worst pair under color-vision deficiency is green↔orange at ΔE 9.8 (deutan); blue sits 20.1 or more from both; normal vision 20.8 or more. Contrast 3.90, 3.77 and 3.18:1: every mark clears 3:1.
- Other `#c7c6c4` is neutral by design: CVD 19.6 or more and normal vision 21.8 or more against the three hues. At 1.71:1 it always has a second cue: white gaps, value labels and a table.
- Comparison `#a39e98` against blue: 16.5 / 19.8. At 2.66:1 it is always dashed and labeled at its end.
- The sequential ramp is one hue (spread 4°), monotone, every gap ≥ 0.06 in lightness, light end 2.25:1. Text on a cell is ink on the two light steps (7.8, 5.7:1) and white on the three dark steps (5.0, 6.9, 9.6:1).
- The diverging arms each pass the ordinal checks (light ends 2.35 and 2.25:1); the poles are 18.8 / 27.0 apart.
- Good and bad pass as text but do not separate for deutan vision (ΔE 4.3), and the status dots are 6.2 apart. Status is never color alone: changes keep their sign and comparison words, pills keep their labels.

Rules:
- At most three hues plus gray in one chart. A fourth real category folds into Other or becomes small multiples.
- Color follows the entity, not its rank: the subject is blue in every figure; other regions are gray, never a second blue.
- Never put the button blue `#0075de` on data, and never a yellow series beside orange.
- Tags carry names, not quantities. Do not use tag colors to encode a measure.


## Typography Rules

| Role | English | Korean | Weights |
|---|---|---|---|
| Sans (everything) | Inter | Pretendard | 400, 500, 600, 700 |
| Mono (code only) | IBM Plex Mono | IBM Plex Mono, then Pretendard for Hangul | 400, 500 |

Inter stands in for NotionInter. notion.com's Korean pages load no Korean webfont (the browser falls back to system fonts), so Korean uses Pretendard. There is no serif: Notion keeps its serif for testimonials, and a dashboard has none.

| Element | Size / weight | Notes |
|---|---|---|
| Title (headline) | `clamp(30px, 2.95vw, 42px)` / 700, line-height 1.14, −0.035em | one sentence that states the result; `text-wrap: balance` |
| Key figure value | 38px / 700, −0.035em | units at 0.45em in text-2 (`$ 1.90 M`, `3:48 min`, `190 만 달러`, `3분 48초`) |
| Section title | 26px / 700, line-height 32px | after a toggle caret, under a hair divider |
| Section intro, callout | 16px / 400, line-height 24px | text-2 / body |
| Card title | 20px / 700, line-height 28px, −0.012em | the finding; `text-wrap: balance` |
| Card subtitle · table · table header | 14px / 400 | text-2 · ink · muted with a property icon |
| Figure label | 13px / 500 text-2 | a 16px view icon and `Figure 3 · Transactions by day` |
| Key · note | 13px / 500 · 13px / 400 | the note starts with `Note:` / `주:` |
| Axis ticks · value labels | 12px muted · 12px / 600 ink | |
| Tags · status pills | 14px (12px on board cards) | 20px tall |
| Calculation label | 11px / 500 uppercase, 0.06em, muted | `COUNT 9`, `SUM $1.90M` (Korean 12px, no tracking) |
| Segmented control · buttons | 14px / 700 · 16px / 500 (small 14px / 500) | |
| Code | mono 12.5px, line-height 1.62 | |

Headings are bold and tight; body text is regular. Korean breaks between words (`word-break: keep-all`), and a number stays on the same line as the particle after it (`27%에`, `21일`).


## Numbers, Dates & Units

| | English | Korean |
|---|---|---|
| Money per order | `$7.93` | `7.93달러` |
| Large money | `$1.90M`, `$248K` | `190만 달러`, `24.8만 달러` |
| Money axis | `$1.4M $1.6M … $2.2M` (one decimal count per axis) | `140만 160만 … 220만`, with the unit in the subtitle (`월별 순매출(달러)`) |
| Counts | `240K` (key figure), `7,365` (text), `9.1K` (calendar) | `24만 건`, `7,365건`, `9,132` |
| Rates | `26.9%`; whole numbers on axes and labels of small charts (`27%`) | the same |
| Points | `−0.4 pts` | `−0.4%p` |
| Durations | `3:48` (min:sec), change `−0:18` | `3분 48초`, change `−18초` |
| Change | `+7.8% vs Oct 2025` | `+7.8% 전년 동월 대비` |
| Dates | `October 31, 2026`; `Saturday, October 31`; ticks `Oct 1 … 31`, `Nov … Oct` | `2026년 10월 31일`; `10월 31일 토요일`; `10월 1일 … 31`, `11월 … 10월` |
| Hours | `8 a.m.`, `noon`; ticks `6 am … 6 pm` | `오전 8시`, `낮 12시`; ticks `6시 … 18시` |

- Money is in the company's own currency; the sample's company is American, so US dollars.
- Signs use the true minus (`−`, U+2212). One decimal for change.
- The change color follows whether the move is good for that metric: handoff `−0:18` is green.
- Units and suffixes are smaller than the digits.
- Missing values are left blank in a table, as Notion does; the reason goes in the note.


## Layout Principles

One column on a white page, at most 1400px wide, 32px side padding (24px up to 1359px, 16px below 640px), a 24px gap between cards and 64px between sections. No sidebar, no app chrome, no logo.

1. **Header** (64px): company name (16px / 700) and report name (14px text-2). On the right: a period pill, the EN/KO segmented control, a tertiary `Export PDF` and the one primary button, `Copy as Markdown`.
2. **Filter row** between two hairlines: the segmented control with the regions on the left, the basis (`As of October 31, 2026 · vs October 2025`) on the right. It scopes every card, and the URL keeps the choice (`?region=texas`).
3. **Page head**: on the left (7 of 12 columns) a 44px line icon, the title that states the result, and three properties (`Scope`, `Compared with`, `Status`); on the right (5) four number widgets, 2 × 2, bottom-aligned with the properties. Under both, a full-width callout with the drivers, then a contents line of links.
4. **Sections**: a hair divider, a toggle caret, a 26px title and a one-line intro; the caret collapses the section. Rows of cards on a 12-column grid; cards in one row share a subgrid, so their heads, bodies and notes line up.
   - `Sales`: Figure 1 net sales (7) · Figure 2 channels (5); Table 1 stores (12), with Table and Board views.
   - `Operations`: Figure 3 calendar (7) · Figure 4 hours (5); Figure 5 handoff (7) · Figure 6 fall menu (5).
5. **`How it's built`**: a paragraph with two buttons (`Read DASHBOARD.md`, `Get one for your company ↗`), three numbered steps, then the workbench window and a caption.
6. **Notes + linked pages**, 7 / 5, on the same card.
7. **White footer** above a hairline.

At most seven views on one screen: the number widgets and three views in Sales, four in Operations. Every view is a standard form an agent or a BI tool can rebuild. A chart's body fills its card, so a chart beside a taller one grows to its height. Density: at 1440 × 900 the header, filter row, title, properties and all four number widgets are on the first screen. Reading order follows the list; never lead with a chart.


## Component Stylings

- **Card**: white, 1px `#e6e5e3` border, 12px radius, 20px 24px 18px padding, no shadow. Three parts on a subgrid: head (view label with any view tabs on the right → title → subtitle → keys, 16px below), body (the view), foot (`Note:` 13px text-2, 14px above). Never a card inside a card.
- **Buttons** (measured): 38px, 8px radius, 16px / 500, icon before the label. Primary: `#0075de`, white text, hover `#005bab`. Secondary: `#e6f3fe`, `#005bab` text, hover `#f2f9ff`. Tertiary: white, `rgba(0,0,0,.1)` border, hover `#f6f5f4`. Small: 28px, 14px / 500. Icon-only: 28 × 28.
- **Segmented control** (the region filter, EN/KO, `Without a spec / With DASHBOARD.md`): a `#f6f5f4` track with a 4px border of the same color and a 24px radius; 30px options with 16px padding, 14px / 700 text-2; the selected option is a white pill with ink text and a hairline shadow. `role="tablist"`, arrow keys move. Small: 3px border, 26px options, 13px.
- **View tabs** (in a card head: `Table · Board`, `Weekdays · Weekends`): 28px, 20px radius, 14px / 500, an icon before the label; muted when off, ink on `#f4f4f3` when selected.
- **Number widget** (key figure): a card with 16px 18px 14px padding; label 14px / 600 ink with a muted icon → value → change line (14px text-2, the change in 600 status color, then `vs Oct 2025`). Two text sizes besides the value; the four share a subgrid so values line up.
- **Properties**: rows 32px high; the name 14px muted with a 16px icon, the value 14px ink; a status value is a status pill.
- **Callout**: `#f9f8f7`, 10px radius, 14px 16px padding, a 20px line icon, 16px / 24px body text.
- **Toggle heading**: a 28px caret button (rotates −90° when closed, `aria-expanded`), then the title.
- **Tags** (select property): 20px high, 4px radius, 0 6px padding, 14px, pastel background and dark text from the tag table. **Status pills**: 10px radius, 0 9px 0 7px padding, an 8px dot in the status color. On track green, Watch yellow, Off track red.
- **Table** (database table view): 14px, rows 37px, cells 8px 10px, `#f0efed` rules on every row and between columns, a rule above the header. Header cells 14px muted with a 14px property icon (`Aa` title, select, `#` number, target, clock, status). Numbers right-aligned with tabular figures; the title column 500. A calculation row closes the table: `COUNT 9`, `SUM $1.90M`, `ON TRACK 6 of 9`, each a calculation label then the value.
- **Number bar** (a number shown as a bar): 120px × 6px on a `#f0efed` track, 3px radius, the value in the subject color, a 1.5px ink tick at the target (100%), the value after it as text. 0–120%.
- **Board** (the same rows grouped by status): one column per group, tinted with the group's lightest color (`#f6f9f7`, `#fcfaef`, `#fdf6f6`), 10px radius, 0 8px 8px padding; a header with the status pill and the count in text-2; white cards with a 10px radius and the shadow `0 0 0 1px rgba(42,28,0,.07), 0 4px 12px rgba(25,25,25,.027), 0 1px 2px rgba(25,25,25,.02)`: name 14px / 600, tags, then a two-column list 12px (property muted, value ink).
- **Calendar** (Notion Calendar's month view): seven columns from Sunday; weekday names 12px muted, left-aligned, in a 30px header row; one row per week, at least 84px, with `#f0efed` rules; the weekend columns shaded `#f9f9f8`, as Notion Calendar shades them. The date sits top left (12px / 500 text-2; the first day reads `Oct 1` · `10월 1일`); the value is plain text at the bottom left (14px / 500 ink, tabular figures), and only the days the title names (Saturdays in the sample) are colored, 600 in the subject's text blue `#1f6fc5`. No chips, fills or bars around values. Events are Notion Calendar all-day events between the date and the value: 22px high, 4px radius, a pale fill, a 3px bar on the left and darker text of the same color, 12px / 500, an emoji before the title. One color per calendar, as in Notion Calendar's sidebar: Marketing orange (fill `#fbebdf`, bar `#dd5b00`, text `#8a3c00`), Operations green (`#e4f1e9`, `#46a171`, `#2a533c`), Holidays purple (`#f1e9f8`, `#b577d6`, `#553b69`); the key lists the calendars with 12px rounded squares. A multi-day event runs across the days as one bar; at a week break it continues on the next row with its title repeated, and the joined ends lose their radius and left bar. Overlapping events stack in lanes. Events only annotate the days; they never color the values.
- **Tooltip** (popover): white, 10px radius, padding 8px 11px 9px, shadow `0 0 0 1px rgba(42,28,0,.08), 0 8px 18px rgba(25,25,25,.08), 0 2px 6px rgba(25,25,25,.05)`; a 12px muted title, then rows of key (square, or a line for line series, dashed for the comparison), value 600 ink, label text-2. It takes the first side that fits inside the card: above, left, right, below.
- **Toast**: ink, white text, 10px radius, bottom center, 2.2s.
- **Workbench window**: white, 12px radius, hair border, notion.com's `shadow-300`. A 240px package panel on `#f9f9f8` (file names in mono 12px with a one-line description, install commands in white boxes with a copy button), the figure pane (segmented `Without a spec / With DASHBOARD.md`, an inline-code chip `region = all` in `#b01601` on `rgba(135,131,120,.15)`, title, plot, note, then **Checks · DASHBOARD.md**), and the code pane (tabs `Prompt · plan.md · figure-1.js · Tableau · Power BI` with an ink underline, a copy button and a primary `Run again`, line-numbered code, a status bar). Syntax: comment `#78736f`, string `#14832b`, number and function `#b01601`, keyword `#005bab`, property `#31302e` 500.
- **Notes**: a numbered list, 14px text-2, ink numbers. **Linked pages**: a page icon, the date 12px muted over a 15px / 500 title underlined in `rgba(55,53,47,.25)`, an arrow on the right, `#f0efed` rules between.
- **Footer**: white over a hairline, 13px text-2; the catalog line in ink, the series in 12px / 600 with 0.06em tracking.


## Charts

- **Choose by the question.**
  - A trend against last year → a line with last year dashed gray and both line ends labeled (Figure 1).
  - Composition over time → 100% stacked bars per month, the subject at the bottom, value labels beside the last bar (Figure 2).
  - Many entities against two goals → a database table with a number bar for the target and a status pill; the same rows as a board grouped by status (Table 1).
  - A daily pattern within a month → a month calendar in Notion Calendar's style: values as text, the days the title names in blue text, weekends shaded, and the events that explain the days as all-day event bars, single- or multi-day (Figure 3).
  - A distribution over the day → bars by hour in gray with only the peak hour in blue and labeled, view tabs for weekdays and weekends (Figure 4).
  - A daily measure against a target, with peers → the subject's line in blue, peers in thin gray, the target as a dashed ink line and `↓ Faster` when lower is better (Figure 5).
  - Items against their own goals → horizontal bars with a goal tick, blue when the item meets its goal and orange when it misses, and a matching blue or orange tag per row (Figure 6).
- **Titles.** The card title is the finding (`Saturdays averaged 27% more transactions than weekdays, and Halloween was the busiest day`), recomputed when the filter changes. The subtitle names the measure and period; the note explains the method and the source.
- **Marks.** Lines 2.5px for the subject, 2px for the comparison, 1.5px for peers; a hollow end marker on the subject. Bars up to 28px wide (24px by hour, 18px tall horizontal), rounded 2px at the end, 2px white gaps between stacked segments.
- **Axes.** Dotted horizontal gridlines `#e6e5e3` (1 on, 3 off), a solid `#e6e5e3` baseline, no vertical axis line; ticks 12px muted, four or five nice ticks, one decimal count per axis; the current month or last day in ink.
- **Labels.** Line ends carry `Name value` instead of a legend; the peak bar carries its value in the subject's text color; values beside bars 12px / 600 ink. Labels over marks have a white halo.
- **Keys** only where labels cannot do the job, as a one-line row in the card head (swatch 12px with a 2px radius, a line, a dashed line, a tick, or a five-step ramp between `Fewer` and `More`).
- **One axis.** Never a dual axis.
- **Never:** pie, donut, 3D, gradients or gradient areas, smoothed lines, the button blue on data, a fourth hue, tag colors as a measure.
- Every chart has a hover tooltip, keyboard control and a screen-reader table.


## Depth & Elevation

Flat. Cards are set apart by a hairline, not by shadows, and never lift on hover. Shadows exist only on board cards (a hairline ring and a soft 12px blur), the tooltip, the toast and the workbench window.


## Interaction & Motion

- **Filter**: the segmented control scopes everything; changing it rewrites the title, properties, callout, number widgets, card titles and notes, and redraws every view. The URL keeps the region.
- **View tabs** switch Table 1 between Table and Board and Figure 4 between weekdays and weekends. **Toggle headings** collapse a section.
- **Hover** shows the tooltip and a crosshair, a hollow dot, a `#f6f5f4` band behind a bar or row, or an ink ring around a calendar day; touch taps pick and a tap elsewhere clears.
- **Keyboard**: every chart and the calendar are focusable; arrow keys step (up and down move a week in the calendar), Home and End jump, Esc clears, and a live region reads the value. Segments and tabs move with arrow keys.
- **Workbench**: the first time it scrolls into view, the code types itself (55ms a line, 380ms between steps) and each step draws its layer of Figure 1 (frame → comparison line → subject line → end labels → title and note) and ticks its checks. Hovering a line of code spotlights its layer; hovering the chart highlights its code. `Without a spec` shows a typical first draft and fails all six checks. Changing the filter rewrites the `region` value and flashes that line.
- `Copy as Markdown` copies the whole report as Markdown with a toast; `Export PDF` prints.
- Motion: lines draw in 0.7s, bars grow in 0.45s, labels fade in 0.3s, `cubic-bezier(0,0,.58,1)`; controls change in 0.2s. `prefers-reduced-motion` turns all motion off and shows the workbench finished.


## Accessibility

- Text ≥ 4.5:1 on its surface: muted 4.7:1 and text-2 6.5:1 on white; good 4.9:1, bad 7.1:1; blue text 5.1:1, orange text 5.7:1; tag text 5.8:1 or more on its tag; white on the primary button 4.6:1; code token colors ≥ 4.5:1.
- Marks below 3:1 (Other 1.71:1, comparison 2.66:1, the gray bars of the hours chart and the calendar) always have a second cue: a gap, a dash, a label, a value in the cell or a table.
- Identity is never color alone: names at line ends, labels on pills and tags, dashes for comparisons and targets, signs on every change.
- Focus ring `#0075de`, 2px, 2px offset. Tab order: header → filter → sections in reading order.
- Real tables with `scope`; every chart has a hidden data table and an `aria-label` that says what it shows.


## Responsive Behavior

Each step keeps what the wider steps changed.

- ≥ 1360: as laid out above.
- 1200–1359: 24px padding, 20px gaps, 56px between sections; cards padded 18px 20px 16px; table cells 8px 8px; number bars 96px; the workbench lifts its package panel into one row above the figure and the code.
- 1024–1199: the same rows; number values 36px; code 12px with wrapped lines.
- 900–1023: cards stack one per row; the page head stacks, with the four number widgets in one row (values 32px); the workbench is one column.
- 640–899: a 56px header without the report name or `Export PDF`; the basis line leaves the filter row; number widgets 2 × 2; steps stack; the table drops Format and vs Oct 2025.
- < 640: 16px padding, 12px gaps, 44px between sections; the period pill and `Copy as Markdown` leave the header; region segments 13px; title 27px, number values 28px, section titles 22px, card titles 17px; cards padded 16px 14px 14px; the table keeps Store, Net sales and Status; the board is one column; calendar rows 62px with 11px text, events drawn as 8px bars without titles (the tooltip names them), the month name dropped from the first day; long item names end in `…`.
- Embedded in a post (`?embed=1`): the footer hides and the page reports its height to the host page.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` (installed in `.claude/skills/dashboard-style/`; or copy the `colors` block from the front matter) and these fonts (the second for Korean). Tag colors are `--tag-<color>-bg`, `--tag-<color>-text` and `--tag-<color>-dot`.

<!--email_off-->

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
```

<!--/email_off-->

**Tableau.** Paste the `<color-palette>` elements of `notion.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette runs blue, orange, green, Other and the comparison gray; assign the subject first.
- Dashboard background `#ffffff`; each sheet in a container with a 1px `#e6e5e3` border and 20/24px inner padding. Worksheet shading white.
- The card head: a text object with the figure label (Tableau Book 9, `#615d59`), the finding as the sheet title (bold, 13–14pt, `#191918`) and the measure as a subtitle line; the method in the caption, starting with `Note:`.
- Grid lines: rows only, dotted, `#e6e5e3`; zero line `#e6e5e3`; no axis rulers on the value axis; ticks Tableau Book 9 in `#78736f`.
- Lines: subject size 3, comparison dashed. Target: a reference line, constant, dashed ink, labeled `Target 4:00`. Stacked bars: Color → the categorical palette, Format → Borders → white separators.
- Calendar: a text table of WEEKDAY(day) by WEEK(day), weekend columns shaded `#f9f9f8`, the value as a label, `#1f6fc5` bold for Saturdays and ink for other days; events as annotations or a Gantt bar sheet above.
- Table: a text table with row dividers `#f0efed`, the target as a bar in a second sheet or a Gantt bar with a reference line at 100%, status as a circle mark in the status dot colors beside the label.
- Formats `$#,##0.00`, `$#,##0,K`, `0.0%`, `+0.0" pts";−0.0" pts"`, durations `m:ss` from seconds; Korean workbooks `#,##0.00"달러"` and `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Inter is installed on every viewing machine and on the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json`. It sets the data colors (blue, orange, green, then Other), the white page, white visuals with a 1px `#e6e5e3` border and a 12px radius, axis and gridline colors and text classes. Install Inter on authoring and viewing machines or accept Segoe UI.
- Title each visual with the finding; put the measure in the subtitle and the method in a text box starting with `Note:`.
- Gridlines dotted; data labels on the last point instead of a legend; a constant line for the target, dashed ink.
- Table: conditional formatting → data bars in `#2783de` for the target column, icons or font color in the status colors for status, `#b01601` for missed handoff times.
- Calendar: a matrix of weekday by week, the value as text (font color `#1f6fc5` for Saturdays by conditional formatting), weekend columns `#f9f9f8`; events in a separate table or as tooltips.
- Key figures as cards with a `#e6e5e3` border and a 12px radius; change measures with conditional formatting in `#14832b` / `#b01601` only.

**Chart libraries (D3, Observable Plot, Vega-Lite, matplotlib, Datawrapper).** Subject `#2783de` (labels `#1f6fc5`), second `#dd5b00` (`#ab4a00`), Other `#c7c6c4`, comparison `#a39e98` dashed `6 4`, target `#191918` dashed `4 3`, gridlines `#e6e5e3` dashed `1 3` on rows only, ticks `#78736f` at 12px, plot background white, bar ends rounded 2px. The sample's Figure 1 in five forms is in the workbench of the live sample; `sales.csv` is its data.


## Do's and Don'ts

- Do open with a title that states the result, three properties, a callout with the drivers and four number widgets. Don't lead with a chart or a dozen KPI tiles.
- Do put every view on the same white card with the same head and foot. Don't mix shadows, gray cards and borderless panels.
- Do choose the form by the question (line, stacked bars, database table and board, calendar, bars by hour, lines against a target, bars against goal ticks). Don't fall back to the same bar chart in every card.
- Do keep blue for what the title is about (the subject, the peak, the highlighted days) and paint the rest gray; a card that is mostly blue has nothing highlighted. Do paint the subject Notion blue `#2783de` and everyone else gray. Don't put the button blue, a fourth hue or a tag color on data.
- Do title each card with its finding and explain the method in the note. Don't title a chart with its measure alone.
- Do use tags and status pills for names and states, with their labels. Don't let a dot or a color stand alone.
- Do use dotted gridlines on rows only and label line ends. Don't keep a legend that labels could replace.
- Do keep tables in Notion's grammar: hairline rules, property icons in the header, a calculation row. Don't zebra-stripe or tint whole rows.
- Do keep seven views or fewer on one screen. Don't add a card only to show a token.
- Don't put a logo, a wordmark, an emoji page icon or a photo anywhere.


## Agent Prompt Guide

Install the style (`npx @vizney/styles@latest add notion`, `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- notion`, or unzip the package in the project root). Agents that read skills load `dashboard-style` on their own and work in one of three modes: **Build** (plan the views, then draw them to this file), **Restyle** (move an existing screen onto this file without changing its data) and **Review** (a table of rule, finding, severity and fix). For an agent without skills, start the prompt with `Read DASHBOARD.md and follow it exactly.` For example:

```
Read DASHBOARD.md and follow it exactly. Build our monthly store operations dashboard as one self-contained HTML file
with fictional data, in English and Korean (?lang=en|ko, English by default).
Top: header with the period pill, EN/KO segmented control, Export PDF and Copy as Markdown; one segmented filter row of
regions that scopes every card. Then a page head: a line icon, a title that states this month's result, three properties
(scope, compared with, status pill), four number widgets 2 × 2 with changes vs last year, a callout with the drivers.
Sales (toggle heading): net sales by month against last year beside channel shares as 100% stacked bars; a stores
database table with tags, a target number bar, handoff time, a status pill and a calculation row, with a Board view.
Operations: a month calendar in Notion Calendar's style with each day's transactions as text (Saturdays in blue) and the month's events as all-day bars beside orders by hour in gray with the peak hour blue, with weekday/weekend tabs; daily
handoff time against a 4:00 target beside fall menu items against their goals.
Every view on the same card: figure label, finding title, subtitle, keys, view, "Note:". At most seven views per screen.
Use only the values in Data Colors, the formats in Numbers, Dates & Units and the components in Component Stylings.
Every chart needs a hover tooltip, keyboard control and a screen-reader table.
```

Before it is done, the agent checks:
- [ ] The title states the result; the callout names the drivers; number widgets carry signed changes colored by good or bad.
- [ ] Every view sits on the same white card; every card title states a finding; every note starts with `Note:` and explains the method.
- [ ] The subject is `#2783de` everywhere; peers and Other gray; comparison dashed `#a39e98`; no button blue, fourth hue or tag color on data.
- [ ] Gridlines dotted on rows only; line ends labeled; keys only where labels cannot work; no dual axis, pie, donut or gradient.
- [ ] Tags and status pills use the tag table and keep their labels; tables have hairline rules, header icons and a calculation row.
- [ ] Numbers, dates and durations follow the formats in both languages.
- [ ] Text ≥ 4.5:1 on its surface; marks below 3:1 have a second cue.
- [ ] Every chart has a tooltip, keyboard control and a data table; the filter changes every card; at most seven views per screen; nothing breaks at 390px.
