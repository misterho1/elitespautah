# Goal — Spa Sites $50k Elevation (2026-06-10)

## Goal
elitespautah.com and jmassageslc.com look and move like a $50,000 agency build: elite gets a structural visual redesign plus a full GSAP motion system; jmassage gets GSAP choreography layered onto its existing editorial design.

## Success criteria
- Elite: masked-line hero with entrance timeline + parallax, dark stats band with count-up, asymmetric featured-services grid, pull-quote reviews, magnetic CTAs, elevated service-page template (weighted 60-min pricing) across all 14 generated pages.
- jmassage: GSAP hero timeline (image settle + line masks), scrubbed editorial-image parallax, magnetic CTAs, smooth FAQ accordion; carousel/counters/cursor-glow untouched and still working.
- Both: self-hosted GSAP 3.13 (no CDN), no-JS and reduced-motion users see a complete static page, zero console errors, Lighthouse ≥90 in all four categories on homepage + one service page.
- Diffs prove copy, schema JSON-LD, canonicals, sitemaps, GA4 (jmassage) byte-identical.
- Elite serves zero assets from squarespace-cdn.com.
- Merged to main, auto-deployed, live-verified.

## Non-goals
Copy changes; new photography/video; Vagaro booking replacement; font self-hosting; GA4 for elite; AggregateRating re-add; www→apex host-level redirects.

## Constraints
- Work on `redesign-50k` branches; main = production (auto-deploy on push).
- jmassage files must stay UTF-8; ★ U+2605 star convention preserved.
- Easing slow/organic (expo/power3 out, 0.8–1.4s), no bounce (jmassage PRODUCT.md rule).
- Spec: docs/superpowers/specs/2026-06-10-spa-sites-50k-redesign-design.md (approved). Plan: docs/superpowers/plans/2026-06-10-spa-sites-50k-elevation.md.
