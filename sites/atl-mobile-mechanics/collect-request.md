---
slug: atl-mobile-mechanics
requested_by: mini
requested_at: 2026-05-13T02:30:00Z
priority: high
type: review-scrape
---

# Collect-request — Atl Mobile Mechanics (review scrape, re-filed)

## Why this request

The live site at https://atl-mobile-mechanics.pages.dev has a placeholder block in the reviews section:

> "Reviews are being gathered from Google, Yelp, and fleet clients. Check back shortly — or call Joseph directly to hear about recent jobs."
> "More customer reviews loading."

Atl Mobile Mechanics postcards have been sent. When Joseph (the owner) clicks through from the postcard, he should land on real reviews — not a placeholder.

Source material is plentiful:
- **4.0★ across 171 Google reviews** — pick the strongest 3-5
- Phone: (470) 809-3146 (Joseph, owner; also owns Douglasville Mobile Mechanics)
- Trade: mobile mechanic (engine repair, brakes, diagnostics, mobile fleet service)

## Note on re-filing

This collect-request was originally filed in commit `68a3b4b` (2026-05-12 evening) and was accidentally overwritten by Mini's site-hero-swap batch (commit `ed07767`). Codex spotted the gap in the queue and Mini is re-filing it intact. Apologies for the noise.

## What we need

1. **Scrape 3-5 strong real reviews from GBP** for Atl Mobile Mechanics
   - Prefer 5-star reviews
   - Prefer ones with specific job detail ("replaced my alternator," "came to my driveway in Marietta") over generic praise ("great service!")
   - Capture: reviewer name (as displayed on GBP), star rating, review text, source attribution ("Google Review" — no fabricated dates or photos)
2. **Write them to** `sites/atl-mobile-mechanics/bruce-collected.md` under a `## Reviews` section, plus the structured equivalent in `bruce-asset-intel.json` under `reviews[]`
3. **Drop a sentinel** in `messages/` for Mini to wire them into `index.html` (replace the "More customer reviews loading" placeholder + the loading text in the section header) — note: per Jesse's lane clarification, the HTML wiring is Mini's lane, not R1VS's

## Hard rules (no fabrication)

- **No fabricated reviews.** If GBP only has 1 usable 5-star review, deliver that one with a note explaining the gap.
- **No fabricated reviewer attribution.** Use the name as it appears on GBP, or "Google Customer" / "Verified Google Review" if you can't capture a name cleanly. Do not invent attributions like "Atlanta Metro Customer" or "Cascade Resident."
- **Preserve detailed 4-star reviews** — a real detailed 4-star is more credible than a generic 5-star. Don't lead with it, but don't reject it either.

## Output

1. `sites/atl-mobile-mechanics/bruce-collected.md` — append `## Reviews (2026-05-13 scrape)` section with each review as a block:
   ```
   ### "<review excerpt or title>"
   - text: <full review body, verbatim from GBP>
   - reviewer: <name as displayed>
   - rating: <1-5>
   - source: Google Business Profile
   - scraped_at: <ISO timestamp>
   ```
2. `sites/atl-mobile-mechanics/bruce-asset-intel.json` — add a `reviews` array with structured entries (same fields as above, but JSON)
3. Append a one-line "## Review scrape v1 — GBP" section to `sites/atl-mobile-mechanics/bruce-asset-intel.md`
4. Drop a sentinel `messages/2026-05-13-bruce-reviews-delivered-atl-mobile-mechanics.md` so Mini knows to wire them in

## Budget

- max_wallclock_minutes: 8
- max_reviews_attempted: 5

— Mini (re-filed after accidental overwrite; original intent commit 68a3b4b)
