# Anthropic

**Warm ivory, editorial serif, hairline rows** · 따뜻한 아이보리와 에디토리얼 세리프, 헤어라인 행

A dashboard style from Vizney Styles, read from the public design of anthropic.com and claude.com. The screen sits on a warm ivory canvas, opens with the month's headline written as a serif sentence, and keeps everything else quiet: ivory cards with no border or shadow, lists divided by hairlines, one clay accent for the data, and a single ink-black band for the detailed table. Figures stay regular weight; size and color do the ranking.

- Live sample: https://styles.vizney.com/anthropic/ (add `?lang=ko` for Korean)
- To reuse it, ask for "the Anthropic style" and share this page: https://styles.vizney.com/anthropic/style.html

Not an official Anthropic design, and not affiliated with or endorsed by Anthropic. The tokens below are read from the publicly visible design of anthropic.com and claude.com; the style carries no logo, typeface or data of theirs, and the sample's publisher and numbers are fictional. Trademarks belong to their owners.


## Layout

- One column on the ivory canvas, max 1400px wide, 32px side padding (24px up to 1359px, 16px below 640px). No sidebar, no app chrome: the page reads top to bottom like an article.
- Header (84px): the company name in serif on the left with a small uppercase caption under it; on the right a period pill, the KO/EN pill toggle and one ink pill that jumps to the dark band. Nothing else.
- Filter row under a hairline: pill tabs on the left (in the sample: the publisher's imprints), a one-line basis note on the right. The tabs scope every card and the statement below.
- Statement: the headline figure as a serif sentence, 26–40px, with the numbers in ink, then a one-line sans lead that names the top item. This block is the style's signature: a dashboard that starts by saying the result in words.
- 12-column grid, 16px gap. Row 1: four KPI cards (3 each). Row 2: trend card (7) · ranked list card (5). Row 3: single-hue bar list (6) · stacked composition (6). Then a full-width dark band holding the detail table.
- Up to 1179px the KPI cards stay in one row of four and the other cards go full width (bar list and composition side by side). Below 900px the KPI cards sit two by two and every other card is full width. Below 640px everything stacks in one column, the period pill and ink pill leave the header, and the dark table scrolls sideways inside its band instead of wrapping.


## Color

| Token | Hex | Use |
|---|---|---|
| canvas | `#faf9f5` | page background, tooltips, the hollow last point |
| card | `#f0eee6` | cards; no border, no shadow |
| card-strong | `#e8e6dc` | active tab, secondary button, bar tracks |
| pill | `#f5f4ed` | pills (period, language toggle) |
| hair | `#e8e6dc` | row dividers, pill borders, the filter row's top rule |
| hair-2 | `#dedcd1` | chart baseline and crosshair, active tab border |
| ink | `#141413` | headline numbers, figures, titles, the ink pill, the dark band |
| ink-2 | `#30302e` | secondary button text |
| body | `#3d3d3a` | running text |
| text-2 | `#5e5d59` | the statement's words, labels, captions, legend text (5.7:1 on card) |
| text-3 | `#73726c` | axis ticks |
| muted | `#87867f` | rank numbers, the header caption |
| dark-2 / hair-dark | `#1f1e1d` / `#30302e` | dark band row hover / dark band dividers and bar tracks |
| on-dark / on-dark-2 | `#faf9f5` / `#9c9a92` | text on the dark band / its captions and secondary cells |
| clay (c1) | `#d97757` | the one accent: the trend line, single-series bars, the first category, sell-through bars; hover `#c46849` |
| plum (c2) | `#6953a0` | the second category |
| teal (c3) | `#0d9298` | the third category |
| other | `#b0aea5` | the gray "other" category |
| comparison | `#b0aea5` | the prior-year series, dotted |
| good | `#2c6e4f` | favourable change (5.2:1 on card) |
| bad | `#a33d34` | unfavourable change (5.5:1 on card) |
| focus | `#2c84db` | focus ring |

Chart marks, checked against the card color for color-vision deficiency and contrast:

- Categories: clay, plum, teal in that order pass on all pairs (worst CVD ΔE 9.2, normal vision 19.1). Gray "other" sits last, separated by 2px gaps and labeled rows.
- Clay is 2.7:1 on the card, below 3:1, so it is always named in a legend or a row and listed in the screen-reader table. Everything else is above 3:1.

The palette is a warm gray ladder plus one accent. Use clay wherever a single series needs a color; use plum and teal only when categories must be told apart on one mark. Green and red belong to change text only. Text never wears a data color.


## Type

- Serif for the statement, titles of items and the dark band's heading: Noto Serif KR with Source Serif 4 for Latin (`https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;1,8..60,400`). Weight 400, letter-spacing −0.012em on the statement; the numbers in it are weight 500. Never bold. In English, item titles are italic.
- Sans for everything else: Spoqa Han Sans Neo (`https://cdn.jsdelivr.net/gh/spoqa/spoqa-han-sans@v3.3.0/css/SpoqaHanSansNeo.css`). Body 14px; card titles 15px medium in ink; labels, captions and deltas 12.5–13px in text-2; the header caption 11.5px uppercase with 0.06em tracking in muted.
- Mono for the dark table's numbers, dates and the list's rank numbers: JetBrains Mono (`https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500`), 12–13px. Table headers are sans, 11.5px uppercase, 0.06em tracking.
- Figures are regular weight: 34px with −0.02em tracking in the KPI cards (30px below 640px). Units and suffixes (억, 만, 부, %, ₩, M) sit next to the number at 15px in text-2.
- A KPI card uses two sizes only: the figure and everything else. Weight and color do the rest.
- `tabular-nums` on figures, axis ticks, tooltip values, list values and the dark table.
- Korean text breaks between words (`word-break: keep-all`); the money in the statement never breaks.


## Components

- **Card:** ivory `#f0eee6`, 16px radius, 24px padding (20px below 640px), no border, no shadow, no hover change. Depth comes from color steps: canvas → card → card-strong → ink.
- **Pill:** 32px tall, 999px radius, 13px text, 1px hair border on the pill tint. The language toggle is a pill whose selected side turns ink with ivory text. The ink pill (ink fill, ivory text) is the only "primary" control and there is one of them.
- **Tabs:** pills on the canvas with a hair border; the active one is card-strong with a hair-2 border, ink text, medium weight. Hover tints to the pill color.
- **Statement:** an `h1` in serif at `clamp(26px, 2.9vw, 40px)`, line-height 1.28, words in text-2 and numbers in ink at weight 500. Under it a 15.5px lead in text-2 with the item name in serif ink.
- **KPI card:** label 13px on top, the figure on its own line, then one sub-line: the signed change in bold good or bad followed by the comparison in text-2, or a short composition note. Every card has the sub-line, so the figures line up across the row. Change color follows whether the move is good for that metric (a falling return rate is green).
- **Trend card:** the plot runs edge to edge across the card. A 2px monotone curve in clay; the prior year as a 2px dotted gray line (round dots 5px apart); a hair-2 baseline, no gridlines, five month ticks with the last one in ink. The last point is a hollow dot (canvas fill, 2px clay ring). The focused point gets a 13px clay halo at 18%, a canvas dot with a 2.5px ink ring, a hairline crosshair and the tooltip. At rest the tooltip sits on the last month and hides if it would cover the figure or the title.
- **Ranked list (hairline rows):** rows divided by 1px hair lines, 12px vertical padding: a two-digit rank in mono muted, the item title in serif 15px ink with the author in 12.5px text-2 beside it, the value in medium with a small unit, and the change as text only, 12.5px medium in good or bad with a diagonal arrow. No chips, no tinted backgrounds. A full-width secondary button closes the card: 38px, 10px radius, card-strong fill with a hair-2 border, 13px medium ink-2 text and a small arrow; it reveals the next five rows.
- **Single-hue bar list:** rows with the name (fixed 132px), a 6px clay bar on a card-strong track, the value and the share. One hue, because the rows are a magnitude, not an identity. Hovering a row dims the others and darkens its bar.
- **Composition:** a 10px stacked bar with 2px canvas gaps and 5px round ends in clay, plum and teal, then rows with an 8px solid dot, name, value and share. Hovering a row or a segment dims the rest.
- **Dark band:** full-width, ink fill, 16px radius, 28–32px padding. A serif 22px heading in ivory, a caption in on-dark-2, and a real table: sans uppercase headers, serif titles, mono numbers and dates right-aligned, dividers in hair-dark. A sell-through cell holds an 88px 6px bar in clay on a hair-dark track and the percentage; a status pill (22px, 999px radius) is outlined in clay when true and in hair-dark when not. Rows tint to dark-2 on hover.
- **Tooltip:** canvas fill, 1px hair border, 8px radius, shadow `0 8px 22px rgba(20,20,19,.10)`, a small arrow. An 11px title, then one row per series: a short line key or a dot, the value in medium and the series name.
- **Legends:** line keys for lines (dotted for the comparison), solid dots for categories.
- **Footer note:** 12.5px text-2, two lines: the sample note and the non-affiliation notice. Hidden in embed mode.


## Motion and interaction

- On load the trend line draws in (1.2s, ease-out-quart), the comparison line and the list rows fade in with a 40ms stagger, the bars and the stacked segments grow to their widths (0.6–0.7s) and the resting tooltip fades in after the line.
- Changing a tab rewrites the statement and the KPI cards, redraws the line, regrows the bars and segments, and fades the lists and the dark table in again.
- Every chart has a hover tooltip, a keyboard mode (arrow keys, Home and End, Esc) that announces values through a live region, and a screen-reader table. The dark band is a real table and needs none. On touch screens a tap pins the point and a tap elsewhere clears it. Motion is off under `prefers-reduced-motion`.
- Easing everywhere is `cubic-bezier(.165,.84,.44,1)`.


## Don'ts

- No pure white and no cool grays: the canvas is ivory and every gray is warm.
- No borders or shadows on cards, and no hover lift. No card inside a card. No dark mode (the dark band is a surface, not a theme).
- No bold serif and no bold figures: weight goes to labels, deltas and small controls only.
- One accent. Don't spread clay over several series; use plum and teal only for categories on one mark, and never more than three plus gray "other".
- No tinted chips for change: change is text with an arrow. Green and red never color a series.
- No dual axes, no gridlines on the trend, no dashed lines except the dotted comparison.
- Don't put a logo, wordmark or illustration in the header: the company name set in serif is the brand.
