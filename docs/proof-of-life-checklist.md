# Proof-of-Life Checklist

Run after deployment to confirm the live site is functional.

**Production deploy:** 2026-07-11 (PR #11 `2006f8b`; PR #12 `57b7b8c` URL alignment; PR #13 `ef037f3` hub JSON-LD fix)  
**GSC baseline:** 2026-07-11 (verified)  
**Recheck window:** July 18–25, 2026  
**Weekly tracking:** `proof-of-life-weekly-tracker.md`

## Core functionality

- [x] Homepage loads over HTTPS
- [x] All 30 sitemap URLs load (200 after redirect)
- [ ] Phone link `tel:4172425370` works on mobile — **awaiting separate approval (not approved)**
- [ ] Quote form submits to Formspree (`mojzdkvg`) — **awaiting separate approval (not approved)**
- [x] Form hidden fields present in HTML: site, market, niche, service
- [x] GTM container loads (`GTM-GDJF54DV`) — verified in page source
- [ ] `analytics-events.js` fires on call click and form submit — **GTM preview test awaiting separate approval**

## Hub pages (live — extensionless canonical URLs)

- [x] `/junk-removal-services-springfield-mo` returns 200
- [x] `/junk-removal-service-areas-springfield-mo` returns 200
- [x] `/junk-removal-guides-springfield-mo` returns 200

## SEO files

- [x] `/sitemap.xml` lists 30 URLs
- [x] `/robots.txt` references sitemap
- [x] Favicon tags present in HTML

## Spot-check pages (live copy)

- [x] Homepage hub links present
- [x] Homepage corrected copy visible (claim-safe cards)
- [x] Money page loads
- [x] Hot tub page — scope confirmation language in production HTML
- [x] Hoarder page — heavy-clutter + hazmat disclaimer visible

## CallRail (do not change without approval)

- [ ] Website calls route to expected tracking number — **not verified this batch**
- [ ] Call events appear in analytics pipeline — **awaiting manual test**

## Search visibility (verified 2026-07-11)

- [x] DNS `google-site-verification` TXT present on apex domain
- [x] Existing Google Search Console **domain property** verified — `springfieldjunkremovalservice.com`
- [x] Sitemap submitted — `https://springfieldjunkremovalservice.com/sitemap.xml`; **Success**; 30 discovered pages; read July 11, 2026
- [x] Page Indexing baseline captured — 37 indexed, 35 not indexed
- [x] Performance baseline captured — 28d: 4.64K imp / 6 clicks / 0.1% CTR / pos 41.4; 7d: 1.47K imp / 2 clicks / 0.1% CTR / pos 40.9
- [x] Tier 1 extensionless canonical URLs inspected — see `indexing-priority-tracker.md`
- [x] Hub JSON-LD unparsable structured data fixed (PR #13) and live-verified
- [x] Indexing requests submitted for eight approved URLs (2026-07-11) — see tracker
- [x] Week-1 metrics recorded in `proof-of-life-weekly-tracker.md`
- [ ] Recheck indexing status — **July 18–25, 2026**
- [ ] Additional indexing requests — **not performed; requires separate approval**

## Proof-of-life assessment (2026-07-11)

| Signal | Status |
|---|---|
| Technically live | Yes — 30/30 URLs, HTTPS, extensionless canonicals |
| Indexed | Yes — 37 pages indexed in GSC |
| Impressions / clicks | Yes — 4.64K impressions / 6 clicks (28d); early query signals visible |
| Early rankings | Yes — e.g. construction debris ~5.9, commercial junk ~15.7, yard waste 1 click @ 10.0 |
| Renter-ready | **No** — call/form conversion verification and authority/citation work incomplete |
