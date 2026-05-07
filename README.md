# elitespautah.com — Cloudflare Pages mirror

Static mirror of [elitespautah.com](https://www.elitespautah.com) (currently hosted on Squarespace), deployed to Cloudflare Pages from this repo.

## Status

**Phase 1: Visual mirror, deployed to `elitespautah.pages.dev`.**

The live elitespautah.com on Squarespace is unchanged and remains the system of record.

## Known limitations

This is a static mirror. Dynamic Squarespace features do not function:

- Contact form (visually present, submission does nothing)
- Booking widget (visually present, does not function)
- Squarespace member login, blog comments, search

Asset images, fonts, and component CSS continue to load from Squarespace's CDN (`images.squarespace-cdn.com`, `static1.squarespace.com`, `definitions.sqspcdn.com`).

## How the mirror was generated

```bash
python mirror.py
```

Pulls every URL listed in `https://www.elitespautah.com/sitemap.xml`, saves each as `<slug>.html` at repo root, and copies `home.html` → `index.html` so `/` works.

## Deploy

Cloudflare Pages auto-builds on push to `main`. No build command — pure static HTML served from repo root.

## Roadmap

- **Phase 2** — Inventory + rewire dynamic features (contact form, etc.) using Cloudflare Workers + email service
- **Phase 3** — DNS cutover from Squarespace to Cloudflare; cancel Squarespace subscription
