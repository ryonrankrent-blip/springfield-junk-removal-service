# Content Brief — Springfield Student Move-Out Donation & Disposal Checklist

**Status:** Deployed through PR #62; live production QA passed; one exact extensionless-URL indexing request submitted; not used for outreach
**Date:** 2026-07-24
**Target file:** `springfield-student-move-out-donation-disposal-checklist.html`
**Canonical:** `https://springfieldjunkremovalservice.com/springfield-student-move-out-donation-disposal-checklist`

## Purpose

Create a neutral, source-led move-out checklist for Springfield students, families, residence-hall occupants, and renters. Campus, property, lease, donation, and official disposal rules remain primary. Commercial junk-removal information is secondary and uses request-and-confirm language.

## Research score

| Dimension | Score | Reason |
|---|---:|---|
| Local usefulness | 9/10 | Addresses current donation-station exclusions and off-campus decision gaps |
| Editorial-link potential | 8/10 | Natural fit for student, campus, storage, and rental resources |
| Search/conversion support | 7/10 | Long-tail intent plus contextual routes to disposal and cleanout pages |
| Claim safety | 9/10 | Neutral checklist with explicit non-affiliation and time-sensitive caveats |
| Reusability | 8/10 | Adaptable to college markets with local campus and city sources |
| Overall | **8.2/10** | Recommended next linkable asset |

## Official and primary sources

| Source | URL | Use | Caution |
|---|---|---|---|
| Missouri State Residence Life — 2026 end-of-semester and donation stations | https://blogs.missouristate.edu/bearsfamilies/2026/04/11/residence-life-housing-and-dining-end-of-the-semester-summer-school-donation-stations-new-bears/ | Dated example of checkout planning, donation-station categories, and excluded bulky items | Semester dates, partners, locations, and accepted items are not permanent |
| Missouri State Recycling FAQ | https://www.missouristate.edu/Sustainability/RecyclingFAQ.htm | Campus recycling rules, home-generated-material limits, and Springfield resource referral | Campus procedures change and do not apply automatically off campus |
| Springfield Waste Wizard | https://www.springfieldmo.gov/5532/Waste-Wizard | Item-specific local research | Link to the current tool instead of duplicating its database |
| Springfield Material Know How | https://www.springfieldmo.gov/5918/Material-Know-How | Local landfill restrictions and material guidance | Does not determine service acceptance |
| City Recycling & Donation Locations Guide | https://www.springfieldmo.gov/DocumentCenter/View/15834/Recycling--Donation-Locations-Guide | Local organization research | Verify each organization directly |
| Missouri DNR specific-waste guidance | https://dnr.mo.gov/waste-recycling/reduce-reuse-recycle/what-to-do-with-specific | Statewide item paths | No specialist handling claim |

## Page structure

- Campus/property-rules-first hero and dated-program warning
- Six-step move-out checklist
- Donate, store, take home, sell, research, or quote decision cards
- Missouri State 2026 donation-station context and explicit non-affiliation
- Furniture, mattresses, electronics, appliances, chemicals, and unknown-material planning
- Official Springfield and Missouri research links
- Five visible FAQs matching FAQPage JSON-LD
- Claim-safe quote form

## Production integration

- One new HTML page
- One guides-hub card
- One extensionless sitemap entry
- QA inventory counts updated from 32 to 33
- No service-page, global navigation, footer, routing, tracking, or external-system change

## Deployment and live verification

- PR: `#62`
- Source commit: `6d2d662e19b0d4524737b508c61a23778fe912f6`
- Production merge commit: `726a4544be9b2e3f56168c53a5d0472c2a7c59a0`
- Cloudflare Pages check: deployed successfully
- Live verification: `2026-07-24T13:55:02Z`
- Production URL returned HTTP 200 with no fallback content.
- Live HTML byte-matched `springfield-student-move-out-donation-disposal-checklist.html`.
- The exact extensionless canonical, title, H1, phone, Formspree endpoint, GTM container, and analytics script were present.
- The live guides hub linked to the checklist.
- The live sitemap contained exactly 33 extensionless URLs, including the checklist.
- `robots.txt` allowed search crawling and referenced the production sitemap.
- Browser review confirmed the checklist, decision cards, official-source links, quote form, FAQs, navigation, and footer rendered with the intended content.
- No blocking production defect was found.

## Guardrails

- No Missouri State, Bear Pantry, Love in Action, storage, nonprofit, facility, or government affiliation claim
- No permanent semester date, donation-program, acceptance, fee, hour, or location claim
- No guaranteed donation, storage, pickup, pricing, scheduling, availability, recycling, or disposal result
- No secure-data-destruction, hazardous-material, asbestos, refrigerant-recovery, or specialist capability claim
- No outreach until the asset is deployed, live-QA verified, and separately approved

## Google Search Console status

- Property: `springfieldjunkremovalservice.com`
- Inspected URL: `https://springfieldjunkremovalservice.com/springfield-student-move-out-donation-disposal-checklist`
- Pre-request result: **URL is not on Google**.
- Page-indexing result: **Page is not indexed: URL is unknown to Google**.
- Discovery reported no referring sitemap or referring page.
- Last crawl, crawler, crawl permission, page fetch, indexing permission, user-declared canonical, and Google-selected canonical displayed as `N/A` because Google had not crawled the URL.
- After separate owner approval, one indexing request was submitted for the exact extensionless URL.
- Confirmation heading: **Indexing requested**.
- Confirmation message: “URL was added to a priority crawl queue. Submitting a page multiple times will not change its queue position or priority.”
- No second request, other URL inspection or submission, sitemap resubmission, quota warning, or blocker occurred.

## Next gate

Allow Google to crawl and process the request. Reinspect the exact extensionless URL only after a reasonable monitoring interval; do not repeat the indexing request or resubmit the sitemap now.
