"""Generate the 14 service detail pages from one template + service data.
Run from the project root: `python build_services.py`
Each service gets a clean ~5KB HTML file matching the homepage's design system."""

import os

# Tiered pricing (2026-06-13 restructure). No 30-minute sessions.
STANDARD_PRICES = [(60, "$85"), (90, "$125"), (120, "$165")]
PREMIUM_PRICES  = [(60, "$165"), (90, "$245"), (120, "$325")]   # couples, 4-hand
SINGLE_HOUR     = [(60, "$85")]                                 # foot reflexology, head spa

SERVICES = [
    {
        "slug": "deep-tissue-massage",
        "name": "Deep Tissue Massage",
        "category": "For pain & tension",
        "tagline": "Targeted pressure for chronic tension.",
        "description": "Slow, deliberate strokes and firm pressure that reach the deeper layers of muscle and connective tissue. Unlike a relaxation massage, deep tissue targets the source of tension, the chronic adhesions that cause persistent pain.",
        "best_for": ["Chronic back pain", "Neck and shoulder tension", "Sports injuries and recovery", "IT band, hamstring, hip tightness"],
        "prices": STANDARD_PRICES,
        "related": ["sports-massage", "shiatsu-massage", "ashiatsu-massage"],
    },
    {
        "slug": "swedish-massage",
        "name": "Swedish Massage",
        "category": "For stress & restoration",
        "tagline": "The classic, full-body unwind.",
        "description": "Long, flowing strokes designed to relax the whole nervous system. The default starting point for first-time clients and the easiest entry into regular bodywork.",
        "best_for": ["First-time massage clients", "Stress and overstimulation", "Better sleep", "Light muscle soreness"],
        "prices": STANDARD_PRICES,
        "related": ["head-spa-massage", "foot-reflexology-massage", "individual-massage"],
    },
    {
        "slug": "head-spa-massage",
        "name": "Japanese Head Spa",
        "category": "For stress & restoration",
        "tagline": "Scalp, neck, and shoulder ritual.",
        "description": "A scalp and neck ritual borrowed from Japanese spa tradition. Full-scalp treatment using rhythmic kneading and pressure-point work from the temples to the base of the skull. Most clients fall asleep.",
        "best_for": ["Tension headaches", "Migraines and screen fatigue", "Hair and scalp health", "Pure relaxation"],
        "prices": SINGLE_HOUR,
        "extra": [
            ("What a Japanese head spa actually is", [
                "A Japanese head spa is a slow, deliberate treatment for your scalp, neck, and shoulders. It borrows from a spa tradition that has been popular in Japan for years and is only now catching on in Salt Lake City. Instead of the quick scalp rub you might get at the end of a haircut, this is a full session dedicated to one of the most tension-holding, most neglected parts of the body: the head.",
                "Your therapist works through the scalp with rhythmic kneading and pressure-point work, from the temples and hairline to the base of the skull, then eases down into the neck and shoulders where so much screen-and-desk tension quietly settles. Most people go somewhere very far away in their head about ten minutes in. A lot of them fall asleep.",
            ]),
            ("What to expect, step by step", [
                "You will be face-up and fully draped on a warm table in a private room. There is no haircut, no styling, and nothing you need to do but breathe.",
                "The session opens with slow neck and shoulder work to settle your nervous system. From there your therapist moves to the scalp, covering the whole head in sections with steady pressure and small circular movements. Warm oil is optional. The pace stays unhurried the entire time, and pressure is always dialed to what feels good to you, never past it.",
                "You leave loose, a little dreamy, and usually surprised at how much tension you were carrying above the neck. Give yourself a few quiet minutes before you drive.",
            ]),
            ("Japanese head spa vs. a regular scalp massage", [
                "A scalp massage is a nice add-on. A Japanese head spa is the whole experience. The difference is time, intention, and range: a dedicated session that treats the scalp, neck, and shoulders as one connected area rather than an afterthought at the end of another service.",
                "That is why people book it on its own, and why it pairs so well with a foot reflexology session or a full-body massage when you want to make an afternoon of it.",
            ]),
            ("Why Salt Lake City is booking head spa", [
                "Demand for Japanese head spa is climbing fast, and very few studios in Salt Lake City actually offer it well. If you have seen it on your feed and wanted to try one without flying to the coast, this is the place to do it. We keep same-day slots open most days.",
            ]),
            ("Who it is for", [
                "Anyone who lives on a screen, sleeps poorly, carries stress in the neck and shoulders, or simply wants an hour of deep quiet. It is a favorite for a first spa visit because there is nothing to figure out, and a favorite gift because almost no one has had one and everyone remembers their first.",
            ]),
        ],
        "faqs": [
            ("How long is a Japanese head spa session?", "Our head spa is a 60-minute session for $85. That gives your therapist time to cover the scalp, neck, and shoulders without rushing."),
            ("Will my hair be wet or styled afterward?", "This is a dry, oil-optional treatment focused on the scalp and muscles, not a wash-and-blowout. If we use a little oil at your request, your hair may feel conditioned afterward. Bring a hair tie if you like."),
            ("Is a head spa good for tension headaches?", "Many clients come in specifically because they hold tension in the scalp, jaw, and neck, and they leave feeling lighter. We keep the work relaxing rather than clinical; if you have a medical concern, check with your doctor."),
            ("Can I add it to a massage?", "Yes. A head spa pairs beautifully with a full-body massage or foot reflexology. Book them back to back, or add a 30-minute infrared sauna at checkout."),
            ("Do you offer same-day appointments?", "Most days, yes. Call (801) 839-8880 or book online; same-day slots appear automatically when a therapist is open."),
        ],
        "related": ["swedish-massage", "couples-massage", "foot-reflexology-massage"],
    },
    {
        "slug": "couples-massage",
        "name": "Couples Massage",
        "category": "Specialty & couples",
        "tagline": "Two therapists. One private suite.",
        "description": "Side-by-side massage in our private couples suite. Two therapists working in sync, two tables, dim lighting. Anniversaries, date nights, traveling together. Book the suite, not just the appointment.",
        "best_for": ["Date nights and anniversaries", "Traveling couples", "Pre-event reset", "Gift experiences"],
        "prices": PREMIUM_PRICES,
        "related": ["4-hands-massage", "head-spa-massage", "swedish-massage"],
    },
    {
        "slug": "4-hands-massage",
        "name": "4-Hands Massage",
        "category": "Specialty & couples",
        "tagline": "Two therapists working in sync, on you.",
        "description": "Two therapists, one client, four hands moving in coordinated pressure. Covers double the body in the same time, and the sensory overload puts the nervous system in a state most single-therapist sessions never reach.",
        "best_for": ["Maximum bodywork in minimum time", "Special-occasion treatment", "Sensory escape", "Severe full-body tension"],
        "prices": PREMIUM_PRICES,
        "related": ["couples-massage", "swedish-massage", "deep-tissue-massage"],
    },
    {
        "slug": "foot-reflexology-massage",
        "name": "Foot Reflexology",
        "category": "Specialty & couples",
        "tagline": "Pressure-point work that resets the whole body.",
        "description": "Reflexology maps zones on the feet to organ systems and energy pathways throughout the body. Targeted pressure on these points releases tension you didn't know was there.",
        "best_for": ["Tired feet after long days", "Improved circulation", "Stress release without disrobing", "Pregnancy-safe relaxation"],
        "prices": SINGLE_HOUR,
        "related": ["swedish-massage", "head-spa-massage", "shiatsu-massage"],
    },
    {
        "slug": "sports-massage",
        "name": "Sports Massage",
        "category": "For pain & tension",
        "tagline": "Active recovery for active bodies.",
        "description": "Deeper than Swedish, more dynamic than deep tissue. Combines stretching, compression, and targeted pressure to flush metabolic waste, restore range of motion, and prevent injury between training sessions.",
        "best_for": ["Athletes pre- and post-event", "Marathon and triathlon training", "CrossFit and Olympic lifting", "Climbers and skiers"],
        "prices": STANDARD_PRICES,
        "related": ["deep-tissue-massage", "ashiatsu-massage", "shiatsu-massage"],
    },
    {
        "slug": "ashiatsu-massage",
        "name": "Ashiatsu",
        "category": "For pain & tension",
        "tagline": "Deeper than hands can go.",
        "description": "Therapist applies pressure with their feet using overhead bars for balance. Reaches muscle depth that elbows and forearms can't access. Surprisingly precise, despite the name.",
        "best_for": ["Severe back tension", "Chronic shoulder bracing", "Athletes who can't get deep enough", "Larger-bodied clients"],
        "prices": STANDARD_PRICES,
        "related": ["deep-tissue-massage", "sports-massage", "shiatsu-massage"],
    },
    {
        "slug": "shiatsu-massage",
        "name": "Shiatsu",
        "category": "For pain & tension",
        "tagline": "Japanese pressure-point therapy.",
        "description": "Originated in Japan, shiatsu uses thumb, palm, and finger pressure along the body's energy meridians. Performed clothed on a mat or table, no oil, no draping.",
        "best_for": ["Stiffness without soreness", "Energy and fatigue rebalance", "Clients who prefer clothed sessions", "First-time pressure-point work"],
        "prices": STANDARD_PRICES,
        "related": ["foot-reflexology-massage", "ashiatsu-massage", "swedish-massage"],
    },
    {
        "slug": "chair-massage",
        "name": "Chair Massage",
        "category": "Specialty & couples",
        "tagline": "Focused neck and shoulder reset.",
        "description": "Fully clothed, focused work on the neck, shoulders, upper back, and arms. Perfect for a between-meetings break or a first try if you've never had bodywork.",
        "best_for": ["Lunch breaks", "First-time clients", "Office workers and screen-staring", "Quick stress relief"],
        "prices": STANDARD_PRICES,
        "related": ["foot-reflexology-massage", "swedish-massage", "shiatsu-massage"],
    },
    {
        "slug": "individual-massage",
        "name": "Individual Massage",
        "category": "Specialty & couples",
        "tagline": "Customized session, single therapist.",
        "description": "Show up, talk to your therapist about what hurts, and get a custom blend of techniques tailored to that day. Most regular clients eventually default to this; they trust their therapist to read the room.",
        "best_for": ["Returning clients", "Mixed needs (some tension, some relaxation)", "When you don't want to choose", "Open-ended pampering"],
        "prices": STANDARD_PRICES,
        "related": ["swedish-massage", "deep-tissue-massage", "head-spa-massage"],
    },
    {
        "slug": "prenatal-massage",
        "name": "Prenatal Massage",
        "category": "For stress & restoration",
        "tagline": "Safe, supportive bodywork through pregnancy.",
        "description": "Gentle, side-lying massage tailored to each trimester. Relieves the lower-back, hip, and leg tension pregnancy brings, improves circulation, and gives you a calm hour to rest. Performed by therapists experienced in prenatal positioning and pressure.",
        "best_for": ["Second- and third-trimester aches", "Lower back and hip relief", "Swelling and circulation", "Stress and better sleep"],
        "prices": STANDARD_PRICES,
        "related": ["swedish-massage", "individual-massage", "foot-reflexology-massage"],
    },
]

# Build slug -> name lookup for related services rendering
SLUG_TO_NAME = {s["slug"]: s["name"] for s in SERVICES}

# Service-page hero photography. Per-service brand shots generated 2026-07-05
# (Higgsfield nano_banana_pro, seeded from the homepage hero for one exposure
# family: warm candlelit amber, terracotta + cream). Swap freely for real
# Elite Spa photography later — keep the alt text.
DEFAULT_HERO = {
    "img": "treatment-room.webp", "w": 1376, "h": 768,
    "alt": "Warm, dimly lit private massage room with a draped table at Elite Spa Utah",
}
HERO_IMAGES = {
    "deep-tissue-massage": {
        "img": "deep-tissue.webp", "w": 2752, "h": 1536,
        "alt": "Therapist applying firm forearm pressure along a client's upper back during a deep tissue massage at Elite Spa Utah",
    },
    "swedish-massage": {
        "img": "swedish.webp", "w": 2752, "h": 1536,
        "alt": "Long, flowing Swedish massage strokes across the shoulders in a candlelit private room at Elite Spa Utah",
    },
    "head-spa-massage": {
        "img": "head-spa.webp", "w": 2752, "h": 1536,
        "alt": "Client fully draped and face-up receiving a Japanese head spa scalp ritual at Elite Spa Utah",
    },
    "foot-reflexology-massage": {
        "img": "foot-reflexology.webp", "w": 2752, "h": 1536,
        "alt": "Therapist pressing thumbs into the arch of a client's foot during reflexology at Elite Spa Utah",
    },
    "ashiatsu-massage": {
        "img": "ashiatsu.webp", "w": 2752, "h": 1536,
        "alt": "Ashiatsu therapist holding overhead bars while gliding barefoot pressure along a client's draped back at Elite Spa Utah",
    },
    "prenatal-massage": {
        "img": "prenatal.webp", "w": 2752, "h": 1536,
        "alt": "Pregnant client resting on her side, supported by bolster pillows during a prenatal massage at Elite Spa Utah",
    },
    "sports-massage": {
        "img": "sports.webp", "w": 2752, "h": 1536,
        "alt": "Therapist guiding an assisted shoulder stretch during a sports massage at Elite Spa Utah",
    },
    "individual-massage": {
        "img": "oil-ritual.webp", "w": 2752, "h": 1536,
        "alt": "Warm massage oil poured into a therapist's palm above a terracotta dish at Elite Spa Utah",
    },
    "couples-massage": {
        "img": "couples-suite.webp", "w": 2752, "h": 1536,
        "alt": "Private couples suite with two side-by-side massage tables at Elite Spa Utah",
    },
}

# Optional ambient hero video per service (lazy-loaded over the hero photo by
# assets/ambient-video.js; the photo stays the LCP + reduced-motion fallback).
HERO_VIDEOS = {
    "head-spa-massage": "/assets/vid/head-spa-ambient.mp4",
}

# Keyword clusters per service (primary phrase first). Used in meta description +
# keywords tag. Primary leads the description for relevance/CTR; no body stuffing.
KEYWORDS = {
    "deep-tissue-massage": ["Deep tissue massage in Salt Lake City", "sports recovery massage", "chronic back pain relief", "muscle knot therapy"],
    "swedish-massage": ["Swedish massage in Salt Lake City", "relaxation massage", "full-body massage", "first-time massage"],
    "head-spa-massage": ["Japanese head spa in Salt Lake City", "scalp massage", "tension headache relief", "head spa treatment"],
    "couples-massage": ["Couples massage in Salt Lake City", "couples spa suite", "date-night massage", "side-by-side massage"],
    "4-hands-massage": ["4-hands massage in Salt Lake City", "four-hand massage", "two-therapist massage"],
    "foot-reflexology-massage": ["Foot reflexology in Salt Lake City", "reflexology massage", "pressure-point foot massage"],
    "sports-massage": ["Sports massage in Salt Lake City", "athletic recovery massage", "post-workout massage", "pre-event massage"],
    "ashiatsu-massage": ["Ashiatsu massage in Salt Lake City", "deep-pressure massage", "barefoot massage therapy"],
    "shiatsu-massage": ["Shiatsu massage in Salt Lake City", "pressure-point therapy", "clothed massage", "Japanese massage"],
    "chair-massage": ["Chair massage in Salt Lake City", "office chair massage", "neck and shoulder massage", "quick massage"],
    "individual-massage": ["Custom massage in Salt Lake City", "personalized massage session", "tailored bodywork"],
    "prenatal-massage": ["Prenatal massage in Salt Lake City", "pregnancy massage", "side-lying massage", "maternity massage"],
}

PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name} · Elite Spa Utah, Salt Lake City</title>
  <meta name="description" content="{kw_primary} at Elite Spa Utah. {tagline} From {price_from}. Same-day appointments. Licensed therapists. 1136 S State Street, Salt Lake City.">
  <meta name="keywords" content="{kw_csv}">
  <link rel="canonical" href="https://elitespautah.com/{slug}">
  <meta property="og:title" content="{name} · Elite Spa Utah">
  <meta property="og:description" content="{tagline} From {price_from}. Same-day appointments at 1136 S State Street.">
  <meta property="og:url" content="https://elitespautah.com/{slug}">
  <meta property="og:image" content="https://elitespautah.com/assets/img/hero-1500.webp">
  <link rel="icon" type="image/x-icon" href="/assets/img/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Marcellus&family=PT+Serif:wght@400;700&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Marcellus&family=PT+Serif:wght@400;700&display=swap"></noscript>
  <link rel="stylesheet" href="/assets/styles.css?v=3">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Service",
        "serviceType": "{name}",
        "provider": {{ "@type": "MassageTherapist", "name": "Elite Spa Utah", "url": "https://elitespautah.com/", "telephone": "+18018398880", "address": {{ "@type": "PostalAddress", "streetAddress": "1136 S State Street", "addressLocality": "Salt Lake City", "addressRegion": "UT", "postalCode": "84111", "addressCountry": "US" }} }},
        "areaServed": {{ "@type": "City", "name": "Salt Lake City" }},
        "offers": {{ "@type": "Offer", "price": "{price_from_num}", "priceCurrency": "USD", "url": "https://elitespautah.com/book" }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://elitespautah.com/" }},
          {{ "@type": "ListItem", "position": 2, "name": "Services", "item": "https://elitespautah.com/services" }},
          {{ "@type": "ListItem", "position": 3, "name": "{name}", "item": "https://elitespautah.com/{slug}" }}
        ]
      }}
    ]
  }}
  </script>
{faq_schema}
  <!-- Motion + chat widget are deferred off the first-paint path (idle /
       first-interaction). See assets/defer-load.js. The page is fully visible
       and usable without JS, so static service pages no longer ship ~116KB of
       GSAP eagerly. -->
  <script src="/assets/defer-load.js?v=1" defer></script>
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
          <li><a class="site-nav__link" href="/pricing">Pricing</a></li>
          <li><a class="site-nav__link" href="/reviews">Reviews</a></li>
          <li><a class="site-nav__link" href="/about">About</a></li>
          <li><a class="site-nav__link" href="/gift-cards">Gift Cards</a></li>
          <li><a class="site-nav__link" href="/faq">FAQ</a></li>
          <li><a class="site-nav__link" href="/contact">Contact</a></li>
          <li><a class="site-nav__link" href="tel:+18018398880">(801) 839-8880</a></li>
          <li><a class="btn btn--primary" href="/book" data-magnetic>Book Now</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
    <section class="page-header" data-hero>
      <div class="container container--narrow">
        <p class="eyebrow">{category}</p>
        <h1><span class="line"><span class="line-inner">{name}</span></span></h1>
        <p class="lead">{tagline}</p>
        <p style="margin-top: var(--space-3)" data-hero-cta>
          <a class="btn btn--primary" href="/book" data-magnetic>Book Now</a>
          <a class="btn btn--secondary" href="tel:+18018398880" style="margin-left: var(--space-1)">Call (801) 839-8880</a>
        </p>
      </div>
    </section>

    <figure class="svc-hero-media{hero_media_class}" data-reveal>
      <img src="/assets/img/{hero_img}" alt="{hero_alt}" width="{hero_w}" height="{hero_h}" loading="eager" decoding="async">{hero_video_tag}
    </figure>

    <section class="container container--content section">
      <div class="cols-2">
        <div>
          <h2 data-reveal>What it does</h2>
          <p data-reveal>{description}</p>
          <h3 class="svc-subhead" data-reveal>Best for</h3>
          <ul class="svc-best-for" data-reveal-stagger>
{best_for_html}
          </ul>
        </div>
        <div>
          <h2 data-reveal>Pricing</h2>
          <div class="price-table" data-reveal>
{prices_html}
          </div>
          <p class="svc-note">Add-ons · hot stones $20; cupping, infrared sauna (30 min), or CBD $30 each, added at booking.</p>
          <p style="margin-top: var(--space-3)">
            <a class="btn btn--primary" href="/book">Book {name}</a>
          </p>
        </div>
      </div>
    </section>
{extra_section}
    <section class="section section--cream">
      <div class="container">
        <p class="eyebrow" data-reveal>Pairs well with</p>
        <h2 data-reveal>Related services</h2>
        <div class="service-grid" style="margin-top: var(--space-3);" data-reveal-stagger>
{related_html}
        </div>
      </div>
    </section>
{faq_section}
    <section class="band-dark">
      <div class="cta-band container">
      <h2 class="cta-band__heading" data-reveal>Ready when you are.</h2>
      <p class="cta-band__text" data-reveal>Same-day appointments available. Open daily, 10am to 10pm.</p>
      <div class="cluster cluster--center" data-reveal>
        <a class="btn btn--primary" href="/book" data-magnetic>Book Now</a>
        <a class="btn btn--ghost btn--on-dark" href="tel:+18018398880">Call (801) 839-8880</a>
      </div>
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

  <script src="/assets/nav.js?v=2" defer></script>{ambient_script}
  <!-- GoHighLevel chat widget is injected by assets/defer-load.js on first
       interaction (or idle) so it never competes with first paint. -->
</body>
</html>
'''


def render_best_for(items):
    return "\n".join(f"            <li>{item}</li>" for item in items)


def render_prices(prices):
    # 60 min is the most-booked duration, visually weighted, no copy change.
    return "\n".join(
        f'            <div class="price-row{" price-row--featured" if minutes == 60 else ""}"><p class="price-row__name">{minutes} min</p><span class="price-row__time">{minutes} minutes</span><span class="price-row__amount">{price}</span></div>'
        for minutes, price in prices
    )


def render_related(related_slugs, services_by_slug):
    return "\n".join(
        f'          <a class="service-card" href="/{slug}"><h3 class="service-card__title">{services_by_slug[slug]}</h3><p class="service-card__desc">View details and pricing →</p></a>'
        for slug in related_slugs
    )


def render_extra(s):
    """Optional long-form content sections. s['extra'] is a list of (heading, [paragraphs])."""
    blocks = s.get("extra")
    if not blocks:
        return ""
    body = ""
    for heading, paras in blocks:
        body += f'      <h2 data-reveal>{heading}</h2>\n'
        for p in paras:
            body += f'      <p data-reveal>{p}</p>\n'
    return (
        '\n    <section class="container container--content section">\n'
        + body
        + '    </section>\n'
    )


def render_faq_section(s):
    """Optional visible FAQ accordion. s['faqs'] is a list of (question, answer)."""
    faqs = s.get("faqs")
    if not faqs:
        return ""
    items = "\n".join(
        f'        <details class="faq__item"><summary>{q}</summary><p class="faq__answer">{a}</p></details>'
        for q, a in faqs
    )
    return (
        '\n    <section class="container container--narrow section">\n'
        '      <p class="eyebrow" data-reveal>Questions</p>\n'
        '      <h2 data-reveal>Good to know</h2>\n'
        f'      <div class="faq" data-reveal>\n{items}\n      </div>\n'
        '    </section>\n'
    )


def render_faq_schema(s):
    """FAQPage JSON-LD matching the visible FAQ. Empty when no faqs."""
    import json as _json
    faqs = s.get("faqs")
    if not faqs:
        return ""
    entities = ", ".join(
        '{"@type": "Question", "name": %s, "acceptedAnswer": {"@type": "Answer", "text": %s}}'
        % (_json.dumps(q), _json.dumps(a))
        for q, a in faqs
    )
    return (
        '  <script type="application/ld+json">\n'
        '  {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [' + entities + ']}\n'
        '  </script>\n'
    )


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    for s in SERVICES:
        price_from = s["prices"][0][1]
        price_from_num = price_from.replace("$", "").replace(",", "")
        kws = KEYWORDS.get(s["slug"], [f'{s["name"]} in Salt Lake City'])
        kw_primary = kws[0]
        kw_csv = ", ".join(kws)
        hero = HERO_IMAGES.get(s["slug"], DEFAULT_HERO)
        video_src = HERO_VIDEOS.get(s["slug"])
        hero_video_tag = (
            f'\n      <video class="ambient-video" muted loop playsinline preload="none" aria-hidden="true" tabindex="-1" data-src="{video_src}"></video>'
            if video_src else ""
        )
        html = PAGE_TEMPLATE.format(
            slug=s["slug"],
            name=s["name"],
            kw_primary=kw_primary,
            kw_csv=kw_csv,
            category=s["category"],
            tagline=s["tagline"],
            description=s["description"],
            best_for_html=render_best_for(s["best_for"]),
            prices_html=render_prices(s["prices"]),
            related_html=render_related(s["related"], SLUG_TO_NAME),
            extra_section=render_extra(s),
            faq_section=render_faq_section(s),
            faq_schema=render_faq_schema(s),
            price_from=price_from,
            price_from_num=price_from_num,
            hero_img=hero["img"],
            hero_alt=hero["alt"],
            hero_w=hero["w"],
            hero_h=hero["h"],
            hero_media_class=" has-ambient" if video_src else "",
            hero_video_tag=hero_video_tag,
            ambient_script=(
                '\n  <script src="/assets/ambient-video.js?v=1" defer></script>'
                if video_src else ""
            ),
        )
        path = os.path.join(out_dir, f"{s['slug']}.html")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print(f"  wrote {s['slug']}.html ({len(html)} bytes)")


if __name__ == "__main__":
    main()
