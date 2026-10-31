# Prompt pack — Anthropic style

Copy `DASHBOARD.md` (and `tokens.css`) into the root of your project, then use one of these. They are written for Claude Code, Cursor, Codex and similar coding agents; the Tableau and Power BI notes are for people. Prompt 5 reproduces one figure of the live sample from `orders.csv`, which makes a quick test of an agent or a tool.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a monthly operations dashboard for <company> as one self-contained HTML file
with fictional data, in English and Korean (?lang=en|ko, English by default).
Top: a header with the period pill, the language toggle, Read in PDF and Copy as markdown; one filter row of pills
(<regions or business units>) that scopes every figure, table and card, kept in the URL.
Then a mono eyebrow, a headline that states this month's result, a serif lede that names the drivers, a numbered section nav,
and four key figures 2 × 2 (label → value → signed change vs last year, colored by whether the change is good).
Then:
- a launch figure: tabs for three measures above a bordered paper panel, legend toggles, our company orange, our last year aqua,
  rivals gray with ink-outlined markers, cost per <unit> on a log axis, our points labeled, a centered caption that states the finding;
- beside it a benchmark table: ink rules, our column outlined in clay, the best per row on peach (ours) or gray (a rival),
  a detached "For reference" column for our last year, footnote markers;
- a carousel of <entity> cards (glyph, title, count, one sentence, a status line) with a 01 / 02 pager;
- a full-width research mat whose title states a finding, with two charts that share one y scale and a FIGURE caption;
- two research mats side by side (a dumbbell before/after per category, and a dot-unit chart of a survey scale);
- a workbench that shows one figure, its checks against DASHBOARD.md and the code that draws it;
- notes, related reports and the ink footer.
Use only the values in "Data Colors", the formats in "Numbers, Dates & Units", the parts in "Component Stylings" and the
breakpoints in "Responsive Behavior". Every chart needs a hover tooltip, keyboard control and a screen-reader table.
Before you finish, run the checklist at the end of "Agent Prompt Guide" and fix anything that fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 월간 운영 대시보드를 가상 데이터로 HTML 파일 하나에 만들어 줘.
한국어·영어를 한 파일에서 ?lang=ko|en으로 바꾸고 기본은 영어야.
맨 위에 기간 알약, 언어 토글, PDF로 읽기, 마크다운으로 복사가 있는 머리. 그 아래 <지역·사업부> 알약 필터 한 줄이
모든 그림·표·카드에 함께 적용되고 주소에도 남게 해 줘.
이어서 고정폭 눈썹, 이달 결과를 말하는 제목 한 문장, 원인을 말하는 세리프 리드, 번호 붙인 절 내비,
핵심 수치 4개(2×2, 지표명 → 값 → 전년 동월 대비 증감, 증감 색은 그 지표에 좋은 변화인지로).
그다음:
- 발표 그림: 지표 탭 세 개, 잉크 테두리 종이 패널, 범례 토글, 우리 회사 주황, 우리 지난해 청록, 경쟁사 회색(점에 잉크 테두리),
  <단위>당 비용은 로그 축, 우리 점에 이름, 프레임 아래 가운데 정렬 캡션으로 결과를 말하기;
- 옆에 비교표: 잉크 괘선, 우리 열은 클레이 테두리, 행마다 최고값은 피치(우리) 또는 회색(경쟁사), 떨어진 '참고' 열에 우리 지난해, 각주 번호;
- <단위> 카드 캐러셀(도형 아이콘, 제목, 개수, 한 문장, 상태 줄)과 01 / 02 페이저;
- 결과를 말하는 제목의 전폭 리서치 매트: 세로 눈금을 공유하는 두 차트와 '그림 2' 캡션;
- 나란한 리서치 매트 둘(유형별 전후 덤벨, 설문 척도의 점 단위 차트);
- 그림 하나와 DASHBOARD.md 점검 목록, 그 그림을 그리는 코드를 보여 주는 워크벤치;
- 주석, 관련 보고서, 잉크 바닥.
색은 "Data Colors" 값만, 숫자·날짜는 "Numbers, Dates & Units"(한국어는 억·만·건·원·%p), 부품은 "Component Stylings",
폭별 배치는 "Responsive Behavior"를 따라 줘. 모든 차트에 호버 툴팁, 키보드 조작, 스크린 리더용 표를 넣고,
끝내기 전에 "Agent Prompt Guide"의 점검 목록을 확인해서 안 맞는 건 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
- colors to the tokens: our series orange #eb6834, our last year aqua, rivals and benchmarks the two grays with ink-outlined
  markers, comparisons dashed #b0aea5; no clay, yellow or fourth hue on data;
- the top to a headline that states the result, a serif lede and four key figures with signed, good/bad-colored changes;
- charts to the brand's forms: a tabbed launch panel for measures across options, research mats for findings,
  a benchmark table with ink rules and a clay-outlined subject column;
- titles and captions so that each figure states its finding and its method;
- number formats to "Numbers, Dates & Units" (true minus, pts / %p, ₩ M K / 억 만 원).
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, legend that labels could replace, bold serif, clay or yellow
series, zebra stripes), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
severity (must fix / should fix / fine), and the fix.
Cover: headline states the result; key figures and change colors; the subject's color and the grays for rivals; the comparison line;
figure forms (launch panel, benchmark table, research mats); finding titles and method captions; labels instead of legends;
shared scales and no dual axis; table rules and the subject column; number and date formats in both languages;
contrast and second cues for light marks; tooltips, keyboard and data tables; density at 1440 × 900 and 390px.
```

## 5. Reproduce Figure 5 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 5 from orders.csv (columns: region, month, orders, orders_last_year;
"all" means the sum of the three regions) for region "all", as one HTML file with an SVG chart.
1. Frame: white plot, light grid #e8e6dc, four y ticks in compact units, five month ticks with the last month in ink.
2. Comparison first: orders_last_year as a dashed #b0aea5 line, 2px, dash 6 4.
3. The subject: orders as a solid #eb6834 line, 2.5px, a hollow marker on the last month.
4. Label both line ends with name and value ("This year 1.86M", "Last year 1.72M"); no legend.
5. Title with the finding ("Orders grew on last year in 11 of 12 months"); a note that starts with "Note:".
Add a hover tooltip, keyboard control and a screen-reader table, then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `anthropic.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. Assign the subject first so it takes orange; rivals take the two grays.
2. Dashboard background `#faf9f5`. A launch figure is a container with a 1px `#141413` border and 16px inner padding; swap its measures with a parameter or navigation buttons placed as text tabs above it.
3. Marks: Color → Effects → Border `#141413` on every marker; line size 3 in the launch figure, 2.5 elsewhere; Edit Axis → Logarithmic for cost.
4. Research figures: an outer container `#e7e7db` around an inner `#fbf9f5`, the finding as a centered bold title, the method in a caption that starts with the figure number. Step chart = running MIN over an attempt index plus a circle layer of every attempt; the target as a dotted reference line.
5. Comparison table: a text table with 1px ink borders, the best value per row highlighted `#ebc9b7` (ours) or `#d1cfc5` (a rival), a floating 3px `#d97757` border around our column.
6. Number formats: `₩#,##0` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0"원"` · `+0.0"%p";−0.0"%p"`.
7. Fonts: Tableau Book unless Inter and Source Serif 4 are installed on every viewing machine and on the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out on paper with a 1px ink border.
2. The first three data colors are the category hues (the subject first), then the two rival grays, then gray Other. Clay is not in the list on purpose.
3. Install Inter on authoring and viewing machines, or accept the Segoe UI fallback.
4. Markers on, with data labels on our points or on the last point; legends off when labels name the series; error bars from the analytics pane for intervals.
5. Key figures: cards with a `#d1cfc5` top border and no background; change measures with conditional formatting in `#4a7b00` / `#b0453b` only, always with a sign.
