# Indexing Priority Tracker — Springfield

**Site:** https://springfieldjunkremovalservice.com  
**Sitemap file:** https://springfieldjunkremovalservice.com/sitemap.xml  
**Production merge:** `2006f8b` (PR #11, 2026-07-11)  
**Status:** Planning only — **do not submit indexing requests without separate approval**

## Canonical URL rule for GSC inspection

Use **extensionless** URLs as the final canonical destination for all non-homepage pages:

| Production behavior | Value |
|---|---|
| `.html` URL request | **308** redirect |
| Extensionless URL | **200** (final canonical) |
| Homepage | `https://springfieldjunkremovalservice.com/` (no redirect) |

**Inspect and record GSC status against the Canonical URL column below — not the `.html` sitemap loc.**

---

## Sitemap / canonical alignment note

**Branch prepared (not deployed):** `cursor/springfield-sitemap-canonical-alignment`

| State | Detail |
|---|---|
| **Before (production)** | `sitemap.xml` listed 29 `.html` locs that 308-redirected to extensionless URLs |
| **Correction (branch)** | `sitemap.xml`, canonical tags, `og:url`, JSON-LD page URLs, and internal navigation aligned to extensionless locs matching live 200 destinations |
| **Deployment** | **Not yet deployed** — prepared on branch only |
| **Local source files** | HTML filenames remain `*.html` on disk |
| **QA** | `link-check.sh` maps extensionless internal paths to local `*.html` files |

---

## Tier definitions

| Tier | Intent | GSC action when approved |
|---|---|---|
| **Tier 1** | Homepage, hubs, money page, top commercial intent | Inspect extensionless canonical URL → request indexing only after separate approval |
| **Tier 2** | High-intent services, guides, top geo pages | Inspect after Tier 1 stabilizes |
| **Tier 3** | Specialty long-tail + secondary geo | Inspect after Tier 2 |

## GSC status legend

Leave blank until manual inspection: `Indexed` / `Discovered` / `Crawled` / `Not indexed` / `Error`

---

## Tier 1 — Index first

| Canonical URL (inspect this) | Sitemap loc | Live status | Internal links (local) | Priority | Reason | GSC status |
|---|---|---:|---:|---|---|---|
| https://springfieldjunkremovalservice.com/ | `/` | 200 | 67 | Tier 1 | Brand + nav hub; highest link equity | |
| https://springfieldjunkremovalservice.com/junk-removal-springfield-mo | Aligned | 200 | 38 | Tier 1 | Primary money page | |
| https://springfieldjunkremovalservice.com/junk-removal-services-springfield-mo | Aligned | 200 | 29 | Tier 1 | New services hub; crawl discovery | |
| https://springfieldjunkremovalservice.com/junk-removal-service-areas-springfield-mo | Aligned | 200 | 21 | Tier 1 | New geo hub | |
| https://springfieldjunkremovalservice.com/junk-removal-guides-springfield-mo | Aligned | 200 | 18 | Tier 1 | New guides hub | |
| https://springfieldjunkremovalservice.com/furniture-removal-springfield-mo | Aligned | 200 | 9 | Tier 1 | Core high-volume service | |
| https://springfieldjunkremovalservice.com/appliance-removal-springfield-mo | Aligned | 200 | 9 | Tier 1 | Core high-volume service | |
| https://springfieldjunkremovalservice.com/house-cleanout-springfield-mo | Aligned | 200 | 17 | Tier 1 | High-intent cleanout | |
| https://springfieldjunkremovalservice.com/estate-cleanout-springfield-mo | Aligned | 200 | 17 | Tier 1 | High-intent cleanout | |
| https://springfieldjunkremovalservice.com/commercial-junk-removal-springfield-mo | Aligned | 200 | 20 | Tier 1 | Commercial buyer intent | |

---

## Tier 2 — Index second

| Canonical URL (inspect this) | Sitemap loc | Live status | Internal links (local) | Priority | Reason | GSC status |
|---|---|---:|---:|---|---|---|
| https://springfieldjunkremovalservice.com/garage-cleanout-springfield-mo | Aligned | 200 | 17 | Tier 2 | Strong cleanout intent | |
| https://springfieldjunkremovalservice.com/mattress-removal-springfield-mo | Aligned | 200 | 9 | Tier 2 | Single-item long-tail | |
| https://springfieldjunkremovalservice.com/couch-removal-springfield-mo | Aligned | 200 | 9 | Tier 2 | Single-item long-tail | |
| https://springfieldjunkremovalservice.com/construction-debris-removal-springfield-mo | Aligned | 200 | 9 | Tier 2 | Contractor / renovation intent | |
| https://springfieldjunkremovalservice.com/yard-waste-removal-springfield-mo | Aligned | 200 | 9 | Tier 2 | Seasonal outdoor intent | |
| https://springfieldjunkremovalservice.com/same-day-junk-removal-springfield-mo | Aligned | 200 | 9 | Tier 2 | Urgency intent; claim-safe FAQ | |
| https://springfieldjunkremovalservice.com/junk-removal-cost-springfield-mo | Aligned | 200 | 30 | Tier 2 | Research / BOFU guide | |
| https://springfieldjunkremovalservice.com/what-items-can-be-removed-springfield-mo | Aligned | 200 | 25 | Tier 2 | Research / acceptance guide | |
| https://springfieldjunkremovalservice.com/how-junk-removal-works-springfield-mo | Aligned | 200 | 30 | Tier 2 | Process / trust guide | |
| https://springfieldjunkremovalservice.com/junk-removal-nixa-mo | Aligned | 200 | 15 | Tier 2 | Top satellite city | |
| https://springfieldjunkremovalservice.com/junk-removal-ozark-mo | Aligned | 200 | 15 | Tier 2 | Top satellite city | |
| https://springfieldjunkremovalservice.com/junk-removal-republic-mo | Aligned | 200 | 15 | Tier 2 | Top satellite city | |

---

## Tier 3 — Index third

| Canonical URL (inspect this) | Sitemap loc | Live status | Internal links (local) | Priority | Reason | GSC status |
|---|---|---:|---:|---|---|---|
| https://springfieldjunkremovalservice.com/trash-removal-springfield-mo | Aligned | 200 | 9 | Tier 3 | Specialty service | |
| https://springfieldjunkremovalservice.com/hot-tub-removal-springfield-mo | Aligned | 200 | 9 | Tier 3 | Specialty; scope confirmation | |
| https://springfieldjunkremovalservice.com/shed-removal-springfield-mo | Aligned | 200 | 9 | Tier 3 | Specialty; teardown scope | |
| https://springfieldjunkremovalservice.com/apartment-cleanout-springfield-mo | Aligned | 200 | 9 | Tier 3 | Property-manager niche | |
| https://springfieldjunkremovalservice.com/eviction-cleanout-springfield-mo | Aligned | 200 | 20 | Tier 3 | Landlord niche | |
| https://springfieldjunkremovalservice.com/hoarder-cleanout-springfield-mo | Aligned | 200 | 20 | Tier 3 | Heavy clutter; URL retained | |
| https://springfieldjunkremovalservice.com/junk-removal-battlefield-mo | Aligned | 200 | 15 | Tier 3 | Secondary geo | |
| https://springfieldjunkremovalservice.com/junk-removal-willard-mo | Aligned | 200 | 15 | Tier 3 | Secondary geo | |

*On branch `cursor/springfield-sitemap-canonical-alignment`, sitemap locs match extensionless canonical URLs (prepared, not deployed).*

---

## GSC workflow (existing property — do not create new)

Search Console is **already set up** for Springfield. Do not create a new property or submit anything in this batch.

- [ ] Verify the existing Search Console property for `springfieldjunkremovalservice.com`
- [ ] Confirm current sitemap submission status (read-only — do not resubmit without approval)
- [ ] Capture current **Page Indexing** baseline (indexed / not indexed counts)
- [ ] Manually inspect **Tier 1 extensionless canonical URLs** (10 URLs in table above)
- [ ] Record status: indexed / not indexed / discovered / crawled
- [ ] Monitor coverage for redirect/canonical warnings related to `.html` sitemap locs
- [ ] Monitor impressions for `junk removal springfield mo` and related terms
- [ ] Request indexing **only after separate approval**

---

## Title / H1 reference (live production)

| Page | Title | H1 |
|---|---|---|
| Homepage | Junk Removal Springfield MO \| Local Junk Hauling & Cleanouts | Junk Removal in Springfield, MO |
| Services hub | Junk Removal Services Springfield MO \| Service Directory | Junk Removal Services in Springfield, MO |
| Service areas hub | Junk Removal Service Areas Springfield MO \| Greene County | Junk Removal Service Areas |
| Guides hub | Junk Removal Guides Springfield MO \| Resources & Tips | Junk Removal Guides & Resources |
| Money page | Junk Removal Springfield MO \| Junk Removal Requests | Junk Removal in Springfield, MO |
| Hoarder | Hoarder Cleanout Springfield MO \| Compassionate Junk Removal | Hoarder Cleanout in Springfield, MO |

*Full title/H1 list for all 30 pages recorded in `production-baseline-2026-07-11.md` verification run.*

---

## Recommended next action (documentation batch)

1. Commit the corrected documentation batch
2. Verify the existing GSC property and current sitemap status
3. Capture GSC baseline data
4. Manually inspect Tier 1 extensionless canonical URLs
5. Prepare, but do not execute, a sitemap canonical-alignment correction — **prepared on branch `cursor/springfield-sitemap-canonical-alignment`, not deployed**
6. Request separate approval for live conversion tests and indexing requests
