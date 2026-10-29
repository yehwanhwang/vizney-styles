# Prompt pack — Anthropic style

Copy `DASHBOARD.md` (and `tokens.css`) into the root of your project, then use one of these. They are written for Claude Code, Cursor, Codex and similar coding agents; the Tableau and Power BI notes are for people.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly.
Build a monthly sales dashboard for <company> as one self-contained HTML file with fictional data.
Open with one serif sentence that states this month's revenue and its change versus the same month last year.
Then: four KPI cards (revenue, orders, return rate, <one metric of ours>), a 12-month trend with the prior year as the dotted comparison,
a top-5 list with hairline rows, and a detail table in the ink band. One filter row at the top applies to every card.
Use only the colors in "Data Colors", the formats in "Numbers, Dates & Units", the components in "Component Stylings"
and the breakpoints in "Responsive Behavior". Every chart needs a hover tooltip, keyboard control and a screen-reader table.
Before you finish, check the list at the end of "Agent Prompt Guide" and fix anything that fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘.
<회사>의 월간 매출 대시보드를 가상 데이터로 HTML 파일 하나에 만들어 줘. 한국어·영어를 한 파일에서 ?lang=ko|en으로 바꾸고 기본은 영어야.
첫머리에 이달 매출과 전년 동월 대비 증감을 세리프 문장 한 줄로 쓰고,
KPI 카드 4개(매출, 주문 수, 반품률, <우리 지표 하나>), 전년을 점선으로 둔 12개월 추세, 헤어라인 행의 상위 5개 목록, 잉크 띠의 상세 표를 넣어 줘.
필터는 화면 위 한 줄에 두고 모든 카드에 함께 적용해 줘.
색은 "Data Colors"의 값만, 숫자·날짜는 "Numbers, Dates & Units"(한국어는 억·만·부·%p), 부품은 "Component Stylings", 폭별 배치는 "Responsive Behavior"를 따라 줘.
모든 차트에 호버 툴팁, 키보드 조작, 스크린 리더용 표를 넣고, 끝내기 전에 "Agent Prompt Guide"의 점검 목록을 확인해 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data or its information architecture:
replace colors with the tokens, fonts with the type rules, chart marks with the chart rules, and number formats with the formats section.
Where the current screen breaks a rule in "Do's and Don'ts" (dual axis, pie, bold figures, colored text), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does, severity (must fix / should fix / fine), and the fix.
Cover: statement first, single accent, comparison style, categorical count, labels on marks, figure weight, number formats, change colors, density, accessibility.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `anthropic.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop.
2. Dashboard background `#faf9f5`; card containers `#f0eee6` with 24px inner padding and no border; the one dark container `#141413` for the detail table.
3. Lines: size 2, markers off except the last point; prior year as a dotted gray reference or dual line in `#73726c`; gridlines off on trend sheets; axis ticks `#73726c`.
4. Number formats: `₩#,##0,,M` · `#,##0.0%` · change `+0.0%;−0.0%`; Korean workbooks use custom formats with 억/만 via calculated fields.
5. Fonts: Tableau Book throughout unless Source Serif 4 is installed on every viewing machine and on the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`.
2. Use only the first four data colors for categories (three hues plus gray Other). The rest exist because Power BI needs a longer list.
3. Install Inter on authoring and viewing machines, or accept the Segoe UI fallback.
4. KPI cards: card visuals with the callout at 28px in ink and the category label in `#5e5d59`; conditional formatting of change measures with `#2c6e4f` / `#a33d34` only.
