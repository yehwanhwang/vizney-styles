---
name: Singapore Airlines style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 5
tagline: Premium, Boarding Pass, Courteous
tagline_ko: 프리미엄, 탑승권, 단아함
source: https://www.singaporeair.com
sample: https://styles.vizney.com/singapore-airlines/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#fafafa"
  paper: "#ffffff"
  plot: "#ffffff"
  navy: "#00266b"
  navy-700: "#001a4f"
  tint: "#e5e9f0"
  tint-2: "#edf4ff"
  grey-blue: "#a6b4cd"
  rule: "#e5e9f0"
  edge: "#c8d6f1"
  hair: "#dddddd"
  orange: "#ff9f00"
  gold: "#946e31"
  ink: "#222222"
  body: "#222222"
  text-2: "#666666"
  muted: "#666666"
  faint: "#999999"
  link: "#0045c5"
  cab-j: "#12447d"
  cab-s: "#4f635f"
  cab-y: "#084935"
  fz: "#e2eee8"
  good-bg: "#cdf0cf"
  bad-bg: "#fff1f0"
  warn: "#ba5400"
  warn-bg: "#fff5e5"
data:
  categorical: ["#0096ae", "#005584", "#c3892a"]
  other: "#afafaf"
  comparison: "#868ba0"
  categorical_text: ["#00788c", "#005584", "#946e31"]
  sequential: ["#74bfcc", "#34a3b8", "#00869e", "#00677b", "#004a59"]
  diverging: ["#8a5a14", "#b57e27", "#d9ab62", "#dddddd", "#74bfcc", "#1f9bb2", "#006a7f"]
  good: "#03760b"
  bad: "#dc0202"
typography:
  sans: { en: "Figtree", ko: "Pretendard" }
  display: { en: "Source Sans 3", ko: "Pretendard" }
  mono: "Source Code Pro"
radius: {card: "4px", pass: "8px", widget: "0 0 16px 16px", tab: "16px 0 0 0", button: "4px", pill: "40px", chip: "4px", tooltip: "4px", bar: "0"}
spacing: {page: "32px", gap: "16px", section: "44px", card: "18px 22px 16px", widget: "24px 28px 22px", field: "12px 16px 14px", footer: "24px 32px 36px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: singapore-airlines.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: monthly.csv}
---

# Singapore Airlines style — DASHBOARD.md

**Premium, Boarding Pass, Courteous** · 프리미엄, 탑승권, 단아함

A dashboard design spec read from the public design of singaporeair.com, its monthly operating statistics and annual report, and the places passengers meet the airline: the boarding pass, the seat map and the booking widget. Singapore Airlines reports its month as a short release and a table of operating statistics, and draws its annual-report charts in thin teal with the unit above the axis. This spec turns those into dashboard parts — the boarding pass as the key figures, the seat map as cabin load, the release and its table as the headline and the detail — under singaporeair.com's navy tab bar, white panels and orange hairlines.

```
npx @vizney/styles@latest add singapore-airlines
# or, without Node:
curl -fsSL https://styles.vizney.com/install.sh | sh -s -- singapore-airlines
```

That puts `DASHBOARD.md` in the project root and the `dashboard-style` agent skill (build, restyle, review) in `.claude/skills/dashboard-style/`, together with `tokens.css`, `tokens.json`, `singapore-airlines.tps`, `powerbi-theme.json` and `prompt.md`. Coding agents that read skills pick it up whenever a task touches a dashboard or a chart; any other agent can be told to follow `DASHBOARD.md`.

- Live sample: https://styles.vizney.com/singapore-airlines/?lang=en (Korean `?lang=ko`; one route region `&region=europe`)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/singapore-airlines/DASHBOARD.md
- Package: [singapore-airlines-dashboard-style.zip](singapore-airlines-dashboard-style.zip) (unzip in your project root) · the skill: [skill/SKILL.md](skill/SKILL.md)
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [singapore-airlines.tps](singapore-airlines.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [monthly.csv](monthly.csv) (the data behind the load factor by month)
- Catalog: VIZNEY STYLES · 05 · https://styles.vizney.com (Vizney Styles is a line of [Vizney](https://www.vizney.com))

Not an official Singapore Airlines design, and not affiliated with or endorsed by Singapore Airlines. A reference style read from the publicly visible design of singaporeair.com and its public touchpoints such as the annual report, monthly operating statistics, seat maps and the app's boarding pass; it carries no logo, typeface, photo or data of theirs. The sample's company, Vizney Air, and all its numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A courteous airline that reports its month on a boarding pass. The page is `#fafafa` under a white header; the route-region filter is singaporeair.com's booking-widget tab bar in navy `#00266b`, the chosen tab white with only its top-left corner rounded 16px, joined to a white panel whose bottom corners round 16px. The panel opens like the monthly release — `Traffic rose 10.9% year-on-year on 9.7% more capacity, and the load factor came in at 86.5%, 0.8 pts above plan.` — beside a 3px orange hairline, then a lead paragraph and the boarding pass.

Three devices carry the report, each built to be read before it is admired. The **boarding pass** is the key-figure row: a navy band, FROM ORD → TO the route region, five fields, and the navy stub with the load factor where the seat number sits; the barcode's place holds passengers by day against the daily average. The **seat map** is cabin load: one 247-seat layout on its side, cabin bands in the cabin colours, seats sold on an average flight. The **operating statistics table** is the detail, in the annual report's order: a navy head, route-region bands, a separate sign column, `n.m.`, Systemwide under a navy rule. Everything else is quiet: thin teal, gray, white space, the unit above the axis.

Restraint is the tone: no shadows on cards, no gradients, no photos, no ornaments. Navy frames, orange is a hairline, teal is the one data colour, red only says that something fell short. Every number answers a decision: against plan and last year, routes ranked by their margin over breakeven, capacity added this year on a route map, the hub's evening bank where departures run late.

Measured in a browser on November 4, 2026 (singaporeair.com/en_UK/sg/home and /ko_KR/kr/home, the KrisFlyer pages, the investor pages, the annual report and seat map PDFs): `--brand-siaBlue #00266b`, `--brand-siaOrange #ff9f00` (also `--color-background-hairline`), `--brand-siaGold #946e31`; grays nightBlack `#222`, extraDarkGrey `#666`, darkGrey `#afafaf`, mediumGrey `#999`, lightGrey `#ddd`, extraLightGrey `#fafafa`; lightBlue `#e5e9f0`, brightLightBlue `#edf4ff`, greyBlue `#a6b4cd`, linkBlue `#0045c5`, stroke `#c8d6f1`; alerts success `#03760b` on `#cdf0cf`, error `#df0000` on `#fff1f0`, warning `#ba5400` on `#fff5e5`; cabin colours business `#12447d`, premium economy `#4f635f`, economy `#084935` (the 'standard' steps); spacing 0 2 4 6 8 12 16 20 24 32 40 48 64 80; buttons 4px radius, pills 40px; titles with a 3px `#ff9f00` left border and 15px padding; h2 24px / 400 navy.


## Color Palette & Roles

| Token | Hex | Role |
|---|---|---|
| canvas | `#fafafa` | page background (extraLightGrey) |
| paper · plot | `#ffffff` | cards, the widget panel, the boarding pass, the table; charts sit on their card |
| navy · navy-700 | `#00266b` · `#001a4f` | headings, the tab bar, the pass band and stub, the table head, primary buttons, focus · hover and the stub's top band |
| tint · tint-2 | `#e5e9f0` · `#edf4ff` | table group rows, card borders and rules, land on the route map · hover rows, the evening-bank band, highlighted code |
| grey-blue · edge | `#a6b4cd` · `#c8d6f1` | axis lines and ticks, empty seat outlines · the pass and tooltip frames, outlined controls |
| hair | `#dddddd` | neutral fills, the diverging midpoint |
| orange | `#ff9f00` | the hairline: 3px title bars, header separators, the active code tab. Never data, never text on white (2.06:1) |
| gold | `#946e31` | figure labels and step numbers (4.63:1) |
| ink · text-2 · faint | `#222222` · `#666666` · `#999999` | body and values (15.9:1) · secondary text, axes, notes (5.74:1) · line numbers only |
| link | `#0045c5` | links |
| cab-j · cab-s · cab-y | `#12447d` · `#4f635f` · `#084935` | cabin bands on the seat map, always with the code and seat count in white; a frame, not data |
| fz | `#e2eee8` | the forward-zone band behind the first five Economy rows |
| good · bad (with backgrounds) | `#03760b` on `#cdf0cf` · `#dc0202` on `#fff1f0` | the site's alert chips; change text |
| warn | `#ba5400` | numbers in code only |

Rules:
- Cards are white with a 1px `#e5e9f0` border and a 4px radius; the boarding pass has a 1px `#c8d6f1` frame and 8px; no shadows except the tooltip and the toast.
- Navy is the frame (tab bar, pass band and stub, table head, buttons); it is never a data colour.
- Orange `#ff9f00` is a hairline only: 3px left bars on the headline and section titles, 1px × 8px separators in the header, the 3px underline of the active code tab.
- Cabin colours band the seat map only.


## Data Colors

The annual report draws its charts in teal with deep blue and bronze as second and third series and a cool gray for comparisons, so the data colours come from there. Teal is the subject everywhere; everything else is gray; red only says that something fell short. Every value passed an OKLab validator (colour-vision-deficiency separation, normal-vision separation, contrast) on the card `#ffffff`; the stub's chart was checked on navy. Use them exactly; do not generate tints.

| Role | Mark | Label text | Use |
|---|---|---|---|
| Subject | `#0096ae` | `#00788c` | what the title names: the actual load factor, the cabin the title names, the busiest day, routes with more departures than last year |
| Second · third category | `#005584` · `#c3892a` | `#005584` · `#946e31` | a second or third series beside teal (not used in the sample) |
| Other | `#afafaf` | text-2 | everything else: other cabins, routes above breakeven, routes with the same schedule, on-time departures |
| Comparison (plan) | `#868ba0`, dashed 2px (6 on, 4 off) | ink | plan; the bars of ordinary days in the daily strip |
| Last year | `#c4c9d4`, solid 2px | text-2 | last year's line; days below the daily average |
| Below breakeven · late | `#dc0202` | `#dc0202` | routes below breakeven, late departures, values short of plan or target |
| Breakeven · average | `#222222` 1px | ink | the zero line of the route board, the daily average line |
| Empty seat | white, 1px `#a6b4cd` | — | seats not sold on an average flight |
| Land · other regions | `#e5e9f0` · `#dfe3ea` | — | the route map's base; routes outside the chosen tab |
| Stub (on navy) | actual `#1aa5bd`, plan `#c3cbdb` dashed | white | the year by month on the stub |
| Sequential | `#74bfcc` `#34a3b8` `#00869e` `#00677b` `#004a59` | ink on the two lightest, white on the rest | colour by value |
| Diverging | `#8a5a14` `#b57e27` `#d9ab62` · `#dddddd` · `#74bfcc` `#1f9bb2` `#006a7f` | each arm's darkest | below and above a midpoint |
| Status | good `#03760b`, bad `#dc0202`, neutral `#868ba0` | — | change text and chips only |

Validation (from `tokens.json`):
- Teal `#0096ae`, deep blue `#005584`, bronze `#c3892a` (all pairs): lightness inside 0.43–0.77, chroma ≥ 0.1, CVD ΔE 17.3 (bronze–teal, protan), normal vision 19.5 (deep blue–teal), contrast 3.52, 7.98 and 3.03:1. Text steps: teal `#00788c` 5.17:1, bronze `#946e31` 4.63:1.
- Other `#afafaf` (2.19:1) is neutral by design; it always has a second cue: value labels, a 2px gap, a table. Plan `#868ba0` 3.38:1 is always dashed and labelled at its end; last year `#c4c9d4` sits behind both, labelled in `#666666`.
- The cabin colours fail as data (lightness under 0.43, chroma under 0.1), so they only band the seat map.
- Status: good `#03760b` 5.83:1 and bad `#dc0202` 5.18:1; between them CVD 8.9 (protan), normal 33.9. Status is never colour alone: arrows, signs and the words `vs plan`, `below breakeven` carry it too.
- On the navy stub (`--mode dark --surface #00266b`): actual `#1aa5bd` sits inside the dark lightness band with chroma ≥ 0.1 and 4.81:1; plan `#c3cbdb` is a neutral reference; between them CVD 14.3, normal 20.2.
- Route map: teal and gray on land `#e5e9f0` are 2.89 and 1.80:1, so every route also carries width, a dot and, for subject routes, a label.
- The sequential ramp is one hue (spread 8°), monotone, every gap ≥ 0.06, the light end 2.09:1. The diverging arms pass the ordinal checks (light ends 2.11 and 2.09:1); poles CVD 14.4, normal 18.3; the midpoint is lightGrey.

Rules:
- Teal only for what the title names; the rest gray. A card that is mostly teal has highlighted nothing.
- Never navy `#00266b`, orange `#ff9f00` or a cabin colour on data.
- Red is a status, not a series: below breakeven, late, short of plan or target.


## Typography Rules

| Role | English | Korean | Weights |
|---|---|---|---|
| Sans (body, labels, tables) | Figtree | Pretendard | 400, 500, 600, 700 |
| Display (headings, airport codes, big values) | Source Sans 3 | Pretendard | 400, 600, 700 |
| Mono (airport and route codes, code) | Source Code Pro | Source Code Pro, Hangul falls back to Pretendard | 400, 500 |

Figtree stands in for Proxima Nova, the site's text face: in the same 20px string Proxima runs 437.5px with a 0.714 x/cap ratio, Figtree 447.7px with 0.714. Source Sans 3 stands in for the site's own heading face, a humanist sans with a binocular g (424.7px against 439.1px in the same 24px string). singaporeair.com/ko_KR loads no Hangul web font, so Korean uses Pretendard throughout.

| Element | Size / weight | Notes |
|---|---|---|
| Headline | display `clamp(23px, 2.05vw, 29px)` / 400, line-height 1.3, navy | the release sentence; the numbers 600; a 3px orange bar 15px to the left; Korean 400 on 1.42 with 700 numbers |
| Lede | 15px / 400, line-height 1.55, text-2 | figures 600 ink |
| Report name · eyebrow | display 30px / 400 navy · 11px / 600 caps 0.14em text-2 | Korean 27px / 500 · 13px |
| Tabs | 12px / 600 caps 0.125em white; the chosen tab 700 navy on white | Korean 14px, no caps |
| Pass band · field label | 11px / 600 caps 0.14em white · 11px / 600 caps 0.12em text-2 | Korean 12.5px · 12px, no caps |
| Airport code | display 32px / 600 navy | `ORD`, `Systemwide` (Korean 28px) |
| Pass value · stub value | display 34px / 600 · 52px / 600 white | units 15px / 20px at text-2 or 80% white (Korean 30px / 46px, 700) |
| Section title | display 24px / 400 navy with a 3px orange bar | Korean 22px / 600 |
| Figure label | 11px / 700 caps 0.14em gold | `FIGURE 2 · ROUTES FROM CHICAGO` (Korean 12.5px: `그림 2 · 시카고 출발 노선`) |
| Card title · subtitle | display 20px / 600 navy, `text-wrap: balance` · 14px on 20px text-2 | Korean 18.5px / 700 on 1.42 |
| Table | 13.5px tabular; head 11px / 600 caps white on navy, units in parentheses 10.5px | |
| Note · axis | 12px on 18px text-2 · 12px text-2, the unit 11px / 700 ink above the axis | notes start `Note 1:` / `주 1:` |

Korean breaks between words (`word-break: keep-all`), and a number stays on the line with the particle after it.


## Numbers, Dates & Units

| | English | Korean |
|---|---|---|
| Passengers | `210.6K`, table `(thousand)` with one decimal | `21.1만 명`, table `(천 명)` |
| Seat-km | `1,793.8M` RPK, `2,073.3M` ASK | `17.9억` |
| Load factor · change | `86.5%` · `+0.8 pts`, `▲ +1.0 pts vs 85.6% in Oct 2025` | `86.5%` · `+0.8%p`, `▲ +1.0%p 지난해 10월 85.6% 대비` |
| Yield · revenue | `11.1¢`, `Revenue $199.9M` | `11.1센트`, `여객 수입 2.00억 달러` (under 1억: `3,047만 달러`) |
| Growth | `+9.5% vs Oct 2025`, `On plan` | `+9.5% 지난해 10월 대비`, `계획대로` |
| Table changes | a separate sign column: `+ 2.3`, `− 3.2`; `n.m.` where there is no last year | the same |
| Departures | `7 a week`, `5→7/wk`, `new · 4/wk` | `주 7편`, `주 5→7편`, `신규 · 주 4편` |
| Dates | `31 October 2026`, `Sun 11 Oct`, `FY2026/27 · Month 7 of 12`, months `Apr … Oct` | `2026년 10월 31일`, `10월 11일(일)`, `2026/27 회계연도 · 12개월 중 7번째`, `4월 … 10월` |
| Times | 24-hour, `17:00–20:59`, hours `00 03 … 21` | `17:00~20:59` |
| Codes | IATA airport codes in mono (`MEX · GRU · LIM`), cabins `J · S · Y` | the same |

- Money is in the company's currency; the sample's airline is American, so US dollars. Routes, schedules and seat counts in the sample are made up and are not the airline's.
- True minus (`−`); one decimal for rates and change; `pts` / `%p` for load factor changes.
- Change colour follows whether the move is good for that metric; capacity change is neutral gray.
- Units are smaller than the digits. A rounded table still adds up: round each route, then give the leftover units to the largest remainders, so routes add to their region and regions to Systemwide; say so in the note.
- The financial year runs from 1 April to 31 March.


## Layout Principles

One column, at most 1400px wide, 32px side padding (24px up to 1359px, 16px below 640px), a 16px gap, 44px above each section title.

1. **Header** (white, 84px): the company eyebrow and the report name; on the right the period with a calendar icon, the EN/KO pill (40px radius), an outlined `Export PDF` and a navy `Copy as Markdown`.
2. **Tab bar** (navy, 56px): `Systemwide 14 · The Americas 3 · Europe 4 · East Asia 3 · South West Pacific 2 · West Asia and Africa 2`; the chosen tab white with a 16px top-left corner; `October 2026 | vs plan and October 2025` on the right behind an orange separator (from 1360px). It is the filter for every view; the URL keeps it (`?region=europe`).
3. **The widget panel** (white, joined to the chosen tab, bottom corners 16px): the headline with its orange bar, the lead, the boarding pass, `Note 1`.
4. **Seats: cabins and the network**: Figure 1 the seat map · Figure 2 the route map.
5. **Routes and the Chicago hub**: Figure 3 routes against breakeven · Figure 4 departures by hour.
6. **Operating statistics**: Table 1, full width.
7. **How it's built** and **Method and sources** (notes in two columns, numbered like the release).
8. **Footer**: the catalog line, the sample note, the notice and the way back.

Cards side by side end on one line: the card without a fixed shape takes the extra height (the route map's area, Figure 4's plot), and the route board's rows stretch from 25 to 44px. Density: at 1440 × 810 the tab bar, the headline, the lead and the whole boarding pass are on the first screen. At most seven views per section; never lead with a chart.


## Component Stylings

- **Card**: white, 1px `#e5e9f0`, 4px radius, 18px 22px 16px. Head: figure label (gold caps) → finding title (navy display) → subtitle → keys; body; `Note 1:` 12px text-2.
- **Section title**: display 24px / 400 navy with a 3px `#ff9f00` left border and 15px padding; the question it answers on the right in 14px text-2.
- **Boarding pass** (key figures): white, 1px `#c8d6f1`, 8px radius; a 270px navy stub on the right (240px up to 1359px; below it under 1024px).
  - Band (38px navy): `MONTHLY OPERATING STATISTICS` · `FY2026/27 · MONTH 7 OF 12`.
  - Route line, one grid: row 1 the labels `FROM` · `TO` · `FLIGHTS` · `SEATS FLOWN` on one line; row 2 `ORD`, the arrow (a 2px `#a6b4cd` line centred on the capital height), the route region, and the two values on one baseline; row 3 `Chicago O'Hare` and the destination codes in mono 11.5px, starting on one line.
  - Five fields on a subgrid (label → value → change vs plan or target → change vs last year or a fact): passengers carried, RPK, ASK (`On plan`, change vs last year neutral), on-time departures (vs the 85% target, `413 of 491 left on time`), passenger yield (vs plan, revenue).
  - Daily strip where the barcode sits: passengers by day against the daily average — a 1px ink average line, bars up on busier days (`#868ba0`) and down on quieter ones (`#c4c9d4`), the busiest day teal, a `+25%` / `Avg` / `−15%` scale, weekday letters with weekends bold, dates under Mondays; the header names the average and the peak (`Peak Sun 11 Oct · 8,346 (+23%)`).
  - Stub: `LOAD FACTOR · OCT 2026`, the load factor at 52px, chips vs plan and vs last year, `FY2026/27 BY MONTH` with `5 of 7 months above plan` and a small line (actual `#1aa5bd`, filled dots above plan, hollow below; plan dashed `#c3cbdb`), and at the bottom the breakeven load factor with its margin as a chip.
- **Seat map** (Figure 1): the 247-seat layout on its side — Business 1-2-1 rows 11–18 (no 13), Premium Economy 2-3-2 rows 21–23, Economy 3-3-3 rows 31–52 — cabin bands `J · 28` in the cabin colours, row numbers above, letters at the left (`A B C · D E G · H J K`), the forward zone as a `#e2eee8` band with its load factor. Seats sold on an average flight fill window and aisle first: the cabin the title names teal, the others gray, empty seats white with a `#a6b4cd` edge. Below, a strip of three cabins (cabin-colour top rule → name and code → load factor → `21 of 28 seats sold · 7 empty` → vs plan). No fuselage, windows or seat icons. Under 420px wide the map stacks J and S above Y.
- **Route map** (Figure 2): great-circle lines from the hub on a Natural Earth projection centred on the Americas (cut at 99°E), land `#e5e9f0` only. Width 0.6 + 0.24px per weekly departure; teal for routes with more departures than last year, labelled with the change (`DUB · 5→7/wk`, `AKL · new · 4/wk`), gray for the same schedule, `#dfe3ea` for other regions when a tab is chosen. The hub is a 4.5px navy dot with a white ring and an `ORD` label. Labels (11px, white halo) are placed so they never overlap; codes that do not fit are grouped by region on one line (`LHR · CDG · FRA`).
- **Route board** (Figure 3): one row per route, lowest margin first: city and mono code, a 12px bar from the breakeven line (1px ink) on a fixed −4 to +14 pts scale, red with its value on the left below breakeven, gray above, then `PLF` and `BLF` columns.
- **Hub bars** (Figure 4): one bar per scheduled hour, on time gray and late red on top with a 2px gap; the evening bank 17:00–20:59 as a `#edf4ff` band labelled `EVENING BANK · 77% ON TIME`; `flights` above the axis.
- **Operating statistics table** (Table 1): a navy head with white caps and units in parentheses; route-region group rows on `#e5e9f0` (navy bold, subtotals); routes with the mono code; a passengers bar; changes in a sign column; bad values red with their sign (group rows too); `n.m.`; the Systemwide row bold under a 2px navy rule; `#edf4ff` hover and a tooltip on every row.
- **Buttons** (measured): 40px (48 on the site), 4px radius, 12px / 600 caps 0.12em; navy `#00266b` with white (hover `#001a4f`); outlined white with a navy border (hover `#edf4ff`). The EN/KO pill and the build section's segment are 40px-radius pills with the chosen one navy.
- **Chips**: 4px radius, 12.5px / 500 with the change in 700: success `#03760b` on `#cdf0cf`, error `#dc0202` on `#fff1f0`, flat navy on `#e5e9f0`.
- **Tooltip**: white, 1px `#c8d6f1`, 4px radius, a navy shadow `0 4px 12px rgba(0,38,107,.14)`; a 13px / 700 navy head, rows of key, value 700 and label text-2. It takes the first side that fits inside its card: above, left, right, below.
- **Workbench**: a window with a 1px `#c8d6f1` frame and 8px radius — the package panel on `#fafafa`, the figure pane with the `Without a spec / With DASHBOARD.md` pill, and the code pane with tabs underlined in 3px orange.


## Charts

- **Choose by the question.**
  - How did the month go → the release sentence and the boarding pass, each field with plan and last year.
  - Which cabin sold → the seat map with the cabin strip (Figure 1).
  - Where the capacity went → the route map, added routes teal (Figure 2).
  - Which routes lost money → the route board against breakeven, lowest first (Figure 3).
  - When the hub runs late → bars by scheduled hour, on time and late, the bank shaded (Figure 4).
  - Is the year on plan → actual against plan by month (the stub; full size in the build section).
  - Which days were busy → bars around the daily average (the pass strip).
  - Every route in detail → the operating statistics table.
- **Titles.** The finding, recomputed when the tab changes (`Capacity grew 9.7% with a new Auckland route and more flights to Lima, Dublin and Johannesburg`; `Delhi and Johannesburg flew below breakeven, by 3.0 pts and 2.4 pts`). The subtitle names the measure; the note starts `Note 1:`.
- **Axes** (the annual report's): the unit above the axis (`%`, `flights`), no gridlines, a `#a6b4cd` base line and ticks, the latest period bold.
- **Marks.** Subject lines 2.5px, comparisons 2px with a hollow end marker; bars square-ended with 2px gaps between stacked parts.
- **Labels.** Line ends carry `Name value` instead of a legend; keys only where labels cannot work.
- **Never:** pie, donut, gauges, 3D, gradients on data, a dual axis, smoothed lines, navy or orange on data, photos, aircraft drawings or logos.
- Every chart and list has a tooltip, keyboard control and a screen-reader table.


## Depth & Elevation

Flat. Cards and the pass are set apart by 1px borders, never by shadows. The widget panel joins the chosen tab without a seam. Shadows exist only on the tooltip and the toast (`0 4px 12px rgba(0,38,107,.14)`).


## Interaction & Motion

- **Filter**: the tab bar scopes everything — the headline, the lead, the pass and stub, every title, key and note, the map's emphasis and the table. The URL keeps the region.
- **Hover**: a band behind a day, month or hour; the cabin outlined on the seat map; the nearest route on the map (others dim to 28%); `#edf4ff` behind a route row; tooltips everywhere.
- **Keyboard**: every chart, the board and the table are focusable; arrow keys step, Home and End jump, Esc clears, and a live region reads the value. Tabs move with arrow keys.
- **Workbench**: on first view the code types itself (55ms a line, 380ms between steps) and each step draws its layer of the load factor by month.
- Motion: lines and routes draw in 0.7s, bars grow in 0.45s, seats pop in 0.35s, rows fade in 0.3s; `cubic-bezier(.4,0,.2,1)`. `prefers-reduced-motion` turns it all off.


## Accessibility

- Text ≥ 4.5:1: ink 15.9:1, text-2 5.74:1, teal labels 5.17:1, gold 4.63:1, good 5.83:1, bad 5.18:1, chips 4.71:1; white on navy 14.1:1.
- Marks under 3:1 (Other `#afafaf`, last year, land, the faded routes) always have a second cue: a label, width, a dot, a gap or a table.
- Identity is never colour alone: names at line ends, `▲`/`▼` and signs on every change, `below breakeven` and `late` in words.
- Focus 2px navy with a 2px offset (orange inside the navy bars).
- Real tables with `scope`; every chart has a hidden data table and an `aria-label` that says how to move.


## Responsive Behavior

- ≥ 1360: as laid out above.
- 1024–1359: 24px padding; the stub 240px; pass values 30px, the stub 44px; the right part of the tab bar hides.
- 1024–1199: tabs 14px padding; the route board drops `BLF`.
- 900–1023: one column; the stub moves under the pass with its year by month across; the route map keeps a 2.17:1 box; the table drops ASK and breakeven.
- 640–899: the header wraps; `Export PDF` hides; the pass fields 3 + 2; the table drops RPK and yield.
- < 640: 16px padding; the pass fields 2 + 2 + 1; the route line moves the flights and seats under FROM and TO; the daily strip keeps dates only; the seat map stacks; the table keeps route, passengers, load factor and vs plan.
- Embedded in a post (`?embed=1`): the footer hides and the page reports its height to the host page.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` and these fonts (the second for Korean).

<!--email_off-->

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Source+Sans+3:wght@400;600;700&family=Source+Code+Pro:wght@400;500&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
```

<!--/email_off-->

The route map needs a base map: Natural Earth 1:110m land (public domain), projected once (d3-geo `geoNaturalEarth1().rotate([81, 0])` gives the same view) and drawn with great-circle lines. Give device parts a prefix (`bp-`, `sm-`, `mp-`, `rt-`, `os-`) so shared classes never leak into them.

**Tableau.** Paste the `<color-palette>` elements of `singapore-airlines.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop; assign the subject first so it takes teal.
- Dashboard background `#fafafa`; the region filter as a single-value list in a `#00266b` container with white text; section titles as text objects with a 3px `#ff9f00` left border (a thin orange container beside the text).
- Boarding pass: a horizontal container with a `#c8d6f1` border: text sheets for the five fields (label 9pt caps `#666666`, value 24–28pt, changes in `#03760b` / `#dc0202` with ▲ ▼) and a navy container for the stub (white text, the load factor 36pt). The daily strip: bars of passengers minus the daily average by day, a zero line in `#222222`.
- Seat map: a scaffold of 247 rows (cabin, row, letter, x, y) as square marks, coloured by sold / empty and cabin; or a bar of load factor by cabin if the seat map is not needed.
- Route map: `MAKEPOINT` for the hub and destinations and `MAKELINE` for routes (Tableau draws them as great circles), size by departures a week, colour by `more than last year`, a light map layer or `#e5e9f0` washout.
- Route board: bars of load factor minus breakeven, sorted ascending, a reference line at 0, colour by `< 0` (`#dc0202` / `#afafaf`).
- No gridlines; axis rulers `#a6b4cd`; tooltips white with a `#c8d6f1` border. Formats `#,##0.0,"K"` · `#,##0.0,,"M"` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Figtree is installed on every viewing machine and the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json` (teal, deep blue, bronze, then gray; white visuals with a 1px `#e5e9f0` border, 4px radius).
- The pass as cards in a shape with a `#c8d6f1` border; the stub as a navy shape with white text; changes as measures with conditional colours `#03760b` / `#dc0202`, always with a sign.
- Route map: Power BI's standard visuals cannot draw route lines; use the Azure Maps visual's path layer (preview) or a flow-map custom visual, or show the same content as a bar of departures a week against last year.
- Seat map: a matrix of rows × seat letters with conditional background colours.
- Gridlines off, axis lines `#a6b4cd`, data labels at line ends, legends off when labels name the series.

**Chart libraries.** Subject `#0096ae` (labels `#00788c`), Other `#afafaf`, plan `#868ba0` dashed `6 4`, last year `#c4c9d4`, bad `#dc0202`, base line `#a6b4cd`, ticks `#666666` 12px, no gridlines, the unit above the axis. The load factor by month in five forms is in the workbench of the live sample; `monthly.csv` is its data.


## Do's and Don'ts

- Do open with the release sentence and the boarding pass, every field with plan and last year. Don't lead with a chart or a row of anonymous KPI tiles.
- Do keep the devices readable: rounded units that add up, bars beside sizes, the daily strip around the average, labels on the routes that changed. Don't keep a device that reads worse than a plain bar or table.
- Do compare against plan, target and breakeven, rank the routes by margin, and show where capacity went. Don't report growth alone.
- Do frame the page with the navy tab bar, the white panel and orange hairlines. Don't fill cards with navy, add shadows or gradients, or put orange on data.
- Do keep teal for what the title names and everything else gray; red only for what fell short. Don't use the cabin colours as series.
- Do end side-by-side cards on one line by giving the extra height to a flexible part. Don't stretch a chart to an odd shape.
- Do write numbers the airline's way (`pts`, `n.m.`, a sign column, `FY2026/27`, IATA codes). Don't use the airline's real routes, seat counts, logo, typeface, the batik motif or aircraft pictures.


## Agent Prompt Guide

Install the style (`npx @vizney/styles@latest add singapore-airlines`, `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- singapore-airlines`, or unzip the package in the project root). Agents that read skills load `dashboard-style` on their own and work in one of three modes: **Build**, **Restyle** and **Review**. For an agent without skills, start the prompt with `Read DASHBOARD.md and follow it exactly.` For example:

```
Read DASHBOARD.md and follow it exactly. Build our monthly operating statistics as one self-contained HTML file with
fictional data, in English and Korean (?lang=en|ko, English by default), on the #fafafa page the spec describes.
Top: a white header with the report name, the period, the EN/KO pill, an outlined Export PDF and a navy Copy as Markdown;
the navy tab bar of route regions as the filter for every view, kept in the URL; the chosen tab joined to a white panel.
In the panel: the release sentence with a 3px orange bar, a lead, and the boarding pass (FROM → TO line, five fields with
plan and last year, passengers by day around the daily average where the barcode sits, a navy stub with the load factor,
the year by month and the breakeven margin).
Then: cabin load as a seat map and the route map (added routes teal); routes against breakeven (lowest first, below in
red) and departures by hour (late in red, the bank shaded); the operating statistics table (navy head, region bands,
sign column, n.m., Systemwide).
Every view on the same white card: figure label, finding title, subtitle, keys, view, "Note 1:". At most seven views per
section. Every chart and list needs a tooltip, keyboard control and a screen-reader table.
```

Before it is done, the agent checks:
- [ ] The headline is the release sentence; every pass field shows plan (or target) and last year with signed, good/bad-coloured changes; capacity change is neutral.
- [ ] Every view sits on a white card (1px `#e5e9f0`, 4px) with a finding title and a `Note 1:` note; navy only on frames, orange only as hairlines.
- [ ] Teal `#0096ae` only for what each title names, the rest gray; red `#dc0202` only for what fell short; no cabin colours, navy or orange on data.
- [ ] The devices read at a glance: the daily strip around its average, the seat map with its cabin strip, the route map with labels on the routes that changed, a table that adds up.
- [ ] Plan, target and breakeven appear where they matter, and the exceptions are ranked and named.
- [ ] No gridlines; units above the axis; line ends labelled; no dual axis, pie, donut, gauge or photo.
- [ ] Numbers, dates and units follow the formats in both languages.
- [ ] Cards side by side end on one line at 1440, 1280 and 1024px; nothing breaks at 390px.
- [ ] Text ≥ 4.5:1; light marks have a second cue; every view has a tooltip, keyboard control and a data table; the tab changes every card.
