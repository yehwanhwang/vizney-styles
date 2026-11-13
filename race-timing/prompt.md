# Prompt pack — F1 style

Install the style in your project first:

```
npx @vizney/styles@latest add race-timing
```

or run `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- race-timing`, or unzip `race-timing-dashboard-style.zip` in the project root. Agents that read skills then load `dashboard-style` by themselves; prompts 1–4 are the same three modes (build, restyle, review) written out for agents that do not. Replace the parts in `<angle brackets>`.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a <race debrief, test-session report or another timed operation> for
<team or company> as one self-contained HTML file with fictional data, in English and Korean (?lang=en|ko, English by
default), on the black page the spec describes.
Header on one line: the team and report name in condensed capitals, <rounds, sessions or events> as pill tabs (the one
filter for every view, the selected tab white with black text, kept in the URL), the EN/KO pill.
First screen in two columns. Left: an eyebrow (<round · place · laps · date> and a FINAL tag), the finding in one or two
sentences, a line on the second car and points against plan, then the onboard display on #0d0d14 with a 1px #303037 rim
and 24px corners: 15 lights for the last 15 laps against the winner (#04a97a quicker, #b88c19 slower, #26262f pit laps),
a dial for the pit stop average with a white tick at the target, the finishing position as a gear readout with ▲ from
the grid, a dial for points with a white tick at the plan, and two readouts (gap to the win against the last round, the
best lap in a #8c51d9 chip when it is the fastest). Right: the circuit map, our best lap against the winner's in 24
mini-sectors on the diverging ramp, white S/F and sector lines, turn numbers outside the apexes, sector gaps in the foot.
01 Race: the timing tower (position boxes, ▲▼, codes, gaps, tyre stints lettered S M H, a purple dot on the fastest lap)
beside the gap to the winner lap by lap, pit cycles shaded and dashed. 02 Lap: the speed trace of both best laps with the
running gap below (up is ahead) and a small circuit that follows the cursor. 03 Pit lane and season: pit stops against
the target, points by round against plan, and the stint report.
Every view on the same #15151e panel with 8px corners and no border: figure label, finding title, subtitle with the unit,
keys, view, note. At most seven views per section. Our cars white, the winner #8b8f99, everyone else #5f6270; purple,
green and yellow only with their timing meanings. Use only the values in "Data Colors", the formats in "Numbers, Dates &
Units" and the components in "Component Stylings". No logos, official typefaces, photos, real teams, drivers or circuits.
Every view needs a tooltip, keyboard control and a screen-reader table; before you finish, run the checklist in
"Agent Prompt Guide" and fix what fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <팀 또는 회사>의 <레이스 디브리프, 테스트 세션 보고 등 시간을 재는 업무 보고>를 가상 데이터로,
HTML 파일 하나에 한국어·영어(?lang=ko|en, 기본 영어)로 명세의 검은 페이지 위에 만들어 줘.
머리는 한 줄: 팀과 보고서 이름, <라운드·세션·행사> 알약 탭(모든 그림에 걸리는 필터 하나, 고른 탭은 흰 바탕에 검은 글자, 주소에 남김), EN/KO.
첫 화면은 두 단. 왼쪽: 눈썹 줄(<라운드 · 장소 · 랩 수 · 날짜>와 FINAL 표시), 결과를 말하는 한두 문장, 두 번째 차량과 계획 대비 포인트 한 줄,
그리고 온보드 계기판(#0d0d14 바탕, 1px #303037 테두리, 모서리 24px): 마지막 15랩을 우승 차량과 견준 라이트 15개(빠름 #04a97a, 느림 #b88c19,
피트 랩 #26262f), 목표에 흰 눈금을 둔 피트 스톱 평균 다이얼, 기어 자리의 순위와 그리드 대비 ▲, 계획에 흰 눈금을 둔 포인트 다이얼, 아래 두 줄
(지난 라운드 대비 우승과의 차이, 레이스 최고 랩이면 #8c51d9 칩에 넣은 최고 랩). 오른쪽: 서킷 맵. 우리 최고 랩과 우승 차량의 최고 랩을 미니 섹터
24칸으로 견줘 발산 색으로 칠하고, 흰 출발선과 섹터 경계, 정점 바깥의 코너 번호, 아래에 섹터별 차이를 둬.
01 레이스: 타이밍 타워(순위 상자, ▲▼, 세 글자 코드, 간격, S M H 글자를 넣은 타이어 스틴트, 레이스 최고 랩에 보라 점)와 랩별 우승 차량과의 차이
(피트 사이클은 음영과 점선). 02 랩: 두 최고 랩의 속도 선과 아래 누적 시간 차이(위가 앞섬), 커서를 따라가는 작은 서킷. 03 피트 레인과 시즌:
목표 대비 피트 스톱, 계획 대비 라운드별 포인트, 스틴트 보고 표.
모든 그림은 같은 #15151e 판(모서리 8px, 테두리 없음)에 그림 번호 → 결과를 말하는 제목 → 단위를 적은 부제 → 범례 → 그림 → 주석. 절마다 그림 7개 이하.
우리 차량은 흰색, 우승 차량 #8b8f99, 나머지 #5f6270. 보라·초록·노랑은 타이밍 화면의 뜻으로만 써. 색은 "Data Colors", 숫자는
"Numbers, Dates & Units"(한국어 표기 포함), 부품은 "Component Stylings"의 값만 써. 로고, 공식 서체, 사진, 실제 팀·드라이버·서킷은 넣지 마.
모든 그림에 툴팁, 키보드 조작, 스크린 리더용 표를 넣고, 끝내기 전에 "Agent Prompt Guide"의 점검 목록으로 확인해서 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
- the page to #000000 and every view onto a #15151e panel with 8px corners, no border and no shadow: a figure label,
  a title that states the finding, a subtitle with the unit, keys, the view, a note;
- the header to one line with condensed capitals, the filter as pill tabs (selected white with black text);
- the headline KPIs to the onboard display (lights for recent laps or periods against a reference, dials with a white
  target or plan tick, the main result as the gear readout, readouts with ▲▼ and a word);
- any lap- or route-position comparison to a circuit map coloured by mini-sector on the diverging ramp, and any
  speed-by-distance comparison to a speed trace with the running gap in a second panel (never a dual axis);
- colours to the tokens: the subject white with a card-coloured halo, the reference #8b8f99, the rest #5f6270;
  purple #8c51d9, green #04a97a and yellow #b88c19 only with their timing meanings and with ▲▼ or a word;
- tyre or category strips to lettered marks (S #cc3336, M #b88c19, H #d9dce2);
- number formats to "Numbers, Dates & Units" (timing to the thousandth, signs on gaps, true minus, pts and km/h).
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, donut, gauges without targets, gradients, glow,
borders on panels, real teams or logos, a colour per car, cards side by side that end on different lines, more than
seven views in a section), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
severity (must fix / should fix / fine), and the fix.
Cover: the headline states the finding; the onboard display shows each key figure against its target, plan, grid or the
last round with ▲▼ and a word; the lights skip pit laps; the map's sector gaps add up to the lap gap and its labels never
touch; whether every device reads at least as well as a plain bar or table; one panel anatomy for every view; white for
our cars and gray for the rest; purple, green and yellow only with their timing meanings; lettered tyres; pit cycles
marked; no dual axis; timing precision and signs in both languages; contrast; tooltips, keyboard and data tables; views
per section; panels in a row ending on one line; density at 1440 × 810 and 390px.
```

## 5. Reproduce Figure 2 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 2 from stints.csv (columns: round, city, position, car, number,
team, stint, compound, lap_start, lap_end, laps, stop_after_s, fastest_lap; position is empty for a retired car;
compound is S, M or H) for round 18, as one HTML file with an SVG chart on a #15151e panel with 8px corners on a
#000000 page.
1. Frame: one row per car in finishing order, the top ten, then our retired car if any; a lap axis under the strips
   (LAP 1, 10, 20 … 57) in 12.5px #aaaaaa condensed.
2. Strips: a 14px bar per stint from lap_start to lap_end with 2px corners and 2px gaps at each stop, filled S #cc3336,
   M #b88c19, H #d9dce2, the letter inside (white on S, #15151e on M and H).
3. Our rows: Vizney Racing's cars (27 and 12) on #1c1c25 with a 3px white edge and a white position box with black
   digits; every other row plain.
4. Marks: a purple #8c51d9 dot over the lap in fastest_lap; a white ✕ where a retired car stopped.
5. Title with the finding ("Two stops put car 27 within half a second of the win"), the subtitle "Tyre stints by lap,
   top ten" and a note that says stints are split at each stop.
Add a tooltip (#1c1c25, 1px #47464c, 6px corners) with the car, the stints and the stops, keyboard control and a
screen-reader table, then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `race-timing.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette is the tyres (soft, medium, hard) then gray; use the status palette for purple, green and yellow.
2. Dashboard background `#000000`; worksheets and panes shaded `#15151e`, no borders, row gridlines `#303037`, text `#d9d9df`, headers `#aaaaaa`. Each sheet's title is the finding; the method goes in the caption.
3. Onboard display: a horizontal container on `#0d0d14`. Lights as a circle mark per lap coloured by a calculated `Quicker / Slower / Pit lap`; the dials as a bar on a fixed axis with a reference line at the target or plan (or a text BAN with its status line); the position as a large text object with `▲3` under it.
4. Circuit map: a line mark on continuous X and Y (equal scales), Path on distance, Detail on mini-sector, Colour on the gap with the diverging palette stepped at ±0.005, ±0.02 and ±0.05 s; a dual-mark copy underneath in `#0d0d14` at a larger size for the track band.
5. Timing tower: a text table (position, change, car, team, gap) beside Gantt bars from `stints.csv` (`lap_start`, size `laps`, colour `compound`, label the compound).
6. Gap to the winner: a line by lap with a reference line at 0 and reference bands over the pit cycles. Telemetry: two sheets stacked on one distance axis (speed; the running gap as an area above and below zero), never a dual axis.
7. Formats: lap times as `m:ss.000` through a calculated string, gaps `+0.000" s";−0.000" s"`, stops `0.00" s"`, points `0" pts"`; Korean workbooks `+0.000"초"` and `0"점"`. Fonts: Tableau Book unless Barlow and Barlow Condensed are installed on every viewing machine and the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out `#15151e` with 8px corners and no border on a black page.
2. The first data colours are the tyres (soft, medium, hard), then gray; status colours (purple, green, yellow) go in conditional formatting, always with a sign or a word.
3. Install Barlow and Barlow Condensed on authoring and viewing machines, or accept the Segoe UI fallback.
4. Title each visual with the finding, put the method in the subtitle, gridlines `#303037`, data labels on line ends, legends off when labels name the series.
5. Onboard display: card visuals on a `#0d0d14` rectangle; the lights as a 15-column matrix with conditional backgrounds; the dials as bar or KPI visuals with a target line (avoid a gauge without the target tick); the best lap card turns `#8c51d9` when it is the race's fastest.
6. Circuit map: a scatter chart of the track's x, y points (equal axes, small markers, no gridlines) with conditional colour on the gap, or a Deneb (Vega-Lite) line with `detail` on mini-sector. Timing tower: a table visual beside stacked bars of stints by lap. Gap and telemetry: line charts with a constant line at 0, speed and gap as two visuals on one x axis.
