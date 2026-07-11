#!/usr/bin/env python3
"""Bulk claim-safe copy pass for Springfield Junk Removal static HTML pages.

REUSABLE MIGRATION TOOL — do not run against production HTML without reviewing
the full git diff. Intended for new markets/niches or controlled batch updates.
"""

import re
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRUST_FULL = """
    <section id="trust-process">
      <div class="wrap">
        <h2>How the Quote Request Works</h2>
        <p>
          Call <a href="tel:4172425370">(417) 242-5370</a> or submit the quote form with a short description of
          what you need removed. Your request can be reviewed for availability, and pickup scope and accepted
          items are confirmed during the quote process. There is no obligation to book after receiving quote
          details.
        </p>

        <div class="grid">
          <div class="card">
            <h3>Information to include</h3>
            <ul>
              <li>Items or project type (furniture, cleanout, debris, etc.)</li>
              <li>Approximate volume and any heavy or awkward pieces</li>
              <li>Location in the home, yard, or building</li>
              <li>Access details (stairs, gate width, parking)</li>
              <li>Photos, if available, and your preferred timing</li>
            </ul>
          </div>
          <div class="card">
            <h3>Items and services requiring confirmation</h3>
            <ul>
              <li>Hot tubs, sheds, and large outdoor structures</li>
              <li>Appliances — utility disconnect status</li>
              <li>Construction or renovation debris volumes</li>
              <li>Heavy clutter cleanouts — scope and access</li>
              <li>Items that may need special disposal handling</li>
            </ul>
          </div>
          <div class="card">
            <h3>Service area and availability</h3>
            <ul>
              <li>Springfield and nearby Greene County communities</li>
              <li>Nixa, Ozark, Republic, Battlefield, and Willard</li>
              <li>Same-day or next-day timing when scheduling allows</li>
              <li>No-obligation quote details after review</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
"""

TRUST_COMPACT = """
        <h3>Quote request and confirmation</h3>
        <p>
          Your request can be reviewed for availability. Pickup scope and accepted items are confirmed during
          the quote process. There is no obligation to book after receiving quote details.
        </p>
"""

# Order matters — more specific first
GLOBAL_REPLACEMENTS = [
    (r"What We Can Haul", "What Can Be Removed"),
    (r"our crew loads it up and hauls it away", "items are loaded and removed on pickup day"),
    (r"Our crew loads it up and hauls it away", "Items are loaded and removed on pickup day"),
    (r"our crew loads everything up and hauls it off", "items are loaded and removed on pickup day"),
    (r"our crew loads everything", "items are loaded on pickup day"),
    (r"Our crew loads everything", "Items are loaded on pickup day"),
    (r"our crew breaks it down", "removal scope may include breaking the unit into sections"),
    (r"Our crew breaks it down", "Removal scope may include breaking the unit into sections"),
    (r"our crew and the tools", "the right approach"),
    (r"our crew", "pickup"),
    (r"Our crew", "Pickup"),
    (r"our truck", "the load"),
    (r"Our truck", "The load"),
    (r"onto the truck", "for removal"),
    (r"onto our truck", "for removal"),
    (r"in the truck", "in the load"),
    (r"full truckload", "large load"),
    (r"Full truckload", "Large load"),
    (r"full-service junk hauling crew", "resource for junk removal requests"),
    (r"Full-Service Junk Hauling", "Junk Removal Requests"),
    (r"full-service junk removal", "junk removal requests"),
    (r"Full-service junk removal", "Junk removal requests"),
    (r"your local crew for", "a local resource for"),
    (r"We do the lifting and loading", "Loading is part of the pickup scope"),
    (r"we do the lifting and loading", "loading is part of the pickup scope"),
    (r"We do the work so you don't have to", "Pickup scope is confirmed during the quote process"),
    (r"we do the work so you don't have to", "pickup scope is confirmed during the quote process"),
    (r"We handle the full job", "Removal scope is confirmed during the quote process"),
    (r"we handle the full job", "removal scope is confirmed during the quote process"),
    (r"We handle the labor and the disposal", "Labor and disposal are confirmed during the quote process"),
    (r"We handle the labor", "Labor requirements are confirmed during the quote process"),
    (r"we handle the labor", "labor requirements are confirmed during the quote process"),
    (r"We handle the demolition and the cleanup", "Teardown and cleanup scope are confirmed during the quote process"),
    (r"we handle the demolition", "teardown scope is confirmed during the quote process"),
    (r"We handle wood sheds", "Wood shed removal requests can be reviewed"),
    (r"We handle", "Your request can be reviewed for"),
    (r"we handle", "your request can be reviewed for"),
    (r"We haul away", "Removal requests can include"),
    (r"we haul away", "removal requests can include"),
    (r"We haul off", "Removal requests can include"),
    (r"we haul off", "removal requests can include"),
    (r"We haul it off", "It can be removed"),
    (r"we haul it off", "it can be removed"),
    (r"We haul it away", "It can be removed"),
    (r"we haul it away", "it can be removed"),
    (r"We haul", "Removal requests can include"),
    (r"we haul", "removal requests can include"),
    (r"We load and haul", "Loading and removal"),
    (r"we load and haul", "loading and removal"),
    (r"We load it up and haul it away", "Items can be loaded and removed on pickup day"),
    (r"we load it up and haul it away", "items can be loaded and removed on pickup day"),
    (r"We load", "Loading"),
    (r"we load", "loading"),
    (r"We clear", "Cleanout requests can include"),
    (r"we clear", "cleanout requests can include"),
    (r"We bring the tools and the muscle", "Removal scope is confirmed during the quote process"),
    (r"We bring the crew and the tools", "Removal scope is confirmed during the quote process"),
    (r"We bring", "Junk removal help can be requested for"),
    (r"we bring", "junk removal help can be requested for"),
    (r"we'll haul", "removal can be arranged"),
    (r"We'll Haul", "Request Removal For"),
    (r"we'll follow up with quote details", "quote details are provided after your request is reviewed"),
    (r"we'll follow up", "your request will be reviewed"),
    (r"we'll let you know", "you'll receive availability details"),
    (r"we'll plan", "scope is confirmed during the quote process"),
    (r"we'll point you", "the right service page can help"),
    (r"we'll take care of it", "scope is confirmed during the quote process"),
    (r"we'll plan the removal", "removal scope is confirmed during the quote process"),
    (r"we'll plan accordingly", "scope is confirmed during the quote process"),
    (r"we'll give you", "you can receive"),
    (r"before we arrive", "before pickup"),
    (r"before we start", "before pickup begins"),
    (r"when we arrive", "on pickup day"),
    (r"When we're done", "After removal"),
    (r"when we're done", "after removal"),
    (r"We serve", "Service requests are accepted for"),
    (r"we serve", "service requests are accepted for"),
    (r"We help", "You can request help with"),
    (r"we help", "you can request help with"),
    (r"We get that", "Many homeowners understand that"),
    (r"We get that\.", "Many homeowners understand that."),
    (r"Our role is to make", "The goal is to make"),
    (r"Our job is to show up", "Pickup scope is confirmed during the quote process"),
    (r"Our job is to", "The goal is to"),
    (r"we never rush", "the pace stays under your direction"),
    (r"We move carefully", "Work proceeds carefully"),
    (r"we move carefully", "work proceeds carefully"),
    (r"We focus on", "Requests can focus on"),
    (r"we focus on", "requests can focus on"),
    (r"We do not provide", "Biohazard, crime-scene, medical-waste, and hazardous-material remediation are not assumed and require separate confirmation. Requests do not include"),
    (r"we do not provide", "biohazard, crime-scene, medical-waste, and hazardous-material remediation are not assumed and require separate confirmation. Requests do not include"),
    (r"donate, and remove", "sort for keep, removal, or donation where options exist"),
    (r"donation and recycling", "donation or recycling options"),
    (r"we donate", "donation options may be available"),
    (r"We donate", "Donation options may be available"),
    (r"we recycle", "recycling options may be available"),
    (r"We recycle", "Recycling options may be available"),
    (r"a local provider can", "your request can be reviewed for"),
    (r"A local provider can", "Your request can be reviewed for"),
    (r"Spa Demolition", "Spa Removal"),
    (r"Shed Teardown", "Shed Removal"),
    (r"Shed Demolition", "Shed Removal"),
    (r"Hot Tub Demolition", "Hot Tub Removal"),
    (r"tear down and haul", "removal and haul-away"),
    (r"Tear down and haul", "Removal and haul-away"),
    (r"tears down and hauls", "removal requests can include teardown and haul-away"),
    (r"tear down and hauls", "removal requests can include teardown and haul-away"),
    (r"We tear down", "Teardown scope is confirmed during the quote process for"),
    (r"we tear down", "teardown scope is confirmed during the quote process for"),
    (r"We dismantle", "Teardown scope may include dismantling"),
    (r"we dismantle", "teardown scope may include dismantling"),
    (r"we typically dismantle", "teardown scope may include dismantling"),
    (r"We typically dismantle", "Teardown scope may include dismantling"),
    (r"we cut the tub down", "breaking the tub into sections may be part of removal scope"),
    (r"We cut the tub down", "Breaking the tub into sections may be part of removal scope"),
    (r"disconnects, breaks down, and hauls", "removal requests for hot tubs and spas"),
    (r"We disconnect", "Utility disconnect status should be confirmed for"),
    (r"we disconnect", "utility disconnect status should be confirmed for"),
    (r"disconnect, break down, and haul", "removal requests for"),
    (r"Electrical disconnection should be handled safely", "Electrical disconnect status should be confirmed before pickup"),
    (r"disconnected from power", "utility disconnect status confirmed"),
    (r"hoarding cleanout help", "heavy clutter cleanout requests"),
    (r"hoarding cleanout", "heavy clutter cleanout"),
    (r"Hoarding cleanout", "Heavy clutter cleanout"),
    (r"patient, judgment-free hoarding cleanout", "patient, judgment-free heavy clutter cleanout"),
    (r"heavily cluttered", "heavily cluttered"),
    (r"guaranteed", "guaranteed"),  # keep negations; handled separately
]

PAGE_OVERRIDES = {
    "hot-tub-removal-springfield-mo.html": [
        (
            r'<title>Hot Tub Removal Springfield MO \| Spa Demolition &amp; Hauling</title>',
            '<title>Hot Tub Removal Springfield MO | Spa Removal &amp; Haul-Away</title>',
        ),
        (
            r'content="Hot tub removal in Springfield, MO\. We disconnect, break down, and haul away old hot tubs and spas from decks, patios, and yards\. Call \(417\) 242-5370 for a free quote\."',
            'content="Hot tub removal in Springfield, MO. Request removal for old hot tubs and spas from decks, patios, and yards. Utility disconnect and teardown scope confirmed during the quote process. Call (417) 242-5370."',
        ),
        (
            r'"description": "Hot tub removal in Springfield, MO\. We disconnect, break down, and haul away old hot tubs and spas from decks, patios, and yards\."',
            '"description": "Hot tub removal in Springfield, MO. Request removal for old hot tubs and spas. Utility disconnect and teardown scope are confirmed during the quote process."',
        ),
        (
            r'<h2>Old Spa Taking Up the Backyard\? We\'ll Haul It Off</h2>',
            '<h2>Old Spa Taking Up the Backyard? Request Removal</h2>',
        ),
        (
            r'Springfield Junk Removal\s+Service disconnects, breaks down, and hauls away worn-out hot tubs and spas from decks, patios, and\s+backyards across Springfield, Missouri\. We bring the tools and the muscle so you reclaim your space\.',
            'Springfield Junk Removal Service helps you request removal for worn-out hot tubs and spas from decks, patios, and backyards across Springfield, Missouri. Utility disconnect status, access, and teardown scope are confirmed during the quote process so you can reclaim your space.',
        ),
    ],
    "shed-removal-springfield-mo.html": [
        (
            r'<title>Shed Removal Springfield MO \| Shed Teardown &amp; Hauling</title>',
            '<title>Shed Removal Springfield MO | Shed Removal &amp; Haul-Away</title>',
        ),
        (
            r'content="Shed removal in Springfield, MO\. We tear down and haul away old wood and metal sheds, plus everything stored inside\. Call \(417\) 242-5370 for a free quote\."',
            'content="Shed removal in Springfield, MO. Request removal for old wood and metal sheds and contents. Teardown and haul-away scope confirmed during the quote process. Call (417) 242-5370."',
        ),
        (
            r'"description": "Shed removal in Springfield, MO\. We tear down and haul away old wood and metal sheds, plus everything stored inside\."',
            '"description": "Shed removal in Springfield, MO. Request removal for old sheds and contents. Teardown and haul-away scope are confirmed during the quote process."',
        ),
        (
            r'Springfield Junk Removal Service tears\s+down and hauls away old sheds, plus everything stored inside, for homeowners across Springfield,\s+Missouri\. We handle the demolition and the cleanup so you get your yard back\.',
            'Springfield Junk Removal Service helps you request removal for old sheds and everything stored inside across Springfield, Missouri. Teardown, contents, and haul-away scope are confirmed during the quote process so you can reclaim your yard.',
        ),
        (
            r'<h2>Old Shed Teardown &amp; Haul-Away</h2>',
            '<h2>Old Shed Removal &amp; Haul-Away</h2>',
        ),
    ],
    "hoarder-cleanout-springfield-mo.html": [
        (
            r'offers patient, judgment-free hoarding cleanout help',
            'helps you request patient, judgment-free heavy clutter cleanout support',
        ),
        (
            r'How we help with a cluttered home',
            'How heavy clutter cleanout requests work',
        ),
        (
            r'We work one area at a time',
            'Work can proceed one area at a time',
        ),
        (
            r'We help homeowners, family members, and caregivers',
            'Homeowners, family members, and caregivers across the Springfield area can request help',
        ),
        (
            r'Both are fine\. We keep your situation private',
            'Both are fine. Your situation stays private',
        ),
        (
            r'When people reach out to us',
            'When people request heavy clutter cleanout help',
        ),
    ],
}


def apply_replacements(content: str, filename: str) -> str:
    for pattern, repl in GLOBAL_REPLACEMENTS:
        if pattern == r"guaranteed":
            continue
        content = re.sub(pattern, repl, content)

    if filename in PAGE_OVERRIDES:
        for pattern, repl in PAGE_OVERRIDES[filename]:
            content = re.sub(pattern, repl, content, flags=re.DOTALL)

    # Fix awkward double spaces
    content = re.sub(r'  +', ' ', content)
    return content


def inject_trust(content: str, filename: str, full: bool = False) -> str:
    if 'id="trust-process"' in content:
        return content

    if full or filename in {
        "index.html",
        "junk-removal-springfield-mo.html",
        "junk-removal-services-springfield-mo.html",
        "junk-removal-service-areas-springfield-mo.html",
        "junk-removal-guides-springfield-mo.html",
    }:
        marker = re.search(r'(\s*<section[^>]*>\s*<div class="wrap">\s*<h2>[^<]*FAQ</h2>)', content)
        if marker:
            return content[: marker.start()] + TRUST_FULL + content[marker.start() :]
        return content

    # Compact trust before FAQ on service/city/guide pages
    marker = re.search(
        r'(<section[^>]*>\s*<div class="wrap">\s*<h2>[^<]*FAQ</h2>)', content
    )
    if marker and 'Quote request and confirmation' not in content:
        return content[: marker.start()] + (
            '\n    <section class="light">\n      <div class="wrap">\n'
            + TRUST_COMPACT
            + "\n      </div>\n    </section>\n"
            + content[marker.start() :]
        )
    return content


def add_hub_links(content: str, filename: str) -> str:
    hub_block = """
          <h3>Browse by topic</h3>
          <div class="related-links">
            <a href="junk-removal-services-springfield-mo.html">All Services</a>
            <a href="junk-removal-service-areas-springfield-mo.html">Service Areas</a>
            <a href="junk-removal-guides-springfield-mo.html">Guides &amp; Resources</a>
          </div>"""
    if 'junk-removal-services-springfield-mo.html">All Services' in content:
        return content
    if 'related-links' in content:
        return content.replace(
            '<h3>Helpful guides</h3>',
            hub_block + '\n\n          <h3>Helpful guides</h3>',
            1,
        )
    return content


def main():
    os.chdir(ROOT)
    for path in sorted(glob.glob("*.html")):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = apply_replacements(content, path)
        content = inject_trust(content, path, full=(path == "index.html"))
        content = add_hub_links(content, path)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {path}")


if __name__ == "__main__":
    main()
