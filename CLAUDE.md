# elitespautah.com — project instructions

Elite Spa Utah. Static HTML on Cloudflare Pages (git-connected: push to `main` = production deploy — use `/ship`).
NAP: (801) 839-8880 · 1136 S State Street, Salt Lake City UT 84111 · daily 10am–10pm · booking at /book (GHL).

## The one rule that matters
Service pages are GENERATED. Never hand-edit a generated `{slug}.html` — edit the `SERVICES` list in `build_services.py` and re-run `python build_services.py`. Hand edits get silently destroyed on the next regeneration.

## Topic ownership (shared strategy with J Massage SLC)
Elite owns facials, sauna, reflexology, head spa. Massage-modality topics belong to jmassageslc.com — never build the same keyword on both. The spa-blog / spa-gbp-post / spa-service-page skills enforce this; follow them for content work.

## Facts
- Pricing: standard $85/$125/$165 (60/90/120) · premium $165/$245/$325 · add-ons $30 (cupping $20) · prenatal 105/155/205.
- Photos: current brand imagery is AI-generated INTERIM (same-room continuity set) — replace when the real shoot lands. Never fabricate "real client" photos or reviews.
- Real rating: 4.8/249 on Google (synced 2026-08-26). Use real numbers only.
- Ambient video pattern: `ambient-video.js` (looping brand videos). Mobile gets the FULL cinematic tier — verify at 375px.
- GA4 currently shares J Massage's `G-HR9MP6ENEP` — Elite should get its OWN id (open task; don't propagate the shared one to new work).

## Verify
`node ~/projects/exclusiveut/tools/verify-elite.mjs` after layout/motion changes (harness lives in the exclusiveut repo on purpose).
