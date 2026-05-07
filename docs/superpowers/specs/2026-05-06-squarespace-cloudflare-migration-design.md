# elitespautah.com — Squarespace → Cloudflare Pages Migration (Phase 1)

**Date:** 2026-05-06
**Owner:** Andrew Ho (`misterho1` on GitHub)
**Source:** elitespautah.com (currently hosted on Squarespace)
**Target:** Cloudflare Pages, deployed from public GitHub repo `misterho1/elitespautah`

## Goal

Get a static, visually-identical mirror of elitespautah.com running on Cloudflare Pages at `elitespautah.pages.dev`, deployed continuously from a public GitHub repo. **Phase 1 only** — no DNS cutover, no form rewiring, no Squarespace cancellation. The live elitespautah.com on Squarespace stays untouched.

## Non-goals (deferred to later phases)

- Migrating the elitespautah.com domain DNS to Cloudflare
- Rewiring contact forms, booking widgets, or any dynamic Squarespace features
- Cancelling the Squarespace subscription
- SEO preservation (sitemap regeneration, redirect maps)
- Email / MX record review

## Architecture

```
elitespautah.com (Squarespace, untouched)
        │
        ▼ wget --mirror (read-only fetch)
C:\Users\goho2\Desktop\elitespautah\elitespautah.com\
        │
        ▼ flatten to repo root + cleanup
C:\Users\goho2\Desktop\elitespautah\  (git working tree)
        │
        ▼ git push
github.com/misterho1/elitespautah  (public repo)
        │
        ▼ Cloudflare Pages connects to repo
elitespautah.pages.dev
```

## Steps

1. **Mirror** — `wget --mirror --convert-links --adjust-extension --page-requisites --no-parent --user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'` against `https://elitespautah.com/`. Output to `C:\Users\goho2\Desktop\elitespautah\elitespautah.com\`.
2. **Flatten** — move contents of `elitespautah.com/` up one level to repo root so Cloudflare Pages serves `index.html` directly.
3. **Cleanup pass** — strip Squarespace analytics/tracking script tags that will 404 (`squarespace-cdn.com` telemetry, `static1.squarespace.com/` tracking pixels). Convert any remaining absolute `https://elitespautah.com/...` URLs to relative paths.
4. **Smoke test** — open `index.html` locally, click through the major pages, watch browser console for unexpected 404s. Note any surviving Squarespace-specific failures as Phase 2 backlog (don't fix them in Phase 1).
5. **Add `.gitignore` and `README.md`** — minimal `.gitignore` (exclude `*.log`, `.DS_Store`, etc.) and a one-line README noting this is a static mirror of elitespautah.com.
6. **Git init + initial commit** — single commit, message: `Initial mirror of elitespautah.com from Squarespace`.
7. **Create GitHub repo** — `gh repo create misterho1/elitespautah --public --source=. --push`. Description: "Static mirror of elitespautah.com — Squarespace → Cloudflare Pages migration".
8. **Connect Cloudflare Pages** — use Cloudflare MCP to create a Pages project named `elitespautah`, source from GitHub repo `misterho1/elitespautah`, branch `main`. No build command (it's pure static HTML), output directory: `/`.
9. **Verify** — open `https://elitespautah.pages.dev`, confirm it loads, spot-check 3–5 pages match the live Squarespace site.

## Known limitations after Phase 1

These are **expected** outcomes, not bugs:

- Contact form: visually present, submission silently fails
- Booking widget: visually present, will not function (already neutralized to phone redirect per recent Squarespace edits, so likely a non-issue)
- Squarespace member login / blog comments / search: broken
- Squarespace-injected analytics: removed in cleanup
- Sitemap.xml may be stale or missing (Squarespace generates dynamically)

## Risk + reversibility

- **Risk: zero to live site.** Phase 1 is read-only against Squarespace. Squarespace stays the system of record until Phase 3.
- **Repo is public** — per user choice. No secrets, credentials, or `.env` files will be committed. Mirrored HTML is already public.
- **Rollback:** if anything goes wrong, delete the Cloudflare Pages project and the GitHub repo. Live elitespautah.com is unaffected.

## Open questions deferred to Phase 2

- What dynamic features does the Squarespace site have? (will inventory from the mirror)
- What email service handles `@elitespautah.com` mail, and where are the MX records?
- Form rewire: Cloudflare Worker + Resend, or Formspree, or another approach?

## Success criteria

1. `https://elitespautah.pages.dev` loads and renders the homepage visually identical to the live Squarespace site.
2. At least the homepage and 3 key inner pages (services, booking, contact, about — whichever exist) load without obvious layout breakage.
3. Public GitHub repo `misterho1/elitespautah` exists and is the source for Cloudflare Pages.
4. No DNS changes have been made to elitespautah.com.
