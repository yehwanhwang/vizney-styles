# Prompt pack — Singapore Airlines style

Install the style in your project first:

```
npx @vizney/styles@latest add singapore-airlines
```

or run `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- singapore-airlines`, or unzip `singapore-airlines-dashboard-style.zip` in the project root. Agents that read skills then load `dashboard-style` by themselves; prompts 1–4 are the same three modes (build, restyle, review) written out, so they also work for agents without skills. Then use one of these. They are written for coding agents such as Claude Code, Cursor and Codex, and for BI agents that read the same folder; the Tableau and Power BI notes are for people. Prompt 5 reproduces the load factor by month from the live sample's build section, using `monthly.csv`, which makes a quick test of an agent or a tool.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a monthly <operating or service> report for <company> as one
self-contained HTML file with fictional data, in English and Korean (?lang=en|ko, English by default), on the #fafafa
page the spec describes.
Top: a white header with the report name, the period, the EN/KO pill, an outlined Export PDF and a navy Copy as
Markdown; a navy #00266b tab bar of <regions, networks or business units> as the one filter for every view, kept in the
URL; the chosen tab white with a 16px top-left corner, joined to a white panel with 16px bottom corners.
In the panel: one sentence in the form of a monthly release ("Traffic rose X% year-on-year on Y% more capacity, and the
load factor came in at Z%, n pts above plan.") with a 3px #ff9f00 bar to its left, a lead, and the key figures as a
boarding pass: a navy band, a FROM → TO line, five fields (label, value, change against plan or target, change against
last year), <a daily measure> by day against its daily average where the barcode sits, and a navy stub with the main
rate, its chips, the year by month against plan and the margin over <breakeven or a floor>.
Then sections with display titles beside a 3px orange bar: <capacity by class or zone> as a seat map; <where capacity
went> as a route map with the routes that grew in teal; <units> ranked against breakeven, lowest first, below it in red;
<departures or jobs> by hour, late in red, the busy bank shaded; the operating statistics table (navy head, group bands,
a sign column, n.m., a total row under a navy rule).
Every view on the same white card (1px #e5e9f0, 4px radius): figure label → finding title → subtitle → keys → view →
"Note 1:". At most seven views per section. Use only the values in "Data Colors" (the subject #0096ae, the rest gray, red
#dc0202 only for what fell short), the formats in "Numbers, Dates & Units" and the components in "Component Stylings".
No photos, logos, aircraft drawings or shadows. Every chart and list needs a tooltip, keyboard control and a
screen-reader table. Before you finish, run the checklist at the end of "Agent Prompt Guide" and fix anything that fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 월간 <운항·서비스> 보고를 가상 데이터로 HTML 파일 하나에 만들어 줘.
명세가 말하는 #fafafa 화면으로, 한국어·영어를 한 파일에서 ?lang=ko|en으로 바꾸고 기본은 영어야.
맨 위에 보고서 이름·기간·EN/KO 알약·테두리만 있는 PDF로 내보내기·남색 마크다운으로 복사가 있는 흰 머리, 그 아래
모든 그림에 함께 적용되고 주소에도 남는 <지역·노선망·사업부> 남색 #00266b 탭 띠를 둬. 고른 탭은 왼쪽 위만 16px로
둥근 흰 탭이고, 아래 모서리가 16px로 둥근 흰 판에 이어져.
판 안에는 월간 보도자료 같은 첫 문장("여객 수송은 지난해보다 X% 늘었고 공급은 Y% 늘었으며, 탑승률은 계획보다
n%p 높은 Z%였습니다")과 왼쪽의 3px #ff9f00 막대, 첫 단락, 그리고 탑승권 모양의 핵심 숫자: 남색 띠, FROM → TO 줄,
필드 다섯(이름, 값, 계획·목표 대비, 지난해 대비), 바코드 자리에 하루 평균 대비 날짜별 <하루 단위 지표>, 그리고
대표 비율·칩·계획 대비 올해 월별 값·<손익분기 같은 기준선> 대비 여유를 담은 남색 쪽지.
그다음 주황 3px 막대를 단 절 제목 아래: <등급·구역별 공급>은 좌석 배치도로, <공급이 어디로 갔는지>는 늘린 노선만
청록인 노선도로, <단위>는 손익분기 대비 낮은 순으로(미달은 빨강), <출발·작업>은 시간대별로(지연은 빨강, 붐비는
시간대는 음영), 운항 통계표(남색 머리, 묶음 띠, 부호 칸, n.m., 남색 선 아래 합계 줄).
모든 그림은 같은 흰 카드(1px #e5e9f0, 모서리 4px)에: 그림 번호 → 결과를 말하는 제목 → 부제 → 범례 → 그림 → "주 1:".
한 절에 그림은 7개 이하. 색은 "Data Colors" 값만(주인공 #0096ae, 나머지 회색, 빨강 #dc0202는 못 미친 것에만),
숫자·날짜는 "Numbers, Dates & Units"(한국어는 만·억·%p, 돈은 회사의 통화), 부품은 "Component Stylings"를 따라 줘.
사진·로고·항공기 그림·그림자는 넣지 마. 모든 차트와 목록에 툴팁, 키보드 조작, 스크린 리더용 표를 넣고, 끝내기 전에
"Agent Prompt Guide"의 점검 목록을 확인해서 안 맞는 건 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
- the frame to singaporeair.com's: a #fafafa page, a white header, a navy #00266b tab bar as the one filter with the
  chosen tab joined to a white panel; section titles in the display face at 24px/400 navy beside a 3px #ff9f00 bar;
- every view onto the same white card (1px #e5e9f0, 4px radius, no shadow): a gold caps figure label, a title that states
  the finding, a subtitle with the measure, keys only where labels cannot work, and a note that starts with "Note 1:";
- the KPIs to a boarding pass (a navy band, a FROM → TO line, five fields with plan or target and last year, a daily strip
  around the average where the barcode sits, a navy stub with the main rate and its year by month);
- detail tables to the operating statistics table: a navy head with units in parentheses, group bands on #e5e9f0,
  a separate sign column, n.m. where there is no last year, a total row under a 2px navy rule, values that add up;
- colors to the tokens: the subject #0096ae only where the title points, the rest #afafaf, plan dashed #868ba0, last year
  #c4c9d4, shortfalls #dc0202; navy only on frames, orange only as hairlines, cabin colours only on a seat map;
- rankings against a threshold to a board with bars from the threshold line, lowest first;
- no gridlines, the unit above the axis, a #a6b4cd base line, line ends labeled;
- number formats to "Numbers, Dates & Units" (true minus, pts / %p, K / 만 for passengers, M / 억 for seat-km, FY2026/27).
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, donut or gauge, gradients, shadows, photos, logos or
aircraft drawings, navy or orange on data, a card that is mostly teal, cards side by side that end on different lines,
more than seven views in a section), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
severity (must fix / should fix / fine), and the fix.
Cover: the headline states the result as a monthly release; the boarding pass with plan or target and last year on every
field and signed, good/bad-colored changes (capacity neutral); one card anatomy for every view; finding titles and
"Note 1:" notes; teal only where the title points and gray for the rest; no navy, orange or cabin colours on data; red
only for what fell short; whether every device reads at least as well as a plain bar or table (the daily strip around its
average, the seat map with its cabin strip, labels on the routes that changed, a table that adds up); plan, target and
breakeven shown and the exceptions ranked; the chart form for each question; no gridlines, units above the axis and
labels instead of legends; no dual axis; number, date, time and money formats in both languages; contrast and second
cues for light marks; tooltips, keyboard and data tables; views per section; cards in a row ending on one line; density
at 1440 × 810 and 390px.
```

## 5. Reproduce the load factor by month

```
Read DASHBOARD.md and follow it exactly. Draw the load factor by month from monthly.csv (columns: region, month,
load_factor_pct, plan_pct, last_year_pct; region is "all", "americas", "europe", "eastasia", "swp" or "wasia"; months
2026-04 to 2026-10) for "all", as one HTML file with an SVG chart on a white card (1px #e5e9f0, 4px radius) on a #fafafa
page.
1. Frame: no gridlines; a #a6b4cd base line and ticks; "%" above the y axis in 11px/700 #222222; four y ticks in 12px
   #666666; month ticks Apr … Oct with Oct in bold.
2. Comparison first: last_year_pct as a solid #c4c9d4 line, 2px; plan_pct as a dashed #868ba0 line, 2px, dash 6 4.
3. The subject: load_factor_pct as a solid #0096ae line, 2.5px, a marker on the last month.
4. Label the line ends with name and value ("Actual 86.5%" with the name in #00788c, "Plan 85.7%" and "Last year 85.6%"
   in #222222 and #666666, 12px/700); no legend.
5. Title with the finding ("October flew 0.8 pts above plan, the fifth month in a row above it"), the subtitle
   "Passenger load factor by month, FY2026/27 to date, against plan and last year" and the note "Note 1: The financial
   year runs from 1 April to 31 March. Plan is the load factor budgeted before the year began."
Add a tooltip (white, 1px #c8d6f1, 4px radius, shadow 0 4px 12px rgba(0,38,107,.14)) that shows the three values and the
gap to plan in pts, keyboard control and a screen-reader table, then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `singapore-airlines.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. Assign the subject first so it takes teal; the rest take the Other gray.
2. Dashboard background `#fafafa`. The header in a white container; the region filter as a single-value list in a `#00266b` container with white text; section titles as text objects with a thin `#ff9f00` container to their left. Each sheet sits in a white container with a 1px `#e5e9f0` border and 18/22px inner padding; tooltips white with a `#c8d6f1` border.
3. Sheet title: the finding in `#00266b`; a subtitle line with the measure in `#666666`; the caption starts with `Note 1:`. A text object above holds the figure label in Tableau Book 9 bold, uppercase, `#946e31`.
4. Boarding pass: a horizontal container with a 1px `#c8d6f1` border — a navy text band, text sheets for the five fields (label 9pt caps `#666666`, value 24–28pt, changes in `#03760b` or `#dc0202` with ▲ or ▼), and a navy container for the stub (white text, the load factor at 36pt, a small line of the year by month in `#1aa5bd` against a dashed `#c3cbdb` plan). The daily strip: bars of the day minus the daily average, a zero line in `#222222`.
5. Seat map: a scaffold of one row per seat (cabin, row, letter, x, y) as square marks, Color by sold / empty and cabin; or bars of load factor by cabin when the map is not needed.
6. Route map: `MAKEPOINT` for the hub and destinations and `MAKELINE` for the routes (drawn as great circles), Size by departures a week, Color by `more than last year` (`#0096ae` / `#afafaf`), a light base map or a `#e5e9f0` washout.
7. Route board: bars of load factor minus breakeven, sorted ascending, a reference line at 0 in `#222222`, Color by `< 0` (`#dc0202` / `#afafaf`).
8. Grid lines: none; axis rulers `#a6b4cd`; ticks `#666666`; the unit as text above the axis. Plan as a dashed `#868ba0` line, last year `#c4c9d4`.
9. Number formats: `#,##0.0,"K"` · `#,##0.0,,"M"` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean workbooks `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Figtree is installed on every viewing machine and on the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out white with a 1px `#e5e9f0` border and a 4px radius on a `#fafafa` page.
2. The first data colors are teal (the subject), deep blue and bronze, then the Other gray; the colors after it exist only because Power BI wants a longer list. Navy `#00266b`, orange `#ff9f00` and the cabin colours are not in the list on purpose.
3. Install Figtree and Source Sans 3 on authoring and viewing machines, or accept the Segoe UI fallback.
4. Title each visual with the finding and put the measure in the subtitle; gridlines off; axis lines `#a6b4cd`; data labels on the last point; legends off when labels name the series.
5. Boarding pass: cards in a shape with a `#c8d6f1` border; the stub as a navy shape with white text; change measures with conditional formatting in `#03760b` / `#dc0202` only, always with a sign. Route board: a bar chart of load factor minus breakeven with a constant line at 0 and `#dc0202` below it.
6. Route map: the standard visuals cannot draw route lines; use the Azure Maps visual's path layer (preview) or a flow-map custom visual, or show departures a week against last year as bars. Seat map: a matrix of rows × seat letters with conditional background colours.
