---
name: Netflix style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 3
tagline: Dark, Cinematic, Bold
tagline_ko: 다크, 시네마틱, 강렬함
source: https://www.netflix.com, https://www.netflix.com/tudum/top10
sample: https://styles.vizney.com/netflix/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#000000"
  card: "#161616"
  plot: "#161616"
  raise: "#232323"
  field: "#2d2d2d"
  hair: "#414141"
  line: "#2d2d2d"
  rule: "#404040"
  ink: "#ffffff"
  body: "#e5e5e5"
  text-2: "#b3b3b3"
  muted: "#808080"
  accent: "#e50914"
  accent-hover: "#c11119"
  gray-button: "#808080"
  good: "#46d369"
  bad: "#e87c03"
  focus: "#ffffff"
data:
  categorical: ["#f0313b", "#6a88f2"]
  other: "#595959"
  comparison: "#808080"
  categorical_text: ["#ff5a63", "#8ea5f6"]
  sequential: ["#9e2027", "#c4262f", "#f0313b", "#ff6b72", "#ffa3a7"]
  diverging: ["#ffa3a7", "#f0313b", "#9e2027", "#3a3a3a", "#3f55a8", "#6a88f2", "#b3c3f9"]
  good: "#46d369"
  bad: "#e87c03"
typography:
  sans: { en: "Roboto", ko: "Pretendard" }
  mono: "Roboto Mono"
radius: {card: "8px", kpi: "8px", button: "4px", feature-card: "16px", chip: "16px", badge: "2px", tooltip: "6px", faq: "0", bar: "2px"}
spacing: {page: "32px", gap: "16px", section: "56px", card: "20px 24px 18px", card-head: "0 0 16px", card-foot: "14px 0 0", billboard: "44px 48px 28px", cell: "8px 10px", episode: "10px", faq: "24px", footer: "28px 32px 40px", feature-card: "24px 16px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: netflix.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: tickets.csv}
---

# Netflix style — DASHBOARD.md

**Dark, Cinematic, Bold** · 다크, 시네마틱, 강렬함

A dashboard design spec read from the public design of netflix.com and its weekly Top 10. Netflix rarely draws a chart: it ranks, badges and lines things up — a billboard with a TOP 10 badge, a Top 10 of outlined numerals, weeks in the Top 10, a thin red progress bar under a thumbnail, an episode list, a hover card with a green score and a rating box, a FAQ accordion. This spec takes those parts and the site's black-and-red tokens and turns them into one card and one chart grammar that a whole dashboard can follow, on one dark page. It then adds what a website spec leaves out and a dashboard needs: validated data colors for a dark surface, card anatomy, chart rules, number and date formats in English and Korean, density, filters, accessibility, and settings for Tableau, Power BI and the web. Add it to a project with one command (or the zip on the sample page), or hand it to whoever builds your dashboards. The live sample was built from it.

```
npx @vizney/styles@latest add netflix
# or, without Node:
curl -fsSL https://styles.vizney.com/install.sh | sh -s -- netflix
```

That puts `DASHBOARD.md` in the project root and the `dashboard-style` agent skill (build, restyle, review) in `.claude/skills/dashboard-style/`, together with `tokens.css`, `tokens.json`, `netflix.tps`, `powerbi-theme.json` and `prompt.md`. Coding agents that read skills pick it up whenever a task touches a dashboard or a chart; any other agent can be told to follow `DASHBOARD.md`.

- Live sample: https://styles.vizney.com/netflix/?lang=en (Korean `?lang=ko`; one city `&city=ny`)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/netflix/DASHBOARD.md
- Package: [netflix-dashboard-style.zip](netflix-dashboard-style.zip) (unzip in your project root) · the skill: [skill/SKILL.md](skill/SKILL.md)
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [netflix.tps](netflix.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [tickets.csv](tickets.csv) (the data behind the sample's Figure 2)
- Catalog: VIZNEY STYLES · 03 · https://styles.vizney.com (Vizney Styles is a line of [Vizney](https://www.vizney.com))

Not an official Netflix design, and not affiliated with or endorsed by Netflix. A reference style read from the publicly visible design of netflix.com; it carries no logo, typeface or data of theirs. The sample's company, Vizney Live, and all its numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A black page with one red. The report opens the way a title opens on Netflix: a billboard. Its key art is a color block — the navy, wine, burgundy and oxblood of the landing page's Trending Now rail — with a giant outlined `1` and a dark vignette on the left. Over it sit a red TOP 10 badge with `#1 this week · <show>`, a bold headline that states the week's result, a short lede like a synopsis, a red button and a translucent gray one, and four key figures on translucent tiles. Below, sections read like the rows of the home screen: a 24px/500 row title, then cards on `#161616` with no border and no shadow, an 8px radius.

The views are the ones Netflix uses for rankings and progress instead of charts: a Top 10 ranked by outlined numerals, each with its title, a bar of tickets, its move since last week and its weeks in the Top 10 (never posters or photos: the data takes the poster's place), weeks in the Top 10 as a grid of ranks, an episode list whose thumbnails carry the continue-watching progress bar, a Top 10 table in the shape of the weekly Top 10 page, and a FAQ accordion for the method. Where a real chart is the right form — a trend, a share over time — it is drawn on the same card with the same restraint: the subject in red, everything else gray.

Red is the voice, and it speaks once per card. The UI red `#e50914` belongs to buttons, the TOP 10 badge and the NEW ribbon; data takes its own step, `#f0313b`, and only for what the title names. Green appears only as good news, orange only as bad. The mood is cinematic and bold: a dark room, one bright figure, the week's result in big type.

Measured in a browser on November 3, 2026 (netflix.com/kr signed out, and netflix.com/tudum/top10): the page is black `#000000`; text is `#ffffff` and, for secondary text, `rgba(255,255,255,.7)` (`#b3b3b3` on black); the headline is 56px/700 on a 70px line and row titles 24px/500; the primary button is red `#e50914` with a 4px radius (32px with 14px/500 in the header, 56px with 24px/500 in the hero) and the secondary button `rgba(128,128,128,.4)` at 40px with 16px/500; the Trending Now posters are `#232323` with an 8px radius (180 × 252), each carrying a 100px/700 numeral filled `#414141` with a 4px white stroke and a soft black glow over its lower-left corner; feature cards are `linear-gradient(149deg, #192247 0%, #210e17 96.86%)` with a 16px radius, 24px/500 titles and `rgba(255,255,255,.7)` text; FAQ rows are `#2d2d2d`, 24px/400 with 24px padding, 8px apart; the rails glow with `#461518` and `#6f181d`, and a curved divider runs `#210d16 → #b82869 → #e50914` with a `rgba(64,97,231,.4)` blue haze. Netflix Sans loads in 400, 500 and 700 with the fallback stack `'Helvetica Neue', 'Segoe UI', Roboto, Ubuntu, sans-serif`, and has no Hangul. The weekly Top 10 page writes the rank as `01` in 36px/900, puts a 16:9 thumbnail before the title, heads its columns in 14px/500 white, draws no rules between rows, and lists weeks in the Top 10, views (`10,700,000`), runtime (`1:48`) and hours viewed in full digits, for Monday-to-Sunday weeks (`10/19/26 - 10/25/26`). The quarterly shareholder letter carries tables, not charts.


## Color Palette & Roles

Surfaces are netflix.com's black and its gray steps; the rules are the product's.

| Token | Hex | Role |
|---|---|---|
| canvas | `#000000` | page, header, footer |
| card · plot | `#161616` · `#161616` | every figure, table and the workbench; the chart sits on the card itself |
| raise | `#232323` | the hover card (tooltip) |
| field | `#2d2d2d` | FAQ rows, install-command boxes |
| hair / line / rule | `#414141` / `#2d2d2d` / `#404040` | the fill of the Top 10 numerals and chart baselines / gridlines and workbench dividers / rules between episode rows |
| ink / body | `#ffffff` / `#e5e5e5` | titles, key figures, table values, the current week's tick / running text, code |
| text-2 | `#b3b3b3` | subtitles, figure labels, KPI labels, values beside end labels; Netflix writes it as `rgba(255,255,255,.7)` on black (8.6:1) |
| muted | `#808080` | notes, axis ticks, table headers, captions (4.6:1 on the card: the lightest gray for small text, and only on `#161616` or darker) |
| accent · accent-hover | `#e50914` · `#c11119` | the primary button, the TOP 10 badge, the NEW ribbon, the selected code tab. White on it is 4.8:1. Data uses its own red, `#f0313b` |
| gray button | `rgba(128,128,128,.4)` with white text | the secondary button beside the red one (Learn more on netflix.com); hover at .6 |
| good / bad | `#46d369` / `#e87c03` | favourable / unfavourable change, text only (9.3:1 / 6.3:1 on the card) |
| focus | `#ffffff` | focus ring, 2px, 2px offset |
| rail | `#192247` `#210e17` `#461518` `#6f181d` | the billboard's key art, thumbnails, the step cards; never data |

Rules:
- Cards are `#161616` on black with no border and no shadow; depth comes from the gray steps, as on netflix.com. Only the hover card and the toast cast a shadow.
- Small text on the card uses muted or lighter; on `#232323` and lighter it uses text-2, because muted drops under 4.5:1 there.
- Red has two steps and they never swap: `#e50914` for UI (buttons, badges, ribbons), `#f0313b` for data. Never a second red series.
- The rail colors are art, not data. Tiles and the billboard use them so the page never needs a photo.


## Data Colors

Netflix shows its own figures with one red against black and gray — the red progress bar, the red TOP 10 badge, the red NEW ribbon — and keeps everything else neutral. This spec keeps that: red is the subject, the gray of the outlined Top 10 numerals is Other, and netflix.com's blue `#4061e7`, raised for a dark surface, is the only second hue. Every value passed an OKLab validator in dark mode (color-vision-deficiency separation, normal-vision separation, contrast) on the card `#161616`, where every chart sits. Use them exactly; do not generate tints.

| Role | Mark | Label text | Use |
|---|---|---|---|
| Subject | `#f0313b` | `#ff5a63` | what the title names: this year, the #1 cells, the sold-out performances, the channel the story is about |
| Second category | `#6a88f2` | `#8ea5f6` | a second real category (web) |
| Other | `#595959` | text-2 | the rest (box office), behind 2px gaps |
| Comparison | `#808080`, dashed 2px (6 on, 4 off) | ink | last year |
| Progress | fill `#f0313b` (the subject) or `#b3b3b3`, track `rgba(255,255,255,.28)` | — | share of a whole: seats sold, seats filled |
| Rank cells | `#f0313b` for #1, `#333333` for #2–10, an outline `#2d2d2d` for not ranked | black on red, `#e5e5e5` on gray | weeks in the Top 10 |
| Target | `#ffffff`, dashed 1.2px (4 on, 3 off) | ink | a goal on an axis |
| Sequential | `#9e2027` `#c4262f` `#f0313b` `#ff6b72` `#ffa3a7` | black on the two brightest, white on the rest | color by value, dim to bright: on a dark card a larger value is brighter |
| Diverging | `#ffa3a7` `#f0313b` `#9e2027` · `#3a3a3a` · `#3f55a8` `#6a88f2` `#b3c3f9` | each arm's brightest | above and below a midpoint that sinks into the card |
| Status | good `#46d369`, bad `#e87c03`, neutral `#808080` | — | change text only |

Validation (from `tokens.json`, dark mode, on `#161616`):
- Red and blue pass every check: CVD ΔE 27.6 (deutan), normal vision 32.8, both inside the dark lightness band, contrast 4.49 and 5.53:1.
- Other `#595959` is neutral by design: CVD 7.4 against red (protan), normal vision 24.9 against blue. At 2.58:1 it always has a second cue: 2px gaps, value labels and a table.
- Comparison `#808080` is 4.58:1, always dashed and labeled at its end.
- The sequential ramp is one hue (spread 8°), monotone, every gap ≥ 0.06 in lightness, the dim end 2.32:1.
- The diverging arms each pass the ordinal checks (dim ends 2.32 and 2.65:1); the poles are 11.7 (CVD) and 15.1 (normal) apart.
- Text: red labels `#ff5a63` 5.9:1, blue labels `#8ea5f6` 7.6:1, good 9.3:1, bad 6.3:1. Digits in rank cells are black on red (5.2:1) and `#e5e5e5` on `#333333` (9.6:1).

Rules:
- Red only for what the title names; the rest gray. A card that is mostly red has highlighted nothing.
- At most two hues plus gray in one chart. A third real category folds into Other or becomes small multiples.
- Color follows the entity, not its rank: the subject is red in every figure.
- Never the UI red `#e50914` on data, never green or orange as a series, never the rail colors as a measure.


## Typography Rules

| Role | English | Korean | Weights |
|---|---|---|---|
| Sans (everything) | Roboto | Pretendard | 400, 500, 700, 900 (Korean 800 where English takes 900) |
| Mono (code only) | Roboto Mono | Roboto Mono, then Pretendard for Hangul | 400, 500 |

Roboto stands in for Netflix Sans; it is in netflix.com's own fallback stack. netflix.com's Korean pages load no Korean webfont (the browser falls back to system fonts), so Korean uses Pretendard. There is no serif.

| Element | Size / weight | Notes |
|---|---|---|
| Headline (billboard) | `clamp(30px, 3.3vw, 48px)` / 700, line-height 1.16, −0.01em | one sentence that states the result, white with a soft shadow (netflix.com: 56px/700 on 70px); Korean line-height 1.28 |
| Billboard line · lede | 18px / 500 · 18px / 400, line-height 1.45 | `#1 this week · <show>` after the TOP 10 badge · two sentences of drivers |
| Key figure value | 40px / 700, −0.02em | units at 0.45em in text-2 (`287.8 K`, `$ 25.68 M`, `28.8 만 장`) |
| Section title · intro | 24px / 500 · 16px / 400 text-2 | the row title of the home screen (measured) |
| Figure label | 12px / 700 uppercase, 0.12em, text-2 | `FIGURE 1 · TOP 10` (Korean 13px, no uppercase: `그림 1 · Top 10`) |
| Card title | 20px / 500, line-height 1.35 | the finding; `text-wrap: balance` |
| Card subtitle · table | 14px / 400 text-2 · 16px / 400 white | |
| Table header | 14px / 500 white, sentence case | the weekly Top 10 page's header (measured) |
| Rank · numeral | `01` 36px / 900 white in the table · 700, filled `#414141` with a 4px white stroke, 58px tall in the Top 10 (44px on phones) | both measured (netflix.com draws the numeral 100px over a 252px poster) |
| Top 10 row | title 16px / 500 white, value 16px / 700 with the unit 12px text-2; meta line 13px text-2 | |
| Note · key | 13px / 400 muted · 13px / 500 body | the note starts with `Note:` / `주:` |
| Axis ticks · value labels | 12px muted · 12px / 700 white | |
| FAQ question · answer | 24px / 400 · 18px / 400 | white on `#2d2d2d` (measured question size) |
| Code | mono 12.5px, line-height 1.62 | |

Headlines are bold (700); titles are medium (500); body is regular. Black weight (900) is only for ranks. Korean breaks between words (`word-break: keep-all`), and a number stays on the same line as the particle after it (`12.3%`, `3주`).


## Numbers, Dates & Units

| | English | Korean |
|---|---|---|
| Tickets, key figure and headline | `287.8K` | `28.8만 장` |
| Tickets in the Top 10 and tables | `33,796` (full digits, as the weekly Top 10 writes them) | `33,796` |
| Tickets on an axis | `150K 200K 250K 300K` | `15만 20만 25만 30만` |
| Money | `$25.68M`, `$924K`; per ticket `$89.22` | `2,568만 달러`, `92.4만 달러`; `89.22달러` |
| Rates | `87.3%`; whole numbers on small labels (`58%`) | the same |
| Points | `+3.8 pts` | `+3.8%p` |
| Runtime | `2:35` (h:mm, as the weekly Top 10 writes it) | `2:35` |
| Change | `+12.3% vs last week` | `+12.3% 지난주 대비` |
| Weeks | `Oct 26 – Nov 1, 2026`; `Week of Oct 26`; ticks `Aug 10 … Oct 26` | `2026년 10월 26일~11월 1일`; `10월 26일 주간`; ticks `8월 10일 … 10월 26일` |
| A performance | `Sat, Nov 7 · 8:00 PM` | `11월 7일(토) 오후 8시` |
| Ranks and weeks in the Top 10 | `#1`, `3 weeks in Top 10`, `12 wk` | `1위`, `Top 10 3주째`, `12주` |
| Missing | `—` (did not play) | `—` |

- Money is in the company's own currency; the sample's company is American, so US dollars.
- Signs use the true minus (`−`, U+2212). One decimal for change.
- The change color follows whether the move is good for that metric: a lower average ticket is orange.
- Units and suffixes are smaller than the digits.
- Weeks run Monday to Sunday and are reported on Tuesday, as the weekly Top 10 is.


## Layout Principles

One column on a black page, at most 1400px wide, 32px side padding (24px up to 1359px, 16px below 640px), a 16px gap between cards and 56px between sections. No sidebar, no logo, no photo.

1. **Header** (72px, black): company name (20px / 900, uppercase in English) and report name (14px text-2). On the right: the period, the EN/KO toggle in an outlined box, an outlined `Export PDF` and the one red button, `Copy as Markdown`.
2. **Filter row**: outlined chips of the cities, the selected chip white with black text; the basis (`Published Tue, Nov 3, 2026 · vs the week before`) on the right. It scopes every card, and the URL keeps the choice (`?city=ny`).
3. **Billboard** (a card of its own, 8px radius, min 420px): on the left (7 of 12 columns) the TOP 10 badge line, the headline, the lede and two buttons (`See the Top 10`, `Method and sources`); the status tag `Final` at the right edge, where Netflix puts the maturity rating; the four key figures in one row across the bottom.
4. **Sections**: a 24px row title and a one-line intro, then rows of cards on a 12-column grid; cards in one row share a subgrid, so their heads, bodies and notes line up.
   - `This week`: Figure 1 the Top 10 (12, two columns of five); Figure 2 tickets by week (7) · Figure 3 weeks in the Top 10 (5).
   - `Coming up`: Figure 4 performances selling fast (7) · Figure 5 where people buy (5); Table 1 every show (12).
5. **`How it's built`**: a paragraph with two 40px buttons, three step cards in the feature-card gradient, the workbench window and a caption.
6. **`Method and sources`**: the FAQ accordion and a source line.
7. **Black footer** with a hairline above the catalog line.

At most seven views on one screen: the billboard and three views in `This week`, three in `Coming up`. Every view is a standard form an agent or a BI tool can rebuild. A chart's body fills its card, so a chart beside a taller one grows to its height. Density: at 1440 × 900 the header, filter row, billboard and all four key figures are on the first screen. Reading order follows the list; never lead with a chart.


## Component Stylings

- **Card**: `#161616`, no border, 8px radius, 20px 24px 18px padding, no shadow. Three parts on a subgrid: head (figure label → title → subtitle → keys, 16px below), body (the view), foot (`Note:` 13px muted, 14px above). Never a card inside a card.
- **Billboard**: the rail gradient at 149° (`#192247 0%, #210e17 48%, #461518 78%, #6f181d 100%`), a left vignette (`linear-gradient(77deg, rgba(0,0,0,.72), rgba(0,0,0,.45) 42%, transparent 78%)`) and a bottom fade to black; a giant numeral `1` in 700 weight, no fill, a 2.5px stroke in `rgba(255,255,255,.16)`, at the right. 44px 48px 28px padding. Text white with a 0–2px shadow.
- **TOP 10 badge**: a 28px red `#e50914` square, 2px radius: `TOP` 7px / 700 over `10` 14px / 900, white. Small: 20px. It marks a show that is in this week's Top 10, and the billboard's #1 line. Decorative (`aria-hidden`); the words beside it carry the meaning.
- **Rating box**: 1px `rgba(255,255,255,.4)` border, 0 6px, 12px / 500 (`ALL`, `8+`, `13+`, `18+`; Korean `전체`). **Status tag** (the billboard's `Final`): 36px, a 3px `#dcdcdc` left bar on `rgba(51,51,51,.6)`, flush with the right edge.
- **Buttons** (measured): 4px radius. Red `#e50914` with white text: 32px, 14px / 500, padding 4px 16px in the header; 40px, 16px / 500, padding 6px 16px for the billboard and calls to action, with a chevron (hover `#c11119`). Gray: `rgba(128,128,128,.4)`, white 16px / 500, 40px, an outlined info icon; hover at .6. Outlined: `rgba(0,0,0,.4)` with a 1px `#808080` border, white text, the border white on hover. Small: 28px, 13px. netflix.com's hero button is 56px with 24px / 500; a dashboard never needs that size.
- **Chips** (the city filter): 32px, 16px radius, 1px `#808080` border on `rgba(0,0,0,.4)`, white 14px / 500; the selected chip white with black text. `role="tablist"`, arrow keys move. The EN/KO toggle is two 26px cells in one outlined box, the selected one white.
- **Key figure**: on the billboard, a tile of `rgba(0,0,0,.45)` with a 1px `rgba(128,128,128,.4)` border and an 8px radius, 14px 16px 12px padding: label 14px / 500 text-2 → value → change line (14px text-2, the change in 700 status color, then `vs last week`). The four share a subgrid so their values line up.
- **Top 10** (Figure 1): two columns of five, ranks running down each column, no rules. Each row: the numeral in a 76px column (700 weight, filled `#414141`, a 4px white stroke, a soft black glow, 58px tall, right-aligned, as on netflix.com's Trending Now), then the title (16px / 500, ellipsis) with a red `NEW` badge in its first week and the tickets in full digits on the right (16px / 700, unit 12px text-2); under it a 6px bar of tickets against #1 on a `rgba(255,255,255,.08)` track, `#f0313b` for #1 and `#595959` for the rest; then a meta line (13px text-2, parts joined by `•` in `#646464`): the move since last week (`▲3` in good, `▼2` in bad, `Same` in muted, `Back` for a return; a new entry shows the badge instead), the genre, the cities, and `N weeks in Top 10` (or `First week in Top 10` in red text). Hover or focus turns the row `#262626` and opens the hover card. Netflix's posters are not drawn: without real key art they would be empty boxes, so the row carries data in their place.
- **Weeks in the Top 10** (Figure 3): one row per show of this week's Top 10 (`1  Neon Harbor World Tour`, 13px, the current and the previous leader in white bold), one square per week (2px radius, 3px apart): red with a black digit for #1, `#333333` with a light digit for #2–10, an outline for weeks out of the Top 10; the count on the right (`12 wk`, white bold when it is all 12). Week ticks above, the current week in ink.
- **Episode list** (Figure 4): rows of 10px padding with `#404040` rules: the index (22px / 500 text-2), a 16:9 thumbnail in the show's tile colors with the weekday (11px uppercase) and date (19px / 900) at the top and the **progress bar** at the bottom (4px, track `rgba(255,255,255,.28)`, fill red for the rows the title names and `#b3b3b3` for the rest, 10px from the edges); then the title (16px / 700) with a small TOP 10 badge, the state on the right (`Sold out` or `97% sold`, 15px / 700 white) and a line of details (14px text-2: city · time · runtime · seats left). The hovered or focused row turns `#333333`.
- **Table** (the weekly Top 10 page, measured): 16px white, rows 56px, cells 8px 10px, no rules between rows; header 14px / 500 white in sentence case (`Ranking`, `Weeks in Top 10`, `Runtime`). The first column is the rank as `01` in 36px / 900 white; the show in 400 white after a 64px 16:9 thumbnail in its poster colors, with a red `NEW` badge in its first week; numbers centred with tabular figures; `vs last week` in good or bad; seats filled as a 96px progress bar and the value (red and red text when ≥ 95%); runtime `h:mm`; the rating box. It shows the Top 10 first; a **show-all button** below (36px, a 2px `rgba(255,255,255,.5)` border on `#2a2a2a`, an 18px radius, a chevron that turns, centred on a `#404040` rule) lists every show.
- **Hover card** (tooltip): `#232323`, 6px radius, padding 10px 12px 11px, shadow `0 3px 10px rgba(0,0,0,.75)`: a 14px / 700 title; for a show, a meta line (the share of seats, in green 700 when it is 90% or more and white otherwise, the way Netflix shows a match score; the rating box; the runtime) and a line of genre and cities joined by `•` in `#646464`; then rows of key (square, or a line, dashed for the comparison), value 700 white, label text-2. It takes the first side that fits inside the card: above, left, right, below.
- **FAQ accordion** (the method, measured): full-width rows 8px apart, `#2d2d2d`, no radius, 24px padding, the question 24px / 400 white and a 28px plus that turns into a cross; the answer below in the same gray, 1px apart, 18px. One open at a time; the first is open. Hover `#414141`.
- **Step cards** (`How it's built`): netflix.com's feature cards, measured: `linear-gradient(149deg, #192247 0%, #210e17 96.86%)`, 16px radius, 24px 16px padding; a 40px outlined number, a 20px / 500 title and 14px text-2.
- **Toast**: white, black 14px / 500 text, 4px radius, bottom centre, 2.2s.
- **Workbench window**: `#161616`, 8px radius. A 240px package panel on `#101010` (file names in mono 12px with a one-line description, install commands in `#2d2d2d` boxes with a copy button), the figure pane (outlined pills `Without a spec / With DASHBOARD.md`, a chip `city = all` in mono on `#2d2d2d`, title, plot, note, then **Checks · DASHBOARD.md**), and the code pane on `#0b0b0b` (tabs `Prompt · plan.md · figure-2.js · Tableau · Power BI` with a red underline, a copy button and a red `Run again`, line-numbered code, a red caret while typing, a status bar). Syntax: comment `#808080`, string `#46d369`, number `#e87c03`, keyword `#8ea5f6`, function `#ff5a63`, property `#e5e5e5` 500.
- **Footer**: black, 13px text-2, a `#232323` hairline above; the catalog line in white, the series in 12px / 700 with 0.08em tracking.


## Charts

- **Choose by the question.** Netflix ranks before it plots; start with its parts and draw a chart only where they cannot answer.
  - What sold most this week → the Top 10: outlined numerals beside each title, a bar against #1 (red only for #1), the move since last week and weeks in the Top 10 (Figure 1).
  - A trend against last year → a line with last year dashed gray and both line ends labeled (Figure 2).
  - How long the leaders have stayed → weeks in the Top 10 as a grid of ranks, #1 in red (Figure 3).
  - Progress toward a whole (seats sold, a target) → the continue-watching progress bar under a thumbnail in an episode list, red only for the rows the title names (Figure 4).
  - Composition over time → 100% stacked bars per week, the subject at the bottom, value labels beside the last bar (Figure 5).
  - Many entities and their measures → the Top 10 table: rank, name, weeks in the Top 10, value in full digits, change, a progress bar, runtime, rating; Top 10 first, then show all (Table 1).
- **Titles.** The card title is the finding (`Neon Harbor World Tour has been #1 for 3 weeks in a row, after The Paper Moon Hotel`), recomputed when the filter changes. The subtitle names the measure and period; the note explains the method and the source.
- **Marks.** Lines 2.5px for the subject, 2px for the comparison; a hollow end marker on the subject. Bars up to 24px wide, rounded 2px at the top, 2px gaps between stacked segments. Progress bars 4px, square ends. Rank squares with a 2px radius.
- **Axes.** Solid `#2d2d2d` gridlines on rows only, a `#414141` baseline, no vertical axis line; ticks 12px muted, four or five nice ticks; the current week in ink.
- **Labels.** Line ends carry `Name value` instead of a legend; values beside bars 12px / 700 in the series' text step; labels over marks have a card-colored halo. Values sit beside titles and bars at rest; the hover card adds detail, never the only copy of a number.
- **Keys** only where labels cannot do the job, as a one-line row in the card head (a 12px square with a 2px radius, a line, a dashed line, an empty square).
- **One axis.** Never a dual axis.
- **Never:** pie, donut, 3D, gauges, gradients on data, smoothed lines, glow on data marks, the UI red on data, photos, posters or logos, green or orange as a series.
- Every chart has a hover card, keyboard control and a screen-reader table.


## Depth & Elevation

Flat and dark. Cards are set apart by a step of gray (`#000000` → `#161616`), never by borders or shadows, and never lift on hover. Shadows exist only on the hover card (`0 3px 10px rgba(0,0,0,.75)`) and the toast. The billboard gets its depth from its vignette and fade, not from a shadow.


## Interaction & Motion

- **Filter**: the chips scope everything; changing one rewrites the billboard (badge line, headline, lede, key figures), every card title and note, and redraws every view. The URL keeps the city.
- **Billboard buttons** jump to Figure 1 and to the method.
- **Hover** opens the hover card and shows a crosshair and a hollow dot, a `#262626` band behind a bar, a white outline on a tile or a rank square, or a `#333333` row; touch taps pick and a tap elsewhere clears.
- **Keyboard**: every chart, the Top 10 row and the episode list are focusable; arrow keys step (up and down move between shows in Figure 3), Home and End jump, Esc clears, and a live region reads the value. Chips and tabs move with arrow keys; the FAQ and the show-all button are buttons with `aria-expanded`.
- **Workbench**: the first time it scrolls into view, the code types itself (55ms a line, 380ms between steps) and each step draws its layer of Figure 2 (frame → comparison line → subject line → end labels → title and note) and ticks its checks. Hovering a line of code spotlights its layer; hovering the chart highlights its code. `Without a spec` shows a typical first draft and fails all six checks. Changing the filter rewrites the `city` value and flashes that line.
- `Copy as Markdown` copies the whole report as Markdown with a toast; `Export PDF` prints the dark page as it is.
- Motion: lines draw in 0.7s, bars and progress grow in 0.45–0.5s, Top 10 rows fade in 0.45s, one after another; labels fade in 0.3s; `cubic-bezier(.5,0,.1,1)`; controls change in 0.2s. `prefers-reduced-motion` turns all motion off and shows the workbench finished.


## Accessibility

- Text ≥ 4.5:1 on its surface: muted 4.6:1 and text-2 8.6:1 on the card; good 9.3:1, bad 6.3:1; red text 5.9:1, blue text 7.6:1; white on the red button and badges 4.8:1; code token colors ≥ 4.5:1 on `#0b0b0b`.
- Marks below 3:1 (Other 2.58:1, the rank cells, the progress track) always have a second cue: a gap, a digit, a label or a value beside them.
- Identity is never color alone: names at line ends, digits in rank cells, `Sold out` and `NEW` in words, dashes for comparisons, signs on every change.
- Focus ring white, 2px, 2px offset. Tab order: header → filter → billboard → sections in reading order.
- Real tables with `scope`; every chart has a hidden data table and an `aria-label` that says what it shows. The TOP 10 badge is decorative; the words beside it carry the meaning.


## Responsive Behavior

Each step keeps what the wider steps changed.

- ≥ 1360: as laid out above.
- 1200–1359: 24px padding, 14px gaps, 48px between sections; the billboard padded 40px 36px 24px; cards padded 18px 20px 16px; table cells 8px 8px; thumbnails 108px; the workbench lifts its package panel into one row above the figure and the code.
- 1024–1199: the same rows; key figure values 34px; code 12px with wrapped lines; the table drops Runtime.
- 900–1023: cards stack one per row; the billboard is one column with the four key figures in a row; the workbench is one column; the table drops Gross.
- 640–899: a 60px header without the report name, the period or `Export PDF`; the basis line leaves the filter row; key figures 2 × 2; the Top 10 row three across; step cards stack; the table drops Genre and vs last week.
- < 640: 16px padding, 12px gaps, 40px between sections; `Copy as Markdown` becomes an icon button; chips 13px; the billboard padded 64px 16px 16px with the numeral smaller; headline 27px, key figure values 28px, section titles 21px, card titles 17px; the Top 10 one column, without cities; the episode list drops its index; the table keeps rank (24px), Show (no thumbnail), Tickets and Seats filled (the value only); FAQ questions 18px.
- Embedded in a post (`?embed=1`): the footer hides and the page reports its height to the host page.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` (installed in `.claude/skills/dashboard-style/`; or copy the `colors` block from the front matter) and these fonts (the second for Korean).

<!--email_off-->

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;500&family=Roboto:wght@400;500;700;900&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
```

<!--/email_off-->

Set `<meta name="color-scheme" content="dark">` and give `html` and `body` the canvas color, so nothing flashes white. The outlined numerals are SVG text with `paint-order: stroke` (fill the card color, stroke `#595959`); squeeze `10` with `textLength` and `lengthAdjust="spacingAndGlyphs"`.

**Tableau.** Paste the `<color-palette>` elements of `netflix.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette runs red, blue, Other and the comparison gray; assign the subject first.
- Dashboard background `#000000`; each sheet in a container shaded `#161616` with 20/24px inner padding and no border. Worksheet shading `#161616`; all text white or `#b3b3b3`; tooltips `#232323`.
- The card head: a text object with the figure label (Tableau Book 9 bold, uppercase, `#b3b3b3`), the finding as the sheet title (bold, 13–14pt, white) and the measure as a subtitle line; the method in the caption, starting with `Note:`.
- Grid lines: rows only, solid, `#2d2d2d`; zero line `#414141`; no axis rulers; ticks Tableau Book 9 in `#808080`.
- Lines: subject size 3, comparison dashed. Stacked bars: Color → the categorical palette, Format → Borders → `#161616` separators.
- Top 10: a sheet of RANK(SUM(tickets)) ≤ 10 as text with big bold rank numbers beside a bar or shape; Tableau cannot outline text, so use the rank as `01` in white 900 weight and the value as a label. Weeks in the Top 10: a highlight table of show by week, red for rank 1, `#333333` for 2–10, the rank as the label.
- Progress: a Gantt bar or a bar on a dual-mark track (`#575757` behind), red only for the rows the title names.
- Formats `#,##0` (Top 10), `#,##0.0,K`, `$#,##0.00,,"M"`, `0.0%`, `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0.00"달러"` and `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Roboto is installed on every viewing machine and on the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json`. It sets the data colors (red, blue, then Other), the black page, `#161616` visuals without borders, axis and gridline colors and text classes. Install Roboto on authoring and viewing machines or accept Segoe UI.
- Title each visual with the finding; put the measure in the subtitle and the method in a text box starting with `Note:`.
- Gridlines solid `#2d2d2d`; data labels on the last point instead of a legend.
- Top 10: a table visual sorted by tickets with Top N = 10, the rank as a column in bold, data bars in `#f0313b` for seats filled; a new entry flagged in a text column, not by a row color.
- Key figures as cards on `#161616` without borders; change measures with conditional formatting in `#46d369` / `#e87c03` only, always with a sign.

**Chart libraries (D3, Observable Plot, Vega-Lite, matplotlib, Datawrapper).** Subject `#f0313b` (labels `#ff5a63`), second `#6a88f2` (`#8ea5f6`), Other `#595959`, comparison `#808080` dashed `6 4`, gridlines `#2d2d2d` on rows only, baseline `#414141`, ticks `#808080` at 12px, plot background `#161616`, bar ends rounded 2px. The sample's Figure 2 in five forms is in the workbench of the live sample; `tickets.csv` is its data.


## Do's and Don'ts

- Do open with a billboard: the #1 line with a TOP 10 badge, a headline that states the result, a short lede and four key figures. Don't lead with a chart or a dozen KPI tiles.
- Do rank with Netflix's own parts — the Top 10 row, weeks in the Top 10, the Top 10 table — and use progress bars for shares of a whole. Don't turn every card into a bar chart.
- Do put every view on the same `#161616` card with the same head and foot. Don't add borders, shadows or glow, and don't mix card colors.
- Do keep red for what the title names (the subject, the #1 cells, the sold-out rows) and everything else gray. Don't put the UI red `#e50914` on data, and don't let a card go mostly red.
- Do set titles in type on color-block tiles. Don't put photos, posters, logos or the N mark anywhere.
- Do write Top 10 values in full digits and runtimes as `h:mm`, as the weekly Top 10 does. Don't round a ranked list's values to K.
- Do title each card with its finding and explain the method in the note and the FAQ. Don't title a chart with its measure alone.
- Do label line ends and write values under tiles. Don't keep a legend that labels could replace or hide a number behind hover.
- Do keep seven views or fewer on one screen. Don't add a card only to show a token.


## Agent Prompt Guide

Install the style (`npx @vizney/styles@latest add netflix`, `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- netflix`, or unzip the package in the project root). Agents that read skills load `dashboard-style` on their own and work in one of three modes: **Build** (plan the views, then draw them to this file), **Restyle** (move an existing screen onto this file without changing its data) and **Review** (a table of rule, finding, severity and fix). For an agent without skills, start the prompt with `Read DASHBOARD.md and follow it exactly.` For example:

```
Read DASHBOARD.md and follow it exactly. Build our weekly ticket sales dashboard as one self-contained HTML file
with fictional data, in English and Korean (?lang=en|ko, English by default), on the dark page the spec describes.
Top: a black header with the period, the EN/KO toggle, an outlined Export PDF and a red Copy as Markdown; one row of
outlined city chips that scopes every card. Then a billboard: color-block key art with a giant outlined numeral, the
TOP 10 badge and "#1 this week · <show>", a headline that states the week's result, a two-sentence lede, a red and a
gray button, four key figures with changes vs last week.
This week: the Top 10 in two columns (outlined numerals, titles, full-digit values, bars against #1 with only #1 in red,
moves since last week, NEW badges); tickets by week against last year (dashed gray) beside weeks in the Top 10 as a grid of ranks, #1 in red.
Coming up: the performances selling fast as an episode list with progress bars under the thumbnails beside channel
shares as 100% stacked bars; a Top 10 table of every show with a show-all button.
Method and sources as a FAQ accordion. Every view on the same #161616 card: figure label, finding title, subtitle, keys,
view, "Note:". At most seven views per screen.
Use only the values in Data Colors, the formats in Numbers, Dates & Units and the components in Component Stylings.
Every chart needs a hover card, keyboard control and a screen-reader table.
```

Before it is done, the agent checks:
- [ ] The billboard states the result; the key figures carry signed changes colored good (`#46d369`) or bad (`#e87c03`).
- [ ] Every view sits on the same `#161616` card with no border or shadow; every card title states a finding; every note starts with `Note:`.
- [ ] Red `#f0313b` only for what each title names; others gray; comparison dashed `#808080`; the UI red `#e50914` only on buttons, badges and ribbons; no photo or logo.
- [ ] Rankings use the Top 10 parts (outlined numerals with bars and rank moves, the rank grid, the Top 10 table) with values in full digits; shares of a whole use progress bars.
- [ ] Gridlines on rows only; line ends labeled; keys only where labels cannot work; no dual axis, pie, donut, gauge or glow.
- [ ] Numbers, dates, runtimes and weeks follow the formats in both languages.
- [ ] Text ≥ 4.5:1 on its surface (muted only on `#161616` or darker); marks below 3:1 have a second cue.
- [ ] Every chart has a hover card, keyboard control and a data table; the filter changes every card; at most seven views per screen; nothing breaks at 390px.
