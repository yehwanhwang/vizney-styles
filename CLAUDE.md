# Vizney Styles 제작 지침

이 저장소는 styles.vizney.com(GitHub Pages, `main` 브랜치)으로 배포된다. 대시보드의 '느낌'을 이름 붙은 스타일로 만들어 쌓고, 블로그(kr.vizney.com, www.vizney.com)의 Gallery에 소개한다. 목적은 실제 데이터 분석이 아니라 스타일 전달이다.


## 새 스타일을 만드는 순서

1. **레퍼런스 읽기:** 사용자가 첨부한 이미지에서 스타일(색, 카드 모양, 레이아웃, 차트 표현)만 가져온다. 브랜드명, 로고, 인물 사진, 문구, 데이터는 가져오지 않는다. 출처는 표기하지 않는다.
2. **샘플 화면 설계:** 스타일이 잘 드러나는 업무 화면 하나를 정한다(예: 온라인몰 주문 분석). 브랜드 자리에는 가상 브랜드명 대신 Vizney 로고를 넣고(아래 '브랜드'), 데이터는 가상 데이터를 쓰며, 합계·비율·증감이 서로 맞는지 계산으로 확인한다.
3. **이름과 부제:** 재료·질감을 떠올리게 하는 영단어 하나로 이름 후보 2~3개를 제안하고 사용자가 고른다. 'Vizney'는 붙이지 않는다(Vizney Styles는 묶음 이름이다). 부제는 생김새를 말하는 한 줄이다(예: "Dark sidebar, pastel KPI tiles · 다크 사이드바와 파스텔 KPI 카드").
4. **구현:** 아래 '화면 규칙'을 따라 `<name>/index.html`을 만든다.
5. **검증:** 아래 '검증'을 모두 통과시킨다.
6. **명세:** `<name>/style.md`를 쓴다(아래 '명세 형식').
7. **대표 이미지:** `<name>/cover-ko.png`, `<name>/cover-en.png`를 만든다. 1440×810 화면을 2배 해상도로 캡처하고, 페이지 하단 안내 문구는 숨긴다.
8. **README:** Styles 표에 행을 추가한다. 블로그 링크는 `/style-<name>/`이다.
9. **배포:** 작업 브랜치 → 커밋 → PR → 머지. GitHub Actions의 'pages build and deployment'가 성공했는지로 배포를 확인한다. `main`에 올라간 것은 바로 공개된다.
10. **포스트 초안:** 아래 '포스트 형식'으로 한국어·영어 전문을 대화창에 바로 준다(Claude Docs는 쓰지 않는다).


## 화면 규칙

- HTML 파일 하나로 완결한다(데이터 포함). 외부에서 불러오는 것은 글꼴뿐이다.
- `<head>`에 세 줄을 넣는다.

  ```html
  <meta name="robots" content="noindex">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/spoqa/spoqa-han-sans@v3.3.0/css/SpoqaHanSansNeo.css">
  <script src="/lib/embed.js" defer></script>
  ```

- 한국어·영어를 한 파일에서 `?lang=ko|en`으로 전환하고, 화면에도 KO/EN 토글을 둔다. 기본은 한국어다.
- 숫자는 한국어에서 억·만·건·원, 영어에서 ₩·M·K로 쓴다. 단위와 접미사는 숫자보다 작게 쓴다.
- KPI 카드: 글자 크기는 대표 수치와 나머지 두 단계만 쓰고 굵기와 색으로 구분한다. 증감은 수치 아래 줄에 두어 카드마다 수치 높이를 맞춘다. 증감 색은 값이 움직인 방향이 아니라 그 지표에서 좋은 변화인지로 정한다.
- 카드 안에 다시 카드(컨테이너)를 넣지 않는다. 다크 모드는 만들지 않는다.
- 필터(탭 등)는 화면 위 한 줄에 두고, 아래 모든 카드에 함께 적용한다.
- 차트: 이중 축은 쓰지 않는다. 범주 색은 세 가지와 회색 '기타'까지만 쓴다. 텍스트에는 데이터 색을 쓰지 않는다. 모든 차트에 호버 툴팁, 키보드 조작, 스크린 리더용 표를 둔다. `prefers-reduced-motion`이면 애니메이션을 끈다.
- 색은 dataviz 스킬의 `validate_palette.js`로 색각 이상 구분과 대비를 검사해서 통과한 조합만 쓴다.
- 임베드 모드(`?embed=1`이면 `<html>`에 `vz-embed` 클래스가 붙는다): `100vh` 같은 화면 높이 기준 레이아웃을 풀고, 페이지 전용 안내 문구를 숨긴다.


## 브랜드

- 샘플 화면에 실제로 없는 브랜드명을 지어 넣지 않는다. 브랜드 자리에는 Vizney 로고를 넣는다(홍보도 겸한다). 샘플 화면, 대표 이미지, 디자인 시스템 모두 같다. 데이터와 문구는 계속 가상으로 만든다.
- 사이드바·헤더처럼 가로 공간이 있으면 워드마크, 아이콘 크기 자리(좁은 레일, 앱 아이콘 타일)에는 V 마크를 쓴다. 좁은 화면에서 그 자리가 사라지면 헤더 왼쪽 위에 V 마크를 따로 둔다.
- 색은 화면에 맞춘다: 어두운 바탕에는 흰색, 밝은 바탕에는 그 스타일의 본문 잉크색, 색 타일 위에는 흰색. 모양은 바꾸지 않는다(늘이기, 기울이기, 윤곽선, 그림자, 그라데이션 채우기 금지).
- 원본은 `brand/`에 있다: `vizney-wordmark.svg`, `vizney-v.svg`(벡터)와 받은 PNG 원본 세 개. 화면에는 SVG의 `<path>`를 인라인으로 넣고 `fill`만 화면 색으로 바꾼다(외부 파일을 불러오지 않는 화면 규칙은 그대로).
- style.md에는 로고를 넣지 않는다. 명세는 스타일만 다룬다.


## 검증

- 1440, 1200(블로그 넓은 폭), 1024, 390px에서 한국어·영어 화면을 캡처해 겹침, 잘림, 들쭉날쭉한 줄바꿈이 없는지 눈으로 확인한다.
- 필터 전환, 호버, 키보드 조작이 동작하고 페이지 오류가 없는지 확인한다.
- 다른 출처의 부모 페이지에 아래 임베드 코드를 넣고, iframe 높이가 내용에 맞는지 확인한다(넓은 폭, 좁은 폭, 모바일, 창 크기 변경, 한 페이지에 두 개).
- 샌드박스에서 글꼴 CDN이 막히면 spoqa/spoqa-han-sans 저장소의 v3.3.0을 부분 클론해서 jsDelivr 요청을 로컬 파일로 돌려 확인한다.


## 명세 형식 (style.md)

- 제목은 이름만 쓴다(`# Chalk`). 그 아래 영어 부제 · 한국어 부제, 한두 문장 소개, 라이브 샘플과 명세 주소를 둔다.
- 섹션: Layout, Color(토큰 표: 이름·Hex·용도), Type, Components, Motion and interaction, Don'ts.
- 이름만 듣고 같은 스타일을 다시 만들 수 있을 만큼 구체적으로 쓴다. 출처 섹션은 두지 않는다.
- 사이트에서는 `<name>/style.html`로 열린다.


## 포스트 형식

- SEO 제목: `<Name> — <부제>의 대시보드 스타일` / `<Name>: A Dashboard Style with <subtitle>`
- 발췌문: 스타일 한 문장과 샘플 한 문장.
- 첫 문장은 바로 스타일 설명으로 시작한다: "<Name>는 …한 대시보드 스타일입니다." 이어서 샘플 데이터와 조작 방법을 한두 문장으로 쓴다.
- 순서: HTML 카드(아래 임베드 코드) → `### Design`(왜 이렇게 표현했는지 불릿 3~4개) → `### Prompt`(명세 링크와 요청 예시 코드 블록) → 제작 문의 링크(https://kr.vizney.com/contact-us/, https://www.vizney.com/contact-us/).
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


## 저장소 규칙

- 공개된 스타일의 폴더 이름은 바꾸지 않는다(포스트 임베드가 깨진다). 고칠 때는 같은 주소에서 고치고, 이력은 Git이 보관한다.
- `lib/embed.js`, `lib/embed-host.js`는 이미 발행된 포스트가 쓰므로, 고칠 때 이전 동작과 호환되게 한다.
