---
from: jesse
to: bruce
date: 2026-04-19
subject: Handy Dandy Atlanta — please retry Places API scrape for reviews
priority: medium (unblocks final polish on this site)
---

## Request

Please run a fresh Places API scrape on `handy-dandy-atlanta` to capture verbatim reviews. The initial research pass captured 0 reviews (reviews.json confirms `captured: 0`), which has been blocking the content-craft polish — no pull quotes possible without real reviewer content per SKILL.md.

## Context

More of the pipeline is built out now than when this site was first researched. The Places API + Firecrawl + direct-scrape combinations you're running on the tier-2 enrichment batch have been producing richer captures than the initial pass. Worth trying handy-dandy again with the current tooling.

## What the site needs

- 3-8 verbatim Google reviews with:
  - Real reviewer names (or whatever the API surfaces — "Google Customer" is fine if that's the verbatim return)
  - Actual review text, not paraphrased
  - Date strings
  - Ideally at least 1 review that names a specific tech / owner / job type (for pull quote material)

Once the reviews land in `sites/handy-dandy-atlanta/reviews.json`, R1VS can add the two pull quotes on the next pass (~5 min of content-craft work per DESIGN-HEURISTICS.md §3).

## Business basics (for reference)

- Phone: (404) 919-3833
- Atlanta-based handyman
- HTML references 5+ years operating
- Flag set on reviews.json: `["owner_input_required_before_publish", "no_verbatim_reviews"]`

If the Places API still blocks after a fresh retry, flag it and I'll reach out to the owner directly for screenshots of their best 5 reviews.

Thanks.

Jesse
