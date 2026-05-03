---
slug: done-right-drywall
request_id: 2026-05-03T11:07:51.511301+00:00
collected_at: 2026-05-03T11:24:00.000000+00:00
status: partial
---

# Bruce Collected — done-right-drywall

## Summary
Attempted enrichment run. Photos already at budget cap (15) from previous run. Added 3 Nextdoor reviews via discovery of their Nextdoor page. No new photos collected. BBB profile exists but has no reviews (login/captcha wall).

## Results by source

### yelp — ALREADY-COLLECTED
- 15 photos → sites/done-right-drywall/photos-raw/yelp-NN.jpg (from previous run)
- 1 review → sites/done-right-drywall/reviews-raw.json (from previous run)
- Notes: No re-scrape needed; budget already consumed

### nextdoor — SUCCESS (new)
- 0 photos (none found on page, no direct image assets)
- 3 reviews → appended to reviews-raw.json
- Discovered via: https://nextdoor.com/pages/done-right-drywall-repair-atlanta-ga/
- Reviews extracted: Brett E., Jeremy J., Brandon V. (all 5-star dated 2020)

### thumbtack — NOT-FOUND
- 0 photos
- 0 reviews
- Notes: No pro profile found for "Done Right Drywall" Atlanta GA. Thumbtack returned 404 on attempted search URL. Moving on.

### bbb — NO-REVIEWS
- 0 photos
- 0 reviews
- Notes: BBB profile exists (https://www.bbb.org/us/ga/atlanta/profile/construction-services/done-right-drywall-repair-0443-28131157) but has 0 customer reviews. Business is NOT BBB Accredited. reCAPTCHA wall on page — not worth fighting. Moving on.

## Totals (cumulative across all collect runs)
- Photos collected: 15 (unchanged from previous run)
- Reviews collected: 4 total (1 Yelp + 3 Nextdoor)
- Wall-clock used: ~2 minutes

## Budget status
- Photos: at cap (15/15) — no more photo collection until a future run with higher budget
- Reviews: 4/30 — well under budget, no further collection needed unless future run adds more

## Next steps for Mini
- No new photos to integrate
- 4 reviews now available (above 3-review render threshold)
- re-run pre-push-gate.sh + verify-build.sh before deploy