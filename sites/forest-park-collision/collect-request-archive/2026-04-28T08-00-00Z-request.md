---
slug: forest-park-collision
requested_at: 2026-04-26T20:30:00Z
requested_by: r1vs
deadline: 2026-04-27T20:30:00Z
priority: normal
hero_intent: aspirational
generated_images_allowed: yes
---

# Collect Request — Forest Park Collision

R1VS-authored as part of the first end-to-end pilot under §11.11. Jesse ACK'd
overriding the "wait until 2nd-3rd run" caution to engage Bruce immediately
on the new model stack. Bruce please proceed with full Asset Intelligence
output (`bruce-asset-intel.md` + `.json`) per §11.11.

## Business context

- **Name:** Forest Park Collision
- **Trade:** Collision Repair (auto body, paint, dent/bumper repair, insurance claims)
- **Owner:** Kevin (referenced by name in 4+ Google reviews)
- **Address:** 198 Central Ave, Forest Park, GA 30297
- **Phone:** +16786470907 / (678) 647-0907
- **Website:** none on file (GBP listing only)
- **Key differentiator:** family-feel body shop, 4.8★ across 70+ Google reviews mostly through word-of-mouth, all body+paint work done in-house (no subcontracting)
- **GBP place_id:** ChIJ-confirmed via Places API; cid 4262659531138535018
- **GBP URL:** https://maps.google.com/?cid=4262659531138535018

## Current state — what we have and what's missing

| Artifact | Status | Notes |
|---|---|---|
| `gbp_snapshot.json` | present | 4.8 rating, 74 total reviews, 5 captured, 10 photos on GBP, last review 2026-03-04 |
| `reviews.json` | captured 5 (>=3) | 5 verbatim Google reviews — Path A reviews-track rendered |
| `RESEARCH.md` | skipped for pilot | Bruce-collected business intel will substitute if needed |
| `legitimacy-check.json` | passed | 4.8 rating, 74 reviews, fresh, GBP-confirmed |
| `BUILD-STATE.md` | initialized | Phases 0-5 marked through verify-build (gates 7/7 + 7/7) |
| Photos in `photos/` | none | All slots open: HERO, GALLERY_1..6, ABOUT_PHOTO, SERVICE_GALLERY (per service page) |
| `business-data.json` | written | 4 services with full per-page content |
| `icon-intent.json` | written | car, paintbrush, shield, file-text per ICON-MAPPING.md collision section |

## Slot targets per HTML data-context

- **HERO** — `shop-exterior-OK | finished-vehicle-OK | owner-portrait-OK | aspirational-body-shop-OK | atmosphere-OK`
  - Per `hero_intent: aspirational`: prefer a clean, editorial composition. A freshly painted vehicle reflecting shop lighting, OR an aspirational shop-exterior shot, OR an atmospheric "modern body shop" scene. Documentary fallback OK if the GBP has a strong real photo.
- **GALLERY_1** — `shop-interior-OK | vehicle-on-lift-OK | repair-in-progress-OK`
- **GALLERY_2** — `completed-vehicle-OK | fresh-paint-OK | finished-quality-OK`
- **GALLERY_3** — `before-after-OK | damage-shot-OK | repair-progress-OK`
- **GALLERY_4** — `owner-portrait-OK | technician-OK | team-OK` (Kevin if visible — he's named in reviews)
- **GALLERY_5** — `shop-exterior-OK | signage-OK | atmosphere-OK`
- **GALLERY_6** — `tools-OK | paint-booth-OK | atmosphere-OK`
- **ABOUT_PHOTO** — `owner-portrait-OK | team-OK | storefront-OK`
- **SERVICE_GALLERY_1..3** per service page — service-specific contexts in respective HTML files

## Why we need Bruce

- **Google Places API:** captured 5 of 74 reviews + saw 10 photos available but didn't pull them. Bruce can pull all 10 GBP photos for proof + gallery slots.
- **Owner website:** none — Kevin's business runs on word-of-mouth, no web presence beyond GBP.
- **Direct Firecrawl scrape:** not attempted.
- **Other sources:** Yelp typically has additional photos for body shops; Nextdoor often has neighbor recommendations with photos; Facebook may have a business page.

## Requested sources (priority order)

1. **GBP photo pull (10 photos available)** — all 10 directly via Places Photo API. Highest-confidence real photos. Primary target for proof + gallery slots.
2. **yelp.com** — search "Forest Park Collision" + Forest Park GA OR phone (678) 647-0907. Typical body-shop Yelp listings have 5-15 additional photos. Secondary target.
3. **facebook.com** — search "Forest Park Collision" + Atlanta. May have a business page with team/shop photos.
4. **nextdoor.com** — local neighborhood reviews of the shop, occasionally with customer-uploaded photos.

## Generated images allowed (per §11.11.1)

`generated_images_allowed: yes` — Bruce may generate via gpt-image-2 for:

- **HERO** (preferred per `hero_intent: aspirational`) — aspirational/editorial body shop composition. Bruce please target the brand tone Kevin's reviews reveal: "looks brand new," "treated like family," "professional," "honest." Avoid generic stock-collision-shop tropes (no leering hot rods, no cliché lift-and-tools images).
- **service-card-bg** for the 4 service cards on services.html — atmospheric backgrounds, no specific company representation.
- **atmosphere** sections — paint booth, clean shop interior, body work in progress (no specific people).

DO NOT generate: owner portraits, technician headshots, anything that would impersonate Kevin or his actual team. Real photos only for `team-OK / owner-portrait-OK` slots.

## What to collect

### Photos
- **Target count:** 10 from GBP + 5-10 enrichment + 1-3 generated for HERO/atmosphere = ~16-20 total
- **Match against intent:** see slot targets above
- **Skip:** blurry photos, low-resolution thumbnails, screenshots, photos of other businesses

### Reviews
- **Target count:** 5 minimum already captured (Places Details cap). Yelp/Nextdoor can add 3-5 more for richer cross-source signal.
- **Verbatim only:** never summarize, paraphrase, or fabricate
- **Required fields:** `author`, `rating`, `date` (ISO), `source`, `text`
- **Reviewer-name slot rule:** never "Google Customer", "Yelp Customer", "Verified Homeowner" — pre-push-gate enforces

## Budget caps (HARD)

- **max_photos:** 20
- **max_reviews:** 15
- **max_wall_clock_minutes:** 12 (image generation counts toward this)
- **max_scrape_attempts_per_source:** 2
- **max_generated_images:** 4 (per §11.11.8 default)

## Success criteria

- **success:** GBP photo pull complete (10/10), at least one secondary source returns photos, review enrichment >= 8 total reviews captured across sources, hero generated per intent.
- **partial:** GBP pull only (no secondary source), or hero generation skipped/failed, or partial review enrichment.
- **failed:** GBP photo pull blocked AND no secondary source.

Even partial is shippable — Mini can decide whether to use what Bruce returned or request enrichment via follow-up `collect-request.md`.

## Output expected from Bruce

- `sites/forest-park-collision/photos-raw/<source>-NN.<ext>` — scraped photos, source-prefixed
- `sites/forest-park-collision/photos-generated/<purpose>-NN.<ext>` — generated images per §11.11.1
- `sites/forest-park-collision/reviews-raw.json` — appended new reviews from secondary sources
- `sites/forest-park-collision/bruce-collected.md` — completion report per §11.6
- `sites/forest-park-collision/bruce-asset-intel.md` — advisory analysis per §11.11.6
- `sites/forest-park-collision/bruce-asset-intel.json` — machine-readable per §11.11.7

## After Bruce returns

R1VS or Mini will run:
- `scripts/reviews-merge.py forest-park-collision` (merges raw + existing into unified reviews.json)
- `scripts/render-reviews-bar.py forest-park-collision` (re-renders homepage with merged set)
- `scripts/consume-asset-intel.py forest-park-collision` (validates schema, surfaces hero rec, files icon flags to R1VS, surfaces photo-quality grouping for Mini)
- Mini integrates photos into `sites/forest-park-collision/photos/` per §11.11.3 default-accept of Bruce's recommendations
- Mini deploys to `forest-park-collision.pages.dev` with claim-bar injection

This is the first §11.11 production run. R1VS will compare the resulting site
quality against the previous (pre-§11.11) builds in `sites/` to evaluate the
improvement from gpt-image-2 hero + better Bruce judgment.
