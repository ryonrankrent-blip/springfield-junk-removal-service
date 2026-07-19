# Content Authority Roadmap — Springfield

**Status:** Research recommendations + detailed briefs complete; construction-debris page deployed/indexed once; yard-waste local draft implemented — **not deployed**
**Date:** 2026-07-11; detailed planning update 2026-07-17; construction-debris deploy/indexing + yard-waste draft update 2026-07-18
**Main commit:** `5f3286d1b51c7af7ac8576b013b929f4efd966ab`
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
| `internal-link-authority-plan.md` | Proposed internal-link map plus construction-debris deployed and yard-waste draft link notes |

---

## 2026-07-18 yard-waste draft status

| Field | Value |
|---|---|
| Target file | `yard-waste-removal-springfield-mo.html` |
| Draft scope | Local file edit and QA only |
| Sections changed | Hero, service-use cases, Springfield yard-waste disposal context, official resources, accepted/confirm-first/restricted materials, process steps, local examples, CTA copy, FAQ |
| Official sources reverified | City Solid Waste, Yardwaste Recycling Center, Material Know How, Noble Hill, Waste Wizard, Missouri DNR PUB2050 |
| Production deployment | **Not deployed** |
| Indexing request | **Not requested** |
| Commit/push | **Not performed** |
| Next gate | Owner approval required before commit, branch, PR, deploy, or indexing |

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
| Next gate | Monitor GSC recrawl/search data; yard-waste implementation remains separately approved |

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
| **Primary action** | Expand `junk-removal-cost-springfield-mo` with factor-based ranges (no guaranteed prices) |
| **Supporting internal links** | Cost guide ↔ all service pages ↔ quote CTA |
| **Local sources required** | Noble Hill tipping-fee context, Yardwaste Recycling Center fee caution, Mattress Recycling fee caution, Material Know How |
| **Reusable template** | **Yes** |
| **Estimated effort** | 3 hours |
| **Approval** | **Required** |

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
| **Primary action** | **New guide page** (not drafted) |
| **Supporting internal links** | Guides hub ↔ all service pages ↔ cost guide |
| **Local sources required** | Full city resource set (see `local-authority-opportunities.md`) |
| **Reusable template** | **Yes** — high-value RankRentOS template |
| **Estimated effort** | 6–8 hours |
| **Approval** | **Required** |

---

## Priority order (30-day research-backed)

| Priority | Cluster | Why first |
|---|---|---|
| 1 | Construction debris + local rules | Best avg position (~5.9); deployed + live QA PASS + GSC indexing requested once on 2026-07-18; awaiting recrawl |
| 2 | Yard waste + landfill ban | Early click signal; local draft implemented 2026-07-18, not deployed |
| 3 | Accepted / not accepted items | Supports conversion qualification |
| 4 | Commercial junk | Position ~15.7 with room to improve |
| 5 | Junk removal cost | Existing guide; supports quote intent |
| 6 | Cleanout guides | Supports PM/rental segment |
| 7 | New disposal guide (linkable asset) | First new-page candidate after priority existing-page updates |

---

## What not to publish

- Guaranteed pricing or same-day promises
- Licensed / insured / crew size claims
- Fake local statistics
- Full republication of city PDFs
- Content implying city/chamber endorsement

---

*Construction-debris cluster is deployed and indexing was requested once. Yard-waste local draft is implemented but not deployed. Remaining clusters still require separate approval before production edits. Do not request construction-debris indexing again; monitor Google recrawl results.*
