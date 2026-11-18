# Prompt pack — LEGO® style

Install the style in your project first:

```
npx @vizney/styles@latest add lego
```

or run `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- lego`, or unzip `lego-dashboard-style.zip` in the project root. Agents that read skills then load `dashboard-style` by themselves; prompts 1–4 are the same three modes (build, restyle, review) written out for agents that do not. Replace the parts in `<angle brackets>`.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a <sales event plan, season plan or another retail report> for
<company> as one self-contained HTML file with fictional data, in English and Korean (?lang=en|ko, English by default),
on the white page the spec describes.
Header: a 56px #ffd502 band with the company and report name in ink and the EN/KO pill in white. Under it, a strip with
a yellow date badge and <the event dates>, and <channels, regions or categories> as #f2f2f2 pills (the one filter for
every card, the selected pill #2c2c2c with white text, kept in the URL).
Then the result in one sentence and four KPI boxes (white, 1px #d9d9d9, 8px corners) with 52px values and ▲ ▼ changes:
blue #1e5aa8 when good, red #bd0000 when bad; a cost that falls is written like a sale price with last year struck out;
a shortfall is a red #dd0000 badge.
First screen: Figure 1, brick towers on a grey 4px baseplate at 0: what each past period added as towers of grey
#a3a3a3 bricks of one unit, then this plan's drivers one brick each from where the last ended (shoppers #1e5aa8, offers
#e05a00, new products #f7c600 with a #b38f00 edge, a white dashed #e05a00 brick for what is taken off), and the plan as
a wide tower of clear bricks with a 2px #2c2c2c edge, its value in 30px under a yellow badge with the total. Beside it,
Figure 2: the offers as lego.com sale tags (yellow badge, red % OFF badge) with a flat brick of <effect per $1,000>,
one stud per <unit>, orange in the plan and grey dropped.
Below: <a histogram against thresholds as the gift ladder>, <a day × hour grid in five blues with the plan as numbered
yellow badges>, and a table of <products> with the box line (age | number | pieces), badge, price and coverage.
Every view in the same box: figure number, finding title, subtitle, keys, view, note. Bricks flat, 2px apart, flat
studs. Red only for sale badges and shortfalls. Use only the values in "Data Colors", the formats in "Numbers, Dates &
Units" and the components in "Component Stylings". No logo, minifigure, Cera Pro, photos, real sets, prices or gifts.
Every view needs a tooltip, keyboard control and a screen-reader table; before you finish, run the checklist in
"Agent Prompt Guide" and fix what fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 <판매 행사 기획, 시즌 계획 등 유통 보고서>를 가상 데이터로,
HTML 파일 하나에 한국어·영어(?lang=ko|en, 기본 영어)로 명세의 흰 페이지 위에 만들어 줘.
머리: 56px #ffd502 띠에 회사와 보고서 이름(잉크색), 오른쪽에 흰 EN/KO 알약. 그 아래 줄에 노란 기준일 배지와
<행사 날짜>, 오른쪽에 <채널·지역·분류> #f2f2f2 알약 필터(모든 카드에 적용, 고른 칸은 #2c2c2c에 흰 글자, 주소에 저장).
이어서 결과 한 문장과 KPI 상자 넷(흰 바탕, 1px #d9d9d9, 모서리 8px, 수치 52px, ▲ ▼ 증감: 좋으면 파랑 #1e5aa8,
나쁘면 빨강 #bd0000). 줄어든 비용은 할인가처럼 작년 값을 취소선으로, 부족은 빨간 #dd0000 배지로.
첫 화면: 그림 1 브릭 탑(0에 놓인 4px 회색 바닥판. 지난 기간마다 더 판 만큼을 한 단위의 회색 #a3a3a3 브릭 탑으로,
올해 계획은 요인마다 브릭 하나를 앞 브릭이 끝난 자리에서: 손님 #1e5aa8 · 혜택 #e05a00 · 신제품 #f7c600(테두리
#b38f00) · 빼는 몫은 흰 바탕 #e05a00 점선 브릭, 끝에 2px #2c2c2c 테두리의 넓은 투명 브릭 탑, 값은 30px, 그 위 노란
합계 배지). 옆에 그림 2: 혜택마다 lego.com 세일 태그(노란 배지, 빨간 % OFF 배지)와 <1천 달러당 효과>의 납작한 브릭,
<단위>마다 돌기 하나, 계획에 넣은 혜택은 주황 · 뺀 혜택은 회색.
아래: <금액 단계에 견준 히스토그램(사은품 사다리)>, <날 × 시간 칸을 파랑 다섯 단계로, 계획은 노란 번호 배지>,
<제품> 표(상자 정보 띠 연령 | 번호 | 부품, 배지, 가격, 채운 정도).
모든 카드는 같은 상자: 그림 번호, 결과 제목, 부제, 범례, 그림, 주. 브릭은 납작하게, 2px 간격, 납작한 돌기.
빨강은 세일 배지와 부족에만. "Data Colors"의 값, "Numbers, Dates & Units"의 표기(한국어 290만 · 1.49억 달러 · 9천),
"Component Stylings"의 부품만 써 줘. 로고·미니피겨·Cera Pro·사진·실제 세트·가격·사은품은 쓰지 마.
모든 그림에 툴팁, 키보드 조작, 화면 낭독기용 표를 넣고, 끝내기 전에 "Agent Prompt Guide"의 점검 목록을 확인해 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
white page and boxes with 1px #d9d9d9 lines and 8px corners, the 56px #ffd502 header band, #f2f2f2 filter pills with
the selected one #2c2c2c, Gantari (Noto Sans KR in Korean), KPI values in 52px.
Give each series a brick colour by its job (shoppers #1e5aa8, offers #e05a00, products #f7c600 with a #b38f00 edge,
past or other #a3a3a3) and keep it on every chart. Turn totals that are built from parts into brick towers and bridges
(each part a flat brick from where the last ended, a dashed brick for what is taken off, the result as clear bricks
with an ink edge). Use the lego.com badge and price formats for offers and prices. Red only for sale badges and
shortfalls. Keep every number; rewrite titles as findings.
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, donut, gradients, bevelled bricks, colour by rank),
replace that view with the one the spec names for its question in "Charts".
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
pass or fail, the fix.
Cover: titles state findings; KPI changes carry ▲ ▼ and blue for good, red for bad; each brick colour has one job;
brick towers start at a baseplate at 0 and every brick starts where the last ended; bricks are flat with 2px gaps and
flat studs; offers carry lego.com badges; red appears only on sale badges and shortfalls; yellow marks have an edge or
a value; text ≥ 4.5:1; every view has a tooltip, keyboard control and a data table; nothing overlaps at 390px; no logo,
Cera Pro, minifigure, photo, real set, price or gift. Then list the fixes in order of how much they change the reading.
```

## 5. Reproduce Figure 1 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 1 from event.csv (columns: channel, order, bar, kind, group,
k_sets, added_k_sets, running_start; kind is event, driver or plan; group is past, demand, offer, sets or plan;
added_k_sets is the change over the year before for events and the driver's effect for drivers; running_start is where
a driver's brick starts) for all channels (add online and stores), as one HTML file with an SVG chart on a white box
with a 1px #d9d9d9 line and 8px corners.
1. Frame: a 4px #c9c9c9 baseplate at 0, row gridlines #ececec with signed ticks (+200K), columns for 2023–2025, the six
   drivers in order and the plan 1.8 columns wide.
2. Bricks: past events as towers of #a3a3a3 bricks, 100K a brick; each driver one brick from running_start
   (demand #1e5aa8, offer #e05a00, sets #f7c600 with a 1px #b38f00 edge); the plan as clear bricks with a 2px #2c2c2c edge.
3. Bricks 2px apart with 2px corners and two flat studs on top (four on the plan); the negative driver (fewer
   discounts) as a white brick with a 2px #e05a00 dashed edge and its value under it; #8a8a8a dashed connectors.
4. A signed value on every column (drivers 14.5px/800), the plan's value in 30px/800 under a #ffd502 badge "2.90M in total".
5. Title with the finding ("The plan adds 420K sets, 2.5 times last year's 170K; gifts add the most"), the subtitle
   "Sets added at each event over the year before, and what builds this year's plan" and a note on the brick unit.
Add a tooltip (white, 1px #bdbdbd, 8px corners) with the online and store split, keyboard control and a screen-reader
table, then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `lego.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette is shoppers, offers, sets, then grey; the sequential palette is the five blues.
2. Dashboard background `#ffffff`; a `#ffd502` text object as the header; each sheet on white with a 1px `#d9d9d9` border, row gridlines `#ececec`, text `#3d3d3d`, headers `#636363`. Each sheet's title is the finding.
3. Brick towers: Gantt bars from `event.csv` (start `running_start`, size `added_k_sets`, colour `group`); past events and the plan from 0; white 2px reference lines every 100K for the brick gaps; the plan with no fill and a 2px `#2c2c2c` border.
4. Sale tags: a horizontal bar per offer, coloured in the plan / dropped, with the badge text as the row label. Gift ladder: a histogram with $10 bins coloured by the step reached and reference lines at the steps. Hours: a highlight table on the blue palette.
5. Formats: `0.00,,"M"` and `+0,"K";−0,"K"` for sets, `$0.00` for prices, `0.0%` for shares; Korean workbooks `0,"만"`. Fonts: Tableau Book unless Gantari is installed on every viewing machine and the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out white with a 1px `#d9d9d9` border and 8px corners.
2. The first data colours are shoppers, offers and sets, then grey; good and bad changes in conditional formatting, always with ▲ ▼.
3. Install Gantari on authoring and viewing machines, or accept the Segoe UI fallback.
4. Brick towers: a waterfall chart (category `bar`, Y `added_k_sets`) beside a column chart of past events in `#a3a3a3`; the total as a white column with an ink border. Studs are not available; leave them out.
5. Sale tags: a bar chart with conditional colour and data labels, badges as a text column with a conditional background. Gift ladder: columns by $10 bin with conditional colour and constant lines at the steps. Hours: a matrix with conditional backgrounds on the five blues.
