---
slug: atl-mobile-mechanics
requested_by: mini
requested_at: 2026-05-12T22:30:00Z
priority: high
type: review-scrape
---

# Collect-request — Atl Mobile Mechanics (review scrape for site placeholder)

## Why this request

The live site at https://atl-mobile-mechanics.pages.dev has a placeholder block in the reviews section that reads:

> "Reviews are being gathered from Google, Yelp, and fleet clients. Check back shortly — or call Joseph directly to hear about recent jobs."

…and below it:

> "More customer reviews loading."

Jesse is sending postcard outreach to this prospect now. We want real customer reviews in place before Joseph (the owner) clicks through from the postcard and lands on his own site. Right now it looks unfinished even though the rest of the site is solid.

The business has plenty of source material:
- **4.0★ across 171 Google reviews** — pick the strongest 3-5
- Phone: (470) 809-3146 (Joseph, owner; also owns Douglasville Mobile Mechanics)
- Trade: mobile mechanic (engine repair, brakes, diagnostics, etc.)

## What we need

1. **Scrape 3-5 strong real reviews from GBP** for Atl Mobile Mechanics
   - Prefer 5-star reviews
   - Prefer ones with specific job detail ("replaced my alternator," "came to my driveway in Marietta") over generic praise ("great service!")
   - Capture: reviewer name (as displayed on GBP), star rating, review text, source attribution ("Google Review" — no fabricated dates or photos)
2. **Write them to** `sites/atl-mobile-mechanics/bruce-collected.md` under a `## Reviews` section, plus the structured equivalent in `bruce-asset-intel.json` under `reviews[]`
3. **Drop a sentinel** for R1VS to wire them into `index.html` (replace the "More customer reviews loading" placeholder + the loading text in the section header)

## Hard rules

- **No fabricated reviews.** If GBP only has 1 usable 5-star review, deliver that one and a clear note ("only 1 strong review found — keep loading placeholder for remaining slots, or drop section to single quote").
- **No fabricated reviewer attribution.** Use the name as it appears on GBP, or "Google Customer" / "Verified Google Review" if you can't capture a name cleanly. No more "Atlanta Metro Customer" or "Cascade Resident" inventions.
- **Preserve any 4-star content if it includes specific detail** — a real detailed 4-star is more credible than a generic 5-star. Just don't lead with it.

## Output

1. `sites/atl-mobile-mechanics/bruce-collected.md` — append `## Reviews (2026-05-12 scrape)` section with each review as a block:
   ```
   ### "<review excerpt or title>"
   - text: <full review body, verbatim from GBP>
   - reviewer: <name as displayed>
   - rating: <1-5>
   - source: Google Business Profile
   - scraped_at: <ISO timestamp>
   ```
2. `sites/atl-mobile-mechanics/bruce-asset-intel.json` — add a `reviews` array with structured entries (same fields as above, but JSON)
3. Append a one-line "## Review scrape v1 — GBP" section to `sites/atl-mobile-mechanics/bruce-asset-intel.md` summarizing what was delivered

## Budget

- max_wallclock_minutes: 8
- max_reviews_attempted: 5

## When done

R1VS picks up the `bruce-collected.md` delta on next site rebuild and wires the reviews into the HTML.

— Mini
