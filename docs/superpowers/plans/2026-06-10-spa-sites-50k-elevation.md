# Spa Sites $50k Elevation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Elevate elitespautah.com (deep structural + motion redesign) and jmassageslc.com (GSAP choreography polish) to agency-grade visual quality without touching copy, schema, or booking funnels.

**Architecture:** Both static HTML sites get self-hosted GSAP 3.13.0 + ScrollTrigger, defer-loaded, driving a declarative data-attribute motion system in one `motion.js` per site. Hidden initial states exist only inside JS (`gsap.set`) so no-JS/reduced-motion users get a fully visible static page. Elite additionally gets token-level CSS evolution, homepage section rebuilds, local image migration, and a regenerated service-page template via `build_services.py`.

**Tech Stack:** Vanilla HTML/CSS/JS, GSAP 3.13.0 (core + ScrollTrigger, MIT-free), Python 3 (page transforms + template regen), Cloudflare Pages (git-connected, branch previews).

**Spec:** `docs/superpowers/specs/2026-06-10-spa-sites-50k-redesign-design.md`

**Hard rules for every task:**
- Copy byte-identical. Never retype copy from memory — always wrap/move existing strings programmatically or via exact Edit anchors read from the file at execution time.
- Schema JSON-LD, canonicals, sitemaps, robots, `_redirects`, `_headers`, GA4 (jmassage only) untouched.
- jmassage files: save UTF-8, verify with `file *.html` after every task touching them.
- Branch `redesign-50k` in both repos. Never push `main` until final merge task.
- Easing: `expo.out`/`power3.out`, 0.8–1.4s, stagger 0.08–0.12. No bounce.

---

## Part 1 — Elite Spa (`C:\Users\goho2\elitespautah`)

### Task 1: Vendor GSAP + script wiring + motion.js guard skeleton

**Files:**
- Create: `assets/vendor/gsap.min.js`, `assets/vendor/ScrollTrigger.min.js`
- Create: `assets/motion.js`
- Modify: every `*.html` except `cart.html`, `404.html` gets scripts too (all pages, consistent)

- [ ] **Step 1: Download pinned GSAP**

```bash
cd ~/elitespautah && mkdir -p assets/vendor
curl -sL -o assets/vendor/gsap.min.js https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js
curl -sL -o assets/vendor/ScrollTrigger.min.js https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js
ls -la assets/vendor/   # expect ~70KB + ~45KB, non-empty
head -c 200 assets/vendor/gsap.min.js   # expect minified JS banner "GSAP 3.13.0"
```

- [ ] **Step 2: Create `assets/motion.js` skeleton**

```js
/* Elite Spa motion system — GSAP 3.13. Fail-safe: page is fully visible
   without JS; all hidden states are set here via gsap.set only. */
(function () {
  'use strict';
  if (!window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);

  var mm = gsap.matchMedia();

  // Motion only when the user allows it.
  mm.add('(prefers-reduced-motion: no-preference)', function (ctx) {
    // wiring added in Task 5
  });

  // ScrollTrigger positions depend on web-font metrics.
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { ScrollTrigger.refresh(); });
  }
})();
```

- [ ] **Step 3: Add script tags to every page (idempotent transform)**

```python
# ~/elitespautah/add_scripts.py — run once, then delete
import pathlib, re
TAGS = ('  <script defer src="/assets/vendor/gsap.min.js?v=1"></script>\n'
        '  <script defer src="/assets/vendor/ScrollTrigger.min.js?v=1"></script>\n'
        '  <script defer src="/assets/motion.js?v=1"></script>\n')
for f in sorted(pathlib.Path('.').glob('*.html')):
    s = f.read_text(encoding='utf-8')
    if 'motion.js' in s or f.name == 'cart.html':
        continue
    s2 = s.replace('</head>', TAGS + '</head>', 1)
    assert s2 != s, f.name
    f.write_text(s2, encoding='utf-8', newline='')
    print('wired', f.name)
```

Run: `cd ~/elitespautah && python add_scripts.py && rm add_scripts.py`
Expected: `wired` printed for every page except cart.html.

- [ ] **Step 4: Verify clean load**

Start preview server on the repo directory, open `/index.html`, check console: zero errors, `window.gsap.version === "3.13.0"`.

- [ ] **Step 5: Commit**

```bash
cd ~/elitespautah && git add -A && git commit -m "feat: self-hosted GSAP 3.13 + ScrollTrigger, defer-wired on all pages, motion.js fail-safe skeleton"
```

### Task 2: Token evolution + base CSS upgrades

**Files:**
- Modify: `assets/styles.css` (append/adjust; bump `?v=` cache strings to `v=3` in all HTML via one sed-style pass at the END of elite work, Task 8)

- [ ] **Step 1: Add new tokens to `:root`** (after existing line tokens)

```css
  /* $50k elevation tokens */
  --ink-deep: #1f1a16;
  --cream-on-dark: #f5efe6;
  --shadow-soft: 0 2px 12px rgba(42, 30, 22, 0.06);
  --shadow-lift: 0 10px 32px rgba(42, 30, 22, 0.10);
  --shadow-bloom: 0 24px 64px rgba(160, 77, 44, 0.16);
  --type-display: clamp(3rem, 2rem + 5.5vw, 6rem);
  --ease-organic: cubic-bezier(0.22, 1, 0.36, 1);
  --t-slow: 0.9s;
```

- [ ] **Step 2: Add component CSS** (new section at end of styles.css)

```css
/* ===== Elevation pass (2026-06) ===== */
.eyebrow {
  font-family: "DM Sans", sans-serif; font-weight: 600;
  font-size: 0.75rem; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--brand-orange);
}
.line { display: block; overflow: hidden; }
.line-inner { display: inline-block; will-change: transform; }
.band-dark { background: var(--ink-deep); color: var(--cream-on-dark); }
.band-dark .eyebrow { color: #c9805a; }
.stat__num { font-family: "Marcellus", serif; font-size: var(--type-2); line-height: 1; }
a.card-link:focus-visible, .service-card a:focus-visible {
  outline: 2px solid var(--brand-orange); outline-offset: 4px; border-radius: var(--radius-md);
}
.u-underline { background-image: linear-gradient(currentColor, currentColor);
  background-size: 0% 1px; background-repeat: no-repeat; background-position: 0 100%;
  transition: background-size var(--t-slow) var(--ease-organic); }
.u-underline:hover, .u-underline:focus-visible { background-size: 100% 1px; }
.site-header--scrolled { background: rgba(250, 247, 243, 0.86);
  backdrop-filter: blur(12px) saturate(1.2); border-bottom: 1px solid var(--line); }
.btn-magnetic { will-change: transform; }
.img-zoom { overflow: hidden; }
.img-zoom img { transition: transform 1.2s var(--ease-organic); will-change: transform; }
.img-zoom:hover img { transform: scale(1.04); }
```

(Adjust selectors to the real class names found in the file — keep BEM consistency. Hero h1 gets `font-size: var(--type-display); line-height: 1.05;`.)

- [ ] **Step 3: Contrast fix** — find usages of `--brand-orange-soft` behind text ≤1rem; replace background with `var(--brand-cream-deep)` or raise text color to `var(--ink)`. Verify pairs ≥4.5:1 (compute, don't eyeball).

- [ ] **Step 4: Verify** — preview homepage + one service page: no visual breakage (new classes unused yet, so page must look unchanged). Console clean.

- [ ] **Step 5: Commit** — `git add assets/styles.css && git commit -m "feat: elevation tokens, eyebrow/line-mask/dark-band/zoom components, focus rings, contrast fix"`

### Task 3: Image migration off Squarespace CDN

**Files:**
- Create: `assets/img/hero-2500.webp`, `hero-1500.webp`, `hero-750.webp`, `assets/img/favicon.ico`
- Modify: all `*.html` (head favicon + og:image; index hero `srcset`)

- [ ] **Step 1: Extract current URLs** — `grep -o 'https://images\.squarespace-cdn\.com[^"]*' index.html | sort -u` and same across `*.html`. Download each referenced variant with curl into `assets/img/` (descriptive names). Verify sizes >10KB and `file` reports WebP/ICO.

- [ ] **Step 2: Rewrite references** — python pass replacing each Squarespace URL with local absolute path (`https://elitespautah.com/assets/img/...` for og:image/schema image fields, `/assets/img/...` for `src`/`srcset`/favicon). Assert zero `squarespace-cdn` matches remain: `grep -rl squarespace-cdn *.html | wc -l` → 0.

- [ ] **Step 3: CLS + LCP hardening (index.html)** — hero `<img>` gets explicit `width`/`height` (real intrinsic ratio), `fetchpriority="high"`, and `<link rel="preload" as="image" href="/assets/img/hero-1500.webp" imagesrcset="..." imagesizes="...">` in head.

- [ ] **Step 4: Verify** — preview: hero renders, favicon shows, `grep -c squarespace *.html` zero everywhere. Console: no 404s.

- [ ] **Step 5: Commit** — `git commit -am "feat: self-host hero images + favicon, kill Squarespace CDN dependency, preload hero for LCP"`

### Task 4: Homepage rebuild (`index.html`, mirror to `home.html`)

**Files:**
- Modify: `index.html` (then copy body changes to `home.html` — they serve the same content)
- Modify: `assets/styles.css` (section layouts)

- [ ] **Step 1: Hero restructure.** Read current hero block. Wrap EXISTING h1 text into mask lines by splitting at its existing visual break (or whole-line if single): each line becomes `<span class="line"><span class="line-inner">…existing text…</span></span>`. Add `class="eyebrow" data-reveal` to existing kicker if present. Add `data-hero` on hero section, `data-hero-media` on the image wrapper, `data-hero-cta` on the CTA group. No text changes.

- [ ] **Step 2: Stats band.** Re-mark existing trust-bar items: section gets `class="band-dark" data-reveal-stagger`; numeric stats get `<span class="stat__num" data-count="N">N</span>` where N is the existing number (keep any existing `+` as separate `<span>+</span>` so copy stays identical). Non-numeric items keep text untouched.

- [ ] **Step 3: Services asymmetric grid.** New CSS:

```css
.svc-editorial { display: grid; gap: var(--space-3); }
@media (min-width: 800px) {
  .svc-editorial { grid-template-columns: repeat(12, 1fr); }
  .svc-editorial__feature--a { grid-column: span 7; }
  .svc-editorial__feature--b { grid-column: span 5; }
  .svc-editorial__rest { grid-column: 1 / -1; display: grid;
    grid-template-columns: repeat(3, 1fr); gap: var(--space-3); }
}
.svc-feature { position: relative; border-radius: var(--radius-md); min-height: 380px;
  display: flex; align-items: flex-end; padding: var(--space-4);
  background-size: cover; background-position: center; box-shadow: var(--shadow-soft); }
.svc-feature::after { content: ""; position: absolute; inset: 0; border-radius: inherit;
  background: linear-gradient(180deg, rgba(31,26,22,0) 30%, rgba(31,26,22,0.72) 100%); }
.svc-feature > * { position: relative; z-index: 1; color: var(--cream-on-dark); }
.svc-feature { transition: box-shadow var(--t-slow) var(--ease-organic), transform var(--t-slow) var(--ease-organic); }
.svc-feature:hover { box-shadow: var(--shadow-bloom); transform: translateY(-4px); }
```

Head Spa + Couples cards become `.svc-feature` (background: hero image crop via `background-image` + scrim — only real photo, treated differently per card via `background-position`). Remaining service cards keep existing `.service-card` styling inside `.svc-editorial__rest`, each `data-reveal`. All link texts/hrefs unchanged.

- [ ] **Step 4: Reviews as pull-quotes.** Existing review blocks get `class="pull-quote" data-reveal`; CSS: oversized leading `“` via `::before` (Marcellus, ~5rem, terracotta, low opacity), quote text bumped one type step, attribution restyled `.eyebrow`. ★ spans untouched.

- [ ] **Step 5: Final CTA band.** Existing closing CTA section gets `band-dark` treatment + button `data-magnetic`. Copy untouched.

- [ ] **Step 6: Mirror to home.html** — apply identical body diff (they duplicate content; diff index vs home first to confirm parity, then port).

- [ ] **Step 7: Verify** — preview 375/768/1280: layout sound at all three, no overflow, no console errors. With JS disabled: everything visible (motion not wired yet anyway).

- [ ] **Step 8: Commit** — `git commit -am "feat: homepage editorial rebuild — masked hero, dark stats band, asymmetric services grid, pull-quote reviews, CTA band"`

### Task 5: motion.js full implementation

**Files:**
- Modify: `assets/motion.js`

- [ ] **Step 1: Replace skeleton body with full system**

```js
/* Elite Spa motion system — GSAP 3.13. Fail-safe: page fully visible without JS. */
(function () {
  'use strict';
  if (!window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);

  var EASE = 'expo.out';
  var mm = gsap.matchMedia();

  // Header scroll state (runs regardless of motion preference — it's a style state)
  var header = document.querySelector('header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('site-header--scrolled', window.scrollY > 24);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  mm.add('(prefers-reduced-motion: no-preference)', function () {

    // Hero entrance
    var hero = document.querySelector('[data-hero]');
    if (hero) {
      var lines = hero.querySelectorAll('.line-inner');
      var eyebrow = hero.querySelector('.eyebrow');
      var cta = hero.querySelector('[data-hero-cta]');
      var tl = gsap.timeline({ defaults: { ease: EASE } });
      if (eyebrow) tl.from(eyebrow, { autoAlpha: 0, y: 14, duration: 0.8 });
      if (lines.length) tl.from(lines, { yPercent: 110, duration: 1.2, stagger: 0.12 }, '-=0.4');
      if (cta) tl.from(cta, { autoAlpha: 0, y: 20, duration: 0.9 }, '-=0.7');
    }

    // Scroll reveals
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

    // Count-up
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

    // FAQ smooth accordion (progressive enhancement over <details>)
    document.querySelectorAll('details.faq-item, .faq details').forEach(function (d) {
      var summary = d.querySelector('summary');
      var body = summary && summary.nextElementSibling;
      if (!summary || !body) return;
      summary.addEventListener('click', function (e) {
        e.preventDefault();
        if (d.open) {
          gsap.to(body, { height: 0, autoAlpha: 0, duration: 0.45, ease: EASE,
            onComplete: function () { d.open = false; gsap.set(body, { clearProps: 'all' }); } });
        } else {
          d.open = true;
          gsap.from(body, { height: 0, autoAlpha: 0, duration: 0.55, ease: EASE,
            onComplete: function () { gsap.set(body, { clearProps: 'all' }); } });
        }
      });
    });

    // Desktop-only effects
    mm.add('(min-width: 800px) and (pointer: fine) and (prefers-reduced-motion: no-preference)', function () {
      // Hero parallax
      var media = document.querySelector('[data-hero-media]');
      if (media) {
        gsap.to(media, { yPercent: -8, ease: 'none',
          scrollTrigger: { trigger: '[data-hero]', start: 'top top', end: 'bottom top', scrub: true } });
      }
      // Generic parallax
      gsap.utils.toArray('[data-parallax]').forEach(function (el) {
        var amt = parseFloat(el.getAttribute('data-parallax')) || 0.08;
        gsap.to(el, { yPercent: -100 * amt, ease: 'none',
          scrollTrigger: { trigger: el, start: 'top bottom', end: 'bottom top', scrub: true } });
      });
      // Magnetic buttons
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
    });
  });

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { ScrollTrigger.refresh(); });
  }
})();
```

- [ ] **Step 2: Verify** — preview homepage: hero plays once, reveals fire on scroll, counts animate, magnetic works ≥800px pointer:fine. Emulate reduced-motion (DevTools): nothing animates, all content visible. Disable JS: all content visible. Console clean.

- [ ] **Step 3: Verify FAQ** — faq.html accordion opens/closes smoothly, keyboard Enter/Space on summary still works.

- [ ] **Step 4: Commit** — `git commit -am "feat: full GSAP motion system — hero timeline, reveals, count-up, parallax, magnetic CTAs, smooth FAQ"`

### Task 6: Service template upgrade + regeneration

**Files:**
- Modify: `build_services.py` (PAGE_TEMPLATE)
- Regenerates: 14 service pages

- [ ] **Step 1: Snapshot for diff** — `git stash list` clean; `mkdir -p /tmp/svc-before && cp *-massage.html cupping-therapy.html medical-infrared-sauna.html /tmp/svc-before/`

- [ ] **Step 2: Template edits in PAGE_TEMPLATE:** mini-hero header (`eyebrow` category + h1 wrapped in `.line/.line-inner` + breadcrumb untouched), pricing table: add class `price-table--weighted`; related cards get `img-zoom`/lift classes + `data-reveal`; main sections get `data-reveal`. Add scripts/tokens only if template's head lacks them (Task 1 wired the generated files; template must now emit the same three script tags so future regens keep them).

- [ ] **Step 3: Pricing weight CSS (styles.css):**

```css
.price-table--weighted .price-row--featured {
  background: var(--brand-cream-soft); border: 1px solid var(--line-strong);
  border-radius: var(--radius-sm); transform: scale(1.015); box-shadow: var(--shadow-soft);
}
```

Template marks the 60-min row `price-row--featured` (price text unchanged).

- [ ] **Step 4: Regenerate + assert** — `python build_services.py` then for each page:

```bash
for f in /tmp/svc-before/*.html; do n=$(basename $f);
  diff <(grep -E 'canonical|application/ld\+json|<title>|name="description"' /tmp/svc-before/$n) \
       <(grep -E 'canonical|application/ld\+json|<title>|name="description"' ~/elitespautah/$n) || echo "DRIFT: $n"; done
```

Expected: zero `DRIFT` lines. Manually eyeball one full diff (`git diff deep-tissue-massage.html`) — only class/attribute/structure changes, zero copy-string changes.

- [ ] **Step 5: Verify** — preview deep-tissue page 375/1280: mini-hero reveal, weighted 60-min row, hover physics. Console clean.

- [ ] **Step 6: Commit** — `git commit -am "feat: service template elevation — mini-hero reveals, weighted 60-min pricing, related-card physics (14 pages regenerated, copy+schema verified unchanged)"`

### Task 7: Secondary pages (services hub, faq, contact, gift-cards, book, 404)

**Files:**
- Modify: `services.html`, `faq.html`, `contact.html`, `gift-cards.html`, `book.html`, `404.html`

- [ ] **Step 1: services.html** — apply `.svc-editorial` grid language to category sections (featured cards where images exist; rest uniform), `data-reveal-stagger` per section. Schema block untouched.
- [ ] **Step 2: faq.html** — ensure `<details>` structure matches motion.js accordion selector (`details.faq-item` or add the class), page-header gets eyebrow + line-mask h1.
- [ ] **Step 3: contact/gift-cards/book/404** — page-header treatment (eyebrow + masked h1 + `data-reveal` on intro), CTA buttons `data-magnetic`. book.html iframe/skeleton untouched.
- [ ] **Step 4: Verify** — preview each at 375/1280, console clean, links resolve.
- [ ] **Step 5: Commit** — `git commit -am "feat: secondary pages elevation — editorial headers, grid language, magnetic CTAs"`

### Task 8: Elite verification suite + content-gaps

**Files:**
- Create: `content-gaps.md`
- Modify: all HTML (cache-bust `styles.css?v=3`, `nav.js` untouched)

- [ ] **Step 1: Cache-bust** — python pass: `styles.css?v=2` → `styles.css?v=3` all pages.
- [ ] **Step 2: content-gaps.md** — list: real photography per service category (14 wishlist shots), optional 60-min "Most booked" badge copy, GA4 property decision, real GBP review count for schema re-add.
- [ ] **Step 3: Full sweep** — preview screenshots: index, services, deep-tissue, faq, contact, book × 375/768/1280. Console: zero errors each. JS-off: index fully readable. Reduced-motion: static but complete.
- [ ] **Step 4: Lighthouse** — run against preview for `/` and `/deep-tissue-massage.html`: all categories ≥90. Fix regressions before proceeding (likely culprits: image sizes, contrast).
- [ ] **Step 5: Link check** — every internal href resolves to a file (script the check).
- [ ] **Step 6: Commit** — `git commit -am "chore: cache-bust v3, content-gaps inventory, verification pass"`

---

## Part 2 — J Massage (`C:\Users\goho2\jmassage-website`)

### Task 9: Branch + vendor GSAP + motion.js skeleton

**Files:**
- Create: `js/vendor/gsap.min.js`, `js/vendor/ScrollTrigger.min.js`, `js/motion.js`
- Modify: all 24 HTML pages (script tags)

- [ ] **Step 1:** `cd ~/jmassage-website && git checkout -b redesign-50k && mkdir -p js/vendor` then download same pinned 3.13.0 files as Task 1.
- [ ] **Step 2:** `js/motion.js` — same fail-safe guard skeleton as elite Task 1 Step 2 (verbatim, with header comment "J Massage motion layer").
- [ ] **Step 3:** Script-wiring python pass (same as Task 1 Step 3 but paths `/js/vendor/...`, `/js/motion.js`, and glob includes `services/*.html`; skip `404.html`? No — include all; skip none except googlebc…html verification file).
- [ ] **Step 4:** `file *.html services/*.html` — every file UTF-8 (or ASCII). Preview index: console clean, gsap 3.13.0 present, existing animations unaffected.
- [ ] **Step 5:** Commit: `git commit -am "feat: self-hosted GSAP 3.13 + ScrollTrigger wired on all pages, motion.js fail-safe skeleton"`

### Task 10: Hero timeline + legacy token fix (`js/main.js`)

**Files:**
- Modify: `js/main.js`

- [ ] **Step 1: Hero block replacement.** Locate the hero reveal block (clip-path `.hero__line` + `[data-reveal-fade]` setTimeout chains, ~lines 117–127). Replace with a guarded GSAP path that falls back to the existing vanilla logic when GSAP is absent:

```js
// Hero entrance — GSAP timeline when available, vanilla fallback otherwise.
var heroLines = document.querySelectorAll('.hero__line');
var heroFades = document.querySelectorAll('[data-reveal-fade]');
var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (window.gsap && !reduced && heroLines.length) {
  var heroImg = document.querySelector('.hero img, .hero__media img');
  var tl = gsap.timeline({ defaults: { ease: 'expo.out' } });
  if (heroImg) tl.fromTo(heroImg, { scale: 1.06 }, { scale: 1, duration: 1.4 }, 0);
  tl.to(heroLines, { y: 0, yPercent: 0, duration: 1.1, stagger: 0.14,
        onStart: function () { heroLines.forEach(function (l) { l.classList.add('is-in'); }); } }, 0.1)
    .to(heroFades, { autoAlpha: 1, y: 0, duration: 0.9, stagger: 0.12 }, '-=0.6');
} else {
  /* existing setTimeout chain stays here as the fallback — do not delete it */
}
```

(Adapt to the file's real initial-state mechanism: if CSS sets `.hero__line { transform: translateY(110%) }` with `.is-in` resetting it, drive the same classes/transforms — read the CSS first, keep the no-JS-visible guarantee exactly as it works today.)

- [ ] **Step 2: Token fix.** svc-card glow `rgba(200,136,42,0.13)` → read computed clay: `getComputedStyle(document.documentElement).getPropertyValue('--lantern-mid')` with the old literal as fallback.
- [ ] **Step 3: Verify** — preview index: hero plays (image settle + lines + fades), reduced-motion = instant visible, JS-off = visible. Card glow now clay-toned. Console clean. `file js/main.js` UTF-8.
- [ ] **Step 4: Commit** — `git commit -am "feat: GSAP hero choreography with vanilla fallback; svc-card glow uses clay token"`

### Task 11: Parallax + magnetic + smooth FAQ (`js/motion.js`)

**Files:**
- Modify: `js/motion.js`

- [ ] **Step 1: Implement** — inside the matchMedia no-preference block:

```js
    // Editorial image parallax (desktop only) — scoped to NEW attribute, never .reveal
    mm.add('(min-width: 820px) and (pointer: fine) and (prefers-reduced-motion: no-preference)', function () {
      gsap.utils.toArray('[data-parallax]').forEach(function (el) {
        var amt = parseFloat(el.getAttribute('data-parallax')) || 0.06;
        gsap.to(el, { yPercent: -100 * amt, ease: 'none',
          scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } });
      });
      document.querySelectorAll('[data-magnetic]').forEach(function (btn) {
        var qx = gsap.quickTo(btn, 'x', { duration: 0.4, ease: 'power3.out' });
        var qy = gsap.quickTo(btn, 'y', { duration: 0.4, ease: 'power3.out' });
        btn.addEventListener('mousemove', function (e) {
          var r = btn.getBoundingClientRect();
          qx((e.clientX - r.left - r.width / 2) * 0.22);
          qy((e.clientY - r.top - r.height / 2) * 0.22);
        });
        btn.addEventListener('mouseleave', function () { qx(0); qy(0); });
      });
    });

    // Smooth FAQ height (replaces class-jump; .faq-item toggle stays the source of truth)
    document.querySelectorAll('.faq-item').forEach(function (item) {
      var q = item.querySelector('.faq-item__q, .faq-q, button');
      var a = item.querySelector('.faq-item__a, .faq-a');
      if (!q || !a) return;
      q.addEventListener('click', function () {
        requestAnimationFrame(function () {
          if (item.classList.contains('open')) {
            gsap.from(a, { height: 0, autoAlpha: 0, duration: 0.5, ease: 'expo.out',
              onComplete: function () { gsap.set(a, { clearProps: 'height,opacity,visibility' }); } });
          }
        });
      });
    });
```

(Read the real FAQ markup in `service-page.js`/faq.html first and match selectors; do not break the existing one-open-at-a-time logic — this layer only animates the height after the class flips.)

- [ ] **Step 2: Wire attributes in HTML** — `data-parallax` on editorial images (index: hero-room is hero, skip; service-body/couples/foot/head images yes; about detail image yes). `data-magnetic` on `.nav__cta`, hero CTA, footer CTA — python pass or targeted Edits across pages; UTF-8 preserved.
- [ ] **Step 3: Verify** — index/about/one service page: parallax subtle, magnetic on CTAs desktop-only, FAQ smooth on service page + faq.html + pricing.html. Carousel/counters/cursor glow regression-checked. Reduced-motion + JS-off clean. `file` UTF-8 sweep on touched files.
- [ ] **Step 4: Commit** — `git commit -am "feat: scroll parallax, magnetic CTAs, smooth FAQ height — layered over existing vanilla systems"`

### Task 12: jmassage verification suite

- [ ] **Step 1:** Preview screenshots: index, services/deep-tissue, pricing, faq, gift-cards × 375/768/1280. Console zero errors each.
- [ ] **Step 2:** Lighthouse on `/` and one service page: ≥90 × 4 categories.
- [ ] **Step 3:** `git diff main --stat` review: no schema/canonical/GA4/copy lines changed (grep the diff for `ld+json`, `canonical`, `G-HR9MP6ENEP` → zero hits).
- [ ] **Step 4:** `file *.html services/*.html js/*.js` — all UTF-8/ASCII.
- [ ] **Step 5:** Commit anything outstanding; branch complete.

---

## Part 3 — Ship

### Task 13: Merge + deploy + live verify

- [ ] **Step 1:** Elite: `git checkout main && git merge --no-ff redesign-50k -m "Elevation: structural redesign + GSAP motion system" && git push origin main`
- [ ] **Step 2:** jmassage: same merge/push.
- [ ] **Step 3:** Wait for Cloudflare Pages deploys; live-verify both domains: homepage renders, motion plays, console clean, `curl -sI` on hero image 200, spot-check one service page each.
- [ ] **Step 4:** Push `redesign-50k` branches too (preserve history): `git push origin redesign-50k` both repos.
- [ ] **Step 5:** Update memory: new motion system architecture note + any lessons.
