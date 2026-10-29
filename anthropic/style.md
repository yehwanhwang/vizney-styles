# Anthropic

**Ivory, Editorial, Quiet** · 아이보리, 에디토리얼, 고요함

A dashboard style from Vizney Styles (Brands 01): a warm ivory page that opens with the month's result written as one serif sentence, then ivory cards with no border or shadow, lists divided by hairlines, one clay accent and a single ink band for the detailed table. Figures stay regular weight; size and color do the ranking.

- Live sample: https://styles.vizney.com/anthropic/ (add `?lang=ko` for Korean)
- To reuse it, ask for "the Anthropic style" and share this page: https://styles.vizney.com/anthropic/style.html

Not an official Anthropic design, and not affiliated with or endorsed by Anthropic. This is a reference style read from the publicly visible design of anthropic.com and claude.com; it carries no logo, wordmark, typeface, image or data of theirs, and the sample's publisher and numbers are fictional. Trademarks belong to their owners.


## Layout

- One page on the ivory canvas with no app shell and no sidebar. It reads top to bottom like an article. Content is at most 1240px wide, with 48px side padding (32px up to 1100px, 24px up to 900px, 16px up to 600px).
- Header: the series line (`VIZNEY STYLES · BRANDS 01`), the name, then the three words. The name is descriptive and set in the serif: "Anthropic style" · "Anthropic 스타일". It is never a large capitalised brand word, which would read as a wordmark. The KO/EN pill sits in the top right corner.
- Filter row under a hairline: pill tabs on the left (in the sample, the publisher's imprints) and the company and period on the right. The tabs scope every card and the sentence below; cards never carry their own filters.
- The statement: the headline result as one serif sentence, with the numbers in ink, then a one-line lead that names the top item. This is the style's signature: a dashboard that starts by saying the result in words.
- Row 1: four KPI cards of equal width, 16px gap.
- Row 2: the trend card (7 of 12 columns) next to the ranked list (5).
- Row 3: three cards that carry the style itself.
  - Cloth colors holds the key colors as the cloths of a clothbound edition.
  - Next to press holds the fonts as the typesetting of the next book.
  - Book of the month holds a cover drawn as a color block, in place of a photo.
- A full-width ink band holds the detailed table, and the disclaimer sits under it.
- At 1080 × 1350 the page is a 4:5 poster in one screen. Captures add `?shot=1`: the language toggle and the sample note hide, the disclaimer stays, and row 3 stretches to the bottom.
- Under 900px the KPI cards go 2 × 2 and the trend and the list stack. Row 3 becomes two cards over the book card, and the table drops its date column.
- Under 600px everything stacks, and the table keeps the title, the sell-through and the reprint status.


## Color

| Token | Hex | Use |
|---|---|---|
| canvas | `#faf9f5` | page background, tooltips, the hollow last point; "Ivory" in the cloth card |
| card | `#f0eee6` | cards, with no border and no shadow; "Oat" in the cloth card |
| card-strong | `#e8e6dc` | the active tab |
| pill | `#f5f4ed` | the language toggle |
| hair | `#e8e6dc` | row dividers, pill and tab borders, the rule above the filter row |
| hair-2 | `#dedcd1` | chart baseline and crosshair, tooltip border, active tab border |
| ink | `#141413` | figures, titles, the selected language, the ink band; "Ink" in the cloth card |
| body | `#3d3d3a` | running text |
| text-2 | `#5e5d59` | the statement's words, labels, captions, legends, the prior year's end value (5.7:1 on card) |
| text-3 | `#73726c` | axis ticks and the prior-year line |
| muted | `#87867f` | rank numbers |
| dark-2 / hair-dark | `#1f1e1d` / `#30302e` | band row hover / band dividers and bar tracks |
| on-dark / on-dark-2 | `#faf9f5` / `#9c9a92` | text on the band / its captions and secondary cells (6.5:1) |
| clay | `#d97757` | the one accent: the trend line and its last point, outlined pills, a cover; "Clay" in the cloth card |
| clay-deep | `#c46849` | sell-through bars on the ink band |
| good / bad | `#2c6e4f` / `#a33d34` | change text only (5.2:1 / 5.5:1 on card) |
| focus | `#2c84db` | focus ring |

Chart marks, checked with the dataviz skill's `validate_palette.js`:

- Trend: the current year is a solid clay line, and the prior year is a dotted line in text-3 `#73726c`. The pair separates for color-vision deficiency (ΔE 8.8) and normal vision (ΔE 17.5). The prior year is gray on purpose: it is the comparison, not a category.
- Clay is 2.7:1 on the card, below 3:1, so the line is always named in the legend, labeled at its end and listed in the screen-reader table.
- Bars on the ink band are clay-deep, which sits inside the dark-surface lightness band (4.8:1 on ink).
- When a chart needs categories, use clay, plum `#6953a0` and teal `#0d9298` in that order, then gray `#b0aea5` for "other" (worst ΔE 12.5 for color-vision deficiency, 19.1 for normal vision). The sample has no categorical chart.

The palette is a warm gray ladder plus one accent. Text never wears a data color: values and labels stay ink or text-2, and green and red belong to change text only.


## Type

- Display serif, one per language: Source Serif 4 in English (with its optical sizes) and Noto Serif KR in Korean. It sets the name, the statement, item titles, the band heading and the book covers. Weight 400, and 500 only for the numbers inside the statement; the serif is never bold. In English, item titles are italic.
- Body sans, one per language: Inter (400, 500, 600) in English and Pretendard in Korean.
- Mono: JetBrains Mono (400, 500) for the band's numbers and dates, rank numbers, hex codes and type sizes.
- A screen introduces only the fonts of its own language.
  - `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Serif+KR:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;1,8..60,400&display=swap`
  - `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css`
- Header and statement:
  - The name is 56px with −0.022em letter spacing and 1.06 line height.
  - The series line is 12.5px, weight 500, with 0.16em letter spacing.
  - The three words are 22px in text-2.
  - The statement is 31px with 1.26 line height, and the lead is 15px.
- Cards:
  - Card titles are 15px medium in ink, with a 12.5px note in text-2.
  - The band heading is 22px serif, and table headers are 11.5px uppercase with 0.06em letter spacing.
- A KPI card uses two sizes only: the figure at 32px regular, and everything else at 13px. That includes the units and suffixes (억, 만, 부, %, ₩, M) that sit next to the number. Weight and color do the rest.
- `tabular-nums` wherever numbers line up: figures, axis ticks, end values, tooltips, lists and the band. Korean text breaks between words (`word-break: keep-all`), and the money in the statement never breaks.


## Components

- **Card:** card color, 16px radius, 18 × 22px padding, no border, no shadow, no hover change. Depth comes from color steps: canvas → card → card-strong → ink.
- **Pills and tabs:** 32px tall with a 999px radius, 13px text and a 1px hair border.
  - The tabs sit on the canvas. The active one is card-strong with a hair-2 border, ink text and medium weight.
  - The language toggle is a pill whose selected side turns ink with ivory text.
- **Statement:** an `h2` in the serif. Its words are text-2 and its numbers are ink at weight 500. Under it, the lead sets the item name in the serif, in ink.
- **KPI card:**
  - The label sits on top, the figure 6px below it, and the change line 12px below the figure.
  - The three rows use CSS subgrid, so figures line up across a row even when a label or a change line wraps.
  - The change line is the signed change in weight 600, then the comparison in text-2. Its color follows whether the move is good for that metric, so a falling return rate is green.
  - A share card shows its split instead ("E-book 17.3% · Audio 5.0%").
- **Trend card:**
  - The plot runs edge to edge across the card. The current year is a 2px monotone curve in clay, and the prior year is a 2px dotted line in text-3, with round dots 5px apart.
  - There is a hair-2 baseline and no gridlines, with five month ticks; the last tick is in ink.
  - The last point is a hollow dot (canvas fill, 2px clay ring). The last values of both lines are written at the right end, in ink and text-2, so the chart reads without hovering.
  - Hovering or focusing a month adds a hairline crosshair, a 13px clay halo at 18%, a canvas dot with a 2.5px ink ring and the tooltip.
- **Ranked list:**
  - Rows are divided by 1px hair lines with 8px vertical padding.
  - Each row has a two-digit rank in mono muted, the item title in the 15px serif, and the author in 12.5px text-2. The author drops out when the card is narrower than 420px.
  - The value is in medium weight with a small unit. The change is text only, 12.5px medium in good or bad, with a diagonal arrow. No chips and no tinted backgrounds.
- **Cloth colors:**
  - Each row has a 26 × 34px cloth swatch with a 3px radius, a 1px border and a faint crosshatch weave. Next to it are the name, the hex in mono, and the count with its share.
  - The four swatches are the key colors: Ivory `#FAF9F5`, Oat `#F0EEE6`, Clay `#D97757` and Ink `#141413`.
- **Next to press:**
  - The title is in the serif (italic in English), with a meta line under it.
  - Below are three hairline rows. Each has the role, the typeface name set in that typeface, and the size in mono: Title Source Serif 4, Text Inter, Figures JetBrains Mono (Noto Serif KR, Pretendard and JetBrains Mono in Korean).
- **Book of the month:**
  - The cover is a 2:3 color block, at most 150px wide, with 2/4px radii and a 7% darker spine on the left. On it sit the title in the serif, a short rule, the author and the publisher in small capitals, all scaled to the cover's width.
  - Covers use only the key colors: clay with ink text, ivory with a hairline and ink text, or ink with ivory text.
  - Beside the cover are an outlined "No. 1" pill (clay border, ink text), the author, the imprint and price, and the copies at the bottom.
- **Ink band:**
  - A full-width ink surface with a 16px radius and 20 × 28px padding. A 22px serif heading in ivory sits beside a caption in on-dark-2.
  - It holds a real table: sans uppercase headers, serif titles, and mono numbers and dates right-aligned, with dividers in hair-dark. Rows tint to dark-2 on hover.
  - A sell-through cell holds an 88 × 6px bar in clay-deep on a hair-dark track, with the percentage.
  - A 22px status pill is outlined in clay when true and in hair-dark when not.
- **Tooltip:**
  - The tooltip has a canvas fill, a 1px hair-2 border, an 8px radius and a `0 8px 22px rgba(20,20,19,.10)` shadow. It is the only thing on the page with a shadow.
  - It has an 11px title, then one row per series: a line key, the value in medium and the series name.
  - It sits above the point, or to its left, its right or below it, whichever fits inside the card. Its arrow always points at the point.
- **Legends:** line keys, with the comparison's key dotted.
- **Footer:** 12px text-2 in two lines, the sample note and the disclaimer. Captures keep the disclaimer, and embeds hide both because the post carries the disclaimer.


## Motion and interaction

- On load, the trend line draws in (1.2s, `cubic-bezier(.165,.84,.44,1)`). The comparison line, the end values, the list rows and the band rows fade in with a short stagger.
- Changing a tab rewrites the statement and every card. The line draws again, and the figures, rows and cover fade in.
- Every chart has a hover tooltip, a keyboard mode and a screen-reader table.
  - On the trend, the arrow keys move between months, Home and End jump to the ends, and Esc clears.
  - The tabs move with the arrow keys.
  - Values are announced through a live region.
- The band is a real table and needs no extra table. On touch screens, a tap picks a month and a tap elsewhere clears it.
- Captures and `prefers-reduced-motion` turn all motion off.


## Don'ts

- No pure white and no cool grays: the canvas is ivory and every gray is warm.
- No borders or shadows on cards, and no hover lift. No card inside a card: the cover is a picture, not a container. No dark mode; the ink band is a surface, not a theme.
- No bold serif and no bold figures. Weight goes to labels, change text and small controls only.
- One accent. Don't spread clay over several series, and never use more than three colored categories plus gray "other".
- No tinted chips for change: change is text with an arrow. Green and red never color a series.
- No dual axes and no gridlines on the trend. The only dotted line is the comparison.
- No logo, wordmark, symbol, the brand's own typefaces, photos or illustrations. The name is written descriptively, and covers are color blocks.
