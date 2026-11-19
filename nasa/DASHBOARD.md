---
name: NASA style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 9
tagline: Space, Countdown, Calm
tagline_ko: 우주, 카운트다운, 침착함
source: https://www.nasa.gov/, https://science.nasa.gov/
sample: https://styles.vizney.com/nasa/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#000000"
  card: "#17171b"
  plot: "#17171b"
  raise: "#2e2e32"
  hair: "#2e2e32"
  rule: "#444447"
  divider: "#333333"
  ink: "#ffffff"
  body: "#e3e3e3"
  muted: "#959599"
  text-2: "#b9b9bb"
  dim: "#717173"
  band: "#0b3d91"
  screen: "#061634"
  screen-land: "#22365e"
  light-page: "#f6f6f6"
  light-card: "#ffffff"
  light-ink: "#1b1b1b"
  light-text-2: "#58585b"
  light-muted: "#717173"
  light-rule: "#e3e3e3"
  accent: "#f64137"
  go: "#14a06a"
  nogo: "#f2473f"
  focus: "#ffffff"
data:
  categorical: ["#3d8af7", "#d5691f", "#14a06a"]
  other: "#58585b"
  comparison: "#959599"
  categorical_text: ["#7fb0ff", "#f2a46d", "#4cd493"]
  sequential: ["#1d52ad", "#2d6fd6", "#4a90f7", "#82b3ff", "#bcd6ff"]
  diverging: ["#98bdf5", "#5189e0", "#2b5aa6", "#444447", "#91491a", "#c96a2b", "#f2a46d"]
  good: "#14a06a"
  bad: "#f2473f"
typography:
  sans: { en: "Public Sans", ko: "Pretendard" }
  display: { en: "Inter", ko: "Pretendard" }
  mono: "DM Mono"
radius: {panel: "0", button: "0", chip: "0", tooltip: "0", bar: "0", circle: "50%"}
spacing: {page: "32px", gap: "16px", section: "56px", card: "16px 20px 12px", band: "12px 22px 11px", poll-row: "22px", cell: "0 8px", footer: "64px 0 0"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: nasa.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: poll.csv}
---

# NASA style — DASHBOARD.md

**Space, Countdown, Calm** · 우주, 카운트다운, 침착함

A dashboard design spec read from the way NASA shows a number on launch day: the L-minus countdown with its built-in holds, the launch director's GO/NO-GO poll, the front wall of mission control with its world map, station circles and row of clocks, and the white Earth Indicators charts of science.nasa.gov. It turns those parts into a calm launch readiness review on black and white sections, with the values, rules and checks an AI coding agent, Tableau or Power BI needs to rebuild it.

```
npx @vizney/styles@latest add nasa
# or, without Node:
curl -fsSL https://styles.vizney.com/install.sh | sh -s -- nasa
```

That puts `DASHBOARD.md` in the project root and the `dashboard-style` agent skill (build, restyle, review) in `.claude/skills/dashboard-style/`, together with `tokens.css`, `tokens.json`, `nasa.tps`, `powerbi-theme.json` and `prompt.md`. Coding agents that read skills pick it up whenever a task touches a dashboard or a chart; any other agent can be told to follow `DASHBOARD.md`.

- Live sample: https://styles.vizney.com/nasa/?lang=en (Korean `?lang=ko`; one flight `&flight=VS-13` or `&flight=VS-14`)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/nasa/DASHBOARD.md
- Package: [nasa-dashboard-style.zip](nasa-dashboard-style.zip) (unzip in your project root) · the skill: [skill/SKILL.md](skill/SKILL.md)
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [nasa.tps](nasa.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [poll.csv](poll.csv) (the data behind the sample's Figure 1)
- Catalog: VIZNEY STYLES · 09 · https://styles.vizney.com (Vizney Styles is a line of [Vizney](https://www.vizney.com))

Not an official NASA design, and not affiliated with, endorsed or sponsored by NASA. A reference style read from the publicly visible design of nasa.gov and science.nasa.gov and from public touchpoints such as launch countdowns and mission control displays; it carries no NASA insignia, logotype, seal, photo or data, and its fonts are open-licence fonts (SIL OFL). Trademarks belong to their owners. The sample's company, Vizney Space, its flights, launch sites, stations and all its numbers are fictional; launch sites and stations are named by number and region only.


## Visual Theme & Atmosphere

A launch control room an hour before the poll. The first screen is black `#000000` with square `#17171b` panels, white digits in DM Mono and a band of countdown blue `#0b3d91`; the screens inside the panels are deep navy `#061634`, never black, framed by a 1px `#0b3d91` rule. Below the fold the page alternates as nasa.gov does: a light `#f6f6f6` band with white panels for open items, then black again for orbit and traffic, then light for how it's built and the terms. Colour is scarce and always a state: green for GO, red for NO-GO, blue only for the band and the clock rows, white for the subject. Everything else is the carbon gray ladder.

Three devices carry the report, and each holds data:

- **Countdown band (the KPI row and the milestone strip).** The nasa.gov countdown block becomes the KPI row: on `#0b3d91`, the flight, the window and backup days, then the L− clock (`L− 06 : 04 : 42`, DAYS · HRS · MINS) and four key figures in cells split by 1px rules (poll GO count, open items against plan, weather % GO, processing margin in days), each label → value → change. Under it a 48px milestone strip runs from now to liftoff, with the last 48 hours at a larger scale, built-in holds as white blocks and a NOW marker.
- **GO/NO-GO poll (Figure 1).** The launch director's poll as a board: one row per position, NO-GO first with a 3px red rule on the left, the call sign in DM Mono, the position name, a dotted leader to the status word (GO in green, NO-GO on a red chip with black text), then the open-item bar and count, the constraints and the need-by L− day.
- **Mission control front wall (Figures 2, 4 and 5).** Navy screens with a clock row on the countdown blue on top: the ground track of the first three orbits over a map with tracking-station circles and a contact timeline (Figure 2); every tracked object below 1,400 km by inclination and mean altitude, with the flight's band in white (Figure 4); every close approach in the first 72 hours by MET and chance of collision on a log axis (Figure 5).

The light sections use the Earth Indicators chart grammar: the subject an ink line, the plan gray with hollow weekly rings, the title in capitals inside the plot, a `Data source:` line under it (Figure 3). No insignia, no photos of rockets or Earth, no starfields, no glow: the space feel comes from the clocks, the navy screens and the dots of the orbit map.

Measured in a browser on November 18, 2026 on nasa.gov (home, a mission page with its countdown block) and on the science.nasa.gov Earth Indicators pages: the Horizon Design System (HDS) carbon ladder `#000000` `#17171b` `#2e2e32` `#444447` `#58585b` `#717173` `#959599` `#b9b9bb` `#e3e3e3` `#f6f6f6`; nasa-blue `#1c67e3` and its shade `#0b3d91` (the countdown block, 16px 24px padding, digits DM Mono 300, units DM Mono 400 11px capitals); nasa-red `#f64137`; headings Inter 700 and 800, body Public Sans 400 16px, labels DM Mono 500 11.2px capitals with 3.5px tracking; rules on dark `rgba(255,255,255,.2)`; corners square, round buttons 50%.


## Color Palette & Roles

| Token | Hex | Role |
|---|---|---|
| canvas | `#000000` | Dark sections (header, first screen, 02 Orbit and traffic) and the footer |
| card | `#17171b` | Every panel on dark; square corners, no border, no shadow |
| raise | `#2e2e32` | Tooltips (with a 2px white top rule), the hovered row, the highlighted code line |
| hair | `#2e2e32` | Row rules and gridlines on dark |
| rule | `#444447` | Axis baselines, the dashed L−2 review marker, the diverging midpoint |
| divider | `#333333` | Section, header and footer rules (white at 20%); `#3c64a7` inside the band |
| ink | `#ffffff` | Titles, values, clock digits, the subject line, the selected tab and its 2px underline, the focus ring |
| body | `#e3e3e3` | Body text and table values (13.9:1 on the card) |
| text-2 | `#b9b9bb` | Subtitles, notes, keys and section kickers on dark (9.1:1) |
| muted | `#959599` | Axis ticks, labels and table heads on dark (6.0:1) |
| dim | `#717173` | Marks only, never text: the plan line, loss-of-signal dashes, open-item bars |
| band | `#0b3d91` | The countdown band and the clock row on every screen; white 10.0:1, labels white at 82% (7.3:1) |
| screen | `#061634` | The screens inside dark panels, framed by a 1px `#0b3d91` rule |
| screen-land | `#22365e` | Land on the map; graticule `#11264e`, equator and frame `#1a3366` |
| light-page | `#f6f6f6` | Light sections, a band the full width of the window |
| light-card | `#ffffff` | Panels in a light section; tooltips there are white with a 2px ink top rule |
| light-ink | `#1b1b1b` | Titles, values and the subject line on white (17.2:1) |
| light-text-2 | `#58585b` | Subtitles, notes and ticks on white (7.1:1) |
| light-muted | `#717173` | Labels and table heads on white (4.9:1) |
| light-rule | `#e3e3e3` | Row rules and gridlines on white; baselines `#b9b9bb` |
| accent | `#f64137` | nasa-red, UI only: the circle behind the arrow of a primary text button. Never data |
| go | `#14a06a` | GO and a good change as a mark; as text `#4cd493` on dark, `#0a7a4c` on white |
| nogo | `#f2473f` | NO-GO: the status chip (black text 5.8:1), the 3px row rule, a station that is down, a pass over the maneuver line; as text `#ff9088` on dark, `#b60109` on white |
| focus | `#ffffff` | Focus ring, 2px with a 2px offset (`#1b1b1b` in light sections) |


## Data Colors

Validated with the dataviz `validate_palette.js` (OKLab) on the dark card `#17171b` (`--mode dark`) and on the white card `#ffffff` (`--mode light`).

| Job | Values | Text step (≥ 4.5:1) |
|---|---|---|
| Subject and context | subject `#ffffff` (white `#1b1b1b`) · context `#959599` · plan `#717173` (white `#8a8a8e`) with hollow rings `#959599` (white `#58585b`) | ink · `#b9b9bb` |
| Categorical (for tools) | blue `#3d8af7` · orange `#d5691f` · green `#14a06a` · other `#58585b` | `#7fb0ff` · `#f2a46d` · `#4cd493` |
| Screens (Figures 2, 4, 5) | catalog dots and loss-of-signal `#7d8496` · in band `#ffffff` · maneuver `#f2473f` in a white ring · station reach edge `#52648c` | ticks `#959599` |
| Sequential | `#1d52ad` `#2d6fd6` `#4a90f7` `#82b3ff` `#bcd6ff` (dim to bright: on a dark card a larger value is brighter) | — |
| Diverging | ahead `#98bdf5` `#5189e0` `#2b5aa6` · `#444447` · `#91491a` `#c96a2b` `#f2a46d` behind | — |
| Status | GO `#14a06a` · NO-GO `#f2473f` · neutral `#444447` | `#4cd493` / `#ff9088` dark · `#0a7a4c` / `#b60109` white |

- Blue, orange and green pass every check with `--pairs all` on both surfaces: worst colour-vision ΔE 9.4 (green and orange, deutan), worst normal-vision ΔE 24.1, each ≥ 3:1 on `#17171b` and `#ffffff`.
- GO and NO-GO pass on both surfaces (CVD ΔE 8.2, normal vision 31.9). Status is always a word, and NO-GO rows add a 3px rule, so colour is never alone.
- NO-GO red and the orange category are about ΔE 8 apart in normal vision: red appears only for NO-GO and never in a figure that also uses orange.
- The sequential ramp is one hue (spread 2°), monotone, every step ΔL ≥ 0.06; each diverging arm passes `--ordinal` on its own.
- On the navy screen white marks are 17.9:1, gray dots `#7d8496` 4.8:1 (3.7:1 under the white ones, so white still leads), the red maneuver dot 4.9:1 inside a white ring.
- Blue is the band, not a series colour on the sample: the figures use ink and gray, and colour only for GO and NO-GO.


## Typography Rules

| Role | English | Korean |
|---|---|---|
| Result sentence, figure titles, business name, tabs, text buttons | Inter 600–800 | Pretendard 600–700 |
| Body, notes, keys, names in the poll and the table | Public Sans 400–700 | Pretendard 400–600 |
| Labels, clocks, every number, call signs, code | DM Mono 300/400/500 | DM Mono for digits and call signs; Korean labels in Pretendard |

One body face and one display face per language, never mixed on one screen; DM Mono is the number face in both. Numerals are tabular everywhere.

| Size | Value |
|---|---|
| Headline | 27px/700 Inter (Korean 25px), line-height 1.12, one sentence |
| L− clock and key figures | 38px/300 DM Mono; units 13px/400 capitals at 82% white (DAYS · HRS · MINS) |
| Label | 11.2px/500 DM Mono capitals, letter-spacing .3125em (`FIG 1 · GO/NO-GO POLL`); Korean 12px without capitals |
| Card title | 19px/700 Inter (Korean 17.5px), the finding as a sentence |
| Poll rows | 22px high: call sign 12.5px/500 DM Mono, position 13.5px Public Sans, dotted leader, status word DM Mono 500 |
| Table | 13.5px, rows 34px high, numbers DM Mono |
| Body | 15px/400 (Korean 14.5px) |
| Notes | 12.5px/400, a data source line under every figure |

Load the fonts as in Tool Mapping. Never the NASA logotype or worm, never a "space" display face.


## Numbers, Dates & Units

| What | English | Korean |
|---|---|---|
| Countdown | `L− 06 : 04 : 42` (DAYS · HRS · MINS); in text `L−6`, `L−38H30M` | same; units `일 · 시간 · 분` |
| Milestones | `L−2 MMT` · `FRR` · `Hold 2H` | `L−2 MMT` · `FRR` · `2시간 정지` |
| Window | `Window NOV 24, 2026 · 18:42 UTC` · `5 min · Backup Nov 25 · Nov 26` | `발사 창 11월 24일 18:42 UTC` |
| Times | UTC, 24-hour: `14:00 UTC`; MET `27:48` (hours:minutes from liftoff) | same |
| Dates | `Nov 22`; in the band capitals `NOV 24` | `11월 22일` |
| Poll | `14/16 GO` | `16자리 중 14 GO` |
| Weather | `70% GO`; change `▲ 10 pts` | `70% GO`; `▲ 10%p` |
| Margin | `+1.5 days`; table `−2 d` | `+1.5일`; `−2일` |
| Open items | whole numbers: `23`, `8 under plan (31)` | `23건`, `계획(31)보다 8건 적음` |
| Chance of collision | `1 in 42,000` (two significant figures) | `4만 2천분의 1` · `1만분의 1` · `1억분의 1` |
| Distances | `400 km` · `±25 km` · `97.6°` | same |

- ▲ ▼ before every change, a true minus (−), the unit never wrapping away from the number (no-break space). Call signs and IDs never break at their hyphen (`VS-12`, `NO-GO`, `CR-1207` carry a word joiner).
- Percentages are whole numbers; margins and pace keep one decimal.


## Layout Principles

- Page 1400px wide at most, 32px side padding (24px under 1360px, 16px under 640px), 16px between panels, 56px between sections.
- Header: 60px, one line on black: business and report name, the flight tabs (call sign in DM Mono and the kind; the selected one white with a 2px underline; the one filter for every card, kept in the URL as `?flight=`), EN/KO.
- First screen (1440 × 810), dark: the result in one sentence, the countdown band, the milestone strip, then row 1 — Figure 1, the poll (584px) | Figure 2, the front wall (1fr). Bottoms on one line.
- 01 Open items, light: Figure 3, open items against plan | Table 1, items to close.
- 02 Orbit and traffic, dark (1.22fr | 1fr): Figure 4, the orbit map | Figure 5, close approaches.
- 03 How it's built and 04 Terms and counts, light; the workbench window in 03 stays dark like a screen. Footer dark.
- Light sections run the full width of the window; their panels keep the page grid.
- Every figure and table is one panel with one anatomy: the DM Mono label (`FIG 3 · OPEN ITEMS AGAINST PLAN`) → the finding as the title → a subtitle with the method → keys → the view → a note with the data source.


## Component Stylings

**Header and tabs.** Black, a 1px white-20% rule under it. Tabs are text: `VS-12` in DM Mono 500 and the kind in Public Sans, 60px tall; the selected tab is white with a 2px white underline, the rest `#959599`.

**Countdown band.** `#0b3d91`, 12px 22px 11px padding, square. Top line: the flight and kind, the window, the backup days and the as-of time in DM Mono capitals at 82% white. Then five cells split by 1px `#3c64a7` rules: the L− clock (DAYS : HRS : MINS) and four key figures, each label (DM Mono 11.2px capitals) → value (38px/300) → change (12.5px). A good change is `#4cd493`, a bad one `#ff9088` (4.6:1 on the blue), with ▲ ▼.

**Milestone strip.** 48px on black under the band. Days from now to liftoff at one scale, the last 48 hours at a larger one, split by a thin rule. Milestones are 1px ticks with L− labels in DM Mono; built-in holds are white blocks; done milestones gray; NOW a white marker. Under 640px a list of the next milestones.

**GO/NO-GO poll (Figure 1).** Rows 22px on `#17171b` with `#2e2e32` rules; NO-GO first, then GO. A NO-GO row carries a 3px `#f2473f` rule on its left edge. Columns: call sign (DM Mono 12.5px/500), position, a dotted `#444447` leader to the status word (GO `#4cd493` DM Mono 500; NO-GO black on a `#f2473f` chip, square), open items as a `#717173` bar with its number, constraints in `#ff9088`, need by as `L−3 · Nov 21`. Weather shows `PENDING` until L−7.

**Front wall (Figure 2).** A navy `#061634` screen in a 1px `#0b3d91` frame. A clock row on `#0b3d91` across its top: liftoff UTC, % in contact, longest loss of signal, events out of contact, in four cells with white values and 82% labels. The map runs from 80°N to 70°S (land `#22365e`, graticule `#11264e`, equator `#1a3366`); station circles at 5° elevation as `#52648c` outlines with a 6% white fill and the station number; a station that is down in `#f2473f` dashes. The ground track of the first three orbits: white 2px in contact, `#7d8496` dashes out of contact; events as diamonds with their name. Under the map a contact timeline by MET with `ORBIT 1 2 3` labels.

**Open items (Figure 3), light.** On a white panel: the subject (open items, all positions) a 2px `#1b1b1b` line; the plan a 1.5px `#8a8a8e` line with hollow `#58585b` rings each week; last week's pace a dotted ink line to the L−2 review, marked by a dashed `#b9b9bb` rule labelled `L−2 MMT`. The chart's own title sits inside the plot in DM Mono capitals; values at the line ends (`23 OPEN`, `5 AT L−2`).

**Items to close (Table 1), light.** Head 11.2px DM Mono capitals over a 1px `#b9b9bb` rule; rows 34px with `#e3e3e3` rules. ID (DM Mono), item and type, position, need by, and margin as a bar diverging from zero (late to the left in `#b60109` text and the NO-GO red mark, early to the right in gray) with its value in days. Least margin first; six rows, then `Show N more`.

**Orbit map (Figure 4).** A navy screen with a clock row (objects, in band, the flight's orbit, against the other altitude). Every tracked object below 1,400 km is a 1.6px `#7d8496` dot by inclination (x, 0–110°) and mean altitude (y, km); the objects within ±25 km of the flight's first-week orbit are white; each flight orbit is a target (a white ring with a cross) labelled with its call sign. A few orbit families are named in `#959599` where no dot sits. Gridlines `#11264e`.

**Close approaches (Figure 5).** A navy screen with a clock row of four cells: passes, watch, maneuver, closest. MET 0–72h on x, chance of collision on a log y axis written `1 in 10,000` (`1만분의 1`). A red dashed line at 1 in 10,000 (plan a maneuver) and a gray dotted line at 1 in 10 million (watch), labelled at the right end. Passes are `#7d8496` dots; watched passes white; a pass over the red line is a `#f2473f` dot in a white ring with a two-line label (chance, object and MET).

**Tooltip.** On dark `#2e2e32` with a 2px white top rule; on white `#ffffff` with a 2px ink top rule and a 1px `#e3e3e3` line. Square, 10px 12px padding, a DM Mono head, rows of label and value. It adds detail and is never the only copy of a number.

**Buttons.** Text buttons in Inter 600 with a 28px round `#f64137` circle behind a white arrow (`Show more`, `Download .zip`); secondary buttons square with a 1px rule. Code windows on `#000000` in DM Mono 12.5px (keyword `#7fb0ff`, string `#4cd493`, number `#f2a46d`, function `#ff9088`, property `#e3e3e3`, highlight `#2e2e32`).


## Charts

- **Choose by the question.**
  - Is the flight ready, and how long until it goes → the result sentence and the countdown band.
  - Which positions hold it up, and by when must they clear → the poll (Figure 1).
  - Will the flight stay in contact through its first events → the front wall (Figure 2).
  - Is the work closing fast enough → open items against plan (Figure 3).
  - Which items to chase first → items to close, least margin first (Table 1).
  - How crowded is the orbit, and must the flight maneuver → the orbit map (Figure 4) and close approaches (Figure 5).
- **Titles.** The finding, recomputed for each flight: `Two of 16 positions are NO-GO, each on one constraint`; `With station 06 out, Burn 1 at MET 00:42 falls in a 33-minute loss of signal`; `Open items are 9 over plan; at last week's pace 36 would remain at the L−2 review`; `382 tracked objects fly within 25 km of VS-14's 600 km orbit, 2.1 times as many as at 400 km`; `One pass crosses the maneuver threshold: 1 in 5,600 with a rocket body at MET 31:24`.
- **Marks.** The subject in ink, everything else gray; colour only for GO, NO-GO and a pass over the maneuver line. Lines 2px, dots ≥ 1.6px on the orbit map and ≥ 6px elsewhere, square bars starting at zero.
- **Axes.** Row gridlines `#2e2e32` on dark, `#e3e3e3` on white; ticks DM Mono 11px. Log axes are written in words (`1 in 10,000`), never `1e-4`.
- **Labels.** Values at line ends and on the few marks the title names; the scatters carry no number on their dots; the tooltip and table give them.
- **One axis.** Never a dual axis. The countdown, open items and traffic are separate views.
- **Never:** pie, donut, 3D, gauges, gradients, glow, starfields, photos of rockets, Earth or space, the insignia, patches, real missions, vehicles, pads, centers or people.
- Every figure and the table have a tooltip, keyboard control and a screen-reader table.


## Depth & Elevation

Flat and square. Panels are `#17171b` on black with no border and no shadow; light panels white on `#f6f6f6` with no border. Screens are inset navy with a 1px blue frame. The tooltip has no shadow either; its top rule sets it apart.


## Interaction & Motion

- The flight tabs filter every card; the URL keeps `?lang=` and `?flight=`. Language switches in place and only the language's own fonts are used.
- Every view responds to hover and to the keyboard: Tab to focus, arrow keys to move (key figures, milestones, positions, events and stations, days, rows, dots), Home and End, Esc to close; a polite live region reads the focused item.
- Motion (`cubic-bezier(.4,0,.2,1)`): the clock digits and key figures turn over 0.34s, 90ms apart; open-item bars grow from the left 25ms apart; the open-items line and the ground track draw in over 1.4s, orbits 0.25s apart; the dots of Figures 4 and 5 fade in over 0.9s, the white band 0.45s later. The clock does not tick live; it shows the as-of time. With `prefers-reduced-motion` everything appears complete.


## Accessibility

- Text ≥ 4.5:1: on the card white 17.9, body 13.9, subtitles 9.1, ticks 6.0, green 9.5, red 8.2; on the band white 10.0, labels 7.3, red 4.6, green 5.3; on white ink 17.2, subtitles 7.1, labels 4.9, red 7.0, green 5.4; black on the NO-GO chip 5.8.
- Dim marks (`#717173` 3.7:1, `#7d8496` on navy 4.8:1) always carry a value, a key or a table view.
- Status never relies on colour alone: GO and NO-GO are words, NO-GO rows add a 3px rule, changes carry ▲ ▼ and signs.
- Every view has a screen-reader table; the focus ring is 2px white (ink in light sections) with a 2px offset; targets at least 32px high.


## Responsive Behavior

- ≥ 1360px: as described.
- 1200–1359px: 24px padding; the band's top line runs across and the clock and four key figures sit under it at 36px; row 1 is 548px | 1fr.
- 1024–1199px: values 32px; row 1 halves; the front wall's clock row becomes 2 × 2 and the poll drops the need-by column.
- Under 1024px: every row stacks (Figures 1 and 2, then 3 and Table 1, then 4 and 5); the poll gets its need-by column back.
- Under 900px: the band becomes two columns with the clock across the top; the flight tabs take their own line.
- Under 640px: 16px padding, values 30px; the tabs show only call signs; the close-approach clock row becomes 2 × 2; the poll keeps call sign, position, status and open items.
- Captured and checked at 1440, 1280, 1200, 1024 and 390px in both languages, with no horizontal scroll and no text over text.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` (installed in `.claude/skills/dashboard-style/`; or copy the `colors` block from the front matter) and the fonts:

<!--email_off-->
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800&family=Public+Sans:wght@400;500;600;700&family=DM+Mono:wght@300;400;500&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
```
<!--/email_off-->

Each figure is one SVG drawn over its panel so the drawing never pushes the panel taller. Light sections are a wrapper with the light tokens (`.lt`) and a full-bleed background; a dark window inside one re-declares the dark tokens.

**Tableau.** Paste the `<color-palette>` elements of `nasa.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette runs blue, orange, green, then gray; status is GO and NO-GO.
- Dashboard background `#000000`, each sheet on `#17171b` with no border, row dividers `#2e2e32`, text `#e3e3e3`, headers `#959599`; light sheets on `#ffffff` with `#e3e3e3` dividers. Title each sheet with the finding.
- Countdown band: a `#0b3d91` container with text objects or BANs in DM Mono.
- Poll: a text table from `poll.csv` sorted by status (NO-GO first), a shape or square mark coloured by status, a bar for `open_items`.
- Open items: a line for actual in ink and plan in gray with circle marks each week; a reference line at the L−2 date.
- Orbit map and close approaches: scatter plots on a `#061634` worksheet shading; a log axis for chance of collision with reference lines at 1e-4 and 1e-7, formatted as `"1 in "#,##0`.
- Fonts: Tableau Book unless Inter, Public Sans and DM Mono are installed on every viewing machine and the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json`. It sets the data colours, `#17171b` visuals with square corners and no border, axis and gridline colours and text classes. Install Public Sans on authoring and viewing machines or accept Segoe UI.
- Countdown band: cards or a multi-row card on a `#0b3d91` shape.
- Poll: a table with conditional formatting (background `#f2473f` on NO-GO, black text) and data bars for open items.
- Open items: a line chart with the plan as a second, gray series and markers; a constant line at L−2.
- Orbit map and close approaches: scatter charts with a `#061634` plot area; a log Y axis for chance of collision and constant lines at the thresholds.
- Title each visual with the finding; the method in the subtitle.

**Chart libraries (D3, Observable Plot, Vega-Lite, matplotlib).** Background `#17171b` (screens `#061634`, light `#ffffff`); subject `#ffffff` (light `#1b1b1b`), context `#959599`, plan `#717173`; categorical `#3d8af7 #d5691f #14a06a`, other `#58585b`; GO `#14a06a`, NO-GO `#f2473f`; gridlines `#2e2e32` (light `#e3e3e3`); ticks `#959599` (light `#58585b`); sequential `#1d52ad #2d6fd6 #4a90f7 #82b3ff #bcd6ff`.


## Do's and Don'ts

| Do | Don't |
|---|---|
| Count down in L− with DAYS · HRS · MINS on the countdown blue | Put a ticking seconds clock or a progress ring on the page |
| Make status a word (GO, NO-GO) and sort NO-GO first | Use red and green without words, or traffic-light gauges |
| Keep the subject in ink and the rest gray; colour only for a state | Paint series in nasa-blue or nasa-red |
| Draw screens in navy `#061634` with a blue frame and a clock row | Draw space as black with stars, glow or nebula gradients |
| Alternate black and light sections as nasa.gov does | Run the whole report on black |
| Name launch sites and stations by number and region | Use real missions, vehicles, pads, centers or people |
| Use the NASA name only to say where the look was read from, with the notice | Use the insignia, logotype, seal, patches or photos |


## Agent Prompt Guide

Install the style (`npx @vizney/styles@latest add nasa`, `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- nasa`, or unzip the package in the project root). Agents that read skills load `dashboard-style` on their own and work in one of three modes: **Build**, **Restyle** and **Review**. Other agents can be given this prompt:

```
Read DASHBOARD.md and follow it exactly. Build our launch readiness review as one self-contained HTML file with
fictional data, in English and Korean (?lang=en|ko, English by default).
Header: 60px on black with the business and report name, flight tabs (call sign in DM Mono, the selected one white
with a 2px underline; the filter for every card, kept in the URL) and EN/KO. Then the result in one sentence and the
countdown band on #0b3d91: the window and backup days, the L− clock (DAYS : HRS : MINS, DM Mono 300) and four key
figures (poll GO, open items against plan, weather % GO, processing margin), then the milestone strip with holds.
First screen: Figure 1, the GO/NO-GO poll (one row per position, NO-GO first with a 3px #f2473f rule, dotted leaders
to the status word, open-item bars, need-by L− day); beside it Figure 2, the front wall: a navy #061634 screen with a
clock row, the ground track of the first three orbits, station circles and a contact timeline.
Below, a light #f6f6f6 section: Figure 3, open items against plan in the Earth Indicators grammar, and Table 1, items
to close by margin. Then a black section: Figure 4, every tracked object by inclination and altitude with the flight's
band in white, and Figure 5, close approaches by MET and chance of collision on a log axis with the maneuver line.
Every view in the same panel: DM Mono label, finding title, subtitle, keys, view, data source note. Use only the
values in Data Colors, the formats in Numbers, Dates & Units and the components in Component Stylings. Every view
needs a tooltip, keyboard control and a screen-reader table.
```

Before it is done, the agent checks:
- [ ] The headline and every title state the finding and change with the flight tabs.
- [ ] The countdown band is `#0b3d91` with the L− clock and four key figures, each label → value → change with ▲ ▼.
- [ ] The poll lists NO-GO first; status is a word; NO-GO rows carry a 3px red rule.
- [ ] Screens are navy `#061634` in a 1px `#0b3d91` frame with a clock row; land `#22365e`; out-of-contact track dashed.
- [ ] The subject is ink and everything else gray; red appears only for NO-GO, a station down and a pass over the maneuver line.
- [ ] Light sections run the full width; their charts follow the Earth Indicators grammar.
- [ ] Panels side by side end on one line at 1440 and 1280px; nothing breaks or overlaps at 390px.
- [ ] Text ≥ 4.5:1; every view has a tooltip, keyboard control and a data table.
- [ ] No insignia, logotype, seal, patch, photo, real mission, vehicle, pad, center or person, and the NASA notice is on the screen.
