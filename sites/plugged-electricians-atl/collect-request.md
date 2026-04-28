---
slug: plugged-electricians-atl
requested_at: 2026-04-27T22:30:00Z
requested_by: r1vs
deadline: 2026-04-28T22:30:00Z
priority: normal
hero_intent: aspirational
generated_images_allowed: yes
---

# Collect Request — Plugged Electricians Atl LLC

R1VS-authored as the **second §11.11 pilot** under the new multi-page scaffold
design system (v2). First pilot was forest-park-collision; this one validates
the same end-to-end Bruce → Mini handoff against a different vertical
(electrical, blue accent) so we can confirm the §11.11.3 default-accept
behavior, the photo-quality labeling under the new hover-caption pattern,
and the icon-flag routing through R1VS.

## Business context

- **Name:** Plugged Electricians Atl LLC
- **Trade:** Electrical services (residential repair, panel upgrades, EV charger install, ceiling fans + lighting)
- **Owner:** Trell Black (named in 4+ Google reviews)
- **Address:** 1445 Woodmont Ln NW, Atlanta, GA 30318
- **Phone:** (404) 800-1700
- **Website:** none on file (GBP listing only)
- **Key differentiator:** owner-operated, "professional and clean" trades reputation, 4.9★ from 13 reviews — small-volume but consistently high-rated electrician
- **GBP place_id:** ChIJC3_VtuzT6WkR9psfNzHcAWo
- **GBP URL:** https://maps.google.com/?cid=...

## Current state — what we have and what's missing

| Artifact | Status | Notes |
|---|---|---|
| `gbp_snapshot.json` | present | 4.9★ rating, 5 reviews captured, place_id confirmed |
| `reviews.json` | captured 5 (>=3) | Path A reviews-track rendered with all 5 verbatim |
| `RESEARCH.md` | not present | Bruce-collected.md substitutes per §11.11 |
| `legitimacy-check.json` | passed | 4.9 rating, 13 reviews, fresh, GBP-confirmed |
| `BUILD-STATE.md` | reads `verified-ready-for-handoff` (was old scaffold) — now re-rendered on multi-page v2 |
| Photos in `photos/` | none yet | All slots open: HERO, GALLERY_1..6, ABOUT_PHOTO, SERVICE_GALLERY for 4 service pages |
| Photos in `photos-raw/` | **16 already collected** (gbp-01..09 + secondary sources) | Bruce can re-rank these against the new design's hover-caption pattern |
| `bruce-collected.md` | present (2026-04-24) | Pre-§11.11 collection — needs §11.11 asset-intel pass |
| `business-data.json` | written | 4 services with full per-page content — all 40 required tokens present |
| `icon-intent.json` | written | zap, battery-charging, plug-zap, lightbulb per ICON-MAPPING.md §Electrical |
| `bruce-asset-intel.{md,json}` | **missing — this request** | Bruce please produce per §11.11.6 + §11.11.7 |
| `photos-generated/hero-01.png` | **missing — this request** | Bruce please generate per §11.11.1, hero_intent=aspirational |

## Slot targets per HTML data-context

(Read these from the rendered `sites/plugged-electricians-atl/index.html` and
the 4 per-service pages to confirm — they're the source of truth.)

- **HERO** — `clean-electrical-work-OK | service-van-OK | aspirational-electrician-OK | atmosphere-OK`
  - Per `hero_intent: aspirational`: prefer a clean, editorial composition. A bright residential breaker panel cleanly wired, OR an aspirational modern electrical work scene, OR atmospheric "tools-of-the-trade" macro shot. Documentary fallback OK if a strong real photo is in `photos-raw/`.
- **GALLERY_1** — `panel-upgrade-OK | breaker-box-OK | clean-wiring-OK`
- **GALLERY_2** — `ev-charger-install-OK | residential-OK | finished-install-OK`
- **GALLERY_3** — `ceiling-fan-OK | lighting-fixture-OK | finished-room-OK`
- **GALLERY_4** — `owner-portrait-OK | technician-OK | service-truck-OK` (Trell if visible)
- **GALLERY_5** — `outdoor-electrical-OK | weatherhead-OK | meter-OK`
- **GALLERY_6** — `tools-OK | meter-on-panel-OK | atmosphere-OK`
- **ABOUT_PHOTO** — `owner-portrait-OK | team-OK | service-truck-OK`
- **SERVICE_GALLERY_1..3** per service page — service-specific contexts in respective HTML files

## Why we need Bruce

- **GBP photo pull:** the `gbp_snapshot.json` shows 0 photos pulled, but `photos-raw/` has 16. These came from Bruce's prior collection runs (yelp-NN.jpg + secondary). Bruce please re-rank against the new design pattern.
- **Owner website:** none — small business, GBP-only. No web-source content beyond what's already collected.
- **Review enrichment:** 5 captured against ~13 GBP total. If easily expandable from secondary sources (Yelp, Nextdoor, Thumbtack), pull more — but not required to ship.
- **Hero generation:** required. No real photo in `photos-raw/` rises to "homepage hero." A generated aspirational shot is the right call.
- **§11.11 asset-intel:** missing. This is the primary deliverable.

## Generated images allowed (per §11.11.1)

`generated_images_allowed: yes` — Bruce may generate via gpt-image-2 for:

- **HERO** (preferred per `hero_intent: aspirational`) — aspirational/editorial electrical-work composition. Brand tone from reviews: "professional," "clean," "knowledgeable," "fair pricing." Avoid generic stock-electrician tropes (no leering hard hats, no neon-blue lightning bolts, no "shocked customer" cliches).
- **service-card-bg** for the 4 service cards on services.html — atmospheric backgrounds, no specific company representation.
- **atmosphere** sections — clean breaker panel, modern outlet install, organized truck interior (no specific people).

DO NOT generate: owner portraits, technician headshots, anything that would impersonate Trell or his actual team. Real photos only for `team-OK / owner-portrait-OK` slots.

## What to collect / produce

### Asset intel (REQUIRED — primary §11.11 deliverable)
- `bruce-asset-intel.md` per §11.11.6 — narrative analysis: hero recommendation, photo-quality labels, object/context verification, icon flags
- `bruce-asset-intel.json` per §11.11.7 — machine-readable: `hero_recommendation` (preferred_path + fallback_path + reasoning), `photo_quality` (per-photo tier + role + caption-overlay-risk), `object_verification`, `icon_warnings`, `generated_images`, `model_stack`

### Generated hero
- `photos-generated/hero-01.png` per §11.11.1 + §11.11.5 guardrails 1–6

### Photo re-ranking (advisory)
- Per Bruce's revalidation message on forest-park-collision (2026-04-27), tag photos for caption-overlay risk: which photos in `photos-raw/` have primary proof detail in the bottom third (where hover captions sit) and would lose punch under the new gallery design.

### Optional review enrichment
- If Yelp / Nextdoor / Thumbtack expose 3-5 more verbatim reviews easily, append to `reviews-raw.json`. Skip if blocked. Path A is already triggered (>=3 captured) so this is purely upside.

## Budget caps (HARD)

- **max_photos:** 0 new (existing 16 are sufficient — re-ranking only)
- **max_reviews:** 10 (advisory enrichment)
- **max_wall_clock_minutes:** 12 (image generation counts toward this)
- **max_scrape_attempts_per_source:** 2
- **max_generated_images:** 2 (hero + 1 alt)

## Success criteria

- **success:** `bruce-asset-intel.{md,json}` shipped per schema, `photos-generated/hero-01.png` generated per `hero_intent: aspirational`, photos in `photos-raw/` re-ranked with caption-overlay-risk tags.
- **partial:** asset-intel shipped without hero, OR hero shipped with placeholder asset-intel.
- **failed:** neither artifact ships.

Even partial is shippable — Mini will default-accept the hero recommendation per §11.11.3 and proceed to deploy.

## Output expected from Bruce

- `sites/plugged-electricians-atl/bruce-asset-intel.md` — advisory analysis per §11.11.6
- `sites/plugged-electricians-atl/bruce-asset-intel.json` — machine-readable per §11.11.7
- `sites/plugged-electricians-atl/photos-generated/hero-01.png` — generated hero
- `sites/plugged-electricians-atl/reviews-raw.json` — appended new reviews from secondary sources (optional)
- `sites/plugged-electricians-atl/bruce-collected.md` — completion update describing what changed since the prior 2026-04-24 collection run (or note "no re-collection — asset-intel only")

## After Bruce returns

R1VS or Mini will:

1. Run `python3 scripts/consume-asset-intel.py plugged-electricians-atl` to validate `bruce-asset-intel.json` against schema, surface hero recommendation, and route any icon flags back to R1VS via `messages/<date>-bruce-icon-flag-<slug>.md`.
2. Mini integrates per §11.11.3 default-accept: copy `photos-generated/hero-01.png` → `gtmdot/sites/plugged-electricians-atl/photos/hero.jpg`; map `photos-raw/gbp-NN.jpg` → `photos/gbp-N.jpg` per Bruce's photo-quality labels; flip all `data-resolved="false"` → `"true"` and add figcaptions + alt text per Bruce's intel; inject claim bar (Mini will pull a fresh code from the checkout system).
3. Mini deploys via Option 1 manual flow (same as forest-park-collision precedent).
4. Mini Slack-pings Jesse with the live URL.
5. Site stays at Supabase `needs_approval` until Jesse confirms on mobile.

— R1VS
