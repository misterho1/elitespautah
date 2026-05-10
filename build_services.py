"""Generate the 14 service detail pages from one template + service data.
Run from the project root: `python build_services.py`
Each service gets a clean ~5KB HTML file matching the homepage's design system."""

import os

# Universal pricing across every service (matches the live Vagaro pricing table):
#   30 min · $115   |   60 min · $165   |   90 min · $245   |   120 min · $325
UNIVERSAL_PRICES = [(30, "$115"), (60, "$165"), (90, "$245"), (120, "$325")]

SERVICES = [
    {
        "slug": "deep-tissue-massage",
        "name": "Deep Tissue Massage",
        "category": "For pain & tension",
        "tagline": "Targeted pressure for chronic tension.",
        "description": "Slow, deliberate strokes and firm pressure that reach the deeper layers of muscle and connective tissue. Unlike a relaxation massage, deep tissue targets the source of tension — the chronic adhesions that cause persistent pain.",
        "best_for": ["Chronic back pain", "Neck and shoulder tension", "Sports injuries and recovery", "IT band, hamstring, hip tightness"],
        "prices": UNIVERSAL_PRICES,
        "related": ["sports-massage", "hot-stone-massage", "ashiatsu-massage"],
    },
    {
        "slug": "swedish-massage",
        "name": "Swedish Massage",
        "category": "For stress & restoration",
        "tagline": "The classic, full-body unwind.",
        "description": "Long, flowing strokes designed to relax the whole nervous system. The default starting point for first-time clients and the easiest entry into regular bodywork.",
        "best_for": ["First-time massage clients", "Stress and overstimulation", "Better sleep", "Light muscle soreness"],
        "prices": UNIVERSAL_PRICES,
        "related": ["hot-stone-massage", "head-spa-massage", "foot-reflexology-massage"],
    },
    {
        "slug": "hot-stone-massage",
        "name": "Hot Stone Massage",
        "category": "For stress & restoration",
        "tagline": "Heated basalt stones reach deeper than hands alone.",
        "description": "Smooth basalt stones heated to a comforting temperature glide along the back, shoulders, and legs while your therapist works around them. The heat penetrates muscle layers your hands can't easily access.",
        "best_for": ["Cold weather aches", "Deep muscle warm-up", "Anxiety and tension", "Combining heat with massage"],
        "prices": UNIVERSAL_PRICES,
        "related": ["swedish-massage", "deep-tissue-massage", "medical-infrared-sauna"],
    },
    {
        "slug": "head-spa-massage",
        "name": "Japanese Head Spa",
        "category": "For stress & restoration",
        "tagline": "Scalp, neck, and shoulder ritual.",
        "description": "A scalp and neck ritual borrowed from Japanese spa tradition. Full-scalp treatment using rhythmic kneading and pressure-point work from the temples to the base of the skull. Most clients fall asleep.",
        "best_for": ["Tension headaches", "Migraines and screen fatigue", "Hair and scalp health", "Pure relaxation"],
        # Head spa runs its own pricing tier — not universal.
        "prices": [(30, "$60"), (60, "$85"), (90, "$125")],
        "related": ["swedish-massage", "couples-massage", "foot-reflexology-massage"],
    },
    {
        "slug": "couples-massage",
        "name": "Couples Massage",
        "category": "Specialty & couples",
        "tagline": "Two therapists. One private suite.",
        "description": "Side-by-side massage in our private couples suite. Two therapists working in sync, two tables, dim lighting. Anniversaries, date nights, traveling together — book the suite, not just the appointment.",
        "best_for": ["Date nights and anniversaries", "Traveling couples", "Pre-event reset", "Gift experiences"],
        "prices": UNIVERSAL_PRICES,
        "related": ["hot-stone-massage", "head-spa-massage", "swedish-massage"],
    },
    {
        "slug": "4-hands-massage",
        "name": "4-Hands Massage",
        "category": "Specialty & couples",
        "tagline": "Two therapists working in sync — on you.",
        "description": "Two therapists, one client, four hands moving in coordinated pressure. Covers double the body in the same time, and the sensory overload puts the nervous system in a state most single-therapist sessions never reach.",
        "best_for": ["Maximum bodywork in minimum time", "Special-occasion treatment", "Sensory escape", "Severe full-body tension"],
        "prices": UNIVERSAL_PRICES,
        "related": ["couples-massage", "hot-stone-massage", "deep-tissue-massage"],
    },
    {
        "slug": "foot-reflexology-massage",
        "name": "Foot Reflexology",
        "category": "Specialty & couples",
        "tagline": "Pressure-point work that resets the whole body.",
        "description": "Reflexology maps zones on the feet to organ systems and energy pathways throughout the body. Targeted pressure on these points releases tension you didn't know was there.",
        "best_for": ["Tired feet after long days", "Improved circulation", "Stress release without disrobing", "Pregnancy-safe relaxation"],
        "prices": UNIVERSAL_PRICES,
        "related": ["swedish-massage", "head-spa-massage", "shiatsu-massage"],
    },
    {
        "slug": "sports-massage",
        "name": "Sports Massage",
        "category": "For pain & tension",
        "tagline": "Active recovery for active bodies.",
        "description": "Deeper than Swedish, more dynamic than deep tissue. Combines stretching, compression, and targeted pressure to flush metabolic waste, restore range of motion, and prevent injury between training sessions.",
        "best_for": ["Athletes pre- and post-event", "Marathon and triathlon training", "CrossFit and Olympic lifting", "Climbers and skiers"],
        "prices": UNIVERSAL_PRICES,
        "related": ["deep-tissue-massage", "ashiatsu-massage", "cupping-therapy"],
    },
    {
        "slug": "ashiatsu-massage",
        "name": "Ashiatsu",
        "category": "For pain & tension",
        "tagline": "Deeper than hands can go.",
        "description": "Therapist applies pressure with their feet using overhead bars for balance. Reaches muscle depth that elbows and forearms can't access. Surprisingly precise, despite the name.",
        "best_for": ["Severe back tension", "Chronic shoulder bracing", "Athletes who can't get deep enough", "Larger-bodied clients"],
        "prices": UNIVERSAL_PRICES,
        "related": ["deep-tissue-massage", "sports-massage", "shiatsu-massage"],
    },
    {
        "slug": "shiatsu-massage",
        "name": "Shiatsu",
        "category": "For pain & tension",
        "tagline": "Japanese pressure-point therapy.",
        "description": "Originated in Japan, shiatsu uses thumb, palm, and finger pressure along the body's energy meridians. Performed clothed on a mat or table — no oil, no draping.",
        "best_for": ["Stiffness without soreness", "Energy and fatigue rebalance", "Clients who prefer clothed sessions", "First-time pressure-point work"],
        "prices": UNIVERSAL_PRICES,
        "related": ["foot-reflexology-massage", "ashiatsu-massage", "swedish-massage"],
    },
    {
        "slug": "cupping-therapy",
        "name": "Cupping Therapy",
        "category": "For stress & restoration",
        "tagline": "Suction releases what hands can't grab.",
        "description": "Silicone or glass cups create gentle suction that lifts skin and fascia, increasing blood flow and breaking up adhesions in tissue layers. Often paired with deep tissue or sports massage.",
        "best_for": ["Stubborn knots that resist pressure", "Lower back tension", "Post-injury circulation", "Athletic recovery"],
        "prices": UNIVERSAL_PRICES,
        "related": ["deep-tissue-massage", "sports-massage", "medical-infrared-sauna"],
    },
    {
        "slug": "chair-massage",
        "name": "Chair Massage",
        "category": "Specialty & couples",
        "tagline": "Focused neck and shoulder reset.",
        "description": "Fully clothed, focused work on the neck, shoulders, upper back, and arms. Perfect for a between-meetings break or a first try if you've never had bodywork.",
        "best_for": ["Lunch breaks", "First-time clients", "Office workers and screen-staring", "Quick stress relief"],
        "prices": UNIVERSAL_PRICES,
        "related": ["foot-reflexology-massage", "swedish-massage", "shiatsu-massage"],
    },
    {
        "slug": "individual-massage",
        "name": "Individual Massage",
        "category": "Specialty & couples",
        "tagline": "Customized session, single therapist.",
        "description": "Show up, talk to your therapist about what hurts, and get a custom blend of techniques tailored to that day. Most regular clients eventually default to this — they trust their therapist to read the room.",
        "best_for": ["Returning clients", "Mixed needs (some tension, some relaxation)", "When you don't want to choose", "Open-ended pampering"],
        "prices": UNIVERSAL_PRICES,
        "related": ["swedish-massage", "deep-tissue-massage", "head-spa-massage"],
    },
    {
        "slug": "medical-infrared-sauna",
        "name": "Medical Infrared Sauna",
        "category": "Specialty & couples",
        "tagline": "Detox and recovery via medical-grade infrared.",
        "description": "Infrared light penetrates deeper than traditional sauna heat — warming muscles directly rather than just the air around you. Pairs perfectly with massage as a pre-session warmup or as a standalone recovery session.",
        "best_for": ["Post-workout recovery", "Cold winter days", "Skin and circulation", "Pre-massage muscle warm-up"],
        "prices": UNIVERSAL_PRICES,
        "related": ["hot-stone-massage", "deep-tissue-massage", "cupping-therapy"],
    },
]

# Build slug -> name lookup for related services rendering
SLUG_TO_NAME = {s["slug"]: s["name"] for s in SERVICES}

PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name} — Elite Spa Utah, Salt Lake City</title>
  <meta name="description" content="{name} at Elite Spa Utah, Salt Lake City. {tagline} From {price_from}. Same-day appointments. Licensed therapists. 1136 S State Street.">
  <link rel="canonical" href="https://elitespautah.com/{slug}">
  <meta property="og:title" content="{name} — Elite Spa Utah">
  <meta property="og:description" content="{tagline} From {price_from}. Same-day appointments at 1136 S State Street.">
  <meta property="og:url" content="https://elitespautah.com/{slug}">
  <meta property="og:image" content="https://images.squarespace-cdn.com/content/v1/69a71f3d2ea46264ee9697f6/9ca02977-91cd-4d36-bd3b-3abfadfe3062/elite-spa-massage-salt-lake-city-utah.webp?format=1500w">
  <link rel="icon" type="image/x-icon" href="https://images.squarespace-cdn.com/content/v1/69a71f3d2ea46264ee9697f6/1615344f-dadc-44d5-9f23-81eb568f09a1/favicon.ico?format=100w">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Marcellus&family=PT+Serif:wght@400;700&display=swap">
  <link rel="stylesheet" href="/assets/styles.css?v=2">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "{name}",
    "provider": {{ "@type": "MassageTherapist", "name": "Elite Spa Utah", "url": "https://elitespautah.com/", "telephone": "+18018398880", "address": {{ "@type": "PostalAddress", "streetAddress": "1136 S State St", "addressLocality": "Salt Lake City", "addressRegion": "UT", "postalCode": "84111", "addressCountry": "US" }} }},
    "areaServed": {{ "@type": "City", "name": "Salt Lake City" }},
    "offers": {{ "@type": "Offer", "price": "{price_from_num}", "priceCurrency": "USD", "url": "https://elitespautah.com/book" }}
  }}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="site-header__brand" href="/">Elite Spa Utah</a>
      <nav class="site-nav" aria-label="Primary">
        <button class="site-nav__menu-toggle" type="button" aria-label="Toggle menu" aria-expanded="false" aria-controls="primary-nav">☰</button>
        <ul class="site-nav__list" id="primary-nav">
          <li><a class="site-nav__link" href="/services">Services</a></li>
          <li><a class="site-nav__link" href="/gift-cards">Gift Cards</a></li>
          <li><a class="site-nav__link" href="/faq">FAQ</a></li>
          <li><a class="site-nav__link" href="/contact">Contact</a></li>
          <li><a class="site-nav__link" href="tel:+18018398880">(801) 839-8880</a></li>
          <li><a class="btn btn--primary" href="/book">Book Now</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
    <section class="page-header">
      <div class="container container--narrow">
        <p class="eyebrow">{category}</p>
        <h1>{name}</h1>
        <p class="lead">{tagline}</p>
        <p style="margin-top: var(--space-3)">
          <a class="btn btn--primary" href="/book">Book Now</a>
          <a class="btn btn--secondary" href="tel:+18018398880" style="margin-left: var(--space-1)">Call (801) 839-8880</a>
        </p>
      </div>
    </section>

    <section class="container container--content section">
      <div class="cols-2">
        <div>
          <h2>What it does</h2>
          <p>{description}</p>
          <h3 style="margin-top: var(--space-4); font-size: var(--type-4); font-family: var(--type-ui); font-weight: 500; letter-spacing: 0;">Best for</h3>
          <ul style="padding-left: 1.2em; color: var(--ink-muted); line-height: 1.7;">
{best_for_html}
          </ul>
        </div>
        <div>
          <h2>Pricing</h2>
          <div class="price-table">
{prices_html}
          </div>
          <p style="margin-top: var(--space-3); font-size: var(--type-7); color: var(--ink-dim);">Add-ons (hot stones, aromatherapy, infrared sauna) at booking.</p>
          <p style="margin-top: var(--space-3)">
            <a class="btn btn--primary" href="/book">Book {name}</a>
          </p>
        </div>
      </div>
    </section>

    <section class="section section--cream">
      <div class="container">
        <p class="eyebrow">Pairs well with</p>
        <h2>Related services</h2>
        <div class="service-grid" style="margin-top: var(--space-3);">
{related_html}
        </div>
      </div>
    </section>

    <section class="cta-band container">
      <h2 class="cta-band__heading">Ready when you are.</h2>
      <p class="cta-band__text">Same-day appointments available. Open daily, 10am to 10pm.</p>
      <div class="cluster cluster--center">
        <a class="btn btn--primary" href="/book">Book Now</a>
        <a class="btn btn--secondary" href="tel:+18018398880">Call (801) 839-8880</a>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="site-footer__grid">
        <div>
          <p class="site-footer__brand">Elite Spa Utah</p>
          <p style="max-width: 36ch;">Salt Lake City's elevated massage therapy and spa. Licensed therapists, private rooms, same-day appointments.</p>
        </div>
        <div>
          <p class="site-footer__heading">Hours</p>
          <p>Mon–Sun<br>10AM–10PM</p>
        </div>
        <div>
          <p class="site-footer__heading">Location</p>
          <p>1136 S State Street<br>Salt Lake City, UT 84111</p>
        </div>
        <div>
          <p class="site-footer__heading">Contact</p>
          <ul class="site-footer__list">
            <li><a href="tel:+18018398880">(801) 839-8880</a></li>
            <li><a href="/book">Book online</a></li>
            <li><a href="/contact">Contact form</a></li>
          </ul>
        </div>
      </div>
      <div class="site-footer__legal">
        <span>© 2026 Elite Spa Utah · Operated by J Massage LLC</span>
        <span>Licensed massage therapists, State of Utah</span>
      </div>
    </div>
  </footer>

  <script src="/assets/nav.js?v=2" defer></script>
</body>
</html>
'''


def render_best_for(items):
    return "\n".join(f"            <li>{item}</li>" for item in items)


def render_prices(prices):
    return "\n".join(
        f'            <div class="price-row"><p class="price-row__name">{minutes} min</p><span class="price-row__time">{minutes} minutes</span><span class="price-row__amount">{price}</span></div>'
        for minutes, price in prices
    )


def render_related(related_slugs, services_by_slug):
    return "\n".join(
        f'          <a class="service-card" href="/{slug}"><h3 class="service-card__title">{services_by_slug[slug]}</h3><p class="service-card__desc">View details and pricing →</p></a>'
        for slug in related_slugs
    )


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    for s in SERVICES:
        price_from = s["prices"][0][1]
        price_from_num = price_from.replace("$", "").replace(",", "")
        html = PAGE_TEMPLATE.format(
            slug=s["slug"],
            name=s["name"],
            category=s["category"],
            tagline=s["tagline"],
            description=s["description"],
            best_for_html=render_best_for(s["best_for"]),
            prices_html=render_prices(s["prices"]),
            related_html=render_related(s["related"], SLUG_TO_NAME),
            price_from=price_from,
            price_from_num=price_from_num,
        )
        path = os.path.join(out_dir, f"{s['slug']}.html")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print(f"  wrote {s['slug']}.html ({len(html)} bytes)")


if __name__ == "__main__":
    main()
