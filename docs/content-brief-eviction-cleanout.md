# Content Brief — Eviction Cleanout Springfield, MO

**Status:** Deployed through PR #45; live QA **PASS**; indexing not requested
**Date:** 2026-07-23; production verification 2026-07-23
**Target page:** `eviction-cleanout-springfield-mo.html`

## Purpose

Strengthen the existing eviction-cleanout page for landlords, property managers, and authorized representatives while preserving request-and-confirm positioning. The page must qualify authority, access, materials, timing, and quote details without deciding possession, abandonment, ownership, or legal compliance.

## Official sources reverified

| Source | URL | Fact used | Caution |
|---|---|---|---|
| Missouri Attorney General — Landlord-Tenant Law | https://ago.mo.gov/get-help/programs-services-from-a-z/landlord-tenant-law/ | Missouri publishes landlord/tenant rights-and-responsibilities guidance and states that eviction requires legal process | Informational only; not legal advice |
| Missouri Revised Statutes § 441.060 | https://revisor.mo.gov/main/OneSection.aspx?section=441.060 | Missouri law addresses possession and removal of property after certain judgments and execution procedures | Do not convert statutory language into universal cleanout permission |
| Missouri Revised Statutes § 441.065 | https://revisor.mo.gov/main/OneSection.aspx?section=441.065 | Missouri has a separate procedure that may apply when a landlord believes rental premises were abandoned | Requester must verify every requirement and obtain legal guidance when uncertain |
| Springfield Waste Wizard | https://www.springfieldmo.gov/5532/Waste-Wizard | City tool provides current item-specific reuse, recycling, donation, and disposal options | Facility rules, fees, hours, and acceptance can change |

## Draft implementation

- Replaced unsupported direct-service, speed, crew, hauling, and one-visit claims.
- Added authority-before-cleanout guidance for possession, entry, notices, storage duties, and removal decisions.
- Added commonly described rental-turnover item groups.
- Added property, scope, access, safety, keep-item, and timing details for quote preparation.
- Added confirm-first guidance for heavy, connected, electronic, regulated, contaminated, and unknown materials.
- Added a six-step request-and-confirmation process.
- Strengthened contextual links to apartment, commercial, house-cleanout, furniture, accepted-items, cost, and core junk-removal pages.
- Added four official references with safe external-link attributes.
- Updated metadata, LocalBusiness description, and five matching visible/structured FAQs.

## Claims deliberately avoided

- Legal conclusions about eviction, possession, abandonment, ownership, notice, storage, or disposal authority
- Guaranteed acceptance, pickup, timing, one-visit completion, price, availability, recycling, or disposal outcomes
- Crew, truck, licensing, insurance, experience, or completed-job claims
- City, court, law-enforcement, facility, recycling, or donation partnership claims
- Hazardous-material, biohazard, asbestos, refrigerant, or data-destruction capabilities

## Protected behavior

- Existing filename, extensionless canonical, and `index, follow`
- Phone and `tel:` links
- Formspree action and form fields
- GTM and `analytics-events.js`
- `click_call`, `click_quote_button`, and `submit_lead_form`
- `#quote` target, navigation, footer, and service-area scope

## Status gates

- QA: **PASS** — 216 repository checks, 683 internal links with none broken, clean diff check, exactly one H1, two valid JSON-LD blocks, five visible/structured FAQs matched, protected conversion values preserved, claim-safety scan passed, and desktop/mobile previews showed no horizontal overflow or broken assets.
- Deployment: **complete** through PR #45 at merge commit `f317e19ba3517db06ff38e76ca6dee6e3d562d5d`.
- Cloudflare Pages deployment: **successful** at `2026-07-23T06:11:45Z`.
- Preview artifact: `https://c7b0c3ba.springfield-junk-removal-service.pages.dev`.
- Production URL: `https://springfieldjunkremovalservice.com/eviction-cleanout-springfield-mo`.
- Live verification: **PASS** — HTTP 200, no unintended redirect, and live HTML byte-matched the merged production file.
- Live integrity: updated title and authority section present; exactly one H1; correct extensionless canonical; `index, follow`; valid LocalBusiness and FAQPage JSON-LD; five visible FAQs matched schema.
- Conversion integrity: phone, Formspree, GTM, `analytics-events.js`, form fields, and `#quote` remained intact; no call or form submission was made.
- Visual and console QA: desktop and mobile showed no horizontal overflow or broken assets; no site-attributable console errors were observed.
- Blocking defects: none found.
- Indexing: **not requested**
- Official legal and facility guidance must be reverified before deployment or future material edits.
