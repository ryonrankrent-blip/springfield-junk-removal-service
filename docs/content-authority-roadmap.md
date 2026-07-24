# Content Authority Roadmap — Springfield

## 2026-07-23 rental-turnover checklist production status

| Field | Value |
|---|---|
| Target file | `rental-turnover-cleanout-checklist-springfield-mo.html` |
| Purpose | Linkable, non-legal checklist for landlords and property managers preparing an authorized turnover |
| Official sources | Missouri Attorney General landlord-tenant resource; Missouri Revised Statutes § 441.065; Springfield Waste Wizard; Material Know How |
| Cluster support | Apartment cleanout, eviction cleanout, commercial junk removal, accepted items, cost, disposal guide |
| Implementation | Complete through PR #53 |
| Deployment | **Complete** — merge commit `04a1748104c1df996b0b737d58252cbd3112cb87` at `2026-07-23T20:46:13Z` |
| Live URL | https://springfieldjunkremovalservice.com/rental-turnover-cleanout-checklist-springfield-mo |
| Live QA | **PASS** — HTTP 200; byte-match; canonical/sitemap/hub/schema/conversion/desktop/mobile/console checks passed |
| Indexing | Not requested |
| Outreach | Not sent; separate recipient-specific approval required after live QA |
| Next gate | Separate approval for one GSC inspection; outreach remains separately gated |

**Status:** Priority authority-page updates and the Springfield disposal/recycling guide are **deployed** with live QA **PASS**; indexing remains separately gated for the new disposal guide
**Date:** 2026-07-11; detailed planning update 2026-07-17; authority-page production updates through 2026-07-23
**Main / deployed accepted-items commit:** `f908715955c779c08689d158f2efaed784688dc3`
**Deployed junk-removal-cost commit:** `502e0876eb78b1deac2e90d0bcae66fec2c8ba9b`
**GSC baseline:** 2026-07-11 (see `indexing-priority-tracker.md`)
**Detailed planning pack:** `content-authority-research-pack.md`

---

## GSC signals driving priority

| Query / theme | GSC signal (Jul 2026) | Existing page | Gap |
|---|---|---|---|
| construction debris removal | Avg position ~**5.9** | `construction-debris-removal-springfield-mo` | Add local disposal rules + landfill ban context |
| commercial junk removal | Avg position ~**15.7** | `commercial-junk-removal-springfield-mo` | Strengthen B2B proof points + internal links |
| yard waste removal services | **1 click**, pos ~**10.0** | `yard-waste-removal-springfield-mo` | Yard-waste ban + city drop-off education |
| junk removal (broad) | 75 imp, pos ~24.2 | Homepage + money page | Authority cluster needed |
| junk removal cost | Not in top signals yet | `junk-removal-cost-springfield-mo` | Expand with local pricing factors (ranges only) |

---

## 2026-07-17 planning deliverables

| File | Purpose |
|---|---|
| `content-authority-research-pack.md` | Existing-content audit, validated source register, keyword map, priority scores, and new-page recommendations |
| `content-brief-construction-debris.md` | Production-ready planning brief for the construction debris page update |
| `content-brief-yard-waste.md` | Production-ready planning brief for the yard waste page update |
| `content-brief-accepted-items.md` | Production-ready planning brief for the accepted/not-accepted items guide update |
| `content-brief-commercial-junk.md` | Production-ready planning brief for the commercial junk removal page update |
| `content-brief-junk-removal-cost.md` | Production-ready planning brief for the cost guide update |
| `internal-link-authority-plan.md` | Proposed internal-link map plus construction-debris/yard-waste/accepted-items deployed link notes |

---

## 2026-07-21 commercial-junk production and GSC status

| Field | Value |
|---|---|
| Target file | `commercial-junk-removal-springfield-mo.html` |
| Live URL | https://springfieldjunkremovalservice.com/commercial-junk-removal-springfield-mo |
| Production deployment | **Complete** — PR #35 merge `388504b2012108f52638fb5b4615a8711ab82aa3` |
| Live QA | **PASS** — HTTP 200; live HTML byte-matched merged file; metadata/schema/links/conversion/mobile/claim-safety/cannibalization checks passed |
| GSC pre-request status | **URL is on Google** / **Page is indexed**; HTTPS passed |
| Last crawl shown | July 4, 2026 at 4:10:14 PM; Googlebot smartphone; crawl allowed; fetch successful; indexing allowed |
| Discovery shown | No referring sitemap or referring page detected in the older crawl snapshot |
| Canonicals shown | User-declared canonical was legacy `.html` in the older crawl snapshot; Google-selected canonical was the inspected extensionless URL; current live canonical and sitemap are extensionless |
| Indexing request | **Submitted successfully once** for the exact extensionless URL — confirmation: Indexing requested / URL added to priority crawl queue |
| Monitoring | Awaiting Google recrawl and refreshed search data; **no additional indexing request or sitemap resubmission should be made now** |
| External systems | No DNS, routing, tracking, forms, CallRail, GTM, GA4, Formspree, citation, listing, outreach, or spending changes |
| Next gate | Monitor GSC recrawl and updated canonical/sitemap reporting; remaining clusters require separate approval |

---

## 2026-07-19 accepted-items production status

| Field | Value |
|---|---|
| Target file | `what-items-can-be-removed-springfield-mo.html` |
| Live URL (canonical) | https://springfieldjunkremovalservice.com/what-items-can-be-removed-springfield-mo |
| Sections changed | Hero, commonly requested groups, Springfield disposal notes, appliances/electronics/yard/construction/mattress/business summaries, accepted/confirm-first/not-standard taxonomy, quote process, local examples, FAQ |
| Official sources reverified | Material Know How, Waste Wizard, HCCC, Mattress Recycling, Missouri DNR HHW; Recycling in Springfield as supporting research |
| Production deployment | **Complete** — Cloudflare Pages success for `f908715` at 2026-07-19T06:34:30Z |
| Live QA | **PASS** — HTTP 200; live HTML byte-matched local; desktop/mobile visual QA passed; metadata/schema/links/conversion/console/claim-safety/cannibalization checks passed; no blocking defects |
| GSC classification | **Non-blocking indexing-URL variance** — not a confirmed indexing request for the canonical extensionless URL |
| GSC submitted URL | https://springfieldjunkremovalservice.com/what-items-can-be-removed-springfield-mo.html |
| GSC live test | URL is available to Google (July 19, 2026 at 6:41 AM) |
| GSC confirmation | Indexing requested / URL added to priority crawl queue (once for `.html` variant only) |
| Redirect verification | `.html` → HTTP 308 → extensionless canonical HTTP 200; no duplicate 200 content; sitemap lists only extensionless URL |
| Monitoring | Do not request either accepted-items URL again now; inspect only the extensionless canonical later (~3–7 days); record user-declared and Google-selected canonical; new request only with fresh inspection + explicit owner approval |
| Future content caveat | Facility rules, fees, hours, appointment slots, accepted items, and disposal requirements still require re-verification before future content changes |
| External systems | No DNS, routing, tracking, forms, CallRail, GTM, GA4, Formspree, citation, listing, outreach, or spending changes |
| Next gate | Monitor GSC crawl settlement for the `.html` request via 308; later inspect extensionless canonical only |

---

## 2026-07-19 yard-waste production status

| Field | Value |
|---|---|
| Target file | `yard-waste-removal-springfield-mo.html` |
| Live URL | https://springfieldjunkremovalservice.com/yard-waste-removal-springfield-mo |
| Sections changed | Hero, service-use cases, Springfield yard-waste disposal context, official resources, accepted/confirm-first/restricted materials, process steps, local examples, CTA copy, FAQ |
| Official sources reverified | City Solid Waste, Yardwaste Recycling Center, Material Know How, Noble Hill, Waste Wizard, Missouri DNR PUB2050 |
| Production deployment | **Complete** — Cloudflare Pages success for `90e7249` at 2026-07-19T06:00:22Z |
| Live QA | **PASS** — HTTP 200; extensionless final URL; live HTML byte-matched local and preview; desktop/mobile visual QA passed; metadata/schema/links/conversion/console/claim-safety checks passed; no blocking defects |
| GSC inspected property | springfieldjunkremovalservice.com |
| GSC pre-request status | URL is on Google |
| Indexing request | **Submitted successfully once** — confirmation: Indexing requested / URL added to priority crawl queue |
| Monitoring | Awaiting Google recrawl and refreshed search data; **no additional indexing request should be made now** |
| Future content caveat | Facility rules, fees, hours, size limits, accepted items, and disposal requirements still require re-verification before future content changes |
| External systems | No DNS, routing, tracking, forms, CallRail, GTM, GA4, Formspree, citation, listing, outreach, or spending changes |
| Next gate | Monitor GSC recrawl/search data; remaining clusters still require separate approval |

---

## 2026-07-18 construction-debris production status

| Field | Value |
|---|---|
| Target file | `construction-debris-removal-springfield-mo.html` |
| Live URL | https://springfieldjunkremovalservice.com/construction-debris-removal-springfield-mo |
| Sections changed | Hero, service-use cases, Springfield disposal context, official resources, accepted/confirm-first/restricted materials, process steps, local examples, CTA copy, FAQ |
| Official sources reverified | City Solid Waste, city C&D PDF, Noble Hill, Material Know How, Waste Wizard, Missouri DNR PUB2045 |
| Production deployment | **Complete** — Cloudflare Pages success for `ca32eca` at 2026-07-18T06:01:28Z |
| Live QA | **PASS** — HTTP 200; live HTML matched deployed commit; desktop/mobile visual QA passed; metadata/schema/links/conversion checks passed; no production defect |
| GSC pre-request status | URL is on Google |
| Indexing request | **Submitted successfully once** — confirmation: Indexing requested / URL added to priority crawl queue |
| Monitoring | Awaiting Google recrawl and refreshed search data; **no additional indexing request should be made now** |
| Future content caveat | Facility rules, fees, hours, accepted items, and disposal requirements still require re-verification before future content changes |
| External systems | No DNS, routing, tracking, forms, CallRail, GTM, GA4, Formspree, citation, listing, outreach, or spending changes |
| Next gate | Monitor GSC recrawl/search data; yard-waste cluster also deployed and indexing requested once on 2026-07-19 |

---

## Proposed content clusters

### Cluster 1 — Construction debris + local disposal rules

| Field | Value |
|---|---|
| **Target query** | construction debris removal springfield mo; construction waste disposal springfield |
| **Search intent** | Commercial / DIY contractor seeking haul-away or dump options |
| **Primary action** | Strengthen existing service page |
| **Supporting internal links** | Debris page ↔ guides hub ↔ `how-junk-removal-works` ↔ commercial page |
| **Local sources required** | [Material Know How](https://www.springfieldmo.gov/5918/Material-Know-How), [Recycle Construction Waste PDF](https://www.springfieldmo.gov/DocumentCenter/View/3099/Recycle-Construction-Waste-PDF), [Noble Hill Landfill](https://www.springfieldmo.gov/486/Noble-Hill-Sanitary-Landfill), Missouri DNR C&D guidance |
| **Reusable template** | **Yes** — swap city/county disposal rules per market |
| **Estimated effort** | 2–3 hours (section additions + source links) |
| **Approval** | **Required** before publish |

### Cluster 2 — Commercial junk removal authority

| Field | Value |
|---|---|
| **Target query** | commercial junk removal springfield mo; office cleanout springfield |
| **Search intent** | Business owner / property manager |
| **Primary action** | Strengthen `commercial-junk-removal-springfield-mo` + cross-link eviction/apartment pages |
| **Supporting internal links** | Commercial ↔ eviction ↔ apartment ↔ services hub |
| **Local sources required** | City Solid Waste, Material Know How, C&D PDF as caution/supporting references |
| **Reusable template** | **Yes** |
| **Estimated effort** | 2 hours |
| **Approval** | **Required** |

### Cluster 3 — Yard waste + landfill ban education

| Field | Value |
|---|---|
| **Target query** | yard waste removal springfield mo; yard waste disposal springfield |
| **Search intent** | Homeowner with branches/bags; may not know landfill ban |
| **Primary action** | Strengthen `yard-waste-removal-springfield-mo` |
| **Supporting internal links** | Yard waste ↔ guides hub ↔ debris page |
| **Local sources required** | [Material Know How — yardwaste ban](https://www.springfieldmo.gov/5918/Material-Know-How), [Yardwaste Recycling Center](https://www.springfieldmo.gov/yardwaste), Missouri DNR yard-waste references |
| **Reusable template** | **Yes** |
| **Estimated effort** | 2 hours |
| **Approval** | **Required** |

### Cluster 4 — Junk removal cost (local factors)

| Field | Value |
|---|---|
| **Target query** | junk removal cost springfield mo; how much junk removal springfield |
| **Search intent** | Price research before calling |
| **Primary action** | Deployed through PR #38: expanded `junk-removal-cost-springfield-mo` with claim-safe local pricing factors and no guaranteed prices |
| **Supporting internal links** | Cost guide ↔ all service pages ↔ quote CTA |
| **Local sources required** | Noble Hill tipping-fee context, Yardwaste Recycling Center fee caution, Mattress Recycling fee caution, Material Know How |
| **Reusable template** | **Yes** |
| **Estimated effort** | 3 hours |
| **Approval** | Deployment complete; one exact extensionless-URL indexing request completed; await Google crawl/index refresh |

## 2026-07-22 junk-removal-cost production and GSC status

| Field | Result |
|---|---|
| Target file | `junk-removal-cost-springfield-mo.html` |
| Live URL | `https://springfieldjunkremovalservice.com/junk-removal-cost-springfield-mo` |
| Deployment | Complete through PR #38 at merge commit `502e0876eb78b1deac2e90d0bcae66fec2c8ba9b` |
| Live QA | **PASS** — HTTP 200, no redirect, live/local byte-match, no blocking defect |
| GSC property | `springfieldjunkremovalservice.com` |
| Pre-request status | **URL is not on Google**; **Page is not indexed: URL is unknown to Google** |
| Discovery | No referring sitemap or referring page detected |
| Crawl/index details | Last crawl, crawler, crawl permission, page fetch, indexing permission, and both canonical fields displayed as `N/A` because Google had not crawled the URL |
| Indexing request | Submitted successfully once for the exact extensionless URL |
| Confirmation | **Indexing requested** — URL added to a priority crawl queue; repeat submissions do not change queue position or priority |
| Monitoring | Await initial crawl, index processing, and refreshed GSC data; do not repeat the request or resubmit the sitemap now |
| External systems | No DNS, routing, tracking, forms, listings, citations, outreach, or spending changes |

### Cluster 5 — Accepted / not accepted items (local rules)

| Field | Value |
|---|---|
| **Target query** | what will junk removal take springfield; items junk removal won't take |
| **Search intent** | Pre-qualification before form/call |
| **Primary action** | Expand `what-items-can-be-removed-springfield-mo` with city banned items + hazmat referral |
| **Supporting internal links** | Items guide ↔ hoarder ↔ hot tub ↔ mattress ↔ guides hub |
| **Local sources required** | Waste Wizard, Material Know How, HCCC, Recycling in Springfield, Mattress Recycling, city recycling/donation guide |
| **Reusable template** | **Yes** |
| **Estimated effort** | 3–4 hours |
| **Approval** | **Required** |

### Cluster 6 — Springfield cleanout guides (property managers)

| Field | Value |
|---|---|
| **Target query** | apartment cleanout springfield mo; eviction cleanout springfield; move out junk springfield |
| **Search intent** | Landlord / PM turnover |
| **Primary action** | Strengthen apartment + eviction pages; optional new "move-out checklist" guide |
| **Supporting internal links** | Apartment ↔ eviction ↔ house cleanout ↔ estate cleanout |
| **Local sources required** | Donation guide PDF; donation centers |
| **Reusable template** | **Yes** |
| **Estimated effort** | 4 hours (if new checklist page) |
| **Approval** | **Required** |

### Cluster 7 — NEW: Springfield disposal & recycling guide (linkable asset)

| Field | Value |
|---|---|
| **Target query** | where to dump junk springfield mo; springfield bulky item disposal |
| **Search intent** | DIY disposal research (may still convert to haul-away) |
| **Primary action** | **Deployed** through PR #48 at merge `69ab96f`; one guides-hub link, extensionless sitemap entry, and 31-page QA counts are live; indexing not requested |
| **Supporting internal links** | Guides hub ↔ all service pages ↔ cost guide |
| **Local sources required** | Full city resource set (see `local-authority-opportunities.md`) |
| **Reusable template** | **Yes** — high-value RankRentOS template |
| **Estimated effort** | Production implementation complete; GSC inspection remains separately gated |
| **Approval** | **Required** before GSC inspection or indexing request |

---

## Priority order (30-day research-backed)

| Priority | Cluster | Why first |
|---|---|---|
| 1 | Construction debris + local rules | Best avg position (~5.9); deployed + live QA PASS + GSC indexing requested once on 2026-07-18; awaiting recrawl |
| 2 | Yard waste + landfill ban | Early click signal; deployed + live QA PASS + GSC indexing requested once on 2026-07-19; awaiting recrawl |
| 3 | Accepted / not accepted items | Supports conversion qualification; **deployed + live QA PASS 2026-07-19**; GSC has non-blocking `.html` indexing-URL variance — canonical extensionless URL not confirmed as requested |
| 4 | Commercial junk | Deployed through PR #35 (`388504b`); live QA PASS; GSC confirmed indexed; one extensionless indexing request submitted 2026-07-21; awaiting recrawl |
| 5 | Junk removal cost | Deployed through PR #38; live QA PASS; one extensionless indexing request submitted 2026-07-22; awaiting initial crawl/index refresh |
| 6 | Apartment and eviction cleanout authority updates | Both deployed, live-QA verified, and submitted once for indexing; supports PM/rental segment |
| 7 | New disposal guide (linkable asset) | Deployed through PR #48 (`69ab96f`); live QA PASS; 31-page sitemap and guides-hub link verified; no indexing request yet |
| 8 | Student move-out donation/disposal checklist | Deployed through PR #62 (`726a454`); live QA PASS; 33-page sitemap and guides-hub link verified; no indexing request or outreach |

---

## What not to publish

- Guaranteed pricing or same-day promises
- Licensed / insured / crew size claims
- Fake local statistics
- Full republication of city PDFs
- Content implying city/chamber endorsement

---

*Construction-debris, yard-waste, commercial, junk-removal-cost, apartment-cleanout, and eviction-cleanout clusters are deployed and indexing was requested once for each. Accepted-items is deployed with a documented indexing-URL variance. Do not repeat indexing requests for these pages now; await crawl/index processing and refreshed search data. Remaining execution steps require separate approval.*

## 2026-07-22–23 apartment-cleanout production status

- Existing `apartment-cleanout-springfield-mo.html` selected as the first property-manager/rental cluster update.
- The deployed update adds authorization, access, tenant/landlord/property-manager, remaining-property, restricted-material, cost, and official-resource guidance.
- No new page or URL was created.
- Deployment completed through PR #42 at merge commit `2b68e6d77252ff76452906d73929c033d2c6ae74`.
- Production verification: **PASS** — extensionless URL returned HTTP 200, live HTML byte-matched `main`, and no blocking defect was found.
- Google Search Console inspection used the exact extensionless production URL.
- Pre-request status: **URL is on Google** and **Page is indexed**.
- Discovery reported no referring sitemap or referring page.
- Last crawl: July 20, 2026 at 1:50:16 AM by Googlebot smartphone.
- Crawl was allowed, page fetch was successful, and indexing was allowed.
- User-declared canonical matched the exact extensionless URL; Google-selected canonical was the inspected URL.
- One indexing request was submitted successfully. Google confirmed **Indexing requested** and added the URL to a priority crawl queue.
- No second request or sitemap resubmission occurred.
- Current gate: await Google recrawl and refreshed search data; do not repeat the request now.

## 2026-07-23 eviction-cleanout production status

- Existing `eviction-cleanout-springfield-mo.html` selected as the second property-manager/rental cluster update.
- Draft adds authority, possession, access, remaining-property, material-disclosure, quote-preparation, and official-source guidance.
- Direct-service, speed, crew, hauling, and one-visit claims were removed.
- No new production URL was created.
- Deployment completed through PR #45 at merge commit `f317e19ba3517db06ff38e76ca6dee6e3d562d5d`.
- Cloudflare Pages deployment succeeded at `2026-07-23T06:11:45Z`.
- Production verification: **PASS** — the extensionless URL returned HTTP 200, live HTML byte-matched the merged file, and no blocking defect was found.
- Canonical, robots, schema, phone, Formspree, GTM, analytics, quote target, desktop/mobile layout, and console checks passed.
- Google Search Console inspection used the exact extensionless production URL.
- Pre-request status: **URL is on Google** and **Page is indexed**.
- Discovery reported no referring sitemap or referring page.
- Last crawl: July 4, 2026 at 3:32:44 PM by Googlebot smartphone.
- Crawl was allowed, page fetch was successful, and indexing was allowed.
- The older crawl reported the user-declared canonical as the legacy `.html` URL; Google selected the inspected extensionless URL as canonical.
- One indexing request was submitted successfully for the exact extensionless URL. Google confirmed **Indexing requested** and added it to a priority crawl queue.
- No second request, other URL submission, or sitemap resubmission occurred; no quota warning or blocker appeared.
- Current gate: await Google recrawl and refreshed canonical/search data; do not repeat the request now.
