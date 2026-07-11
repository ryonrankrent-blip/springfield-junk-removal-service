# Indexing Priority Tracker — Springfield

**Site:** https://springfieldjunkremovalservice.com  
**Sitemap file:** https://springfieldjunkremovalservice.com/sitemap.xml  
**Production merge:** `ef037f3` (PR #13 hub JSON-LD fix; PR #12 `57b7b8c` URL alignment)  
**GSC baseline captured:** 2026-07-11  
**Recheck window:** July 18–25, 2026  
**Status:** Tier 1 baseline complete; eight indexing requests submitted 2026-07-11 — **no additional requests without separate approval**

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

**Deployed (PR #12, merge `57b7b8c`, 2026-07-11):**

| State | Detail |
|---|---|
| **Before (`2006f8b`)** | `sitemap.xml` listed 29 `.html` locs that 308-redirected to extensionless URLs |
| **After (`57b7b8c`)** | `sitemap.xml`, canonical tags, `og:url`, JSON-LD page URLs, and internal navigation aligned to extensionless URLs |
| **Live sitemap (verified)** | 30 unique extensionless locs; 0 `.html` locs |
| **Local source files** | HTML filenames remain `*.html` on disk |
| **QA** | `link-check.sh` maps extensionless internal paths to local `*.html` files |

---

## GSC baseline capture — 2026-07-11

**Phase:** Baseline captured + Tier 1 URL inspection + approved indexing requests (eight URLs)

### Property verification

| Field | Status | Notes |
|---|---|---|
| Property | `springfieldjunkremovalservice.com` | **Existing verified domain property** — no new property created |
| Property type | **Domain property** | DNS TXT `google-site-verification` on apex domain |
| Verification | **Verified** | Confirmed in GSC 2026-07-11 |

### Sitemap status (GSC dashboard — verified 2026-07-11)

| Field | Live production | GSC submitted sitemap |
|---|---|---|
| Sitemap URL | `https://springfieldjunkremovalservice.com/sitemap.xml` | Same |
| Loc count | **30** extensionless | **30 discovered pages** |
| `.html` locs | **0** | Extensionless URLs |
| Last read | — | **July 11, 2026** |
| Status | — | **Success** |

**Do not resubmit sitemap without separate approval.**

### Performance baseline (verified 2026-07-11)

| Range | Impressions | Clicks | CTR | Avg position |
|---|---:|---:|---:|---:|
| Last 28 days | 4.64K | 6 | 0.1% | 41.4 |
| Last 7 days | 1.47K | 2 | 0.1% | 40.9 |

**Notable query signals (7-day view unless noted):**

| Query | Signal |
|---|---|
| construction debris removal | Avg position ~5.9 |
| commercial junk removal | Avg position ~15.7 |
| yard waste removal services | 1 click, position 10.0 |
| junk removal | 75 impressions, position 24.2 |

### Page Indexing baseline (verified 2026-07-11)

| Metric | Value |
|---|---|
| Indexed pages | **37** |
| Not indexed pages | **35** |
| Page with redirect | **14** |
| Alternate page with proper canonical | **9** |
| Redirect error | **8** |
| Crawled – currently not indexed | **3** |
| Discovered – currently not indexed | **1** |

**Redirect-error note:** Example URLs are legacy `.html` paths last crawled **before** the July 11 canonical-alignment deployment (PR #12). Recheck after Google recrawl — **not an active production defect**.

### Hub JSON-LD issue (resolved PR #13)

| Item | Detail |
|---|---|
| Original issue | Three hub pages showed **unparsable structured data** (double-brace `{{` / `}}` in LocalBusiness JSON-LD) |
| Fix | PR #13 (`42c704d` → merge `ef037f3`, 2026-07-11) |
| Live verification | Production HTML parses; 57/57 JSON-LD blocks valid |
| Indexing | Requests submitted successfully for all three hubs after fix |

### Prior qualitative GSC signal (June 2026, pre-PR #11)

Homepage authority pass referenced early GSC data showing impressions for garage-cleanout terms and page-2 positions for buyer-intent queries. Superseded by verified July 11 baseline above.

---

## Tier definitions

| Tier | Intent | GSC action when approved |
|---|---|---|
| **Tier 1** | Homepage, hubs, money page, top commercial intent | Inspect extensionless canonical URL → request indexing only after separate approval |
| **Tier 2** | High-intent services, guides, top geo pages | Inspect after Tier 1 stabilizes |
| **Tier 3** | Specialty long-tail + secondary geo | Inspect after Tier 2 |

## GSC status legend

`Indexed` / `Indexing requested` / `Discovered` / `Crawled` / `Not indexed` / `Error`

---

## Tier 1 — Index first

| Canonical URL (inspect this) | Sitemap loc | Live status | GSC status (2026-07-11) | Last crawl | Google canonical | Next action |
|---|---|---:|---|---|---|---|
| https://springfieldjunkremovalservice.com/ | `/` | 200 | **Indexed** | — | — | Monitor; no request needed |
| https://springfieldjunkremovalservice.com/junk-removal-springfield-mo | Aligned | 200 | **Indexed** | — | — | Monitor; no request needed |
| https://springfieldjunkremovalservice.com/junk-removal-services-springfield-mo | Aligned | 200 | **Indexing requested** | — | — | Recheck July 18–25; JSON-LD fixed PR #13 |
| https://springfieldjunkremovalservice.com/junk-removal-service-areas-springfield-mo | Aligned | 200 | **Indexing requested** | — | — | Recheck July 18–25; JSON-LD fixed PR #13 |
| https://springfieldjunkremovalservice.com/junk-removal-guides-springfield-mo | Aligned | 200 | **Indexing requested** | — | — | Recheck July 18–25; JSON-LD fixed PR #13 |
| https://springfieldjunkremovalservice.com/furniture-removal-springfield-mo | Aligned | 200 | **Indexed** | — | — | Monitor; no request needed |
| https://springfieldjunkremovalservice.com/appliance-removal-springfield-mo | Aligned | 200 | **Indexing requested** | — | — | Recheck July 18–25 |
| https://springfieldjunkremovalservice.com/house-cleanout-springfield-mo | Aligned | 200 | **Indexing requested** | — | — | Recheck July 18–25 |
| https://springfieldjunkremovalservice.com/estate-cleanout-springfield-mo | Aligned | 200 | **Indexing requested** | — | — | Recheck July 18–25 |
| https://springfieldjunkremovalservice.com/commercial-junk-removal-springfield-mo | Aligned | 200 | **Indexed** | — | — | Monitor; no request needed |

---

## Tier 2 — Index second

| Canonical URL (inspect this) | Sitemap loc | Live status | Internal links (local) | Priority | Reason | GSC status |
|---|---|---:|---:|---|---|---|
| https://springfieldjunkremovalservice.com/garage-cleanout-springfield-mo | Aligned | 200 | 17 | Tier 2 | Strong cleanout intent | |
| https://springfieldjunkremovalservice.com/mattress-removal-springfield-mo | Aligned | 200 | 9 | Tier 2 | Single-item long-tail | |
| https://springfieldjunkremovalservice.com/couch-removal-springfield-mo | Aligned | 200 | 9 | Tier 2 | Single-item long-tail | |
| https://springfieldjunkremovalservice.com/construction-debris-removal-springfield-mo | Aligned | 200 | 9 | Tier 2 | Contractor / renovation intent | **Indexing requested** (2026-07-11) |
| https://springfieldjunkremovalservice.com/yard-waste-removal-springfield-mo | Aligned | 200 | 9 | Tier 2 | Seasonal outdoor intent | **Indexing requested** (2026-07-11) |
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

*Production sitemap locs match extensionless canonical URLs (deployed PR #12, `57b7b8c`).*

---

## GSC workflow (existing property — do not create new)

Search Console property for `springfieldjunkremovalservice.com` is **verified** (domain property). Baseline captured 2026-07-11.

- [x] Confirm DNS `google-site-verification` TXT on apex domain
- [x] Verify existing Search Console property for `springfieldjunkremovalservice.com`
- [x] Confirm sitemap submission status — Success, 30 discovered, read July 11, 2026
- [x] Capture Page Indexing baseline (37 indexed / 35 not indexed)
- [x] Capture Performance baseline (28-day + 7-day)
- [x] Inspect Tier 1 extensionless canonical URLs (10 URLs)
- [x] Record status: indexed / indexing requested
- [x] Fix hub JSON-LD unparsable structured data (PR #13) and verify live
- [x] Submit indexing requests for eight approved URLs (2026-07-11)
- [ ] Recheck indexing status — **July 18–25, 2026**
- [ ] Monitor coverage for redirect/canonical warnings (legacy `.html` redirect errors expected to clear on recrawl)
- [ ] Monitor impressions for `junk removal springfield mo` and related terms
- [ ] Request additional indexing **only after separate approval**

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

## Recommended next action

1. Recheck GSC indexing status for eight requested URLs — **July 18–25, 2026**
2. Monitor redirect-error coverage as legacy `.html` URLs recrawl post-PR #12
3. Record week-2 metrics in `proof-of-life-weekly-tracker.md`
4. **Pending approval:** live conversion tests (call/form/GTM preview)
5. **Pending approval:** citations/listings and authority work
6. **Do not:** resubmit sitemap, create new GSC property, or submit additional indexing requests without approval
