---
from: mini
to: jesse
date: 2026-04-21
subject: Done Right Drywall deployed — Bruce Yelp delivery (25 photos → 7 picked + 6 reviews)
priority: normal
---

## Deployed

- **Live:** https://done-right-drywall.pages.dev
- **Claim:** `MTJL8654`
- **Commit:** `4fb2f04` on `intake/done-right-drywall`

## Second Bruce round-trip processed this session

Bruce delivered **25 real photos** across both Yelp listings
(Atlanta 15 + Norcross 10) plus 7 reviews. That's the biggest photo
jackpot from any Bruce delivery this overnight batch.

## Photo-selection judgment

Bruce's 25 photos were a mix — some great real work, some branded
marketing cards with text overlay, some non-photos (SMS screenshots,
Yelp-review screenshots). I skipped:

- `yelp-atlanta-10` — branded logo card (good for social but not
  gallery-appropriate)
- `yelp-norcross-03` — screenshot of a customer text message ("German
  was very kind…")
- `yelp-norcross-05` — screenshot of a Yelp review from Clarice
  Farrell

Picked 7 clean work shots:

- **hero**: Tech on ladder sanding a kitchen ceiling with Dewalt
  drywall sander (owner-in-action, THE drywall identity shot)
- **gbp-1**: "Now-you-see-it / now-you-don't" branded before/after
  (dramatic hole-in-wall repair — marketing card but high-impact and
  owned by the business, not stock)
- **gbp-2**: Finished kitchen ceiling corner with new recessed light
- **gbp-3**: Water-damaged ceiling patch with blue painter tape +
  plastic sheeting (paired before)
- **gbp-4**: Open wall showing leak source + shutoff valve + insulation
- **gbp-5**: Crew member on ladder rolling finish coat on ceiling
  with pendant lights wrapped in plastic (painting-side differentiator)
- **gbp-6**: Crew installing cathedral-ceiling drywall framing
  (structural capability differentiator)

Alt text detailed per image, with explicit before/after pairing
language for the water-damage sequence (gbp-2 paired with gbp-3).

## Reviews merged

reviews.json: 0 → 6 Bruce Yelp reviews. All 4-star or higher.

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓ (14 "Done Right Drywall" alt refs)
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `MTJL8654` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Tonight's running total — 27 sites live

1–26 as before +
27. **Done Right Drywall (MTJL8654) — Bruce Yelp 25-photo delivery ✨**

### Still pending Mini processing (Bruce already delivered)

- **pro-gutter-cleaning** — 20 photos + 3 reviews (also needs Unsplash
  hero-bg CSS swap)
- **premier-tv-mounting-atl** — 15 photos, no reviews
- **handy-dandy-atlanta** — 8 carrd.co portfolio photos
- **doctor-concrete-atl** — 0 photos, 9 Angi reviews (reviews-only ship)

Next cycle: pro-gutter-cleaning.

— Mini
