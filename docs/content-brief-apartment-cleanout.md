# Content Brief — Apartment Cleanout Springfield, MO

**Status:** Deployed through PR #42; live QA **PASS**; one extensionless-URL indexing request submitted successfully
**Date:** 2026-07-22; production verification 2026-07-23
**Target page:** `apartment-cleanout-springfield-mo.html`

## Purpose

Strengthen the existing apartment-cleanout page for tenants, landlords, and property managers while preserving request-and-confirm positioning. The page must qualify authorization, access, materials, and scheduling without deciding ownership or providing legal advice.

## Official sources reverified

| Source | URL | Fact used | Caution |
|---|---|---|---|
| Missouri Attorney General — Landlord Tenant Law | https://ago.mo.gov/get-help/programs-services-from-a-z/landlord-tenant-law/ | Missouri publishes landlord/tenant rights-and-responsibilities guidance | Informational only; not a substitute for legal advice |
| Missouri Revised Statutes § 441.065 | https://revisor.mo.gov/main/OneSection.aspx?section=441.065 | Missouri has a defined procedure that may apply when a landlord believes rental premises were abandoned | Do not summarize as universal permission to remove property; requester must confirm compliance |
| Springfield Waste Wizard | https://www.springfieldmo.gov/5532/Waste-Wizard | City tool helps users research item-specific reuse, recycling, donation, and disposal options | Organizations, rules, fees, hours, and acceptance can change |
| Springfield Recycling & Donation Locations Guide | https://www.springfieldmo.gov/DocumentCenter/View/15834/Recycling--Donation-Locations-Guide | City guide instructs users to verify material needs, requirements, and fees before visiting | Research support only; page links to Waste Wizard as the more current lookup tool |

## Draft implementation

- Rewrote broken and unsupported operator copy.
- Added tenant, landlord, property-manager, move-out, and rental-turnover use cases.
- Added authorization and remaining-property safeguards without legal advice.
- Added access planning for stairs, elevators, gates, parking, loading areas, and carrying distance.
- Added confirm-first guidance for appliances, electronics, heavy items, chemicals, biohazards, asbestos-related material, and unknown items.
- Added contextual links to eviction, commercial, accepted-items, cost, furniture, mattress, house-cleanout, and core junk-removal pages.
- Added three purposeful official links with safe external-link attributes.
- Updated metadata, LocalBusiness description, and five matching visible/structured FAQs.

## Claims deliberately avoided

- Guaranteed pickup, timing, one-visit completion, acceptance, price, recycling, or donation outcome
- Crew, truck, licensing, insurance, experience, or completed-job claims
- Legal conclusions about abandonment, ownership, notice, court orders, or authority
- City, facility, recycling, or donation partnership claims
- Hazardous-material, biohazard, asbestos, or refrigerant-handling claims

## Protected behavior

- Canonical URL and `index, follow`
- Phone and `tel:` links
- Formspree action and fields
- GTM and `analytics-events.js`
- `click_call`, `click_quote_button`, and `submit_lead_form`
- `#quote` target, navigation, footer, and service-area scope

## Status gates

- QA: **PASS** — 216 repository checks, 691 internal links with none broken, clean diff check, valid JSON-LD, five visible/structured FAQs matched, protected conversion values preserved, and desktop/mobile overflow checks passed.
- Deployment: **complete** through PR #42 at merge commit `2b68e6d77252ff76452906d73929c033d2c6ae74`.
- Production URL: `https://springfieldjunkremovalservice.com/apartment-cleanout-springfield-mo`.
- Live verification: **PASS** at `2026-07-23T05:45:11Z` — HTTP 200, live HTML byte-matched `main`, updated title and authorization section were present, and canonical, robots, phone, Formspree, GTM, analytics, and quote target remained correct.
- Blocking defects: none found.
- Google Search Console property: `springfieldjunkremovalservice.com`
- Inspected URL: `https://springfieldjunkremovalservice.com/apartment-cleanout-springfield-mo`
- Pre-request status: **URL is on Google** and **Page is indexed**
- Discovery: no referring sitemap or referring page detected
- Last crawl: July 20, 2026 at 1:50:16 AM by Googlebot smartphone
- Crawl allowed: **Yes**
- Page fetch: **Successful**
- Indexing allowed: **Yes**
- User-declared canonical: exact extensionless inspected URL
- Google-selected canonical: **Inspected URL**
- Indexing request: submitted successfully once
- Confirmation: **Indexing requested** — URL added to a priority crawl queue
- No second request or sitemap resubmission occurred
- Monitoring: await Google recrawl and refreshed search data; do not repeat the request now
- Official rules and legal guidance must be reverified before deployment or future material edits.
