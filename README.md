# Springfield Junk Removal Service

Static HTML rank-and-rent site for junk removal quote requests in Springfield, MO.

## Protected values (do not change without approval)

- Phone: `(417) 242-5370` / `tel:4172425370`
- Formspree: `https://formspree.io/f/mojzdkvg`
- GTM: `GTM-GDJF54DV`
- Domain: `https://springfieldjunkremovalservice.com`

## Local QA

```bash
chmod +x scripts/qa-check.sh scripts/link-check.sh
./scripts/qa-check.sh
./scripts/link-check.sh
python3 -m http.server 8080
```

Open `http://localhost:8080/` to preview.

## Documentation

See `docs/` for audits, claim logs, link maps, and deployment checklists.

## Reusable scripts (review before running)

- `scripts/qa-check.sh` — run before commit/deploy
- `scripts/link-check.sh` — internal link validation
- `scripts/fix-claims.py` — **reusable migration tool** for bulk claim-safe copy passes. Do not run against production HTML without manual review of the diff.
- `scripts/create-hubs.py` — **reusable generator** for hub pages from a template page. Regenerates hub HTML files; review output before committing.
