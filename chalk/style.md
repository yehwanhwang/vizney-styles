# Chalk

**Pastel, calm, clean.** · 파스텔톤, 차분함, 깔끔함.

A dashboard style from Vizney Styles: pastel KPI tiles and thin, dark charts on a white page, under a large grotesque name. Calm, friendly and quick to scan. The pastels color the tiles, while the data marks stay thin and dark.

- Live sample: https://styles.vizney.com/chalk/ (add `?lang=ko` for Korean)
- To reuse it, ask for "the Chalk style" and share this page: https://styles.vizney.com/chalk/style.html


## Layout

- One page with no app shell and no sidebar. The page starts with the name.
- Content is at most 1240px wide, with 48px side padding (24px under 960px, 16px under 600px).
- Header: the series line (`VIZNEY STYLES · 01`), the name in capitals, then the three words. The KO/EN toggle sits top right.
- One row of filter pills under the header. They scope every card below; cards never carry their own filters.
- Section label row: section name on the left, period note ("Last 30 days · vs. previous 30 days") on the right.
- Row 1: four KPI tiles of equal width, 16px gap.
- Row 2: the main line chart (2fr) next to a gauge donut (1fr).
- Row 3: a ranked table and horizontal bars, half and half.
- Row 4: three cards that carry the style itself. Sales by color uses the four tile colors as product colors. A campaign banner sets the display font on the dark tile color. A product card holds a photo.
- At 1080 × 1350 the page is a 4:5 poster in one screen. Captures add `?shot=1`, which hides the language toggle and the footer note and stretches the last row to the bottom.
- Under 960px the tiles go 2 × 2, rows 2 and 3 stack, and row 4 becomes one card over two. Under 600px everything stacks.


## Color

| Token | Hex | Use |
|---|---|---|
| ink | `#161616` | primary text, the name |
| ink-2 | `#474747` | secondary text, the three words, series line |
| muted | `#8B8B8B` | notes, legend values, hex codes |
| faint | `#A3A3A3` | axis ticks, ranks |
| surface | `#FFFFFF` | page and card background |
| border | `#EAEAEA` | outline of cards |
| grid | `#EFEFEF` | gridlines, table rules, bar tracks |
| pill / pill-active | `#F1F1F1` / `#D2E7F3` | filter pills |
| tile-blue | `#D2E7F3` | KPI tile 1, color chip |
| tile-green | `#D9EEC8` | KPI tile 2, color chip, "Active" tag |
| tile-orange | `#FEC48E` | KPI tile 3, color chip, "No. 1" tag |
| tile-dark | `#2A2A2A` | KPI tile 4 with white text, color chip, campaign banner |
| good / bad | `#1E8449` / `#D0392B` | change arrows only |

Chart marks, checked for color-vision deficiency against white:

- Line series: ink `#1A1A1A` (solid, the main series) and green `#478F35` (dashed 6/5, the comparison).
- Categories: up to three hues, `#5EA6DA`, `#478F35`, `#F39D52`, plus gray `#8C8C8C` for "other".
- Bars: ink `#1A1A1A` on a `#EFEFEF` track. When a filter picks one channel, the other bars turn `#CFCFCF`.

Pastels are for tiles, chips and tags only, never for marks or text.


## Type

- Name and display: Space Grotesk 700. The name is 84px in capitals with 0.86 line height. The series line is 13px with 0.2em letter spacing. The campaign headline is 34px.
- Body and figures use one font per language: Inter (400, 500, 700) in English and Pretendard in Korean. A screen introduces only the fonts of its own language.
  - `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Space+Grotesk:wght@700&display=swap`
  - `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css`
- The three words: 24px, weight 500, ink-2.
- Body 13px. Card titles 15px bold with a 13px muted note. KPI values 28px bold. The total in the gauge center 22px bold.
- Units and suffixes (억, 건, 원, 개, %, M, ₩) sit next to the number at 13px bold.
- A KPI tile uses two sizes only: the value and everything else. Weight and color do the rest.
- `tabular-nums` wherever numbers line up: axis ticks, tables, tooltips, legend values.


## Components

- **KPI tile:** 12px radius, 16 × 20px padding (18px at the bottom), no border.
  - The label sits top left and the outline icon (20px) top right.
  - The value comes 6px below the label, and the delta chip 14px below the value.
  - The value and chip sit at the bottom of the tile, so values line up across a row even when a label wraps.
  - The delta chip is white with a 6px radius. Its arrow is green or red by direction × whether up is good, and its text stays ink.
- **Card:** white, 1px border, 12px radius, 20 × 22px padding (18px at the bottom). The title row sits 8px above the content.
- **Line chart:** 2px monotone curves, 1px solid gridlines, hollow end markers (4.5px radius) on the main series.
  - Focus is pinned at the peak with a 1px ink crosshair.
  - A dark tooltip (`#232323`, 8px radius) sits at the top beside the crosshair and lists every series with line keys.
  - When the chart is narrower than 520px, the values move into the legend.
- **Gauge donut:** 270° arc, 20px stroke, 3° gaps between segments, round caps on the two outer ends only, at most 164px wide.
  - The center shows a 12px label over the 22px total. Hovering a segment or legend item switches it to that category's share.
  - Legend: two columns with an 11px dot, bold name, and muted value and share.
- **Ranked table:** two-digit rank in faint, bold product name, right-aligned numbers, and 1px `#EFEFEF` rules. The change column has a 14px arrow (green or red) and ink text.
- **Horizontal bars:** 10px bars with a 5px radius on a track, channel name bold on the left, share on the right.
  - When the filter picks a channel, the other rows dim: muted text and `#CFCFCF` bars.
  - Hover or focus shows revenue and change in the dark tooltip.
- **Color list:** 34px chips (8px radius) in the tile colors, with the name in bold over the hex code in muted. Count and share sit on the right, and 1px rules split the rows.
- **Feature card** (campaign, bestseller): a media block on top (8px radius) that fills the card. Below it come the name (13px bold), a meta line (12px muted), and a value row with a 12px bold tag (tile color background, 6px radius).
  - The campaign banner is the dark tile color with a faint chalk-dust noise, a 12px kicker, the headline in the display font, and one line of copy in `#C8C8C8`. The meta line names the fonts.
  - The bestseller photo is a real photo of the product, cropped with `object-fit: cover`.
- **Icons:** outline, 1.8px stroke, round caps.


## Motion and interaction

- Changing a filter fades the KPI values (140ms), tweens lines and arcs (480ms, ease-out) and slides bar widths (480ms).
- Every chart has a hover tooltip and keyboard access:
  - Arrow keys move the line chart's focus.
  - Bars take focus.
  - Legend items focus the donut segments.
  - Filter pills move with the arrow keys.
- Screen-reader tables back the line chart, the donut and the bars.
- Motion is off under `prefers-reduced-motion`.


## Don'ts

- No sidebar or app shell; the page starts with the name.
- No separate swatch or type-specimen panels. Colors, fonts and photos appear inside data cards.
- No card inside a card. Media blocks are pictures, not containers.
- No gradients or shadows on cards; only tooltips cast a shadow.
- No pastel marks or pastel text.
- No more than three colored categories; fold the rest into gray "other".
- No dual axes.
