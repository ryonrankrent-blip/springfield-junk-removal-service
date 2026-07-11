# Proof-of-Life Checklist

Run after deployment to confirm the live site is functional.

**Production deploy:** 2026-07-11 (PR #11, merge `2006f8b`)  
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

## Search visibility (manual, ongoing)

- [ ] Verify existing Google Search Console property (do not create new)
- [ ] Confirm current sitemap submission status (read-only)
- [ ] Capture Page Indexing baseline
- [ ] Inspect Tier 1 extensionless canonical URLs — see `indexing-priority-tracker.md`
- [ ] Request indexing only after separate approval
- [ ] Week-1 metrics recorded in `proof-of-life-weekly-tracker.md`
