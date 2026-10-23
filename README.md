# Vizney Styles

Named dashboard styles from [Vizney](https://www.vizney.com). Each style has a live sample screen and a short spec (`style.md`), so it can be rebuilt by name: share the spec and ask for "the Chalk style".

Served at **https://styles.vizney.com** (GitHub Pages, `main` branch). Everything pushed to `main` is published immediately, so keep work in progress off `main`. The home page is `index.html`: the style gallery and an introduction to company styles.


## Styles

A style is a look and feel, not a dataset. The sample data only shows the style at work.

| Style | Feel | Sample | Spec | Blog posts |
|---|---|---|---|---|
| Chalk (초크) | Dark sidebar, pastel KPI tiles | [Live sample](https://styles.vizney.com/chalk/) · online store orders (fictional) | [style.md](chalk/style.md) | [KO](https://kr.vizney.com/style-chalk/) · [EN](https://www.vizney.com/style-chalk/) |
| Glass (글래스) | Pastel gradient, frosted glass cards | [Live sample](https://styles.vizney.com/glass/) · online store sales (fictional) | [style.md](glass/style.md) | [KO](https://kr.vizney.com/style-glass/) · [EN](https://www.vizney.com/style-glass/) |
| Tile (타일) | Airy white cards, blue–mint rings | [Live sample](https://styles.vizney.com/tile/) · hotel operations (fictional) | [style.md](tile/style.md) | [KO](https://kr.vizney.com/style-tile/) · [EN](https://www.vizney.com/style-tile/) |


## Adding a style

The full production checklist used with Claude is in [CLAUDE.md](https://github.com/yehwanhwang/vizney-styles/blob/main/CLAUDE.md).

1. Name the style with one evocative material or texture word (Chalk, Glass, Linen …) and use the name on its own: Vizney Styles is the collection, not part of the name. The folder is the name in lowercase, at the root: `chalk/`. Never name a folder after its sample data.
2. Give it a one-line subtitle that says what it looks like ("Dark sidebar, pastel KPI tiles"). The name is for remembering; the subtitle is for first-time readers and search.
3. Put two files in the folder:
   - `index.html`: the sample screen, self-contained (data included), Korean and English in one file via `?lang=ko` / `?lang=en`.
   - `style.md`: layout, colors, type, components, motion and don'ts, detailed enough to rebuild the style from its name. It is published at `<name>/style.html`.
4. Add these lines to the page's `<head>`:

   ```html
   <meta name="robots" content="noindex">
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/spoqa/spoqa-han-sans@v3.3.0/css/SpoqaHanSansNeo.css">
   <script src="/lib/embed.js" defer></script>
   ```

   `noindex` keeps search traffic on the blog post instead of the bare screen.
5. In embed mode `<html>` gets the class `vz-embed`. Reset any viewport-height layout there (for example `html.vz-embed .app { min-height: 0 }`) and hide page-only notes.
6. Optional: `cover-ko.png` / `cover-en.png` (1440×810 at 2×) for the post's feature image.
7. Publish the blog post at `style-<name>` (for example `/style-chalk/`) on both sites.
8. Update in place; Git history keeps the old versions. Add a row to the Styles table and a card to the home page (`index.html`).


## Embedding in a Ghost post

Paste into an HTML card and change the style, language and title:

```html
<figure class="kg-card kg-embed-card kg-width-wide">
  <iframe data-vizney-embed src="https://styles.vizney.com/chalk/?lang=ko&amp;embed=1" title="Chalk 스타일 대시보드" loading="lazy" style="display:block;width:100%;height:820px;border:1px solid #e6e6e6;border-radius:12px"></iframe>
  <figcaption><a href="https://styles.vizney.com/chalk/?lang=ko" target="_blank" rel="noopener">전체 화면으로 보기 ↗</a></figcaption>
</figure>
<script src="https://styles.vizney.com/lib/embed-host.js" defer></script>
```

`lib/embed-host.js` resizes the iframe to the height the page reports through `lib/embed.js`, so the whole screen shows without an inner scrollbar. Without it, the iframe keeps its fixed height and scrolls.
