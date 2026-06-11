# Spa Sites $50k Elevation — Design Spec

Date: 2026-06-10
Sites: elitespautah.com (deep redesign) + jmassageslc.com (choreography polish)
Approved by: Andrew (design gate, 2026-06-10) — full autonomy through merge.

## Goal

Both sites should look and move like a top agency built them. Elite Spa gets a structural visual redesign plus a full GSAP motion system (it currently has 21 lines of JS and zero motion). J Massage keeps its editorial design and gains GSAP choreography where it beats the existing vanilla animation. All copy verbatim. All SEO infrastructure untouched.

## Decisions (locked)

1. Scope: Elite deep, jmassage polish.
2. Elite direction: elevate current warm cream/terracotta palette — no rebrand.
3. GSAP: self-hosted `gsap.min.js` + `ScrollTrigger.min.js` per repo, defer-loaded. No CDN. (GSAP 3.13+ is 100% free.)
4. jmassage: layer GSAP where it wins; keep working vanilla systems (carousel, counters, IO reveals, cursor glow, nav).
5. Deploy: feature branch per repo → verify → merge to main (auto-deploy). Andrew may run /ultrareview (code-review ultra) on the branch before merge; not required.

## Part A — Elite Spa (repo `~/elitespautah`, branch `redesign-50k`)

### A1. Token evolution (`assets/styles.css`)

Keep all existing hues. Add/adjust:

- `--ink-deep: #1f1a16` — espresso near-black for dark bands (stats, final CTA, footer already dark).
- Warm shadow scale: `--shadow-soft`, `--shadow-lift`, `--shadow-bloom` (terracotta-tinted low-alpha, layered).
- Display scale: `--type-display: clamp(3rem, 2rem + 5.5vw, 6rem)` for hero h1; tighten `line-height` to 1.05; existing `--type-1` stays for inner-page headers.
- Eyebrow style utility: DM Sans 600, 0.75rem, uppercase, `letter-spacing: 0.14em`, terracotta.
- Fix contrast: anywhere `--brand-orange-soft` backs small text, swap to a token meeting AA (verify against cream).
- New `--ease-organic: cubic-bezier(0.22, 1, 0.36, 1)` and duration tokens `--t-slow: 0.9s`, used by CSS-only transitions too.

### A2. Homepage (`index.html` / `home.html`)

Section order and copy unchanged. Presentation rebuilt:

1. **Hero** — full-bleed local WebP (migrated from Squarespace CDN), layered scrim (radial pool, like jmassage hero treatment), h1 wrapped in `.line > .line-inner` mask spans (manual spans, no SplitText dependency), GSAP entrance: eyebrow fade-track-in → lines rise 110%→0 staggered 0.12s → lead + CTA fade-up. ScrollTrigger scrubbed parallax: image drifts y −8% over scroll; scrim constant.
2. **Stats band** — existing trust-bar content restyled as full-width `--ink-deep` strip; numerals in Marcellus `--type-2`, cream; `data-count` count-up on enter (only for numeric stats; non-numeric items fade).
3. **Services grid** — asymmetric editorial grid (CSS Grid, 12-col): two featured cards (Head Spa, Couples — distinct offerings) span 7/5 cols with image background + gradient overlay + hover image scale 1.04; remaining services in uniform 3-up grid below. All `data-reveal-stagger`.
4. **Reviews** — editorial pull-quotes: oversized Marcellus `"` glyph, larger quote type, attribution in eyebrow style; fade-stagger on enter. ★ glyphs keep existing convention.
5. **Final CTA band** — full-width `--ink-deep`, headline + `data-magnetic` button.

### A3. Service page template (`build_services.py` → regenerate 14 pages)

- Mini-hero: category eyebrow + h1 line-mask reveal + breadcrumb.
- Pricing: card treatment; 60-min row visually weighted (tint + slight scale + stronger border). NO new label text (copy is Andrew's; "Most booked" badge offered as future option).
- "Best for" list: staggered reveal.
- Related services: hover lift + shadow bloom, focus-visible ring.
- All sections `data-reveal`.
- Regeneration must preserve: canonicals, Service schema JSON-LD, titles/descriptions, all copy strings byte-identical.

### A4. Other pages

- `services.html`: same grid language as homepage services section; ItemList/Breadcrumb schema untouched.
- `faq.html`: GSAP smooth-height accordion replacing instant `<details>` jump (progressive enhancement on top of `<details>` so no-JS still works); FAQPage schema untouched.
- `contact.html`, `gift-cards.html`, `book.html`, `404.html`: page-header reveal treatment + consistent eyebrow/type upgrades; book.html Vagaro iframe + skeleton untouched.
- `cart.html`: leave as-is (legacy redirect).

### A5. Image migration

- Download hero WebP variants (2500/1500/750w) from Squarespace CDN → `assets/img/`, rewrite `srcset`/`og:image` to local absolute URLs.
- Favicon → local `assets/img/favicon.ico` (or 32px PNG), head links updated on all pages.
- Featured-card imagery: crops/treatments of the one real photo + color-block/texture design. No fabricated photography. Photo wishlist → `content-gaps.md`.
- Explicit `width`/`height` on all `<img>` for CLS 0; `fetchpriority="high"` + preload on hero.

### A6. Elite motion file (`assets/motion.js`)

See Part C shared architecture. Elite-specific wiring: hero timeline, stats count-up, grid staggers, magnetic CTA, FAQ accordion, header scroll state (backdrop blur + border on scroll — new for elite).

## Part B — J Massage (repo `~/jmassage-website`, branch `redesign-50k`)

1. **Hero choreography** — replace setTimeout chains in `js/main.js` hero block with one GSAP timeline: line masks rise + hero image scale-settle 1.06→1 (1.4s, organic ease) + eyebrow letter-track-in. Same visual language, tighter rhythm.
2. **Scroll parallax** — ScrollTrigger scrub on editorial images (`.editorial img`, service feature images): subtle y drift (±6%), desktop only via `gsap.matchMedia()`.
3. **Magnetic CTAs** — header `.nav__cta`, hero CTA, footer CTA. `pointer: fine` only.
4. **FAQ smooth accordion** — GSAP height tween on `.faq-item` open/close (service pages + faq.html + pricing.html), replacing class-toggle jump.
5. **Token fix** — `js/main.js` svc-card radial glow hardcoded `rgba(200,136,42,0.13)` → read from CSS custom property (clay `--lantern` family).
6. **Keep untouched** — reviews carousel, counters, IO `.reveal` system, cursor glow, mobile nav, gift-card tilt.
7. **No bounce/spring easing** (PRODUCT.md rule). UTF-8 on every edited file. ★ U+2605 convention preserved.

Vendor files at `js/vendor/gsap.min.js`, `js/vendor/ScrollTrigger.min.js`; `js/motion.js` for new choreography; existing `main.js`/`service-page.js` edited minimally.

## Part C — Shared motion architecture

- **Load order**: `<script defer src=".../gsap.min.js">` → `ScrollTrigger.min.js` → `motion.js` (defer preserves order).
- **Fail-safe rule (hard)**: initial hidden/offset states are set ONLY via `gsap.set()` inside motion.js. CSS never hides content. No JS / GSAP missing = fully visible static site. Zero CLS from motion.
- **Guard**: `if (!window.gsap || !window.ScrollTrigger) return;` at top of motion.js.
- **Reduced motion**: `gsap.matchMedia()` registers `(prefers-reduced-motion: no-preference)` for all tweens; reduce-preference contexts get instant `gsap.set` end-states. Existing CSS kill-switches stay.
- **Data-attribute API**: `data-reveal` (fade-up 28px), `data-reveal-stagger` (children stagger 0.1s), `data-parallax="0.08"`, `data-count="450"`, `data-magnetic`. Declarative — template-friendly.
- **Easing language**: `expo.out`/`power3.out`, durations 0.8–1.4s, staggers 0.08–0.12s. Slow, organic, breathing. Never snappy, never bouncy.
- **ScrollTrigger hygiene**: `once: true` for reveals (no re-trigger jank); scrubbed triggers desktop-only; `ScrollTrigger.refresh()` after font load.

## Part D — Guardrails (do not touch)

- Canonicals, all JSON-LD schema (NO AggregateRating anywhere), sitemap.xml, robots.txt, llms*.txt, `_redirects`, `_headers`, GA4 `G-HR9MP6ENEP` (jmassage only — elite gets none).
- Copy: byte-identical. Spelling/grammar issues found → flag, never fix.
- Booking funnel: Vagaro iframes untouched both sites.

## Part E — Verification (per site, before merge)

1. Local preview server → screenshots: 375 / 768 / 1280 px on homepage, one service page, faq, pricing/services, book.
2. Console: zero errors on every screenshotted page.
3. Reduced-motion emulation: content fully visible, no tweens.
4. JS-disabled check: content fully visible (fail-safe rule).
5. Lighthouse ≥90 all four categories on homepage + one service page.
6. jmassage: `file *.html` UTF-8 check post-edit; `git diff` reviewed for copy/schema deltas (expect none).
7. Elite: regenerated pages diffed — only intended template changes.
8. Internal links resolve; schema validates (structure unchanged = low risk).

## Part F — Risks

- **build_services.py regeneration drift** — mitigate: diff every regenerated page against main, assert copy/schema/canonical lines unchanged.
- **Squarespace image download fails** — fallback: keep CDN URLs this pass, note follow-up.
- **GSAP + existing jmassage IO reveals double-animating** — motion.js must not attach to `.reveal` classes on jmassage; only new attributes.
- **Pages auto-deploy on push to main** — all work on `redesign-50k`; main untouched until verification passes.

## Out of scope

Copy changes; new photography/video; Vagaro replacement; font self-hosting; GA4 for elite; review-schema re-add (needs real GBP counts); www→apex host-level 301s.
