# Content Brief — Springfield Junk Disposal & Recycling Guide

**Status:** Deployed through PR #48; live production QA PASS; not submitted for indexing
**Date:** 2026-07-23
**Target file:** `springfield-junk-disposal-guide.html`
**Canonical:** `https://springfieldjunkremovalservice.com/springfield-junk-disposal-guide`

## Purpose

Create the first new linkable authority asset after the priority existing-page upgrades. The guide helps Springfield users research reuse, donation, recycling, drop-off, landfill, and special-material paths while preserving request-and-confirm positioning and directing commercial-intent users to relevant service pages.

## Official sources reverified

| Source | Official URL | Fact or use | Caution |
|---|---|---|---|
| Springfield Waste Wizard | https://www.springfieldmo.gov/5532/Waste-Wizard | Item-specific local research starting point | Current tool controls; do not duplicate a permanent acceptance table |
| Springfield Material Know How | https://www.springfieldmo.gov/5918/Material-Know-How | Landfill restrictions and special-material context | A landfill restriction is not an automatic service acceptance decision |
| Noble Hill Sanitary Landfill | https://www.springfieldmo.gov/486/Noble-Hill-Sanitary-Landfill | Official facility research path | Verify hours, fees, vehicle rules, and acceptance before travel |
| Yardwaste Recycling Center | https://www.springfieldmo.gov/yardwaste | Yard waste, brush, and item-preparation context | Specifications, fees, and limits can change |
| Household Chemical Collection Center | https://www.springfieldmo.gov/5553/Household-Chemical-Collection-Center | Household paint, chemical, battery, oil, and related research | Appointments, residency, quantity, and material rules require direct confirmation |
| Springfield Mattress Recycling | https://www.springfieldmo.gov/5939/Mattress-Recycling | Mattress condition and program research | Do not publish fees or conditions as permanent |
| City Recycling & Donation Locations Guide | https://www.springfieldmo.gov/DocumentCenter/View/15834/Recycling--Donation-Locations-Guide | Broad category and organization research | The guide itself directs users to verify needs, requirements, and fees |
| Missouri DNR — What To Do With Specific Waste | https://dnr.mo.gov/waste-recycling/reduce-reuse-recycle/what-to-do-with-specific | Statewide links for electronics, household hazardous waste, C&D, treated wood, tires, and oil | Link to current official guidance rather than reproduce instructions |
| Missouri DNR — Household Hazardous Waste | https://dnr.mo.gov/waste-recycling/reduce-reuse-recycle/what-to-do-with-specific/household-hazardous | Household paint, chemicals, batteries, bulbs, and related guidance | No hazardous-material handling claim |

## Draft structure

- Springfield-focused hero and verify-before-you-go notice
- Reuse/donation, recycling/drop-off, landfill, household chemical, quote, and specialist paths
- Official city and state resource section
- Furniture, appliances, electronics, mattresses, yard waste, C&D, tires, batteries, oil, paint, chemicals, pesticides, propane, fuel, and unknown-material guidance
- DIY-versus-quote decision section
- Five visible and structured FAQs
- Claim-safe quote form and relevant commercial-intent links

## Internal links added from the new guide

- `/junk-removal-guides-springfield-mo`
- `/what-items-can-be-removed-springfield-mo`
- `/junk-removal-cost-springfield-mo`
- `/how-junk-removal-works-springfield-mo`
- `/junk-removal-springfield-mo`
- `/furniture-removal-springfield-mo`
- `/appliance-removal-springfield-mo`
- `/mattress-removal-springfield-mo`
- `/yard-waste-removal-springfield-mo`
- `/construction-debris-removal-springfield-mo`
- `/commercial-junk-removal-springfield-mo`
- `#quote`

## Guardrails

- No permanent fee, hour, appointment, quantity, or acceptance claims
- No municipal, facility, nonprofit, recycler, or contractor partnership claims
- No guaranteed donation, recycling, pickup, pricing, scheduling, or disposal outcomes
- No hazardous-material, asbestos, refrigerant-recovery, secure-data-destruction, or specialist capability claims
- No facility instructions beyond linking to current official guidance
- Production integration is limited to one guides-hub card, one extensionless sitemap entry, and fixed QA-count updates from 30 to 31
- No unrelated HTML page, navigation, footer, routing, or external system changed

## Production deployment and live verification

- PR #48 merged into `main` at `69ab96fd0e8f367d9e0996315fa1db15ba6caa21` on 2026-07-23.
- Cloudflare Pages production deployment completed successfully through the connected repository workflow.
- The extensionless production URL returned HTTP 200 with no blocking `X-Robots-Tag`.
- Live HTML byte-matched `springfield-junk-disposal-guide.html` at the merge commit (19,791 bytes).
- The guides hub contains one link to the guide, and the live sitemap contains 31 URLs with the guide listed exactly once.
- Title, one H1, canonical, `index, follow`, phone, Formspree, GTM, analytics, form, and `#quote` checks passed.
- Post-merge repository QA passed: 222 checks, 0 failures, 0 warnings; 702 internal links, 0 broken.
- No indexing request or sitemap resubmission has occurred for this guide.

## Next gate

Perform one read-only GSC inspection of the exact extensionless URL after separate approval. Record current index status, crawl/fetch details, user-declared canonical, Google-selected canonical, and referring sitemap before deciding whether one indexing request is appropriate.
