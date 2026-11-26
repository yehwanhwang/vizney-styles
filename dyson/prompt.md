# Prompt pack — Dyson style

Install the style in your project first:

```
npx @vizney/styles@latest add dyson
```

or run `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- dyson`, or unzip `dyson-dashboard-style.zip` in the project root. Agents that read skills then load `dashboard-style` by themselves; prompts 1–4 are the same three modes (build, restyle, review) written out for agents that do not. Replace the parts in `<angle brackets>`.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a <test review, quality review or another engineering report> for
<company> as one self-contained HTML file with fictional data, in English and Korean (?lang=en|ko, English by default).
Header: black, two lines. Line one: business and report name, the build or period, EN/KO. Line two: <models,
products or lines> as tabs set like a menu row (16px Light white, the selected one Medium with a 2px white
underline; the one filter for every card, kept in the URL).
First screen: a kicker (subject · period · targets met, the count in red), the result in two Light sentences, then
round screens for <two to four run-time or capacity measures> (black circles, the measure's name in its colour, the
value in Light, a battery filled by value ÷ MIN, the gap to the MIN under each) beside spec rows for <the other
targets> (label and limit → large Light value with a small unit → ✓ or ✗ → hairline). On the right, on the one
#f7f7f7 panel, an exploded view of <the parts of the product> (parts along one dash-dot axis, each as long as its
weight or cost, a budget bracket, a red tip over budget, purple for a part changed since the last review, numbered
balloons) with the assembled total against the MAX. Under the left column, a laser-floor strip of <what is left
behind>, one dot per small share.
Below: one section of black graph screens (bars from a white dash-dot target line, white when met, red #f0403a when
missed, the latest value large at the right) beside a table of the measures the screens do not show; then a test
timeline on a black screen beside an issue table.
Every view in the same card: FIG. n, finding title, subtitle, keys, view, caption. Use only the values in "Data
Colors", the formats in "Numbers, Dates & Units" and the components in "Component Stylings". Never fill a table cell
or a plot background with green or red. No Dyson logo or typeface, photos, renders, product or technology names, or
real numbers. Every view needs a tooltip, keyboard control and a screen-reader table; before you finish, run the
checklist in "Agent Prompt Guide" and fix what fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 <시험 보고, 품질 보고 등 엔지니어링 보고서>를 가상 데이터로,
HTML 파일 하나에 한국어·영어(?lang=ko|en, 기본 영어)로 만들어 줘.
머리: 검정 두 줄. 첫 줄에 사업부와 보고서 이름, 빌드나 기간, EN/KO. 둘째 줄에 <모델·제품·라인> 탭을 메뉴 줄처럼
(16px Light 흰 글자, 고른 탭은 Medium에 2px 흰 밑줄. 모든 카드에 걸리는 필터 하나, 주소에 남김).
첫 화면: 키커(대상 · 기간 · 목표 달성 수, 수는 빨강), 결과를 두 문장 Light로, 그다음 <런타임·용량 지표 2~4개>의
둥근 화면(검은 원, 지표 이름은 그 색, 값은 Light, 값 ÷ 최소만큼 채운 배터리, 아래에 최소와의 차이)과 나머지
목표의 사양 줄(라벨과 기준 → 큰 Light 값과 작은 단위 → ✓ 또는 ✗ → 머리카락 선). 오른쪽 #f7f7f7 판 하나에
<제품 부품>의 분해도(1점 쇄선 축 하나에 부품, 길이는 무게나 비용, 예산 괄호, 예산 초과는 빨간 끝, 지난 검토
이후 바꾼 부품은 보라, 번호 풍선)와 조립 합계 대 최대. 왼쪽 열 아래에 <남은 것>의 레이저 바닥 띠(점 하나가 작은 몫).
아래: 검은 그래프 화면 절(흰 1점 쇄선 목표선에서 시작하는 막대, 채우면 흰색, 못 채우면 빨강 #f0403a, 최신 값은
오른쪽에 크게)과 그 화면에 없는 지표의 표, 그다음 검은 화면의 시험 일정과 문제 표.
모든 그림은 같은 카드: 그림 번호, 결과를 말하는 제목, 부제, 범례, 그림, 주석. "Data Colors"의 값, "Numbers,
Dates & Units"의 표기, "Component Stylings"의 부품만 써. 표 칸이나 그림 바탕을 초록·빨강으로 칠하지 마.
Dyson 로고·서체, 사진, 렌더, 제품·기술 이름, 실제 숫자는 쓰지 마. 모든 그림에 툴팁, 키보드 조작, 스크린 리더용
표를 두고, 끝내기 전에 "Agent Prompt Guide"의 점검 목록을 돌려 틀린 곳을 고쳐 줘.
```

## 3. Restyle an existing dashboard

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
a white page under a black two-line header, one #f7f7f7 panel at most, ink #333333 text, Jost with Light 300 for
every measured value and Medium 500 for labels (Noto Sans KR in Korean), figure labels as 'FIG. n'.
Turn the KPI row into round screens or spec rows with the gap to each limit and ✓ or ✗. Put every chart that
measures on a black screen with white values: bars from the target line, white when met, red #f0403a when missed.
Remove coloured table cells and coloured plot zones; a miss is a red value with ✗. Keep every number; rewrite titles
as findings; drop numbers a chart and its neighbouring table both show.
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, donut, gauge, mode colours as series, gradients),
replace that view with the one the spec names for its question in "Charts".
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
pass or fail, the fix.
Cover: titles state findings; the page is white with one #f7f7f7 panel; measurements sit on black screens with white
Light values; red appears only for a miss and always with ✗ or a word; purple only for a changed part with its
balloon; mode colours only on round screens; no filled table cells or tinted plot zones; no numbers repeated between
a chart and the table beside it; text ≥ 4.5:1; every view has a tooltip, keyboard control and a data table; nothing
overlaps at 390px; no Dyson logo, typeface, photo, render, product or technology name. Then list the fixes in order of
how much they change the reading.
```

## 5. Reproduce Figure 1 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 1 from parts.csv (columns: model, build, no, part, weight_g,
budget_g, over_budget_g, changed_in_build; build 41 only) for model C60, as one HTML file with an SVG on a #f7f7f7
panel.
1. Axis: a vertical #7d8083 dash-dot line (14 4 2 4) from the floor to the hand.
2. Parts: no 1 (cleaner head) at the bottom to no 8 (battery) at the top, at even gaps, centred on the axis; each a
   5px-rounded rectangle as long as weight_g on one scale, #d9dbdd with a #7d8083 edge; #6b46c1 when changed_in_build
   is after 37; over_budget_g as a #d0273b cap at the top of the part.
3. Budget: a 1px #555555 bracket as long as budget_g on the opposite side of each part.
4. Labels: a numbered balloon (19px, 1px #333333, purple when changed) on a leader line, then the name 14px/500,
   the weight 21px Light with 'g', and the gap 12.5px (red 500 when over, 'changed in build 38' in purple).
5. Under the stack: the assembled weight as one bar of the eight parts in order, the MAX (2,900 g) as a dotted line,
   the total and '40 g over' at the right.
6. The label "FIG. 1", the title with the finding ("The cleaner head is 50 g over its budget, so the machine is
   40 g over"), the subtitle "Weight by part from the floor to the hand, each against its budget" and the note on
   how it was weighed.
Animate the parts sliding apart from assembled (0.9s), add a tooltip, keyboard control and a screen-reader table,
then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `dyson.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette is purple, green, copper, then nickel grey; the sequential palette is the five purples.
2. Dashboard background `#ffffff`, sheets on white with no borders, row dividers `#dadada`, text `#333333`, headers `#555555`. One container on `#f7f7f7` for the exploded view. Each sheet's title is the finding.
3. Round screens: a BAN on a black container, the measure name in its mode colour above, the gap to the MIN as a second line with ✓ or ✗.
4. Exploded view: a Gantt bar on one axis from `parts.csv`, `[Start] = RUNNING_SUM([weight_g]) - [weight_g] + [no] * gap`, size `[weight_g]`, colour by state (changed, over, other).
5. Graph screens: worksheet shading `#000000`, a bar of `[Value] - [Target]` with a white dash-dot reference line at 0, colour white when met and `#f0403a` when missed, the latest value as a large label.
6. Fonts: Tableau Book unless Jost and Noto Sans KR are installed on every viewing machine and the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out white with square corners and no border.
2. Misses in conditional formatting: font colour `#b0122f` with ✗ in the value; never a coloured cell background.
3. Install Jost on authoring and viewing machines, or accept the Segoe UI fallback.
4. Graph screens: a column chart of the gap to target on a `#000000` plot area, a white constant line at 0, data colours white and `#f0403a` by rule.
5. Exploded view: a stacked bar with a transparent spacer series between parts, or a Deneb (Vega-Lite) visual.
