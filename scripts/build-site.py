#!/usr/bin/env python3
"""Build the Springfield Junk Removal Service static site.

Writes the kept HTML pages, sitemap.xml, robots.txt, llms.txt, and _redirects.
Does not change Cloudflare project settings.
"""

import html
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://springfieldjunkremovalservice.com"
PHONE_DISPLAY = "(417) 242-5370"
PHONE_TEL = "4172425370"
FORM = "https://formspree.io/f/mojzdkvg"

CITIES = [
    ("Springfield", "Missouri"),
    ("Battlefield", "Missouri"),
    ("Nixa", "Missouri"),
    ("Ozark", "Missouri"),
    ("Republic", "Missouri"),
    ("Willard", "Missouri"),
]

NAV = [
    ("/", "Home", "index.html"),
    ("/residential-junk-removal-springfield-mo", "Residential", "residential-junk-removal-springfield-mo.html"),
    ("/cleanouts-springfield-mo", "Cleanouts", "cleanouts-springfield-mo.html"),
    ("/commercial-junk-removal-springfield-mo", "Commercial", "commercial-junk-removal-springfield-mo.html"),
    ("/yard-waste-removal-springfield-mo", "Yard & Outdoor", "yard-waste-removal-springfield-mo.html"),
    ("/junk-removal-service-areas-springfield-mo", "Service Area", "junk-removal-service-areas-springfield-mo.html"),
    ("/junk-removal-cost-springfield-mo", "Cost & FAQ", "junk-removal-cost-springfield-mo.html"),
    ("/springfield-junk-disposal-guide", "Disposal Guide", "springfield-junk-disposal-guide.html"),
    ("/contact", "Contact", "contact.html"),
]

REMOVED = {
    "junk-removal-services-springfield-mo": "/",
    "junk-removal-springfield-mo": "/",
    "same-day-junk-removal-springfield-mo": "/",
    "furniture-removal-springfield-mo": "/residential-junk-removal-springfield-mo",
    "appliance-removal-springfield-mo": "/residential-junk-removal-springfield-mo",
    "mattress-removal-springfield-mo": "/residential-junk-removal-springfield-mo",
    "couch-removal-springfield-mo": "/residential-junk-removal-springfield-mo",
    "trash-removal-springfield-mo": "/residential-junk-removal-springfield-mo",
    "what-items-can-be-removed-springfield-mo": "/residential-junk-removal-springfield-mo",
    "estate-cleanout-springfield-mo": "/cleanouts-springfield-mo",
    "eviction-cleanout-springfield-mo": "/cleanouts-springfield-mo",
    "apartment-cleanout-springfield-mo": "/cleanouts-springfield-mo",
    "garage-cleanout-springfield-mo": "/cleanouts-springfield-mo",
    "house-cleanout-springfield-mo": "/cleanouts-springfield-mo",
    "hoarder-cleanout-springfield-mo": "/cleanouts-springfield-mo",
    "rental-turnover-cleanout-checklist-springfield-mo": "/cleanouts-springfield-mo",
    "springfield-student-move-out-donation-disposal-checklist": "/cleanouts-springfield-mo",
    "construction-debris-removal-springfield-mo": "/commercial-junk-removal-springfield-mo",
    "hot-tub-removal-springfield-mo": "/yard-waste-removal-springfield-mo",
    "shed-removal-springfield-mo": "/yard-waste-removal-springfield-mo",
    "junk-removal-nixa-mo": "/junk-removal-service-areas-springfield-mo",
    "junk-removal-ozark-mo": "/junk-removal-service-areas-springfield-mo",
    "junk-removal-republic-mo": "/junk-removal-service-areas-springfield-mo",
    "junk-removal-battlefield-mo": "/junk-removal-service-areas-springfield-mo",
    "junk-removal-willard-mo": "/junk-removal-service-areas-springfield-mo",
    "how-junk-removal-works-springfield-mo": "/junk-removal-cost-springfield-mo",
    "junk-removal-guides-springfield-mo": "/springfield-junk-disposal-guide",
}

SERVICE_OPTIONS = [
    "Residential junk, furniture, or appliances",
    "Cleanout (estate, eviction, apartment, or garage)",
    "Commercial junk or construction debris",
    "Yard waste, shed, or hot tub",
    "Other",
]


def esc(text):
    return html.escape(text, quote=True)


def strip_tags(text):
    return re.sub(r"<[^>]+>", "", text)


def business_ld():
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": DOMAIN + "/#business",
        "name": "Springfield Junk Removal Service",
        "url": DOMAIN + "/",
        "telephone": "+1-417-242-5370",
        "image": DOMAIN + "/site-icon-512.png",
        "description": (
            "Junk removal in Springfield, Missouri. We haul household junk, "
            "cleanouts, commercial junk, construction debris, yard waste, sheds, and hot tubs."
        ),
        "areaServed": [
            {
                "@type": "City",
                "name": name,
                "containedInPlace": {"@type": "State", "name": state},
            }
            for name, state in CITIES
        ],
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+1-417-242-5370",
            "contactType": "customer service",
            "areaServed": "US",
            "availableLanguage": "English",
        },
    }


def faq_ld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)},
            }
            for q, a in faqs
        ],
    }


def json_ld(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False)


GTM = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-GDJF54DV');</script>
<!-- End Google Tag Manager -->"""

GTM_BODY = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-GDJF54DV"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

GA4_NOTE = """<!--
GA4 PLACEHOLDER for property 541475893.
The measurement ID (G-…) for this property was not found in the repository or git history.
Do not guess an ID. GTM-GDJF54DV stays installed.
Docs mention GTM destination G-GWT8GR7QJC; that ID is not recorded as property 541475893.
When the real measurement ID is known, set GA4_MEASUREMENT_ID_PROPERTY_541475893 in analytics-events.js.
-->"""


def nav_html(current):
    parts = []
    for href, label, _file in NAV:
        current_attr = ' aria-current="page"' if href == current else ""
        parts.append(f'<a href="{href}"{current_attr}>{esc(label)}</a>')
    return "\n".join(parts)


def footer_html():
    links = "\n".join(f'<a href="{href}">{esc(label)}</a>' for href, label, _file in NAV)
    return f"""<footer>
<div class="wrap">
<p><strong>Springfield Junk Removal Service</strong></p>
<p>Phone: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
<div class="foot-links">{links}</div>
<p>Junk removal in Springfield, MO and nearby towns. Call for a quote. No text line.</p>
</div>
</footer>"""


def form_html(selected):
    options = ['<option value="" disabled>What do you need hauled?</option>']
    for label in SERVICE_OPTIONS:
        sel = " selected" if label == selected else ""
        options.append(f"<option{sel}>{esc(label)}</option>")
    option_html = "\n".join(options)
    return f"""<form action="{FORM}" method="POST">
<input type="hidden" name="site" value="springfieldjunkremovalservice.com">
<input type="hidden" name="market" value="Springfield, MO">
<input type="hidden" name="niche" value="Junk Removal">
<label for="lead-name">Name</label>
<input id="lead-name" type="text" name="name" autocomplete="name" required>
<label for="lead-phone">Phone</label>
<input id="lead-phone" type="tel" name="phone" autocomplete="tel" required>
<label for="lead-email">Email</label>
<input id="lead-email" type="email" name="email" autocomplete="email">
<label for="lead-service">Job type</label>
<select id="lead-service" name="service" required>
{option_html}
</select>
<label for="lead-message">What should we haul?</label>
<textarea id="lead-message" name="message" rows="5" required placeholder="Items, about how much, stairs or gates, and the town"></textarea>
<button class="btn" type="submit">Request a Quote</button>
</form>"""


def quote_box(selected):
    return f"""<div class="quote-box" id="quote">
<h2>Request a Quote</h2>
<p>Tell us what you have. We will quote the job. Prefer to talk? Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
{form_html(selected)}
</div>"""


def faq_html(faqs):
    blocks = []
    for q, a in faqs:
        blocks.append(f'<div class="faq"><h3>{esc(q)}</h3><p>{a}</p></div>')
    return "\n".join(blocks)


def crumbs(current_label, current_href):
    if current_href == "/":
        return ""
    return f'<p class="crumbs"><a href="/">Home</a> / {esc(current_label)}</p>'


def render(page):
    href = page["href"]
    canonical = DOMAIN + "/" if href == "/" else DOMAIN + href
    faqs = page["faqs"]
    title = page["title"]
    description = page["description"]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{GTM}
{GA4_NOTE}
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Springfield Junk Removal Service">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_US">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#14221b">
<link rel="stylesheet" href="/site.css">
<script type="application/ld+json">
{json_ld(business_ld())}
</script>
<script type="application/ld+json">
{json_ld(faq_ld(faqs))}
</script>
</head>
<body>
{GTM_BODY}
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
<div class="wrap bar">
<a class="logo" href="/">Springfield Junk Removal Service<span>Springfield, MO</span></a>
<a class="call" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
<details class="menu">
<summary>Menu</summary>
<nav class="nav" aria-label="Primary">
{nav_html(href)}
</nav>
</details>
</div>
</header>
<main id="main">
<section class="hero">
<div class="wrap">
{crumbs(page["crumb"], href)}
<h1>{esc(page["h1"])}</h1>
<p class="lede">{page["lede"]}</p>
<div class="cta">
<a class="btn" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
<a class="btn dark" href="#quote">Get a Quote</a>
</div>
</div>
</section>
{page["body"]}
<section>
<div class="wrap split">
<div>
<h2>{esc(page["quote_heading"])}</h2>
{page["quote_copy"]}
</div>
{quote_box(page["service"])}
</div>
</section>
<section>
<div class="wrap">
<h2>Questions</h2>
{faq_html(faqs)}
</div>
</section>
</main>
{footer_html()}
<script src="/analytics-events.js"></script>
</body>
</html>
"""


def pages():
    phone = f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>'
    return [
        {
            "file": "index.html",
            "href": "/",
            "crumb": "Home",
            "title": "Junk Removal in Springfield, MO | Springfield Junk Removal Service",
            "description": "We haul junk in Springfield, MO. Homes, cleanouts, job sites, and yards. Call (417) 242-5370 for a quote.",
            "h1": "Junk Removal in Springfield, MO",
            "lede": f"We are Springfield Junk Removal Service. We pick up junk from homes and businesses in Springfield, Missouri. Call {phone} or send the form and we will quote the job.",
            "service": "Residential junk, furniture, or appliances",
            "quote_heading": "Tell us what needs to go",
            "quote_copy": "<p>List the items, about how much there is, and whether anything is upstairs or behind a gate. We quote from that.</p>",
            "faqs": [
                (
                    "How much does junk removal cost in Springfield, MO?",
                    "Call (417) 242-5370 for a quote. The price depends on how much there is, how heavy it is, what it is, and how hard it is to reach. We do not publish a flat rate.",
                ),
                (
                    "What junk do you take in Springfield?",
                    "We take household junk, furniture, mattresses, couches, appliances, garage and house cleanouts, estate and eviction cleanouts, commercial junk, non-hazardous construction debris, yard waste, sheds, and hot tubs. We do not take hazardous waste, asbestos, fuel, ammunition, or medical waste.",
                ),
                (
                    "Do I need to move the junk outside?",
                    "No. We carry it out from where it sits. Tell us about stairs, gates, and tight access when you call.",
                ),
                (
                    "Where do you work?",
                    "We work in Springfield, MO, and in Battlefield, Nixa, Ozark, Republic, and Willard.",
                ),
                (
                    "Can you come today?",
                    "Call with the day you need. We will tell you the first time we can be there. We do not promise same-day service.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Junk removal for Springfield homes and businesses</h2>
<dl class="facts">
<div><dt>Business</dt><dd>Springfield Junk Removal Service</dd></div>
<div><dt>Service</dt><dd>Junk removal and hauling</dd></div>
<div><dt>City</dt><dd>Springfield, MO</dd></div>
<div><dt>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></dd></div>
<div><dt>Price</dt><dd>Call for a quote</dd></div>
</dl>
</div>
</section>
<section>
<div class="wrap">
<h2>What we haul</h2>
<div class="grid">
<article class="card"><span class="kicker">Homes</span><h3><a href="/residential-junk-removal-springfield-mo">Residential junk</a></h3><p>Furniture, mattresses, couches, appliances, and household trash.</p></article>
<article class="card"><span class="kicker">Properties</span><h3><a href="/cleanouts-springfield-mo">Cleanouts</a></h3><p>Estate, eviction, apartment, garage, and whole-house cleanouts.</p></article>
<article class="card"><span class="kicker">Job sites</span><h3><a href="/commercial-junk-removal-springfield-mo">Commercial and debris</a></h3><p>Office and store junk, plus non-hazardous construction debris.</p></article>
<article class="card"><span class="kicker">Outdoors</span><h3><a href="/yard-waste-removal-springfield-mo">Yard, sheds, and hot tubs</a></h3><p>Brush, bagged yard waste, sheds, and hot tubs.</p></article>
</div>
</div>
</section>
<section>
<div class="wrap">
<h2>How a pickup works</h2>
<ol class="steps">
<li><strong>Call or send the form.</strong> Tell us the items, the amount, and the town.</li>
<li><strong>We quote the job.</strong> You decide whether to book it. <a href="/junk-removal-cost-springfield-mo">What changes the price</a>.</li>
<li><strong>We load it and haul it away.</strong> You do not need to drag it to the curb.</li>
</ol>
</div>
</section>
<section>
<div class="wrap split">
<div>
<h2>Service area</h2>
<p>We haul junk in Springfield and in Battlefield, Nixa, Ozark, Republic, and Willard. <a href="/junk-removal-service-areas-springfield-mo">See the service area</a>.</p>
</div>
<div class="panel">
<h2>What we do not take</h2>
<p>Hazardous waste, asbestos, fuel, ammunition, and medical waste are not junk we haul. Paint and chemicals belong at the city's household chemical drop-off. See the <a href="/springfield-junk-disposal-guide">Springfield disposal guide</a>.</p>
</div>
</div>
</section>
""",
        },
        {
            "file": "residential-junk-removal-springfield-mo.html",
            "href": "/residential-junk-removal-springfield-mo",
            "crumb": "Residential",
            "title": "Residential Junk Removal in Springfield, MO | Furniture & Appliances",
            "description": "We haul furniture, mattresses, couches, appliances, and household junk in Springfield, MO. Call (417) 242-5370 for a quote.",
            "h1": "Residential Junk Removal in Springfield, MO",
            "lede": f"We remove household junk from Springfield homes. That includes furniture, mattresses, couches, appliances, boxes, and piled-up trash. Call {phone} for a quote.",
            "service": "Residential junk, furniture, or appliances",
            "quote_heading": "Quote a household pickup",
            "quote_copy": "<p>Name the pieces and where they sit. A couch in a living room and a basement full of boxes are different jobs.</p>",
            "faqs": [
                (
                    "Do you take mattresses and couches in Springfield?",
                    "Yes. We haul mattresses, box springs, couches, sectionals, loveseats, and recliners. Tell us the size and the room it is in.",
                ),
                (
                    "Do you take appliances?",
                    "Yes. We haul refrigerators, washers, dryers, ovens, dishwashers, and freezers. Tell us if the unit is still connected to water, gas, or power. We do not advertise refrigerant recovery.",
                ),
                (
                    "Do you take household trash?",
                    "Yes. We haul bagged household trash and boxes that will not fit in the cart. We do not take hazardous waste, chemicals, fuel, or medical waste.",
                ),
            ],
            "body": """
<section>
<div class="wrap">
<h2>Furniture, mattress, and couch removal</h2>
<p>We pick up couches, sectionals, loveseats, recliners, tables, chairs, dressers, desks, mattresses, and box springs. One piece or a whole room is fine.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Appliances</h3><p>Refrigerators, freezers, washers, dryers, ovens, and dishwashers. If it is still hooked up, say so when you book. We haul the unit. We do not claim Freon recovery.</p></article>
<article class="card"><h3>Household junk and trash</h3><p>Boxes, bagged trash, small household goods, shelving, and clutter from closets, basements, and spare rooms.</p></article>
<article class="card"><h3>Electronics</h3><p>Televisions, monitors, and computers can go on the list. We do not wipe data and we do not promise a recycling certificate.</p></article>
</div>
</section>
<section>
<div class="wrap">
<div class="note"><strong>Not ordinary junk.</strong> Paint, chemicals, asbestos, fuel, ammunition, and medical waste stay off the truck. Use the <a href="/springfield-junk-disposal-guide">Springfield disposal guide</a> for city drop-off pages, or book a <a href="/cleanouts-springfield-mo">cleanout</a> if the job is a whole room or house.</div>
</div>
</section>
""",
        },
        {
            "file": "cleanouts-springfield-mo.html",
            "href": "/cleanouts-springfield-mo",
            "crumb": "Cleanouts",
            "title": "Estate, Eviction, Apartment & Garage Cleanouts in Springfield, MO",
            "description": "We clean out houses, garages, apartments, estates, and eviction units in Springfield, MO. Call (417) 242-5370 for a quote.",
            "h1": "Property Cleanouts in Springfield, MO",
            "lede": f"We clean out houses, garages, and rentals in Springfield, Missouri. Estate cleanouts, eviction cleanouts, apartment turnovers, and garage cleanouts are the same phone call. Call {phone} and describe the property.",
            "service": "Cleanout (estate, eviction, apartment, or garage)",
            "quote_heading": "Quote a cleanout",
            "quote_copy": "<p>Tell us the property type, about how full it is, and who will let us in. We quote the haul.</p>",
            "faqs": [
                (
                    "Do you do estate cleanouts in Springfield, MO?",
                    "Yes. We haul furniture, household junk, and leftover belongings from houses after a move, a downsizing, or an estate. You show us what goes.",
                ),
                (
                    "Can a landlord book an eviction or apartment cleanout?",
                    "Yes. Property managers call us to haul belongings and trash left in a unit. We need access and a clear list of what goes. We do not handle lockouts or legal notices.",
                ),
                (
                    "Do you clean out garages?",
                    "Yes. We empty garages of boxes, shelving, old tools, and broken equipment. Tell us if a vehicle is still parked inside.",
                ),
            ],
            "body": """
<section>
<div class="wrap grid">
<article class="card"><span class="kicker">Estate cleanout</span><h3>House and estate cleanouts</h3><p>We clear houses when a family is moving, downsizing, or settling an estate. We haul what you mark. We do not appraise items or act as an estate sale company.</p></article>
<article class="card"><span class="kicker">Eviction cleanout</span><h3>Eviction and apartment cleanouts</h3><p>We haul furniture, trash, and leftover belongings from apartments and rental houses. Landlords and property managers can book the job. Tell us the unit, the access, and what stays.</p></article>
<article class="card"><span class="kicker">Garage cleanout</span><h3>Garage cleanouts</h3><p>Boxes, shelving, sports gear, old tools, and junk that filled the garage. If the load is mostly yard waste or a shed, use the <a href="/yard-waste-removal-springfield-mo">yard and outdoor page</a>.</p></article>
<article class="card"><span class="kicker">Heavy clutter</span><h3>Heavy household clutter</h3><p>We take on houses and storage areas with a lot of belongings. Describe how full the rooms are so the quote matches the work.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Rental turnovers and move-outs</h2>
<p>Moving out of a rental or a student apartment? We haul the furniture, mattresses, and leftover household junk. If you want to donate usable items, call that organization yourself before pickup day. We are not a donation center. Single items such as a couch or mattress are on the <a href="/residential-junk-removal-springfield-mo">residential junk page</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "commercial-junk-removal-springfield-mo.html",
            "href": "/commercial-junk-removal-springfield-mo",
            "crumb": "Commercial",
            "title": "Commercial Junk Removal & Construction Debris in Springfield, MO",
            "description": "Commercial junk removal and construction debris removal in Springfield, MO. Offices, stores, and job sites. Call (417) 242-5370 for a quote.",
            "h1": "Commercial Junk Removal in Springfield, MO",
            "lede": f"We haul junk from offices, shops, rentals, and job sites in Springfield, Missouri. Commercial junk removal and construction debris removal start with a call. Call {phone} and describe the load.",
            "service": "Commercial junk or construction debris",
            "quote_heading": "Quote a commercial or debris job",
            "quote_copy": "<p>Tell us the site, the material, and about how much there is. Include parking and the hours we can get in.</p>",
            "faqs": [
                (
                    "Do you remove construction debris in Springfield?",
                    "Yes. We haul non-hazardous remodel debris such as drywall, lumber, cabinets, and flooring. Concrete, brick, roofing, and dirt need a description before we quote. We do not take asbestos or hazardous waste.",
                ),
                (
                    "Do you haul junk from offices and stores?",
                    "Yes. We pick up furniture, fixtures, boxes, and other commercial junk from offices, retail spaces, and small businesses in Springfield and nearby towns.",
                ),
            ],
            "body": """
<section>
<div class="wrap grid">
<article class="card"><h3>Offices, stores, and rentals</h3><p>Desks, chairs, shelving, fixtures, and boxes from a closeout, a remodel, or a tenant turnover. Property managers booking a unit cleanout can also start on the <a href="/cleanouts-springfield-mo">cleanouts page</a>.</p></article>
<article class="card"><h3>Construction debris removal</h3><p>We haul drywall, lumber, cabinets, flooring, and other leftover remodel material. Tell us if the pile includes concrete, brick, roofing, dirt, or anything hazardous. We will tell you whether that material is part of the quote.</p></article>
</div>
</section>
<section>
<div class="wrap">
<div class="note">We price commercial jobs from the volume, the weight, and the access. There is no published rate card. <a href="/junk-removal-cost-springfield-mo">See what changes a quote</a>.</div>
</div>
</section>
""",
        },
        {
            "file": "yard-waste-removal-springfield-mo.html",
            "href": "/yard-waste-removal-springfield-mo",
            "crumb": "Yard & Outdoor",
            "title": "Yard Waste, Shed & Hot Tub Removal in Springfield, MO",
            "description": "Yard waste removal, shed removal, and hot tub removal in Springfield, MO. Call (417) 242-5370 for a quote.",
            "h1": "Yard Waste and Outdoor Removal in Springfield, MO",
            "lede": f"We haul yard waste, sheds, and hot tubs in Springfield, Missouri. Branches, brush, bagged yard debris, and outdoor junk can go on one quote. Call {phone}.",
            "service": "Yard waste, shed, or hot tub",
            "quote_heading": "Quote yard, shed, or hot tub removal",
            "quote_copy": "<p>Tell us the material, the size, and where it sits on the property.</p>",
            "faqs": [
                (
                    "Do you remove sheds in Springfield, MO?",
                    "Yes. We remove wood and metal sheds. Tell us the size, what it is made of, and what is stored inside. If it has to come apart to be hauled, we include that in the quote.",
                ),
                (
                    "Do you remove hot tubs?",
                    "Yes. We remove hot tubs and spas. Tell us the size and where it sits, including whether it has to come apart to leave the yard or deck.",
                ),
                (
                    "What yard waste do you take?",
                    "Branches, brush, bagged leaves, and outdoor junk. Large stumps, soil, and rocks need a description before we quote them. City yard-waste drop-off rules are separate from our pickup price.",
                ),
            ],
            "body": """
<section>
<div class="wrap grid">
<article class="card"><span class="kicker">Yard waste</span><h3>Yard waste removal</h3><p>We pick up branches, brush, bagged yard debris, and outdoor junk. Springfield's Yardwaste Recycling Center is a city drop-off, not our price. Check the city page if you plan to haul it yourself. Details are in the <a href="/springfield-junk-disposal-guide">disposal guide</a>.</p></article>
<article class="card"><span class="kicker">Shed removal</span><h3>Shed removal</h3><p>We remove wood and metal sheds in Springfield and nearby towns. The quote depends on size, access, and whether the shed has to be taken apart. Tell us what is stored in it.</p></article>
<article class="card"><span class="kicker">Hot tub removal</span><h3>Hot tub removal</h3><p>We remove hot tubs from yards, patios, and decks. Tell us the size and the path out. We quote the teardown when the tub cannot come out in one piece.</p></article>
</div>
</section>
""",
        },
        {
            "file": "junk-removal-service-areas-springfield-mo.html",
            "href": "/junk-removal-service-areas-springfield-mo",
            "crumb": "Service Area",
            "title": "Junk Removal Service Area | Springfield, MO, Battlefield & Nearby",
            "description": "We haul junk in Springfield, MO, plus Battlefield, Nixa, Ozark, Republic, and Willard. Call (417) 242-5370 for a quote.",
            "h1": "Junk Removal Service Area",
            "lede": f"We serve Springfield, Missouri, and nearby towns: Battlefield, Nixa, Ozark, Republic, and Willard. The work is the same in each town. Call {phone} and give us the address.",
            "service": "Other",
            "quote_heading": "Quote a pickup in our service area",
            "quote_copy": "<p>Include the town. We will tell you if the address is in the area we cover.</p>",
            "faqs": [
                (
                    "Do you do junk removal in Battlefield, MO?",
                    "Yes. We haul junk in Battlefield, southwest of Springfield. Household junk, cleanouts, commercial debris, and yard waste are the same services we offer in Springfield. Call (417) 242-5370 with the Battlefield address.",
                ),
                (
                    "Which towns do you cover?",
                    "Springfield, Battlefield, Nixa, Ozark, Republic, and Willard. If your town is not on that list, call and ask. We will tell you yes or no.",
                ),
            ],
            "body": """
<section>
<div class="wrap grid">
<article class="card"><h3>Springfield, MO</h3><p>Our home base for junk removal. Homes, rentals, businesses, and job sites across Springfield.</p></article>
<article class="card"><h3>Battlefield, MO</h3><p>Battlefield junk removal covers the southwest Springfield metro. We haul household junk, cleanouts, commercial debris, yard waste, sheds, and hot tubs in Battlefield.</p></article>
<article class="card"><h3>Nixa, MO</h3><p>Junk removal south of Springfield. Call with the Nixa address and what needs to go.</p></article>
<article class="card"><h3>Ozark, MO</h3><p>Residential and rental junk removal in Ozark. Cleanouts and single-item pickups use the same phone number.</p></article>
<article class="card"><h3>Republic, MO</h3><p>Junk removal west of Springfield in Greene County. Tell us the street and the size of the load.</p></article>
<article class="card"><h3>Willard, MO</h3><p>Junk removal in Willard, in northwest Greene County. We quote the job the same way we do in Springfield.</p></article>
</div>
</section>
<section>
<div class="wrap">
<p>Looking for a job type? Start with <a href="/residential-junk-removal-springfield-mo">residential junk</a>, <a href="/cleanouts-springfield-mo">cleanouts</a>, <a href="/commercial-junk-removal-springfield-mo">commercial and construction debris</a>, or <a href="/yard-waste-removal-springfield-mo">yard waste, sheds, and hot tubs</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "junk-removal-cost-springfield-mo.html",
            "href": "/junk-removal-cost-springfield-mo",
            "crumb": "Cost & FAQ",
            "title": "Junk Removal Cost in Springfield, MO | Call for a Quote",
            "description": "Junk removal cost in Springfield, MO depends on volume, weight, material, and access. Call (417) 242-5370 for a quote. No published price list.",
            "h1": "Junk Removal Cost in Springfield, MO",
            "lede": f"We do not publish junk removal prices. Call {phone} and we will quote your job in Springfield, MO. The quote is based on the load in front of us, not a city fee chart.",
            "service": "Other",
            "quote_heading": "Get the quote for your load",
            "quote_copy": "<p>Photos help. So does a plain list: item types, amount, stairs, and anything heavy or hazardous.</p>",
            "faqs": [
                (
                    "How much does junk removal cost in Springfield, MO?",
                    "Call (417) 242-5370 for a quote. We price each job from the amount, the weight, the material, and the access. We do not publish a price list.",
                ),
                (
                    "Why is there no junk removal price list?",
                    "A couch by the door and a house full of junk are different jobs. We quote after you tell us what you have.",
                ),
                (
                    "Do Springfield landfill fees change the price?",
                    "They can. The City of Springfield publishes rules for Noble Hill Sanitary Landfill and the Yardwaste Recycling Center. Those city charges are not our prices. Call us for the pickup price.",
                ),
                (
                    "What should I tell you so the quote is accurate?",
                    "Item types, about how much there is, stairs or gates, parking, and whether anything is heavy, wet, or hazardous.",
                ),
                (
                    "How does junk removal work?",
                    "You call or send the form. We quote the job. You approve it. We load the junk and haul it away.",
                ),
            ],
            "body": """
<section>
<div class="wrap">
<h2>What changes the quote</h2>
<div class="grid">
<article class="card"><h3>Volume and weight</h3><p>A few pieces cost less to haul than a full garage or a job-site pile. Heavy material takes more of the load.</p></article>
<article class="card"><h3>Material</h3><p>Furniture, household junk, yard waste, and construction debris are priced from what is actually there. Hazardous waste is not part of the job.</p></article>
<article class="card"><h3>Access</h3><p>Stairs, narrow doors, gates, and parking change the labor. Tell us before we quote.</p></article>
</div>
</div>
</section>
<section>
<div class="wrap split">
<div>
<h2>DIY drop-off or a pickup</h2>
<p>You can haul some material yourself. Springfield publishes landfill information for Noble Hill and yard-waste information for the Yardwaste Recycling Center. Facility hours, minimums, and accepted materials change. Check the city site before you load a truck. Those fees are the city's, not ours.</p>
<p>If you want the junk picked up, call for a quote. Links to the city pages are on the <a href="/springfield-junk-disposal-guide">disposal guide</a>.</p>
</div>
<div class="panel">
<h2>How a pickup works</h2>
<ol>
<li>Call or send the form.</li>
<li>We quote the job.</li>
<li>You approve the price.</li>
<li>We load the junk and haul it away.</li>
</ol>
</div>
</div>
</section>
""",
        },
        {
            "file": "contact.html",
            "href": "/contact",
            "crumb": "Contact",
            "title": "Contact Springfield Junk Removal Service | Springfield, MO",
            "description": "Call Springfield Junk Removal Service at (417) 242-5370 or send a quote request. Serving Springfield, MO. No text line.",
            "h1": "Contact Springfield Junk Removal Service",
            "lede": f"Call {phone} or send the form. We quote junk removal in Springfield, MO and nearby towns. We do not publish a street address, and we do not have a text line.",
            "service": "Other",
            "quote_heading": "What to include",
            "quote_copy": "<p>Your name, a phone number, the town, and a short description of the junk. We use that to quote the job.</p><p>Phone: <a href=\"tel:" + PHONE_TEL + "\">" + PHONE_DISPLAY + "</a></p>",
            "faqs": [
                (
                    "How do I contact Springfield Junk Removal Service?",
                    "Call (417) 242-5370 or send the quote form on this page. We do not offer text messaging, and we do not publish a street address.",
                ),
                (
                    "What happens after I send the form?",
                    "We read the description and follow up about a quote. Sending the form does not book the job. The job is booked when you approve the quote.",
                ),
            ],
            "body": """
<section>
<div class="wrap">
<dl class="facts">
<div><dt>Phone</dt><dd><a href="tel:4172425370">(417) 242-5370</a></dd></div>
<div><dt>Area</dt><dd>Springfield, Battlefield, Nixa, Ozark, Republic, Willard</dd></div>
<div><dt>Quote</dt><dd>Call for a quote</dd></div>
<div><dt>Text</dt><dd>No text line</dd></div>
</dl>
</div>
</section>
""",
        },
        {
            "file": "springfield-junk-disposal-guide.html",
            "href": "/springfield-junk-disposal-guide",
            "crumb": "Disposal Guide",
            "title": "Springfield, MO Junk Disposal Guide | Drop-Off or Pickup",
            "description": "Springfield, MO junk disposal options: city drop-off pages, and pickup by Springfield Junk Removal Service. Call (417) 242-5370 for a quote.",
            "h1": "Springfield, MO Junk Disposal Guide",
            "lede": f"Springfield publishes drop-off and recycling pages if you want to haul junk yourself. If you want it picked up, call {phone}. We are a private junk removal company, not the city landfill.",
            "service": "Other",
            "quote_heading": "Want us to haul it?",
            "quote_copy": "<p>Describe the items. We will quote a pickup in Springfield or a nearby town we serve.</p>",
            "faqs": [
                (
                    "Where do I look up disposal rules in Springfield, Missouri?",
                    "Start with the City of Springfield Waste Wizard and Material Know How pages. Hours, fees, and accepted materials change, so read the city page before you drive there.",
                ),
                (
                    "Can Springfield Junk Removal Service haul it instead?",
                    "Yes. Call (417) 242-5370 or send the form. We quote the pickup. We do not take hazardous waste, asbestos, fuel, ammunition, or medical waste.",
                ),
                (
                    "Where do paint, chemicals, and batteries go?",
                    "Not on our truck. Springfield publishes Household Chemical Collection Center guidance, and Missouri DNR publishes household hazardous-waste information. Check those pages for current rules.",
                ),
                (
                    "Are you the City of Springfield?",
                    "No. Springfield Junk Removal Service is a private company. We are not affiliated with the City of Springfield or Missouri DNR.",
                ),
            ],
            "body": """
<section>
<div class="wrap">
<div class="note"><strong>Check the city page before you go.</strong> Hours, fees, appointments, and accepted materials change. We link these pages for research. We are not the operator of any city facility.</div>
</div>
</section>
<section>
<div class="wrap">
<h2>City and state pages</h2>
<ul>
<li><a href="https://www.springfieldmo.gov/5532/Waste-Wizard">Springfield Waste Wizard</a> for item-by-item disposal lookup.</li>
<li><a href="https://www.springfieldmo.gov/5918/Material-Know-How">Material Know How</a> for landfill limits.</li>
<li><a href="https://www.springfieldmo.gov/486/Noble-Hill-Sanitary-Landfill">Noble Hill Sanitary Landfill</a> for self-haul rules.</li>
<li><a href="https://www.springfieldmo.gov/yardwaste">Yardwaste Recycling Center</a> for brush and yard waste.</li>
<li><a href="https://www.springfieldmo.gov/5553/Household-Chemical-Collection-Center">Household Chemical Collection Center</a> for household chemicals.</li>
<li><a href="https://www.springfieldmo.gov/5939/Mattress-Recycling">Mattress recycling</a> for the city's mattress program.</li>
<li><a href="https://dnr.mo.gov/waste-recycling/reduce-reuse-recycle/what-to-do-with-specific/household-hazardous">Missouri DNR household hazardous waste</a>.</li>
</ul>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Furniture and household goods</h3><p>Donate usable items only if the organization agrees to take them. Otherwise we can haul them. See <a href="/residential-junk-removal-springfield-mo">residential junk removal</a>.</p></article>
<article class="card"><h3>Appliances and mattresses</h3><p>Refrigerators and mattresses have extra disposal rules in Springfield. We can pick them up. We do not promise a recycling outcome.</p></article>
<article class="card"><h3>Yard waste and debris</h3><p>Brush can go to the city yard-waste site or on our truck. Remodel debris is on the <a href="/commercial-junk-removal-springfield-mo">commercial and construction debris</a> page.</p></article>
<article class="card"><h3>Paint, fuel, and chemicals</h3><p>We do not haul these. Use the household chemical pages above.</p></article>
</div>
</section>
<section>
<div class="wrap">
<p>Pricing for a pickup is a quote, not a city tipping fee. <a href="/junk-removal-cost-springfield-mo">Junk removal cost in Springfield</a>.</p>
</div>
</section>
""",
        },
    ]


def write_redirects():
    lines = [
        "# 301 redirects for retired Springfield Junk Removal URLs.",
        "# Cloudflare Pages reads this file. It does not change the production branch or project settings.",
        "",
    ]
    for old, new in REMOVED.items():
        for path in (f"/{old}", f"/{old}.html", f"/{old}/"):
            lines.append(f"{path} {new} 301")
    path = os.path.join(ROOT, "_redirects")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def write_sitemap(page_list):
    urls = []
    for page in page_list:
        loc = DOMAIN + "/" if page["href"] == "/" else DOMAIN + page["href"]
        urls.append(f"  <url><loc>{loc}</loc></url>")
    body = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
%s
</urlset>
""" % "\n".join(urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as handle:
        handle.write(body)


def write_robots():
    text = """# Search and AI crawlers may read this site.
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: CCBot
Allow: /

Sitemap: https://springfieldjunkremovalservice.com/sitemap.xml
"""
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


def write_llms():
    text = """# Springfield Junk Removal Service

> Private junk removal company in Springfield, Missouri. We haul household junk, cleanouts, commercial junk, construction debris, yard waste, sheds, and hot tubs. Call for a quote. No published street address and no published price list.

## Contact

- Phone: (417) 242-5370
- Website: https://springfieldjunkremovalservice.com/
- Text messaging: none
- Quote: call or use the form on the site

## Service area

Springfield, Battlefield, Nixa, Ozark, Republic, and Willard, Missouri.

## Pages

- [Junk Removal in Springfield, MO](https://springfieldjunkremovalservice.com/): Homepage. Who we are, what we haul, and how a pickup works.
- [Residential junk removal](https://springfieldjunkremovalservice.com/residential-junk-removal-springfield-mo): Furniture, mattresses, couches, appliances, and household trash.
- [Property cleanouts](https://springfieldjunkremovalservice.com/cleanouts-springfield-mo): Estate, eviction, apartment, garage, house, and move-out cleanouts.
- [Commercial junk and construction debris](https://springfieldjunkremovalservice.com/commercial-junk-removal-springfield-mo): Offices, stores, and non-hazardous remodel debris.
- [Yard waste, sheds, and hot tubs](https://springfieldjunkremovalservice.com/yard-waste-removal-springfield-mo): Brush, sheds, and hot tubs.
- [Service area](https://springfieldjunkremovalservice.com/junk-removal-service-areas-springfield-mo): Springfield plus Battlefield, Nixa, Ozark, Republic, and Willard.
- [Cost and FAQ](https://springfieldjunkremovalservice.com/junk-removal-cost-springfield-mo): Call for a quote. What changes the price. How a pickup works.
- [Springfield disposal guide](https://springfieldjunkremovalservice.com/springfield-junk-disposal-guide): City drop-off links for people hauling junk themselves, plus a pickup option.
- [Contact](https://springfieldjunkremovalservice.com/contact): Phone and quote form.

## We do not haul

Hazardous waste, asbestos, fuel, ammunition, and medical waste.

## Do not invent

This file does not state a street address, a license number, years in business, reviews, ratings, or prices. Those details are not published here.
"""
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


def delete_retired(keep):
    for name in os.listdir(ROOT):
        if not name.endswith(".html"):
            continue
        if name not in keep:
            os.remove(os.path.join(ROOT, name))


def main():
    page_list = pages()
    keep = set()
    for page in page_list:
        html_out = render(page)
        # One H1 check while generating.
        if html_out.count("<h1>") != 1:
            raise SystemExit(f"{page['file']} h1 count != 1")
        if "streetAddress" in html_out or "PostalAddress" in html_out:
            raise SystemExit(f"{page['file']} contains an address schema")
        path = os.path.join(ROOT, page["file"])
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(html_out)
        keep.add(page["file"])
    delete_retired(keep)
    write_sitemap(page_list)
    write_robots()
    write_llms()
    write_redirects()
    print(f"Wrote {len(page_list)} pages and removed retired HTML.")


if __name__ == "__main__":
    main()
