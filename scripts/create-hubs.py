#!/usr/bin/env python3
"""Generate Springfield hub pages with claim-safe copy.

REUSABLE GENERATOR — overwrites hub HTML files from a template. Do not run against
production without reviewing output. Update PAGES/SERVICES_GRID constants per market.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STYLE = open(os.path.join(ROOT, "mattress-removal-springfield-mo.html"), encoding="utf-8").read()
STYLE = STYLE[STYLE.find("<style>") : STYLE.find("</style>") + 8]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-GDJF54DV');</script>
  <!-- End Google Tag Manager -->

  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://springfieldjunkremovalservice.com/{canonical}" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="https://springfieldjunkremovalservice.com/{canonical}" />
  <meta property="og:locale" content="en_US" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  <meta name="theme-color" content="#111827" />

{style}

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Springfield Junk Removal Service",
    "url": "https://springfieldjunkremovalservice.com/{canonical}",
    "telephone": "+1-417-242-5370",
    "description": "{schema_desc}",
    "areaServed": {{
      "@type": "City",
      "name": "Springfield",
      "containedInPlace": {{
        "@type": "State",
        "name": "Missouri"
      }}
    }},
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "Springfield",
      "addressRegion": "MO",
      "addressCountry": "US"
    }}
  }}
  </script>
</head>
"""

TRUST = """
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
              <li>Items or project type</li>
              <li>Approximate volume and access details</li>
              <li>Location and preferred timing</li>
              <li>Photos when helpful</li>
            </ul>
          </div>
          <div class="card">
            <h3>Requiring confirmation</h3>
            <ul>
              <li>Hot tubs, sheds, and large structures</li>
              <li>Appliance utility disconnect status</li>
              <li>Heavy clutter cleanouts</li>
              <li>Hazardous or special-disposal items</li>
            </ul>
          </div>
          <div class="card">
            <h3>Service area</h3>
            <ul>
              <li>Springfield and Greene County</li>
              <li>Nixa, Ozark, Republic, Battlefield, Willard</li>
              <li>Same-day or next-day when scheduling allows</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
"""

FORM = """
        <div class="quote-box" id="quote">
          <h2>Get a Free Quote</h2>
          <p>Describe what you need removed and quote details are provided after your request is reviewed.</p>
          <p>Prefer to talk now? Call <a href="tel:4172425370">(417) 242-5370</a>.</p>
          <form action="https://formspree.io/f/mojzdkvg" method="POST">
            <input type="hidden" name="site" value="springfieldjunkremovalservice.com" />
            <input type="hidden" name="market" value="Springfield, MO" />
            <input type="hidden" name="niche" value="Junk Removal" />
            <input type="hidden" name="service" value="{service}" />
            <input type="text" name="name" placeholder="Your name" required />
            <input type="tel" name="phone" placeholder="Phone number" required />
            <input type="email" name="email" placeholder="Email address" />
            <textarea name="message" rows="5" placeholder="Describe the junk, location, and timing" required></textarea>
            <button type="submit">Request Free Quote</button>
          </form>
        </div>
"""

FOOTER = """
  <footer>
    <p>Springfield Junk Removal Service | {footer_line}</p>
    <p>Phone: <a href="tel:4172425370">(417) 242-5370</a></p>
    <p><a href="index.html">Back to Home</a> | <a href="junk-removal-services-springfield-mo.html">Services</a> | <a href="junk-removal-service-areas-springfield-mo.html">Service Areas</a> | <a href="junk-removal-guides-springfield-mo.html">Guides</a></p>
  </footer>
  <script src="analytics-events.js"></script>
</body>
</html>
"""


def build_page(meta, breadcrumb, h1, hero, sections_html, service):
    body_start = f"""<body>
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-GDJF54DV"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <header>
    <div class="wrap">
      <div class="logo"><a href="index.html">Springfield Junk Removal Service</a></div>
      <div class="phone">Call: <a href="tel:4172425370">(417) 242-5370</a></div>
    </div>
  </header>
  <nav class="breadcrumb">
    <a href="index.html">Home</a> &rsaquo; {breadcrumb}
  </nav>
  <main>
    <section class="hero">
      <div class="wrap">
        <h1>{h1}</h1>
        <p>{hero}</p>
        <div class="cta-row">
          <a class="button" href="tel:4172425370">Call (417) 242-5370</a>
          <a class="button secondary" href="#quote">Get a Free Quote</a>
        </div>
      </div>
    </section>
{sections_html}
{TRUST}
    <section class="light">
      <div class="wrap two-col">
        <div>
          <h3>Browse other hubs</h3>
          <div class="related-links">
            <a href="junk-removal-services-springfield-mo.html">All Services</a>
            <a href="junk-removal-service-areas-springfield-mo.html">Service Areas</a>
            <a href="junk-removal-guides-springfield-mo.html">Guides &amp; Resources</a>
            <a href="junk-removal-springfield-mo.html">Junk Removal in Springfield</a>
          </div>
        </div>
{FORM.replace("{service}", service)}
      </div>
    </section>
  </main>
"""
    head = HEAD.replace("{style}", STYLE)
    head = head.replace("{title}", meta["title"])
    head = head.replace("{description}", meta["description"])
    head = head.replace("{canonical}", meta["canonical"])
    head = head.replace("{schema_desc}", meta["schema_desc"])
    return head + body_start + FOOTER.replace("{footer_line}", meta["footer_line"]).replace("{service}", service)


SERVICES_GRID = """
    <section>
      <div class="wrap">
        <h2>Core Junk Removal Services</h2>
        <div class="grid">
          <div class="card"><h3><a href="junk-removal-springfield-mo.html">Junk Removal</a></h3><p>General junk removal requests for homes and businesses.</p></div>
          <div class="card"><h3><a href="furniture-removal-springfield-mo.html">Furniture Removal</a></h3><p>Couches, dressers, tables, and bulky household items.</p></div>
          <div class="card"><h3><a href="appliance-removal-springfield-mo.html">Appliance Removal</a></h3><p>Refrigerators, washers, dryers, and large appliances.</p></div>
          <div class="card"><h3><a href="garage-cleanout-springfield-mo.html">Garage Cleanouts</a></h3><p>Clutter, tools, shelving, and stored junk.</p></div>
          <div class="card"><h3><a href="yard-waste-removal-springfield-mo.html">Yard Waste Removal</a></h3><p>Brush, branches, and non-hazardous yard debris.</p></div>
          <div class="card"><h3><a href="construction-debris-removal-springfield-mo.html">Construction Debris</a></h3><p>Remodeling and renovation debris.</p></div>
        </div>
        <h2>Cleanouts &amp; Hauling</h2>
        <div class="grid">
          <div class="card"><h3><a href="trash-removal-springfield-mo.html">Trash Removal</a></h3><p>Bulk trash and bagged garbage pickup requests.</p></div>
          <div class="card"><h3><a href="house-cleanout-springfield-mo.html">House Cleanouts</a></h3><p>Whole-home and room-by-room cleanout requests.</p></div>
          <div class="card"><h3><a href="estate-cleanout-springfield-mo.html">Estate Cleanouts</a></h3><p>Property clearing after a loss or downsizing.</p></div>
          <div class="card"><h3><a href="same-day-junk-removal-springfield-mo.html">Same-Day Junk Removal</a></h3><p>Faster timing when scheduling allows.</p></div>
        </div>
        <h2>Specialty Removal</h2>
        <div class="grid">
          <div class="card"><h3><a href="hot-tub-removal-springfield-mo.html">Hot Tub Removal</a></h3><p>Spa removal — scope confirmed during quote.</p></div>
          <div class="card"><h3><a href="shed-removal-springfield-mo.html">Shed Removal</a></h3><p>Shed and contents — teardown scope confirmed.</p></div>
          <div class="card"><h3><a href="mattress-removal-springfield-mo.html">Mattress Removal</a></h3><p>Mattresses and box springs.</p></div>
          <div class="card"><h3><a href="couch-removal-springfield-mo.html">Couch Removal</a></h3><p>Sofas, sectionals, and recliners.</p></div>
          <div class="card"><h3><a href="apartment-cleanout-springfield-mo.html">Apartment Cleanouts</a></h3><p>Unit and turnover cleanouts.</p></div>
          <div class="card"><h3><a href="eviction-cleanout-springfield-mo.html">Eviction Cleanouts</a></h3><p>Rental property clearing requests.</p></div>
          <div class="card"><h3><a href="hoarder-cleanout-springfield-mo.html">Heavy Clutter Cleanouts</a></h3><p>Patient heavy clutter cleanout requests.</p></div>
          <div class="card"><h3><a href="commercial-junk-removal-springfield-mo.html">Commercial Junk Removal</a></h3><p>Office and business junk removal requests.</p></div>
        </div>
      </div>
    </section>
"""

AREAS_GRID = """
    <section>
      <div class="wrap">
        <h2>Springfield &amp; Greene County</h2>
        <p>Service requests are accepted for Springfield, MO and nearby Greene County communities. Your request can be reviewed for availability in your area.</p>
        <div class="grid">
          <div class="card"><h3><a href="junk-removal-springfield-mo.html">Springfield, MO</a></h3><p>Primary service area for junk removal requests.</p></div>
          <div class="card"><h3><a href="junk-removal-nixa-mo.html">Nixa, MO</a></h3><p>Junk removal requests south of Springfield.</p></div>
          <div class="card"><h3><a href="junk-removal-ozark-mo.html">Ozark, MO</a></h3><p>Residential and rental junk removal requests.</p></div>
          <div class="card"><h3><a href="junk-removal-republic-mo.html">Republic, MO</a></h3><p>West of Springfield in Greene County.</p></div>
          <div class="card"><h3><a href="junk-removal-battlefield-mo.html">Battlefield, MO</a></h3><p>Southwest Springfield metro coverage.</p></div>
          <div class="card"><h3><a href="junk-removal-willard-mo.html">Willard, MO</a></h3><p>Northwest Greene County requests.</p></div>
        </div>
        <h2>Popular services by area</h2>
        <div class="related-links">
          <a href="furniture-removal-springfield-mo.html">Furniture Removal</a>
          <a href="garage-cleanout-springfield-mo.html">Garage Cleanouts</a>
          <a href="house-cleanout-springfield-mo.html">House Cleanouts</a>
          <a href="commercial-junk-removal-springfield-mo.html">Commercial Junk Removal</a>
        </div>
      </div>
    </section>
"""

GUIDES_GRID = """
    <section>
      <div class="wrap">
        <h2>Junk Removal Guides</h2>
        <div class="grid">
          <div class="card"><h3><a href="junk-removal-cost-springfield-mo.html">Junk Removal Cost</a></h3><p>What affects pricing and why quotes are itemized.</p></div>
          <div class="card"><h3><a href="what-items-can-be-removed-springfield-mo.html">What Can Be Removed</a></h3><p>Common accepted items and materials requiring confirmation.</p></div>
          <div class="card"><h3><a href="how-junk-removal-works-springfield-mo.html">How Junk Removal Works</a></h3><p>From quote request to pickup day.</p></div>
        </div>
        <h2>Ready to request service?</h2>
        <p>These guides pair with high-intent service pages when you are ready to send a request.</p>
        <div class="related-links">
          <a href="junk-removal-springfield-mo.html">Junk Removal Springfield</a>
          <a href="commercial-junk-removal-springfield-mo.html">Commercial Junk Removal</a>
          <a href="house-cleanout-springfield-mo.html">House Cleanouts</a>
          <a href="garage-cleanout-springfield-mo.html">Garage Cleanouts</a>
        </div>
      </div>
    </section>
"""

PAGES = [
    {
        "file": "junk-removal-services-springfield-mo.html",
        "title": "Junk Removal Services Springfield MO | Service Directory",
        "description": "Browse junk removal services in Springfield, MO. Furniture, cleanouts, debris, specialty removal, and commercial requests. Call (417) 242-5370.",
        "schema_desc": "Directory of junk removal services in Springfield, MO for quote requests.",
        "footer_line": "Junk Removal Services in Springfield, MO",
        "breadcrumb": "Junk Removal Services",
        "h1": "Junk Removal Services in Springfield, MO",
        "hero": "Browse junk removal and cleanout services available for quote requests in Springfield, Missouri. Pickup scope and accepted items are confirmed during the quote process. Call <a href=\"tel:4172425370\">(417) 242-5370</a> or request a quote online.",
        "sections": SERVICES_GRID,
        "service": "Services Hub",
    },
    {
        "file": "junk-removal-service-areas-springfield-mo.html",
        "title": "Junk Removal Service Areas Springfield MO | Greene County",
        "description": "Junk removal service areas in Springfield, MO and nearby Greene County cities. Your request can be reviewed for availability. Call (417) 242-5370.",
        "schema_desc": "Junk removal service areas in Springfield, MO and Greene County communities.",
        "footer_line": "Junk Removal Service Areas",
        "breadcrumb": "Service Areas",
        "h1": "Junk Removal Service Areas",
        "hero": "Service requests are accepted for Springfield and nearby Greene County communities. Your request can be reviewed for availability in your area. Call <a href=\"tel:4172425370\">(417) 242-5370</a> or send a quote request.",
        "sections": AREAS_GRID,
        "service": "Service Areas Hub",
    },
    {
        "file": "junk-removal-guides-springfield-mo.html",
        "title": "Junk Removal Guides Springfield MO | Resources &amp; Tips",
        "description": "Junk removal guides for Springfield, MO — cost, accepted items, and how the quote process works. Call (417) 242-5370 to request service.",
        "schema_desc": "Junk removal guides and resources for Springfield, MO homeowners and businesses.",
        "footer_line": "Junk Removal Guides &amp; Resources",
        "breadcrumb": "Guides &amp; Resources",
        "h1": "Junk Removal Guides &amp; Resources",
        "hero": "Research pricing, accepted items, and the quote request process before you send a junk removal request in Springfield, Missouri. Call <a href=\"tel:4172425370\">(417) 242-5370</a> when you are ready.",
        "sections": GUIDES_GRID,
        "service": "Guides Hub",
    },
]


def main():
    os.chdir(ROOT)
    for p in PAGES:
        meta = {k: p[k] for k in ("title", "description", "schema_desc", "footer_line")}
        meta["canonical"] = p["file"]
        html = build_page(meta, p["breadcrumb"], p["h1"], p["hero"], p["sections"], p["service"])
        with open(p["file"], "w", encoding="utf-8") as f:
            f.write(html)
        print("Created", p["file"])


if __name__ == "__main__":
    main()
