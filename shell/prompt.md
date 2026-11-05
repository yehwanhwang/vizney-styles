# Prompt pack — Shell style

Install the style in your project first:

```
npx @vizney/styles@latest add shell
```

or run `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- shell`, or unzip `shell-dashboard-style.zip` in the project root. Agents that read skills then load `dashboard-style` by themselves; prompts 1–4 are the same three modes (build, restyle, review) written out, so they also work for agents without skills. Then use one of these. They are written for coding agents such as Claude Code, Cursor and Codex, and for BI agents that read the same folder; the Tableau and Power BI notes are for people. Prompt 5 reproduces Figure 2 of the live sample from `bridge.csv`, which makes a quick test of an agent or a tool.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a weekly <operations or results> report for <company> as one
self-contained HTML file with fictional data, in English and Korean (?lang=en|ko, English by default), on the white
page the spec describes.
Top: a white canopy band with "<Company> |" in red, the period and the report name, the EN/KO toggle, a dark Export PDF
and a yellow Copy as Markdown; a 6px #dd1d21 bar across the page; a menu of <regions, corridors or business units> as
the one filter for every view (the selected item bold with a 4px #ffc800 underline), kept in the URL.
Open with the price sign as a pillar of key figures: a #fbce07 head with the one big number, a 5px red bar, a #262626
zone with one row per <grade, product or line> (the value large and white, the change and a second figure small), and a
#595959 base band with the count and the time. Beside it: a kicker, the finding headline in one sentence, a lede, a 2px
yellow rule, five compare boxes (#f7f7f7, a 2px yellow bottom rule, the measure with its unit in parentheses, the figure,
the change against plan or target with ▲▼ in status color, "(Wk 43: x)"), and three small key markers (lines, the subject
red, the comparison gray, the current week shaded #f2f2f2). The two columns end on one line.
Sections open like results slides: a kicker with the number in red, the heading, a 2px yellow rule. Then a bridge from
plan to actual (gray totals cut at a break, increases #008443, decreases #e03a35, negatives in parentheses, steps that
add up); ranked exception lists against a dashed threshold (rows past it red, the rest #a3a3a3); <a time profile> with
the busiest hours red; <a schematic map of sites with small price-sign pins and alert badges, and a zoom on the selected
site with what to do>; and a results table with group heads, the current week shaded and negatives in parentheses.
Every view on the same white panel (1px #e4e4e4): figure label → finding title → yellow rule → red chart title with the
unit → keys → view → a #f2f2f2 note band. At most seven views per section. Use only the values in "Data Colors", the
formats in "Numbers, Dates & Units" and the components in "Component Stylings". No photos, logos or shadows.
Every chart, list and map needs a tooltip, keyboard control and a screen-reader table; before you finish, run the
checklist in "Agent Prompt Guide" and fix what fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 주간 <운영·실적> 보고를 가상 데이터로 HTML 파일 하나에 만들어 줘.
명세가 말하는 흰 화면으로, 한국어·영어를 한 파일에서 ?lang=ko|en으로 바꾸고 기본은 영어야.
맨 위에 "<회사> |"를 빨강으로, 기간과 보고서 이름, EN/KO 토글, 어두운 PDF로 내보내기와 노란 마크다운으로 복사를 둔
흰 캐노피 띠를 두고, 그 아래 화면 폭 전체에 6px #dd1d21 막대, 그 아래 모든 그림에 함께 적용되고 주소에도 남는
<지역·구간·사업부> 메뉴(고른 항목은 굵게, 4px #ffc800 밑줄)를 둬.
첫 화면은 가격 기둥 모양의 핵심 지표: #fbce07 머리에 가장 중요한 숫자 하나, 5px 빨간 막대, <등급·제품·라인>마다
한 줄씩인 #262626 영역(큰 흰 값, 작은 증감과 둘째 숫자), 개수와 시각을 적은 #595959 바닥 띠. 그 옆에 작은 머리말,
결과를 말하는 한 문장, 리드, 2px 노란 선, 비교 상자 5개(#f7f7f7, 아래 2px 노란 선, 단위를 괄호에 넣은 지표명,
값, ▲▼와 상태 색으로 적은 계획·목표 대비, "(43주: x)"), 작은 선 그림 세 개(주인공 빨강, 비교 회색, 이번 주 칸
#f2f2f2). 두 단의 아래 끝을 맞춰 줘.
절은 실적 발표 슬라이드처럼 시작해: 번호를 빨강으로 쓴 머리말, 제목, 2px 노란 선. 그다음 계획에서 실적까지의
브리지(합계는 회색에 끊음 표시, 늘어남 #008443, 줄어듦 #e03a35, 음수는 괄호, 단계를 더하면 실적과 맞게), 점선
기준을 넘은 줄만 빨강인 예외 목록(나머지 #a3a3a3), 가장 붐빈 시간이 빨간 <시간 분포>, <사이트를 작은 가격 기둥
핀과 경고 배지로 세운 가상의 지도와, 고른 사이트를 확대해 할 일을 적은 칸>, 그룹 머리·이번 주 음영·괄호 음수가
있는 실적 표.
모든 그림은 같은 흰 패널(1px #e4e4e4)에: 그림 번호 → 결과를 말하는 제목 → 노란 선 → 단위를 붙인 빨간 차트 제목 →
범례 → 그림 → #f2f2f2 주석 띠. 한 절에 그림은 7개 이하. 색은 "Data Colors" 값만, 숫자·날짜는
"Numbers, Dates & Units"(한국어는 만·센트·%p, 돈은 회사의 통화), 부품은 "Component Stylings"를 따라 줘.
사진·로고·그림자는 넣지 마. 모든 차트·목록·지도에 툴팁, 키보드 조작, 스크린 리더용 표를 넣고, 끝내기 전에
"Agent Prompt Guide"의 점검 목록을 확인해서 안 맞는 건 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
- the frame to the forecourt and the results deck: a white canopy band with the company in red, a 6px #dd1d21 bar, a menu
  as the one filter with a 4px #ffc800 underline; sections that open with a kicker, the heading and a 2px #fbce07 rule;
- every view onto the same white panel (1px #e4e4e4, no radius, no shadow): a figure label, a title that states the
  finding, a yellow rule, a red chart title with the unit, keys, the view, and a #f2f2f2 note band;
- the headline KPIs to the price sign (yellow head, red bar, dark zone of rows, gray base band) and compare boxes
  (#f7f7f7 with a yellow bottom rule, the unit in parentheses, the change against plan, "(Wk 43: x)");
- variance explanations to a bridge with gray totals, green increases, red decreases and negatives in parentheses;
- colors to the tokens: the subject #e03a35 only where the title points, the rest #a3a3a3, comparisons #7b7b7b (dashed for
  plan); #dd1d21 and #fbce07 only on the frame;
- rankings to exception lists against a dashed threshold, and site maps to a schematic map with price-sign pins;
- gridlines #e4e4e4 on rows only, line ends labeled, the current period shaded #f2f2f2;
- number formats to "Numbers, Dates & Units" (true minus, pts / %p, ¢/gal, a tenth of a cent on pump prices,
  parentheses for negatives in tables).
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, donut or gauge, gradients, shadows or rounded cards,
photos, logos or real maps, the brand red or yellow on data, a card that is mostly red, cards side by side that end on
different lines, more than seven views in a section), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
severity (must fix / should fix / fine), and the fix.
Cover: the headline states the finding; the price sign and compare boxes with signed, good/bad-colored changes against
plan and last week in parentheses; one panel anatomy for every view (yellow rule, red chart title, note band); red only
where the title points and gray for the rest; no #dd1d21 or yellow on data; the bridge adds up with parentheses on
negatives; whether every device reads at least as well as a plain bar or table; plan and the exceptions shown, ranked
and tied to an action; the chart form for each question; row gridlines and labels instead of legends; no dual axis;
number, date, hour and money formats in both languages; contrast and second cues for light marks; tooltips, keyboard and
data tables; views per section; panels in a row ending on one line; density at 1440 × 810 and 390px.
```

## 5. Reproduce Figure 2 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 2 from bridge.csv (columns: corridor, week_ending, step, kind, usd;
corridor is "all", "i5", "i10" or "i95"; kind is "total" or "step") for "all", as one HTML file with an SVG chart on a
white panel (1px #e4e4e4, no radius) on a white page.
1. Frame: #e4e4e4 gridlines on rows only, the y axis in $ thousand from 1,080 to 1,110 with ticks every 10 in 12px
   #707070, the step names under the bars (Plan, Volume, Margin, Mix, Shop, EV, Actual).
2. Totals: Plan and Actual as #818181 bars cut at a white double break near the axis floor.
3. Steps: each floats from the running total, increases #008443, decreases #e03a35, in the file's order, with dotted 1px
   connectors at the running total.
4. Values: in $ thousand with one decimal, negatives in parentheses, rounded so the steps add up to Actual (1,099.5 →
   1,102.0), in #404040 above or below each bar.
5. Title with the finding ("Gross margin finished $2.5K above plan as a wider margin per gallon more than made up for
   lower fuel volume"), a yellow rule, the red chart title "Gross margin, plan to actual, week 44" with "$ thousand", and
   a note band that says the axis is cut at the break marks.
Add a tooltip (white, 1px #d9d9d9, 4px radius) with the exact step and the running total, keyboard control and a
screen-reader table, then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `shell.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. Assign the subject first so it takes red; the rest take the Other gray.
2. Dashboard background `#ffffff`. The header as a text object with the company in red `#dd1d21`; a 6px blank object filled `#dd1d21` across the dashboard; the filter as a single-value list. Section heads as text objects with a 2px `#fbce07` blank object under them. Each sheet sits in a container with a 1px `#e4e4e4` border and 16/20px inner padding.
3. Sheet title: the finding, bold, `#404040`; a subtitle line with the red chart title (`#dd1d21`, bold) and the unit in `#707070`; the note in a text object on `#f2f2f2`.
4. Price sign: a container with a `#fbce07` text object for the big number, a 5px red blank, a text table on a `#262626` worksheet with white text (write `$3.556`; Tableau cannot raise the tenth of a cent) and a `#595959` text object at the foot.
5. Compare boxes: text sheets on `#f7f7f7` with a 2px yellow blank under each; the change in `#007a3d` or `#c4161c` with ▲ or ▼; `(Wk 43: x)` in a small line.
6. Bridge: Gantt bars on `RUNNING_SUM(SUM([usd]))` with size `-SUM([usd])`, Color by kind (`#818181`, `#008443`, `#e03a35`); fix the axis start at the break and say so in the caption. Number format `#,##0.0;(#,##0.0)`.
7. Exception lists: bars sorted by value, a dashed `#bfbfbf` reference line at the threshold, Color by `past threshold` (`#e03a35` / `#a3a3a3`). The corridor map is easiest as a route list (sites in exit order, a bar from the plan line, shapes for alerts) with a parameter action that fills a detail sheet for the selected site.
8. Grid lines: rows only, `#e4e4e4`; the current week as a reference band `#f2f2f2`; ticks `#707070`. Number formats `"$"#,##0.000` · `0.0"¢"` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0.000"달러"` · `0.0"센트"` · `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Jost is installed on every viewing machine and on the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out white with a 1px `#e4e4e4` border and no radius on a white page.
2. The first data color is red (the subject), then blue and ochre for rare second and third series, then the Other gray; the colors after it exist only because Power BI wants a longer list. The brand red `#dd1d21` and Shell yellow are not in the list on purpose.
3. Install Jost on authoring and viewing machines, or accept the Segoe UI fallback.
4. Title each visual with the finding and put the red chart title in the subtitle; gridlines `#e4e4e4`; data labels on the last point; legends off when labels name the series.
5. Price sign: a yellow card over a table visual with a `#262626` background and white text. Compare boxes: cards on `#f7f7f7`, change measures with conditional formatting in `#007a3d` / `#c4161c`, always with a sign. Bridge: the waterfall visual with increase `#008443`, decrease `#e03a35`, total `#818181`, labels in thousands with one decimal and negatives in parentheses. Exception lists: bar charts with a constant line at the threshold and conditional colors.
