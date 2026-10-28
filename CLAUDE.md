# Vizney Styles 제작 지침

이 저장소는 styles.vizney.com(GitHub Pages, `main` 브랜치)으로 배포된다. 대시보드의 '느낌'을 이름 붙은 스타일로 만들어 쌓고, 블로그(kr.vizney.com, www.vizney.com)의 Gallery에 소개한다. 목적은 실제 데이터 분석이 아니라 스타일 전달이다.


## 새 스타일을 만드는 순서

1. **레퍼런스 읽기:** 사용자가 첨부한 이미지에서 스타일(색, 카드 모양, 레이아웃, 차트 표현)만 가져온다. 브랜드명, 로고, 인물 사진, 문구, 데이터는 가져오지 않는다. 출처는 표기하지 않는다. (브랜드 시리즈는 아래 '브랜드 시리즈'를 따른다.)
2. **샘플 화면 설계:** 스타일이 잘 드러나는 업무 화면 하나를 정한다(예: 온라인몰 주문 분석). 가상 브랜드명과 가상 데이터를 쓰고, 합계·비율·증감이 서로 맞는지 계산으로 확인한다.
3. **이름과 부제:** 질감 시리즈는 재료·질감을 떠올리게 하는 영단어 하나로 이름 후보 2~3개를 제안하고 사용자가 고른다. 브랜드 시리즈는 브랜드 이름이 곧 스타일 이름이다. 'Vizney'는 붙이지 않는다(Vizney Styles는 묶음 이름이다). 부제는 생김새를 말하는 한 줄이다(예: "Dark sidebar, pastel KPI tiles · 다크 사이드바와 파스텔 KPI 카드").
4. **구현:** 아래 '화면 규칙'을 따라 `<name>/index.html`을 만든다.
5. **검증:** 아래 '검증'을 모두 통과시킨다.
6. **명세:** `<name>/style.md`를 쓴다(아래 '명세 형식').
7. **대표 이미지:** `<name>/cover-ko.png`, `<name>/cover-en.png`를 만든다. 1440×810 화면을 2배 해상도로 캡처하고, 페이지 하단 안내 문구는 숨긴다.
8. **README와 홈:** README의 Styles 표에 행을 추가하고, 홈(`index.html`)에 스타일 카드를 넣는다(아래 '홈 페이지'). 블로그 링크는 `/style-<name>/`이다.
9. **배포:** 작업 브랜치 → 커밋 → PR → 머지. GitHub Actions의 'pages build and deployment'가 성공했는지로 배포를 확인한다. `main`에 올라간 것은 바로 공개된다.
10. **포스트 초안:** 아래 '포스트 형식'으로 한국어·영어 전문을 대화창에 바로 준다(Claude Docs는 쓰지 않는다).


## 브랜드 시리즈

스타일은 두 시리즈로 나뉜다. 질감 시리즈(Chalk, Glass, Tile)는 재료 이름을 쓰고 우리 고유의 룩을 보여 준다. 브랜드 시리즈(Anthropic)는 getdesign.md(awesome-design-md)처럼, 공개된 기업 웹사이트에서 읽어 낸 룩을 그 기업 이름으로 올린다. 브랜드 시리즈는 다음을 따른다.

- **이름:** 흔히 쓰는 브랜드 이름 그대로(Anthropic (앤트로픽)). 폴더는 소문자(`anthropic/`), 포스트는 `style-anthropic`. 이름은 "Anthropic 스타일"처럼 설명적으로만 쓰고 제품명처럼 쓰지 않는다.
- **읽는 법:** 공개된 사이트의 실제 CSS 토큰(색, 서체 크기, 간격, 모서리)을 브라우저로 읽는다. 추정값보다 실제 값을 우선한다. 브랜드의 포인트 색 하나와 회색 사다리를 그대로 쓰고, 차트 범주색은 브랜드 팔레트에 가까운 색으로 `validate_palette.js`를 통과하는 조합을 찾는다.
- **쓰지 않는 것:** 로고, 워드마크, 심벌, 자체 서체(오픈 서체로 대체), 사진·일러스트, 실제 문구와 데이터. 샘플은 가상 회사와 가상 데이터로 만들고, 그 회사 제품 화면처럼 읽힐 주제는 피한다.
- **출처와 고지:** 질감 시리즈와 달리 출처(공개 사이트 주소)를 명세 머리에 적는다. 샘플 화면 하단(임베드에서는 숨김), style.md 머리, 포스트 끝에 고지를 둔다: "Anthropic의 공식 디자인이 아니며 제휴·승인 관계가 없습니다. 공개된 웹사이트(anthropic.com, claude.com)에서 보이는 디자인을 읽어 낸 참고용 스타일이며 로고·서체·데이터는 포함하지 않습니다. 상표는 각 소유자의 것입니다."
- **내리기:** 해당 기업이 요청하면 내린다. 폴더는 남기지 않고 포스트도 내린다.
- **제외:** BI 벤더(Tableau, Microsoft, Google, Qlik 등)의 스타일은 만들지 않는다. Tableau를 대체하는 이야기로 읽힌다.


## 화면 규칙

- HTML 파일 하나로 완결한다(데이터 포함). 외부에서 불러오는 것은 글꼴뿐이다. 스타일에 세리프나 모노가 필요하면 Google Fonts(Noto Serif KR, Source Serif 4, JetBrains Mono 등)를 한 줄 더 불러온다. 샌드박스에서는 fontsource/font-files 저장소를 부분 클론해 같은 방법으로 로컬 파일로 돌린다.
- `<head>`에 세 줄을 넣는다.

  ```html
  <meta name="robots" content="noindex">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/spoqa/spoqa-han-sans@v3.3.0/css/SpoqaHanSansNeo.css">
  <script src="/lib/embed.js" defer></script>
  ```

- 한국어·영어를 한 파일에서 `?lang=ko|en`으로 전환하고, 화면에도 KO/EN 토글을 둔다. 기본은 영어다(`lang`이 없거나 `ko`가 아니면 영어). 포스트 임베드와 링크에는 기본값에 기대지 않고 `lang`을 늘 적는다.
- 숫자는 한국어에서 억·만·건·원, 영어에서 ₩·M·K로 쓴다. 단위와 접미사는 숫자보다 작게 쓴다.
- KPI 카드: 글자 크기는 대표 수치와 나머지 두 단계만 쓰고 굵기와 색으로 구분한다. 증감은 수치 아래 줄에 두어 카드마다 수치 높이를 맞춘다. 증감 색은 값이 움직인 방향이 아니라 그 지표에서 좋은 변화인지로 정한다.
- 카드 안에 다시 카드(컨테이너)를 넣지 않는다. 다크 모드는 만들지 않는다.
- 필터(탭 등)는 화면 위 한 줄에 두고, 아래 모든 카드에 함께 적용한다.
- 차트: 이중 축은 쓰지 않는다. 범주 색은 세 가지와 회색 '기타'까지만 쓴다. 텍스트에는 데이터 색을 쓰지 않는다. 모든 차트에 호버 툴팁, 키보드 조작, 스크린 리더용 표를 둔다. `prefers-reduced-motion`이면 애니메이션을 끈다.
- 색은 dataviz 스킬의 `validate_palette.js`로 색각 이상 구분과 대비를 검사해서 통과한 조합만 쓴다.
- 임베드 모드(`?embed=1`이면 `<html>`에 `vz-embed` 클래스가 붙는다): `100vh` 같은 화면 높이 기준 레이아웃을 풀고, 페이지 전용 안내 문구를 숨긴다.


## 검증

- 1440, 1200(블로그 넓은 폭), 1024, 390px에서 한국어·영어 화면을 캡처해 겹침, 잘림, 들쭉날쭉한 줄바꿈이 없는지 눈으로 확인한다.
- 필터 전환, 호버, 키보드 조작이 동작하고 페이지 오류가 없는지 확인한다.
- 다른 출처의 부모 페이지에 아래 임베드 코드를 넣고, iframe 높이가 내용에 맞는지 확인한다(넓은 폭, 좁은 폭, 모바일, 창 크기 변경, 한 페이지에 두 개).
- 샌드박스에서 글꼴 CDN이 막히면 spoqa/spoqa-han-sans 저장소의 v3.3.0을 부분 클론해서 jsDelivr 요청을 로컬 파일로 돌려 확인한다.


## 명세 형식 (style.md)

- 제목은 이름만 쓴다(`# Chalk`). 그 아래 영어 부제 · 한국어 부제, 한두 문장 소개, 라이브 샘플과 명세 주소를 둔다. 브랜드 시리즈는 그 아래에 고지 한 단락을 둔다.
- 섹션: Layout, Color(토큰 표: 이름·Hex·용도), Type, Components, Motion and interaction, Don'ts.
- 이름만 듣고 같은 스타일을 다시 만들 수 있을 만큼 구체적으로 쓴다. 출처 섹션은 두지 않는다(브랜드 시리즈의 출처는 머리의 고지 단락에만 적는다).
- 사이트에서는 `<name>/style.html`로 열린다.


## 포스트 형식

- SEO 제목: `<Name> — <부제>의 대시보드 스타일` / `<Name>: A Dashboard Style with <subtitle>`
- 발췌문: 스타일 한 문장과 샘플 한 문장.
- 첫 문장은 바로 스타일 설명으로 시작한다: "<Name>는 …한 대시보드 스타일입니다." 이어서 샘플 데이터와 조작 방법을 한두 문장으로 쓴다.
- 순서: HTML 카드(아래 임베드 코드) → `### Design`(왜 이렇게 표현했는지 불릿 3~4개) → `### Prompt`(명세 링크와 요청 예시 코드 블록) → 제작 문의 링크(https://kr.vizney.com/contact-us/, https://www.vizney.com/contact-us/). 브랜드 시리즈는 맨 끝에 고지 한 단락을 더한다.
- 태그는 Gallery, 슬러그는 `style-<name>`, 대표 이미지는 cover-ko.png / cover-en.png.
- Tableau를 대체하는 이야기로 읽힐 표현(예: "BI 플랫폼 없이도")은 쓰지 않는다.


## 임베드 코드

한국어 포스트의 HTML 카드:

```html
<figure class="kg-card kg-embed-card kg-width-wide">
  <iframe data-vizney-embed src="https://styles.vizney.com/<name>/?lang=ko&amp;embed=1" title="<Name> 스타일 대시보드" loading="lazy" style="display:block;width:100%;height:820px;border:1px solid #e6e6e6;border-radius:12px"></iframe>
  <figcaption><a href="https://styles.vizney.com/<name>/?lang=ko" target="_blank" rel="noopener">전체 화면으로 보기 ↗</a></figcaption>
</figure>
<script src="https://styles.vizney.com/lib/embed-host.js" defer></script>
```

영어 포스트는 `lang=en`, 제목 "<Name> style dashboard", 링크 문구 "Open full screen ↗"로 바꾼다.


## 홈 페이지

- 루트의 `index.html`이 styles.vizney.com의 첫 화면이다. 스타일 카드와 회사 스타일 제작 소개를 담고, 한국어·영어를 `?lang=ko|en`과 KO/EN 토글로 바꾼다. 기본은 영어이고, 토글로 한국어를 고르면 주소에 `?lang=ko`가 붙고 영어로 돌아오면 빠진다. 없는 주소에는 `404.html`이 보인다. 둘 다 HTML 파일 하나로 완결하고 머리글·바닥글·CSS가 같으므로, 한쪽을 고치면 다른 쪽도 맞춘다.
- 새 스타일 카드: 기존 `article.swatch` 하나를 복사해 '우리 회사' 카드 앞에 두고 폴더 이름과 이름을 바꾼다. 페이지 스크립트의 `STR` 한국어·영어에 `sub_<name>`(부제)과 `meta_<name>`(샘플 설명)을 더한다. 첫 화면 라벨의 스타일 개수는 카드 수로 계산되니, 본문에 적힌 기본 문구의 숫자만 고친다.
- 화면 문구는 `STR`이 기준이다. 본문의 영어 문구와 링크(영어 블로그·`cover-en.png`)는 스크립트 없이 읽힐 때의 기본값이므로, 문구를 고칠 때는 둘 다 고친다. `<head>`의 제목·설명·`og:` 메타도 영어로 쓴다.
- 머리글·버튼·바닥글, 색 값과 글꼴은 Vizney Blocks(blocks.vizney.com)에 맞춘다. 본문 링크 밑줄(노랑 2px)만 Styles의 것으로 둔다.
- 홈과 404의 글꼴은 Blocks와 같은 VZ Sans다. Spoqa Han Sans Neo 원본(`Original/SpoqaHanSansNeo`)에서 두 페이지에 쓰인 글자만 담고 이름을 바꾼 부분 글꼴이다(SIL OFL, `OFL.txt`). 두 페이지의 문구를 고치거나 스타일 카드를 더하면 `python3 tools/font.py <spoqa-han-sans 저장소>/Original/SpoqaHanSansNeo`로 `assets/fonts/`를 다시 만든다. 글꼴 주소의 `?v=`도 함께 바뀐다. Spoqa CDN이 주는 `Subset` 폴더 글꼴은 커닝과 일부 기호(© – −)가 없고 Windows에서 글자를 1~3px 아래에 그리므로 홈과 404에는 쓰지 않는다. 샘플 화면은 '화면 규칙'대로 CDN을 쓴다.
- 사이트 마크는 Vizney Blocks의 2×2 블록에서 위 두 칸을 가로로 합친 모양이다(잉크 `#1b1b1b`, 노랑 `#ffcc00`, 분홍 `#ff2d55`). 사이트 머리글, `favicon.svg`(브라우저가 어두운 테마면 잉크 칸을 `#f4f5f7`로 바꾼다), 공유 이미지 `og.png`(1200×630)에만 쓰고 샘플 화면에는 넣지 않는다. 공유 미리보기는 스크립트를 실행하지 않아 한 언어만 보이므로 `og.png`도 기본 언어인 영어로 만들고, 이미지를 바꾸면 `og:image` 주소의 `?v=` 숫자를 올린다.
- `sitemap.xml`에는 홈만 넣는다. 샘플 화면은 `noindex`로 검색 유입을 블로그 포스트에 남긴다.


## 저장소 규칙

- 공개된 스타일의 폴더 이름은 바꾸지 않는다(포스트 임베드가 깨진다). 고칠 때는 같은 주소에서 고치고, 이력은 Git이 보관한다.
- `lib/embed.js`, `lib/embed-host.js`는 이미 발행된 포스트가 쓰므로, 고칠 때 이전 동작과 호환되게 한다.
