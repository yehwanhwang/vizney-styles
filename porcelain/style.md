# Porcelain

**Airy white cards, blue–mint rings** · 여백 넓은 흰 카드와 파랑·민트 링

A dashboard style from Vizney Styles. Plain white cards sit on a pale blue-gray canvas beside a white icon rail, with wide margins and very soft shadows. Light and orderly: thin lines, rings and a gauge carry the data in one clear blue and a fresh mint, and the cards stay white.

- Live sample: https://styles.vizney.com/porcelain/ (add `?lang=en` for English)
- To reuse it, ask for "the Porcelain style" and share this page: https://styles.vizney.com/porcelain/style.html


## Layout

- App shell: a white icon rail (88px, sticky) beside the main area on a pale canvas. Main area max 1480px wide with 28px padding (24px on top).
- Header bar: a white card, at least 64px high, along the top of the main area. On the left the page title (15px medium) and a hairline divider, then the filter tabs. On the right a period chip with a calendar icon, the KO/EN pill toggle, a notification bell with a small dot, the user's role and a 36px avatar.
- Filter: plain text tabs in the header (in the sample: the hotel's properties). They scope every card below; cards never carry their own filters.
- 12-column grid, 16px gap. Row 1: line card (4) · bar card (5) · gauge card (3). Rows 2–3: two ring cards (3 each) and, under them, two list cards (3 each), beside a calendar heatmap card (6) that spans both rows.
- Up to 1359px the rail narrows to 72px, the padding to 20px, the gap to 14px and card padding to 24px, so the full desktop layout still fits a 1200px blog column. Below 1180px the grid goes to two columns (line | gauge, bars full width, ring | ring, calendar full width, list | list) and the role name hides. Below 1024px the tabs move to their own row in the header. Below 900px the rail disappears. Below 640px everything stacks in one column (16px page padding, 20px card padding).


## Color

| Token | Hex | Use |
|---|---|---|
| ink-strong | `#2F3546` | page and card titles |
| ink | `#3D4257` | figures, values, list names |
| ink-2 | `#6B7387` | labels, captions, legend text, units (4.7:1 on white) |
| muted | `#8A92A3` | axis ticks, weekday names |
| canvas | `#F5F6FA` | page background |
| card | `#FFFFFF` | cards, header bar and rail; shadow `0 1px 2px rgba(35,48,77,.04), 0 3px 10px rgba(35,48,77,.045)`, on hover `0 14px 34px rgba(35,48,77,.11), 0 3px 8px rgba(35,48,77,.05)` |
| hair / grid | `#EEF1F5` / `#EDF0F5` | row dividers, gridlines |
| hair-2 | `#E3E7EE` | baselines, crosshair, tooltip border |
| blue (c1) | `#2D94F0` | the main series and single-series marks: the trend line, the target ring, the first category, rail icons |
| mint (c2) | `#27CF8E` | the highlighted period in bars, the gauge, the share ring, the second category; hover `#19B97B` |
| amber (c3) | `#EAA20E` | the third category |
| other | `#B8BFCB` | the gray "other" category |
| comparison | `#AEB6C4` | the comparison series, dotted |
| bar-muted | `#DFE3EB` | bars outside the highlighted period; hover `#C4CBD8` |
| tracks | `#DBE9FC` / `#D3F2E4` | ring and gauge tracks (light blue / light mint) |
| blue-text | `#1A6FCF` | the active tab |
| good | `#0A7F51` on `#E5F8EF` | positive delta text and change chips |
| bad | `#B3352F` on `#FEECEB` | negative delta text and change chips |
| heat | `#EEF5FE` → `#D3E6FC` → `#A6CDF8` → `#68A8F1` → `#2480E2` | sequential ramp, one hue, from 60% to 100% |
| accent dot | `#F25F5C` | the notification dot only |

Chart marks, checked for color-vision deficiency against white:

- Categories: blue, mint, amber in that order pass on all pairs (worst CVD ΔE 11.3, normal vision 21.4). Gray "other" sits next to amber and is separated by 2px gaps and labeled rows.
- Mint (2.0:1) and amber (2.2:1) are below 3:1 on white, so they are always named in a legend or list row and listed in the screen-reader table.

The canvas is the only tint. Cards stay white, marks use the tokens above, and data colors never color text.


## Type

- Spoqa Han Sans Neo: `https://cdn.jsdelivr.net/gh/spoqa/spoqa-han-sans@v3.3.0/css/SpoqaHanSansNeo.css`
- Body 14px. Card titles 15px medium in ink-strong. Labels, deltas and captions 12.5px in ink-2. Axis ticks 11px in muted.
- Figures are light in weight, not bold: 36px regular with −0.02em tracking (28px in the ring centers). Units and suffixes (억, 건, 명, 박, %, ₩, M, K) sit next to the number at 15px medium in ink-2, 13px in the rings.
- A KPI block uses two sizes only: the figure and everything else. Weight and color do the rest.
- `tabular-nums` only where numbers line up: axis ticks, tooltip values, list values.
- Korean text breaks between words (`word-break: keep-all`).


## Components

- **Card:** white, 6px radius, 28px padding, no border. On hover the shadow grows and softens, as if the card lifts.
- **KPI block:** label on top, the figure on its own line, then the delta: the signed value in bold good or bad, then the comparison in ink-2. Every block has a label line, so the figures line up across a row.
- **Line card:** the plot runs edge to edge across the card. A 2px monotone curve in blue, the comparison as a 2px dotted gray line (round dots 5px apart), no gridlines, five month ticks. The last point is a hollow dot (white fill, 2px blue ring). The focused point gets a 13px blue halo at 18%, a white dot with a 2.5px ink ring, a hairline crosshair and the tooltip. At rest the tooltip sits on the peak month and hides if it would cover the figure.
- **Before/after bars:** thin columns (at most 14px, about a third of the slot) with 4px round tops on a hairline baseline, three ticks on the right. Bars before the event in bar-muted, after it in mint, with x labels a step darker. A mint teardrop pin with a white flag marks the first month after the event.
- **Gauge:** a 240° arc open at the bottom, 7px with round caps, mint on the mint track, with a white knob (3px mint ring) at the value and −100 / 100 at the ends. A small mint smiley and the 36px score sit in the middle, the grade in bold below (good color when strong), then two short lines of shares and the response count.
- **Rings:** 148px, 7px stroke with round caps, starting at 12 o'clock: blue on the blue track for progress to a target, mint on the mint track for a share. In the center a small outline icon with two tiny sparkles, the figure, and a 12px caption. A legend with hollow dots underneath (it stacks into two rows when the card is narrow).
- **Calendar heatmap:** a Monday-first month in seven columns, cells with a 6px radius and a 6px gap colored on the heat ramp, the day number top left (11px) and the value bottom right (13px medium), in ink or white, whichever reads better on the cell. Holidays carry a mint dot with a white ring. Days outside the month are faint blanks. Under a hairline, weekday averages as 10px bars aligned to the columns, with values above them and the month average on the right. Below 440px the cell values hide.
- **Composition:** an 8px stacked bar with 2px white gaps and round ends, then rows with a hollow dot, name, value with a small unit and the share. Hovering a row or a segment dims the rest.
- **Ranking list:** name, value with a small unit and a pill change chip (diagonal arrow and one decimal) in good or bad.
- **Tooltip:** white, 1px hair-2 border, 6px radius, shadow `0 8px 22px rgba(35,48,77,.13)`, a small arrow. An 11px title, then one row per series: a short line key, the value in bold and the series name.
- **Legends:** line keys for lines, small squares for bars, hollow dots for rings and lists.
- **Tabs and toggles:** text tabs, the active one in blue-text and medium weight. The KO/EN toggle is a pill on `#F1F3F8` with the selected side in white with a soft shadow.
- **Icon rail:** outline icons in blue (1.7px stroke, round caps). The active item sits in a 48px white tile with a soft blue-gray shadow.


## Motion and interaction

- On load the trend line draws in (1.2s), the bars grow from the baseline (0.7s, staggered 35ms), the rings and the gauge sweep into place (1.1s) and the resting tooltip fades in after the line.
- Changing the filter redraws the line, regrows the bars, sweeps the rings, the gauge and its knob to the new values, crossfades the calendar cells (0.5s), resizes the stacked bar (0.6s) and fades the lists in.
- Every chart has a hover tooltip, a keyboard mode (arrow keys, Home and End, Esc) that announces values, and a screen-reader table. On touch screens a tap pins the point and a tap elsewhere clears it. Motion is off under `prefers-reduced-motion`.


## Don'ts

- No card inside a card. No dark mode.
- Keep the cards plain white: no gradients, no tinted card backgrounds, no borders. The canvas is the only tint.
- No more than three category colors; fold the rest into gray "other". Text never wears a data color.
- No dual axes and no dashed gridlines: dots are for the comparison series, and the line card has no gridlines at all.
- No bold figures: weight goes to labels and deltas, the figures stay regular.
- Don't use the good or bad colors on a series.
