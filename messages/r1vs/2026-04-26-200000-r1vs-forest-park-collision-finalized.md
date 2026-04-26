---
from: r1vs (MacBook Claude Code)
to: jesse, mini (Master Site Builder), bruce (Collector + Asset Intelligence)
date: 2026-04-26
subject: FINALIZED — forest-park-collision: first end-to-end §11.11 production run
priority: high — Bruce please pick up the collect-request immediately per Jesse direction
refs:
 - HANDOFF-CONTRACT.md §11.11 (Asset Intelligence Layer)
 - sites/forest-park-collision/collect-request.md (filed by R1VS for Bruce, hero_intent: aspirational + generated_images_allowed: yes)
 - jesse direction 2026-04-26 ("override Bruce's waiting until the second or third run, just to see what kind of real output we could get from Bruce with the new model")
---

## TL;DR

First end-to-end production run of the §11.11 pipeline. forest-park-collision
(Forest Park, GA — Kevin's collision shop, 4.8★/74 GBP reviews) ran cleanly
through Phases 0-5. Both gates passing 7/7. **Bruce is engaged** via
`collect-request.md` with `hero_intent: aspirational` + `generated_images_allowed: yes`
per Jesse's direction to test gpt-image-2 on this first run rather than wait.

## Phase results

| Phase | Tool | Result |
|---|---|---|
| 0 — Legitimacy | `legitimacy-screen.py --places-api` | ✅ PASS (4.8 / 74 reviews / GBP-match-verified / not dormant) |
| 1 — Snapshot+reviews | `write-gbp-snapshot.py --places-api` | ✅ atomic write of `gbp_snapshot.json` (10 GBP photos noted) + `reviews.json` (5 verbatim Google) |
| 1b — State files | hand | ✅ `BUILD-STATE.md` initialized, `icon-intent.json` written per ICON-MAPPING.md collision section |
| 2 — Business data | hand | ✅ `business-data.json` with 4 services, full per-page content (4 paragraphs / 4 steps / 3 FAQs each) |
| 3 — Scaffold fill | `fill-scaffold.py` | ✅ 9 HTML files generated; `render-reviews-bar.py` auto-rendered Path A with all 5 verbatim reviews |
| 4 — Pre-push gate | `pre-push-gate.sh` | ✅ 7/7 PASS first try |
| 5 — Verify-build | `verify-build.sh` (local) | ✅ 7/7 PASS first try |

## Sources Attempted (per §11.3)

| Source | Status | Photos | Reviews | Notes |
|---|---|---|---|---|
| Google Places API v1 (findplacefromtext + Place Details) | success | 0 (count only — 10 available) | 5 | place_id confirmed, rating 4.8, 74 total reviews on GBP, last review 2026-03-04 |
| Owner website | not-applicable | — | — | No website on file. GBP-only business. |
| Yelp | not-attempted | — | — | Requires persistent browser — handed to Bruce |
| Nextdoor | not-attempted | — | — | Same |
| Facebook | not-attempted | — | — | Same |

## Photo slot inventory (for Mini integration + Bruce reference)

20 photo slots open across the 9 HTML files. All carry `.gtmdot-photo-slot` + `data-context` markers. **No pre-written captions** — Master Site Builder writes captions after Bruce's photo handoff.

| Slot ID | Page | data-context |
|---|---|---|
| HERO | index.html | `shop-exterior-OK\|finished-vehicle-OK\|owner-portrait-OK\|aspirational-body-shop-OK\|atmosphere-OK` |
| GALLERY_1..6 | index.html | per-slot mix (shop interior / completed vehicle / before-after / team / shop exterior / paint booth) |
| ABOUT_PHOTO | about.html | `owner-portrait-OK\|team-OK\|storefront-OK` |
| SERVICE_GALLERY_1..3 | per service page (×4) | service-specific photo contexts |

Full per-slot list in `business-data.json` and the per-page HTML.

## What Bruce should do

Read `sites/forest-park-collision/collect-request.md` end-to-end. Headline points:

- **`hero_intent: aspirational`** — Kevin's reviews emphasize "looks brand new," "treated like family," "professional." Hero should evoke that brand tone, not generic stock-collision-shop tropes.
- **`generated_images_allowed: yes`** — full §11.11.1 capability authorized for hero, brand, service-card-bg, atmosphere. Per §11.11.5 guardrails, generated images stay in `photos-generated/`, get `license_note`, stay out of forbidden slot contexts (no team/owner/real-customer slots).
- **GBP photo pull**: 10 photos available — primary target.
- **Yelp/Nextdoor/Facebook**: secondary enrichment for both photos and reviews.
- **Budget caps**: 20 photos / 15 reviews / 12 wall-clock minutes / 4 generated images.

Bruce's `bruce-asset-intel.md` and `bruce-asset-intel.json` are due per §11.11.6 + §11.11.7. R1VS will `consume-asset-intel.py` your output the moment it lands.

## What Mini should do (post-Bruce)

When Bruce's `bruce-collected.md` + `bruce-asset-intel.md/.json` land:

1. `python3 scripts/reviews-merge.py forest-park-collision` — dedupes Bruce's raw reviews against R1VS's existing 5
2. `python3 scripts/render-reviews-bar.py forest-park-collision` — re-renders if review count changed paths
3. `python3 scripts/consume-asset-intel.py forest-park-collision` — validates schema, surfaces hero rec for default-accept (§11.11.3), files icon-flag messages back to R1VS (§11.11.4), groups photo_quality for QA
4. Per §11.11.3: default-accept Bruce's hero recommendation. Override only on documented QA reason.
5. Integrate selected photos from `photos-raw/` and `photos-generated/` into `sites/forest-park-collision/photos/`. Preserve `data-source="generated"` on the HTML side for any generated images per §11.11.5 guardrail 6.
6. Write captions/alt text per §11.11 — Mini's authority, not Bruce's.
7. Inject claim bar (`FPCJ7255` from Supabase) + popup at deploy time per CLAUDE.md.
8. Deploy to `forest-park-collision.pages.dev`.
9. Verify post-deploy with `./scripts/verify-build.sh forest-park-collision --live https://forest-park-collision.pages.dev`.
10. Supabase: advance stage from `needs_enrichment` → `needs_approval` (or whatever post-Bruce stage applies in the new split).

## Why this is the first §11.11 production run worth watching

This is the first site where:

- Bruce's expanded scope (§11.11.1) is exercised in production
- gpt-image-2 generates a hero (per `hero_intent: aspirational`)
- Mini's default-accept behavior (§11.11.3) is tested against real Bruce output
- Icon-flag routing (§11.11.4) gets a real-world trial if Bruce flags any
- The 30% generated-image cap (§11.11.5 guardrail 5) gets first production data
- The full pipeline runs end-to-end against a real CRM-side prospect with real Google reviews

Per Jesse direction: this is also a **comparison data point** against the
pre-§11.11 build at `sites/plugged-electricians-atl/` (which used the same
gates but no §11.11 capabilities). Compare both sites once Bruce delivers
to evaluate whether the new capabilities measurably improve the output.

## Files committed for this build (intake branch should include)

- `sites/forest-park-collision/legitimacy-check.json`
- `sites/forest-park-collision/gbp_snapshot.json`
- `sites/forest-park-collision/reviews.json`
- `sites/forest-park-collision/icon-intent.json`
- `sites/forest-park-collision/business-data.json`
- `sites/forest-park-collision/BUILD-STATE.md`
- `sites/forest-park-collision/index.html` (243 lines)
- `sites/forest-park-collision/services.html`
- `sites/forest-park-collision/about.html`
- `sites/forest-park-collision/contact.html`
- `sites/forest-park-collision/_base.css`
- `sites/forest-park-collision/collision-repair-atlanta.html` (per-service)
- `sites/forest-park-collision/auto-body-paint-atlanta.html`
- `sites/forest-park-collision/dent-bumper-repair-atlanta.html`
- `sites/forest-park-collision/insurance-claim-help-atlanta.html`
- `sites/forest-park-collision/collect-request.md` (filed for Bruce)

R1VS handing off. Bruce + Mini own the rest.

— R1VS (Rule1, MacBook Claude Code)
