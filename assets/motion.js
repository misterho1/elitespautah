/* Elite Spa motion system — GSAP 3.13 + ScrollTrigger.
   Fail-safe: the page is fully visible without JS. Every hidden/offset
   initial state is created here (gsap.from/gsap.set), never in CSS. */
(function () {
  'use strict';
  if (!window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);

  var EASE = 'expo.out';

  /* Header scroll state — style state, runs regardless of motion preference. */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('site-header--scrolled', window.scrollY > 24);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  var mm = gsap.matchMedia();

  mm.add(
    {
      motionOK: '(prefers-reduced-motion: no-preference)',
      isDesktop: '(min-width: 800px) and (pointer: fine)'
    },
    function (context) {
      var motionOK = context.conditions.motionOK;
      var isDesktop = context.conditions.isDesktop;
      if (!motionOK) return;

      /* Hero entrance — eyebrow, masked lines, lead, CTA. */
      var hero = document.querySelector('[data-hero]');
      if (hero) {
        var lines = hero.querySelectorAll('.line-inner');
        var eyebrow = hero.querySelector('.eyebrow');
        var lead = hero.querySelector('.hero__lead, .lead');
        var cta = hero.querySelector('[data-hero-cta]');
        var tl = gsap.timeline({ defaults: { ease: EASE } });
        if (eyebrow) tl.from(eyebrow, { autoAlpha: 0, y: 14, duration: 0.8 });
        if (lines.length) tl.from(lines, { yPercent: 110, duration: 1.2, stagger: 0.12 }, '-=0.4');
        if (lead) tl.from(lead, { autoAlpha: 0, y: 18, duration: 0.9 }, '-=0.7');
        if (cta) tl.from(cta, { autoAlpha: 0, y: 20, duration: 0.9 }, '-=0.65');
      }

      /* Scroll reveals — once, never re-trigger. */
      gsap.utils.toArray('[data-reveal]').forEach(function (el) {
        gsap.from(el, {
          autoAlpha: 0, y: 28, duration: 1.0, ease: EASE,
          scrollTrigger: { trigger: el, start: 'top 86%', once: true }
        });
      });
      gsap.utils.toArray('[data-reveal-stagger]').forEach(function (group) {
        gsap.from(group.children, {
          autoAlpha: 0, y: 28, duration: 1.0, ease: EASE, stagger: 0.1,
          scrollTrigger: { trigger: group, start: 'top 84%', once: true }
        });
      });

      /* Count-up numerals. */
      gsap.utils.toArray('[data-count]').forEach(function (el) {
        var target = parseFloat(el.getAttribute('data-count'));
        if (isNaN(target)) return;
        var obj = { v: 0 };
        gsap.to(obj, {
          v: target, duration: 1.6, ease: 'power3.out',
          scrollTrigger: { trigger: el, start: 'top 88%', once: true },
          onUpdate: function () { el.textContent = Math.round(obj.v); }
        });
      });

      /* FAQ smooth accordion — progressive enhancement over <details>. */
      gsap.utils.toArray('details.faq__item').forEach(function (d) {
        var summary = d.querySelector('summary');
        var body = d.querySelector('.faq__answer');
        if (!summary || !body) return;
        summary.addEventListener('click', function (e) {
          e.preventDefault();
          if (d.open) {
            gsap.to(body, {
              height: 0, autoAlpha: 0, duration: 0.4, ease: EASE,
              onComplete: function () { d.open = false; gsap.set(body, { clearProps: 'all' }); }
            });
          } else {
            d.open = true;
            gsap.from(body, {
              height: 0, autoAlpha: 0, duration: 0.55, ease: EASE,
              onComplete: function () { gsap.set(body, { clearProps: 'all' }); }
            });
          }
        });
      });

      if (!isDesktop) return;

      /* Hero parallax — image drifts as the page scrolls away. */
      var media = document.querySelector('[data-hero-media]');
      if (media) {
        gsap.to(media, {
          yPercent: 12, ease: 'none',
          scrollTrigger: { trigger: '[data-hero]', start: 'top top', end: 'bottom top', scrub: true }
        });
      }

      /* Generic parallax. */
      gsap.utils.toArray('[data-parallax]').forEach(function (el) {
        var amt = parseFloat(el.getAttribute('data-parallax')) || 0.08;
        gsap.to(el, {
          yPercent: -100 * amt, ease: 'none',
          scrollTrigger: { trigger: el, start: 'top bottom', end: 'bottom top', scrub: true }
        });
      });

      /* Magnetic buttons. */
      document.querySelectorAll('[data-magnetic]').forEach(function (btn) {
        btn.classList.add('btn-magnetic');
        var qx = gsap.quickTo(btn, 'x', { duration: 0.4, ease: 'power3.out' });
        var qy = gsap.quickTo(btn, 'y', { duration: 0.4, ease: 'power3.out' });
        btn.addEventListener('mousemove', function (e) {
          var r = btn.getBoundingClientRect();
          qx((e.clientX - r.left - r.width / 2) * 0.25);
          qy((e.clientY - r.top - r.height / 2) * 0.25);
        });
        btn.addEventListener('mouseleave', function () { qx(0); qy(0); });
      });
    }
  );

  /* ScrollTrigger positions depend on web-font metrics. */
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { ScrollTrigger.refresh(); });
  }
})();
