---
name: Race Timing style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 7
tagline: Racing, Telemetry, Precise
tagline_ko: 레이싱, 텔레메트리, 정밀함
source: https://www.formula1.com/en/results/2026/races
sample: https://styles.vizney.com/race-timing/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#000000"
  card: "#15151e"
  plot: "#15151e"
  raise: "#1c1c25"
  sunk: "#0d0d14"
  hair: "#303037"
  rule: "#47464c"
  ink: "#ffffff"
  body: "#d9d9df"
  muted: "#aaaaaa"
  text-2: "#aaaaaa"
  best: "#8c51d9"
  good: "#04a97a"
  missed: "#b88c19"
  focus: "#ffffff"
data:
  categorical: ["#cc3336", "#b88c19", "#d9dce2"]
  other: "#5f6270"
  comparison: "#aaaaaa"
  categorical_text: ["#ff8f87", "#f2c94c", "#d9dce2"]
  reference: ["#8c51d9"]
  sequential: ["#5d3c94", "#7c54be", "#9973df", "#b598f2", "#d1befe"]
  diverging: ["#bb9ef9", "#946ade", "#6f4bac", "#4a4d57", "#7b5f06", "#a58108", "#d6ab32"]
  good: "#04a97a"
  bad: "#b88c19"
typography:
  sans: { en: "Barlow", ko: "Pretendard" }
  display: { en: "Barlow Condensed", ko: "Pretendard" }
  mono: "Roboto Mono"
radius: {panel: "8px", display: "24px", tab: "17px", button: "18px", chip: "4px", tooltip: "6px", tyre: "3px", bar: "2px"}
spacing: {page: "32px", gap: "16px", section: "56px", card: "18px 20px 14px", row: "34px", cell: "0 10px", footer: "22px 32px 36px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: race-timing.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: stints.csv}
---

# Race Timing style — DASHBOARD.md

**Racing, Telemetry, Precise** · 레이싱, 텔레메트리, 정밀함

A dashboard design spec read from the way motor racing shows its numbers on television and on its results pages: the timing tower down the side of the picture, the purple, green and yellow of the sector times, the onboard display with its shift lights and gear readout, the circuit map coloured mini-sector by mini-sector, the speed trace with the running gap underneath, and the tyre graphic that splits a race into stints. It turns those parts into a working race debrief on a black page, with the values, rules and checks an AI coding agent, Tableau or Power BI needs to rebuild it.

```
npx @vizney/styles@latest add race-timing
# or, without Node:
curl -fsSL https://styles.vizney.com/install.sh | sh -s -- race-timing
```

That puts `DASHBOARD.md` in the project root and the `dashboard-style` agent skill (build, restyle, review) in `.claude/skills/dashboard-style/`, together with `tokens.css`, `tokens.json`, `race-timing.tps`, `powerbi-theme.json` and `prompt.md`. Coding agents that read skills pick it up whenever a task touches a dashboard or a chart; any other agent can be told to follow `DASHBOARD.md`.

- Live sample: https://styles.vizney.com/race-timing/?lang=en (Korean `?lang=ko`; one round `&round=16`)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/race-timing/DASHBOARD.md
- Package: [race-timing-dashboard-style.zip](race-timing-dashboard-style.zip) (unzip in your project root) · the skill: [skill/SKILL.md](skill/SKILL.md)
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [race-timing.tps](race-timing.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [stints.csv](stints.csv) (the data behind the sample's Figure 2)
- Catalog: VIZNEY STYLES · 07 · https://styles.vizney.com (Vizney Styles is a line of [Vizney](https://www.vizney.com))

Not an official Formula 1 design, and not affiliated with or endorsed by Formula 1. A reference style read from the publicly visible design of formula1.com and public touchpoints such as race broadcasts and timing documents; it carries no logo, typeface, photo or data of theirs. This website is unofficial and is not associated in any way with the Formula 1 companies. F1, FORMULA ONE, FORMULA 1, FIA FORMULA ONE WORLD CHAMPIONSHIP, GRAND PRIX and related marks are trade marks of Formula One Licensing B.V. The sample's team, Vizney Racing, its series, circuits and drivers, and all its numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A pit wall after the flag. The page is black and the panels are the near-black `#15151e` of the results pages, with 8px corners, no borders and no shadows; everything else is condensed capitals, tabular numerals and three status colours that mean the same thing everywhere: **purple** is the fastest (of the race, or the quicker of two), **green** is a target met or a lap won, **yellow** is a target missed or time lost. Our cars are white. Every other car is gray.

Three devices carry the report, and each holds data:

- **The onboard display** is the row of key figures. Fifteen shift lights across the top are the last fifteen laps against the winner (green quicker, yellow slower, dark for in- and out-laps); a dial on each side holds the pit stop average against its target and the team's points against plan, each with a white tick; the gear readout in the middle is the finishing position with the places gained from the grid; two readouts below hold the gap to the win and the best lap, the latter in a purple chip when it is the race's fastest.
- **The circuit map** is Figure 1 and shares the first screen with the display. The track is a dark band; car 27's best lap is compared with the winner's in 24 mini-sectors, each coloured on the purple–gray–yellow diverging ramp, with a white start/finish bar, white sector lines and the turn numbers outside the apexes.
- **The timing tower with tyre stints** is Figure 2: position boxes, places gained, three-letter car codes, the gap at the flag and a stint strip per car with S, M and H in the compound colours. Our rows are raised and carry a white edge.

Two charts from the broadcast support them: the gap to the winner lap by lap (Figure 3) and the speed trace of both best laps with the running gap below and a small circuit that follows the cursor (Figure 4). Pit stops against target, season points against plan and a stint report finish the debrief. The rest of the page stays quiet so the devices stand out: no carbon fibre, no chequered flags, no glow on the lights, no photos.

Measured in a browser on November 11, 2026 on formula1.com's results pages (`/en/results/2026/races` and each round's race result, qualifying, starting grid, pit stop summary and fastest laps): surfaces `#000000`, `#15151e` and `#1c1c25`; rules `#303037` and `#47464c`; text `#ffffff` and `#aaaaaa`; table heads 14px/600 uppercase `#aaaaaa`; cells 16px/600 with 58px rows and a 1px `#303037` rule; radii 8px, 50% and 1000px on the site's chrome. The notation read there is used as is: race time `1:35:23.504`, gaps `+14.602s`, lapped `+2 laps`, lap times `1:12.689`, `DNF`, `DNS`, `NC`. The official typefaces are not used (Barlow and Barlow Condensed stand in; Titillium Web is not used either), and no team, driver, circuit, livery or logo appears: the sample's series, circuits, teams and drivers are invented.


## Color Palette & Roles

Surfaces, rules and text are the results pages'; the status colours belong to the timing screens.

| Token | Hex | Role |
|---|---|---|
| canvas | `#000000` | Page, header and footer |
| card | `#15151e` | Every panel (figures, tables, the workbench): 8px corners, no border, no shadow |
| plot | `#15151e` | Chart background: the panel itself, never a second box |
| raise | `#1c1c25` | Our rows in the timing tower, pit-cycle shading in Figure 3, the tooltip |
| sunk | `#0d0d14` | The onboard display's face, the circuit's track band, the code window, bar tracks in tables |
| hair | `#303037` | Gridlines and row rules; the display's 1px rim |
| rule | `#47464c` | Sector lines in Figure 4, the zero line, axis ticks, the dials' scale ticks |
| ink | `#ffffff` | Titles, values, our car 27, the selected round tab, our position boxes, target and plan ticks |
| body | `#d9d9df` | Body text and table values (12.9:1 on the card) |
| muted | `#aaaaaa` | Axis ticks, notes, subtitles, turn numbers (7.8:1 on the card) |
| text-2 | `#aaaaaa` | Labels, table heads and keys in condensed capitals |
| best | `#8c51d9` | Purple: the fastest of the race, the quicker of two; white text on it 4.9:1 |
| good | `#04a97a` | Green: target or plan met, a lap won, places gained |
| missed | `#b88c19` | Yellow: target or plan missed, time lost, places lost |
| focus | `#ffffff` | Focus ring, 2px with a 2px offset |

Marks: car 12 `#b9bcc6`, the winner or rival `#8b8f99`, every other car `#5f6270`, hover row `#262631`, unlit lights and dial tracks `#26262f`. Text that sits on a colour uses the text steps below, never the mark colour.


## Data Colors

Validated with the dataviz `validate_palette.js` (OKLab, `--mode dark`) on the card `#15151e`, where every chart sits.

| Job | Values | Text step (≥ 4.5:1) |
|---|---|---|
| Status | best `#8c51d9` · good `#04a97a` · missed `#b88c19` · neutral band `#47464c` | `#c4b5fd` · `#6ee7a8` · `#f2c94c` |
| Tyres (categorical) | soft S `#cc3336` · medium M `#b88c19` · hard H `#d9dce2` | `#ff8f87` · `#f2c94c` · `#d9dce2` |
| Subject and others | car 27 `#ffffff` · car 12 `#b9bcc6` · winner `#8b8f99` · others `#5f6270` | — |
| Sequential | `#5d3c94` `#7c54be` `#9973df` `#b598f2` `#d1befe` | — |
| Diverging (quicker → slower) | `#bb9ef9` `#946ade` `#6f4bac` · `#4a4d57` · `#7b5f06` `#a58108` `#d6ab32` | — |

- Purple, green, yellow and red pass every check with `--pairs all`: lightness band 0.48–0.67, chroma ≥ 0.1, worst colour-vision ΔE 9.7 (yellow ↔ green, protan; tritan 14.5), worst normal-vision ΔE 17.2, contrast ≥ 3:1 on the card. Soft and medium separate by ΔE 10.5 (deutan) and 19.8 (normal).
- Hard `#d9dce2` is the white of the hard compound on purpose, so it sits above the lightness band and below the chroma floor; it separates from soft and medium by lightness (13.2:1 on the card), and every tyre mark carries its letter.
- White is the subject. A white mark keeps a 2px card-coloured gap around it (a 6px halo under a 2.5px line). Never colour our car with a status colour; status colours describe a result, not a car.
- The diverging ramp is for comparisons by place on the lap (Figure 1, the running gap in Figure 4): purple is where car 27 was quicker than the winner, yellow slower, gray within 0.005 s. Steps per mini-sector: under 0.005 s gray, 0.005–0.02 s the dim step, 0.02–0.05 s the middle step, 0.05 s and more the bright step. Lap-by-lap verdicts (the lights, tooltips) use green and yellow.
- Status always carries a word or a sign as well (▲ ▼, "over target", "quicker"), so no reading depends on telling purple, green and yellow apart.
- The sequential ramp is for counts on one scale (heat in a lap × car grid if one is ever needed); it is not used in the sample.


## Typography Rules

| Role | English | Korean |
|---|---|---|
| Text: headline, titles, sentences, notes | Barlow 400/500/600 | Pretendard 400/500/600 |
| Labels, tabs, keys, figure numbers | Barlow Condensed 600, capitals, letter-spacing .06–.1em | Pretendard 600, no capitals, no letter-spacing |
| Timing numerals: lap times, gaps, positions, car codes, the display's digits, axis ticks | Barlow Condensed 500–700, tabular | Barlow Condensed (the numerals stay the same in Korean) |
| Code and file names | Roboto Mono 400/500 | Roboto Mono |

| Size | Value |
|---|---|
| Headline | 31px/600, line-height 1.22 (Korean 27px) |
| Card title | 18px/600 (Korean 17px) |
| Body | 15px/400 (Korean 14.5px) |
| Labels | 12.5–15px/600 capitals; figure labels 12.5px with .1em tracking |
| Timing tower | 17px/500 tabular; our rows 600 |
| Gear readout | 98px/700, the `P` at half size in `#aaaaaa` |
| Dial value | 31px/700 in the arc; unit 13px/600 muted |
| Readouts | 30px/700, the unit at 56% |
| Notes | 12.5px/400 |

Load the fonts as in Tool Mapping. Never the official Formula 1 typefaces or Titillium Web, which would suggest an official relationship.


## Numbers, Dates & Units

| What | English | Korean |
|---|---|---|
| Race time | `1:35:23.504` | `1:35:23.504` |
| Lap time | `1:20.142` | `1:20.142` |
| Gap to the winner | `+0.457 s` (`+14.602s` in dense tables) | `+0.457초` |
| Lapped | `+2 laps` | `+2랩` |
| Not classified | `DNF` · `DNS` · `NC` | `DNF` · `DNS` · `NC` |
| Position | `P2`; in a sentence "second" | `P2`; 문장에서는 `2위` |
| Places gained | `▲3` · `▼2` · `–` | `▲3` · `▼2` · `–` |
| Pit stop | `2.41 s`; against target `+0.93` / `−0.09` | `2.41초`; `+0.93` / `−0.09` |
| Speed and distance | `243 km/h` · `2,840 m` · axis `0 1 2 … 5 km` | `243 km/h` · `2,840 m`; 문장에서는 `시속 240km` |
| Points | `30 pts` | `30점` |
| Laps | `Lap 43` · `laps 43–57` | `43랩` · `43~57랩` |
| Rounds and dates | `Round 18 · Boston · 57 laps · 8 Nov 2026` | `18라운드 · 보스턴 · 57랩 · 2026년 11월 8일` |

- Timing keeps the thousandth (that is how races are timed and decided); stationary times two decimals; averages per lap two decimals (`0.33 s a lap`); swings over a stint one decimal (`took 11.4 s out of the winner`).
- The minus sign is a true minus (−). Units are smaller than the number and never wrap away from it (no-break space).
- Positive gaps carry `+`; a gap at the flag is never shown without its sign. The winner's row shows the race time instead of a gap.


## Layout Principles

- Page 1400px wide at most, 32px side padding (24px under 1360px, 16px under 640px), 16px between panels, 56px between sections.
- Header, one line, 60px: the team and report name in condensed capitals (`VIZNEY RACING  RACE DEBRIEF`), the round tabs as pills (the selected round white with black text), the EN/KO pill. The round filter applies to every view and is kept in the URL (`?round=18`).
- First screen (1440 × 810): two columns, 560px | the rest. Left: the eyebrow (`ROUND 18 · BOSTON · 57 LAPS · 8 NOV 2026` and a `FINAL CLASSIFICATION` tag), the result in one or two sentences, a line on the second car and points against plan, then the onboard display. Right: Figure 1, the circuit map, the same height as the left column.
- Sections are numbered and named like a timing sheet: `01 RACE` (Figure 2 tower 1.15 | Figure 3 gap 1), `02 LAP` (Figure 4 telemetry, full width), `03 PIT LANE AND SEASON` (Figure 5 | Figure 6, then Table 1), `04 HOW IT'S BUILT`, `05 HOW THE NUMBERS ARE COUNTED`, footer.
- Every figure and table is one panel with one anatomy: figure label (`FIG 2`, condensed capitals, muted) → the finding as the title → a subtitle with the method and unit → keys → the view → a note that starts with `Note:`.
- Panels side by side end on one line (`grid-template-rows: subgrid` over label, view and note); the shorter view grows. At most seven views per section.


## Component Stylings

**Round tabs.** 34px pills, condensed 15px/600 capitals, the round number bold; hover `#15151e` with white text; selected white with `#000000` text.

**Onboard display.** A face of `#0d0d14` with a 1px `#303037` rim and 24px corners, padding 16px 20px 14px.
- Lights: 15 circles of 15px, 7px apart, centred; green `#04a97a` for a lap quicker than the winner's same lap, yellow `#b88c19` slower, `#26262f` when either car was on an in- or out-lap. A 13px caption under them: `LAPS 43–57 AGAINST THE WINNER, OKA ● QUICKER ● SLOWER`.
- Dials: a 240° arc (150° to 390°), radius 50, 9px stroke; the track `#26262f`, the value arc green when the target or plan is met and yellow when not; scale ticks `#47464c` outside the arc; the target or plan as a white 2.25px tick with a 5px card-coloured halo; the value 31px/700 in the middle with its unit under it; the scale ends (`2.0` `3.5`, `0` `43`) 12.5px muted. Pit stop average runs 2.0–3.5 s with the 2.50 s target; team points run 0–43 (the most two cars can score) with the round's plan.
- Gear readout: the finishing position of the lead car, `P` small and gray, the digit 98px/700 white; a status line under it (`▲ 3 places from grid P5`).
- Readouts: two cells under a 1px `#303037` rule, split by a rule: gap to the win (`+0.457 s`, `▲ 12.9 s closer than round 17`) and the best lap (`1:20.142`, in a purple `#8c51d9` chip with 4px corners when it is the race's fastest, and `Fastest of the race · lap 43`).
- Each status line is 13.5px/600 in the text step of its status with ▲ or ▼.

**Circuit map.** The track as a `#0d0d14` band of 19px (15px on phones) with round joins; the 24 mini-sectors on top as 10px strokes in the diverging ramp, separated by 2px `#0d0d14` cuts; a white 4px start/finish bar with a card-coloured halo, white 2px sector lines, labels `S/F`, `S2`, `S3` 13px/700 white; turn numbers 12.5px/600 muted outside each apex, moved further out or inside when they would touch the track or another label; a small gray chevron after the line for the direction. The foot holds the ramp as seven 22 × 8px swatches between `QUICKER` and `SLOWER`, and the sector and lap gaps (`S1 −0.194  S2 +0.071  S3 −0.378  LAP −0.501`) in the purple or yellow text step. Hover outlines the mini-sector in white and puts a white dot where the pointer is. On phones the map's height follows the track's proportions.

**Timing tower.** Rows of 34px with a 1px `#1f1f29` rule; columns: position (a 28 × 23px box, white with black digits for our cars), places gained (`▲3` green text step, `▼2` yellow text step, `–` muted), the car code 700 with .05em tracking, the team muted, the gap right-aligned and tabular, and the tyre stints. Stint strips are 14px high with 2px corners, 2px gaps at each stop, the compound letter 11px/700 inside; a purple dot over the lap of the race's fastest lap; `✕` at a retirement. Our rows are `#1c1c25` with a 3px white inset edge. The top ten, then our retired car under a rule with `DNF` and the lap. The lap axis under the strips: `LAP 1 10 20 … 57`.

**Gap to the winner (Figure 3).** One white line for car 27 at the end of each lap; the winner is the zero line (`#8b8f99`, 1.5px, labelled with its code at the right); above the line is ahead. Laps between one car's stop and the other's matching stop are shaded `#1c1c25` and drawn dashed in `#b9bcc6`, and may run off the scale; the axis is set from the other laps. Two tyre strips under the plot (ours, then the winner's), labelled with the car number and code.

**Telemetry (Figure 4).** The speed of both best laps against distance (50–350 km/h, gridlines at 100, 200, 300): car 27 white 2px over a 5px card halo, the winner `#8b8f99` 1.5px. Sector lines `#47464c` dashed through both panels with `S1`, `S2`, `S3` at the top; turn numbers `T1`… under each speed minimum, nudged down when they would touch. Below, the running gap: up is car 27 ahead (fill `#8c51d9` at 30%), down is behind (`#b88c19` at 30%), the white line on top, the final value at the right end in its text step. A 170 × 104px circuit in the panel's top-right corner shows where the cursor is.

**Pit stops (Figure 5), season (Figure 6), stint report (Table 1).** Pit stops are bars of stationary time, slowest first, with the target as a white dashed line, the field's best and median as reference rows and the excess printed beside each bar (`+0.93` in the yellow text step). Season points are a running total by round: our team white, the team ahead `#8b8f99`, the plan dashed; the rounds to go in a `#0d0d14` band. The stint report groups rows by car (`Car 27 · MAR · P2 · 18 pts`): stint, a lettered tyre chip, a laps bar on a 120px track with the range, average lap, a wear bar with `+0.034` (s/lap), the best lap in a purple chip (race's fastest) or green chip (car's own best), the stop with its excess against target, a note for anything unusual.

**Tooltip.** `#1c1c25`, 1px `#47464c`, 6px corners, a soft shadow, 9px 12px 10px padding; a bold head, a muted sub line, then rows of key swatch, value and label; status values in their text step. It adds detail and is never the only copy of a number.

**Buttons and code.** Pills: 36px, 18px corners, condensed 15px/600 capitals, white fill with black text for the primary, a 1px white outline for the secondary. Code windows on `#0d0d14` in Roboto Mono 12.5px with the screen's own text steps (keyword `#c4b5fd`, string `#6ee7a8`, number `#f2c94c`, function `#ff8f87`).


## Charts

- **Choose by the question.** Start with the race's own instruments and draw a chart only where they cannot answer.
  - How did the round go against target and plan → the finding headline and the onboard display (position from the grid, gap to the win against the last round, best lap against the fastest, pit stop average against 2.50 s, points against plan).
  - Where on the lap did we gain or lose → the circuit map by mini-sector with the sector gaps (Figure 1).
  - How did the field finish, and on which strategy → the timing tower with tyre stints (Figure 2).
  - How did the race unfold against the winner → the gap at the end of each lap with pit cycles marked (Figure 3).
  - Why the lap was quicker or slower: straights or corners, which turn → the speed trace with the running gap (Figure 4).
  - Which stops missed the target, and why → pit stops, slowest first, against target, the field's best and median (Figure 5).
  - Where do we stand in the season → points by round against plan and the team ahead (Figure 6).
  - The detail of every stint → the stint report (Table 1).
- **Titles.** The title is the finding, recomputed for each round: `Car 27’s best lap beat the winner’s by 0.501 s, but lost 0.071 s in sector 2`; `Car 27 ran ahead of the winner from lap 51 until the last lap and finished 0.457 s behind`; `Car 27 gained 0.554 s on the straights but lost 0.094 s around turn 9`. The subtitle names the method and the unit.
- **Marks.** Subject lines 2.5px white over a 6px card halo; comparisons 1.5–1.75px `#8b8f99`; pit cycles and plans dashed (`3 3`); markers ≥ 8px; bars with 2px corners and 2px gaps.
- **Axes.** Gridlines `#303037` on rows only, no axis lines; ticks 12.5px/600 condensed muted, four to six nice steps; the lap axis `LAP 1, 10, 20 … last`; distance in km.
- **Labels.** Line ends carry the car and the value; the map's sector gaps are in its foot; values in tables are rounded to the timing precision above.
- **One axis.** Never a dual axis. Speed and the running gap are two panels with their own scales on one distance axis.
- **Never:** pie, donut, 3D, gauges that hold no target, gradients on data, smoothed lines, rainbow sector colours, real circuits, teams, drivers or liveries, chequered-flag or carbon textures, glowing LEDs, photos or logos, decoration that carries no number.
- Every chart, the map, the display and the tower have a tooltip, keyboard control and a screen-reader table.


## Depth & Elevation

Flat. Depth comes only from surface steps: page `#000000`, panels `#15151e`, our rows and the tooltip `#1c1c25`; the onboard display and the track sit lower, on `#0d0d14`. The tooltip is the only element with a shadow. No gradients, no glow, no bevels.


## Interaction & Motion

- The round tabs filter every view; the URL keeps `?lang=` and `?round=`. Language switches in place and only the language's own fonts are used.
- Every view responds to hover and to the keyboard: Tab to focus, arrow keys to move (laps, mini-sectors, cars, 100 m of track, stints), Home and End, Esc to close; a polite live region reads the focused item. The onboard display moves in visual order: lights, stop dial, position, points dial, gap, best lap.
- Motion (`cubic-bezier(.4,0,.2,1)`): the lights fade in 0.25s, 40ms apart; dial arcs draw in 0.9s; the map's mini-sectors fade in lap order, 0.3s, 28ms apart; tyre stints grow from the left, 0.5s, 120ms apart. With `prefers-reduced-motion` everything appears complete.


## Accessibility

- Text ≥ 4.5:1: white 18.1:1, `#d9d9df` 12.9:1 and `#aaaaaa` 7.8:1 on the card; status text steps ≥ 4.5:1; white on purple 4.9:1, `#15151e` on green 6.0:1 and on yellow 5.9:1.
- Status never relies on colour alone: ▲ ▼, signs and words; tyres carry S, M, H; the map's foot and tooltip give every sector and mini-sector as a number.
- Every view has a screen-reader table; the focus ring is 2px white with a 2px offset; targets are at least 30px high.


## Responsive Behavior

- ≥ 1360px: as described.
- 1200–1359px: 24px padding; first screen 500px | the rest.
- 1024–1199px: first screen 452px | the rest, the display's dials at 128px and the gear at 84px; the tower drops the team column.
- 900–1023px: the first screen stacks (headline and display, then the map at 420px); figures stack one per row.
- 640–899px: one column; the telemetry's small circuit is hidden.
- Under 640px: 16px padding; the display puts the position on top and the two dials side by side; the map's height follows the track; the tower keeps position, change, car, gap and stints; the stint report drops average lap, wear and note (the row tooltip keeps them).
- Captured and checked at 1440, 1200, 1024 and 390px in both languages, with no horizontal scroll.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` (installed in `.claude/skills/dashboard-style/`; or copy the `colors` block from the front matter) and these fonts (the second for Korean).

<!--email_off-->

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Barlow:wght@400;500;600&family=Roboto+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
```

<!--/email_off-->

The dials are one SVG each (two arcs and three lines on a 150 × 118 viewBox); the lights are 15 `<i>` elements. The map is one SVG: the circuit as a closed path of x, y points every 20 m, each mini-sector a separate path over the dark band, labels placed by testing candidate offsets against the track and the labels already placed. Figure 4 is one SVG with two panels and two clip paths for the purple and yellow fills. Panels use `grid-template-rows: subgrid` so neighbours end on one line.

**Tableau.** Paste the `<color-palette>` elements of `race-timing.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette runs soft, medium, hard, then gray; the status palette purple, green, yellow.
- Dashboard background `#000000`; each sheet's worksheet and pane shading `#15151e`, no borders, gridlines `#303037` on rows only, text `#d9d9df`, headers `#aaaaaa`. Title each sheet with the finding; the method in a caption.
- Onboard display: a horizontal container on `#0d0d14`. Lights: a circle mark per lap (15 columns) coloured by a calculated `Quicker / Slower / Pit lap`. Dials: a donut-free version — a bar on a fixed axis (2.0–3.5 s; 0–43 pts) with a reference line for the target or plan, or a text BAN with the status line; the position as a large text object `P2` with `▲3` under it.
- Circuit map: a line mark with X and Y as continuous axes (fixed to equal scales), Path on distance, Detail on mini-sector, Colour on the gap (diverging, purple for negative, stepped at ±0.005, ±0.02, ±0.05); a second line mark (dual-mark, same axes) in `#0d0d14` and a larger size underneath for the track band.
- Timing tower: a text table for position, change, car, team and gap beside a Gantt bar sheet (`lap_start`, size `laps`, colour `compound`) from `stints.csv`; highlight our rows with a calculated band.
- Gap to the winner: a line on `gap_s` by lap with a reference line at 0 and a reference band for each pit cycle; telemetry: two sheets on one distance axis (speed; running gap with an area for ahead and behind), not a dual axis.
- Formats: `m:ss.000` via a calculated string for lap times, `+0.000" s";−0.000" s"`, `0.00" s"`, `0" pts"`; Korean workbooks `+0.000"초"`, `0"점"`. Fonts: Tableau Book unless Barlow is installed on every viewing machine and the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json`. It sets the data colours (soft, medium, hard, then gray), the black page, `#15151e` visuals with 8px corners and no border, axis and gridline colours and text classes. Install Barlow and Barlow Condensed on authoring and viewing machines or accept Segoe UI.
- Title each visual with the finding; the method in the subtitle; notes in a text box that starts with `Note:`.
- Onboard display: card visuals on a `#0d0d14` rectangle; lights as a 15-column matrix with conditional background colours; the dials as a bar or KPI visual with a target (avoid the gauge unless it shows the target tick); the best lap card with a `#8c51d9` background when it is the race's fastest.
- Circuit map: a scatter chart of the track's x, y points (equal axes, markers 3–4px, no gridlines) with conditional colour on the gap, or a Deneb (Vega-Lite) line with `detail` on mini-sector.
- Timing tower: a table visual beside a stacked bar of stints by lap (colour by compound, data labels S, M, H).
- Gap and telemetry: line charts with a constant line at 0; speed and gap as two visuals stacked on one x axis.

**Chart libraries (D3, Observable Plot, Vega-Lite, matplotlib, Datawrapper).** Background `#15151e`; subject `#ffffff` 2.5px with a 6px `#15151e` halo; second `#b9bcc6`; winner or rival `#8b8f99`; other cars `#5f6270`; gridlines `#303037`; text `#d9d9df`, ticks `#aaaaaa`; status `#8c51d9` / `#04a97a` / `#b88c19` (text `#c4b5fd` / `#6ee7a8` / `#f2c94c`); tyres `#cc3336` / `#b88c19` / `#d9dce2` with letters; diverging `#bb9ef9 #946ade #6f4bac #4a4d57 #7b5f06 #a58108 #d6ab32`.


## Do's and Don'ts

| Do | Don't |
|---|---|
| Use purple, green and yellow with their timing meanings everywhere, with a word or ▲ ▼ | Use the status colours to tell cars or teams apart |
| Keep our cars white and every other car gray | Give every car its own colour or a team livery colour |
| Put a target or plan on every key figure (dial tick, dashed line, chip) | Draw a dial or gauge that has no target |
| Letter every tyre mark S, M, H | Rely on red, yellow and white alone for compounds |
| Show timing to the thousandth, stops to the hundredth | Round lap times to tenths, or drop the sign of a gap |
| Mark pit cycles when you compare cumulative time | Let a pit stop's 20 seconds flatten the rest of the race |
| Keep panels flat on `#15151e` with 8px corners | Add borders, glow, carbon fibre or chequered flags |
| Name the style by its format | Use F1 marks, logos or the official typefaces |


## Agent Prompt Guide

Install the style (`npx @vizney/styles@latest add race-timing`, `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- race-timing`, or unzip the package in the project root). Agents that read skills load `dashboard-style` on their own and work in one of three modes: **Build** (plan the views, then draw them to this file), **Restyle** (keep the data and the questions, change the look) and **Review** (check a screen against the checklist below). Other agents can be given this prompt:

```
Read DASHBOARD.md and follow it exactly. Build our race debrief as one self-contained HTML file with fictional data,
in English and Korean (?lang=en|ko, English by default), on the black page the spec describes.
Header on one line: "VIZNEY RACING  RACE DEBRIEF" in condensed capitals, the round tabs as pills (the filter for every
view, kept in the URL), the EN/KO pill.
First screen: the eyebrow with round, city, laps and date and a FINAL CLASSIFICATION tag; the result in one or two
sentences; the second car and points against plan; then the onboard display (15 lights for the last 15 laps against
the winner, a pit stop dial with the 2.50 s target, the finishing position as the gear readout, a points dial with the
plan, the gap to the win and the best lap). Beside it, Figure 1: the circuit map, car 27's best lap against the winner's
in 24 mini-sectors on the purple–gray–yellow ramp, with S/F, sector lines, turn numbers and the sector gaps.
01 Race: the timing tower with tyre stints, and the gap to the winner lap by lap with pit cycles shaded.
02 Lap: the speed trace of both best laps with the running gap below and a small circuit that follows the cursor.
03 Pit lane and season: pit stops against target, season points against plan, the stint report.
Every view on the same panel: figure label, finding title, subtitle, keys, view, note. At most seven views per section.
Use only the values in Data Colors, the formats in Numbers, Dates & Units and the components in Component Stylings.
Every view needs a tooltip, keyboard control and a screen-reader table.
```

Before it is done, the agent checks:
- [ ] The headline is the finding; the onboard display shows all five figures, each against its target, plan, grid or the last round, with ▲ ▼ and a word.
- [ ] The lights are the last 15 laps against the winner with pit laps dark; the dials carry a white target or plan tick.
- [ ] The map compares the two best laps by mini-sector on the diverging ramp; its sector gaps add up to the lap gap; labels never touch the track or each other.
- [ ] Our cars are white (car 12 `#b9bcc6`), the winner `#8b8f99`, everyone else `#5f6270`; purple, green and yellow are used only with their timing meanings.
- [ ] Every tyre mark is lettered; stints split at each stop; the fastest lap is a purple dot or chip.
- [ ] The gap chart marks pit cycles; the telemetry has two panels on one distance axis, never a dual axis.
- [ ] Timing to the thousandth, stops to the hundredth, signs on every gap, true minus signs, in both languages.
- [ ] Panels side by side end on one line at 1440, 1280 and 1024px; nothing breaks at 390px.
- [ ] Text ≥ 4.5:1; every view has a tooltip, keyboard control and a data table; the round filter changes every card.
- [ ] No logo, official typeface, photo, real team, driver or circuit, and the style is named by its format.
