# Prompt pack — Costco style

Install the style in your project first:

```
npx @vizney/styles@latest add costco
```

or run `curl -fsSL https://styles.vizney.com/install.sh | sh -s -- costco`, or unzip `costco-dashboard-style.zip` in the project root. Agents that read skills then load `dashboard-style` by themselves; prompts 1–4 are the same three modes (build, restyle, review) written out, so they also work for agents without skills. Then use one of these. They are written for coding agents such as Claude Code, Cursor and Codex, and for BI agents that read the same folder; the Tableau and Power BI notes are for people. Prompt 5 reproduces Figure 1 of the live sample from `comps.csv`, which makes a quick test of an agent or a tool.

## 1. A new dashboard (English)

```
Read DASHBOARD.md and follow it exactly. Build a weekly <operations or sales> report for <company> as one self-contained
HTML file with fictional data, in English and Korean (?lang=en|ko, English by default), on the white page the spec
describes.
Top: a blue #005dab promo band with the week and the current promotion's dates; a #fafafa header with the report name,
the period, the EN/KO toggle, an outlined Export PDF and a blue Copy as Markdown; a blue band of <regions, stores or
business units> as the one filter for every view, kept in the URL; a #fafafa status row with the reporting count in green.
Open with one sentence in the form of a sales release ("Net sales of $X million for the week ended …, an increase of
n percent from $Y million last year"), a lede with the second measure and the result against plan, and six price signs:
code, caps name, a big value with superscript $ and decimals, a signed change colored by whether it is good, a
fine-print line (plan, a per-unit figure or a rate) and a date code.
Beside them, the detail as a register receipt in a monospace font: one line per <department or category> with a
barcode-striped bar for its size, the value in $K rounded so the lines add up, VS LY with negatives in orange, then
SUBTOTAL and **** TOTAL, the item count, and <transactions by hour or another time profile> as the receipt's barcode.
The two columns end on one line.
Then charcoal #333333 bands with ruled blocks: a ranked board of <stores or units> against plan (bars from the plan
line, behind plan in #bc4700, the rest #cccccc); <stock or capacity> as racks of 100 slots against a plan-to-date line;
promotions as a ruled grid of coupons with redemptions against forecast; standard lines and bars for the rest.
Every view on the same white card (1px #d9d9d9): figure label → finding title → subtitle → keys → view → "Note:".
At most seven views per band. Use only the values in "Data Colors" (the subject #1a70c2, the rest gray; red #d42f37
only for a second channel beside blue), the formats in "Numbers, Dates & Units" and the components in "Component
Stylings". No photos, logos or shadows. Every chart and list needs a tooltip, keyboard control and a screen-reader table.
Before you finish, run the checklist at the end of "Agent Prompt Guide" and fix anything that fails.
```

## 2. 새 대시보드 (한국어)

```
DASHBOARD.md를 읽고 그대로 따라 줘. <회사>의 주간 <운영·매출> 보고를 가상 데이터로 HTML 파일 하나에 만들어 줘.
명세가 말하는 흰 화면으로, 한국어·영어를 한 파일에서 ?lang=ko|en으로 바꾸고 기본은 영어야.
맨 위에 이번 주와 진행 중인 행사 기간을 적은 파란 #005dab 공지 띠, 보고서 이름·기간·EN/KO 토글·테두리만 있는
PDF로 내보내기·파란 마크다운으로 복사가 있는 #fafafa 머리, 모든 그림에 함께 적용되고 주소에도 남는 <지역·매장·사업부>
파란 띠, 보고 현황을 초록으로 적은 #fafafa 상태 줄을 둬.
첫 문장은 매출 보도자료처럼("11월 1일까지 한 주 순매출은 X로, 지난해 Y보다 n% 늘었습니다"), 그 아래 둘째 지표와
계획 대비를 적은 문장, 그리고 가격표 6장: 번호, 굵은 이름, $와 소수부를 위첨자로 올린 큰 값, 좋은 변화인지로 색을
정한 증감, 작은 글씨 줄(계획, 단위당 값이나 비율)과 날짜 코드.
그 옆에는 고정폭 글꼴의 계산대 영수증으로 상세를 보여 줘: <부서·카테고리>마다 크기를 보여 주는 바코드 줄무늬 막대,
줄을 더하면 맞도록 반올림한 천 달러 값, 감소는 주황인 전년비, 이어서 소계와 **** 합계, 판매 수량, 영수증 바코드
자리에는 <시간대별 구매 건수 같은 시간 분포>. 두 단의 아래 끝을 맞춰 줘.
그다음 숯색 #333333 띠와 괘선 블록: 계획 대비 <매장·사업부> 순위(계획선에서 갈라지는 막대, 계획 미달은 #bc4700,
나머지는 #cccccc), 이번 주까지 계획선을 그은 100칸 랙으로 쌓은 <재고·용량>, 예측 대비 사용을 보여 주는 쿠폰 괘선
격자, 나머지는 표준 선·막대.
모든 그림은 같은 흰 카드(1px #d9d9d9)에: 그림 번호 → 결과를 말하는 제목 → 부제 → 범례 → 그림 → "주:".
한 띠에 그림은 7개 이하. 색은 "Data Colors" 값만(주인공 #1a70c2, 나머지 회색, 빨강 #d42f37은 파랑 옆의 둘째 경로에만),
숫자·날짜는 "Numbers, Dates & Units"(한국어는 만·건·%p, 돈은 회사의 통화), 부품은 "Component Stylings"를 따라 줘.
사진·로고·그림자는 넣지 마. 모든 차트와 목록에 툴팁, 키보드 조작, 스크린 리더용 표를 넣고, 끝내기 전에
"Agent Prompt Guide"의 점검 목록을 확인해서 안 맞는 건 고쳐 줘.
```

## 3. Restyle an existing screen

```
Read DASHBOARD.md. Restyle the dashboard in <file> to match it without changing its data:
- the frame to costco.com's: a blue #005dab promo band, a #fafafa header, a blue band as the one filter, a #fafafa
  status row; sections under charcoal #333333 bands with white 22px/700 headings and ruled #eeeeee blocks;
- every view onto the same white card (1px #d9d9d9, no radius, no shadow): an uppercase figure label, a title that states
  the finding, a subtitle with the measure, keys only where labels cannot work, and a note that starts with "Note:";
- the KPIs to price signs (a 1px #333333 frame, code, caps name, a big value with superscript $ and decimals, a signed
  change, a fine-print line, a date code), with plan beside last year where there is one;
- detail tables to the register receipt: monospace lines, a barcode-striped bar for each size, values rounded to a
  readable unit so the lines add up, negatives in #bc4700, SUBTOTAL and **** TOTAL;
- colors to the tokens: the subject #1a70c2 only where the title points, red #d42f37 only for a second channel beside it,
  the rest #cccccc, comparisons dashed #909090, shortfalls #bc4700; #005dab only on bands, buttons and links;
- rankings against a target to a board with bars from the plan line, and shares of a stock to 100-slot racks;
- gridlines solid #eeeeee on rows only, line ends labeled;
- number formats to "Numbers, Dates & Units" (true minus, pts / %p, $K in tables, M / 만 in signs and sentences).
Where the screen breaks a rule in "Do's and Don'ts" (dual axis, pie, donut or gauge, gradients, shadows or rounded cards,
photos or logos, cents in a table of millions, a card that is mostly blue, cards side by side that end on different
lines, more than seven views in a band), fix it and list what you changed.
```

## 4. Review a dashboard against the spec

```
Read DASHBOARD.md. Review <file or screenshot> against it and report, as a table: rule, what the screen does,
severity (must fix / should fix / fine), and the fix.
Cover: the headline states the result as a sales release; price signs with signed, good/bad-colored changes and plan;
one card anatomy for every view; finding titles and "Note:" notes; blue only where the title points and gray for the
rest; no #005dab or logo red on data; shortfalls in #bc4700 and never red; whether every device reads at least as well as
a plain bar or table (readable units, totals that add up, bars beside sizes); plan and the exceptions shown and ranked;
the chart form for each question; row gridlines and labels instead of legends; no dual axis; number, date, hour and
money formats in both languages; contrast and second cues for light marks; tooltips, keyboard and data tables; views
per band; cards in a row ending on one line; density at 1440 × 810 and 390px.
```

## 5. Reproduce Figure 1 of the sample

```
Read DASHBOARD.md and follow it exactly. Draw Figure 1 from comps.csv (columns: week_ended, region,
comparable_sales_reported_pct, comparable_sales_adjusted_pct; region is "all", "west", "central" or "east") for "all",
as one HTML file with an SVG chart on a white card (1px #d9d9d9, no radius) on a white page.
1. Frame: solid #eeeeee gridlines on rows only, the lowest one #cccccc, y ticks in % from 3% to 8% in 12px #707070, and
   four week ticks (08/09, 09/06, 10/04, 11/01) with the last week in #333333.
2. Comparison first: comparable_sales_reported_pct as a dashed #909090 line, 2px, dash 6 4.
3. The subject: comparable_sales_adjusted_pct as a solid #1a70c2 line, 2.5px, a hollow marker on the last week.
4. Label both line ends with name and value ("Adjusted* 5.4%" with the name in #004c8a, "Reported 6.2%" with the name
   in #333333, values in #333333, 12px/700); no legend.
5. Title with the finding ("Adjusted comparable sales rose 5.4%, in line with the 13-week average of 5.4%") and the note
   "*Excluding the impacts from changes in gasoline prices."
Add a tooltip (white, 1px #cccccc, 3px radius, shadow 0 0 5px rgba(0,0,0,.3)) that shows both values and the gas price
impact in pts, keyboard control and a screen-reader table, then list which checks in "Agent Prompt Guide" pass.
```

## Tableau (for people)

1. Paste the `<color-palette>` elements from `costco.tps` into `My Tableau Repository/Preferences.tps` and restart Tableau Desktop. Assign the subject first so it takes blue; a second channel takes red, the rest take the Other gray.
2. Dashboard background `#ffffff`. The header in a `#fafafa` container; the region filter as a single-value list in a `#005dab` container with white text; section bands as text objects on `#333333` with white bold text. Each sheet sits in a container with a 1px `#d9d9d9` border and 18/22px inner padding; tooltips white with a `#cccccc` border.
3. Sheet title: the finding, bold, `#333333`; a subtitle line with the measure in `#5f5f5f`; the caption starts with `Note:`. A text object above holds the figure label in Tableau Book 9 bold, uppercase, `#707070`.
4. Price signs: text sheets in containers with a 1px `#333333` border — the code small and gray, the name in bold caps, the value at 36–40pt bold (write `$51.46M`; Tableau cannot raise the cents), the change in `#0b6e22` or `#bc4700` with ▲ or ▼.
5. Receipt: a text table in a monospace font with `$K` (format `#,##0,`) and `VS LY%` (negatives in `#bc4700`), beside a thin bar sheet in `#333333`, the title's row in `#1a70c2`. Tableau has no pattern fills, so the barcode bar becomes a plain bar. Transactions by hour: bars of hour inside day, both discrete, small, `#333333`, no axis.
6. Warehouse board: bars of vs plan sorted descending, a reference line at 0 in `#333333`, Color by `vs plan < 0` (`#bc4700` / `#cccccc`), labels at the bar ends. Racks: a 100-row scaffold per category, `X = INT((INDEX()-1)/5)`, `Y = (INDEX()-1) % 5`, Color by state, a reference line at the plan's bay.
7. Grid lines: rows only, solid, `#eeeeee`; zero line `#cccccc`; no axis rulers; ticks `#707070`. Comparisons as dashed lines in `#909090`.
8. Number formats: `$#,##0.00,,"M"` · `#,##0,` for `$K` · `#,##0` · `0.0%` · `+0.0" pts";−0.0" pts"`; Korean workbooks `#,##0.00"달러"` · `+0.0"%p";−0.0"%p"`. Fonts: Tableau Book unless Barlow is installed on every viewing machine and on the server.

## Power BI (for people)

1. View → Themes → Browse for themes → `powerbi-theme.json`. Visuals come out white with a 1px `#d9d9d9` border and no radius on a white page.
2. The first two data colors are blue (the subject) and red (a second channel), then the Other gray; the colors after it exist only because Power BI wants a longer list. The UI blue `#005dab` and the logo red are not in the list on purpose.
3. Install Barlow on authoring and viewing machines, or accept the Segoe UI fallback.
4. Title each visual with the finding and put the measure in the subtitle; gridlines solid `#eeeeee`; data labels on the last point; legends off when labels name the series.
5. Price signs: cards with a `#333333` border, change measures with conditional formatting in `#0b6e22` / `#bc4700` only, always with a sign. Receipt: a table visual in a monospace font, display units in thousands, data bars in `#333333` on the sales column, VS LY in `#bc4700` below zero. Warehouse board: a bar chart of vs plan with a constant line at 0 and `#bc4700` below it.
