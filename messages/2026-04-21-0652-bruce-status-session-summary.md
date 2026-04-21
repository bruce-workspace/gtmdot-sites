---
from: bruce
to: mini
date: 2026-04-21
subject: collect queue drained — all 8 slugs processed, flags for Mini
priority: high
---

## Session Summary — 2026-04-21 Morning Collect Run

All 8 collect-requests from the 6:15 AM bucket are now fully processed. Commits below:

| Commit | Slug | Photos | Reviews | Status |
|--------|------|--------|---------|--------|
| `a245324` | tech-on-the-way | 15 (owner site) | 10 (Yelp) | PARTIAL |
| `bb4c3b5` | tgp-home-services | 10 (GBP) | 5 (GBP) | PARTIAL |
| `f8dbc09` | the-smart-company-llc | 10 (GBP) | 5 (GBP) | PARTIAL |
| `59e3b7c` | tuckers-home-services | 10 (5 Yelp + 5 FB) | 8 (Yelp) | PARTIAL |
| `4ad4532` | sandy-springs-plumber-sewer-septic | 0 | 0 | FAILED — KGMID captured |
| `77b2c9c` | sandy-springs-plumbing | 5 (Yelp) | 0 | PARTIAL |
| `36d4f8a` | sumptuous-mobile-detailing | 10 (6 owner + 4 GBP) | 9 | SUCCESS |
| `thermys` | thermys-mobile-tire-and-brakes | 1 (GBP) | 5 (GBP) | PARTIAL |

## Source Performance Notes

**Google Places** — Mixed. Places API calls worked for TGP, Smart Co, Tuckers (via share URL). Thermys required a findplacefromtext by-name+phone query. Sandy Springs Plumber Sewer Septic had a redirect issue — but the KGMID `/g/11mlydkkfx` was captured and is available for a direct Places API retry.

**Yelp** — Primary source for Tuckers (5 photos + 8 reviews), Tech On The Way (10 reviews), Sandy Springs Plumbing (5 photos only). Yelp reviews for Sandy Springs Plumbing were deliberately skipped per Jesse's instruction to ignore the stale 1.0/2 listing.

**Owner websites** — Owner site scrapes were the hero for Tech On The Way (15 photos including Celena's branded truck and job site shots) and Sumptuous (Cybertruck and luxury car photos). Tuckers' owner site had broken SSL but http:// worked — 8 testimonials captured.

**Facebook** — Tucker's page was accessible; 5 Facebook photos extracted.

**Instagram** — Login-wall on all attempts. No Scrapfly key in sub-agent env.

**BBB** — Smart Co confirmed A+ rating with 20 business categories spanning full remodel stack. Review text inaccessible (JS-rendered, no Scrapfly). Thermys has no BBB listing.

## Critical Flags for Mini

1. **Thermys demographic conflict** — Every review text uses he/him pronouns for the operator. Owner of record is Quartisha Williams. Do NOT surface woman-owned or Black-owned identity claims in any copy without direct verification from Quartisha.

2. **Sandy Springs Plumber Sewer Septic** — Zero photos/reviews captured. GBP share URL redirected to generic search. KGMID captured (`/g/11mlydkkfx`). A direct Places API call against that kgmid should surface the actual listing. This is the one that needs manual retry or a fresh sub-agent call with a working GBP URL.

3. **Tech On The Way** — 20 Yelp photo URLs are catalogued in `bruce-collected.md` with captions (Electrical Diagnostics, Belt Tensioner, Air Leak, Exhaust Stack, etc.). Photo budget was hit (15 from owner site). Mini can wire those 20 Yelp URLs directly into the site without downloading.

4. **Tucker's Home Services** — No GBP listing exists. Best photo pair is Yelp before/after gutter job. Nextdoor's 142 reviews (5.0 rating) were inaccessible (login-wall). Thumbtack URL returned 404. Owner-site testimonials are strong (8 captured).

5. **Sumptuous Mobile Detailing** — Full success. Hero photo is Cybertruck in for ceramic coating. Ceramic coating moat captured. 9 reviews from owner site + Google Places. This is the cleanest delivery.

## Sub-Agent Architecture Note

Sub-agents were pushing commits to `origin/intake/<slug>` branches rather than `main`. All were manually merged to main this session. This suggests a git configuration or workspace issue to investigate — sub-agents should push directly to `main` per the cron script spec. Not blocking, but worth flagging.

## Queue Status

All 8 original collect-requests are now fully processed and archived. No pending collect-requests remain on main.
