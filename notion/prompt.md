# Prompt pack — Notion style

Install the style in your project first:

```
npx @vizney/styles@latest add notion
```

or run `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- notion`, or unzip `notion-dashboard-style.zip` in the project root. Agents that read skills then load `dashboard-style` by themselves; prompts 1–4 are the same three modes (build, restyle, review) written out, so they also work for agents without skills. Then use one of these. They are written for coding agents such as Claude Code, Cursor and Codex, and for BI agents that read the same folder; the Tableau and Power BI notes are for people. Prompt 5 reproduces Figure 1 of the live sample from `sales.csv`, which makes a quick test of an agent or a tool.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a monthly operations dashboard for <company> as one self-contained HTML file
with fictional data, in English and Korean (?lang=en|ko, English by default).
Top: a header with the period pill, the EN/KO segmented control, Export PDF and Copy as Markdown; one segmented control of
<regions or business units> between two hairlines that scopes every card, kept in the URL.
Then the page head: a line icon, a bold title that states this month's result, three properties (Scope, Compared with,
Status as a status pill) and four number widgets 2 × 2 beside them (label → value → signed change vs last year, colored by
whether the change is good); under both, a gray callout that names the drivers, and a contents line.
Toggle headings open each section; at most seven views per screen; every view on the same white card with a hairline border
(figure label → finding title → subtitle → keys → view → "Note:"):
- Sales: <revenue> by month against last year (dashed gray) beside channel shares as 100% stacked bars; an <entity> database
  table with tags, a number bar against the target, a status pill and a calculation row, plus a Board view grouped by status.
- Operations: a month calendar of daily <volume> in Notion Calendar's style, values as text (the days the title names in
  blue), weekends shaded, and the month's events as all-day bars, some running several days, beside <volume> by hour in
  gray with the peak hour blue and Weekdays/Weekends view tabs; daily <service time>
  against a dashed target beside <items> against their goal ticks (blue when met, orange when missed).
Use only the values in "Data Colors" (the subject Notion blue #2783de, others gray, the button blue only on buttons), the formats in "Numbers, Dates &
Units", the components in "Component Stylings" and the breakpoints in "Responsive Behavior". Every chart needs a hover
tooltip, keyboard control and a screen-reader table.
Before you finish, run the checklist at the end of "Agent Prompt Guide" and fix anything that fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 월간 운영 대시보드를 가상 데이터로 HTML 파일 하나에 만들어 줘.
한국어·영어를 한 파일에서 ?lang=ko|en으로 바꾸고 기본은 영어야.
맨 위에 기간 알약, EN/KO 세그먼트, PDF로 내보내기, 마크다운으로 복사가 있는 머리. 그 아래 두 줄 괘선 사이에
<지역·사업부> 세그먼트 필터 하나가 모든 카드에 함께 적용되고 주소에도 남게 해 줘.
이어서 페이지 머리: 선 아이콘, 이달 결과를 말하는 굵은 제목, 속성 세 줄(범위, 비교 기준, 상태 알약), 그 옆에
숫자 위젯 4개(2×2, 지표명 → 값 → 전년 동월 대비 증감, 증감 색은 그 지표에 좋은 변화인지로). 그 아래 원인을 말하는
회색 콜아웃과 목차 한 줄.
절은 토글 제목으로 열고, 한 화면의 그림은 7개 이하, 모든 그림은 가는 테두리의 같은 흰 카드
(그림 번호 → 결과를 말하는 제목 → 부제 → 범례 → 그림이나 표 → "주:")에 넣어 줘:
- 매출: 월별 <매출>과 지난해(회색 점선) 비교 선, 채널 비중 100% 누적 막대, 태그·목표 대비 숫자 막대·상태 알약·계산 행이
  있는 <단위> 데이터베이스 표와 상태별 보드 보기.
- 운영: 노션 캘린더 월 보기처럼 값은 글자로만 적은 일별 <물량> 달력(제목이 말하는 날만 파랑 글자, 주말 열은 옅은
  회색, 여러 날에 걸친 일정을 포함한 행사는 종일 일정 막대), 회색 막대에 가장 붐비는 시간만 파랑인 시간대별 <물량>
  (평일·주말 보기 탭), 점선 목표가 있는 일별 <처리 시간>, 목표 눈금이 있는 <품목> 가로 막대(목표 달성은 파랑,
  미달은 주황).
색은 "Data Colors" 값만(주인공은 노션 파랑 #2783de, 나머지 회색, 단추 파랑 #0075de는 데이터에 쓰지 않음), 숫자·날짜는 "Numbers, Dates & Units"(한국어는
억·만·건·%p, 돈은 회사의 통화), 부품은 "Component Stylings", 폭별 배치는 "Responsive Behavior"를 따라 줘.
모든 차트에 호버 툴팁, 키보드 조작, 스크린 리더용 표를 넣고, 끝내기 전에 "Agent Prompt Guide"의 점검 목록을 확인해서
안 맞는 건 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
- every view onto the same white card (1px #e6e5e3 border, 12px radius, no shadow): figure label with a line icon, a title
  that states the finding, a subtitle with the measure, keys only where labels cannot work, and a note that starts with "Note:";
- the top to a page head: line icon, a title that states the result, three properties, four number widgets with signed,
  good/bad-colored changes, and a #f9f8f7 callout with the drivers;
- colors to the tokens: the subject #2783de everywhere, a second real category #dd5b00, the rest #c7c6c4 behind 2px white gaps,
  last year dashed #a39e98, targets dashed #191918; no button blue, fourth hue or tag color on data;
- each chart to the form "Charts" picks for its question; dotted #e6e5e3 gridlines on rows only; line ends labeled;
- tables to Notion's database grammar: #f0efed rules, 14px muted headers with property icons, tags and status pills from the
  tag table, number bars for targets, a calculation row;
- filters to one segmented control in a #f6f5f4 track above everything;
- number formats to "Numbers, Dates & Units" (true minus, pts / %p, $ M K / 만 건, m:ss / 분 초).
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie or donut, legend that labels could replace, button blue on
data, shadows or gray cards, zebra stripes, more than seven views on a screen), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
severity (must fix / should fix / fine), and the fix.
Cover: the title states the result; properties, callout and number widgets with change colors; one card anatomy for every
view; finding titles and "Note:" notes; the subject blue and gray for everyone else; no button blue on data; the comparison and
target lines; the chart form for each question; dotted row gridlines and labels instead of legends; no dual axis; tags and
status pills with labels; database table rules, header icons and the calculation row; number, date and duration formats in
both languages; contrast and second cues for light marks; tooltips, keyboard and data tables; views per screen; density at
1440 × 900 and 390px.
```

## 5. Reproduce Figure 1 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 1 from sales.csv (columns: region, month, net_sales,
net_sales_last_year; regions california, texas, washington; "all" means their sum) for region "all", as one HTML file with an
SVG chart on a white card (1px #e6e5e3 border, 12px radius).
1. Frame: dotted gridlines #e6e5e3 (dash 1 3) on rows only, a solid #e6e5e3 baseline, five y ticks in compact money
   ($1.4M … $2.2M) in 12px #78736f, five month ticks (Nov, Feb, May, Aug, Oct) with the last month in ink.
2. Comparison first: net_sales_last_year as a dashed #a39e98 line, 2px, dash 6 4.
3. The subject: net_sales as a solid #2783de line, 2.5px, a hollow marker on the last month.
4. Label both line ends with name and value ("This year $1.90M" in #1f6fc5, "Last year $1.77M" in ink, values in #615d59);
   no legend.
5. Title with the finding ("Net sales beat last year in all 12 months"); a note that starts with "Note:".
Add a hover tooltip (a white popover), keyboard control and a screen-reader table, then list which checks in
"Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `notion.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. Assign the subject first so it takes blue; a second real category takes orange and the rest take the Other gray.
2. Dashboard background `#ffffff`. Each sheet sits in a container with a 1px `#e6e5e3` border and 20/24px inner padding; worksheet shading white.
3. Sheet title: the finding, bold, ink `#191918`; a subtitle line with the measure; the caption starts with `Note:`. A text object above holds the figure label in Tableau Book 9, `#615d59`.
4. Grid lines: rows only, dotted, `#e6e5e3`; no axis ruler on the value axis; ticks `#78736f`. Last year as a dashed line in `#a39e98`; a target as a dashed ink reference line labeled `Target 4:00`.
5. Calendar: WEEKDAY by WEEK of the date, the value as a label (`#1f6fc5` bold for the days the title names, ink for the rest), weekend columns `#f9f9f8`; events as annotations or a Gantt sheet; stacked bars with white borders between segments.
6. Store table: row dividers `#f0efed`, the target as a blue bar in its own column with a reference line at 100%, status as a circle in the status dot colors next to its label.
7. Number formats: `$#,##0.00` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0.00"달러"` · `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Inter is installed on every viewing machine and on the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out white with a 1px `#e6e5e3` border and a 12px radius on a white page.
2. The first three data colors are blue (the subject), orange and green, then the Other gray; the colors after it exist only because Power BI wants a longer list. The button blue #0075de is not in the list on purpose.
3. Install Inter on authoring and viewing machines, or accept the Segoe UI fallback.
4. Title each visual with the finding and put the measure in the subtitle; gridlines dotted; data labels on the last point; legends off when labels name the series; a constant line for the target, dashed ink.
5. Key figures: cards with the hairline border and no fill; change measures with conditional formatting in `#14832b` / `#b01601` only, always with a sign. Tables: data bars in `#2783de` for the target column, `#b01601` text for missed times.
