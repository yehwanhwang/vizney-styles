---
name: Costco style
spec: dashboard.md/0.1
extends: DESIGN.md
number: 4
tagline: Warehouse, Receipt, No-Frills
tagline_ko: 창고형, 영수증, 꾸밈없음
source: https://www.costco.com, https://investor.costco.com, https://www.costco.co.kr
sample: https://styles.vizney.com/costco/
author: Vizney (https://www.vizney.com)
license: reference only — not an official design; trademarks belong to their owners
colors:
  canvas: "#ffffff"
  bar: "#fafafa"
  paper: "#ffffff"
  plot: "#ffffff"
  rule: "#eeeeee"
  hair: "#eeeeee"
  line: "#d9d9d9"
  edge: "#cccccc"
  sign: "#333333"
  band: "#333333"
  ink: "#333333"
  body: "#333333"
  text-2: "#5f5f5f"
  muted: "#707070"
  faint: "#909090"
  blue: "#005dab"
  blue-700: "#004c8a"
  blue-100: "#eff7fb"
  red: "#e51937"
  red-500: "#c13533"
  green: "#008000"
  green-700: "#0b6e22"
  caution: "#ca4d00"
data:
  categorical: ["#1a70c2", "#d42f37"]
  other: "#cccccc"
  comparison: "#909090"
  categorical_text: ["#004c8a", "#c13533"]
  sequential: ["#8eb6e5", "#5c96d7", "#2174c7", "#10599e", "#0a3e6f"]
  diverging: ["#9b1e22", "#d42f34", "#e9a29c", "#d9d9d9", "#8eb6e5", "#2174c7", "#0b569a"]
  good: "#0b6e22"
  bad: "#bc4700"
typography:
  sans: { en: "Barlow", ko: "Pretendard" }
  mono: "Overpass Mono"
radius: {sign: "2px", card: "0", button: "3px", tag: "3px 0 0 3px", tooltip: "3px", bar: "0"}
spacing: {page: "32px", gap: "16px", section: "40px", card: "18px 22px 16px", sign: "10px 14px 9px", coupon: "14px 18px 16px", band: "12px 16px 8px", receipt: "18px 20px 16px", footer: "24px 32px 36px"}
layout: {maxWidth: "1400px", columns: 12}
files: {tokens: tokens.json, css: tokens.css, tableau: costco.tps, powerbi: powerbi-theme.json, prompts: prompt.md, sample_data: comps.csv}
---

# Costco style — DASHBOARD.md

**Warehouse, Receipt, No-Frills** · 창고형, 영수증, 꾸밈없음

A dashboard design spec read from the public design of costco.com, its monthly sales releases and the places members meet the company: the warehouse price sign, the register receipt and the Warehouse Savings coupon book. Costco publishes almost no charts; it shows its numbers on signs, receipts, coupons and in release tables. This spec turns those into dashboard parts — price signs as key figures, the receipt as the department table (with barcode bars, and transactions by hour where the receipt prints its barcode), the coupon book as a figure — and adds a warehouse board against plan and the holiday buy stacked as pallet racks, all in one card and chart grammar on costco.com's blue bands, charcoal section bands and ruled grids. It then adds what a website spec leaves out and a dashboard needs: validated data colors, card anatomy, chart rules, number and date formats in English and Korean, density, filters, accessibility, and settings for Tableau, Power BI and the web. Add it to a project with one command (or the zip on the sample page), or hand it to whoever builds your dashboards. The live sample was built from it.

```
npx @vizney/styles@latest add costco
# or, without Node:
curl -fsSL https://styles.vizney.com/install.sh | sh -s -- costco
```

That puts `DASHBOARD.md` in the project root and the `dashboard-style` agent skill (build, restyle, review) in `.claude/skills/dashboard-style/`, together with `tokens.css`, `tokens.json`, `costco.tps`, `powerbi-theme.json` and `prompt.md`. Coding agents that read skills pick it up whenever a task touches a dashboard or a chart; any other agent can be told to follow `DASHBOARD.md`.

- Live sample: https://styles.vizney.com/costco/?lang=en (Korean `?lang=ko`; one region `&region=west`)
- Raw file for your project: https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main/costco/DASHBOARD.md
- Package: [costco-dashboard-style.zip](costco-dashboard-style.zip) (unzip in your project root) · the skill: [skill/SKILL.md](skill/SKILL.md)
- Files in this folder: [tokens.json](tokens.json) (the source of every value here), [tokens.css](tokens.css), [costco.tps](costco.tps) (Tableau), [powerbi-theme.json](powerbi-theme.json), [prompt.md](prompt.md), [comps.csv](comps.csv) (the data behind the sample's Figure 1)
- Catalog: VIZNEY STYLES · 04 · https://styles.vizney.com (Vizney Styles is a line of [Vizney](https://www.vizney.com))

Not an official Costco design, and not affiliated with or endorsed by Costco Wholesale. A reference style read from the publicly visible design of costco.com and its public touchpoints such as warehouse signs, receipts and printed coupons; it carries no logo, typeface, photo or data of theirs. The sample's company, Vizney Wholesale, and all its numbers are fictional. Trademarks belong to their owners.


## Visual Theme & Atmosphere

A warehouse that prints its numbers. The page is white under costco.com's frame: a blue promo band with the week and the coupon book's dates, a `#fafafa` header, the blue region band that is the filter, and a `#fafafa` status row that reports in green, where costco.com says which warehouse is open. The report opens like a monthly sales release — `Net sales of $51.46 million for the retail week ended November 1, 2026, an increase of 8.6 percent from $47.39 million last year.` — set in regular weight with only the money and the percent bold, the way a price is. Below it stand six price signs: white cards in a thin black frame, an item code at the top, the name in bold caps, the figure huge with `$` and decimals as superscripts, and a date code in the corner.

Three devices carry the report, and each is built to be read before it is admired. The **price sign** is the key figure. The **register receipt** is the department table: monospace lines with a barcode-striped bar for each department's sales, thousands of dollars that add up to the subtotal, `****  TOTAL`, the item count, and — where a receipt prints its barcode — transactions by hour as thin ink bars. The **coupon book** is the promotion figure: a charcoal band and a ruled grid of coupons with the channel line, the item number and limit, the green savings and a bar of redemptions against forecast. Around them sit standard views on plain white cards: comparable sales as lines (reported against `Adjusted*`), a warehouse board ranked against plan, and the holiday buy stacked as pallets on racks.

No frills: no shadows, no rounded cards, no gradients, no photos. Section bands are charcoal `#333333` with white 22px/700 headings, like the coupon page's categories; blocks under them are ruled by 1px `#eeeeee`. One blue does the data's talking, gray does the rest, and orange flags what fell short. Every number answers a question someone acts on: against last year and against plan, the shortfalls ranked, the busy hours shown where the receipt's barcode sits.

Measured in a browser on November 4, 2026 (costco.com signed out, its Warehouse Savings page and warehouse locator, costco.co.kr, investor.costco.com): costco.com's MUI tokens are costco-blue `#005dab`, blue-700 `#004c8a`, blue-100 `#eff7fb`, the logo red `#e51937`, red-500 `#c13533`, green `#008000`, green-700 `#0b6e22`, caution `#ca4d00` and a gray ladder `#fafafa` `#eeeeee` `#d9d9d9` `#cccccc` `#909090` `#707070` `#5f5f5f` `#333333`; text `#333333` / `#5f5f5f` / `#707070`; spacing 4 · 8 · 12 · 16 · 24 · 32; radius 4px (shape) and 3px (buttons). The header is a 31px `#005dab` promo band (white 18px), a 138px `#fafafa` header, a 44px `#005dab` nav band (white 16px) and a `#fafafa` row that names the member's warehouse with an `Open until <time>` status in 12px `#008000`. The primary button is `#005dab` with white 16px/400, a 3px radius and 12px 16px padding. A product tile sets its price at 24px/700 with 14px/700 superscript `$` and cents; badges are 20px slanted tags (`clip-path: polygon(0 0, 100% 0, calc(100% - 12px) 100%, 0 100%)`). The Warehouse Savings page has 22px/700 white headings on `#333333` bands (12px 16px 4px, 50px tall), a grid of white cells ruled 1px `#eeeeee`, and coupons that read: the channel (`Warehouse` 16px/700 `#c13533` `&` `Online` `#005dab`, or an `Online Only` tag) → the item name 16px → `Item <7 digits>` and `Limit <n>.` in 12px `#707070` → the price in `#0b6e22` at 40px/700 with 18px superscripts → `After $<n> OFF`. The locator writes gas prices to a tenth of a cent with the last digit as a superscript. The monthly sales release writes one sentence of net sales and tables of comparable sales, with a second set `*Excluding the impacts from changes in gasoline prices and foreign exchange.`; there are no charts. On a warehouse price sign the item code sits at the top, a date code at the bottom right, and an asterisk marks an item that will not be restocked; at the exit the item count at the foot of the receipt is checked against the cart. Costco Sans has no Hangul, and costco.co.kr loads no Korean web font.


## Color Palette & Roles

Surfaces and text are costco.com's gray ladder; blue frames the page; the rules are the coupon page's.

| Token | Hex | Role |
|---|---|---|
| canvas | `#ffffff` | page background |
| bar | `#fafafa` | header, the status row, the footer, the workbench's package panel |
| paper · plot | `#ffffff` · `#ffffff` | price signs, cards, the receipt, coupon cells; a chart sits on its card |
| rule · hair | `#eeeeee` | the ruled grid between cells, rules between board rows, chart gridlines |
| line | `#d9d9d9` | the edge of a standalone card, the workbench window |
| edge | `#cccccc` | chart baselines, the tooltip border, the language toggle, the edge of an arriving pallet slot |
| sign · band · ink | `#333333` | the 1px frame of a price sign · section bands · titles, key figures and table values |
| text-2 | `#5f5f5f` | subtitles, the comparison words of a change, secondary values (6.4:1) |
| muted | `#707070` | figure labels, notes, axis ticks, item numbers, table headers (4.95:1) |
| faint | `#909090` | date codes, line numbers and the receipt's dashed rules only (3.2:1, never running text) |
| blue · blue-700 · blue-100 | `#005dab` · `#004c8a` · `#eff7fb` | the promo and region bands, buttons, links, focus, the `Online` channel word, slanted tags · button hover and the subject's text step · hovered rows and cells |
| red · red-500 | `#e51937` · `#c13533` | the logo red, only on a second kind of slanted tag · the `Warehouse` channel word |
| green · green-700 | `#008000` · `#0b6e22` | status text (`24 of 24 warehouses reporting`) · coupon savings (`$10 OFF`) and good changes |
| caution → bad | `#ca4d00` → `#bc4700` | costco.com's caution, darkened to 4.5:1 for text: bad changes, behind plan |

Rules:
- Cards are white with a 1px `#d9d9d9` edge, or cells of a ruled block (1px `#eeeeee`). No radius except the price sign's 2px and the buttons' 3px; no shadows except the tooltip and the toast.
- Blue `#005dab` is the frame (bands, buttons, links); data gets its own blue `#1a70c2`. The logo red `#e51937` is never data.
- Charcoal `#333333` is for section bands, the sign frame and ink; never fill a card with it.
- Green says that something is fine, in words (`reporting`, `ahead of plan`, `OFF`); orange says that something fell short. Neither is ever a series.


## Data Colors

Costco draws almost no charts — its sales releases are tables — so the data hues come from the pair costco.com uses to split its channels: `Warehouse` red and `Online` blue. Blue is the subject everywhere; red appears only beside blue, in the channel figure; everything else is gray. Every value passed an OKLab validator (color-vision-deficiency separation, normal-vision separation, contrast) on the card `#ffffff` and the header `#fafafa`. Use them exactly; do not generate tints.

| Role | Mark | Label text | Use |
|---|---|---|---|
| Subject | `#1a70c2` | `#004c8a` | what the title names: adjusted comparable sales, the department or coupon the title picks, the busiest day, sold pallets, Premium sign-ups, Online |
| Second category | `#d42f37` | `#c13533` | Warehouse, only beside Online in the channel figure |
| Other | `#cccccc` | text-2 | everything else; bars of warehouses ahead of plan; pallets in the warehouse |
| Comparison | `#909090`, dashed 2px (6 on, 4 off) | ink | reported comparable sales against adjusted; last year |
| Plan | `#333333`, solid 1px (the board) or 2px (the racks) | ink | the plan line; `PLAN 30%` |
| Behind plan | `#bc4700` | `#bc4700` | bars and values of warehouses behind plan; negative VS LY in the receipt |
| Receipt bar | stripes of `#333333`; the line the title names `#1a70c2` | — | department sales in the receipt |
| Arriving | `#ffffff` with a 1px `#cccccc` edge | — | pallet slots still to come |
| Sequential | `#8eb6e5` `#5c96d7` `#2174c7` `#10599e` `#0a3e6f` | ink on the two lightest, white on the rest | color by value |
| Diverging | `#9b1e22` `#d42f34` `#e9a29c` · `#d9d9d9` · `#8eb6e5` `#2174c7` `#0b569a` | each arm's darkest | above and below a midpoint |
| Status | good `#0b6e22`, bad `#bc4700`, neutral `#909090` | — | change text and status words only |

Validation (from `tokens.json`, light mode, on `#ffffff` and `#fafafa`):
- Blue `#1a70c2` and red `#d42f37`: CVD ΔE 21.4 (protan), normal vision 32.1, lightness inside 0.43–0.77, contrast 5.07 and 4.93:1 on white (4.86 and 4.72:1 on `#fafafa`). Blue sits one step lighter than the UI blue `#005dab`; red sits between the logo red `#e51937` and the error red `#c13533`.
- Other `#cccccc` is costco.com's gray-500, neutral by design (the lightness band and chroma floor do not apply). At 1.61:1 it always has a second cue: value labels, a 2px gap, a table.
- Comparison `#909090` (gray-600) is 3.19:1, always dashed and labeled at its end.
- The sequential ramp is one hue (spread 1°), monotone, every gap ≥ 0.06 in lightness, the light end 2.11:1. The diverging arms pass the ordinal checks (light ends 2.08 and 2.11:1); the poles are 19.5 (CVD) and 26.6 (normal vision) apart; the midpoint is gray-300.
- Text: blue labels `#004c8a` 8.75:1, red labels `#c13533` 5.49:1, good 6.43:1, bad 5.20:1 (4.98:1 on `#fafafa`).

Rules:
- Blue only for what the title names; the rest gray. A card that is mostly blue has highlighted nothing. The one exception is the holiday racks, where blue is the share sold in every rack — the measure the title talks about — beside gray stock and empty slots.
- Red belongs to the Warehouse channel, so a bad change is caution orange, never red.
- Status is never color alone: arrows, signs, the side of the plan line and the words `behind plan` carry it too.
- Never the UI blue `#005dab` or the logo red `#e51937` on data.


## Typography Rules

| Role | English | Korean | Weights |
|---|---|---|---|
| Sans (everything) | Barlow | Pretendard | 400, 500, 600, 700 |
| Mono (the receipt, codes) | Overpass Mono | Overpass Mono, then Pretendard for Hangul | 400, 500, 600 |

Barlow stands in for Costco Sans. Measured at 100px, Costco Sans has a 72 cap height, a 52 x-height and 540 for ten digits; among about fifty open sans faces Barlow came second by these proportions, and it is drawn from California road signs and plates, which suits warehouse signage. Overpass comes from Highway Gothic, the US highway sign face; it sets the receipt, item numbers, sign codes, date codes and code. costco.co.kr loads no Hangul web font, so Korean uses Pretendard. There is no serif.

| Element | Size / weight | Notes |
|---|---|---|
| Headline | `clamp(24px, 2.15vw, 30px)` / 400, line-height 1.28 | the sales-release sentence; only the money and the percent bold (700), like a price; Korean line-height 1.38 |
| Lede | 16px / 400, line-height 1.5, text-2 | figures in 600 ink |
| Report name · eyebrow | 28px / 400 · 12px / 700 uppercase, 0.1em, text-2 | costco.com's h1 (measured); the company name above it |
| Sign code · name | mono 11px / 500 muted · 15px / 700 uppercase, 0.02em | `101` · `NET SALES` (Korean 15px, no uppercase) |
| Sign value | 58px / 700, line-height 0.92, −0.015em, tabular | `$` and decimals at 0.42em as superscripts; the unit word under the decimals (11px / 700, 0.08em, uppercase: `MILLION`, `PER TRIP`) or after the number (13px / 700: `TRIPS`, `M GAL`); Korean 50px with the unit after it (`5,146만 달러`, `302,773건`) |
| Sign change · fine print | 13px text-2, the change in 700 status color · 12px, the key 11px / 700 uppercase muted, the date code mono 11px faint | |
| Section band | 22px / 700 white | the coupon page's category band (measured); Korean 21px |
| Figure label | 12px / 700 uppercase, 0.08em, muted | `FIGURE 1 · COMPARABLE SALES`, `TABLE 1 · DEPARTMENT LEDGER` (Korean 13px, no uppercase: `그림 1 · 기존점 매출`) |
| Card title · subtitle | 19px / 600, line-height 1.3 · 14px on 20px, text-2 | the finding; `text-wrap: balance` (Korean 18px on 1.42) |
| Receipt | mono 12.5px on 19px | caps; Korean department names in Pretendard 13px |
| Coupon | channel 14px / 700 uppercase · name 16px · item line 12px muted, the number in mono 11.5px · savings 40px / 700 `#0b6e22` with 18px `$` and `OFF` | |
| Board | rank mono 11.5px muted · code mono 13.5px / 600 · region 12.5px muted · values 12.5px / 600 | |
| Rack | name 14px / 700 uppercase, 0.04em · `27.4% sold` 17px / 700 `#004c8a` · status 13px / 600 | |
| Note · key | 12px on 18px muted · 13px / 500 ink | the note starts with `Note:` / `주:` |
| Axis ticks · value labels | 12px muted · 12px / 700 ink | |
| Fine print (method) | 12.5px, line-height 1.65 | the coupon book's terms |

Headlines are regular (400) with bold money, as costco.com sets its h1; card titles are semibold (600); sign names and figures are bold (700). Korean breaks between words (`word-break: keep-all`), and a number stays on the line with the particle after it.


## Numbers, Dates & Units

| | English | Korean |
|---|---|---|
| Net sales in the headline | `$51.46 million` | `5,146만 달러` |
| On a price sign | `$51.46 MILLION`, `$150.55 PER TRIP` (superscript `$` and decimals) | `5,146만 달러`, `150.55달러` |
| In the receipt | thousands of dollars: `3,720`, `51,464`; the header `$K` | the same digits; the header `천 달러` |
| Warehouses and plans | `$2.19M`, `PLAN $50.86M (+1.2%)` | `219만 달러`, `계획 5,086만 달러(+1.2%)` |
| Counts | `302,773 trips`, `3,096,130` items | `302,773건`; in sentences `30만 2,773번` |
| Members · gallons | `1.28 million` · `1.74 M gal` | `128.5만 명` · `174.1만 갤런` |
| Savings | `$721,748` in sentences, `$721,748.46` in the receipt | `72만 1,748달러`, `721,748.46` |
| Pump price | `$3.37⁸` (the tenth of a cent as a superscript, as on a gas sign) | `3.37⁸달러` |
| Coupon | `$10 OFF`, `Item 9310542 · Limit 10.` | `10 달러 할인`, `상품 번호 9310542 · 구매 한도 10개` |
| Rates · points | `6.2%` · `−0.1 pts`, `▲ 4.5 pts ahead of plan` | `6.2%` · `−0.1%p`, `▲ 계획보다 4.5%p 앞섬` |
| Change | `+8.6% from $47.39M last year` | `+8.6% 지난해 4,739만 달러 대비` |
| Dates | `11/01/26`, `10/26/26 – 11/01/26`, `Week ended 11/01/26`; axis `08/09` | `11/1(일)`, `10/26(월) ~ 11/1(일)`, `11/1(일) 마감 주`; axis `8/9` |
| Hours | `12 PM`, `9–10 AM` | `낮 12시`, `오전 9시~오전 10시` |
| Codes | sign codes `101`–`106`, date codes `11/01`, departments `01`–`14`, warehouses `W-04` | the same |
| Missing | `—` (no sales last year) | `—` |

- Money is in the company's currency; the sample's company is American, so US dollars. The item numbers, warehouse codes and prices in the sample are made up.
- Signs use the true minus (`−`, U+2212); one decimal for change.
- Change colors follow whether the move is good for that metric (a lower comparable-sales rate is orange).
- Units and suffixes are smaller than the digits.
- A table that is rounded still adds up: round each line to the unit, then hand the leftover units to the lines with the largest remainders (the receipt's `$K` lines sum to its subtotal, and subtotal plus gas to the total). The exact value is in the tooltip.
- Weeks run Monday to Sunday; the report is as of Sunday 11:59 PM and published Monday morning.


## Layout Principles

One column on a white page, at most 1400px wide, 32px side padding (24px up to 1359px, 16px below 640px), a 16px gap, 40px above each band. No sidebar, no logo, no photo.

1. **Promo band** (`#005dab`, 32px): `Week ended 11/01/26 · Warehouse Savings valid 10/26/26 – 11/22/26 · Week 1 of 4`, white 15px / 500, centered.
2. **Header** (`#fafafa`, 76px): the company eyebrow and the report name; on the right the period with a calendar icon, the EN/KO toggle, an outlined `Export PDF` and a blue `Copy as Markdown`.
3. **Region band** (`#005dab`, 44px): `All warehouses (24) · West (9) · Central (7) · East (8)`, the selected one bold with a 3px white underline; `vs the same week last year` on the right. It is the filter: it scopes every card, and the URL keeps it (`?region=west`).
4. **Status row** (`#fafafa`, 40px, 1px `#eeeeee` below): a green dot and `24 of 24 warehouses reporting`, gas stations, paid members, and `Data as of Sun 11/01/26, 11:59 PM PT` on the right.
5. **This week** (no band): the left 8 of 12 columns hold the headline, the lede, six price signs (3 × 2 on a subgrid), the asterisk footnote and Figure 1 comparable sales; the right 4 hold Table 1, the receipt. The two columns end on one line: the shorter one takes the extra height — Figure 1's plot, or the receipt's hourly barcode up to 124px, with any rest above the barcode.
6. **Warehouses and holiday stock** (a band): Table 2 the warehouse board (two columns) and Figure 2 the holiday buy (four racks), stacked in a ruled block.
7. **Warehouse Savings** (a band with the book's dates, the week and the coupon count): Figure 3, eight coupons in a 4 × 2 ruled grid.
8. **Channels, members and gas** (a band): Figure 4 channels · Figure 5 new members · Figure 6 gas by day, three cells in a ruled row.
9. **How it's built** (a band): a paragraph with two buttons, three ruled steps, the workbench window and a caption.
10. **Method and sources** (a band): fine print in two columns, like the coupon book's terms.
11. **Footer** (`#fafafa`): the catalog line, the sample note, the notice and the way back.

At most seven views in one band, and every view a standard form an agent or a BI tool can rebuild. Density: at 1440 × 810 the frame, the headline, all six price signs and the top half of the receipt are on the first screen. Reading order follows the list; never lead with a chart.


## Component Stylings

- **Card**: white, 1px `#d9d9d9`, no radius, no shadow, 18px 22px 16px. Head (figure label → title → subtitle → keys, 14px below), body, foot (`Note:` 12px muted, 12px above). Never a card inside a card. Inside a ruled block the card loses its edge and the 1px `#eeeeee` rules take over.
- **Price sign** (key figure): white, a 1px `#333333` frame, 2px radius, 10px 14px 9px, 12px apart. Five rows on a subgrid so the values line up: the code (mono 11px muted) → the name (15px / 700 caps) → the value (58px / 700 with superscripts) → the change (`▲ +8.6%` in good or `▼ −0.1 pts` in bad, 700, then the comparison words in text-2) → a fine-print line above a 1px `#eeeeee` rule, with a key (11px / 700 caps muted) and a value (600 ink) — `PLAN $50.86M (+1.2%)`, `REPORTED 6.2%`, `PER WAREHOUSE A DAY 1,802`, `ITEMS PER TRIP 10.2`, `RENEWAL RATE 88.3%`, `PUMP PRICE $3.37⁸` — and the date code `11/01` at the right in mono faint. An asterisk in a name points to the footnote under the signs.
- **Receipt** (Table 1): a card padded 18px 20px 16px in Overpass Mono 12.5px on 19px. A dashed `#909090` rule, then two centered caps lines (`ALL WAREHOUSES · 24 WAREHOUSES`, `WEEK ENDED 11/01/26 · RPT 044`). Columns `DEPT` (4.4ch) · `DESCRIPTION` (17ch, receipt abbreviations: `MEAT/SEAFOOD`, `HOME/SEASONAL`) · `SALES` (the bar) · `$K` (6.6ch, right) · `VS LY%` (7ch, right); headers 11.5px muted. Each department line carries a **barcode bar**: 11px tall, its length the line's net sales against the largest line, filled with vertical stripes of uneven width — a 38px pattern, about 63% ink, widths 3 · 1 · 1 · 1 · 2 · 1 · 4 · 1 · 1 · 1 · 2 · 2 · 1 · 1 · 3 · 1 · 2 · 1 · 1 · 1 · 3 · 1 · 1 · 2 px, ink first — and a solid 2px end, so the length reads exactly. Ink `#333333`; the line the title names in `#1a70c2`, its text in `#004c8a` / 600. Negative VS LY in `#bc4700` / 600. A blank line, `SUBTOTAL` and `GAS STATION` (600) and `****  TOTAL` (700), all in `$K` that add up. After a dashed rule: `TOTAL NUMBER OF ITEMS SOLD = 3,096,130` (700), `INSTANT SAVINGS`, `TRANSACTIONS`, `AVERAGE TICKET`. After another dashed rule, where a receipt prints its barcode: `TRANSACTIONS BY HOUR` with `PEAK SAT 12 PM · 10,538` (600) on the right, then one ink bar per open hour (Mon–Fri 10 AM–9 PM, Sat 9 AM–6 PM, Sun 10 AM–6 PM), each about 62% of its slot and at most 4px wide, a 9px gap between days, heights from zero, the day names under them (mono 10.5px muted); then the code line (`11/01/26 23:59  W-ALL 24  RPT 044`, 11.5px muted, centered). A line turns `#eff7fb` on hover and shows a tooltip: net sales in full dollars, last year, vs last year, the share of merchandise, items sold.
- **Section band**: `#333333`, at least 50px, 12px 16px 8px; a 22px / 700 white heading on the left and a 14px `#e6e6e6` line on the right (bold parts white). The blocks under it are ruled: 1px `#eeeeee` outside and between cells, no top edge.
- **Coupon** (Figure 3): cells 14px 18px 16px in a 4-column ruled grid, the best coupon first. The channel line (`WAREHOUSE` `#c13533` `&` `ONLINE` `#005dab`, 14px / 700 caps; `WAREHOUSE ONLY`; or the slanted `Online Only` tag); a 24px asterisk at the top right for a seasonal item that will not be restocked; the item 16px; `Item 9310542 · Limit 10.` 12px muted; the savings in `#0b6e22` (`$` 18px, the amount 40px / 700, `OFF` 18px); a 10px bar of redemptions against forecast on a `#eeeeee` track — the coupon the title names in blue, the rest `#cccccc`, a 2px ink forecast tick that overhangs 3px, bars stopping at 250%; `11,731 redeemed` and `188% of forecast` (13px; the title's coupon in `#004c8a`); `Member savings $117,310` (12px muted). A hovered cell turns `#eff7fb`.
- **Slanted tag** (measured): 20px, 12px / 600 white on `#005dab` (or `#e51937` for a second kind), padding 0 16px 0 5px, `clip-path: polygon(0 0, 100% 0, calc(100% - 12px) 100%, 0 100%)`, radius 3px 0 0 3px. Small (18px, 11px) for `New` on the warehouse board.
- **Warehouse board** (Table 2), from the warehouse locator's numbered list: two columns of equal length, ranked best first, 40px apart. Columns: the rank (mono 11.5px muted, `01`), the warehouse (the code in mono 13.5px / 600, the region in 12.5px muted in the all-regions view, a small `New` tag), `VS PLAN` (the bar), `NET SALES` (`$2.19M`, 600, right) and `VS LY` (13px text-2; `—` for a new warehouse). The header is 11px / 700 caps muted over a 1px `#d9d9d9` rule, with ticks `−4%` `PLAN` `+4%` `+8%`; rows are 29px with 1px `#eeeeee` rules. The bar is 12px tall and starts at the plan line (1px ink through every row): to the right in `#cccccc` when ahead, to the left in `#bc4700` when behind, its value (12.5px / 600) beyond its end and orange when behind. The scale runs from −6% to +10% of plan, with room for labels on both sides. The title counts the warehouses behind plan and names the furthest.
- **Pallet rack** (Figure 2): four racks in a row (two on narrower screens), 30px apart. Each: the category in 14px / 700 caps and `2,560 pallets` (12.5px muted); a grid of 20 bays × 5 levels with 2px gaps and square slots, filled bay by bay from the left and from the floor up — sold `#1a70c2`, in the warehouse `#cccccc`, arriving white with a 1px `#cccccc` edge; one slot is 1% of the category's pallets, rounded so the three parts make 100; a 2px ink floor line; the plan-to-date line, 2px ink at a bay boundary, overhanging 6px above and 5px below, labeled `PLAN 30%` (mono 10.5px / 600) above it. Under the rack: `27.4% sold` (17px / 700 `#004c8a`) and `▼ 2.6 pts behind plan` (13px / 600 in bad; `▲ … ahead of plan` in good; `On plan` in text-2), then `1,460 in the warehouse · 398 arriving` (12.5px muted). Plans to date are multiples of 5% so the line falls between bays. A hovered rack turns `#eff7fb`.
- **Buttons** (measured): 40px, 3px radius, 15px / 500, 0 16px. Blue `#005dab` with white text (hover `#004c8a`); outlined white with a 1px `#005dab` border and blue text (hover `#eff7fb`). Small: 32px, 14px.
- **Region band tabs**: 16px white with 14px side padding, the count 14px at 0.85 opacity; the selected tab bold with a 3px white underline; `role="tablist"`, arrow keys move. The EN/KO toggle is a 40px box with a 1px `#cccccc` edge and two 32px cells, the selected one blue with white text.
- **Status row**: 13px; `24 of 24 warehouses reporting` in `#008000` / 500 after an 8px green dot; keys 12px muted, values bold.
- **Tooltip**: white, 1px `#cccccc`, 3px radius, 9px 12px 10px, costco.com's shadow `0 0 5px rgba(0,0,0,.3)`: a 13px / 700 head, an optional 12px muted line, then rows of key (a 9px square, a 14px line, dashed for the comparison, or an outlined square), value 700 ink and label text-2. It takes the first side that fits inside its card: above, left, right, below.
- **Toast**: `#333333` with white 14px / 500, 3px radius, bottom centre, 2.2s.
- **Workbench window**: 1px `#d9d9d9`, white. A 240px package panel on `#fafafa` (file names in mono 12px, blue links, install commands in white boxes with a copy button), the figure pane (the `Without a spec / With DASHBOARD.md` toggle in a 3px box with the selected cell blue, a chip `region = all` in mono, the title, the plot, the note, then **Checks · DASHBOARD.md**), and the code pane on white (tabs `Prompt · plan.md · figure-1.js · Tableau · Power BI` with a 3px blue underline, a copy button and a blue `Run again`, line-numbered code, a blue caret while typing, a status bar). Syntax: comment `#707070`, string `#0b6e22`, number `#bc4700`, keyword `#004c8a`, function `#c13533`, property `#333333` 500.
- **Fine print** (Method and sources): 12.5px, line-height 1.65, in two columns; terms bold; the sources line in text-2.
- **Footer**: `#fafafa`, a 1px `#eeeeee` rule above, 13px text-2; the catalog line in 600 ink, the series in 12px / 700 with 0.08em tracking.


## Charts

- **Choose by the question.** Costco shows its numbers on signs, receipts and coupons; start with those parts and draw a chart only where they cannot answer.
  - How did the week do → the sales-release headline and six price signs, each with its comparison (last year, the week before, plan).
  - A rate against its own history → lines, the subject solid blue and the comparison dashed gray, both ends labeled (Figure 1, Figure 4).
  - Where the money came from, by department → the receipt: `$K` lines with barcode bars, VS LY beside them, totals that add up (Table 1).
  - When the members came → the receipt's barcode: transactions by hour, one bar an hour, a gap between days (Table 1).
  - Who hit plan → the warehouse board: a ranked list with bars from the plan line, the shortfalls in orange (Table 2).
  - How fast a stock sells against plan → pallet racks: 100 slots per category, sold / in the warehouse / arriving, the plan-to-date line (Figure 2).
  - Which promotions worked → the coupon grid with redemptions against forecast (Figure 3).
  - Composition over time → stacked bars, the subject at the bottom, a 2px gap (Figure 5).
  - One measure by day → bars, the day the title names in blue, values on top (Figure 6).
- **Titles.** The card title is the finding (`Electronics grew the most, up 14.7%; food court was the only department down`; `7 of 24 warehouses finished behind plan; E-03 missed it by the most, 4.1%`), recomputed when the filter changes. The subtitle names the measure and the period; the note explains the method.
- **Marks.** Lines 2.5px for the subject and 2px for the comparison, with a hollow end marker. Bars up to 22px wide (44px for seven days), square ends, 2px gaps between stacked segments. Board bars 12px, coupon bars 10px, receipt bars 11px; rack slots square with 2px gaps.
- **Axes.** `#eeeeee` gridlines on rows only, a `#cccccc` baseline, no vertical axis line; ticks 12px muted, four to six nice ticks; dates `08/09`, the last one in ink.
- **Labels.** Line ends carry `Name value` (the name in the series' text step, the value in ink) instead of a legend; values above bars 12px / 700, the bar the title names in ink and the rest in 500 text-2. The tooltip adds detail; it is never the only copy of a number.
- **Keys** only where labels cannot do the job, as one row in the card head (a 14 × 10 square, a line, a dashed line, a tick, an outlined square).
- **Rounding.** Tables round to a readable unit and still add up; the exact value is in the tooltip.
- **One axis.** Never a dual axis.
- **Never:** pie, donut, 3D, gauges, gradients on data, smoothed lines, the UI blue or the logo red on data, photos, product shots or logos, decoration that carries no number.
- Every chart and list has a tooltip, keyboard control and a screen-reader table.


## Depth & Elevation

Flat and white. Cards are set apart by a 1px `#d9d9d9` edge or by the ruled grid, never by shadows, and never lift on hover. Shadows exist only on the tooltip and the toast (`0 0 5px rgba(0,0,0,.3)`, costco.com's). Bands are flat charcoal; the price sign's frame is a line, not a shadow.


## Interaction & Motion

- **Filter**: the region band scopes everything. Changing it rewrites the headline, the lede, the signs, every title and note, the receipt's header and code line, and redraws every view. The URL keeps the region.
- **Hover** shows a crosshair and hollow dots on lines, a blue-tinted band behind a bar or an hour, `#eff7fb` behind a receipt line, a board row, a coupon cell or a rack, and the tooltip; a tap picks on touch screens.
- **Keyboard**: every chart, the receipt table, the hourly barcode, the board, the racks and the coupon grid are focusable; arrow keys step, Home and End jump, Esc clears, and a live region reads the value. Tabs move with arrow keys.
- **Workbench**: the first time it scrolls into view, the code types itself (55ms a line, 380ms between steps) and each step draws its layer of Figure 1 (frame → reported → adjusted → end labels → title and note) and ticks its checks. Hovering a line of code spotlights its layer; hovering the chart highlights its code. `Without a spec` shows a typical first draft and fails all six checks. Changing the region rewrites the `region` value and flashes that line.
- `Copy as Markdown` copies the whole report (the key figures, the receipt, the board, the racks, the coupons and the notes) with a toast; `Export PDF` prints the page.
- Motion: lines draw in 0.7s; bars, receipt bars and hours grow in 0.45–0.5s, one after another; board rows and sold slots fade in 0.3s; buttons change in 0.15s; `cubic-bezier(.4,0,.2,1)`. `prefers-reduced-motion` turns all motion off and shows the workbench finished.


## Accessibility

- Text ≥ 4.5:1: ink 12.6:1, text-2 6.4:1 and muted 4.95:1 on white; blue labels 8.75:1, red labels 5.49:1, good 6.43:1, bad 5.20:1; white on `#005dab` 6.7:1 and on `#333333` 12.6:1. Faint `#909090` only for date codes, line numbers and rules.
- Marks below 3:1 (Other `#cccccc` at 1.61:1, the arriving slots, the coupon track) always have a second cue: a value label, a gap, an edge or a table.
- Identity is never color alone: names at line ends, the side of the plan line and the sign, `behind plan` and `ahead of plan` in words, dashes for comparisons, `▲` / `▼` on every change.
- Focus ring 2px `#005dab` with a 2px offset (white inside the blue band).
- Real tables with `scope` (the receipt is a table); every chart has a hidden data table and an `aria-label` that says what it shows and how to move.


## Responsive Behavior

Each step keeps what the wider steps changed.

- ≥ 1360: as laid out above.
- 1024–1359: 24px padding, 14px gaps; sign values 50px (Korean 43px); the receipt 12px. The headline and the lede run across; below them the left 7 of 12 columns hold the price signs in two columns of three, the footnote and Figure 1, and the receipt takes the right 5, so it keeps room for its bars and both columns still end on one line. The workbench lifts its package panel into one row.
- 1024–1199: code 12px with wrapped lines; the racks two by two; the coupon grid keeps four columns.
- 900–1023: one column — the signs in three columns, Figure 1, then the receipt at most 620px wide; the channel row stacks; the coupons 2 × 4; the workbench in one column; the fine print in one column.
- 640–899: the header wraps; `Export PDF` and the band's right-hand line hide; the signs 2 × 3; the board in one column.
- < 640: 16px padding; the promo band shows two lines; sign values 34px (Korean 30px); the receipt 11px; the coupons and the racks in one column; the board drops the region and `VS LY` and keeps only `PLAN` in its header.
- Embedded in a post (`?embed=1`): the footer hides and the page reports its height to the host page.


## Tool Mapping

**Web and coding agents.** Load `tokens.css` (installed in `.claude/skills/dashboard-style/`; or copy the `colors` block from the front matter) and these fonts (the second for Korean).

<!--email_off-->

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=Overpass+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
```

<!--/email_off-->

The barcode bar is a `repeating-linear-gradient(90deg, …)` of the stripe widths above, with `box-shadow: inset -2px 0 0` for its solid end. The racks are a CSS grid (`grid-template-columns: repeat(20, 1fr)`, `grid-auto-flow: column`) whose slots are classed in fill order, so each bay fills from the floor. Superscripts are spans at 0.42em aligned to the top of the digits. Give a device's parts a prefix (`rc-`, `bd-`, `rk-`) so shared classes never leak into them.

**Tableau.** Paste the `<color-palette>` elements of `costco.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette runs blue, red, Other and the comparison gray; assign the subject first.
- Dashboard background `#ffffff`. The header in a `#fafafa` container; the region filter as a single-value list in a `#005dab` container with white text; section bands as text objects on `#333333` with white bold text.
- Each sheet in a container with a 1px `#d9d9d9` border and 18/22px inner padding; worksheet shading white; tooltips white with a `#cccccc` border.
- Price signs: text sheets in containers with a 1px `#333333` border — the code in Tableau Book 8 `#707070`, the name in bold caps, the value at 36–40pt bold (Tableau cannot raise the cents; write `$51.46M`), the change in `#0b6e22` or `#bc4700` with ▲ or ▼, the plan or the comparison in a small line under it.
- Receipt: a text table in a monospace font with Measure Names columns for `$K` and `VS LY%` (negatives in `#bc4700`), beside a thin bar sheet in `#333333` with the subject's row in `#1a70c2`. Tableau has no pattern fills, so the barcode bar becomes a plain bar; keep it thin and keep the totals in the table. Transactions by hour: a bar chart of hour inside day (both discrete), small bars in `#333333`, no axis, the peak as a label.
- Warehouse board: bars of `SUM([Net sales]) / SUM([Plan]) - 1`, sorted descending, a reference line at 0 in `#333333`, Color by `vs plan < 0` (`#bc4700` / `#cccccc`), labels at the bar ends; the code and region as row headers.
- Racks: one waffle per category from a 100-row scaffold (`X = INT((INDEX()-1)/5)`, `Y = (INDEX()-1) % 5`), Color by state (`#1a70c2`, `#cccccc`, white with a gray border as a square shape), a reference line at the plan's bay.
- Coupons: bars of redemptions over forecast with a reference line at 100%, the title's coupon in blue.
- Grid lines on rows only, solid `#eeeeee`; zero line `#cccccc`; ticks Tableau Book 9 in `#707070`.
- Formats: `$#,##0.00,,"M"` · `#,##0,` (thousands, for `$K`) · `#,##0` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0.00"달러"` and `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Barlow is installed on every viewing machine and on the server.

**Power BI.** View → Themes → Browse for themes → `powerbi-theme.json`. It sets the data colors (blue, red, then Other), the white page, white visuals with a 1px `#d9d9d9` border and no radius, axis and gridline colors and text classes. Install Barlow on authoring and viewing machines or accept Segoe UI.
- Title each visual with the finding; put the measure in the subtitle and the method in a text box that starts with `Note:`.
- Price signs: cards with a `#333333` border, the callout value 28–36pt bold, the change as a measure with conditional formatting in `#0b6e22` / `#bc4700`, always with a sign.
- Receipt: a table visual in a monospace font, `$K` with display units in thousands, data bars on the sales column in `#333333` (the stripes become a solid bar), VS LY with a conditional font color `#bc4700` below zero.
- Warehouse board: a bar chart of vs plan with an X-axis constant line at 0 and conditional colors (`#bc4700` below zero, `#cccccc` above).
- Racks: a matrix of 5 rows × 20 columns with conditional background colors, or a waffle custom visual; the plan as a constant line or a text marker.

**Chart libraries (D3, Observable Plot, Vega-Lite, matplotlib, Datawrapper).** Subject `#1a70c2` (labels `#004c8a`), second `#d42f37` (`#c13533`), Other `#cccccc`, comparison `#909090` dashed `6 4`, plan `#333333`, behind `#bc4700`, gridlines `#eeeeee` on rows only, baseline `#cccccc`, ticks `#707070` at 12px, plot background `#ffffff`, square bar ends. The sample's Figure 1 in five forms is in the workbench of the live sample; `comps.csv` is its data.


## Do's and Don'ts

- Do open with the sales-release sentence and six price signs, each with a comparison and a date code. Don't lead with a chart or a dozen KPI tiles.
- Do make every device readable first: round the receipt to `$K` so it adds up, put a bar beside every size that is compared, and turn ornaments into data (the receipt's barcode is transactions by hour). Don't print cents in a table of millions, and don't keep a device that reads worse than a plain bar or table.
- Do compare against plan as well as last year, rank the warehouses with the shortfalls in orange, and show stock as pallets against the plan to date. Don't report growth alone.
- Do frame the page with costco.com's blue bands and the coupon page's charcoal bands and ruled grids. Don't add shadows, gradients, rounded cards or photos.
- Do keep blue for what the title names and everything else gray; red only for the Warehouse channel beside Online. Don't put `#005dab` or the logo red on data, and don't color a bad change red.
- Do end cards in one row on one line. Don't stretch a chart to an odd height to get there; change the layout instead.
- Do title each card with its finding and explain the method in the note and the fine print. Don't title a chart with its measure alone.
- Do write money and dates the Costco way (`$3.37⁸`, `11/01/26`, `Item 9310542 · Limit 10.`). Don't use a real item number, warehouse number or price, or Costco's logo, wordmark or typeface.
- Do keep at most seven views in a band. Don't add a card only to show a token.


## Agent Prompt Guide

Install the style (`npx @vizney/styles@latest add costco`, `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- costco`, or unzip the package in the project root). Agents that read skills load `dashboard-style` on their own and work in one of three modes: **Build** (plan the views, then draw them to this file), **Restyle** (move an existing screen onto this file without changing its data) and **Review** (a table of rule, finding, severity and fix). For an agent without skills, start the prompt with `Read DASHBOARD.md and follow it exactly.` For example:

```
Read DASHBOARD.md and follow it exactly. Build our weekly warehouse report as one self-contained HTML file with
fictional data, in English and Korean (?lang=en|ko, English by default), on the white page the spec describes.
Top: a blue promo band with the week and the coupon book's dates; a #fafafa header with the report name, the period,
the EN/KO toggle, an outlined Export PDF and a blue Copy as Markdown; the blue region band as the filter for every view,
kept in the URL; a #fafafa status row with the reporting count in green.
This week: the sales-release headline ("Net sales of $X million for the retail week ended …, an increase of n percent
from $Y million last year"), a lede with comparable sales and the result against plan, and six price signs (code, caps
name, a big value with superscript $ and decimals, a signed change, a fine-print line, a date code); comparable sales as
lines (adjusted solid blue, reported dashed gray, ends labeled); beside them the department receipt: $K lines with
barcode bars and VS LY, SUBTOTAL, GAS STATION, **** TOTAL, the item count, and transactions by hour as its barcode.
The two columns end on one line.
Warehouses and holiday stock: a warehouse board ranked against plan (bars from the plan line, behind plan in orange,
two columns) and the holiday buy as pallet racks (20 × 5 slots per category: sold blue, in the warehouse gray, arriving
outlined, a plan-to-date line).
Warehouse Savings: eight coupons in a ruled grid with redemptions against forecast. Then channels, new members and gas
by day in a ruled row, and the method as fine print.
Every view on the same white card: figure label, finding title, subtitle, keys, view, "Note:". At most seven views per band.
Use only the values in Data Colors, the formats in Numbers, Dates & Units and the components in Component Stylings.
Every chart and list needs a tooltip, keyboard control and a screen-reader table.
```

Before it is done, the agent checks:
- [ ] The headline is the sales-release sentence; the six price signs carry signed changes colored good (`#0b6e22`) or bad (`#bc4700`), a fine-print line and a date code; net sales shows its plan.
- [ ] Every view sits on a white card (1px `#d9d9d9`) or in a ruled cell, with no shadow; every card title states a finding; every note starts with `Note:`.
- [ ] Blue `#1a70c2` only for what each title names and the rest gray; red only for Warehouse beside Online; behind plan and bad changes in `#bc4700`; no `#005dab` or logo red on data.
- [ ] The receipt reads at a glance: `$K` lines that add up to the subtotal, a barcode bar on every department, VS LY with negatives in orange, transactions by hour where the barcode sits.
- [ ] Plan appears where it matters (the lede, the net sales sign, the warehouse board, the racks), and the shortfalls are ranked and named.
- [ ] Gridlines on rows only; line ends labeled; no dual axis, pie, donut, gauge, gradient or photo.
- [ ] Numbers, dates, hours and money follow the formats in both languages.
- [ ] Cards side by side end on one line at 1440, 1280 and 1024px without a stretched chart; nothing breaks at 390px.
- [ ] Text ≥ 4.5:1; marks below 3:1 have a second cue; every view has a tooltip, keyboard control and a data table; the filter changes every card.
