# Prompt pack — Netflix style

Install the style in your project first:

```
npx @vizney/styles@latest add netflix
```

or run `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- netflix`, or unzip `netflix-dashboard-style.zip` in the project root. Agents that read skills then load `dashboard-style` by themselves; prompts 1–4 are the same three modes (build, restyle, review) written out, so they also work for agents without skills. Then use one of these. They are written for coding agents such as Claude Code, Cursor and Codex, and for BI agents that read the same folder; the Tableau and Power BI notes are for people. Prompt 5 reproduces Figure 2 of the live sample from `tickets.csv`, which makes a quick test of an agent or a tool.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a weekly <sales or usage> dashboard for <company> as one self-contained HTML
file with fictional data, in English and Korean (?lang=en|ko, English by default), on the dark page the spec describes.
Top: a black header with the period, the EN/KO toggle, an outlined Export PDF and a red Copy as Markdown; one row of
outlined chips for <cities, regions or business units> that scopes every card, kept in the URL.
Then the billboard: color-block key art in the rail gradient with a giant outlined numeral, the TOP 10 badge and
"#1 this week · <item>", a bold headline that states the week's result, a two-sentence lede with the drivers, a
red and a gray button, and four key figures on translucent tiles (label → value → signed change vs last week, colored
by whether the change is good).
Sections are rows with a 24px title; at most seven views per screen; every view on the same #161616 card with no border
(figure label → finding title → subtitle → keys → view → "Note:"):
- This week: the Top 10 of <items> in two columns (an outlined numeral, the name, full-digit value, a bar against #1 in red
  only for #1, the move since last week and weeks in the Top 10; a red NEW badge for new entries); <measure> by week
  against last year (dashed gray, line ends labeled) beside weeks in the Top 10 as a grid of ranks with #1 in red.
- Coming up: <upcoming items> as an episode list with the progress bar under each thumbnail (red only for the rows the
  title names) beside <channel> shares as 100% stacked bars; a Top 10 table of every <item> (rank, name, weeks in the
  Top 10, value, change, a progress bar, runtime or duration, rating) with a show-all button.
- Method and sources as a FAQ accordion.
Use only the values in "Data Colors" (the subject red #f0313b, others gray; the UI red #e50914 only on buttons, badges
and ribbons), the formats in "Numbers, Dates & Units", the components in "Component Stylings" and the breakpoints in
"Responsive Behavior". No photos, posters or logos. Every chart needs a hover card, keyboard control and a
screen-reader table.
Before you finish, run the checklist at the end of "Agent Prompt Guide" and fix anything that fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 주간 <판매·이용> 대시보드를 가상 데이터로 HTML 파일 하나에 만들어 줘.
명세가 말하는 어두운 화면으로, 한국어·영어를 한 파일에서 ?lang=ko|en으로 바꾸고 기본은 영어야.
맨 위에 기간, EN/KO 토글, 테두리만 있는 PDF로 내보내기, 빨간 마크다운으로 복사가 있는 검정 머리. 그 아래
<도시·지역·사업부> 칩 한 줄이 모든 카드에 함께 적용되고 주소에도 남게 해 줘.
이어서 빌보드: 레일 그라데이션 색 블록에 큰 외곽선 숫자를 얹은 키 아트, TOP 10 배지와 "이번 주 1위 · <항목>",
이번 주 결과를 말하는 굵은 제목, 원인을 말하는 두 문장, 빨간 단추와 회색 단추, 반투명 타일의 핵심 수치 4개
(지표명 → 값 → 지난주 대비 증감, 증감 색은 그 지표에 좋은 변화인지로).
절은 24px 제목의 줄로 열고, 한 화면의 그림은 7개 이하, 모든 그림은 테두리 없는 #161616 카드
(그림 번호 → 결과를 말하는 제목 → 부제 → 범례 → 그림이나 표 → "주:")에 넣어 줘:
- 이번 주: <항목> Top 10(두 줄 다섯 칸, 외곽선 숫자 옆에 이름과 전체 자릿수 값, 1위만 빨강인 1위 대비 막대,
  지난주 순위 변화와 Top 10 주 수, 새로 든 항목엔 빨간 신규 배지), 지난해(회색 점선)와 비교한 주별 <지표> 선(선 끝 라벨),
  1위만 빨강인 Top 10 주 수 순위 격자.
- 다가오는 것: 섬네일 아래 진행 막대가 있는 에피소드 목록 형식의 <다가오는 항목>(제목이 말하는 줄만 빨강),
  <경로> 비중 100% 누적 막대, 모든 <항목>의 Top 10 표(순위, 이름, Top 10 주 수, 값, 증감, 진행 막대,
  시간, 등급)와 모두 보기 단추.
- 방법과 출처는 FAQ 아코디언.
색은 "Data Colors" 값만(주인공 빨강 #f0313b, 나머지 회색, UI 빨강 #e50914는 단추·배지·띠에만), 숫자·날짜는
"Numbers, Dates & Units"(한국어는 만·장·%p, Top 10 값은 전체 자릿수, 시간은 시:분, 돈은 회사의 통화), 부품은
"Component Stylings", 폭별 배치는 "Responsive Behavior"를 따라 줘. 사진·포스터·로고는 넣지 마.
모든 차트에 호버 카드, 키보드 조작, 스크린 리더용 표를 넣고, 끝내기 전에 "Agent Prompt Guide"의 점검 목록을 확인해서
안 맞는 건 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
- the page to black #000000 and every view onto the same #161616 card (8px radius, no border, no shadow): an uppercase
  figure label, a title that states the finding, a subtitle with the measure, keys only where labels cannot work, and a
  note that starts with "Note:";
- the top to a billboard: color-block key art in the rail gradient, the TOP 10 badge line, a headline that states the
  result, a lede, a red and a gray button, four key figures with signed, good/bad-colored changes;
- colors to the tokens: the subject #f0313b only where the title points, a second real category #6a88f2, the rest
  #595959 behind 2px gaps, last year dashed #808080; the UI red #e50914 only on buttons, badges and ribbons;
- rankings to the Top 10 parts (outlined numerals with bars and rank moves, a grid of ranks, the Top 10 table with full-digit values)
  and shares of a whole to 4px progress bars; other charts to the form "Charts" picks for their question;
- gridlines solid #2d2d2d on rows only, line ends labeled;
- filters to one row of outlined chips above everything, the selected chip white;
- number formats to "Numbers, Dates & Units" (true minus, pts / %p, K M / 만, full digits in Top 10 lists, h:mm).
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, donut or gauge, glow, borders or shadows on cards,
photos or logos, a card that is mostly red, more than seven views on a screen), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
severity (must fix / should fix / fine), and the fix.
Cover: the billboard states the result; key figures with change colors; one card anatomy for every view; finding
titles and "Note:" notes; red only where the title points and gray for everyone else; no UI red on data; the comparison
line; Netflix's parts for rankings and progress; the chart form for each question; row gridlines and labels instead of
legends; no dual axis; full-digit values in Top 10 lists; number, date, runtime and week formats in both languages;
contrast on dark surfaces (muted only on #161616 or darker) and second cues for dim marks; hover cards, keyboard and
data tables; views per screen; density at 1440 × 900 and 390px.
```

## 5. Reproduce Figure 2 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 2 from tickets.csv (columns: week_start, week_end, city, tickets,
tickets_last_year; city is "All cities", "Los Angeles", "New York" or "Chicago") for "All cities", as one HTML file with
an SVG chart on a #161616 card (8px radius, no border) on a black page.
1. Frame: solid #2d2d2d gridlines on rows only, a #414141 baseline, four y ticks in compact counts (150K … 300K) in 12px
   #808080, four week ticks (Aug 10, Sep 7, Oct 5, Oct 26) with the last week in white.
2. Comparison first: tickets_last_year as a dashed #808080 line, 2px, dash 6 4.
3. The subject: tickets as a solid #f0313b line, 2.5px, a hollow marker on the last week.
4. Label both line ends with name and value ("This year 287.8K" in #ff5a63, "Last year 269.0K" in white, values in
   #b3b3b3); no legend.
5. Title with the finding ("Tickets beat last year in 10 of 12 weeks"); a note that starts with "Note:".
Add a hover card (#232323, 6px radius, shadow 0 3px 10px rgba(0,0,0,.75)), keyboard control and a screen-reader table,
then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `netflix.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. Assign the subject first so it takes red; a second real category takes blue and the rest take the Other gray.
2. Dashboard background `#000000`. Each sheet sits in a container shaded `#161616` with 20/24px inner padding and no border; worksheet shading `#161616`; tooltips `#232323` with white text.
3. Sheet title: the finding, bold, white; a subtitle line with the measure in `#b3b3b3`; the caption starts with `Note:`. A text object above holds the figure label in Tableau Book 9 bold, uppercase, `#b3b3b3`.
4. Grid lines: rows only, solid, `#2d2d2d`; zero line `#414141`; no axis rulers; ticks `#808080`. Last year as a dashed line in `#808080`.
5. Top 10: filter to RANK(SUM(tickets)) ≤ 10, the rank as a big bold white label, the value in full digits. Weeks in the Top 10: a highlight table of show by week, red `#f0313b` for rank 1 and `#333333` for 2–10, the rank as the label (black on red).
6. Progress: a bar on a `#575757` track (a dual-mark bar or a Gantt), red only for the rows the title names, the value as a label.
7. Number formats: `#,##0` for Top 10 values · `#,##0.0,K` · `$#,##0.00,,"M"` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0.00"달러"` · `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Roboto is installed on every viewing machine and on the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out `#161616` without borders on a black page.
2. The first two data colors are red (the subject) and blue, then the Other gray; the colors after it exist only because Power BI wants a longer list. The UI red #e50914 is not in the list on purpose.
3. Install Roboto on authoring and viewing machines, or accept the Segoe UI fallback.
4. Title each visual with the finding and put the measure in the subtitle; gridlines solid `#2d2d2d`; data labels on the last point; legends off when labels name the series.
5. Key figures: cards on `#161616` with no border; change measures with conditional formatting in `#46d369` / `#e87c03` only, always with a sign. Top 10: a table visual with Top N = 10, the rank in bold, data bars in `#f0313b` for seats filled.
