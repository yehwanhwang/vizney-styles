# Prompt pack — Anthropic style

Copy `DASHBOARD.md` (and `tokens.css`) into the root of your project, then use one of these. They are written for Claude Code, Cursor, Codex and similar coding agents; the Tableau and Power BI notes are for people.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a monthly sales dashboard for <company> as one self-contained HTML file with fictional data,
laid out like a research post, not a KPI grid.
Top: a meta row (Published · Team · Period), then one run-in statement — a bold sans sentence with this month's revenue and its change
versus the same month last year, running into a serif sentence that names the driver and the return rate — then a section nav "(1) Revenue (2) Titles (3) <entities> (4) Returns".
Then: a Key findings card (three or four serif bullets beside hairline key–value rows: revenue, orders, return rate, <one metric of ours>),
Figure 1 (12-month revenue with the prior year as a dashed gray line; the title states the finding; the caption starts with "Note:")
beside Table 1 (top items with 1px ink rules, the current-month column tinted, group label rows, "—" for missing values),
one card per <entity> using the card anatomy (eyebrow → title → one sentence → key–value rows → full-width secondary button),
Figure 2 (a rate by <entity> over 12 months with the target as a dashed reference line) beside a Notes card (numbered method notes, sources, update time),
and the ink footer. One filter row of pills at the top applies to every figure, table and card.
Use only the colors in "Data Colors" (no clay on data), the formats in "Numbers, Dates & Units", the components in "Component Stylings"
and the breakpoints in "Responsive Behavior". Label line ends instead of legends. Every chart needs a hover tooltip, keyboard control and a screen-reader table.
Before you finish, check the list at the end of "Agent Prompt Guide" and fix anything that fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 월간 매출 대시보드를 가상 데이터로 HTML 파일 하나에 만들어 줘. KPI 격자가 아니라 리서치 글처럼 짜 줘.
한국어·영어를 한 파일에서 ?lang=ko|en으로 바꾸고 기본은 영어야.
맨 위에 메타 행(발행 · 팀 · 기간), 그다음 런인 문장 하나 — 이달 매출과 전년 동월 대비 증감을 산세리프 굵은 문장으로, 이어서 증가를 이끈 것과 반품률을 세리프 문장으로 — 그리고 절 내비 "(1) 매출 (2) 도서 (3) <단위> (4) 반품".
이어서 핵심 결과 카드(세리프 불릿 3~4개 옆에 헤어라인 키–값 행: 매출, 주문, 반품률, <우리 지표 하나>),
그림 1(전년을 회색 점선으로 둔 12개월 매출. 제목은 결과를 말하는 문장, 캡션은 "주:"로 시작) 옆에 표 1(상위 항목, 1px 잉크 괘선, 이달 열에 연한 바탕, 그룹 라벨 행, 결측은 "—"),
<단위>마다 카드 하나(눈썹 → 제목 → 문장 하나 → 키–값 행 → 전폭 보조 버튼), 그림 2(<단위>별 12개월 비율, 목표는 점선 기준선) 옆에 주석 카드(번호 붙인 방법 주석, 출처, 갱신 시각), 잉크 바닥.
필터는 화면 위 알약 한 줄에 두고 모든 그림·표·카드에 함께 적용해 줘.
색은 "Data Colors"의 값만(데이터에 클레이 금지), 숫자·날짜는 "Numbers, Dates & Units"(한국어는 억·만·부·%p), 부품은 "Component Stylings", 폭별 배치는 "Responsive Behavior"를 따라 줘.
범례 대신 선 끝에 라벨을 써 줘. 모든 차트에 호버 툴팁, 키보드 조작, 스크린 리더용 표를 넣고, 끝내기 전에 "Agent Prompt Guide"의 점검 목록을 확인해 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
replace colors with the tokens (series → sky/fig/amber, comparisons → dashed gray, no clay on data), fonts with the type rules (sans headings 600–700, serif only in the statement and findings),
chart marks with the chart rules (finding titles, Note captions, end labels instead of legends, light gridlines on a white plot panel), tables with ink rules and a tinted subject column,
KPI tiles with a Key findings card (serif bullets beside key–value rows), and number formats with the formats section.
Where the current screen breaks a rule in "Do's and Don'ts" (dual axis, pie, legend, bold serif, clay series, colored values), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does, severity (must fix / should fix / fine), and the fix.
Cover: run-in statement first, key findings, figure titles as findings with Note captions, end labels and no legends, comparison dashed gray, no clay on data,
categorical count, ink-ruled tables with a tinted subject column, card anatomy, heading weights, number formats, change colors, density, accessibility.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `anthropic.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop.
2. Dashboard background `#faf9f5`; card containers `#f5f4ed` with 24–28px inner padding and no border; each chart sheet white (`#ffffff`) inside its card.
3. Sheet titles bold, written as the finding; the method in the caption ("Note: …"). Legends off; label the line ends (Mark labels → Line ends). Prior year and target as dashed `#b0aea5` reference lines with labels.
4. Lines size 2–2.5, markers off except the last point; gridlines `#e8e6dc`; axis ticks `#87867f`.
5. Key figures as a text table with hairline row dividers, not big-number tiles; the current-month column highlighted with `#e4edf8`.
6. Number formats: `₩#,##0,,M` · `#,##0.0%` · change `+0.0%;−0.0%`; Korean workbooks use custom formats with 억/만 via calculated fields.
7. Fonts: Tableau Book throughout unless Source Serif 4 is installed on every viewing machine and on the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`.
2. Use only the first four data colors for categories (three hues plus gray Other). Clay is not in the list on purpose.
3. Install Inter on authoring and viewing machines, or accept the Segoe UI fallback.
4. Title each visual with the finding (bold) and put the method in the subtitle; legends off, data labels on the last point only.
5. Key figures: a table or multi-row card with hairlines in `#dedcd1`, values at 17px in ink, change measures with conditional formatting in `#4e7a30` / `#b0453b` only.
