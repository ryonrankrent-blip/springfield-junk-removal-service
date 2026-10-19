# Springfield Junk Removal Service

Static business site for junk removal in Springfield, MO. Cloudflare Pages deploys `main`. This repo does not change production deploy settings.

## Protected values

- Phone: `(417) 242-5370` / `tel:4172425370` (existing CallRail number)
- Formspree: `https://formspree.io/f/mojzdkvg`
- GTM: `GTM-GDJF54DV`
- Domain: `https://springfieldjunkremovalservice.com`
- GA4 property `541475893`: measurement ID was not in the repo. `analytics-events.js` leaves `GA4_MEASUREMENT_ID_PROPERTY_541475893` empty on purpose.

## Pages

Nine public URLs. Retired URLs 301 in `_redirects`.

- `/` — Junk Removal in Springfield, MO
- `/residential-junk-removal-springfield-mo`
- `/cleanouts-springfield-mo`
- `/commercial-junk-removal-springfield-mo`
- `/yard-waste-removal-springfield-mo`
- `/junk-removal-service-areas-springfield-mo`
- `/junk-removal-cost-springfield-mo`
- `/springfield-junk-disposal-guide`
- `/contact`

## Local QA

```bash
python3 scripts/build-site.py
chmod +x scripts/qa-check.sh scripts/link-check.sh
./scripts/qa-check.sh
./scripts/link-check.sh
python3 scripts/preview-server.py
```

Open `http://127.0.0.1:8080/`.

`scripts/fix-claims.py` and `scripts/create-hubs.py` are retired and exit immediately.
