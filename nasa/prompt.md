# Prompt pack — NASA style

Install the style in your project first:

```
npx @vizney/styles@latest add nasa
```

or run `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- nasa`, or unzip `nasa-dashboard-style.zip` in the project root. Agents that read skills then load `dashboard-style` by themselves; prompts 1–4 are the same three modes (build, restyle, review) written out for agents that do not. Replace the parts in `<angle brackets>`.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a <readiness review, go-live review or another countdown report> for
<company> as one self-contained HTML file with fictional data, in English and Korean (?lang=en|ko, English by default).
Header: 60px on black with the company and report name, <projects, releases or sites> as tabs (code in DM Mono, the
selected one white with a 2px underline; the one filter for every card, kept in the URL) and EN/KO.
Then the result in one sentence and the countdown band on #0b3d91: the target date and backups, an L− clock
(DAYS : HRS : MINS in DM Mono 300, units in capitals at 82% white) and four key figures split by 1px rules, each
label → value → change with ▲ ▼ (#4cd493 good, #ff9088 bad). Under it a milestone strip with holds as white blocks.
First screen: Figure 1, a GO/NO-GO poll of <teams or positions> (NO-GO first with a 3px #f2473f rule, call signs in
DM Mono, dotted leaders to the status word, NO-GO on a red chip with black text, open-item bars, need-by L− day);
beside it Figure 2, <a map or timeline> on a navy #061634 screen in a 1px #0b3d91 frame with a clock row on top.
Below, a light #f6f6f6 section with white panels: <open items against plan> in the Earth Indicators grammar (ink
subject line, gray plan with hollow weekly rings, the title in capitals inside the plot) and a table of <items to
close> by margin. Then a black section with <one or two scatters> on navy screens: gray dots, the subject in white,
red only past a threshold.
Every view in the same panel: DM Mono label, finding title, subtitle, keys, view, data source note. Colour only for a
state; the rest ink and gray. Use only the values in "Data Colors", the formats in "Numbers, Dates & Units" and the
components in "Component Stylings". No insignia, logotype, seal, patches, photos, starfields, real missions, vehicles,
pads, centers or people. Every view needs a tooltip, keyboard control and a screen-reader table; before you finish,
run the checklist in "Agent Prompt Guide" and fix what fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 <준비 점검, 오픈 점검 등 카운트다운이 있는 보고서>를 가상 데이터로,
HTML 파일 하나에 한국어·영어(?lang=ko|en, 기본 영어)로 만들어 줘.
머리: 검정 60px 줄에 회사와 보고서 이름, <프로젝트·릴리스·현장> 탭(코드는 DM Mono, 고른 탭은 흰 글자에 2px 밑줄,
모든 카드에 적용되는 필터, 주소에 저장), EN/KO.
이어서 결과 한 문장과 #0b3d91 카운트다운 띠: 목표일과 예비일, L− 시계(일 : 시간 : 분, DM Mono 300, 단위는 흰색 82%),
1px 선으로 나눈 핵심 수치 넷(지표명 → 수치 → 증감, ▲ ▼, 좋으면 #4cd493 · 나쁘면 #ff9088). 그 아래 정지 구간을
흰 블록으로 둔 마일스톤 띠.
첫 화면: 그림 1 <팀·자리>의 GO/NO-GO 폴(NO-GO 먼저, 왼쪽 3px #f2473f 선, 호출 부호는 DM Mono, 점선 리더 끝에 판정
단어, NO-GO는 빨간 칩에 검은 글자, 미결 항목 막대, 필요 시점 L− 날). 옆에 그림 2 <지도·타임라인>을 1px #0b3d91
테두리의 남색 #061634 화면에, 위에는 시계 칸 줄.
아래는 연회색 #f6f6f6 띠와 흰 카드의 밝은 절: <계획 대비 미결 항목>을 Earth Indicators 문법(잉크색 주인공 선,
주마다 빈 원을 단 회색 계획선, 그림 안 대문자 제목)으로, <닫을 항목> 표는 여유 순으로. 이어서 검정 절에 남색 화면의
<산점도 한두 개>: 회색 점, 주인공은 흰색, 기준을 넘은 것만 빨강.
모든 카드는 같은 해부: DM Mono 라벨, 결과 제목, 부제, 범례, 그림, 자료 출처 주. 색은 상태에만 쓰고 나머지는
잉크와 회색. "Data Colors"의 값, "Numbers, Dates & Units"의 표기(한국어 16자리 중 14 GO · 1만분의 1 · ▲ 10%p),
"Component Stylings"의 부품만 써 줘. 휘장·로고타이프·인장·패치·사진·별 배경·실제 임무·발사체·발사대·센터·인물은
쓰지 마. 모든 그림에 툴팁, 키보드 조작, 화면 낭독기용 표를 넣고, 끝내기 전에 "Agent Prompt Guide"의 점검 목록을
확인해 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
black dark sections with square #17171b panels and no borders, light sections on #f6f6f6 with white panels, Inter
titles, Public Sans text and DM Mono for every number and label (Pretendard in Korean), 11.2px DM Mono capitals as
figure labels.
Turn the KPI row into the countdown band on #0b3d91 (an L− clock if the report has a date to count to). Turn status
lists into a GO/NO-GO poll: status as a word, failing rows first with a 3px #f2473f rule. Put maps and scatters on
navy #061634 screens with a clock row. Keep the subject in ink and everything else gray; colour only for GO and
NO-GO. Keep every number; rewrite titles as findings.
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, donut, gauges, glow, starfields, a series in
nasa-blue or nasa-red), replace that view with the one the spec names for its question in "Charts".
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
pass or fail, the fix.
Cover: titles state findings; the countdown band and its key figures carry ▲ ▼ changes; status is a word and NO-GO
comes first with a 3px rule; screens are navy with a blue frame and a clock row; the subject is ink and the rest gray;
red appears only for NO-GO, a station down and a pass over the threshold; light sections run the full width; text
≥ 4.5:1; every view has a tooltip, keyboard control and a data table; nothing overlaps at 390px; no insignia,
logotype, seal, patch, photo, real mission, vehicle, pad, center or person. Then list the fixes in order of how much
they change the reading.
```

## 5. Reproduce Figure 1 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 1 from poll.csv (columns: flight, call_sign, position, status,
open_items, constraints, need_by_L, need_by_date; status is GO, NO-GO or PENDING) for flight VS-12, as one HTML file
with an SVG or HTML board on a #17171b panel with square corners.
1. Frame: one 22px row per position, NO-GO first, then GO, then PENDING; #2e2e32 row rules; a DM Mono 11.2px
   capitals head (Position · Status · Open · Cons. · Need by).
2. Each row: the call sign in DM Mono 12.5px/500, the position name in Public Sans 13.5px, a dotted #444447 leader to
   the status word.
3. Status: GO in #4cd493 DM Mono 500; NO-GO in black on a square #f2473f chip, and a 3px #f2473f rule on the row's
   left edge; PENDING in #959599.
4. Open items as a #717173 bar with its number; constraints in #ff9088 (blank when zero); need by as "L−3 · NOV 21".
5. The label "FIG 1 · GO/NO-GO POLL", the title with the finding ("Two of 16 positions are NO-GO, each on one
   constraint"), the subtitle "Readiness by position on Nov 18, NO-GO first: open constraint to launch means NO-GO"
   and the note on open items and constraints.
Add a tooltip (#2e2e32 with a 2px white top rule) with the constraint names, keyboard control and a screen-reader
table, then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `nasa.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. The categorical palette is blue, orange, green, then gray; the sequential palette is the five blues.
2. Dashboard background `#000000`; each sheet on `#17171b` with no border, row dividers `#2e2e32`, text `#e3e3e3`, headers `#959599`; light sheets on `#ffffff` with `#e3e3e3` dividers and `#58585b` ticks. Each sheet's title is the finding.
3. Countdown band: a `#0b3d91` container with BANs in DM Mono (or Tableau Book), labels in capitals.
4. Poll: a text table from `poll.csv` sorted by status, a square mark coloured GO `#14a06a` / NO-GO `#f2473f`, a bar for `open_items`. Open items: actual in ink, plan in gray with circle marks, a reference line at L−2. Scatters on a `#061634` worksheet shading; a log axis for chance of collision with reference lines at 1e-4 and 1e-7, formatted `"1 in "#,##0`.
5. Fonts: Tableau Book unless Inter, Public Sans and DM Mono are installed on every viewing machine and the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out `#17171b` with square corners and no border.
2. Status in conditional formatting: NO-GO background `#f2473f` with black text, GO text `#4cd493`; changes always with ▲ ▼.
3. Install Public Sans on authoring and viewing machines, or accept the Segoe UI fallback.
4. Countdown band: cards on a `#0b3d91` shape. Open items: a line chart with the plan as a gray second series with markers and a constant line at L−2.
5. Scatters: a `#061634` plot area, a log Y axis for chance of collision and constant lines at the thresholds; the subject in white, the rest `#7d8496`.
