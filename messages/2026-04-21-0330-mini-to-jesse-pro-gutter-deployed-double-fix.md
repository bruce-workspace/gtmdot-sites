---
from: mini
to: jesse
date: 2026-04-21
subject: Pro Gutter Cleaning deployed — Unsplash hero-CSS swap + gallery built from scratch + Bruce photos
priority: normal
---

## Deployed

- **Live:** https://pro-gutter-cleaning.pages.dev
- **Claim:** `PROG4046`
- **Commit:** `83dfc51` on `intake/pro-gutter-cleaning`

## Two bugs fixed, one rewire

### Bug 1: Unsplash hero-CSS (template-bug-b)

Rule1 shipped `.hero-bg { background: url('https://images.unsplash.com/
photo-1558618666-fcd25c85cd64?w=2000&q=80') center/cover; }`. Classic
stock-image-in-CSS pattern (same as forest-park-collision caught earlier
tonight). Swapped to `url('photos/hero.jpg')` with the standard
brightness/contrast filter.

### Bug 2: No gallery section at all

Rule1's pro-gutter-cleaning template was 757 lines with stats, services,
reviews, history, area, FAQ, contact sections — but **no gallery
section**. With Bruce's delivery I added one between services and
reviews, with full CSS for gallery-grid / gallery-item / data-caption
overlay matching the other sites in the batch.

## Gallery picks from Bruce's 20 Yelp photos

- **hero**: Close-up of a gloved hand pulling a clump of red-and-yellow
  leaves from a gutter (quintessential gutter-service identity shot)
- **gbp-1**: Branded service-card overlay — aerial autumn forest with
  "PRO GUTTER / CLEANING & REPAIR / 404-606-2950" text (brand confirm
  + phone matches RESEARCH)
- **gbp-2**: Finished white gutter on beige siding + weathervane on
  roofline (clean residential install)
- **gbp-3**: Finished gutter corner + downspout on cream siding ranch
- **gbp-4**: Roof-level gutter inspection shot (aerial)
- **gbp-5**: Storm damage — tree crashed through residential roof
  (dramatic roof-repair differentiator, also matches sister entity
  "Pro Roof Gutters and Siding LLC" service scope)
- **gbp-6**: Close-up of storm-damaged asphalt shingles

## Content angle

The storm-damage + roof-repair photos confirm the service scope goes
well beyond gutter cleaning. The parent/sister entity "Pro Roof
Gutters and Siding LLC" (same address, same phone) explains it:
**Matt's crew handles whole-exterior roof + gutter + storm recovery.**
Worth leading outreach copy with that — "gutter cleaning is 20% of
what we do, storm recovery is the rest."

## Reviews merged

reviews.json: 7 → 10 (3 new Bruce Yelp reviews merged, all 5-star).

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓
- (b) No stock ✓ (Unsplash CSS swap succeeded, 0 matches)
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `PROG4046` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Tonight's running total — 28 sites live, 3 Bruce deliveries pending

1–27 as before +
28. **Pro Gutter Cleaning (PROG4046) — Unsplash hero-CSS + gallery
    built + Bruce photos ✨**

Still pending (Bruce delivered, awaiting Mini):
- **premier-tv-mounting-atl** — 15 photos, 0 reviews (Yelp JS-only)
- **handy-dandy-atlanta** — 8 carrd.co portfolio photos
- **doctor-concrete-atl** — reviews-only merge (9 Angi reviews, no photos)

Next: premier-tv-mounting.

— Mini
