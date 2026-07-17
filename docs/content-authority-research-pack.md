# Content Authority Research Pack — Springfield

**Status:** Research and planning only — **no production content edited or published**
**Date:** 2026-07-17
**Main commit reviewed:** `ddfd4191b26347187dc34516c6a4a6b4a396e5d5`
**Scope:** Content-authority source validation, existing-content audit, keyword map, priority scoring, and implementation planning

## Guardrails

- No HTML, JavaScript, sitemap, DNS, tracking, routing, form, call-handling, listing, credential, or production files changed.
- No indexing requests submitted.
- No listings created, claimed, edited, submitted, or verified.
- No outreach, business contact, organization contact, payment, commit, push, or deploy performed.
- Recommendations below require approval before any production edit.

## Current Authority Context

| Area | Current state |
|---|---|
| Brownbook | Live and claimed |
| Bing Places | Creation review complete; creation deferred |
| Yelp | Creation review complete; creation deferred |
| ShowMeLocal | Creation review complete; creation deferred |
| GBP | Blocked / not eligible now |
| Site readiness | Technically lead-ready; production content unchanged in this task |
| GSC baseline | 2026-07-11: 4.64K impressions / 6 clicks over 28 days; priority query signals documented in `indexing-priority-tracker.md` |

## Existing-Content Audit

| Cluster | Existing target page | Related supporting pages | Current title | Current H1 | Intent | Gaps | Cannibalization risk | Recommendation |
|---|---|---|---|---|---|---|---|---|
| Construction debris removal and Springfield disposal rules | `construction-debris-removal-springfield-mo.html` | `junk-removal-springfield-mo.html`, `trash-removal-springfield-mo.html`, `garage-cleanout-springfield-mo.html`, `house-cleanout-springfield-mo.html`, `yard-waste-removal-springfield-mo.html`, `junk-removal-cost-springfield-mo.html`, `what-items-can-be-removed-springfield-mo.html`, `how-junk-removal-works-springfield-mo.html` | Construction Debris Removal Springfield MO \| Renovation Cleanup | Construction Debris Removal in Springfield, MO | Homeowner/contractor wants renovation debris hauled or wants to understand disposal options | Needs local C&D rules, clean-fill distinction, landfill accepted/non-accepted framing, reuse/donation options, asbestos caution, and source-backed FAQ | Medium: overlaps with `trash-removal`, `yard-waste`, and `what-items`; keep page focused on renovation/construction debris and link to accepted-items for broader item rules | **Update existing page first** |
| Yard waste removal and local disposal restrictions | `yard-waste-removal-springfield-mo.html` | `construction-debris-removal-springfield-mo.html`, `garage-cleanout-springfield-mo.html`, `junk-removal-cost-springfield-mo.html`, `what-items-can-be-removed-springfield-mo.html`, `how-junk-removal-works-springfield-mo.html` | Yard Waste Removal Springfield MO \| Brush & Yard Debris Hauling | Yard Waste Removal in Springfield, MO | Homeowner has brush, leaves, branches, lawn bags, or outdoor cleanup debris | Needs Missouri landfill ban, Springfield Yardwaste Recycling Center rules, brush size restrictions, bag/container removal notes, fee caution, and prohibited materials | Medium: construction vegetation can overlap; keep yard page focused on organic yard waste and refer construction debris to debris page | **Update existing page second** |
| Accepted and not accepted items | `what-items-can-be-removed-springfield-mo.html` | `junk-removal-cost-springfield-mo.html`, `how-junk-removal-works-springfield-mo.html`, all major service pages, `yard-waste-removal-springfield-mo.html`, `construction-debris-removal-springfield-mo.html`, `appliance-removal-springfield-mo.html`, `mattress-removal-springfield-mo.html`, `hoarder-cleanout-springfield-mo.html` | What Items Can Be Removed? \| Junk Removal Springfield, MO | What Items Can Be Removed in Springfield, MO? | Pre-call qualification for what haulers may take and what needs special handling | Needs clearer accepted/not-accepted table, city banned-items references, HCCC referral, Waste Wizard referral, appliance/mattress special paths, and cautious "confirm before pickup" language | High: could compete with individual service pages if expanded too broadly; use concise category summaries and link out to service pages | **Update existing page; do not create duplicate accepted-items guide** |
| Commercial junk removal | `commercial-junk-removal-springfield-mo.html` | `construction-debris-removal-springfield-mo.html`, `apartment-cleanout-springfield-mo.html`, `eviction-cleanout-springfield-mo.html`, `house-cleanout-springfield-mo.html`, `junk-removal-cost-springfield-mo.html`, `what-items-can-be-removed-springfield-mo.html`, `how-junk-removal-works-springfield-mo.html` | Commercial Junk Removal Springfield MO \| Office & Business Hauling | Commercial Junk Removal in Springfield, MO | Business, landlord, property manager, retail/office operator needs low-disruption hauling | Needs B2B segment examples, landlord/property-manager paths, construction crossover, quote-prep checklist, disposal-compliance caveats, and stronger internal links | Low-medium: overlaps with apartment/eviction cleanout pages; keep commercial page as B2B hub and link to vertical pages | **Update existing page after debris/yard/items** |
| Springfield junk removal cost guide | `junk-removal-cost-springfield-mo.html` | `junk-removal-springfield-mo.html`, all major service pages, `what-items-can-be-removed-springfield-mo.html`, `how-junk-removal-works-springfield-mo.html`, `yard-waste-removal-springfield-mo.html`, `construction-debris-removal-springfield-mo.html`, `commercial-junk-removal-springfield-mo.html` | Junk Removal Cost in Springfield, MO \| What Affects Pricing | Junk Removal Cost in Springfield, MO | Price researcher comparing DIY disposal, hauling factors, and quote expectations | Needs local disposal-fee context, prohibited-item cost caveats, quote-factor table, no-guaranteed-price guardrails, and service-specific cost drivers | Medium-high: cost modifiers touch all services; preserve cost page as central guide and link service pages to it | **Update existing page; no new cost page** |
| Broader disposal/recycling guide | No existing page | Guides hub, items guide, debris page, yard waste page, cost guide, service hub | N/A | N/A | Informational DIY disposal research that may convert to haul-away | Would consolidate city facilities, Waste Wizard, HCCC, YRC, Noble Hill, recycling/donation paths, and banned-item notes | Medium: must not replace service pages; position as "Springfield disposal resources" linkable asset | **First new page candidate, defer until existing priority pages are improved** |

## Validated Local Sources

| Source name | Official URL | Relevant fact | Last updated visible? | Page where fact could be used | Cautious wording needed? | Outbound citation recommended? |
|---|---|---|---|---|---|---|
| City of Springfield Solid Waste Management & Recycling | https://www.springfieldmo.gov/2331/Solid-Waste-Management-Recycling | Springfield's solid-waste system includes Noble Hill Sanitary Landfill, recycling drop-off sites, Yardwaste Recycling Center, Household Chemical Collection Center, and education/market programs; curbside trash/recycling is provided by private independent haulers. | Not visible in fetched page | Disposal guide, cost guide, items guide | Yes: avoid implying city partnership or city-provided junk removal | Yes |
| City Waste Wizard | https://www.springfieldmo.gov/5532/Waste-Wizard | City tool helps residents search item-specific repurpose, reuse, recycle, and disposal options. | Not visible | Accepted-items guide, disposal guide, yard waste, construction debris | Yes: use as referral, not as a substitute for live confirmation | Yes |
| City Material Know How | https://www.springfieldmo.gov/5918/Material-Know-How | Lists landfill-banned items including explosives, hazardous wastes, flammables, infectious waste, lead-acid batteries, liquids, major appliances, PCB's, asbestos, septic tank pumpings, whole tires, waste oil, and yardwaste; clean fill may include uncontaminated soil, sand, gravel, concrete, cinder blocks, asphalt, and brick subject to staff verification. | Not visible | Accepted-items, construction debris, yard waste, cost guide | Yes: item acceptance can depend on condition, contamination, facility review, and current rules | Yes |
| Noble Hill Sanitary Landfill | https://www.springfieldmo.gov/486/Noble-Hill-Sanitary-Landfill | Landfill accepts municipal solid waste and non-hazardous materials; published tipping fee is $43.85/ton with $20 minimum; customer guidelines require secured loads and staff direction. | Fee note references July 1 increase; page date not visible | Cost guide, construction debris, disposal guide | Yes: fees/hours can change; use "published" or "as listed by the city" language and verify before publishing | Yes |
| Recycling in Springfield | https://www.springfieldmo.gov/5550/Recycling-in-Springfield | City recycling facilities accept household recyclables, yardwaste, household chemicals, and mattresses through specific facilities; recycling is generally free but donations/fees may apply; mattress recycling has a linked program. | Not visible | Accepted-items, yard waste, cost guide, disposal guide | Yes: facility-specific accepted items, hours, and fees can change | Yes |
| Yardwaste Recycling Center | https://www.springfieldmo.gov/yardwaste | YRC accepts yardwaste, leaves, brush, sticks, organic holiday decor; yardwaste facility requires materials free of rocks/lumber/limbs/trash and removed from bags/containers; brush has size limits and fee schedule. | Not visible | Yard waste, construction debris, accepted-items, disposal guide | Yes: brush size, fees, and facility rules need current verification before publish | Yes |
| Household Chemical Collection Center | https://www.springfieldmo.gov/5553/Household-Chemical-Collection-Center | HCCC accepts household hazardous/toxic/flammable materials by appointment only and serves Greene, Christian, Polk, Dallas, and Webster county residents. | Not visible | Accepted-items, hoarder cleanout, disposal guide | Yes: service should not claim hazmat pickup; refer residents to official resource | Yes |
| Mattress Recycling | https://www.springfieldmo.gov/5939/Mattress-Recycling | Mattress recycling is offered at City facilities for a set per-piece fee; items must be clean, dry, and free of infestation. | Not visible | Accepted-items, mattress page, cost guide | Yes: fee and condition rules can change; verify before publish | Yes |
| City Recycle Construction Waste PDF | https://www.springfieldmo.gov/DocumentCenter/View/3099/Recycle-Construction-Waste-PDF | C&D guidance encourages planning, source separation, donation/reuse, clean-fill classification, and proper landfill disposal for unsalvageable materials; asbestos caution applies to older buildings. | Not visible | Construction debris, commercial, disposal guide | Yes: do not copy long PDF text; summarize and cite | Yes |
| City Recycling & Donation Locations Guide | https://www.springfieldmo.gov/DocumentCenter/View/15834/Recycling--Donation-Locations-Guide | Guide directs users to verify needs, fees, and accepted materials before visiting; Waste Wizard is identified as the most current recycling/donation database. | Not visible | Accepted-items, disposal guide, cleanout pages | Yes: organizations and acceptance rules change frequently | Yes |
| Missouri DNR Managing Construction and Demolition Waste | https://oembed-dnr.mo.gov/document-search/managing-construction-demolition-waste-pub2045/pub2045 | Clean fill excludes roofing shingles, sheet rock, lumber, and other C&D waste beyond minimal wood/metal; generator responsibility and contamination concerns matter. | Search result references 07/27/2022 for the fact sheet in one mirror; official page date not visible in fetched result | Construction debris, accepted-items | Yes: state guidance is technical; simplify carefully and cite | Optional; useful for authority |
| Missouri DNR Special Waste / Yard Waste references | https://dnr.mo.gov/document-search/special-waste-pub2050/pub2050 | Missouri landfill exclusions include yard waste, tires, lead-acid batteries, waste oil, major appliances, hazardous waste, bulk liquids, flammables, explosives, infectious waste, and more. | Not visible | Yard waste, accepted-items, disposal guide | Yes: state and facility language differs; cite city source first | Optional |

## Search-Intent and Keyword Map

| Page/update | Primary query | Secondary queries | User intent | Local modifier | Conversion role | GSC signal | Content type | Suggested title tag | Suggested H1 | Proposed URL | Effort | Future-market reuse |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Update construction debris page | construction debris removal springfield mo | construction waste disposal springfield mo; renovation debris hauling springfield; drywall removal springfield mo; clean fill springfield mo | Hire haul-away or understand legal disposal after renovation | Springfield MO, Greene County | High-intent service page with authority sections | Avg position ~5.9 | Service page expansion | Construction Debris Removal Springfield MO \| Disposal Rules & Hauling | Construction Debris Removal in Springfield, MO | `/construction-debris-removal-springfield-mo` | Medium | High |
| Update yard waste page | yard waste removal springfield mo | brush removal springfield mo; yard debris hauling springfield; where to take yard waste springfield mo | Dispose of branches, leaves, brush, outdoor organic debris | Springfield MO | Seasonal service page and education | 1 click, pos ~10.0 for yard waste removal services | Service page expansion | Yard Waste Removal Springfield MO \| Brush, Leaves & Local Rules | Yard Waste Removal in Springfield, MO | `/yard-waste-removal-springfield-mo` | Medium | High |
| Update accepted-items guide | what items can junk removal take springfield mo | junk removal accepted items; items junk haulers won't take; hazardous waste disposal springfield mo | Pre-qualify items and avoid surprises before quote | Springfield MO | Conversion qualifier and trust builder | Tier 2 guide; no direct query signal documented | Guide update | What Items Can Junk Removal Take in Springfield, MO? | What Items Can Be Removed in Springfield, MO? | `/what-items-can-be-removed-springfield-mo` | Medium-high | High |
| Update commercial page | commercial junk removal springfield mo | office junk removal springfield; business cleanout springfield mo; retail cleanout springfield; property cleanout springfield | Business/PM wants low-disruption pickup and quote | Springfield MO | B2B lead page | Avg position ~15.7 | Service page expansion | Commercial Junk Removal Springfield MO \| Office & Business Cleanouts | Commercial Junk Removal in Springfield, MO | `/commercial-junk-removal-springfield-mo` | Medium | High |
| Update cost guide | junk removal cost springfield mo | junk removal prices springfield mo; how much does junk removal cost; furniture removal cost springfield; disposal fees springfield mo | Price research before requesting quote | Springfield MO | Bottom-funnel guide that warms leads | Not top signal yet; existing Tier 2 guide with 30 internal links | Cost guide update | Junk Removal Cost Springfield MO \| Pricing Factors & Local Fees | Junk Removal Cost in Springfield, MO | `/junk-removal-cost-springfield-mo` | Medium-high | High |
| New disposal guide | where to dump junk springfield mo | springfield bulky item disposal; springfield recycling and donation; waste wizard springfield mo | DIY disposal research; may convert if effort is too high | Springfield MO, Greene County | Linkable asset and informational capture | Broad "junk removal" 75 impressions, pos ~24.2 | New guide page | Springfield Junk Disposal Guide \| Recycling, Landfill & Donation Options | Springfield Junk Disposal & Recycling Guide | `/springfield-junk-disposal-guide` | High | Very high |

## Priority Scores

Scores are 1-5 where 5 is best. For implementation effort, 5 means easier/lower effort.

| Opportunity | Ranking ease | GSC evidence | Commercial value | Local-authority value | Implementation effort | Repeatability | Total /30 | Recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Construction debris page update | 5 | 5 | 4 | 5 | 4 | 5 | **28** | First page to update |
| Yard waste page update | 4 | 4 | 3 | 5 | 4 | 5 | **25** | Second page to update |
| Accepted-items guide update | 4 | 3 | 4 | 5 | 3 | 5 | **24** | Third update; supports all service pages |
| Commercial junk page update | 3 | 4 | 5 | 3 | 4 | 5 | **24** | Fourth update; B2B value |
| Cost guide update | 3 | 2 | 5 | 4 | 3 | 5 | **22** | Fifth update; quote-intent support |
| New Springfield disposal guide | 3 | 3 | 3 | 5 | 2 | 5 | **21** | First new page candidate after existing updates |

## Recommended Implementation Order

1. **First page to update:** `construction-debris-removal-springfield-mo.html`
2. **Second page to update:** `yard-waste-removal-springfield-mo.html`
3. **First new page to create, if approved later:** `/springfield-junk-disposal-guide`
4. **Defer:** Any new cost page, duplicate accepted-items page, outreach-driven linkable assets, sitemap/indexing requests, citation/listing actions, and any page that requires current operator claims not yet verified.

## New-Page Recommendations

| Proposed new page | Decision | Reason |
|---|---|---|
| `/springfield-junk-disposal-guide` | Recommend later, after top two updates | Strong local-authority/linkable asset; can consolidate official resource links without diluting service-page intent |
| Separate construction disposal guide | Defer | Existing construction debris page already ranks and should be strengthened first |
| Separate yard-waste disposal guide | Defer | Existing yard-waste service page has click/position signal and should absorb the rule-focused content first |
| Separate accepted/not-accepted page | Reject duplicate | Existing guide already targets this intent |
| Separate cost page or pricing table page | Reject duplicate | Existing cost guide should remain canonical |

## Unresolved Questions and Risks

- City facility hours, fees, accepted items, and Waste Wizard recommendations can change; verify again immediately before production edits.
- Avoid claims that the service accepts hazardous waste, asbestos, infectious waste, liquids, whole tires, major appliances requiring special handling, or landfill-banned material without operator confirmation.
- Avoid implying city endorsement, city partnership, or guaranteed disposal path.
- Avoid guaranteed pricing, same-day availability, licensed/insured claims, crew-size claims, or exact service capacity claims unless separately verified.
- Current operator/renter model remains unresolved; content should stay request-and-confirm oriented.
- GSC data is from the documented July 11 baseline only; no new GSC pull or indexing request was performed.

## Related Briefs

- `content-brief-construction-debris.md`
- `content-brief-yard-waste.md`
- `content-brief-accepted-items.md`
- `content-brief-commercial-junk.md`
- `content-brief-junk-removal-cost.md`
- `internal-link-authority-plan.md`

*Research only. Stop for approval before implementation.*
