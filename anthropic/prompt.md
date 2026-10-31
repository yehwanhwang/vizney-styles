# Prompt pack — Anthropic style

Put `DASHBOARD.md` (and `tokens.css`) in your project folder and add one line to your agent's instructions file (for example `CLAUDE.md`): `Build every dashboard to DASHBOARD.md and run its checks before you finish.` Then use one of these. They are written for coding agents such as Claude Code, Cursor and Codex, and for BI agents that read the same folder; the Tableau and Power BI notes are for people. Prompt 5 reproduces Figure 2 of the live sample from `orders.csv`, which makes a quick test of an agent or a tool.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a monthly operations dashboard for <company> as one self-contained HTML file
with fictional data, in English and Korean (?lang=en|ko, English by default).
Top: a header with the period pill, the EN/KO toggle, Read in PDF and Copy as markdown; one filter row of pills
(<regions or business units>) that scopes every card, kept in the URL.
Then a mono eyebrow, a headline that states this month's result, a serif lede that names the drivers, a section nav,
and four key figures 2 × 2 (label → value → signed change vs last year, colored by whether the change is good).
Sections with a numbered ink rule, each at most seven views, every view on the same card
(figure label → finding title → subtitle → keys → chart or table → "Note:"):
- 01 Overview: <quality> against cost by <tier>, tabs for three measures, on a log cost axis, beside a rivals table with our
  column tinted; <volume> by month against last year beside an <entity> table with bullets against the target.
- 02 Operations: a step chart of <attempts> beside two bars with 95% error bars on the same scale; a dumbbell of before and
  after per <category> beside a dot-unit chart of a survey scale.
Use only the values in "Data Colors", the formats in "Numbers, Dates & Units", the parts in "Component Stylings" and the
breakpoints in "Responsive Behavior". Every chart needs a hover tooltip, keyboard control and a screen-reader table.
Before you finish, run the checklist at the end of "Agent Prompt Guide" and fix anything that fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 월간 운영 대시보드를 가상 데이터로 HTML 파일 하나에 만들어 줘.
한국어·영어를 한 파일에서 ?lang=ko|en으로 바꾸고 기본은 영어야.
맨 위에 기간 알약, EN/KO 토글, PDF로 읽기, 마크다운으로 복사가 있는 머리. 그 아래 <지역·사업부> 알약 필터 한 줄이
모든 카드에 함께 적용되고 주소에도 남게 해 줘.
이어서 고정폭 눈썹, 이달 결과를 말하는 제목 한 문장, 원인을 말하는 세리프 리드, 절 내비,
핵심 수치 4개(2×2, 지표명 → 값 → 전년 동월 대비 증감, 증감 색은 그 지표에 좋은 변화인지로).
번호와 잉크 괘선으로 여는 절마다 그림은 7개 이하, 모든 그림은 같은 카드
(그림 번호 → 결과를 말하는 제목 → 부제 → 범례 → 그림이나 표 → "주:")에 넣어 줘:
- 01 개요: <등급>별 비용 대비 <품질>(지표 탭 셋, 로그 비용 축)과 우리 열을 칠한 경쟁사 비교표,
  월별 <물량>과 지난해 비교 선, 목표 대비 불릿이 있는 <단위> 표.
- 02 운영: <시도>의 계단선과 같은 눈금의 95% 구간 막대 둘, <유형>별 전후 덤벨과 설문 척도의 점 단위 차트.
색은 "Data Colors" 값만, 숫자·날짜는 "Numbers, Dates & Units"(한국어는 억·만·건·%p, 돈은 회사의 통화),
부품은 "Component Stylings", 폭별 배치는 "Responsive Behavior"를 따라 줘. 모든 차트에 호버 툴팁, 키보드 조작,
스크린 리더용 표를 넣고, 끝내기 전에 "Agent Prompt Guide"의 점검 목록을 확인해서 안 맞는 건 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
- every view onto the same card (#f5f4ed, 16px radius): figure label, a title that states the finding, a subtitle with the
  measure, keys only where labels cannot work, and a note that starts with "Note:";
- colors to the tokens: our series orange #eb6834, our last year aqua, rivals and benchmarks the two grays, comparisons
  dashed #b0aea5, a 1px #141413 outline on every filled mark; no clay, yellow or fourth hue on data;
- the top to a headline that states the result, a serif lede and four key figures with signed, good/bad-colored changes;
- each chart to the form "Charts" picks for its question; side-by-side charts on one scale;
- tables to light rules with our column tinted #f4e5d9 and the best value per row bold;
- number formats to "Numbers, Dates & Units" (true minus, pts / %p, $ M K / 만 건).
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, legend that labels could replace, bold serif, clay or yellow
series, zebra stripes, more than seven views on a screen), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
severity (must fix / should fix / fine), and the fix.
Cover: headline states the result; key figures and change colors; one card anatomy for every view; finding titles and
"Note:" notes; the subject's color, the grays for rivals and the ink outlines; the comparison line; the chart form for each
question; labels instead of legends; shared scales and no dual axis; table rules and the tinted subject column; number and
date formats in both languages; contrast and second cues for light marks; tooltips, keyboard and data tables; views per
screen; density at 1440 × 900 and 390px.
```

## 5. Reproduce Figure 2 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 2 from orders.csv (columns: region, month, orders, orders_last_year;
regions california, texas, washington; "all" means their sum) for region "all", as one HTML file with an SVG chart on a
#f5f4ed card.
1. Frame: light grid #dedcd1, four y ticks in compact units, an ink baseline, five month ticks with the last month in ink.
2. Comparison first: orders_last_year as a dashed #b0aea5 line, 2px, dash 6 4.
3. The subject: orders as a solid #eb6834 line, 2.5px, a hollow marker on the last month.
4. Label both line ends with name and value ("This year 1.86M", "Last year 1.72M"); no legend.
5. Title with the finding ("Orders grew on last year in 11 of 12 months"); a note that starts with "Note:".
Add a hover tooltip, keyboard control and a screen-reader table, then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `anthropic.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. Assign the subject first so it takes orange; rivals take the two grays.
2. Dashboard background `#faf9f5`. Each sheet sits in a container shaded `#f5f4ed` with 22/24px inner padding; worksheet shading `#f5f4ed`.
3. Sheet title: the finding, bold, ink; a subtitle line with the measure; the caption starts with `Note:`. A text object above holds the figure label in Tableau Book 9, uppercase, `#5e5d59`.
4. Marks: Color → Effects → Border `#141413` on every filled mark; line size 3 for the cost scatter, 2.5 elsewhere; Edit Axis → Logarithmic for cost. Gridlines `#dedcd1`, rows only.
5. Comparison table: row dividers `#dedcd1`, an ink header divider, our column shaded `#f4e5d9`, the best value bold and a rival's best shaded `#e9e6dc`.
6. Number formats: `$#,##0.00` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0.00"달러"` · `+0.0"%p";−0.0"%p"`.
7. Fonts: Tableau Book unless Inter and Source Serif 4 are installed on every viewing machine and on the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out on the card color without borders, on an ivory page.
2. The first three data colors are the category hues (the subject first), then the two rival grays, then gray Other. Clay is not in the list on purpose.
3. Install Inter on authoring and viewing machines, or accept the Segoe UI fallback.
4. Title each visual with the finding and put the measure in the subtitle; markers on, with data labels on the last point; legends off when labels name the series; error bars from the analytics pane for intervals.
5. Key figures: cards with a `#d1cfc5` top border and no background; change measures with conditional formatting in `#4a7b00` / `#b0453b` only, always with a sign.
