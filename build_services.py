"""Generate service detail pages and neighborhood hub pages from templates + data.
Run from the project root: `python build_services.py`
Each service gets a clean ~5KB HTML file matching the homepage's design system.
Each neighborhood hub page captures '{service} in {area}' local search intent."""

import os

# Tiered pricing (2026-06-13 restructure). No 30-minute sessions.
STANDARD_PRICES = [(60, "$85"), (90, "$125"), (120, "$165")]
PREMIUM_PRICES  = [(60, "$165"), (90, "$245"), (120, "$325")]   # couples, 4-hand
SPA_TREATMENT_PRICES = [(60, "$85"), (90, "$125")]             # foot reflexology, head spa (90-min added 2026-09-04)
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
        "prices": SPA_TREATMENT_PRICES,
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
                'Wondering about price before you book? Read our guide to <a href="/blog/head-spa-cost-worth-it-salt-lake-city">what a head spa costs in Salt Lake City and whether it is worth it</a>.',
            ]),
            ("Who it is for", [
                "Anyone who lives on a screen, sleeps poorly, carries stress in the neck and shoulders, or simply wants an hour of deep quiet. It is a favorite for a first spa visit because there is nothing to figure out, and a favorite gift because almost no one has had one and everyone remembers their first.",
            ]),
        ],
        "faqs": [
            ("How long is a Japanese head spa session?", "Our head spa comes in a 60-minute session for $85 or a 90-minute session for $125. Either way, your therapist has time to cover the scalp, neck, and shoulders without rushing."),
            ("Will my hair be wet or styled afterward?", "This is a dry, oil-optional treatment focused on the scalp and muscles, not a wash-and-blowout. If we use a little oil at your request, your hair may feel conditioned afterward. Bring a hair tie if you like."),
            ("Is a head spa good for tension headaches?", "Many clients come in specifically because they hold tension in the scalp, jaw, and neck, and they leave feeling lighter. We keep the work relaxing rather than clinical; if you have a medical concern, check with your doctor."),
            ("Can I add it to a massage?", "Yes. A head spa pairs beautifully with a full-body massage or foot reflexology. Book them back to back, or add a 30-minute infrared sauna at checkout."),
            ("Do you offer same-day appointments?", "Most days, yes. Call (801) 839-8880 or book online; same-day slots appear automatically when a therapist is open."),
        ],
        "related": ["spa-combo", "foot-reflexology-massage", "couples-massage"],
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
        "prices": SPA_TREATMENT_PRICES,
        "faqs": [
            ("Do I have to undress for reflexology?", "No. Reflexology is done fully clothed, with only your feet and lower legs bare. It is a great option if you want real bodywork without disrobing."),
            ("Does it only work on my feet, or the whole body?", "The hands-on work stays on your feet, but reflexology maps points there to the rest of the body, so many clients feel the effect well beyond their feet, often as a full-body calm."),
            ("Is reflexology safe during pregnancy?", "It is one of the gentler, pregnancy-friendly options because you stay comfortably seated or reclined and clothed. Let us know you are expecting when you book, and check with your doctor if you have any concerns."),
            ("Will it feel good or is it painful?", "Certain points can feel tender for a moment, but the work is meant to feel relieving, not painful. Your therapist keeps the pressure at a level you enjoy and eases off any sensitive spot."),
        ],
        "related": ["spa-combo", "head-spa-massage", "swedish-massage"],
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
    {
        "slug": "spa-combo",
        "name": "Two-Hour Spa Combo",
        "category": "Specialty & couples",
        "tagline": "Two services, two hours, one visit.",
        "description": "Pick any two of our signature hour-long treatments, Japanese head spa, foot reflexology, or a full-body massage, and take them back to back in one unhurried two-hour visit. One booking, one room, head to toe.",
        "best_for": ["A full head-to-toe reset", "Head spa and massage together", "A slower afternoon for yourself", "Gifting an experience"],
        "prices": [(120, "$165")],
        "extra": [
            ("How the combo works", [
                "Choose two of three hour-long services: a Japanese head spa, a foot reflexology session, or a full-body massage. We schedule them back to back, so you settle in once and stay put for the full two hours.",
                "A natural pairing is the head spa with foot reflexology, head to toe in one sitting. If you would rather trade the reflexology for a full-body massage, that works too. Tell us your two when you book.",
            ]),
            ("Why people book the combo", [
                "One hour is a treatment. Two hours is an afternoon. The combo gives your body time to settle, and it lets you try the head spa alongside a service you already like without making two trips.",
                "It also makes a thoughtful gift, since few people book themselves two full hours.",
            ]),
        ],
        "faqs": [
            ("Which two services can I combine?", "Any two of the three: Japanese head spa, foot reflexology, or a full-body massage. Head spa with reflexology is a natural pairing. Choose your two when you book, or call and we will help you decide."),
            ("Is the combo cheaper than booking two services?", "The two-hour combo is $165, priced as a full two hours of hands-on time, the same rate as any two-hour session with us. You are paying for the time rather than a discount. What you gain is one visit instead of two."),
            ("Can I add an infrared sauna or cupping?", "Yes. Add a 30-minute infrared sauna or CBD for $30, or hot stones or cupping for $20, at booking. They slot in around your two services."),
            ("Can we do the combo as a couple?", "We can. Two people, side by side, each with the full two-hour combo. Ask about it when you book, or reserve our couples spa combo directly."),
        ],
        "related": ["head-spa-massage", "foot-reflexology-massage", "couples-spa"],
    },
    {
        "slug": "couples-spa",
        "name": "Couples Spa Combo",
        "category": "Specialty & couples",
        "tagline": "Two people, two hours, side by side.",
        "description": "You and a guest, side by side in our private couples suite. Each of you takes the two-hour combo, a Japanese head spa paired with your choice of foot reflexology or a full-body massage. Two therapists, one quiet room.",
        "best_for": ["Date nights and anniversaries", "A shared afternoon off", "Gifting two", "Head to toe, together"],
        "prices": [(120, "$325")],
        "note_suffix": " The $325 is the total for both of you, not per person.",
        "extra": [
            ("What the couples spa combo includes", [
                "Both of you get the full two-hour combo: a Japanese head spa, then your choice of foot reflexology or a full-body massage. You are side by side on two tables in one private suite, each with your own therapist, for the whole two hours.",
                "You can pick different second services from each other. One of you can do head spa and reflexology while the other does head spa and a massage. Tell us your pairings when you book.",
            ]),
        ],
        "faqs": [
            ("Are we in the same room the whole time?", "Yes. You are side by side in one private couples suite, each with your own therapist, for the full two hours. You can talk quietly or simply rest; the room is yours."),
            ("Does it have to be a romantic couple?", "Not at all. The suite is just as welcoming for friends, a parent and adult child, or two people celebrating something. Anyone who wants the experience side by side is welcome."),
            ("How does draping work?", "Exactly as it does for a single session. Each of you undresses to your comfort level in private and stays fully draped the entire time, with only the area being worked on uncovered."),
            ("Should we book ahead?", "We recommend it. Two therapists and a private suite mean fewer slots, so a few days out gives you the best choice of times, especially on weekends and around holidays."),
        ],
        "related": ["couples-massage", "head-spa-massage", "4-hands-massage"],
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
    "couples-spa": {
        "img": "couples-suite.webp", "w": 1376, "h": 768,
        "alt": "Private couples suite with two side-by-side massage tables in a warm terracotta room at Elite Spa Utah",
    },
    "spa-combo": {
        "img": "head-spa.webp", "w": 1376, "h": 768,
        "alt": "Reclining head-spa lounger with a ceramic scalp-wash basin in a warm terracotta treatment room at Elite Spa Utah",
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
    "spa-combo": ["Two-hour spa combo in Salt Lake City", "head spa and massage package", "spa combo package", "head to toe spa"],
    "couples-spa": ["Couples spa in Salt Lake City", "couples head spa", "couples spa package", "couples spa combo"],
}

PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en-US">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=AW-17967111406"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'AW-17967111406');
    gtag('config', 'G-N0NTBPE7FC');
  </script>
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
  <link rel="stylesheet" href="/assets/styles.css?v=4">
  <link rel="preload" as="image" href="/assets/img/{hero_img}" imagesrcset="/assets/img/{hero_img_750} 750w, /assets/img/{hero_img} {hero_w}w" imagesizes="100vw" fetchpriority="high">

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
          <li><a class="site-nav__link" href="/blog">Blog</a></li>
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
      <img src="/assets/img/{hero_img}" srcset="/assets/img/{hero_img_750} 750w, /assets/img/{hero_img} {hero_w}w" sizes="100vw" alt="{hero_alt}" width="{hero_w}" height="{hero_h}" loading="eager" fetchpriority="high" decoding="async">{hero_video_tag}
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
        <div>
          <p class="site-footer__heading">Areas We Serve</p>
          <ul class="site-footer__list">
            <li><a href="/massage-in-sugar-house">Massage in Sugar House</a></li>
            <li><a href="/massage-in-downtown-salt-lake-city">Massage in Downtown SLC</a></li>
            <li><a href="/massage-in-millcreek">Massage near Millcreek</a></li>
            <li><a href="/massage-in-holladay">Massage near Holladay</a></li>
          </ul>
        </div>
      </div>
      <div class="site-footer__legal">
        <span>© 2026 Elite Spa Utah &middot; Operated by J Massage LLC</span>
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


# ---------------------------------------------------------------------------
# Neighborhood hub pages
# ---------------------------------------------------------------------------

AREAS = [
    {
        "slug": "sugar-house",
        "name": "Sugar House",
        "title_area": "Sugar House, Salt Lake City",
        "area_type": "Place",
        "meta_desc": "Massage in Sugar House at Elite Spa Utah. Licensed therapists, private rooms, same-day appointments. 10 minutes from 2100 South on State Street.",
        "body": """\
    <section class="page-header" data-hero>
      <div class="container container--narrow">
        <p class="eyebrow">Salt Lake City &rsaquo; Sugar House</p>
        <h1><span class="line"><span class="line-inner">Massage in Sugar House</span></span></h1>
        <p class="lead">Elite Spa Utah serves Sugar House residents from our studio at 1136 S State Street, about 10 minutes north on State Street.</p>
        <p style="margin-top: var(--space-3)" data-hero-cta>
          <a class="btn btn--primary" href="/book" data-magnetic>Book Now</a>
          <a class="btn btn--secondary" href="tel:+18018398880" style="margin-left: var(--space-1)">Call (801) 839-8880</a>
        </p>
      </div>
    </section>

    <figure class="svc-hero-media" data-reveal>
      <img src="/assets/img/treatment-room.webp" alt="Warm, dimly lit private massage room at Elite Spa Utah" width="1376" height="768" loading="eager" decoding="async">
    </figure>

    <section class="container container--content section">
      <h2 data-reveal>A short trip from the &ldquo;Second Downtown&rdquo;</h2>
      <p data-reveal>Sugar House sits at the center of Salt Lake City's social life. The neighborhood around 2100 South and Highland Drive runs dense with coffee shops, restaurants, and independent businesses. That energy is part of what makes Sugar House residents so worn out by Thursday. You move through the city, you stay active at Sugar House Park, and the tension builds up in your neck and lower back the way it always does.</p>
      <p data-reveal>Elite Spa Utah is a 10-minute drive north on State Street from the Sugar House commercial core. If you take the S Line streetcar to the 900 South TRAX station, the walk south to our studio is about eight minutes. No parking problems, no complicated detour. You finish work, you come in, you leave feeling like a different person.</p>

      <h2 data-reveal>Why Sugar House clients choose Elite</h2>
      <p data-reveal>Westminster University students, remote workers in the apartments along 1300 East, people who spend their weekends at Hidden Hollow or on the trails above the neighborhood: they all carry the same physical pattern. Shoulders loaded from screens, hips tight from sitting, and a baseline of stress that does not switch off when the laptop closes.</p>
      <p data-reveal>Our therapists work with that pattern every day. A deep tissue session targets the adhesions in the mid-back and shoulder girdle. Sports massage restores hip flexor length for runners who log miles on the Bonneville Shoreline Trail. Swedish massage works for the person who just needs to stop thinking for 60 minutes. We match the technique to what your body is actually carrying, not a default protocol.</p>
      <p data-reveal>Same-day appointments are available most days. Private rooms, licensed therapists, no shared waiting areas. The studio is quiet in a way that the Sugar House restaurant strip is not, and that difference is part of the service.</p>

      <h2 data-reveal>Services worth knowing about</h2>
      <p data-reveal>Sugar House clients tend to start with one service and build from there. Here is a practical starting point based on what works for this neighborhood's lifestyle:</p>
      <ul class="svc-best-for" data-reveal-stagger>
        <li><a href="/deep-tissue-massage">Deep Tissue Massage</a>: the go-to for chronic back, neck, and shoulder tension from desk work or heavy training. 60, 90, or 120 minutes.</li>
        <li><a href="/sports-massage">Sports Massage</a>: active-recovery work for runners, cyclists, and gym-goers who use the parks and trails in and around Sugar House.</li>
        <li><a href="/swedish-massage">Swedish Massage</a>: full-body relaxation for when tension is systemic and you need to reset the whole nervous system.</li>
        <li><a href="/couples-massage">Couples Massage</a>: private suite, two therapists, side-by-side. A reliable date-night upgrade for Sugar House's weekend crowd.</li>
        <li><a href="/head-spa-massage">Japanese Head Spa</a>: scalp, neck, and shoulder work for the screen-fatigued professional. One hour, fully clothed, and most clients fall asleep.</li>
        <li><a href="/individual-massage">Individual Massage</a>: tell the therapist what is bothering you. They build the session from there. The best option once you become a regular.</li>
      </ul>
      <p data-reveal>Add-ons are available at booking: hot stones ($20), cupping, infrared sauna, or CBD ($30 each).</p>

      <h2 data-reveal>Getting here from Sugar House</h2>
      <p data-reveal>The address is 1136 S State Street, Salt Lake City, UT 84111. From the Sugar House commercial core at 2100 South and Highland Drive, head west on 2100 South to State Street, then north on State Street. The drive is under 10 minutes with light traffic. Street parking is available on State Street and on adjacent side streets. If you take the S Line to the 900 South TRAX/streetcar station, we are a short walk south on State Street.</p>
      <p data-reveal>We are open daily from 10AM to 10PM. Same-day bookings are accepted online and by phone. Call (801) 839-8880 or book at the button below.</p>

      <h2 data-reveal>Questions from Sugar House clients</h2>

      <h3 class="svc-subhead" data-reveal>How long does it take to get to Elite Spa Utah from Sugar House?</h3>
      <p data-reveal>From 2100 South and Highland Drive, expect 8 to 12 minutes by car depending on traffic on State Street. The S Line streetcar to the downtown TRAX network puts you within walking distance of the studio without a car.</p>

      <h3 class="svc-subhead" data-reveal>Do you offer same-day massage appointments?</h3>
      <p data-reveal>Yes. Same-day appointments are available most days depending on therapist schedule. Book online at elitespautah.com/book or call (801) 839-8880 to check availability.</p>

      <h3 class="svc-subhead" data-reveal>What is the difference between deep tissue and sports massage?</h3>
      <p data-reveal>Deep tissue targets chronic adhesions and persistent tension through slow, firm pressure. Sports massage combines compression, stretching, and targeted pressure to aid active recovery and restore range of motion. If you train regularly, sports massage is the better fit. If your tension is from sitting and stress, deep tissue tends to address it more directly.</p>

      <h3 class="svc-subhead" data-reveal>Is parking available near the studio?</h3>
      <p data-reveal>Street parking on State Street and the surrounding blocks is generally available. The studio does not have a dedicated lot, but the neighborhood is navigable on foot from the 900 South TRAX station.</p>

      <h3 class="svc-subhead" data-reveal>How do I know which service to book for my first visit?</h3>
      <p data-reveal>If you carry tension in your upper back and neck, start with deep tissue. For full-body relaxation with no specific complaint, Swedish is the right choice. When you are unsure, call the studio at (801) 839-8880 and we will point you in the right direction based on what you describe.</p>

      <div class="nap-block" style="margin-top: var(--space-4); padding: var(--space-3); background: var(--color-cream, #f9f6f1); border-radius: 4px;">
        <p><strong>Elite Spa Utah</strong><br>
        1136 S State Street, Salt Lake City, UT 84111<br>
        <a href="tel:+18018398880">(801) 839-8880</a><br>
        Open daily 10AM&ndash;10PM</p>
      </div>
    </section>""",
    },
    {
        "slug": "downtown-salt-lake-city",
        "name": "Downtown Salt Lake City",
        "title_area": "Downtown Salt Lake City",
        "area_type": "Place",
        "meta_desc": "Massage in downtown Salt Lake City at Elite Spa Utah, 1136 S State Street. Same-day appointments, licensed therapists, private rooms. Walk from most downtown hotels.",
        "body": """\
    <section class="page-header" data-hero>
      <div class="container container--narrow">
        <p class="eyebrow">Salt Lake City &rsaquo; Downtown</p>
        <h1><span class="line"><span class="line-inner">Massage in Downtown Salt Lake City</span></span></h1>
        <p class="lead">Elite Spa Utah is on State Street in the downtown corridor. For anyone working, visiting, or staying in central SLC, this is not a destination spa requiring a drive.</p>
        <p style="margin-top: var(--space-3)" data-hero-cta>
          <a class="btn btn--primary" href="/book" data-magnetic>Book Now</a>
          <a class="btn btn--secondary" href="tel:+18018398880" style="margin-left: var(--space-1)">Call (801) 839-8880</a>
        </p>
      </div>
    </section>

    <figure class="svc-hero-media" data-reveal>
      <img src="/assets/img/treatment-room.webp" alt="Warm, dimly lit private massage room at Elite Spa Utah in Salt Lake City" width="1376" height="768" loading="eager" decoding="async">
    </figure>

    <section class="container container--content section">
      <h2 data-reveal>On State Street, in the thick of it</h2>
      <p data-reveal>State Street runs south from the steps of the Utah State Capitol. By the time it reaches 1136 South, it has passed through the heart of downtown: the financial district, the legal corridor, the hotel row, the dining cluster around 200 South. Our studio sits a few blocks past that concentration, which means it is quiet enough to unwind in but close enough to reach on foot from most downtown blocks.</p>
      <p data-reveal>Downtown Salt Lake City employs tens of thousands of people in offices within a five-block radius of State Street. The pattern in those buildings is familiar: long hours, stressful weeks, and a nagging tension in the neck and shoulders that accumulates from Monday to Friday. Elite Spa Utah exists to interrupt that pattern. We are open daily from 10AM to 10PM, same-day appointments accepted, and you do not need to leave the general downtown area to get here.</p>

      <h2 data-reveal>Who we serve in the downtown area</h2>
      <p data-reveal>Downtown SLC draws office workers, hotel guests, and convention visitors in roughly equal measure on any given day. Each group has a different reason to come in.</p>
      <p data-reveal>Office workers in the nearby buildings tend to book a 60-minute session after work or on a lunch hour when the schedule allows. The 60-minute deep tissue or Swedish massage fits the downtown workday cadence: in at 5:30, out by 7:00, dinner on the way home. For the person who sits at a desk for eight hours straight, that 60 minutes addresses more than the physical tension. It creates a clear boundary between the work day and the evening.</p>
      <p data-reveal>Hotel guests and convention visitors face a different problem: they are tired from travel, they are sleeping in a different bed, and they have no car to get to a wellness appointment across town. Our location on State Street is a short taxi or rideshare from every major downtown hotel. Several guests walk from the Marriott and Hilton properties on West Temple. The same-day booking model works well for this group because conference schedules change and you need flexibility.</p>

      <h2 data-reveal>Services for the downtown visitor and worker</h2>
      <p data-reveal>The full service menu is available to downtown clients. These options align most closely with what downtown clients typically need:</p>
      <ul class="svc-best-for" data-reveal-stagger>
        <li><a href="/swedish-massage">Swedish Massage</a>: full-body relaxation, ideal for travel fatigue or a mid-week stress reset. 60, 90, or 120 minutes from $85.</li>
        <li><a href="/deep-tissue-massage">Deep Tissue Massage</a>: targeted pressure for the chronic shoulder and neck tension that desk work produces. The most-requested service among our downtown regulars.</li>
        <li><a href="/chair-massage">Chair Massage</a>: focused work on the neck, upper back, and shoulders. Fully clothed. A strong option for a lunch-break reset without the full session commitment.</li>
        <li><a href="/couples-massage">Couples Massage</a>: private suite, two therapists working in tandem. A well-used option for hotel guests on a special occasion visit to the city.</li>
        <li><a href="/4-hands-massage">4-Hands Massage</a>: two therapists, one client. Covers the full body with coordinated pressure and is the most efficient session for someone who has limited time and significant full-body tension.</li>
        <li><a href="/individual-massage">Individual Massage</a>: a customized blend of techniques built around what you describe to the therapist. Preferred by returning clients who trust the therapist to read the room.</li>
      </ul>
      <p data-reveal>Add-ons available at booking: hot stones ($20), cupping, infrared sauna, or CBD ($30 each). Add-ons work well when you have the time to let the session run long and want more out of the hour.</p>

      <h2 data-reveal>Getting here from downtown</h2>
      <p data-reveal>The studio is at 1136 S State Street, Salt Lake City, UT 84111. From Temple Square and the City Creek area, drive or walk south on State Street for about 1.2 miles. From the TRAX stations at 400 South and 600 South, UTA Route 200 (State Street bus) runs directly along State Street to our stop. Street parking is available on State Street and on the side streets east of the studio.</p>
      <p data-reveal>We are open every day of the week from 10AM to 10PM. If you are booking same-day, call (801) 839-8880 to confirm availability before coming in. Online booking is at elitespautah.com/book and updates in real time.</p>

      <h2 data-reveal>Questions from downtown clients</h2>

      <h3 class="svc-subhead" data-reveal>Can I book a massage on the same day I arrive in Salt Lake City?</h3>
      <p data-reveal>Yes. Same-day appointments are our most common booking type. Check availability at elitespautah.com/book or call (801) 839-8880. We recommend calling if you need a specific time window within a few hours, since the online system updates but may not reflect the most recent opening.</p>

      <h3 class="svc-subhead" data-reveal>How far is Elite Spa Utah from the downtown hotels?</h3>
      <p data-reveal>From the hotel cluster along 100 South to 300 South, the studio is about 1 to 1.5 miles south on State Street. A rideshare takes 5 minutes. The walk is manageable in good weather and under 25 minutes.</p>

      <h3 class="svc-subhead" data-reveal>Do you take walk-in appointments?</h3>
      <p data-reveal>Walk-ins are welcome when there is availability. To avoid waiting, book ahead online or by phone. Same-day slots often fill by early afternoon, so morning booking gives you the best selection of times.</p>

      <h3 class="svc-subhead" data-reveal>What should I do about parking on State Street?</h3>
      <p data-reveal>Street parking is available on State Street and on the cross streets near the studio. Metered parking is common in this part of downtown. TRAX and buses run on State Street if you prefer to arrive without a car.</p>

      <h3 class="svc-subhead" data-reveal>Is a couples massage available without booking far in advance?</h3>
      <p data-reveal>The couples suite requires two therapists to be available at the same time. For weekend evenings and Friday nights, a day or two of advance booking is practical. For weekday sessions or off-peak hours, same-day or next-day availability is common. Call us to check.</p>

      <div class="nap-block" style="margin-top: var(--space-4); padding: var(--space-3); background: var(--color-cream, #f9f6f1); border-radius: 4px;">
        <p><strong>Elite Spa Utah</strong><br>
        1136 S State Street, Salt Lake City, UT 84111<br>
        <a href="tel:+18018398880">(801) 839-8880</a><br>
        Open daily 10AM&ndash;10PM</p>
      </div>
    </section>""",
    },
    {
        "slug": "millcreek",
        "name": "Millcreek",
        "title_area": "Millcreek, Utah",
        "area_type": "City",
        "meta_desc": "Massage near Millcreek, Utah at Elite Spa Utah. 15 to 20 minutes north on State Street. Deep tissue, sports massage, Swedish, and more. Same-day appointments available.",
        "body": """\
    <section class="page-header" data-hero>
      <div class="container container--narrow">
        <p class="eyebrow">Salt Lake County &rsaquo; Millcreek</p>
        <h1><span class="line"><span class="line-inner">Massage near Millcreek</span></span></h1>
        <p class="lead">Elite Spa Utah is 15 minutes north of Millcreek on State Street. Same-day appointments, licensed therapists, and private rooms on the Salt Lake City side of the county line.</p>
        <p style="margin-top: var(--space-3)" data-hero-cta>
          <a class="btn btn--primary" href="/book" data-magnetic>Book Now</a>
          <a class="btn btn--secondary" href="tel:+18018398880" style="margin-left: var(--space-1)">Call (801) 839-8880</a>
        </p>
      </div>
    </section>

    <figure class="svc-hero-media" data-reveal>
      <img src="/assets/img/treatment-room.webp" alt="Private massage room at Elite Spa Utah, serving Millcreek residents" width="1376" height="768" loading="eager" decoding="async">
    </figure>

    <section class="container container--content section">
      <h2 data-reveal>Millcreek: Utah&rsquo;s newest city, with familiar tension</h2>
      <p data-reveal>Millcreek incorporated in December 2016, making it the newest city in Utah. The people who live here have been here for generations, and the tension they carry is not new. The median age is 35, the household rate for children under 18 is 28%, and the recreational culture runs deep. Mill Creek Canyon is out the back door. The Wasatch is 15 minutes east. Families here are active, and active bodies accumulate wear in specific places.</p>
      <p data-reveal>Millcreek also sends a large number of commuters north into Salt Lake City every workday. If you are already making that drive, the turn onto State Street toward Elite Spa Utah adds almost no time to your trip. The studio is at 1136 S State Street, which sits between Millcreek and the core of downtown SLC. You pass through our neighborhood on the way in or on the way back.</p>

      <h2 data-reveal>What brings Millcreek clients in</h2>
      <p data-reveal>The Canyon Rim, East Mill Creek, and Mount Olympus neighborhoods in particular send us clients with a consistent physical pattern: hip flexor and IT band tightness from trail running and canyon hiking, lower-back tension from desk work layered on top of weekend exertion, and the general full-body fatigue that comes from being a working parent in a place where the mountains are always visible and always calling.</p>
      <p data-reveal>Our therapists know that pattern. Sports massage is the most effective tool for the Millcreek hiker who pushed too hard on a Saturday in Big Cottonwood Canyon and is paying for it by Monday. Deep tissue addresses the chronic adhesions that build up when high-activity weekends and high-stress workweeks alternate without a recovery protocol. Swedish massage serves the person who simply needs to stop moving for an hour and let the nervous system recalibrate.</p>
      <p data-reveal>We do not rush sessions. A 90-minute deep tissue appointment runs a full 90 minutes of hands-on work. Private rooms, licensed therapists, no shared spaces. The studio stays quiet in a way that makes the hour feel longer than it is, which is the point.</p>

      <h2 data-reveal>Services for the Millcreek lifestyle</h2>
      <p data-reveal>These services address what Millcreek clients most frequently bring in:</p>
      <ul class="svc-best-for" data-reveal-stagger>
        <li><a href="/sports-massage">Sports Massage</a>: active-recovery work combining stretching, compression, and targeted pressure. The best fit for canyon hikers, trail runners, and weekend cyclists. 60, 90, or 120 minutes from $85.</li>
        <li><a href="/deep-tissue-massage">Deep Tissue Massage</a>: slow, firm pressure targeting chronic adhesions in the back, hips, and shoulders. The layered tension of an active outdoor life over a desk-work week responds well to this approach.</li>
        <li><a href="/prenatal-massage">Prenatal Massage</a>: gentle, side-lying work for second and third trimester. Addresses lower back, hip, and leg tension. Millcreek&rsquo;s high proportion of households with children under 18 makes this a frequently requested service in the area.</li>
        <li><a href="/swedish-massage">Swedish Massage</a>: full-body relaxation. Long, flowing strokes to reset the entire nervous system after a week that moved too fast.</li>
        <li><a href="/shiatsu-massage">Shiatsu</a>: pressure-point work along energy meridians, performed clothed. A good option when you want effective bodywork without oil or draping.</li>
        <li><a href="/individual-massage">Individual Massage</a>: customized blend based on what you tell the therapist. The best return-visit option once you know what your body needs.</li>
      </ul>
      <p data-reveal>Add-ons at booking: hot stones ($20), cupping, infrared sauna, or CBD ($30 each).</p>

      <h2 data-reveal>Getting here from Millcreek</h2>
      <p data-reveal>The studio is at 1136 S State Street, Salt Lake City, UT 84111. From the Millcreek area, take 1300 East or 900 East north toward Salt Lake City, then connect to State Street and head north. From Millcreek Common near 3900 South and 1300 East, the drive is approximately 15 to 20 minutes depending on traffic. Parking is on-street along State Street and the side streets east of the studio.</p>
      <p data-reveal>We are open daily 10AM to 10PM. Same-day appointments are available most days. Book online or call (801) 839-8880 to check the current schedule.</p>

      <h2 data-reveal>Questions from Millcreek clients</h2>

      <h3 class="svc-subhead" data-reveal>How far is Elite Spa Utah from the Millcreek area?</h3>
      <p data-reveal>From central Millcreek near 3900 South and 1300 East, the studio is about 7 to 8 miles north. The drive takes 15 to 20 minutes on a typical weekday, depending on traffic on 1300 East or State Street.</p>

      <h3 class="svc-subhead" data-reveal>Is sports massage good for hiking recovery?</h3>
      <p data-reveal>Yes. Sports massage combines compression, assisted stretching, and targeted pressure on overworked muscle groups. After a long day in Mill Creek Canyon, the glutes, hip flexors, calves, and lower back take the most load. A 90-minute sports massage addresses all of those areas with enough time to work each zone properly.</p>

      <h3 class="svc-subhead" data-reveal>Do you offer prenatal massage for Millcreek clients?</h3>
      <p data-reveal>Yes. Prenatal massage is available for clients in their second and third trimester. Our therapists are trained in prenatal positioning and pressure and work with each trimester's specific needs. It is a good option for lower-back, hip, and leg tension that increases as pregnancy progresses.</p>

      <h3 class="svc-subhead" data-reveal>Can I book a same-day appointment from Millcreek?</h3>
      <p data-reveal>Same-day appointments are available most days. The easiest path is to check elitespautah.com/book, which shows real-time availability. If you need a specific window within the same afternoon, calling (801) 839-8880 directly is faster than waiting for the online system to update.</p>

      <h3 class="svc-subhead" data-reveal>What is the difference between Millcreek and Millcreek Canyon for your clients?</h3>
      <p data-reveal>Millcreek the city is the incorporated community in central Salt Lake County where many of our clients live and work. Mill Creek Canyon is the national forest canyon east of the city that many of them hike and trail-run in. Both are common reference points when clients describe where they are coming from or what brought on their tension.</p>

      <div class="nap-block" style="margin-top: var(--space-4); padding: var(--space-3); background: var(--color-cream, #f9f6f1); border-radius: 4px;">
        <p><strong>Elite Spa Utah</strong><br>
        1136 S State Street, Salt Lake City, UT 84111<br>
        <a href="tel:+18018398880">(801) 839-8880</a><br>
        Open daily 10AM&ndash;10PM</p>
      </div>
    </section>""",
    },
    {
        "slug": "holladay",
        "name": "Holladay",
        "title_area": "Holladay, Utah",
        "area_type": "City",
        "meta_desc": "Massage near Holladay, Utah at Elite Spa Utah. 20 minutes on I-215 and State Street. Licensed therapists, private rooms, same-day appointments for Holladay residents.",
        "body": """\
    <section class="page-header" data-hero>
      <div class="container container--narrow">
        <p class="eyebrow">Salt Lake County &rsaquo; Holladay</p>
        <h1><span class="line"><span class="line-inner">Massage near Holladay</span></span></h1>
        <p class="lead">Elite Spa Utah serves Holladay residents from our studio at 1136 S State Street. The drive is about 20 minutes, and the gap in local spa options makes it worth it.</p>
        <p style="margin-top: var(--space-3)" data-hero-cta>
          <a class="btn btn--primary" href="/book" data-magnetic>Book Now</a>
          <a class="btn btn--secondary" href="tel:+18018398880" style="margin-left: var(--space-1)">Call (801) 839-8880</a>
        </p>
      </div>
    </section>

    <figure class="svc-hero-media" data-reveal>
      <img src="/assets/img/treatment-room.webp" alt="Private massage room at Elite Spa Utah, accessible from Holladay Utah" width="1376" height="768" loading="eager" decoding="async">
    </figure>

    <section class="container container--content section">
      <h2 data-reveal>Holladay: fine homes, few spas</h2>
      <p data-reveal>Holladay is one of the most established residential communities in Salt Lake County. The city has been continuously inhabited since 1847, and the character reflects that history: wooded lots, well-kept homes, quiet streets near the base of Mount Olympus, and a community that has deliberately kept commercial development limited. That restraint produces a pleasant place to live and a limited selection of personal-care services within city limits.</p>
      <p data-reveal>Holladay has no day spa operating at the level most residents are accustomed to when they travel. The Olympus Hills Shopping Center covers basic retail. For massage, most Holladay residents have historically driven to a hotel spa in SLC or booked wherever a deal appeared. Those options are inconvenient or expensive. Elite Spa Utah at 1136 S State Street is a focused alternative: private rooms, licensed therapists, consistent pricing, no resort fee attached.</p>

      <h2 data-reveal>The 20-minute drive is the whole obstacle</h2>
      <p data-reveal>From central Holladay, the trip to our studio is approximately 20 minutes. Take I-215 west from the Holladay exit and connect to State Street north. Or take 1300 East north through Millcreek and into SLC. Both routes are straightforward and familiar to most Holladay residents who already commute to work in the city.</p>
      <p data-reveal>The demographic here tends toward established families and long-term residents. Median age in Holladay is just over 39. More than half of households are married couples. The lifestyle runs toward Mount Olympus hikes, Cottonwood Country Club, and the kind of weekend that leaves the body tired in a specific way. Holladay residents understand the value of a proper recovery session. They also understand that a 20-minute drive for a 90-minute deep tissue massage is a reasonable trade.</p>

      <h2 data-reveal>What works for Holladay clients</h2>
      <p data-reveal>Holladay's physical culture is less urban grind and more sustained outdoor activity. The clients who come from this area tend to carry tension from hiking the Grandeur Peak trail, from long days at the club, from the cumulative fatigue of a household that stays active. The upper back and hips take the load. Our therapists work with that pattern efficiently.</p>
      <p data-reveal>The couples dynamic also shapes what Holladay clients book. More than half of households are married-couple families, and a couples massage session in our private suite is the kind of evening that works better than most other options for a date night in the city. Two therapists, two tables, a quiet private room. We do not offer a shared lounging area or a resort experience. We offer a focused, professional massage session without the overhead that hotel spas charge.</p>

      <h2 data-reveal>Services for Holladay residents</h2>
      <p data-reveal>These are the services that align most closely with what Holladay clients bring in:</p>
      <ul class="svc-best-for" data-reveal-stagger>
        <li><a href="/couples-massage">Couples Massage</a>: private suite, two therapists, side-by-side. A natural fit for Holladay&rsquo;s married-couple majority. 60, 90, or 120 minutes from $165.</li>
        <li><a href="/deep-tissue-massage">Deep Tissue Massage</a>: firm, deliberate pressure for the chronic back and shoulder tension that accumulates through an active and working life. From $85.</li>
        <li><a href="/swedish-massage">Swedish Massage</a>: full-body restoration for the client who needs to stop moving and let the body recover from the week. A reliable reset regardless of fitness level.</li>
        <li><a href="/sports-massage">Sports Massage</a>: active-recovery work for the Mount Olympus hiker or outdoor athlete who carries specific muscle tightness after weekend exertion.</li>
        <li><a href="/prenatal-massage">Prenatal Massage</a>: side-lying, trimester-appropriate work for lower-back and hip tension during pregnancy. Available for clients in the second and third trimester.</li>
        <li><a href="/foot-reflexology-massage">Foot Reflexology</a>: pressure-point work on the feet, no disrobing required. A straightforward option when you want a focused 60-minute session without committing to a full table massage.</li>
      </ul>
      <p data-reveal>Add-ons at booking: hot stones ($20), cupping, infrared sauna, or CBD ($30 each). The infrared sauna add-on is a popular combination with deep tissue for clients driving in from the Holladay area.</p>

      <h2 data-reveal>Getting here from Holladay</h2>
      <p data-reveal>The studio address is 1136 S State Street, Salt Lake City, UT 84111. The most direct route from Holladay is I-215 west to the State Street exit, then north on State Street to 1136 South. From the Holladay area near 4800 South, that drive is typically 18 to 22 minutes depending on traffic. Street parking is available on State Street and on the side streets near the studio. No lot is required.</p>
      <p data-reveal>We are open every day from 10AM to 10PM. Call (801) 839-8880 or book online at elitespautah.com/book. Same-day appointments are available most days, though the couples suite benefits from a day or two of advance booking on weekends.</p>

      <h2 data-reveal>Questions from Holladay clients</h2>

      <h3 class="svc-subhead" data-reveal>Is there a spa or massage studio in Holladay itself?</h3>
      <p data-reveal>Holladay has limited commercial development by design. There are few dedicated massage studios within city limits. Most residents with a regular massage practice drive to Salt Lake City, Murray, or Cottonwood Heights for appointments. Elite Spa Utah on State Street is the closest licensed spa at this service level in the direction of downtown SLC.</p>

      <h3 class="svc-subhead" data-reveal>How long is the drive from Holladay to your studio?</h3>
      <p data-reveal>From central Holladay near 4800 South, expect 18 to 22 minutes via I-215 west to State Street north. Weekday afternoon traffic can push that toward 25 minutes. The drive is direct and on familiar roads for anyone who commutes north into the city.</p>

      <h3 class="svc-subhead" data-reveal>What is included in the couples massage suite?</h3>
      <p data-reveal>The couples suite has two side-by-side tables and two therapists working simultaneously, one per client. The room is private for the duration of your session. You choose your massage type and duration independently; they do not have to match. Both clients are worked at the same time, which is the point of a couples session. Pricing starts at $165 per person for 60 minutes.</p>

      <h3 class="svc-subhead" data-reveal>Do you offer gift cards for Holladay residents?</h3>
      <p data-reveal>Yes. Gift cards are available at elitespautah.com/gift-cards. They cover any service amount and do not expire. A popular option for Holladay households looking for a considered gift that is not another object.</p>

      <h3 class="svc-subhead" data-reveal>Is deep tissue massage appropriate for hikers and outdoor athletes?</h3>
      <p data-reveal>Deep tissue works well for the specific tension patterns that hiking and outdoor activity produce: IT band tightness, hip flexor shortening, lower back adhesions from carrying a pack or absorbing trail impact. For acute post-activity soreness within 48 hours, Swedish is gentler and equally effective. For chronic tension that has built up over multiple weeks of activity, deep tissue addresses the underlying tissue layers more directly.</p>

      <div class="nap-block" style="margin-top: var(--space-4); padding: var(--space-3); background: var(--color-cream, #f9f6f1); border-radius: 4px;">
        <p><strong>Elite Spa Utah</strong><br>
        1136 S State Street, Salt Lake City, UT 84111<br>
        <a href="tel:+18018398880">(801) 839-8880</a><br>
        Open daily 10AM&ndash;10PM</p>
      </div>
    </section>""",
    },
]

HUB_TEMPLATE = '''<!DOCTYPE html>
<html lang="en-US">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=AW-17967111406"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'AW-17967111406');
    gtag('config', 'G-N0NTBPE7FC');
  </script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Massage in {title_area} · Elite Spa Utah</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="massage in {name}, {name} massage, massage near {name}, Elite Spa Utah {name}">
  <link rel="canonical" href="https://elitespautah.com/massage-in-{slug}">
  <meta property="og:title" content="Massage in {title_area} · Elite Spa Utah">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="https://elitespautah.com/massage-in-{slug}">
  <meta property="og:image" content="https://elitespautah.com/assets/img/hero-1500.webp">
  <link rel="icon" type="image/x-icon" href="/assets/img/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Marcellus&family=PT+Serif:wght@400;700&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Marcellus&family=PT+Serif:wght@400;700&display=swap"></noscript>
  <link rel="stylesheet" href="/assets/styles.css?v=4">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": ["LocalBusiness", "MassageTherapist"],
        "name": "Elite Spa Utah",
        "url": "https://elitespautah.com/",
        "telephone": "+18018398880",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "1136 S State Street",
          "addressLocality": "Salt Lake City",
          "addressRegion": "UT",
          "postalCode": "84111",
          "addressCountry": "US"
        }},
        "geo": {{
          "@type": "GeoCoordinates",
          "latitude": 40.7447,
          "longitude": -111.8909
        }},
        "openingHours": "Mo-Su 10:00-22:00",
        "priceRange": "$$",
        "areaServed": {{
          "@type": "{area_type}",
          "name": "{name}"
        }}
      }},
      {{
        "@type": "Service",
        "serviceType": "Massage Therapy",
        "provider": {{
          "@type": "MassageTherapist",
          "name": "Elite Spa Utah",
          "url": "https://elitespautah.com/"
        }},
        "areaServed": {{
          "@type": "{area_type}",
          "name": "{name}"
        }},
        "offers": {{
          "@type": "Offer",
          "price": "85",
          "priceCurrency": "USD",
          "url": "https://elitespautah.com/book"
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://elitespautah.com/" }},
          {{ "@type": "ListItem", "position": 2, "name": "Services", "item": "https://elitespautah.com/services" }},
          {{ "@type": "ListItem", "position": 3, "name": "Massage in {name}", "item": "https://elitespautah.com/massage-in-{slug}" }}
        ]
      }}
    ]
  }}
  </script>
  <script src="/assets/defer-load.js?v=1" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="site-header__brand" href="/">Elite Spa Utah</a>
      <nav class="site-nav" aria-label="Primary">
        <button class="site-nav__menu-toggle" type="button" aria-label="Toggle menu" aria-expanded="false" aria-controls="primary-nav">&#9776;</button>
        <ul class="site-nav__list" id="primary-nav">
          <li><a class="site-nav__link" href="/services">Services</a></li>
          <li><a class="site-nav__link" href="/pricing">Pricing</a></li>
          <li><a class="site-nav__link" href="/reviews">Reviews</a></li>
          <li><a class="site-nav__link" href="/about">About</a></li>
          <li><a class="site-nav__link" href="/gift-cards">Gift Cards</a></li>
          <li><a class="site-nav__link" href="/faq">FAQ</a></li>
          <li><a class="site-nav__link" href="/blog">Blog</a></li>
          <li><a class="site-nav__link" href="/contact">Contact</a></li>
          <li><a class="site-nav__link" href="tel:+18018398880">(801) 839-8880</a></li>
          <li><a class="btn btn--primary" href="/book" data-magnetic>Book Now</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
{body}

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
          <p style="max-width: 36ch;">Salt Lake City&rsquo;s elevated massage therapy and spa. Licensed therapists, private rooms, same-day appointments.</p>
        </div>
        <div>
          <p class="site-footer__heading">Hours</p>
          <p>Mon&ndash;Sun<br>10AM&ndash;10PM</p>
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
        <div>
          <p class="site-footer__heading">Areas We Serve</p>
          <ul class="site-footer__list">
            <li><a href="/massage-in-sugar-house">Massage in Sugar House</a></li>
            <li><a href="/massage-in-downtown-salt-lake-city">Massage in Downtown SLC</a></li>
            <li><a href="/massage-in-millcreek">Massage near Millcreek</a></li>
            <li><a href="/massage-in-holladay">Massage near Holladay</a></li>
          </ul>
        </div>
      </div>
      <div class="site-footer__legal">
        <span>&copy; 2026 Elite Spa Utah &middot; Operated by J Massage LLC</span>
        <span>Licensed massage therapists, State of Utah</span>
      </div>
    </div>
  </footer>

  <script src="/assets/nav.js?v=2" defer></script>
</body>
</html>
'''


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
            hero_img_750=hero["img"].replace(".webp", "-750.webp"),
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

    # Generate neighborhood hub pages
    for area in AREAS:
        html = HUB_TEMPLATE.format(
            slug=area["slug"],
            name=area["name"],
            title_area=area["title_area"],
            meta_desc=area["meta_desc"],
            area_type=area["area_type"],
            body=area["body"],
        )
        path = os.path.join(out_dir, f"massage-in-{area['slug']}.html")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print(f"  wrote massage-in-{area['slug']}.html ({len(html)} bytes)")


if __name__ == "__main__":
    main()
