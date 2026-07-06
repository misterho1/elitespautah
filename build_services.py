"""Generate the 14 service detail pages from one template + service data.
Run from the project root: `python build_services.py`
Each service gets a clean ~5KB HTML file matching the homepage's design system."""

import os

# Tiered pricing (2026-06-13 restructure). No 30-minute sessions.
STANDARD_PRICES = [(60, "$85"), (90, "$125"), (120, "$165")]
PREMIUM_PRICES  = [(60, "$165"), (90, "$245"), (120, "$325")]   # couples, 4-hand
SINGLE_HOUR     = [(60, "$85")]                                 # foot reflexology, head spa
PRENATAL_PRICES = [(60, "$105"), (90, "$155"), (120, "$205")]   # prenatal (2026-07-05)

SERVICES = [
    {
        "slug": "deep-tissue-massage",
        "name": "Deep Tissue Massage",
        "category": "For pain & tension",
        "tagline": "Targeted pressure for chronic tension.",
        "description": "Slow, deliberate strokes and firm pressure that reach the deeper layers of muscle and connective tissue. Unlike a relaxation massage, deep tissue targets the source of tension, the chronic adhesions that cause persistent pain.",
        "best_for": ["Chronic back pain", "Neck and shoulder tension", "Sports injuries and recovery", "IT band, hamstring, hip tightness"],
        "prices": STANDARD_PRICES,
        "faqs": [
            ("Is deep tissue supposed to hurt?", "It should feel like a firm, productive pressure, not sharp pain. Good deep tissue works at the edge of what your body can release, and your therapist checks in throughout. Tell us to ease off any time; the work is more effective when you stay relaxed."),
            ("Will I be sore afterward?", "Some clients feel a mild next-day soreness, similar to after a workout, especially the first few sessions. Drink water, move gently, and it usually settles within a day. Let your therapist know your history so they can pace the pressure."),
            ("How often should I come in for chronic tension?", "For a specific issue, many clients start with every one to two weeks, then space out to monthly maintenance once the tension eases. We will suggest a rhythm based on what we find, never a hard sell."),
            ("Is a longer session worth it for deep tissue?", "Sixty minutes covers a focused area like back, neck, and shoulders. If you want full-body deep work or several problem spots addressed without rushing, the 90-minute session gives your therapist room to go deeper."),
        ],
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
        "faqs": [
            ("I have never had a massage. Is Swedish the right start?", "Yes. Swedish is the gentlest, most familiar style and the one we recommend for a first visit. There is nothing to prepare and nothing to know; your therapist walks you through it and adjusts to your comfort."),
            ("Do I have to undress fully?", "You undress to your comfort level in private, then lie under a sheet and blanket. You are kept draped the whole session; only the area being worked on is uncovered at a time. Many clients keep underwear on, and that is completely fine."),
            ("Is Swedish too light to help with tension?", "Swedish uses lighter, flowing pressure than deep tissue, but it still releases everyday tightness and calms the nervous system. If you want firmer work on a problem area, just ask; your therapist can add focused pressure without changing the relaxing feel."),
            ("How long should my first session be?", "Sixty minutes is a great full-body introduction. If you know you hold a lot of stress or simply want to sink in without watching the clock, ninety minutes is the easy upgrade."),
        ],
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
        "faqs": [
            ("Are we in the same room the whole time?", "Yes. You are side by side on two tables in one private suite, each with your own therapist. You can talk quietly or simply relax together; the room is yours for the session."),
            ("How does draping work for two people?", "Exactly as it does for a single massage. Each of you undresses to your comfort level in private and stays fully draped under a sheet the entire time, with only the area being worked on uncovered. Privacy and modesty are the standard, not the exception."),
            ("Does it have to be a romantic couple?", "Not at all. The couples suite is just as popular with friends, a parent and adult child, or coworkers celebrating a win. Anyone who wants to share the experience side by side is welcome."),
            ("Should we book ahead?", "We recommend it. Two therapists and a private suite means fewer slots than a single massage, so booking a few days out gives you the best choice of times, especially on weekends and around holidays."),
        ],
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
        "faqs": [
            ("What is a 4-hand massage like?", "Two therapists work on you at once, moving in coordinated, mirrored strokes. Because your mind cannot track four hands at a time, it tends to stop trying and let go completely. Most people describe it as deeply immersive."),
            ("Is it two massages at the same time?", "In effect, yes. You get double the hands for the same session length, so more of your body is covered and the whole thing feels twice as full. It is a treat rather than an everyday massage for most clients."),
            ("Can I choose the pressure?", "Absolutely. Both therapists match the pressure you ask for, from light and flowing to firm and deep, and check in as they go. You are always in control of how intense it feels."),
            ("Why does it cost more than a single massage?", "You are booking two licensed therapists for the full session instead of one. That is the reason for the premium price, and the reason it feels like a special occasion."),
        ],
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
        "faqs": [
            ("Do I have to undress for reflexology?", "No. Reflexology is done fully clothed, with only your feet and lower legs bare. It is a great option if you want real bodywork without disrobing."),
            ("Does it only work on my feet, or the whole body?", "The hands-on work stays on your feet, but reflexology maps points there to the rest of the body, so many clients feel the effect well beyond their feet, often as a full-body calm."),
            ("Is reflexology safe during pregnancy?", "It is one of the gentler, pregnancy-friendly options because you stay comfortably seated or reclined and clothed. Let us know you are expecting when you book, and check with your doctor if you have any concerns."),
            ("Will it feel good or is it painful?", "Certain points can feel tender for a moment, but the work is meant to feel relieving, not painful. Your therapist keeps the pressure at a level you enjoy and eases off any sensitive spot."),
        ],
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
        "faqs": [
            ("Should I book sports massage before or after an event?", "Both work. A session a few days before helps loosen and prime the muscles, while one after helps flush fatigue and speed recovery. Tell your therapist your event timing and we will tailor the work."),
            ("How is it different from deep tissue?", "Sports massage adds stretching, compression, and movement aimed at range of motion and recovery, not just deep pressure on knots. It is more dynamic and often targets the muscle groups your sport loads most."),
            ("Do I need to be a serious athlete?", "No. Anyone who trains, lifts, runs, skis, or is simply active gets value from it. We scale the work to your body and your activity level, not a competition schedule."),
            ("Will it help with an old nagging injury?", "It can ease the tension and compensation patterns around a recurring tight spot, and we work carefully around it. For a diagnosed injury, we stay in the relaxation-and-recovery lane and defer to your medical provider."),
        ],
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
        "faqs": [
            ("The therapist uses their feet? Is that safe?", "Yes. Your therapist holds overhead bars for full control and balance, applying smooth, broad pressure with the soles of the feet. It is a trained, precise technique, and the pressure is more even and less pointed than an elbow."),
            ("Does ashiatsu hurt?", "It should feel like deep, gliding compression rather than a sharp dig. Because the pressure spreads over a larger surface, many clients find it more comfortable than deep tissue at the same depth. You set the intensity."),
            ("Who is ashiatsu best for?", "People who love deep pressure and feel that hands and elbows never quite reach deep enough, including athletes and larger-bodied clients. If regular deep tissue leaves you wanting more, this is worth trying."),
            ("Do I stay draped?", "Yes. Ashiatsu is performed with oil on bare skin, and you stay fully draped with only the area being worked on uncovered, exactly as in any table massage."),
        ],
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
        "faqs": [
            ("Do I stay dressed for shiatsu?", "Yes. Shiatsu is done fully clothed, with no oil and no draping, so wear something comfortable you can move in. It is a good fit if you would rather not undress for bodywork."),
            ("What does shiatsu feel like?", "Your therapist applies steady thumb, palm, and finger pressure along the body's energy lines, sometimes with gentle stretches. It feels rhythmic and grounding rather than slippery or flowing, and many people leave feeling both calm and re-energized."),
            ("Is it better for relaxation or for tension?", "Both, in its own way. Shiatsu eases stiffness and tension while also aiming to rebalance energy and fatigue, so it suits clients who feel tight and drained rather than simply sore."),
            ("I have never tried pressure-point work. Is shiatsu a good start?", "It is a gentle, approachable introduction because it stays clothed and the pressure is easy to dial in. Tell your therapist it is your first time and they will guide you through it."),
        ],
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
        "faqs": [
            ("Do I need to undress for a chair massage?", "No. Chair massage is done fully clothed, seated in a supportive massage chair. It is the easiest, lowest-commitment way to try bodywork or fit relief into a busy day."),
            ("What areas does it cover?", "The focus is your neck, shoulders, upper back, and arms, the spots that carry desk and screen tension. It is targeted rather than full-body, which is what makes it quick and effective."),
            ("Is chair massage good for a first-timer?", "Very. There is nothing to figure out, no oil, and no table, so it is a comfortable first taste of massage. Many clients start here and later book a full table session."),
            ("How long does a chair session take?", "It is designed to be efficient, so you can fit it around a lunch break or errand. Let us know your time window when you book and we will suggest the right length."),
        ],
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
        "faqs": [
            ("What is an individual massage exactly?", "It is a fully customized session. Instead of picking a named style, you tell your therapist what you need that day and they blend techniques to match, from relaxing to focused, in one massage."),
            ("How do I know what to ask for?", "You do not have to know. Just describe how you feel and where you hold tension, and your therapist chooses the approach. This is the go-to for clients who would rather not decide between styles."),
            ("Can the therapist mix relaxation and deep work?", "Yes, that is the whole point. You might get gentle, flowing work over most of the body and firmer pressure on a stubborn area, all in the same session."),
            ("Is this good for regular clients?", "It is a favorite for returning clients who trust their therapist to read the day and adjust. Over time, many people default to this once they know how their body responds."),
        ],
        "related": ["swedish-massage", "deep-tissue-massage", "head-spa-massage"],
    },
    {
        "slug": "prenatal-massage",
        "name": "Prenatal Massage",
        "category": "For stress & restoration",
        "tagline": "Safe, supportive bodywork through pregnancy.",
        "description": "Gentle, side-lying massage tailored to each trimester. Relieves the lower-back, hip, and leg tension pregnancy brings, improves circulation, and gives you a calm hour to rest. Performed by therapists experienced in prenatal positioning and pressure.",
        "best_for": ["Second- and third-trimester aches", "Lower back and hip relief", "Swelling and circulation", "Stress and better sleep"],
        "prices": PRENATAL_PRICES,
        "note_suffix": " Add 30 minutes to any prenatal session for $50.",
        "faqs": [
            ("Is prenatal massage safe during pregnancy?", "For most healthy pregnancies, yes, and it is performed by therapists experienced in prenatal positioning and pressure. We keep the work gentle and supportive. If your pregnancy is high-risk or you have any concern, please check with your doctor first."),
            ("How am I positioned so it stays comfortable?", "You rest on your side, supported by bolster pillows, rather than lying face-down. This keeps pressure off your abdomen and lower back and is comfortable well into the third trimester."),
            ("When in my pregnancy can I come in?", "Many clients start in the second and third trimesters, when lower-back, hip, and leg aches tend to build. If you are in your first trimester or have questions about timing, talk with your provider and we will follow their guidance."),
            ("What if I need a little more time?", "You can add 30 minutes to any prenatal session for $50, which is a nice option if you want extra time on your back, hips, and legs at an unhurried pace."),
        ],
        "related": ["swedish-massage", "individual-massage", "foot-reflexology-massage"],
    },
]

# Build slug -> service lookup for related-services cross-sell (name, tagline, price)
SLUG_TO_SERVICE = {s["slug"]: s for s in SERVICES}

# Service-page hero photography. Per-service brand shots generated 2026-07-05
# (Higgsfield nano_banana_pro, seeded from the homepage hero for one exposure
# family: warm candlelit amber, terracotta + cream). Swap freely for real
# Elite Spa photography later — keep the alt text.
DEFAULT_HERO = {
    "img": "treatment-room.webp", "w": 1376, "h": 768,
    "alt": "Warm, sunlit private massage room with a draped table and terracotta plaster walls at Elite Spa Utah",
}
# Distinct room setups, all shot in the SAME real boutique room for continuity
# (seeded 2026-07-06). Single-massage services intentionally share the
# treatment-room default so the whole site reads as one consistent space.
HERO_IMAGES = {
    "head-spa-massage": {
        "img": "head-spa.webp", "w": 1376, "h": 768,
        "alt": "Reclining head-spa lounger with a ceramic scalp-wash basin in a warm terracotta treatment room at Elite Spa Utah",
    },
    "foot-reflexology-massage": {
        "img": "foot-reflexology.webp", "w": 1376, "h": 768,
        "alt": "Reclining reflexology chair with a folded throw and a copper foot basin in a warm terracotta treatment room at Elite Spa Utah",
    },
    "couples-massage": {
        "img": "couples-suite.webp", "w": 1376, "h": 768,
        "alt": "Private couples suite with two side-by-side massage tables in a warm terracotta room at Elite Spa Utah",
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
          <a class="btn btn--primary" href="/book?service={slug}" data-magnetic>Book Now</a>
          <a class="btn btn--secondary" href="tel:+18018398880" style="margin-left: var(--space-1)">Call (801) 839-8880</a>
        </p>
      </div>
    </section>

    <figure class="svc-hero-media{hero_media_class}" data-reveal>
      <img src="/assets/img/{hero_img}" alt="{hero_alt}" width="{hero_w}" height="{hero_h}" loading="lazy" decoding="async">{hero_video_tag}
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
          <p class="svc-note">Add-ons · hot stones or cupping $20 each; infrared sauna (30 min) or CBD $30 each, added at booking.{note_suffix}</p>
          <p style="margin-top: var(--space-3)">
            <a class="btn btn--primary" href="/book?service={slug}">Book {name}</a>
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
        <a class="btn btn--primary" href="/book?service={slug}" data-magnetic>Book Now</a>
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
    # Real cross-sell: each card shows the related service's own tagline + a
    # "From $X" price instead of identical boilerplate.
    cards = []
    for slug in related_slugs:
        svc = services_by_slug[slug]
        price_from = svc["prices"][0][1]
        cards.append(
            f'          <a class="service-card" href="/{slug}">'
            f'<h3 class="service-card__title">{svc["name"]}</h3>'
            f'<p class="service-card__desc">{svc["tagline"]}</p>'
            f'<p class="service-card__price">From {price_from}</p></a>'
        )
    return "\n".join(cards)


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
            related_html=render_related(s["related"], SLUG_TO_SERVICE),
            extra_section=render_extra(s),
            faq_section=render_faq_section(s),
            faq_schema=render_faq_schema(s),
            note_suffix=s.get("note_suffix", ""),
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
