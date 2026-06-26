/* Defer heavy, non-critical scripts off the first-paint path for static
   service pages. The page is fully visible and usable without any of these:
   - Motion (GSAP + ScrollTrigger + motion.js, ~116KB) only adds reveal/parallax
     animation, so it loads on browser idle.
   - The GoHighLevel chat widget loads on first interaction (or idle fallback),
     so its third-party loader never competes with first paint.
   Vanilla, no deps. Matches nav.js / motion.js style. */
(function () {
  'use strict';

  var motionLoaded = false;
  function loadMotion() {
    if (motionLoaded) return;
    motionLoaded = true;
    var srcs = [
      '/assets/vendor/gsap.min.js?v=1',
      '/assets/vendor/ScrollTrigger.min.js?v=1',
      '/assets/motion.js?v=1'
    ];
    srcs.forEach(function (src) {
      var s = document.createElement('script');
      s.src = src;
      s.async = false; // preserve execution order so motion.js sees gsap
      document.head.appendChild(s);
    });
  }

  var chatLoaded = false;
  function loadChat() {
    if (chatLoaded) return;
    chatLoaded = true;
    var s = document.createElement('script');
    s.src = 'https://widgets.leadconnectorhq.com/loader.js';
    s.setAttribute('data-resources-url', 'https://widgets.leadconnectorhq.com/chat-widget/loader.js');
    s.setAttribute('data-widget-id', '6a3602e7d896e3ca46331853');
    s.setAttribute('data-source', 'WEB_USER');
    document.body.appendChild(s);
  }

  // Motion: idle (with a short timeout fallback for browsers without rIC).
  if ('requestIdleCallback' in window) {
    requestIdleCallback(loadMotion, { timeout: 2000 });
  } else {
    window.addEventListener('load', function () { setTimeout(loadMotion, 200); });
  }

  // Chat: first interaction, or idle after a longer grace period.
  ['pointerdown', 'keydown', 'touchstart', 'scroll'].forEach(function (evt) {
    window.addEventListener(evt, loadChat, { once: true, passive: true });
  });
  if ('requestIdleCallback' in window) {
    requestIdleCallback(loadChat, { timeout: 6000 });
  } else {
    window.addEventListener('load', function () { setTimeout(loadChat, 3000); });
  }
})();
