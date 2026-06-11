# Content Gaps — Elite Spa Utah

Items that need real content from Andrew. Do not fabricate any of these.

## Photography (highest impact)
The site has ONE real photo (the hero). The 2026-06 elevation works around this with
typographic/color-block design, but real photography would lift every page:

- Couples suite (two tables, dim lighting) — featured card + couples page
- Head spa in progress (washbasin/scalp work) — featured card + head spa page
- 2–3 treatment rooms (the "8+ private rooms" claim, shown)
- Reception / entry at 1136 S State
- Hot stone setup, cupping detail, sauna interior
- Therapist portrait(s) with permission

When supplied: drop into `assets/img/`, wire into `.svc-feature` cards as
`background-image`, and add per-service heroes to `build_services.py`.

## Optional copy decisions (Andrew owns copy)
- "Most booked" badge text for the visually weighted 60-min pricing row
  (currently weighted with color only, no label).
- Featured-service choice on homepage: currently Japanese Head Spa + Couples
  Massage. Swap targets if the business wants to push something else.

## Analytics
- Elite has NO analytics tag (jmassage's G-HR9MP6ENEP must NOT be used here).
  Needs its own GA4 property or Cloudflare Web Analytics decision.

## Reviews schema
- AggregateRating was removed 2026-05-31 (unverifiable). Re-add only with the
  real Google Business Profile review count + average once GBP is claimed.
