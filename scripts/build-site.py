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
    "couch-removal-springfield-mo": "/residential-junk-removal-springfield-mo",
    "what-items-can-be-removed-springfield-mo": "/residential-junk-removal-springfield-mo",
    "rental-turnover-cleanout-checklist-springfield-mo": "/cleanouts-springfield-mo",
    "springfield-student-move-out-donation-disposal-checklist": "/cleanouts-springfield-mo",
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


def form_html(selected, market="Springfield, MO"):
    options = ['<option value="" disabled>What do you need hauled?</option>']
    for label in SERVICE_OPTIONS:
        sel = " selected" if label == selected else ""
        options.append(f"<option{sel}>{esc(label)}</option>")
    option_html = "\n".join(options)
    return f"""<form action="{FORM}" method="POST">
<input type="hidden" name="site" value="springfieldjunkremovalservice.com">
<input type="hidden" name="market" value="{esc(market)}">
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


def quote_box(selected, market="Springfield, MO"):
    return f"""<div class="quote-box" id="quote">
<h2>Request a Quote</h2>
<p>Tell us what you have. We will quote the job. Prefer to talk? Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
{form_html(selected, market)}
</div>"""


def faq_html(faqs):
    blocks = []
    for q, a in faqs:
        blocks.append(f'<div class="faq"><h3>{esc(q)}</h3><p>{a}</p></div>')
    return "\n".join(blocks)


def crumbs(page):
    if page["href"] == "/":
        return ""
    parts = ['<a href="/">Home</a>']
    for href, label in page.get("parents") or []:
        parts.append(f'<a href="{esc(href)}">{esc(label)}</a>')
    parts.append(esc(page["crumb"]))
    return '<p class="crumbs">' + " / ".join(parts) + "</p>"


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
{nav_html(page.get("nav_href", href))}
</nav>
</details>
</div>
</header>
<main id="main">
<section class="hero">
<div class="wrap">
{crumbs(page)}
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
{quote_box(page["service"], page.get("market", "Springfield, MO"))}
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


def dedicated_pages(phone):
    cleanouts = [("/cleanouts-springfield-mo", "Cleanouts")]
    commercial = [("/commercial-junk-removal-springfield-mo", "Commercial")]
    yard = [("/yard-waste-removal-springfield-mo", "Yard & Outdoor")]
    area = [("/junk-removal-service-areas-springfield-mo", "Service Area")]
    cleanout_service = "Cleanout (estate, eviction, apartment, or garage)"
    return [
        {
            "file": "apartment-cleanout-springfield-mo.html",
            "href": "/apartment-cleanout-springfield-mo",
            "dedicated": True,
            "parents": cleanouts,
            "crumb": "Apartment cleanout",
            "title": "Apartment Cleanout Springfield, MO | Move-Outs",
            "description": "Apartment cleanouts in Springfield, MO for move-outs and rental turnovers. We haul furniture, trash, and leftover belongings. Call (417) 242-5370.",
            "h1": "Apartment Cleanout in Springfield, MO",
            "lede": f"We clean out apartments in Springfield, Missouri. Tenants, landlords, and property managers call {phone} when furniture, trash, and leftover belongings have to leave a unit.",
            "service": cleanout_service,
            "quote_heading": "Quote an apartment cleanout",
            "quote_copy": "<p>Include the unit number, the floor, stairs or an elevator, and what must stay. A one-room pile and a full unit are different quotes.</p>",
            "faqs": [
                (
                    "Do you do apartment cleanouts in Springfield, MO?",
                    "Yes. We haul furniture, trash, boxes, and leftover belongings from Springfield apartments. Call (417) 242-5370 with the unit number and what has to go.",
                ),
                (
                    "Can a landlord book an apartment cleanout?",
                    "Yes. A landlord or property manager can book the haul when they can let us in and can point out what goes. We do not handle lockouts, legal notices, or questions about who owns the belongings.",
                ),
                (
                    "What access details do you need for an apartment?",
                    "The floor, stairs or an elevator, parking, gate or building entry, and anything that must stay in the unit. Those details change the quote.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Apartment move-outs and rental turnovers in Springfield, MO</h2>
<p>An apartment cleanout is a unit job, not a whole house. We haul the couches, beds, dressers, boxes, and bagged trash you list. We do not handle lockouts, court notices, or decide who owns what is inside. Call {phone} and name the complex or the street.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>What usually goes</h3><p>Furniture, mattresses, kitchen leftovers, and boxes from a move-out. A single couch or mattress, with the rest of the unit staying, is a <a href="/residential-junk-removal-springfield-mo">residential pickup</a>, not a full cleanout.</p></article>
<article class="card"><h3>Access in the building</h3><p>Unit number, floor, stairs or an elevator, parking, and any gate or building code. Carrying distance from the unit to where we can load changes the quote. Say what must stay in the unit.</p></article>
<article class="card"><h3>Appliances and problem items</h3><p>Tell us if a refrigerator, washer, or other appliance is part of the job and whether it is still connected. Paint, chemicals, fuel, and anything hazardous stay off the truck. See the <a href="/springfield-junk-disposal-guide">disposal guide</a>.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Who can book the apartment cleanout</h2>
<p>The person who books needs to let us in and point out what goes. That may be the tenant on the way out, or a landlord or property manager once the unit is empty of people. We do not give legal advice about abandonment, notices, or security deposits. A rental house, rather than an apartment, is a <a href="/house-cleanout-springfield-mo">house cleanout</a>. Other property types are on the <a href="/cleanouts-springfield-mo">cleanouts</a> page.</p>
<p>The price depends on how full the unit is and how hard it is to carry the load out. There is no published apartment rate. <a href="/junk-removal-cost-springfield-mo">What changes a junk removal quote</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "estate-cleanout-springfield-mo.html",
            "href": "/estate-cleanout-springfield-mo",
            "dedicated": True,
            "parents": cleanouts,
            "crumb": "Estate cleanout",
            "title": "Estate Cleanout Springfield, MO | House Clearing",
            "description": "Estate cleanouts in Springfield, MO. We haul the furniture and household belongings you mark after a downsizing or an estate. Call (417) 242-5370.",
            "h1": "Estate Cleanout in Springfield, MO",
            "lede": f"We haul furniture and household belongings from Springfield houses when a family is downsizing or settling an estate. You mark what goes. Call {phone}. We do not appraise items or run an estate sale.",
            "service": cleanout_service,
            "quote_heading": "Quote an estate cleanout",
            "quote_copy": "<p>Tell us who will be there, about how full the house is, and whether a garage or basement is included.</p>",
            "faqs": [
                (
                    "Do you do estate cleanouts in Springfield, MO?",
                    "Yes. We haul furniture and household belongings you mark after a downsizing or an estate in Springfield. We do not appraise items or run an estate sale.",
                ),
                (
                    "Will you decide what to keep in an estate?",
                    "No. You, or someone you choose, show us what goes and what stays with the family. We haul the items marked to go.",
                ),
                (
                    "Is an estate cleanout the same as a house cleanout?",
                    "No. An estate cleanout is the haul while a family is sorting a house. A house cleanout empties a home for a move or a vacant rental without that sorting. Both start with a call to (417) 242-5370.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>What an estate cleanout means here</h2>
<p>Families call when a Springfield house holds a lifetime of furniture, boxes, and household goods, and someone has to decide what leaves. We take the items you mark. We do not buy belongings, price them, or act as an estate-sale company. Call {phone} and describe the house.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>You decide what stays</h3><p>Photos, papers, and specific furniture often stay with the family. Walk the rooms with us, or leave notes on what goes. A normal move, with no estate sorting, fits the <a href="/house-cleanout-springfield-mo">house cleanout</a> page better.</p></article>
<article class="card"><h3>Several rooms, not one piece</h3><p>Estate jobs usually cover more than one room, plus a garage, attic, or basement when you include it. One or two pieces, with the house otherwise staying as it is, can go on the <a href="/residential-junk-removal-springfield-mo">residential junk</a> page.</p></article>
<article class="card"><h3>Donation is a separate call</h3><p>If you want usable items donated, contact that organization yourself before pickup day and confirm they will take them. We are not a donation center. Unwanted leftovers can go on our truck.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>What we need before an estate quote</h2>
<p>Tell us who will let us in, about how full the rooms are, and whether a garage or basement is part of the haul. Stairs and parking matter. Hazardous waste, asbestos, fuel, ammunition, and medical waste are not part of the job. Rental and apartment work is listed on the <a href="/cleanouts-springfield-mo">cleanouts</a> page, including the <a href="/apartment-cleanout-springfield-mo">apartment cleanout</a> page when the property is a unit rather than a family house.</p>
</div>
</section>
""",
        },
        {
            "file": "house-cleanout-springfield-mo.html",
            "href": "/house-cleanout-springfield-mo",
            "dedicated": True,
            "parents": cleanouts,
            "crumb": "House cleanout",
            "title": "House Cleanout Springfield, MO | Whole Home",
            "description": "House cleanouts in Springfield, MO for whole homes, basements, and move-outs. We haul the junk you want gone. Call (417) 242-5370.",
            "h1": "House Cleanout in Springfield, MO",
            "lede": f"We empty houses in Springfield, Missouri: rooms, a basement, and an attic when you include them. Call {phone} with the address and how full the home is.",
            "service": cleanout_service,
            "quote_heading": "Quote a house cleanout",
            "quote_copy": "<p>List the floors and rooms that are part of the job. A vacant rental house and a lived-in move are both house cleanouts.</p>",
            "faqs": [
                (
                    "Do you clean out whole houses in Springfield, MO?",
                    "Yes. We haul furniture, boxes, and household junk from the rooms, basement, and attic you include. Call (417) 242-5370 and describe how full the house is.",
                ),
                (
                    "Do you clean out basements as part of a house cleanout?",
                    "Yes, when the basement is part of the house you want emptied. Tell us what is down there. If the rest of the house is staying, describe the basement on its own so the quote matches that pile.",
                ),
                (
                    "Can you clean out a rental house in Springfield?",
                    "Yes. Landlords and property managers can book a rental-house cleanout. We need access and a list of what goes. We do not handle lockouts or legal notices.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Whole-house cleanouts in Springfield, MO</h2>
<p>A house cleanout empties a home. People book it for a move, a vacant rental house, or rooms that filled up over time. It is not the same job as an estate, where a family is sorting what to keep. That work is on the <a href="/estate-cleanout-springfield-mo">estate cleanout</a> page. Call {phone} and say which floors are included.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Rooms, basement, and attic</h3><p>We haul furniture, boxes, bagged trash, and broken household goods from the areas you name. A basement of storage or an attic of old belongings can be part of the same house. Describe each area so the volume in the quote is the volume in the house.</p></article>
<article class="card"><h3>Rental houses</h3><p>Landlords and property managers can book a house when a rental house, not an apartment, needs belongings and trash removed. We need access and a list of what goes. We do not handle lockouts or legal notices. Apartment units are on the <a href="/apartment-cleanout-springfield-mo">apartment cleanout</a> page.</p></article>
<article class="card"><h3>Garage and yard on the same visit</h3><p>A garage of boxes can be included if you say so. A freestanding shed is <a href="/shed-removal-springfield-mo">shed removal</a>. Brush and bagged yard waste are on the <a href="/yard-waste-removal-springfield-mo">yard waste</a> page.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>How a house cleanout quote works</h2>
<p>We quote from the amount, the weight, and the access, including stairs. There is no flat whole-house price on this site. <a href="/junk-removal-cost-springfield-mo">See what changes the quote</a>. A couch or appliance, with the rest of the house staying, belongs on the <a href="/residential-junk-removal-springfield-mo">residential junk removal</a> page. The <a href="/cleanouts-springfield-mo">cleanouts</a> page links the other property types.</p>
</div>
</section>
""",
        },
        {
            "file": "garage-cleanout-springfield-mo.html",
            "href": "/garage-cleanout-springfield-mo",
            "dedicated": True,
            "parents": cleanouts,
            "crumb": "Garage cleanout",
            "title": "Garage Cleanout Springfield, MO | Clutter Haul",
            "description": "Garage cleanouts in Springfield, MO. We haul boxes, shelving, tools, and clutter so you can use the garage again. Call (417) 242-5370.",
            "h1": "Garage Cleanout in Springfield, MO",
            "lede": f"We empty garages in Springfield, Missouri: boxes, shelving, sports gear, old tools, and broken equipment. Call {phone} and say how full the bay is.",
            "service": cleanout_service,
            "quote_heading": "Quote a garage cleanout",
            "quote_copy": "<p>Say whether a vehicle is still parked inside, whether the door opens, and whether the job stops at the garage.</p>",
            "faqs": [
                (
                    "Do you clean out garages in Springfield, MO?",
                    "Yes. We haul boxes, shelving, old tools, sports gear, and broken equipment from Springfield garages. Call (417) 242-5370 and say how full the garage is.",
                ),
                (
                    "What if a car is still in the garage?",
                    "Tell us. A vehicle left inside changes the space we have to work. Say so before we quote the job.",
                ),
                (
                    "Do you take paint and fuel from a garage?",
                    "No. Paint, fuel, solvents, and other hazardous chemicals are not junk we haul. Use the Springfield disposal guide for the city's household chemical drop-off.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Garage cleanouts in Springfield, MO</h2>
<p>This page is the garage, not the whole house. People call when they want the bay usable again for parking or storage. If every room in the home is part of the job, use the <a href="/house-cleanout-springfield-mo">house cleanout</a> page. Call {phone} with a plain description of the pile.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>What we haul from a garage</h3><p>Cardboard, bins, shelves, junk lawn equipment, and furniture that was stored out of the weather. Items you want to keep stay put. Tell us if a car is still parked inside so the working space is clear in the quote.</p></article>
<article class="card"><h3>Chemicals stay off the truck</h3><p>Paint, solvents, fuel, and propane are not garage junk we haul. Springfield's household chemical drop-off is listed in the <a href="/springfield-junk-disposal-guide">disposal guide</a>.</p></article>
<article class="card"><h3>A shed is not a garage</h3><p>A backyard shed is <a href="/shed-removal-springfield-mo">shed removal</a>. Branches and bagged leaves are <a href="/yard-waste-removal-springfield-mo">yard waste</a>. Mention them only if they are mixed into the same visit.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Access for a garage pickup</h2>
<p>Say whether the garage is attached to the house, whether the overhead door opens, and where we can park. A storage loft, a steep driveway, or a wall of shelves changes the work. We quote the load you describe. There is no garage price list. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>. Other property types are on the <a href="/cleanouts-springfield-mo">cleanouts</a> page.</p>
</div>
</section>
""",
        },
        {
            "file": "construction-debris-removal-springfield-mo.html",
            "href": "/construction-debris-removal-springfield-mo",
            "dedicated": True,
            "parents": commercial,
            "crumb": "Construction debris",
            "title": "Construction Debris Removal Springfield, MO",
            "description": "Construction debris removal in Springfield, MO for drywall, lumber, cabinets, and flooring from remodels. Call (417) 242-5370 for a quote.",
            "h1": "Construction Debris Removal in Springfield, MO",
            "lede": f"We haul non-hazardous remodel debris in Springfield, Missouri: drywall, lumber, cabinets, flooring, and fixtures. Call {phone} and describe the pile. Office furniture is a different job.",
            "service": "Commercial junk or construction debris",
            "quote_heading": "Quote a debris haul",
            "quote_copy": "<p>Name the material, about how much there is, and whether it is upstairs or behind a locked job site.</p>",
            "faqs": [
                (
                    "Do you remove construction debris in Springfield, MO?",
                    "Yes. We haul non-hazardous remodel debris such as drywall, lumber, cabinets, and flooring. Call (417) 242-5370 and describe the pile.",
                ),
                (
                    "Do you take concrete, brick, or roofing?",
                    "Only after you describe that material and we include it in the quote. Those loads are not the same as a pile of drywall. We do not take asbestos or hazardous waste.",
                ),
                (
                    "Are you the Springfield landfill?",
                    "No. Noble Hill Sanitary Landfill is a city facility. We are a private junk removal company. City fees and hours are on the city pages, not our price.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Remodel and job-site debris in Springfield, MO</h2>
<p>This page is construction debris, not a store closeout. We haul drywall, lumber, cabinets, flooring, doors, fixtures, and packaging left from a remodel or a small job site. Desks, chairs, and retail fixtures belong on the <a href="/commercial-junk-removal-springfield-mo">commercial junk removal</a> page. Call {phone} before the pile is mixed with trash you have not described.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Debris we can quote from a description</h3><p>Drywall scraps, wood, cabinets, flooring, and fixtures from a kitchen or bath update. Bagged or piled is fine. Tell us the volume and whether it is upstairs or across a lawn.</p></article>
<article class="card"><h3>Heavy material needs its own description</h3><p>Concrete, brick, roofing, dirt, and fill are not the same load as drywall. Describe them before we quote. We will tell you whether that material is part of the job.</p></article>
<article class="card"><h3>Asbestos and hazardous waste</h3><p>We do not haul asbestos, hazardous waste, fuel, or liquids. Older buildings can involve materials that need special handling. We do not do that handling. Paint and chemicals belong at the city's household chemical drop-off.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Springfield disposal context for debris</h2>
<p>If you haul debris yourself, the City of Springfield publishes <a href="https://www.springfieldmo.gov/5918/Material-Know-How">Material Know How</a> and <a href="https://www.springfieldmo.gov/486/Noble-Hill-Sanitary-Landfill">Noble Hill Sanitary Landfill</a>. Those pages describe landfill limits and examples of clean fill, such as uncontaminated soil, concrete, and brick, and they say facility staff verify what they will accept. Hours and fees change. We are not the landfill, and a city tipping fee is not our price.</p>
<p>Mixed remodel debris, including drywall, lumber, and roofing, is a different load from clean fill. Describe shingles, sheet rock, and mixed construction waste as mixed debris. More city links are on the <a href="/springfield-junk-disposal-guide">disposal guide</a>. <a href="/junk-removal-cost-springfield-mo">What changes a quote</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "shed-removal-springfield-mo.html",
            "href": "/shed-removal-springfield-mo",
            "dedicated": True,
            "parents": yard,
            "crumb": "Shed removal",
            "title": "Shed Removal Springfield, MO | Tear Down",
            "description": "Shed removal in Springfield, MO for wood and metal sheds, including teardown when the shed will not come out whole. Call (417) 242-5370.",
            "h1": "Shed Removal in Springfield, MO",
            "lede": f"We remove wood and metal sheds in Springfield, Missouri. Size, access, and whether the shed has to come apart all change the quote. Call {phone} before you take it apart yourself.",
            "service": "Yard waste, shed, or hot tub",
            "quote_heading": "Quote a shed removal",
            "quote_copy": "<p>Include the footprint, the material, what is stored inside, and the path out of the yard.</p>",
            "faqs": [
                (
                    "Do you remove sheds in Springfield, MO?",
                    "Yes. We remove wood and metal sheds. Tell us the size, the material, and what is stored inside. Call (417) 242-5370.",
                ),
                (
                    "Do you take a shed apart?",
                    "When the shed will not come out in one piece, teardown can be part of the quote. Describe the gate, the fence, and the path to the street. We do not promise the shed comes out whole.",
                ),
                (
                    "Does shed removal include the junk inside?",
                    "It does if you want that junk hauled. List what is stored in the shed. A concrete pad is not removed unless you describe it and we include it in the quote.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Wood and metal shed removal in Springfield, MO</h2>
<p>A shed removal is the building, not a bag of leaves. We quote wood, metal, and plastic storage sheds from the size, the material, the path out of the yard, and the contents you want hauled. Brush, bagged leaves, and hot tubs stay on the <a href="/yard-waste-removal-springfield-mo">yard and outdoor</a> page unless you add them to this job. Call {phone} with photos if you have them.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Size and material</h3><p>Tell us the approximate footprint, the height, and whether the shed is wood, metal, or plastic. A small storage box and a large workshop shed are different loads. Photos of each side help.</p></article>
<article class="card"><h3>Teardown and the path out</h3><p>Some sheds will not fit through a gate in one piece. If the shed has to be taken apart, say so. Fences, slopes, and tight side yards change the labor. We include that in the quote when you describe it. We do not promise the shed leaves in one piece.</p></article>
<article class="card"><h3>Contents and the pad</h3><p>Tools, boxes, and junk stored inside are part of the haul if you want them gone. A concrete pad or footings stay unless you describe them and we include them. Concrete and dirt are not assumed.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Shed removal versus a garage cleanout</h2>
<p>An attached garage full of boxes and shelves is a <a href="/garage-cleanout-springfield-mo">garage cleanout</a>. A freestanding shed is this page. If brush is piled around the shed, mention it so we do not quote the building alone. Chemicals stored inside stay off the truck. <a href="/junk-removal-cost-springfield-mo">What changes the price</a>. Nearby towns use the same phone number. <a href="/junk-removal-service-areas-springfield-mo">See the service area</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "junk-removal-battlefield-mo.html",
            "href": "/junk-removal-battlefield-mo",
            "dedicated": True,
            "parents": area,
            "crumb": "Battlefield",
            "title": "Junk Removal Battlefield, MO | Southwest Metro",
            "description": "Junk removal in Battlefield, MO. Household junk, cleanouts, job-site debris, and yard waste southwest of Springfield. Call (417) 242-5370.",
            "h1": "Junk Removal in Battlefield, MO",
            "lede": f"We haul junk at Battlefield, Missouri addresses, southwest of Springfield. Call {phone} with the street address. Household junk, cleanouts, job-site debris, and yard waste use that same number.",
            "service": "Other",
            "quote_heading": "Quote a Battlefield pickup",
            "quote_copy": "<p>Use the Battlefield address, not a Springfield landmark. Include the items, the amount, and any gate or stairs.</p>",
            "faqs": [
                (
                    "Do you do junk removal in Battlefield, MO?",
                    "Yes. We haul household junk, cleanouts, non-hazardous construction debris, and yard waste at Battlefield addresses, southwest of Springfield. Call (417) 242-5370 with the street address.",
                ),
                (
                    "Is this the same page as the Springfield service-area list?",
                    "No. This page is for Battlefield jobs. Nixa, Ozark, and Republic have their own pages. Willard is listed on the service area page.",
                ),
                (
                    "Do you publish a Battlefield street address?",
                    "No. We do not publish a street address. Call (417) 242-5370 or send the quote form with the pickup address in Battlefield.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Junk removal for Battlefield addresses</h2>
<p>Battlefield sits southwest of Springfield. We pick up at Battlefield houses, rentals, and small job sites. The phone number is the Springfield business number, {phone}. We do not publish a shop address in Battlefield or in Springfield. Give us the pickup address and what has to go.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Homes and rentals</h3><p>Furniture, appliances, garage clutter, and move-out piles in Battlefield. A single room can be a <a href="/residential-junk-removal-springfield-mo">residential pickup</a>. A full property is a <a href="/cleanouts-springfield-mo">cleanout</a>, including <a href="/house-cleanout-springfield-mo">house</a> and <a href="/garage-cleanout-springfield-mo">garage</a> jobs.</p></article>
<article class="card"><h3>Job sites in Battlefield</h3><p>Drywall, lumber, cabinets, and other non-hazardous remodel debris. Limits are on the <a href="/construction-debris-removal-springfield-mo">construction debris</a> page. We do not take asbestos or hazardous waste.</p></article>
<article class="card"><h3>Yards and outbuildings</h3><p>Brush, bagged yard waste, and <a href="/shed-removal-springfield-mo">shed removal</a> when a wood or metal shed has to go. Hot tubs are quoted from the <a href="/yard-waste-removal-springfield-mo">yard and outdoor</a> page.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Battlefield and the other towns</h2>
<p>Nixa, Ozark, Republic, and Willard are covered from the same phone number. Nixa, south of Springfield, has its own page: <a href="/junk-removal-nixa-mo">junk removal in Nixa</a>. <a href="/junk-removal-ozark-mo">Ozark</a> and <a href="/junk-removal-republic-mo">Republic</a> do too. Willard stays on the <a href="/junk-removal-service-areas-springfield-mo">service area</a> page. If the address is outside those towns, call and ask. We will tell you yes or no. The quote still depends on volume, weight, material, and access. <a href="/junk-removal-cost-springfield-mo">What changes the price</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "junk-removal-nixa-mo.html",
            "href": "/junk-removal-nixa-mo",
            "dedicated": True,
            "parents": area,
            "crumb": "Nixa",
            "title": "Junk Removal Nixa, MO | South Springfield",
            "description": "Junk removal in Nixa, MO, south of Springfield. Homes, rentals, cleanouts, and job sites. Call (417) 242-5370 for a quote.",
            "h1": "Junk Removal in Nixa, MO",
            "lede": f"We haul junk at Nixa, Missouri addresses, south of Springfield. Call {phone} with the Nixa street, the items, and about how much there is.",
            "service": "Other",
            "quote_heading": "Quote a Nixa pickup",
            "quote_copy": "<p>Put the Nixa address in the message. Say whether the stop is a house, an apartment, a garage, or a job site.</p>",
            "faqs": [
                (
                    "Do you do junk removal in Nixa, MO?",
                    "Yes. We haul junk at Nixa addresses south of Springfield. Call (417) 242-5370 with the street, the items, and about how much there is.",
                ),
                (
                    "Which Nixa jobs can you quote?",
                    "Household junk, apartment and house cleanouts, garage piles, non-hazardous remodel debris, yard waste, and sheds. Hazardous waste, asbestos, fuel, ammunition, and medical waste are not hauled.",
                ),
                (
                    "Is Nixa junk removal priced on this page?",
                    "No price is published for Nixa or for Springfield. The quote depends on volume, weight, material, and access at the address you give us.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Junk removal for Nixa addresses</h2>
<p>Nixa is south of Springfield, and this page is only for Nixa pickups. Battlefield, southwest of Springfield, is a different town. Call {phone} and use the Nixa street address. We do not publish a Nixa shop address or a price list.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Nixa houses and apartments</h3><p>Move-outs, leftover furniture, and garage piles. Name the property type. Apartment details are on the <a href="/apartment-cleanout-springfield-mo">apartment cleanout</a> page. A whole house is a <a href="/house-cleanout-springfield-mo">house cleanout</a>. One couch or appliance, with the rest staying, is <a href="/residential-junk-removal-springfield-mo">residential junk removal</a>.</p></article>
<article class="card"><h3>Job sites south of Springfield</h3><p>Remodel debris in Nixa is quoted from the material, not from a Nixa rate card. Drywall, lumber, cabinets, and flooring are the usual items. Concrete, roofing, and dirt need a description. Read the <a href="/construction-debris-removal-springfield-mo">construction debris</a> page before you book a job site. Hazardous waste and asbestos are not hauled.</p></article>
<article class="card"><h3>Outdoor loads in Nixa</h3><p>Branches, bagged yard waste, and sheds on Nixa lots. Shed size and the path out of the yard are on the <a href="/shed-removal-springfield-mo">shed removal</a> page. City of Springfield drop-off sites are in Springfield, not in Nixa, and their fees are not our prices. Links are in the <a href="/springfield-junk-disposal-guide">disposal guide</a>.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>How Nixa fits the service area</h2>
<p>We also serve Springfield, <a href="/junk-removal-battlefield-mo">Battlefield</a>, <a href="/junk-removal-ozark-mo">Ozark</a>, <a href="/junk-removal-republic-mo">Republic</a>, and Willard. Willard stays on the <a href="/junk-removal-service-areas-springfield-mo">service area</a> hub. A Nixa quote uses the address, gates, stairs, and parking you describe. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>.</p>
</div>
</section>
""",
        },

        {
            "file": "junk-removal-ozark-mo.html",
            "href": "/junk-removal-ozark-mo",
            "dedicated": True,
            "parents": area,
            "nav_href": "/junk-removal-service-areas-springfield-mo",
            "market": "Ozark, MO",
            "crumb": "Ozark",
            "title": "Junk Removal in Ozark, MO",
            "description": "Junk removal in Ozark, MO, the Christian County seat south of Springfield. Homes, rentals, and cleanouts. Call (417) 242-5370 for a quote.",
            "h1": "Junk Removal in Ozark, MO",
            "lede": f"We haul junk in Ozark, Missouri. Ozark is the Christian County seat, south of Springfield, along the Finley River. Call {phone} with the Ozark address and what needs to go.",
            "service": "Other",
            "quote_heading": "Quote a pickup in Ozark",
            "quote_copy": "<p>Include the Ozark street, the items, and whether anything is upstairs or in a garage.</p>",
            "faqs": [
                (
                    "Do you offer junk removal in Ozark, MO?",
                    "Yes. Ozark is in Christian County, south of Springfield. Call (417) 242-5370 with the address and a list of what goes.",
                ),
                (
                    "Do you clean out Ozark rentals and garages?",
                    "Yes. A rental turnover, a garage, or a house can be quoted. Tell us how full it is and who will meet us there. We do not handle lockouts or legal notices.",
                ),
                (
                    "How much does junk removal cost in Ozark?",
                    "Call (417) 242-5370. The quote depends on the amount, the material, and the access. We do not publish a price list for Ozark or Springfield.",
                ),
            ],
            "body": """
<section>
<div class="wrap">
<h2>Junk removal south of Springfield</h2>
<p>Ozark jobs are the same kinds of hauls we do in Springfield: household junk, rental cleanouts, and single items. The address is what changes. Downtown Ozark, neighborhoods on the north side toward Springfield, and the south side of town all use this page. <a href="/junk-removal-nixa-mo">Nixa</a> and <a href="/junk-removal-battlefield-mo">Battlefield</a> have their own pages. Willard stays on the <a href="/junk-removal-service-areas-springfield-mo">service area</a> page. <a href="/junk-removal-republic-mo">Republic</a> is west of Springfield and has its own page.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Homes and rentals</h3><p>Furniture, mattresses, appliances, and leftover household junk from Ozark houses and rentals. One piece or a room. Item details are on the <a href="/residential-junk-removal-springfield-mo">residential junk</a> page.</p></article>
<article class="card"><h3>Cleanouts</h3><p>Garages, move-outs, and houses that need more than a few items hauled. Tell us how full the space is. <a href="/cleanouts-springfield-mo">Property cleanouts</a> use the same phone number, including <a href="/apartment-cleanout-springfield-mo">apartment</a> and <a href="/house-cleanout-springfield-mo">house</a> jobs.</p></article>
<article class="card"><h3>Yards and job sites</h3><p>Brush, <a href="/shed-removal-springfield-mo">sheds</a>, and hot tubs are on the <a href="/yard-waste-removal-springfield-mo">yard and outdoor</a> page. Non-hazardous remodel debris is on the <a href="/construction-debris-removal-springfield-mo">construction debris</a> page.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>What to send with an Ozark quote</h2>
<ul>
<li>The street in Ozark</li>
<li>The items: furniture, appliances, a garage, a rental, or a mix</li>
<li>Stairs, gates, and whether a vehicle is blocking the load</li>
</ul>
<p>The price is a quote for that load. <a href="/junk-removal-cost-springfield-mo">What changes the price</a>. We do not publish a rate card.</p>
</div>
</section>
""",
        },
        {
            "file": "junk-removal-republic-mo.html",
            "href": "/junk-removal-republic-mo",
            "dedicated": True,
            "parents": area,
            "nav_href": "/junk-removal-service-areas-springfield-mo",
            "market": "Republic, MO",
            "crumb": "Republic",
            "title": "Junk Removal in Republic, MO",
            "description": "Junk removal in Republic, MO, west of Springfield in Greene County. Homes, rentals, and non-hazardous remodel debris. Call (417) 242-5370 for a quote.",
            "h1": "Junk Removal in Republic, MO",
            "lede": f"We haul junk in Republic, Missouri, in Greene County west of Springfield. Call {phone} with the Republic street and the size of the load.",
            "service": "Other",
            "quote_heading": "Quote a pickup in Republic",
            "quote_copy": "<p>Name the Republic street, the items, and about how much there is. A single appliance and a garage of remodel debris are different jobs.</p>",
            "faqs": [
                (
                    "Do you provide junk removal in Republic, MO?",
                    "Yes. Republic is in Greene County, west of Springfield. Call (417) 242-5370 with the street and what needs to go.",
                ),
                (
                    "Do you haul remodel debris in Republic?",
                    "Yes, when it is non-hazardous. Drywall, lumber, cabinets, and flooring can go on the quote. Describe concrete, brick, roofing, or dirt before we price them. We do not take asbestos or hazardous waste.",
                ),
                (
                    "Can you pick up one item in Republic?",
                    "Yes. A couch, mattress, or appliance can be a job by itself. A whole house uses the same phone number. Tell us the size of the load either way.",
                ),
            ],
            "body": """
<section>
<div class="wrap">
<h2>Junk removal west of Springfield</h2>
<p>Republic addresses are west of Springfield, in Greene County. We quote streets near the center of town and subdivisions toward the edge of the city from the same details: what the junk is, how much there is, and how we get to it. Ozark is a different town, south of Springfield in Christian County. Those addresses belong on the <a href="/junk-removal-ozark-mo">Ozark junk removal</a> page. <a href="/junk-removal-nixa-mo">Nixa</a> and <a href="/junk-removal-battlefield-mo">Battlefield</a> have their own pages. Willard stays on the <a href="/junk-removal-service-areas-springfield-mo">service area</a> hub.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Single items</h3><p>A couch, a mattress, a refrigerator, or a washer from a Republic house. Say which room it is in. Household loads are described on the <a href="/residential-junk-removal-springfield-mo">residential junk</a> page.</p></article>
<article class="card"><h3>Rentals and houses</h3><p>Move-outs and houses with more than one room of junk. Tell us who will let us in. <a href="/cleanouts-springfield-mo">Cleanouts</a> cover estate, eviction, apartment, and garage jobs.</p></article>
<article class="card"><h3>Remodel piles and yards</h3><p>Drywall, lumber, cabinets, and flooring from a Republic remodel, when the material is not hazardous. Yard waste, sheds, and hot tubs are on the <a href="/yard-waste-removal-springfield-mo">yard and outdoor</a> page. The <a href="/construction-debris-removal-springfield-mo">construction debris</a> page explains what we need before we quote concrete, brick, or roofing.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Republic streets and load size</h2>
<p>Send the street and the size of the load. Include parking and the hours we can get to the property. <a href="/junk-removal-cost-springfield-mo">What changes the price</a>. We do not publish a price list.</p>
</div>
</section>
""",
        },
        {
            "file": "junk-removal-willard-mo.html",
            "href": "/junk-removal-willard-mo",
            "dedicated": True,
            "parents": area,
            "nav_href": "/junk-removal-service-areas-springfield-mo",
            "market": "Willard, MO",
            "crumb": "Willard",
            "title": "Junk Removal in Willard, MO",
            "description": "Junk removal in Willard, MO, northwest of Springfield in Greene County. Homes, rentals, and cleanouts. Call (417) 242-5370 for a quote.",
            "h1": "Junk Removal in Willard, MO",
            "lede": f"We haul junk in Willard, Missouri, northwest of Springfield in Greene County. Call {phone} with the Willard address and what needs to go.",
            "service": "Other",
            "quote_heading": "Quote a pickup in Willard",
            "quote_copy": "<p>Include the Willard street, the items, and whether the job is one room, a garage, or a whole cleanout.</p>",
            "faqs": [
                (
                    "Do you offer junk removal in Willard, MO?",
                    "Yes. Willard is in Greene County, northwest of Springfield. Call (417) 242-5370 with the address and a list of what goes.",
                ),
                (
                    "Do you clean out Willard rentals and garages?",
                    "Yes. A rental turnover, a garage, or a house can be quoted. Tell us how full it is and who will meet us there. We do not handle lockouts or legal notices.",
                ),
                (
                    "How much does junk removal cost in Willard?",
                    "Call (417) 242-5370. The quote depends on the amount, the material, and the access. We do not publish a price list for Willard or Springfield.",
                ),
            ],
            "body": """
<section>
<div class="wrap">
<h2>Junk removal northwest of Springfield</h2>
<p>Willard addresses are northwest of Springfield, in Greene County. Household junk, rental cleanouts, and single items use this page. Republic is a different Greene County town, west of Springfield, and those addresses belong on the <a href="/junk-removal-republic-mo">Republic junk removal</a> page. <a href="/junk-removal-ozark-mo">Ozark</a> is south of Springfield in Christian County. <a href="/junk-removal-nixa-mo">Nixa</a> and <a href="/junk-removal-battlefield-mo">Battlefield</a> have their own pages. The rest of the list is on the <a href="/junk-removal-service-areas-springfield-mo">service area</a> page.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Homes and rentals</h3><p>Furniture, mattresses, appliances, and leftover household junk from Willard houses and rentals. One piece or a room. Item details are on the <a href="/residential-junk-removal-springfield-mo">residential junk</a> page.</p></article>
<article class="card"><h3>Cleanouts</h3><p>Garages, move-outs, and houses that need more than a few items hauled. Tell us how full the space is and who will meet us there. <a href="/cleanouts-springfield-mo">Property cleanouts</a> use the same phone number, including <a href="/garage-cleanout-springfield-mo">garage</a> and <a href="/house-cleanout-springfield-mo">house</a> jobs.</p></article>
<article class="card"><h3>Yards and job sites</h3><p>Brush, <a href="/shed-removal-springfield-mo">sheds</a>, and hot tubs are on the <a href="/yard-waste-removal-springfield-mo">yard and outdoor</a> page. Non-hazardous remodel debris is on the <a href="/construction-debris-removal-springfield-mo">construction debris</a> page.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>What to send with a Willard quote</h2>
<ul>
<li>The street in Willard</li>
<li>The items: furniture, appliances, a garage, a rental, or a mix</li>
<li>Stairs, gates, and whether a vehicle is blocking the load</li>
</ul>
<p>The price is a quote for that load. <a href="/junk-removal-cost-springfield-mo">What changes the price</a>. We do not publish a rate card.</p>
</div>
</section>
""",
        },
        {
            "file": "junk-removal-springfield-mo.html",
            "href": "/junk-removal-springfield-mo",
            "dedicated": True,
            "crumb": "Junk removal",
            "nav_href": "/",
            "title": "Junk Removal Springfield, MO | Pickup Quote",
            "description": "Junk removal in Springfield, MO. We pick up furniture, cleanouts, and other junk at the address. Call (417) 242-5370 for a quote.",
            "h1": "Junk Removal Springfield, MO",
            "lede": f"Springfield Junk Removal Service picks up junk at Springfield, Missouri addresses. You do not drag it to the curb. Call {phone} and describe the load.",
            "service": "Residential junk, furniture, or appliances",
            "quote_heading": "Quote a Springfield pickup",
            "quote_copy": "<p>Name the street or neighborhood, the items, and whether anything is upstairs or behind a gate.</p>",
            "faqs": [
                (
                    "Do you do junk removal in Springfield, MO?",
                    "Yes. We pick up junk at Springfield addresses. Call (417) 242-5370 with the items, the amount, and the access. We quote that load.",
                ),
                (
                    "Do I have to haul the junk to the curb?",
                    "No. We carry it from where it sits. Tell us about stairs, gates, and parking when you call.",
                ),
                (
                    "What should I book if the job is only one kind of junk?",
                    'Use the page that matches the load: <a href="/furniture-removal-springfield-mo">furniture</a>, <a href="/appliance-removal-springfield-mo">appliances</a>, <a href="/mattress-removal-springfield-mo">mattresses</a>, <a href="/trash-removal-springfield-mo">trash</a>, <a href="/cleanouts-springfield-mo">a cleanout</a>, or <a href="/hot-tub-removal-springfield-mo">a hot tub</a>. The full list is on <a href="/junk-removal-services-springfield-mo">junk removal services</a>.',
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>A Springfield pickup, not a drop-off</h2>
<p>This page is for a pickup at a Springfield address. City drop-off sites are a different choice, and their fees are not our price. Those links are on the <a href="/springfield-junk-disposal-guide">disposal guide</a>. Call {phone} if you want the junk loaded and hauled. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Homes</h3><p>Furniture, mattresses, appliances, and household trash are on the <a href="/residential-junk-removal-springfield-mo">residential junk</a> page, with separate pages for <a href="/furniture-removal-springfield-mo">furniture</a>, <a href="/mattress-removal-springfield-mo">mattresses</a>, <a href="/appliance-removal-springfield-mo">appliances</a>, and <a href="/trash-removal-springfield-mo">trash</a>.</p></article>
<article class="card"><h3>Cleanouts</h3><p>A house, garage, apartment, estate, or eviction is a <a href="/cleanouts-springfield-mo">cleanout</a>. Heavy clutter across many rooms is a <a href="/hoarder-cleanout-springfield-mo">hoarder cleanout</a>. Landlords start with <a href="/eviction-cleanout-springfield-mo">eviction cleanout</a> when that is the job.</p></article>
<article class="card"><h3>Businesses and yards</h3><p>Offices and remodel debris are <a href="/commercial-junk-removal-springfield-mo">commercial junk</a>. Brush, sheds, and hot tubs are <a href="/yard-waste-removal-springfield-mo">yard and outdoor</a> work, including <a href="/hot-tub-removal-springfield-mo">hot tub removal</a>.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>What to include in the quote</h2>
<p>Tell us the items, about how much there is, stairs or a gate, and the Springfield street or neighborhood. Nearby towns are <a href="/junk-removal-battlefield-mo">Battlefield</a>, <a href="/junk-removal-nixa-mo">Nixa</a>, <a href="/junk-removal-ozark-mo">Ozark</a>, <a href="/junk-removal-republic-mo">Republic</a>, and <a href="/junk-removal-willard-mo">Willard</a>. If you need a day named, read <a href="/same-day-junk-removal-springfield-mo">same-day junk removal</a>. We do not promise same-day service. The service list is on <a href="/junk-removal-services-springfield-mo">junk removal services</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "junk-removal-services-springfield-mo.html",
            "href": "/junk-removal-services-springfield-mo",
            "dedicated": True,
            "crumb": "Services",
            "nav_href": "/",
            "title": "Junk Removal Services in Springfield, MO",
            "description": "Junk removal services in Springfield, MO: homes, cleanouts, commercial debris, yards, sheds, and hot tubs. Call (417) 242-5370.",
            "h1": "Junk Removal Services in Springfield, MO",
            "lede": f"These are the junk removal services Springfield Junk Removal Service quotes in Springfield, Missouri. Pick the job that matches the load, or call {phone} and describe it.",
            "service": "Other",
            "quote_heading": "Not sure which service to pick?",
            "quote_copy": "<p>Describe the items and the property. We will quote the job that matches what you wrote.</p>",
            "faqs": [
                (
                    "What junk removal services do you offer in Springfield, MO?",
                    "We quote residential junk, furniture, mattresses, appliances, trash, property cleanouts, commercial junk, construction debris, yard waste, sheds, and hot tubs. Call (417) 242-5370.",
                ),
                (
                    "Do you publish prices for each service?",
                    "No. Every service is a quote from the amount, the weight, the material, and the access. We do not publish a price list.",
                ),
                (
                    "Where do you offer these services?",
                    "Springfield, Battlefield, Nixa, Ozark, Republic, and Willard. Call with the address if your town is not on that list.",
                ),
            ],
            "body": """
<section>
<div class="wrap">
<h2>Services we quote in Springfield</h2>
<p>Each link is a booking page for that job. A Springfield pickup can also start on <a href="/junk-removal-springfield-mo">junk removal in Springfield</a>. Hazardous waste, asbestos, fuel, ammunition, and medical waste are not services we offer.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><span class="kicker">Homes</span><h3><a href="/residential-junk-removal-springfield-mo">Residential junk</a></h3><p><a href="/furniture-removal-springfield-mo">Furniture</a>, <a href="/mattress-removal-springfield-mo">mattresses</a>, <a href="/appliance-removal-springfield-mo">appliances</a>, and <a href="/trash-removal-springfield-mo">trash</a>.</p></article>
<article class="card"><span class="kicker">Properties</span><h3><a href="/cleanouts-springfield-mo">Cleanouts</a></h3><p><a href="/estate-cleanout-springfield-mo">Estate</a>, <a href="/eviction-cleanout-springfield-mo">eviction</a>, <a href="/hoarder-cleanout-springfield-mo">hoarder</a>, <a href="/apartment-cleanout-springfield-mo">apartment</a>, <a href="/garage-cleanout-springfield-mo">garage</a>, and <a href="/house-cleanout-springfield-mo">house</a>.</p></article>
<article class="card"><span class="kicker">Job sites</span><h3><a href="/commercial-junk-removal-springfield-mo">Commercial junk</a></h3><p>Offices and stores, plus <a href="/construction-debris-removal-springfield-mo">construction debris</a> that is not hazardous.</p></article>
<article class="card"><span class="kicker">Outdoors</span><h3><a href="/yard-waste-removal-springfield-mo">Yard and outdoor</a></h3><p>Brush and bagged yard waste, <a href="/shed-removal-springfield-mo">sheds</a>, and <a href="/hot-tub-removal-springfield-mo">hot tubs</a>.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Timing, towns, and the quote</h2>
<p>If you need a day named, use <a href="/same-day-junk-removal-springfield-mo">same-day junk removal</a>. We do not promise same-day service. Towns outside Springfield are on the <a href="/junk-removal-service-areas-springfield-mo">service area</a> page. The price is a quote. <a href="/junk-removal-cost-springfield-mo">What changes the price</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "same-day-junk-removal-springfield-mo.html",
            "href": "/same-day-junk-removal-springfield-mo",
            "dedicated": True,
            "crumb": "Same-day",
            "nav_href": "/",
            "title": "Same-Day Junk Removal in Springfield, MO",
            "description": "Same-day junk removal in Springfield, MO when the schedule allows. We do not promise same-day service. Call (417) 242-5370.",
            "h1": "Same-Day Junk Removal in Springfield, MO",
            "lede": f"Call {phone} with the day you need. We will tell you the first time we can be there. We do not promise same-day service.",
            "service": "Other",
            "quote_heading": "Ask about a day",
            "quote_copy": "<p>Name the day, the items, the amount, and the town. We will say whether that day is open.</p>",
            "faqs": [
                (
                    "Do you promise same-day junk removal in Springfield?",
                    "No. Call (417) 242-5370 with the day you need. We will tell you the first time we can be there. We do not promise same-day service.",
                ),
                (
                    "What if you cannot come today?",
                    "We will name the next time we can be there. A call or a form does not book the job until you approve the quote.",
                ),
                (
                    "Does asking for today change the published price?",
                    "We do not publish a price for today or for any other day. The quote still depends on the amount, the weight, the material, and the access.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>What same-day means on this site</h2>
<p>Same-day means you asked for today and we have an opening. It is not a promise, and it is not a separate service with its own price list. Call {phone} and we will tell you yes or no for the day you named. The job is still a quote you approve before it is booked.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>What to say when you call</h3><p>The items, about how much there is, stairs or a gate, the town, and the day you want. A couch by the door and a full house are different answers for the same day.</p></article>
<article class="card"><h3>If today is full</h3><p>We will name the next time we can be there. Sending the form does not hold a spot. You book when you approve the quote.</p></article>
<article class="card"><h3>The job type still matters</h3><p>Household junk is <a href="/residential-junk-removal-springfield-mo">residential removal</a>. A property is a <a href="/cleanouts-springfield-mo">cleanout</a>. The service list is on <a href="/junk-removal-services-springfield-mo">junk removal services</a>.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Springfield and nearby towns</h2>
<p>Ask for Springfield, <a href="/junk-removal-battlefield-mo">Battlefield</a>, <a href="/junk-removal-nixa-mo">Nixa</a>, <a href="/junk-removal-ozark-mo">Ozark</a>, <a href="/junk-removal-republic-mo">Republic</a>, or <a href="/junk-removal-willard-mo">Willard</a>. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a> does not change because you asked for today.</p>
</div>
</section>
""",
        },
        {
            "file": "furniture-removal-springfield-mo.html",
            "href": "/furniture-removal-springfield-mo",
            "dedicated": True,
            "parents": [("/residential-junk-removal-springfield-mo", "Residential")],
            "nav_href": "/residential-junk-removal-springfield-mo",
            "crumb": "Furniture removal",
            "title": "Furniture Removal in Springfield, MO",
            "description": "Furniture removal in Springfield, MO for couches, tables, dressers, and other pieces you want gone. Call (417) 242-5370.",
            "h1": "Furniture Removal in Springfield, MO",
            "lede": f"We haul furniture you want gone from Springfield, Missouri homes. Couches, tables, dressers, and desks. One piece or a room. Call {phone}. We do not move furniture into another house.",
            "service": "Residential junk, furniture, or appliances",
            "quote_heading": "Quote a furniture pickup",
            "quote_copy": "<p>Name the pieces, the rooms, and stairs. A single couch and a house of furniture are different quotes.</p>",
            "faqs": [
                (
                    "Do you remove furniture in Springfield, MO?",
                    "Yes. We haul couches, sectionals, tables, chairs, dressers, desks, and other furniture you want gone. Call (417) 242-5370 and name the pieces.",
                ),
                (
                    "Do you move furniture to another house?",
                    "No. This is junk removal. We haul furniture away. We do not relocate it to a new home.",
                ),
                (
                    "Can you take one couch?",
                    "Yes. One piece is fine. Tell us the room and whether there are stairs. A mattress with the furniture can go on the same quote if you list it.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Furniture we haul in Springfield, MO</h2>
<p>Couches, sectionals, loveseats, recliners, tables, chairs, dressers, desks, and bookcases. Tell us the pieces and the floor they are on. Call {phone}. Mattresses are a separate page if that is the whole job: <a href="/mattress-removal-springfield-mo">mattress removal</a>. Mixed household junk is <a href="/residential-junk-removal-springfield-mo">residential junk removal</a>.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>One piece or a room</h3><p>A couch by the door and a living room of furniture are both furniture removal. Describe the pieces so the quote matches the load.</p></article>
<article class="card"><h3>Stairs and tight doors</h3><p>Say if a piece is upstairs or has to turn through a narrow door. Access changes the labor. We carry it from where it sits.</p></article>
<article class="card"><h3>Not a moving company</h3><p>We haul furniture you are done with. We do not deliver it to another address. A whole house of belongings is a <a href="/house-cleanout-springfield-mo">house cleanout</a>.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Couches and the rest of the house</h2>
<p>Couches are furniture removal. There is no separate couch price on this site. If the couch is the only item, say so. Appliances are <a href="/appliance-removal-springfield-mo">appliance removal</a>. Bagged trash with the furniture can be listed on the same job, or booked as <a href="/trash-removal-springfield-mo">trash removal</a> when trash is the load. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "mattress-removal-springfield-mo.html",
            "href": "/mattress-removal-springfield-mo",
            "dedicated": True,
            "parents": [("/residential-junk-removal-springfield-mo", "Residential")],
            "nav_href": "/residential-junk-removal-springfield-mo",
            "crumb": "Mattress removal",
            "title": "Mattress Removal in Springfield, MO",
            "description": "Mattress removal in Springfield, MO for mattresses and box springs. Tell us the size and the room. Call (417) 242-5370.",
            "h1": "Mattress Removal in Springfield, MO",
            "lede": f"We haul mattresses and box springs in Springfield, Missouri. Tell us the size and the room. Call {phone}. We do not promise a recycling outcome.",
            "service": "Residential junk, furniture, or appliances",
            "quote_heading": "Quote a mattress pickup",
            "quote_copy": "<p>Include the size, how many mattresses, box springs, and whether a bed frame goes too.</p>",
            "faqs": [
                (
                    "Do you pick up mattresses in Springfield, MO?",
                    "Yes. We haul mattresses and box springs. Call (417) 242-5370 with the size and the room. Stains and tears are fine to describe.",
                ),
                (
                    "Do you take box springs and bed frames?",
                    "Box springs, yes. A bed frame can go on the same quote if you list it. Say whether the frame is metal or wood and whether it is already apart.",
                ),
                (
                    "Do you recycle every mattress?",
                    "No. We do not promise a recycling outcome. Springfield publishes its own mattress program. That city page is linked from our disposal guide. It is not our price and not our process.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Mattress and box spring pickup in Springfield, MO</h2>
<p>Twin, full, queen, and king mattresses, plus box springs. One mattress or several. Tell us the floor and the stairs. Call {phone}. A couch or dresser on the same visit is <a href="/furniture-removal-springfield-mo">furniture removal</a> added to the list. Other household junk is <a href="/residential-junk-removal-springfield-mo">residential junk removal</a>.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Size and condition</h3><p>Name the size and how many. A stained or torn mattress can still be hauled. Describe it. We do not need it bagged unless you already bagged it.</p></article>
<article class="card"><h3>Bed frames</h3><p>A frame is part of the job only if you list it. Say if it is still attached to the bed. We quote the pieces you name.</p></article>
<article class="card"><h3>City recycling is separate</h3><p>Springfield's mattress program is a city option if you haul it yourself. The link is on the <a href="/springfield-junk-disposal-guide">disposal guide</a>. We pick the mattress up. We do not promise that it is recycled.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>When a mattress is part of a larger job</h2>
<p>A move-out with furniture, trash, and mattresses may be an <a href="/apartment-cleanout-springfield-mo">apartment cleanout</a> or a <a href="/house-cleanout-springfield-mo">house cleanout</a>. A mattress alone stays on this page. There is no published mattress price. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "appliance-removal-springfield-mo.html",
            "href": "/appliance-removal-springfield-mo",
            "dedicated": True,
            "parents": [("/residential-junk-removal-springfield-mo", "Residential")],
            "nav_href": "/residential-junk-removal-springfield-mo",
            "crumb": "Appliance removal",
            "title": "Appliance Removal in Springfield, MO",
            "description": "Appliance removal in Springfield, MO for refrigerators, washers, dryers, and ovens. Call (417) 242-5370. No refrigerant recovery claim.",
            "h1": "Appliance Removal in Springfield, MO",
            "lede": f"We haul refrigerators, washers, dryers, ovens, dishwashers, and freezers in Springfield, Missouri. Call {phone}. Tell us if the unit is still connected. We do not advertise refrigerant recovery.",
            "service": "Residential junk, furniture, or appliances",
            "quote_heading": "Quote an appliance pickup",
            "quote_copy": "<p>Name the appliance, the floor, and whether it is still hooked up to water, gas, or power.</p>",
            "faqs": [
                (
                    "Do you remove appliances in Springfield, MO?",
                    "Yes. We haul refrigerators, freezers, washers, dryers, ovens, and dishwashers. Call (417) 242-5370 and name the unit.",
                ),
                (
                    "What if the appliance is still connected?",
                    "Tell us. Disconnect scope is confirmed when we quote. We do not assume a gas, water, or power line is already off.",
                ),
                (
                    "Do you recover refrigerant?",
                    "No. We do not advertise refrigerant recovery. We haul the appliance. Say if it is a refrigerator or freezer so the quote matches that unit.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Appliance pickup in Springfield, MO</h2>
<p>Refrigerators, freezers, washers, dryers, ovens, dishwashers, and similar household appliances. One unit or a laundry pair. Call {phone} with the type and the room. Furniture on the same visit can be listed with <a href="/furniture-removal-springfield-mo">furniture removal</a>. The broader household page is <a href="/residential-junk-removal-springfield-mo">residential junk removal</a>.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Connected units</h3><p>Say if the appliance is still on water, gas, or power. We confirm disconnect scope in the quote. We do not assume the lines are already capped or unplugged.</p></article>
<article class="card"><h3>Refrigerators and freezers</h3><p>We haul the box. We do not advertise refrigerant recovery, and we do not promise a recycling certificate. Empty loose food before pickup day if you can.</p></article>
<article class="card"><h3>Stairs and doorways</h3><p>A basement washer and a kitchen refrigerator are different carries. Tell us the floor and any tight turn.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>What we do not take with the appliance</h2>
<p>Fuel, chemicals, and hazardous waste stay off the truck. Those drop-off links are on the <a href="/springfield-junk-disposal-guide">disposal guide</a>. A remodel that left cabinets and flooring is <a href="/construction-debris-removal-springfield-mo">construction debris</a>, not an appliance pickup. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "trash-removal-springfield-mo.html",
            "href": "/trash-removal-springfield-mo",
            "dedicated": True,
            "parents": [("/residential-junk-removal-springfield-mo", "Residential")],
            "nav_href": "/residential-junk-removal-springfield-mo",
            "crumb": "Trash removal",
            "title": "Trash Removal in Springfield, MO",
            "description": "Trash removal in Springfield, MO for bagged household trash and junk that will not fit the cart. Call (417) 242-5370. Not city trash service.",
            "h1": "Trash Removal in Springfield, MO",
            "lede": f"We haul bagged household trash, boxes, and junk that will not fit the cart in Springfield, Missouri. Call {phone}. We are not the city trash service.",
            "service": "Residential junk, furniture, or appliances",
            "quote_heading": "Quote a trash haul",
            "quote_copy": "<p>Say about how many bags or how full the room is, and whether furniture is mixed in.</p>",
            "faqs": [
                (
                    "Do you haul household trash in Springfield, MO?",
                    "Yes. We haul bagged household trash and boxes that will not fit the cart. Call (417) 242-5370 and describe the amount. We are not the city trash service.",
                ),
                (
                    "Do you take hazardous waste with the trash?",
                    "No. Paint, chemicals, fuel, asbestos, ammunition, and medical waste stay off the truck. Use the Springfield disposal guide for city drop-off pages.",
                ),
                (
                    "Is a pile of furniture called trash removal?",
                    "Name the furniture if that is the load. Furniture has its own page. Mixed bags and household junk can stay on this trash removal quote.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Household trash pickup in Springfield, MO</h2>
<p>This is a private haul for extra trash: bags, boxes, and small household junk piled in a garage, basement, or spare room. It is not weekly city cart service, and it is not a city bulk-trash program. Call {phone} with the amount. Furniture pieces are <a href="/furniture-removal-springfield-mo">furniture removal</a>. A mix of household goods is <a href="/residential-junk-removal-springfield-mo">residential junk removal</a>.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Bags, boxes, and clutter</h3><p>Bagged trash, broken household goods, and cardboard. Tell us how many bags or how much of the room is full. Loose food waste should be bagged if you can.</p></article>
<article class="card"><h3>Not the city truck</h3><p>Springfield Junk Removal Service is a private company. City drop-off rules are on the <a href="/springfield-junk-disposal-guide">disposal guide</a>. A city fee is not our price.</p></article>
<article class="card"><h3>What stays off the truck</h3><p>Paint, chemicals, fuel, asbestos, ammunition, and medical waste. If the pile is mostly those items, we cannot haul it as trash.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Trash versus a cleanout</h2>
<p>A few bags is trash removal. A house, apartment, or garage full of belongings is a <a href="/cleanouts-springfield-mo">cleanout</a>. Say which one you have so the quote matches the volume. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "eviction-cleanout-springfield-mo.html",
            "href": "/eviction-cleanout-springfield-mo",
            "dedicated": True,
            "parents": cleanouts,
            "nav_href": "/cleanouts-springfield-mo",
            "crumb": "Eviction cleanout",
            "title": "Eviction Cleanout in Springfield, MO",
            "description": "Eviction cleanouts in Springfield, MO for landlords and property managers. We haul leftover belongings and trash. Call (417) 242-5370.",
            "h1": "Eviction Cleanout in Springfield, MO",
            "lede": f"We haul furniture, trash, and leftover belongings from Springfield rentals when a landlord or property manager can let us in. Call {phone}. We do not handle lockouts, court notices, or ownership questions.",
            "service": cleanout_service,
            "quote_heading": "Quote an eviction cleanout",
            "quote_copy": "<p>Name the property type, who will let us in, the access, and what must stay. We quote the haul.</p>",
            "faqs": [
                (
                    "Do you do eviction cleanouts in Springfield, MO?",
                    "Yes. We haul belongings and trash left in a rental when the person who books can let us in and can point out what goes. Call (417) 242-5370.",
                ),
                (
                    "Do you handle the legal side of an eviction?",
                    "No. We do not file notices, change locks, decide who owns the belongings, or give legal advice. We haul what you show us once we have access.",
                ),
                (
                    "Is an eviction cleanout the same as an apartment move-out?",
                    "No. A tenant move-out is an apartment cleanout or a house cleanout. An eviction cleanout is the haul a landlord or property manager books. Both use the same phone number.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Eviction cleanouts for Springfield rentals</h2>
<p>Landlords and property managers call when a unit still holds furniture, bags, and household junk and someone with access wants it gone. We need that person to let us in and to show what goes and what stays. Call {phone}. We do not decide possession, abandonment, or who owns an item.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Who can book it</h3><p>The person who can open the door and point out the load. Tell us if you are the landlord or the property manager, and whether the property is an apartment or a house.</p></article>
<article class="card"><h3>Apartment or rental house</h3><p>An apartment unit is also described on the <a href="/apartment-cleanout-springfield-mo">apartment cleanout</a> page. A whole rental house is a <a href="/house-cleanout-springfield-mo">house cleanout</a>. Use this page when the job is an eviction cleanout.</p></article>
<article class="card"><h3>What we do not do</h3><p>Lockouts, legal notices, storage decisions, and ownership questions. Hazardous waste and medical waste stay off the truck. We are not a law office.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>What to send with the quote</h2>
<p>Unit or street, floor, stairs or an elevator, parking, and a plain list of furniture and trash. Photos help. Other property types are on the <a href="/cleanouts-springfield-mo">cleanouts</a> page. Heavy clutter in a house the occupant still lives in is a <a href="/hoarder-cleanout-springfield-mo">hoarder cleanout</a>, not this page. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "hoarder-cleanout-springfield-mo.html",
            "href": "/hoarder-cleanout-springfield-mo",
            "dedicated": True,
            "parents": cleanouts,
            "nav_href": "/cleanouts-springfield-mo",
            "crumb": "Hoarder cleanout",
            "title": "Hoarder Cleanout in Springfield, MO",
            "description": "Hoarder cleanouts in Springfield, MO for heavy household clutter. We haul the junk you want gone. Call (417) 242-5370. Not biohazard cleanup.",
            "h1": "Hoarder Cleanout in Springfield, MO",
            "lede": f"We haul heavy household clutter from Springfield homes: furniture, boxes, and bagged trash you want gone. Call {phone}. This is not biohazard, crime-scene, or medical-waste cleanup.",
            "service": cleanout_service,
            "quote_heading": "Quote a heavy-clutter cleanout",
            "quote_copy": "<p>Say how many rooms are full, who will be there, and what must stay. A large house may be quoted as more than one load.</p>",
            "faqs": [
                (
                    "Do you do hoarder cleanouts in Springfield, MO?",
                    "Yes. We haul furniture, boxes, and household junk from homes with heavy clutter. Call (417) 242-5370 and describe how many rooms are full.",
                ),
                (
                    "Do you clean biohazards or medical waste?",
                    "No. We do not do biohazard, crime-scene, or medical-waste cleanup, and we do not take hazardous chemicals. We haul ordinary household junk and furniture you want gone.",
                ),
                (
                    "Will you decide what to keep?",
                    "No. You, or someone you choose, show us what goes and what stays. We haul the items marked to go.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Heavy clutter cleanouts in Springfield, MO</h2>
<p>People use this page when rooms are packed with furniture, boxes, bags, and household goods and a normal single-item pickup is not the job. We call that a heavy clutter cleanout. Call {phone} and describe the rooms. We do not treat it as biohazard remediation, and we do not sort what the household should keep.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>What we haul</h3><p>Furniture, mattresses, boxes, bagged trash, and broken household goods you mark to go. One room or several. Tell us how full each room is.</p></article>
<article class="card"><h3>What we do not haul</h3><p>Hazardous chemicals, fuel, asbestos, ammunition, and medical waste. Biohazard and crime-scene cleanup are not this service. City chemical drop-off is on the <a href="/springfield-junk-disposal-guide">disposal guide</a>.</p></article>
<article class="card"><h3>Access and pace</h3><p>Say who will meet us and whether pathways are blocked. A large house may be quoted as more than one load. We will say so when we quote. We do not promise a single visit.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>How this differs from other cleanouts</h2>
<p>A house being emptied for a move, without the heavy-clutter sorting, is a <a href="/house-cleanout-springfield-mo">house cleanout</a>. A family deciding what to keep after a death is an <a href="/estate-cleanout-springfield-mo">estate cleanout</a>. A landlord clearing a rental is an <a href="/eviction-cleanout-springfield-mo">eviction cleanout</a>. The <a href="/cleanouts-springfield-mo">cleanouts</a> page links those jobs. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "hot-tub-removal-springfield-mo.html",
            "href": "/hot-tub-removal-springfield-mo",
            "dedicated": True,
            "parents": yard,
            "nav_href": "/yard-waste-removal-springfield-mo",
            "crumb": "Hot tub removal",
            "title": "Hot Tub Removal in Springfield, MO",
            "description": "Hot tub removal in Springfield, MO. Tell us the size and the path out. Teardown and disconnect are confirmed in the quote. Call (417) 242-5370.",
            "h1": "Hot Tub Removal in Springfield, MO",
            "lede": f"We remove hot tubs and spas in Springfield, Missouri. Tell us the size and the path out of the yard or deck. Call {phone}. Teardown and utility disconnect are confirmed when we quote, not assumed.",
            "service": "Yard waste, shed, or hot tub",
            "quote_heading": "Quote a hot tub removal",
            "quote_copy": "<p>Include the size, where it sits, the gate or stairs, and whether it is still connected to power or water.</p>",
            "faqs": [
                (
                    "Do you remove hot tubs in Springfield, MO?",
                    "Yes. We remove hot tubs and spas from yards, patios, and decks. Call (417) 242-5370 with the size and the path out.",
                ),
                (
                    "Do you take a hot tub apart?",
                    "When it will not come out in one piece, teardown can be part of the quote. Describe the gate, the fence, and the deck. We do not promise the tub leaves in one piece.",
                ),
                (
                    "Do you disconnect the power and water?",
                    "Only if that scope is in the quote. Tell us if the tub is still wired or plumbed. We do not assume it is already disconnected.",
                ),
            ],
            "body": f"""
<section>
<div class="wrap">
<h2>Hot tub and spa removal in Springfield, MO</h2>
<p>A hot tub removal is the tub, not a bag of leaves. We quote from the size, the location, and the path to where we can load it. Call {phone}. Brush and sheds stay on the <a href="/yard-waste-removal-springfield-mo">yard and outdoor</a> page unless you add them. Sheds have their own page: <a href="/shed-removal-springfield-mo">shed removal</a>.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3>Size and location</h3><p>Tell us the approximate size or seat count, and whether the tub is in a yard, on a patio, or on a deck. Photos of the tub and the path out help.</p></article>
<article class="card"><h3>Path and teardown</h3><p>Gates, fences, stairs, and deck rails change the job. If the tub has to come apart to leave, say so. That teardown is part of the quote when you describe it. We do not promise it comes out whole.</p></article>
<article class="card"><h3>Power and water</h3><p>Say if the tub is still connected. Utility disconnect is confirmed during the quote. We do not assume the power or water is already off, and we do not treat a connected tub as a yard-waste load.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>What else can go on the same visit</h2>
<p>A cover, steps, or a small pile of related junk can be listed. A concrete pad is not removed unless you describe it and we include it. Chemicals and old water-treatment products are not junk we haul. <a href="/junk-removal-cost-springfield-mo">What changes the quote</a>. Nearby towns use the same phone number. <a href="/junk-removal-service-areas-springfield-mo">See the service area</a>.</p>
</div>
</section>
""",
        },
    ]


def pages():
    phone = f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>'
    base = [
        {
            "file": "index.html",
            "href": "/",
            "crumb": "Home",
            "title": "Junk Removal in Springfield, MO | Home & Cleanout Quotes",
            "description": "We haul junk in Springfield, MO: homes, estate and apartment cleanouts, job sites, and yards. No need to drag it to the curb. Call (417) 242-5370 for a quote.",
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
                    'Call with the day you need. We will tell you the first time we can be there. We do not promise same-day service. Details are on the <a href="/same-day-junk-removal-springfield-mo">same-day junk removal</a> page.',
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
<article class="card"><span class="kicker">Homes</span><h3><a href="/residential-junk-removal-springfield-mo">Residential junk</a></h3><p><a href="/furniture-removal-springfield-mo">Furniture</a>, <a href="/mattress-removal-springfield-mo">mattresses</a>, couches, <a href="/appliance-removal-springfield-mo">appliances</a>, and <a href="/trash-removal-springfield-mo">household trash</a>.</p></article>
<article class="card"><span class="kicker">Properties</span><h3><a href="/cleanouts-springfield-mo">Cleanouts</a></h3><p><a href="/estate-cleanout-springfield-mo">Estate</a>, <a href="/eviction-cleanout-springfield-mo">eviction</a>, <a href="/hoarder-cleanout-springfield-mo">hoarder</a>, <a href="/apartment-cleanout-springfield-mo">apartment</a>, <a href="/garage-cleanout-springfield-mo">garage</a>, and <a href="/house-cleanout-springfield-mo">whole-house</a> cleanouts.</p></article>
<article class="card"><span class="kicker">Job sites</span><h3><a href="/commercial-junk-removal-springfield-mo">Commercial and debris</a></h3><p>Office and store junk, plus non-hazardous <a href="/construction-debris-removal-springfield-mo">construction debris</a>.</p></article>
<article class="card"><span class="kicker">Outdoors</span><h3><a href="/yard-waste-removal-springfield-mo">Yard, sheds, and hot tubs</a></h3><p>Brush, bagged yard waste, <a href="/shed-removal-springfield-mo">sheds</a>, and <a href="/hot-tub-removal-springfield-mo">hot tubs</a>.</p></article>
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
<p>We haul junk in Springfield and in <a href="/junk-removal-battlefield-mo">Battlefield</a>, <a href="/junk-removal-nixa-mo">Nixa</a>, <a href="/junk-removal-ozark-mo">Ozark</a>, <a href="/junk-removal-republic-mo">Republic</a>, and <a href="/junk-removal-willard-mo">Willard</a>. <a href="/junk-removal-service-areas-springfield-mo">See the service area</a>. The service list is on <a href="/junk-removal-services-springfield-mo">junk removal services</a>. A Springfield pickup request can also start on <a href="/junk-removal-springfield-mo">junk removal in Springfield</a>.</p>
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
            "title": "Residential Junk Removal in Springfield, MO",
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
<h2><a href="/furniture-removal-springfield-mo">Furniture removal</a></h2>
<p>We pick up couches, sectionals, loveseats, recliners, tables, chairs, dressers, and desks. One piece or a whole room is fine.</p>
</div>
</section>
<section>
<div class="wrap">
<h2><a href="/mattress-removal-springfield-mo">Mattress removal</a></h2>
<p>We haul mattresses and box springs. Tell us the size and the room it is in.</p>
</div>
</section>
<section>
<div class="wrap">
<h2><a href="/appliance-removal-springfield-mo">Appliance removal</a></h2>
<p>Refrigerators, freezers, washers, dryers, ovens, and dishwashers. If a unit is still hooked up, say so when you book. We haul the unit. We do not claim Freon recovery.</p>
</div>
</section>
<section>
<div class="wrap grid">
<article class="card"><h3><a href="/trash-removal-springfield-mo">Household junk and trash</a></h3><p>Boxes, bagged trash, small household goods, shelving, and clutter from closets, basements, and spare rooms.</p></article>
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
            "title": "Property Cleanouts in Springfield, MO",
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
<article class="card"><span class="kicker">Estate cleanout</span><h3><a href="/estate-cleanout-springfield-mo">Estate cleanouts</a></h3><p>We clear houses when a family is downsizing or settling an estate. We haul what you mark. We do not appraise items or act as an estate sale company.</p></article>
<article class="card"><span class="kicker">House cleanout</span><h3><a href="/house-cleanout-springfield-mo">House cleanouts</a></h3><p>We empty whole homes for a move or a vacant rental house, including rooms, a basement, and an attic when you include them.</p></article>
<article class="card"><span class="kicker">Eviction cleanout</span><h3><a href="/eviction-cleanout-springfield-mo">Eviction</a> and <a href="/apartment-cleanout-springfield-mo">apartment cleanouts</a></h3><p>We haul furniture, trash, and leftover belongings from apartments and rental houses. Landlords and property managers can book the job. Tell us the unit, the access, and what stays. Heavy clutter across many rooms is a <a href="/hoarder-cleanout-springfield-mo">hoarder cleanout</a>.</p></article>
<article class="card"><span class="kicker">Garage cleanout</span><h3><a href="/garage-cleanout-springfield-mo">Garage cleanouts</a></h3><p>Boxes, shelving, sports gear, old tools, and junk that filled the garage. If the load is a shed, use the <a href="/shed-removal-springfield-mo">shed removal</a> page.</p></article>
</div>
</section>
<section>
<div class="wrap">
<h2>Rental turnovers and move-outs</h2>
<p>Moving out of a rental or a student apartment? We haul the furniture, mattresses, and leftover household junk. Apartment units are quoted on the <a href="/apartment-cleanout-springfield-mo">apartment cleanout</a> page. A whole rental house is a <a href="/house-cleanout-springfield-mo">house cleanout</a>. If you want to donate usable items, call that organization yourself before pickup day. We are not a donation center. Single items such as a couch or mattress are on the <a href="/residential-junk-removal-springfield-mo">residential junk page</a>.</p>
</div>
</section>
""",
        },
        {
            "file": "commercial-junk-removal-springfield-mo.html",
            "href": "/commercial-junk-removal-springfield-mo",
            "crumb": "Commercial",
            "title": "Commercial Junk Removal in Springfield, MO",
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
<article class="card"><h3>Offices, stores, and rentals</h3><p>Desks, chairs, shelving, fixtures, and boxes from a closeout, a remodel, or a tenant turnover. Property managers booking a unit cleanout can start on the <a href="/cleanouts-springfield-mo">cleanouts page</a> or the <a href="/eviction-cleanout-springfield-mo">eviction cleanout</a> page.</p></article>
<article class="card"><h3><a href="/construction-debris-removal-springfield-mo">Construction debris removal</a></h3><p>We haul drywall, lumber, cabinets, flooring, and other leftover remodel material. Tell us if the pile includes concrete, brick, roofing, dirt, or anything hazardous. We will tell you whether that material is part of the quote.</p></article>
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
<article class="card"><span class="kicker">Shed removal</span><h3><a href="/shed-removal-springfield-mo">Shed removal</a></h3><p>We remove wood and metal sheds in Springfield and nearby towns. The quote depends on size, access, and whether the shed has to be taken apart. Tell us what is stored in it.</p></article>
<article class="card"><span class="kicker">Hot tub removal</span><h3><a href="/hot-tub-removal-springfield-mo">Hot tub removal</a></h3><p>We remove hot tubs from yards, patios, and decks. Tell us the size and the path out. We quote the teardown when the tub cannot come out in one piece.</p></article>
</div>
</section>
""",
        },
        {
            "file": "junk-removal-service-areas-springfield-mo.html",
            "href": "/junk-removal-service-areas-springfield-mo",
            "crumb": "Service Area",
            "title": "Junk Removal Service Area | Springfield, MO",
            "description": "We haul junk in Springfield, MO, plus Battlefield, Nixa, Ozark, Republic, and Willard. Call (417) 242-5370 for a quote.",
            "h1": "Junk Removal Service Area",
            "lede": f"We serve Springfield, Missouri, and nearby towns: Battlefield, Nixa, Ozark, Republic, and Willard. The work is the same in each town. Call {phone} and give us the address.",
            "service": "Other",
            "quote_heading": "Quote a pickup in our service area",
            "quote_copy": "<p>Include the town. We will tell you if the address is in the area we cover.</p>",
            "faqs": [
                (
                    "Do you do junk removal in Battlefield, MO?",
                    'Yes. We haul junk in Battlefield, southwest of Springfield. Household junk, cleanouts, commercial debris, and yard waste are the same services we offer in Springfield. Call (417) 242-5370 with the Battlefield address. Details are on the <a href="/junk-removal-battlefield-mo">Battlefield junk removal</a> page.',
                ),
                (
                    "Do you do junk removal in Nixa, MO?",
                    'Yes. We haul junk in Nixa, south of Springfield. Call (417) 242-5370 with the Nixa address. Details are on the <a href="/junk-removal-nixa-mo">Nixa junk removal</a> page.',
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
<article class="card"><h3><a href="/junk-removal-battlefield-mo">Battlefield, MO</a></h3><p>Battlefield junk removal covers the southwest Springfield metro. We haul household junk, cleanouts, commercial debris, yard waste, sheds, and hot tubs in Battlefield.</p></article>
<article class="card"><h3><a href="/junk-removal-nixa-mo">Nixa, MO</a></h3><p>Junk removal south of Springfield. Call with the Nixa address and what needs to go.</p></article>
<article class="card"><h3><a href="/junk-removal-ozark-mo">Ozark, MO</a></h3><p>Junk removal in Ozark, the Christian County seat south of Springfield. Homes, rentals, and cleanouts use the same phone number.</p></article>
<article class="card"><h3><a href="/junk-removal-republic-mo">Republic, MO</a></h3><p>Junk removal in Republic, west of Springfield in Greene County. Tell us the street and the size of the load.</p></article>
<article class="card"><h3><a href="/junk-removal-willard-mo">Willard, MO</a></h3><p>Junk removal in Willard, northwest of Springfield in Greene County. Homes, rentals, and cleanouts use the same phone number.</p></article>
</div>
</section>
<section>
<div class="wrap">
<p>Looking for a job type? Start with <a href="/junk-removal-services-springfield-mo">junk removal services</a>, <a href="/residential-junk-removal-springfield-mo">residential junk</a>, <a href="/cleanouts-springfield-mo">cleanouts</a>, <a href="/commercial-junk-removal-springfield-mo">commercial junk</a>, <a href="/construction-debris-removal-springfield-mo">construction debris</a>, or <a href="/yard-waste-removal-springfield-mo">yard waste, sheds, and hot tubs</a>.</p>
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
<article class="card"><h3>Material</h3><p>Furniture, household junk, yard waste, and construction debris are priced from what is actually there. Hazardous waste is not part of the job. See <a href="/furniture-removal-springfield-mo">furniture</a>, <a href="/appliance-removal-springfield-mo">appliances</a>, <a href="/mattress-removal-springfield-mo">mattresses</a>, <a href="/trash-removal-springfield-mo">trash</a>, and <a href="/hot-tub-removal-springfield-mo">hot tubs</a>.</p></article>
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
<article class="card"><h3>Furniture and household goods</h3><p>Donate usable items only if the organization agrees to take them. Otherwise we can haul them. See <a href="/furniture-removal-springfield-mo">furniture removal</a> and <a href="/residential-junk-removal-springfield-mo">residential junk removal</a>.</p></article>
<article class="card"><h3>Appliances and mattresses</h3><p>Refrigerators and mattresses have extra disposal rules in Springfield. We can pick them up. We do not promise a recycling outcome. Start with <a href="/appliance-removal-springfield-mo">appliance removal</a> or <a href="/mattress-removal-springfield-mo">mattress removal</a>.</p></article>
<article class="card"><h3>Yard waste and debris</h3><p>Brush can go to the city yard-waste site or on our truck. Remodel debris is on the <a href="/construction-debris-removal-springfield-mo">construction debris</a> page. Office and store junk is on the <a href="/commercial-junk-removal-springfield-mo">commercial</a> page.</p></article>
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
    extra = {page["file"]: page for page in dedicated_pages(phone)}
    after = {
        "index.html": [
            "junk-removal-springfield-mo.html",
            "junk-removal-services-springfield-mo.html",
            "same-day-junk-removal-springfield-mo.html",
        ],
        "residential-junk-removal-springfield-mo.html": [
            "furniture-removal-springfield-mo.html",
            "mattress-removal-springfield-mo.html",
            "appliance-removal-springfield-mo.html",
            "trash-removal-springfield-mo.html",
        ],
        "cleanouts-springfield-mo.html": [
            "apartment-cleanout-springfield-mo.html",
            "estate-cleanout-springfield-mo.html",
            "house-cleanout-springfield-mo.html",
            "garage-cleanout-springfield-mo.html",
            "eviction-cleanout-springfield-mo.html",
            "hoarder-cleanout-springfield-mo.html",
        ],
        "commercial-junk-removal-springfield-mo.html": [
            "construction-debris-removal-springfield-mo.html",
        ],
        "yard-waste-removal-springfield-mo.html": [
            "shed-removal-springfield-mo.html",
            "hot-tub-removal-springfield-mo.html",
        ],
        "junk-removal-service-areas-springfield-mo.html": [
            "junk-removal-battlefield-mo.html",
            "junk-removal-nixa-mo.html",
            "junk-removal-ozark-mo.html",
            "junk-removal-republic-mo.html",
            "junk-removal-willard-mo.html",
        ],
    }
    ordered = []
    for item in base:
        ordered.append(item)
        for name in after.get(item["file"], []):
            ordered.append(extra.pop(name))
    if extra:
        raise SystemExit("unplaced dedicated pages: " + ", ".join(sorted(extra)))
    return ordered


def write_redirects():
    lines = [
        "# 301 redirects for retired Springfield Junk Removal URLs.",
        "# Cloudflare Pages reads this file. It does not change the production branch or project settings.",
        "# Restored pages are real HTML and must stay out of this file:",
        "# apartment, estate, house, garage, eviction, and hoarder cleanouts;",
        "# furniture, mattress, appliance, trash, same-day, and hot tub removal;",
        "# junk-removal-springfield-mo and junk-removal-services-springfield-mo;",
        "# shed removal; construction debris;",
        "# Battlefield; Nixa; Ozark; Republic; Willard.",
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
- [Junk removal Springfield, MO](https://springfieldjunkremovalservice.com/junk-removal-springfield-mo): Pickup at a Springfield address. Routes to the job-type pages.
- [Junk removal services](https://springfieldjunkremovalservice.com/junk-removal-services-springfield-mo): List of services we quote.
- [Same-day junk removal](https://springfieldjunkremovalservice.com/same-day-junk-removal-springfield-mo): Ask for a day. Same-day service is not promised.
- [Residential junk removal](https://springfieldjunkremovalservice.com/residential-junk-removal-springfield-mo): Furniture, mattresses, couches, appliances, and household trash.
- [Furniture removal](https://springfieldjunkremovalservice.com/furniture-removal-springfield-mo): Couches, tables, dressers, and other furniture hauled away. Not a move into another house.
- [Mattress removal](https://springfieldjunkremovalservice.com/mattress-removal-springfield-mo): Mattresses and box springs. No promised recycling outcome.
- [Appliance removal](https://springfieldjunkremovalservice.com/appliance-removal-springfield-mo): Refrigerators, washers, dryers, and similar units. No refrigerant recovery claim.
- [Trash removal](https://springfieldjunkremovalservice.com/trash-removal-springfield-mo): Bagged household trash and junk that will not fit the cart. Not city trash service.
- [Property cleanouts](https://springfieldjunkremovalservice.com/cleanouts-springfield-mo): Hub for estate, eviction, apartment, garage, house, hoarder, and move-out cleanouts.
- [Apartment cleanout](https://springfieldjunkremovalservice.com/apartment-cleanout-springfield-mo): Springfield apartment move-outs and rental turnovers.
- [Estate cleanout](https://springfieldjunkremovalservice.com/estate-cleanout-springfield-mo): Belongings a family marks to leave a Springfield house. Not an estate sale.
- [House cleanout](https://springfieldjunkremovalservice.com/house-cleanout-springfield-mo): Whole-home cleanouts, including basements and rental houses.
- [Garage cleanout](https://springfieldjunkremovalservice.com/garage-cleanout-springfield-mo): Boxes, shelving, tools, and garage clutter.
- [Eviction cleanout](https://springfieldjunkremovalservice.com/eviction-cleanout-springfield-mo): Landlord or property-manager haul. Not legal advice, lockouts, or ownership decisions.
- [Hoarder cleanout](https://springfieldjunkremovalservice.com/hoarder-cleanout-springfield-mo): Heavy household clutter. Not biohazard or medical-waste cleanup.
- [Commercial junk](https://springfieldjunkremovalservice.com/commercial-junk-removal-springfield-mo): Offices, stores, and other commercial junk.
- [Construction debris removal](https://springfieldjunkremovalservice.com/construction-debris-removal-springfield-mo): Non-hazardous remodel debris. Not asbestos.
- [Yard waste and hot tubs](https://springfieldjunkremovalservice.com/yard-waste-removal-springfield-mo): Brush, yard waste, sheds, and hot tubs.
- [Shed removal](https://springfieldjunkremovalservice.com/shed-removal-springfield-mo): Wood and metal shed removal and teardown when needed.
- [Hot tub removal](https://springfieldjunkremovalservice.com/hot-tub-removal-springfield-mo): Hot tubs and spas. Teardown and utility disconnect are confirmed in the quote.
- [Service area](https://springfieldjunkremovalservice.com/junk-removal-service-areas-springfield-mo): Hub for Springfield plus Battlefield, Nixa, Ozark, Republic, and Willard.
- [Junk removal in Battlefield](https://springfieldjunkremovalservice.com/junk-removal-battlefield-mo): Battlefield, MO, southwest of Springfield.
- [Junk removal in Nixa](https://springfieldjunkremovalservice.com/junk-removal-nixa-mo): Nixa, MO, south of Springfield.
- [Junk removal in Ozark, MO](https://springfieldjunkremovalservice.com/junk-removal-ozark-mo): Christian County, south of Springfield. Homes, rentals, and cleanouts.
- [Junk removal in Republic, MO](https://springfieldjunkremovalservice.com/junk-removal-republic-mo): Greene County, west of Springfield. Homes, rentals, and remodel debris.
- [Junk removal in Willard, MO](https://springfieldjunkremovalservice.com/junk-removal-willard-mo): Greene County, northwest of Springfield. Homes, rentals, and cleanouts.
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


def render_404():
    """Unknown URLs. Cloudflare Pages serves this file with HTTP 404.

    Without a top-level 404.html, Pages treats the project as a single-page
    app and serves the homepage with HTTP 200 for missing paths.
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{GTM}
{GA4_NOTE}
<title>Page Not Found | Springfield Junk Removal</title>
<meta name="description" content="That page is not on Springfield Junk Removal Service. Call (417) 242-5370 or use the quote form.">
<meta name="robots" content="noindex, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Springfield Junk Removal Service">
<meta property="og:title" content="Page Not Found | Springfield Junk Removal">
<meta property="og:description" content="That page is not on Springfield Junk Removal Service. Call (417) 242-5370 or use the quote form.">
<meta property="og:locale" content="en_US">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#14221b">
<link rel="stylesheet" href="/site.css">
<script type="application/ld+json">
{json_ld(business_ld())}
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
{nav_html("")}
</nav>
</details>
</div>
</header>
<main id="main">
<section class="hero">
<div class="wrap">
<p class="crumbs"><a href="/">Home</a> / Page not found</p>
<h1>Page not found</h1>
<p class="lede">That address is not a page on this site. Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or pick a page below.</p>
<div class="cta">
<a class="btn" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
<a class="btn dark" href="/">Back to home</a>
</div>
</div>
</section>
<section>
<div class="wrap">
<h2>Pages on this site</h2>
<ul>
<li><a href="/junk-removal-springfield-mo">Junk removal in Springfield, MO</a> and <a href="/junk-removal-services-springfield-mo">services</a></li>
<li><a href="/same-day-junk-removal-springfield-mo">Same-day junk removal</a>. We do not promise same-day service.</li>
<li><a href="/residential-junk-removal-springfield-mo">Residential junk removal</a>, including <a href="/furniture-removal-springfield-mo">furniture</a>, <a href="/mattress-removal-springfield-mo">mattresses</a>, <a href="/appliance-removal-springfield-mo">appliances</a>, and <a href="/trash-removal-springfield-mo">trash</a></li>
<li><a href="/cleanouts-springfield-mo">Cleanouts</a>, including <a href="/apartment-cleanout-springfield-mo">apartment</a>, <a href="/estate-cleanout-springfield-mo">estate</a>, <a href="/house-cleanout-springfield-mo">house</a>, <a href="/garage-cleanout-springfield-mo">garage</a>, <a href="/eviction-cleanout-springfield-mo">eviction</a>, and <a href="/hoarder-cleanout-springfield-mo">hoarder</a></li>
<li><a href="/commercial-junk-removal-springfield-mo">Commercial junk</a> and <a href="/construction-debris-removal-springfield-mo">construction debris</a></li>
<li><a href="/yard-waste-removal-springfield-mo">Yard waste</a>, <a href="/shed-removal-springfield-mo">shed removal</a>, and <a href="/hot-tub-removal-springfield-mo">hot tub removal</a></li>
<li><a href="/junk-removal-service-areas-springfield-mo">Service area</a>, including <a href="/junk-removal-battlefield-mo">Battlefield</a>, <a href="/junk-removal-nixa-mo">Nixa</a>, <a href="/junk-removal-ozark-mo">Ozark</a>, <a href="/junk-removal-republic-mo">Republic</a>, and <a href="/junk-removal-willard-mo">Willard</a></li>
<li><a href="/junk-removal-cost-springfield-mo">Cost and FAQ</a></li>
<li><a href="/springfield-junk-disposal-guide">Disposal guide</a></li>
<li><a href="/contact">Contact</a></li>
</ul>
</div>
</section>
<section>
<div class="wrap split">
<div>
<h2>Request a quote anyway</h2>
<p>If you reached this page from an old link, the form still works. Tell us the town and what needs to be hauled.</p>
</div>
{quote_box("Other")}
</div>
</section>
</main>
{footer_html()}
<script src="/analytics-events.js"></script>
</body>
</html>
"""


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
        if len(page["title"]) > 60:
            raise SystemExit(f"{page['file']} title is {len(page['title'])} chars")
        if page.get("dedicated"):
            h1 = page["h1"]
            places = ("Springfield, MO", "Battlefield, MO", "Nixa, MO", "Ozark, MO", "Republic, MO", "Willard, MO")
            if not any(place in h1 for place in places):
                raise SystemExit(f"{page['file']} H1 missing place name")
            if f'href="{page["href"]}"' not in html_out and page["href"] not in html_out:
                raise SystemExit(f"{page['file']} missing self canonical")
        path = os.path.join(ROOT, page["file"])
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(html_out)
        keep.add(page["file"])
    not_found = render_404()
    if not_found.count("<h1>") != 1 or "noindex" not in not_found or 'rel="canonical"' in not_found:
        raise SystemExit("404.html must have one H1, noindex, and no canonical")
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as handle:
        handle.write(not_found)
    keep.add("404.html")
    delete_retired(keep)
    write_sitemap(page_list)
    write_robots()
    write_llms()
    write_redirects()
    print(f"Wrote {len(page_list)} pages, 404.html, and removed retired HTML.")


if __name__ == "__main__":
    main()
