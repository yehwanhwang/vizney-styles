/*!
 * Vizney embed helper — host side (Ghost post)
 *
 * Put next to the iframe in a Ghost HTML card:
 *   <iframe data-vizney-embed src="https://styles.vizney.com/<name>/?lang=ko&amp;embed=1" ...></iframe>
 *   <script src="https://styles.vizney.com/lib/embed-host.js" defer></script>
 *
 * Resizes every iframe[data-vizney-embed] to the content height its page
 * reports through lib/embed.js. Messages are accepted only from the origin
 * of the iframe's own src. Safe to include more than once on a page.
 *
 * Fit mode (opt-in): add data-vizney-fit to the iframe to lay the page out at
 * 1080px (or data-vizney-fit="<width>") and scale it down so the whole screen
 * fits the post width and the window height at a glance. Below 600px of post
 * width the page shows at full size, as without the attribute.
 */
(function () {
  'use strict';

  if (window.__vizneyEmbedHost) { window.__vizneyEmbedHost.scan(); return; }

  var MSG_HEIGHT = 'vizney:embed-height';
  var MSG_PING = 'vizney:embed-ping';
  var MIN_HEIGHT = 240;
  var MAX_HEIGHT = 20000;
  var FIT_WIDTH = 1080;        // layout width of a fitted page (the poster width)
  var FIT_MIN_WIDTH = 600;     // narrower posts show the page at full size
  var FIT_HEIGHT = 0.9;        // share of the window height a fitted page may use

  function frames() {
    return Array.prototype.slice.call(document.querySelectorAll('iframe[data-vizney-embed]'));
  }

  function originOf(frame) {
    try { return new URL(frame.getAttribute('src'), window.location.href).origin; } catch (e) { return null; }
  }

  function ping(frame) {
    var origin = originOf(frame);
    if (!origin || !frame.contentWindow) return;
    try { frame.contentWindow.postMessage({ type: MSG_PING }, origin); } catch (e) { /* not loaded yet */ }
  }

  function bind(frame) {
    if (frame.__vizneyBound) return;
    frame.__vizneyBound = true;
    frame.addEventListener('load', function () { ping(frame); });
    ping(frame);
  }

  function scan() { frames().forEach(bind); layoutAll(); }

  // ---- fit mode ----
  function fitWidth(frame) {
    var v = parseInt(frame.getAttribute('data-vizney-fit'), 10);
    return v >= 320 ? v : FIT_WIDTH;
  }

  // The frame goes into a wrapper that takes its place, its border and its radius;
  // the frame itself is laid out at the fit width and scaled down inside it.
  function wrap(frame) {
    if (frame.__vizneyWrap) return frame.__vizneyWrap;
    var cs = window.getComputedStyle(frame);
    var w = document.createElement('div');
    w.className = 'vizney-embed-fit';
    w.style.cssText = 'position:relative;overflow:hidden;max-width:100%;margin:0 auto;box-sizing:border-box';
    w.style.border = cs.borderTopWidth + ' ' + cs.borderTopStyle + ' ' + cs.borderTopColor;
    w.style.borderRadius = cs.borderTopLeftRadius;
    frame.parentNode.insertBefore(w, frame);
    w.appendChild(frame);
    frame.style.border = '0';
    frame.style.borderRadius = '0';
    frame.style.maxWidth = 'none';
    frame.style.display = 'block';
    frame.__vizneyWrap = w;
    return w;
  }

  function layout(frame) {
    var h = frame.__vizneyH || parseFloat(frame.getAttribute('height')) || parseFloat(frame.style.height) || 820;
    var w = wrap(frame);
    var avail = w.parentNode.clientWidth;
    if (!avail) return;
    if (avail < FIT_MIN_WIDTH) {
      w.style.width = '100%';
      w.style.height = 'auto';
      frame.style.position = 'static';
      frame.style.transform = 'none';
      frame.style.width = '100%';
      frame.style.height = h + 'px';
      return;
    }
    var dw = fitWidth(frame);
    var s = Math.min(1, (avail - 2) / dw, (window.innerHeight * FIT_HEIGHT) / h);
    w.style.width = Math.round(dw * s + 2) + 'px';
    w.style.height = Math.round(h * s + 2) + 'px';
    frame.style.position = 'absolute';
    frame.style.left = '0';
    frame.style.top = '0';
    frame.style.width = dw + 'px';
    frame.style.height = h + 'px';
    frame.style.transformOrigin = '0 0';
    frame.style.transform = 'scale(' + s + ')';
  }

  function layoutAll() {
    frames().forEach(function (f) { if (f.hasAttribute('data-vizney-fit')) layout(f); });
  }
  window.addEventListener('resize', layoutAll);

  window.addEventListener('message', function (e) {
    var data = e.data;
    if (!data || data.type !== MSG_HEIGHT) return;
    var list = frames();
    for (var i = 0; i < list.length; i++) {
      var frame = list[i];
      if (frame.contentWindow !== e.source) continue;
      if (originOf(frame) !== e.origin) return;
      var h = Math.round(Number(data.height));
      if (!isFinite(h)) return;
      h = Math.max(MIN_HEIGHT, Math.min(MAX_HEIGHT, h));
      if (frame.hasAttribute('data-vizney-fit')) {
        frame.__vizneyH = h;
        layout(frame);
        if (!frame.__vizneyAcked) { frame.__vizneyAcked = true; ping(frame); }
        return;
      }
      // Themes often set `box-sizing: border-box` globally; then the height must include the frame's border and padding.
      var cs = window.getComputedStyle(frame);
      if (cs.boxSizing === 'border-box') {
        h += Math.ceil(parseFloat(cs.borderTopWidth) + parseFloat(cs.borderBottomWidth) +
                       parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom)) || 0;
      }
      if (frame.style.height !== h + 'px') frame.style.height = h + 'px';
      if (!frame.__vizneyAcked) { frame.__vizneyAcked = true; ping(frame); }
      return;
    }
  });

  window.__vizneyEmbedHost = { scan: scan };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', scan);
  else scan();
})();
