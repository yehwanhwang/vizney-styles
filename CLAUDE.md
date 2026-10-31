# Vizney Styles 제작 지침

이 저장소는 styles.vizney.com(GitHub Pages, `main` 브랜치)으로 배포된다. 기업의 공개 웹사이트에서 읽어 낸 룩을 대시보드용 명세 **DASHBOARD.md**로 만들어 카탈로그에 쌓고, 같은 패키지를 기업에 비공개로 만들어 주는 것이 사업이다. 대상은 기업(해외 중심, 국내 포함)이고, 블로그(kr.vizney.com, www.vizney.com)의 Gallery 포스트로 소개한다. 목적은 실제 데이터 분석이 아니라, AI 코딩 에이전트·Tableau·Power BI가 그대로 따를 수 있는 '우리 회사 대시보드 룩'을 전달하는 것이다.

**한 브랜드에 패키지 하나.** `<name>/` 폴더에 DASHBOARD.md, 참고 화면(`index.html`), 토큰 원본(`tokens.json`)과 거기서 생성한 `tokens.css`·`<name>.tps`·`powerbi-theme.json`, 프롬프트(`prompt.md`), 만드는 법 섹션이 그리는 그림의 데이터(예: `orders.csv`), 커버(`cover-en.png`, `cover-ko.png`)가 들어간다. 명세로 적은 것, 화면에서 보이는 것, 도구 파일의 값이 모두 같아야 한다.


## 핵심 약속: AI 대시보드가 어색한 이유 8가지

카탈로그의 모든 화면과 명세는 이 여덟 가지를 지킨다. 이것이 Dribbble의 그림이나 DESIGN.md 생성기와 다른 점이다.

1. **브랜드 가이드는 대시보드를 모른다.** 대표색은 로고와 포인트에 남기고, 데이터 색은 따로 설계한다.
2. **차트 선택.** 질문에 맞는 차트. 도넛·이중 축·무지개 범주 금지.
3. **정보 위계.** 한 역할의 한 질문. 결과를 말하는 머리, 그 근거인 카드.
4. **숫자와 언어.** 억·만·건·%p와 ₩·M·K·pts, 반올림, 부호, 날짜를 규칙으로 적는다.
5. **색 검증.** 색각 이상 구분·일반 시각 구분·대비를 계산으로 검사한 조합만 쓴다.
6. **실제 환경의 밀도.** 노트북(1366~1440)에서 머리와 KPI 줄이 첫 화면에 들어온다.
7. **수백 장의 일관성.** 한 장이 아니라 규칙을 적는다. 명세만 보고 같은 화면을 다시 만들 수 있어야 한다.
8. **도구로의 번역.** 웹 CSS, Tableau 팔레트·서식, Power BI 테마로 바로 들어간다.


## 새 브랜드를 만드는 순서

1. **읽기:** 공개된 사이트의 실제 CSS 토큰(색, 서체 크기, 간격, 모서리)을 브라우저로 읽는다(연결된 컴퓨터의 내장 브라우저에서 `getComputedStyle`로 계산값을 뽑는다). 추정값보다 실제 값을 우선한다. 브랜드의 포인트 색 하나와 회색 사다리를 그대로 쓴다. 로고, 워드마크, 심벌, 자체 서체(오픈 서체로 대체), 사진·일러스트, 실제 문구와 데이터는 가져오지 않는다.
2. **패턴 인벤토리:** 토큰만으로는 색과 서체만 입힌 템플릿이 된다. 기업이 **즐겨 쓰는 구성과 부품**을 페이지에서 읽어 목록으로 적는다: 머리 구조, 버튼 종류(모양·높이·채움·호버), 카드 해부(눈썹 → 제목 → 문장 → 행 → 버튼), 표(괘선, 주인공 열, 그룹 행, 결측 표기), 숫자·날짜 표기, 리스트 페이지의 카운터와 정렬 UI, 툴팁·배지·세그먼트. 그 기업이 **차트를 발행하면**(리서치·IR·블로그·발표 자료) 그 차트 문법(제목 쓰는 법, 캡션, 색, 선 끝 라벨, 기준선, 격자)이 일반 규칙보다 우선한다. 한국어 페이지가 있으면 거기서 쓰는 한국어 서체를 쓴다. 화면 구성은 '화면 규칙'의 기본 틀이 아니라 이 인벤토리의 부품으로 짠다. 기본 틀은 인벤토리가 빈약할 때의 폴백이다.
3. **데이터 색 설계:** 브랜드가 차트에 쓰는 색상군이 있으면 그 색상군에서, 없으면 포인트 색과 보조 스와치에서 범주(최대 3 + 회색 기타), 비교(회색 점선), 순차(5단계), 발산(7단계), 상태(좋음·나쁨) 색을 만들고, dataviz 스킬의 `validate_palette.js`로 플롯 면과 카드 면 기준 검사를 통과시킨다(범주는 기본, 순차·발산 팔은 `--ordinal`). 로고와 UI의 대표색은 데이터 색으로 쓰지 않는다(약속 1). 브랜드가 자기 차트에서 주인공에 따로 쓰는 색이 있으면(예: Anthropic 차트의 주황. 대표색 클레이와 다른 색이다) 그 색을 주인공 계열로 쓰고 나머지는 회색으로 물린다. 선 끝 라벨처럼 글자에 쓰는 색은 같은 색상군의 더 짙은 단계로 4.5:1을 맞춘다. 결과와 수치를 `tokens.json`의 `data.validation`에 적는다.
4. **샘플 설계:** 샘플의 회사는 지어낸 이름 대신 Vizney의 가상 사업부로 쓰고(예: Vizney Logistics · 비즈니 로지스틱스), 데이터는 가상이다. 그 회사 제품 화면처럼 읽히지 않는 업무 보고 하나를 정한다(예: 배송 회사 운영 보고). 지역·지점은 해외 독자가 알아보는 미국 지명으로 쓰고(예: California · Texas · Washington, Los Angeles · Houston · Seattle), 돈은 그 회사의 통화(미국 달러)로 쓴다. 대상 기업의 이름을 비튼 회사 이름은 쓰지 않는다(고지와 부딪힌다). 만드는 법 섹션이 그리는 그림 하나의 데이터는 CSV로 패키지에 넣는다. 합계·비율·증감이 서로 맞는지 Python으로 검산하고, 필터의 모든 선택지마다 모든 카드의 숫자가 맞아야 한다. 토큰을 보여 주려고 끼워 넣는 카드(색상표, 서체 견본)는 만들지 않는다. 모든 카드는 보고서에 필요한 내용이어야 하고, 스타일은 부품과 문법으로 드러난다. 사진은 쓰지 않고 색 블록을 쓴다.
5. **세 단어:** 부제는 세 단어다. 단어마다 첫 글자를 대문자로 쓰고 쉼표로 이으며 마침표는 붙이지 않는다("Ivory, Editorial, Quiet" · "아이보리, 에디토리얼, 고요함"). 한두 단어는 사람들이 검색하는 말, 하나는 분위기 단어로 고르고, 다른 스타일과 겹치지 않는 단어를 하나 이상 넣는다. 영어와 한국어는 직역하지 않는다. 해시태그는 SNS 캡션에만 쓴다.
6. **구현:** 아래 '화면 규칙'대로 `<name>/index.html`을 만든다.
7. **검증:** 아래 '검증'을 모두 통과시킨다.
8. **명세와 패키지:** `tokens.json`을 쓰고 `python3 tools/package.py <name>`으로 `tokens.css`, `<name>.tps`, `powerbi-theme.json`, DASHBOARD.md 머리를 만든다. DASHBOARD.md 본문과 `prompt.md`를 쓴다(아래 '명세 형식').
9. **커버:** `python3 tools/shots.py <name>`으로 `cover-en.png`, `cover-ko.png`(1440×810, 2배)를 만든다. 홈 카드, 포스트 대표 이미지, 링크 미리보기에 쓴다.
10. **README와 홈:** README의 Catalog 표에 행을 추가하고, 홈(`index.html`)에 카드를 넣는다(아래 '홈 페이지').
11. **배포:** 작업 브랜치 → 커밋 → PR → 머지. GitHub Actions의 'pages build and deployment'가 성공했는지로 배포를 확인한다. `main`에 올라간 것은 바로 공개된다.
12. **포스트 초안:** 아래 '포스트 형식'으로 한국어·영어 전문과 SNS 캡션을 대화창에 바로 준다(Claude Docs는 쓰지 않는다).

번호는 공개 순서대로 하나로 매긴다(01 Anthropic). 요청은 GitHub 이슈 템플릿(`.github/ISSUE_TEMPLATE/request.yml`)으로 받고 👍 투표 순으로 고른다. BI 벤더(Tableau, Microsoft, Google, Qlik 등)와 그 계열사의 스타일은 만들지 않는다. 해당 기업이 요청하면 폴더와 포스트를 내린다.


## 고지

Materials 시리즈는 없다. 모든 스타일은 기업 이름을 쓰므로 세 곳에 고지를 둔다: 샘플 화면 하단(임베드에서는 숨김), DASHBOARD.md 머리, 포스트 끝. 문구: "Anthropic의 공식 디자인이 아니며 제휴·승인 관계가 없습니다. 공개된 웹사이트(anthropic.com, claude.com)에서 보이는 디자인을 읽어 낸 참고용 스타일이며 로고·서체·데이터는 포함하지 않습니다. 상표는 각 소유자의 것입니다." 이름은 "Anthropic 스타일" · "Anthropic style"처럼 설명형으로만 쓰고, 화면에 브랜드 이름을 워드마크처럼 크게 세우지 않는다. 화면의 회사는 Vizney의 가상 사업부이고 숫자는 가상이다. 대상 기업의 실제 데이터처럼 보이게 하지 않는다.


## 화면 규칙

- **가로형 실제 업무 대시보드**다. 최대 폭 1400px(여백 32px, 1359px 이하 24px, 639px 이하 16px). 구성은 패턴 인벤토리에서 고른 부품으로 짜되 늘 들어가는 것이 있다: 머리(샘플 회사 이름과 보고서 이름, 기간, EN/KO 토글), 필터 한 줄(아래 모든 카드에 적용), 결과를 말하는 머리 문장, 그 근거인 카드들, 상세 표, 만드는 법(패키지 파일 목록, 화면의 그림 하나와 DASHBOARD.md 점검 목록, 그 그림을 그리는 JS·Python·Tableau·Power BI·프롬프트 코드 창. 처음 보일 때 코드가 한 줄씩 쳐지며 그림이 층별로 그려진다. 받는 것과 의뢰하는 법을 보여 주는 자리다), 바닥(카탈로그 줄 `Vizney Styles · 01 · Anthropic style Ivory, Editorial, Quiet`, 샘플 안내, 고지). 인벤토리가 빈약한 브랜드의 폴백 틀은 12열 그리드(KPI 4장, 추세 7 + 목록 5, 카드 3장) → 상세 표다. 예: Anthropic은 그 회사가 실제로 발행하는 그림의 종류(모델 발표의 비용·성능 그림과 비교표, 리서치 글의 계단선·오차 막대·덤벨·점 단위 설문)를 골라, 하나의 카드와 하나의 차트 문법으로 다시 그렸다(01 개요 · 02 운영 · 03 만드는 법).
- **한 문법, 한 화면에 그림 7개 이하.** 참고한 그림(발표 자료, 리서치 글 등)은 형식만 가져오고 붙여 넣지 않는다. 모든 그림과 표는 같은 카드에 같은 해부(그림 번호 → 결과를 말하는 제목 → 부제 → 범례 → 그림·표 → 주석)로 넣고, 색·선·축·툴팁도 한 가지로 맞춘다. 화면 묶음(절)마다 그림은 7개 이하이고, 에이전트나 BI 도구가 템플릿으로 다시 만들 수 있는 표준 그림만 쓴다.
- HTML 파일 하나로 완결한다(데이터 포함). 외부에서 불러오는 것은 글꼴뿐이다(Google Fonts와 jsDelivr만).
- 서체: 본문 서체는 언어마다 하나. 영어는 브랜드 서체를 대신할 오픈 라틴 서체, 한국어는 브랜드의 한국어 페이지가 쓰는 서체(없으면 Pretendard). 디스플레이 서체를 쓰면 언어마다 하나씩(예: Source Serif 4 · Noto Serif KR). 숫자용 고정폭은 스타일의 특징일 때만. 화면에 서체 이름을 보여 줄 때도 그 언어의 서체만 쓴다.
- `<head>`에 robots, 글꼴 링크, embed.js를 넣는다:

  ```html
  <meta name="robots" content="noindex">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;1,8..60,400&display=swap">
  <!-- 한국어 서체가 Pretendard일 때: https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css -->
  <script src="/lib/embed.js" defer></script>
  ```

- 한국어·영어를 한 파일에서 `?lang=ko|en`으로 전환하고 화면에도 EN/KO 토글(EN이 앞)을 둔다. 기본은 영어다. 포스트 임베드와 링크에는 `lang`을 늘 적는다.
- 숫자는 한국어에서 억·만·건·부·%p, 영어에서 M·K·pts로 쓰고, 돈은 샘플 회사의 통화로 쓴다(미국 달러: `$7.85` · `7.85달러`). 단위와 접미사는 숫자보다 작게 쓴다. 부호는 진짜 마이너스(−)다.
- KPI 카드: 글자 크기는 대표 수치와 나머지 두 단계만 쓴다. 지표명 → 수치 → 증감 순서로 두고, 같은 줄 카드의 수치 높이가 맞게 한다(subgrid). 증감 색은 값이 움직인 방향이 아니라 그 지표에서 좋은 변화인지로 정한다.
- 카드 안에 다시 카드를 넣지 않는다. 다크 모드는 만들지 않는다. 필터는 화면 위 한 줄에 두고 아래 모든 카드에 함께 적용한다.
- 차트: 이중 축 금지. 범주 색은 세 가지와 회색 '기타'까지. 텍스트에 데이터 색을 쓸 때는 4.5:1을 넘는 글자용 단계만 쓴다. 쉬는 상태에서는 선 끝에 값을 적고, 툴팁은 호버·키보드에서만 띄운다. 모든 차트에 호버 툴팁, 키보드 조작(방향키, Home, End, Esc, 라이브 리전), 스크린 리더용 표를 둔다. `prefers-reduced-motion`이면 애니메이션을 끈다.
- 임베드 모드(`?embed=1`이면 `<html>`에 `vz-embed`): 화면 높이 기준 레이아웃을 풀고 바닥 안내를 숨긴다. 포스트에는 넓은 카드로 원래 크기 그대로 넣는다.
- 반응형: 1024~1359 같은 구성에 여백만 줄임, 900~1023 추세·목록 세로 쌓기, 640~899 2열(KPI 2×2), 640 미만 1열(KPI는 2×2 유지). 표는 좁은 폭에서 열을 줄인다.


## 검증

- 1440, 1200(블로그 넓은 폭), 1024, 390px에서 한국어·영어 화면을 캡처해 겹침, 잘림, 들쭉날쭉한 줄바꿈이 없는지 눈으로 확인한다. `python3 tools/shots.py <name> --review <저장소 밖 폴더>`가 네 폭의 전체 화면을 찍고 가로 넘침을 알려 준다.
- 필터의 모든 선택지에서 모든 카드가 바뀌고 검산 값과 같은지, 호버·키보드가 동작하는지, 언어 전환에서 언어별 서체만 쓰이는지, 페이지 오류가 없는지 확인한다.
- 다른 출처의 부모 페이지에 임베드 코드를 넣고 iframe 높이가 내용에 맞는지 확인한다(넓은 폭, 좁은 폭, 모바일, 창 크기 변경, 한 페이지에 두 개).
- 데이터 색은 `validate_palette.js`를 통과해야 한다. 검사 결과를 DASHBOARD.md의 Data Colors에 적는다. 경쟁사·기타처럼 일부러 회색인 계열은 채도 검사 대상이 아니고, 옆의 색과 구분되는지만 본다.
- 만드는 법 섹션: 처음 화면에 들어올 때 코드가 한 줄씩 쳐지며 그림 층과 점검이 차례로 나타나는지, 치는 중에 탭·필터·언어를 바꿔도 깨지지 않는지, 움직임 줄이기와 캡처에서는 완성된 상태로 보이는지 확인한다.
- 샌드박스에서 글꼴 CDN이 막히면 `tools/shots.py`에 `--offline-fonts <저장소 밖 폴더>`를 붙인다. 다른 검사 스크립트도 같은 파일의 `OfflineFonts`를 Playwright 컨텍스트에 붙이면 된다.


## 명세 형식 (DASHBOARD.md)

- DESIGN.md 형식과 호환되게: YAML 머리(토큰)와 본문 섹션. 머리는 `tools/package.py`가 `tokens.json`에서 다시 쓰므로 손으로 고치지 않는다.
- 제목 `# <Name> style — DASHBOARD.md`, 영어 세 단어 · 한국어 세 단어, 한 단락 소개(무엇을 담은 파일인지), 라이브 샘플·원본(raw) 주소·같은 폴더의 파일 링크·카탈로그 번호, 고지 한 단락.
- 섹션 순서: Visual Theme & Atmosphere · Color Palette & Roles · Data Colors · Typography Rules · Numbers, Dates & Units · Layout Principles · Component Stylings · Charts · Depth & Elevation · Interaction & Motion · Accessibility · Responsive Behavior · Tool Mapping · Do's and Don'ts · Agent Prompt Guide.
- 이름만 듣고 같은 스타일을 다시 만들 수 있을 만큼 구체적으로 쓴다. 영어로 쓰되 숫자·날짜 규칙은 한국어 표기도 적는다. 사이트에서는 `<name>/DASHBOARD.html`로 열린다.
- `prompt.md`: 새 대시보드(영어·한국어), 기존 화면 고치기, 명세로 검토하기, 샘플 그림 하나 다시 그리기 프롬프트와 Tableau·Power BI 적용 메모.
- `tokens.json`: 색(토큰·용도), 데이터 색과 검증 결과, 서체(언어별)와 크기 체계, 모서리, 간격, 레이아웃, 움직임, 도구 메모. 값을 바꾸면 `package.py`를 다시 돌린다.


## 포스트 형식

- SEO 제목: `<Name> 대시보드 스타일 — <세 단어>` / `<Name> Dashboard Style — <Three, Words>`. 메타 설명은 145자 안팎으로 따로 쓴다.
- 발췌문: 생김새를 말하는 한 문장과 샘플 한 문장. 메타 설명과 대표 이미지 대체 텍스트에도 세 단어를 넣는다.
- 첫 문장은 바로 스타일 설명으로 시작한다. 이어서 DASHBOARD.md가 무엇인지(에이전트·Tableau·Power BI에 넣는 파일) 한두 문장, 샘플과 조작 방법 한두 문장.
- 순서: HTML 카드(아래 임베드 코드) → `### Design`(불릿 3~4개) → `### DASHBOARD.md`(파일 링크, 받는 것, 프롬프트 예시 코드 블록) → 우리 회사 것 제작 문의 링크(https://kr.vizney.com/contact-us/, https://www.vizney.com/contact-us/)와 브랜드 요청 링크 → 고지 한 단락.
- 태그 Gallery, Brand Styles. 슬러그 `style-<name>`. 대표 이미지 cover-ko.png / cover-en.png.
- SNS 캡션(링크드인 중심): 스타일 한 문장, 라이브 샘플 링크, 고지 한 줄, 세 단어 해시태그와 #VizneyStyles #DashboardDesign · #대시보드디자인.
- Tableau를 대체하는 이야기로 읽힐 표현은 쓰지 않는다. Tableau 적용 파일은 Tableau를 더 잘 쓰게 하는 것이다.


## 임베드 코드

한국어 포스트의 HTML 카드(넓은 카드, 원래 크기):

```html
<figure class="kg-card kg-embed-card kg-width-wide">
  <iframe data-vizney-embed src="https://styles.vizney.com/<name>/?lang=ko&amp;embed=1" title="<Name> 스타일 대시보드" loading="lazy" style="display:block;width:100%;height:820px;border:1px solid #e6e6e6;border-radius:12px"></iframe>
  <figcaption><a href="https://styles.vizney.com/<name>/?lang=ko" target="_blank" rel="noopener">전체 화면으로 보기 ↗</a></figcaption>
</figure>
<script src="https://styles.vizney.com/lib/embed-host.js" defer></script>
```

영어 포스트는 `lang=en`, 제목 "<Name> style dashboard", 링크 문구 "Open full screen ↗"로 바꾼다.


## 홈 페이지

- 루트의 `index.html`이 첫 화면이다. 머리(문제와 약속), 카탈로그, AI 대시보드가 어색한 이유(전후 비교), 받는 것과 진행 순서, 문의·요청. 한국어·영어를 `?lang=ko|en`과 토글로 바꾸고 기본은 영어다. 없는 주소에는 `404.html`이 보인다. 둘은 머리글·바닥글·CSS·`STR`이 같으므로 한쪽을 고치면 다른 쪽도 맞춘다.
- 새 카드: 기존 `article.swatch`를 복사해 '우리 회사' 카드 앞에 두고, 번호와 이름(`01 Anthropic`), 폴더, 링크(샘플, DASHBOARD.md, 파일, 소개 글)를 바꾼다. `STR` 한국어·영어에 `sub_<name>`(세 단어)과 `meta_<name>`(샘플 설명)을 더한다.
- 화면 문구는 `STR`이 기준이고, 본문의 영어 문구와 링크는 스크립트 없이 읽힐 때의 기본값이므로 둘 다 고친다. `<head>`의 제목·설명·`og:` 메타도 영어로 쓴다.
- 머리글·버튼·바닥글, 색 값과 글꼴은 Vizney Blocks(blocks.vizney.com)에 맞춘다. 글꼴은 VZ Sans(Spoqa Han Sans Neo 부분 글꼴, SIL OFL). 두 페이지의 문구를 고치거나 카드를 더하면 `python3 tools/font.py <spoqa-han-sans 저장소>/Original/SpoqaHanSansNeo`로 `assets/fonts/`를 다시 만든다. 글꼴 주소의 `?v=`도 함께 바뀐다.
- 사이트 마크(Blocks의 2×2 블록에서 위 두 칸을 합친 모양)는 머리글, `favicon.svg`, `og.png`에만 쓰고 샘플 화면에는 넣지 않는다. `sitemap.xml`에는 홈만 넣고 샘플 화면은 `noindex`다.


## 저장소 규칙

- 공개된 스타일의 폴더 이름은 바꾸지 않는다(포스트 임베드가 깨진다). 고칠 때는 같은 주소에서 고치고 이력은 Git이 보관한다.
- `lib/embed.js`, `lib/embed-host.js`는 발행된 포스트가 쓰므로 이전 동작과 호환되게 고친다.
- 생성 파일(`tokens.css`, `.tps`, `powerbi-theme.json`, DASHBOARD.md 머리)은 손으로 고치지 않고 `tokens.json`을 고친 뒤 `package.py`를 돌린다.
