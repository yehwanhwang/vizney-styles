# Glass

**Pastel gradient, frosted glass cards** · 파스텔 그라데이션과 반투명 글래스 카드

A dashboard style from Vizney Styles. Frosted, translucent cards sit in a soft glass frame over a peach-to-periwinkle gradient, with two pearl-like orbs at the corners. Airy and polished: the background carries the color, while the data stays in one clear blue and two accents.

- Live sample: https://styles.vizney.com/glass/ (add `?lang=ko` for Korean)
- To reuse it, ask for "the Glass style" and share this page: https://styles.vizney.com/glass/style.html


## Layout

- Page: a pastel gradient fills the viewport. Four soft radial blobs (peach top left, lilac top right, periwinkle bottom right, pink bottom left) sit over a 135° peach → pink → lavender → periwinkle base. Two pearl orbs (96px top left, 72px bottom right) overlap the corners of the frame.
- Glass frame: max 1440px wide including 36px side padding (44px on top), 34px radius. Inside, a 78px icon rail (brand tile, nav icons, the active item as a blue gradient tile) sits beside the main area (28 × 30px padding).
- Header row: page title (22px bold) with a one-line period note under it on the left; a period chip and the KO/EN toggle on the right.
- Filter row: one row of glass pills under the header (in the sample: customer type). It scopes every card below; cards never carry their own filters or tabs.
- 12-column grid, 18px gap. Row 1: four KPI cards (3 columns each). Row 2: the main trend card (8) beside a composition card (4). Row 3: a heatmap card (7) beside a ranking card (5).
- Below 1280px the KPI cards go 2 × 2. Below 1100px the trend and heatmap cards take the full width and the two smaller cards sit side by side. Below 760px the rail and orbs disappear and everything stacks in one column (16 × 12px page padding, 16px card padding).


## Color

| Token | Hex | Use |
|---|---|---|
| ink | `#1D2142` | primary text |
| ink-2 | `#4B5075` | labels, legend names |
| muted | `#6A6F8C` | subtitles, captions, units (4.5:1 on the cards) |
| faint | `#868BA5` | axis ticks, rank numbers |
| frame | `rgba(255,255,255,.34)` | glass frame: 26px backdrop blur, 150% saturation, 1px border `rgba(255,255,255,.78)`, shadow `0 40px 100px rgba(104,84,178,.18)` |
| card | `rgba(255,255,255,.64)` | cards: 1px border `rgba(255,255,255,.92)`, shadow `0 12px 32px rgba(107,88,186,.10)` |
| tip | `#1C2142` | tooltip background |
| c1 | `#3A78FF` | the main series and every single-series mark (lines, sparklines, ring, bars) |
| c2 / c3 | `#E87BA4` / `#EDA100` | second and third categories |
| other | `#C5C8D7` | the gray "other" category |
| comparison | `#868BA5` | the comparison series, dashed |
| good / bad | `#0E7448` / `#B93232` | delta text and change chips only (chip fill: the same color at 10%) |
| annotation | `#BF4646` on `rgba(255,107,107,.09)` | a highlighted period band and its label |
| heat | `#E6EDFF` → `#9DBBFF` → `#2F62F5` | sequential ramp, one hue |
| background | `#FDE4D4` → `#F4DBEE` → `#DFD6FB` → `#CBD6FB` | page base; blobs `#FFD5BF`, `#E5C8FF`, `#B8C8FF`, `#FFC6DA` |

Chart marks, checked for color-vision deficiency against the card surface:

- Categories: c1, c2, c3 in that order pass on all pairs (worst CVD ΔE 16.3, normal vision 19.6). Gray "other" stays at least ΔE 11 from each of them.
- Series marks clear 3:1 (c1 3.6:1, comparison 3.1:1). The lighter c2 and c3 are always labeled in the legend and listed in the table.

The pastels belong to the background. Cards are white glass, marks use the tokens above, and data colors never color text.


## Type

- Spoqa Han Sans Neo: `https://cdn.jsdelivr.net/gh/spoqa/spoqa-han-sans@v3.3.0/css/SpoqaHanSansNeo.css`
- Body 13px. Card titles 15px bold with a 12px muted subtitle. Page title 22px bold.
- A KPI card uses two sizes only: the value at 28px bold and everything else at 13px. Weight and color do the rest. Units and suffixes (억원, 만원, 건, %, ₩, B, K) sit next to the number at 13px in muted ink.
- The donut center value is 28px bold over a 13px muted name.
- `tabular-nums` only where numbers line up: axis ticks, tooltip values, legend shares, change chips.
- Korean text breaks between words (`word-break: keep-all`).


## Components

- **KPI card:** glass card, 22px radius, 18 × 20px padding. Label on top, the value on its own line, then the delta (▲/▼ and the value in good or bad) with its comparison note, so the values line up across the row. A visual on the right: a 64px progress ring (7px stroke, c1 on a 14% c1 track, the percentage in the center, a caption below) for a target, or a 54px-high sparkline (2px c1 curve, a 16% wash fading down, an end dot of radius 4 with a 2px white ring).
- **Chart card:** the same glass card with 20 × 22px padding.
- **Trend chart:** a 2px monotone curve in c1 with a soft wash for the current period, a 2px dashed line for the comparison period, solid hairline gridlines and a legend with line keys above the plot. A highlighted period is a tinted band with a small label above it. The focused day gets a rounded c1 gradient column, filled dots with a 2px white ring and a tooltip. Focus starts at the peak day.
- **Donut:** 188px, 16px stroke, 7px gaps, round caps on every segment, with arc lengths corrected so the visible length follows the share. The center shows the largest share and its name. Hovering or focusing a segment or legend row switches the center to it, thickens it to 19px and dims the rest to 25%. Legend rows: dot, name, share, then the change in muted ▲/▼ pp.
- **Heatmap:** days down, 2-hour slots across, 26px cells with a 7px radius and a 5px gap, colored on the heat ramp scaled to the current filter. The peak cell gets a white and blue ring, and one sentence under the grid names it next to a small gradient scale.
- **Ranking:** number, name, value with a small unit, and a pill change chip. Under each row, an 8px c1 bar on a faint c1 track, square at the baseline and 4px round at the end, scaled to the top row. Rows re-sort when the filter changes.
- **Tooltip:** `#1C2142`, 12px radius, 9 × 12px padding, soft shadow, a small arrow. Bold title, one row per series with a line key or dot, values bold and right aligned. It sits above the point and moves beside it near the card edges.
- **Pills and toggles:** 36px high, 12px radius, white at 42% with a white border. The selected one is solid white with a soft shadow.
- **Icons:** outline, 1.8px stroke, round caps.


## Motion and interaction

- On load the cards rise 12px and fade in (0.7s, staggered 40ms), the trend line draws in, the ring fills, the donut turns into place, the heatmap cells fade in on a diagonal and the ranking bars grow.
- Changing the filter fades the KPI values (140ms), tweens the lines, sparklines, ring and arcs (480ms, ease-out), crossfades the heatmap colors (450ms) and slides the ranking rows into their new order.
- Every chart has a hover tooltip, a keyboard mode (arrow keys, Home and End, Esc) that announces values, and a screen-reader table. On touch screens a tap pins the point. Motion is off under `prefers-reduced-motion`.


## Don'ts

- No card inside a card. No dark mode.
- Don't move the background pastels into the data: marks use c1–c3, and text never wears a data color.
- No more than three category colors; fold the rest into gray "other".
- No dual axes, and no dashed gridlines: dashes are for the comparison series.
- Don't use the status green or red on a series.
