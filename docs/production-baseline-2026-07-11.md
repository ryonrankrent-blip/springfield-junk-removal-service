# Springfield Production Baseline — 2026-07-11

| Field | Value |
|---|---|
| **Site** | springfieldjunkremovalservice.com |
| **Production URL** | https://springfieldjunkremovalservice.com |
| **PR** | #11 |
| **Merge commit** | `2006f8bc8baff01a9c8c050be72e893d07473ccf` |
| **Branch merged** | `cursor/springfield-homepage-authority-pass` → `main` |
| **Deployment date** | 2026-07-11 |
| **Host** | Cloudflare Pages |
| **Deployment status** | Success on merge commit `2006f8b` |
| **Phase** | Post-deploy → indexing + tracking verification |

---

## 1. Executive snapshot

Springfield Junk Removal Service is live in production with 30 HTML pages, claim-safe copy, hub IA, QA scripts, and RankRentOS documentation. Pre-merge QA: **216 passed, 0 failed**. Internal links: **691 checked, 0 broken**.

No DNS, CallRail, Formspree, GTM, GA4, citation, listing, or renter outreach changes were made as part of this deploy.

---

## 2. Live technical baseline

| Check | Result | Notes |
|---|---|---|
| Homepage HTTP status | **200** | `/` |
| Sitemap URLs | **30/30** | All return 200 after redirect follow |
| `robots.txt` | **200** | Contains `Sitemap:` directive |
| `sitemap.xml` | **200** | 30 `<url>` entries |
| Canonical domain | **OK** | Base domain consistent; see sitemap/canonical alignment note below |
| Phone `tel:4172425370` | **OK** | Present on all HTML pages |
| Formspree `mojzdkvg` | **OK** | Present on all form pages |
| GTM `GTM-GDJF54DV` | **OK** | Present on all HTML pages |
| `analytics-events.js` | **OK** | Present on all HTML pages |
| Mobile viewport | **OK** | `<meta name="viewport">` on all pages |
| H1 count | **OK** | Exactly 1 H1 per page |
| Internal links (local) | **OK** | 691 links, 0 broken |
| Schema types | **OK** | `LocalBusiness` all pages; `FAQPage` on pages with FAQ |

### Schema types observed

- **All pages:** `LocalBusiness`, `PostalAddress`, `City`, `State`
- **FAQ pages:** `FAQPage`, `Question`, `Answer` (homepage, money page, service pages, guides, cities)

---

## 3. Sitemap / canonical alignment (non-blocking, recommended cleanup)

### Production routing (verified live)

Cloudflare serves **308 permanent redirects** from `.html` paths to extensionless URLs.

| Pattern | Example |
|---|---|
| `.html` request | `/junk-removal-springfield-mo.html` → **308** |
| Final canonical URL | `/junk-removal-springfield-mo` → **200** |
| Homepage | `/` → **200** (no redirect) |

### Current mismatch (production baseline)

| Source | State on production (`2006f8b`) |
|---|---|
| `sitemap.xml` | Listed **29 `.html` URLs** + homepage `/` |
| Live routing | `.html` → **308** → extensionless **200** |
| HTML `<link rel="canonical">` | Still references `.html` on 29 pages |

### Sitemap alignment correction (branch — not deployed)

| Item | Detail |
|---|---|
| Branch | `cursor/springfield-sitemap-canonical-alignment` |
| Change | `sitemap.xml`, canonical tags, Open Graph page URLs, JSON-LD page URLs, and internal navigation aligned to extensionless URLs |
| Local source files | HTML filenames remain `*.html` on disk |
| Deployment | **Prepared only — not deployed** |
| Live routing | Cloudflare serves extensionless URLs with **200**; `.html` paths **308** redirect |

### GSC inspection rule

Inspect and track indexing status using **extensionless canonical URLs** (see `indexing-priority-tracker.md`), not `.html` sitemap locs.

---

## 4. Protected tracking values (unchanged)

| Item | Value |
|---|---|
| Phone | (417) 242-5370 / `tel:4172425370` |
| Formspree | `https://formspree.io/f/mojzdkvg` |
| GTM | `GTM-GDJF54DV` |
| Canonical base | `https://springfieldjunkremovalservice.com` |
| Analytics events | `click_call`, `click_quote_button`, `submit_lead_form` |

---

## 5. Page inventory summary

| Type | Count |
|---|---|
| Homepage | 1 |
| Hub pages | 3 |
| Money / core service | 1 |
| Service pages | 18 |
| Guide pages | 3 |
| City pages | 5 |
| **Total** | **30** |

---

## 6. External systems — no changes

| System | Status |
|---|---|
| DNS | Not changed |
| CallRail routing | Not changed |
| Formspree | Not changed |
| GA4 / GTM container | Not changed |
| Public listings / citations | Not created or modified |
| Renter outreach | Not performed |
| Paid spend | None |

---

## 7. Recommended next action

1. **Commit** the corrected documentation batch
2. **Verify** the existing Google Search Console property and current sitemap submission status (read-only)
3. **Capture** GSC Page Indexing baseline data
4. **Manually inspect** Tier 1 extensionless canonical URLs — record indexed / not indexed / discovered / crawled
5. **Sitemap canonical-alignment** — prepared on branch `cursor/springfield-sitemap-canonical-alignment`, **not deployed**
6. **Request separate approval** for live conversion tests and indexing requests

Do not create a new GSC property. Do not submit sitemaps or indexing requests in this batch.

---

*Prepared by RankRentOS post-deployment workflow. No commit required for this baseline record until approved.*
