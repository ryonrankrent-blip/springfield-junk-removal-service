# Content Brief — Apartment Cleanout Springfield, MO

**Status:** Local draft implemented; QA **PASS**; not committed, pushed, deployed, or indexed
**Date:** 2026-07-22
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
- Deployment: **not deployed**
- Indexing: **not requested**
- Official rules and legal guidance must be reverified before deployment or future material edits.
