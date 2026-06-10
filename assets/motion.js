/* Elite Spa motion system — GSAP 3.13. Fail-safe: page is fully visible
   without JS; all hidden states are set here via gsap.set only. */
(function () {
  'use strict';
  if (!window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);

  var mm = gsap.matchMedia();

  mm.add('(prefers-reduced-motion: no-preference)', function () {
    /* motion wiring lands with the homepage rebuild */
  });

  /* ScrollTrigger positions depend on web-font metrics. */
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { ScrollTrigger.refresh(); });
  }
})();
