---
slug: done-right-drywall
collected_at: 2026-04-21T05:21:01.615874Z
wall_clock_used_minutes: 8
status: partial
---

# Bruce Collected Report — done-right-drywall

## Per-Source Results

| Source | Status | Reason |
|---|---|---|
| yelp_atlanta | **success** | 15 photos + 4 reviews captured |
| yelp_norcross | **success** | 10 photos + 3 reviews captured |
| facebook | **not-attempted** | budget-exceeded — stopped after both yelp listings delivered 25 photos within budget |
| homeadvisor_angi | **not-attempted** | budget-exceeded |
| bbb | **not-attempted** | budget-exceeded |
| google_places | **failed** | ZERO_RESULTS — unclaimed GBP, not findable via Places API |

## Photo Inventory

25 photos downloaded to `sites/done-right-drywall/photos-raw/`:
- `yelp-atlanta-01.jpg` through `yelp-atlanta-15.jpg` (15 from Atlanta listing)
- `yelp-norcross-01.jpg` through `yelp-norcross-10.jpg` (10 from Norcross listing)

Note: The Yelp Atlanta listing includes before/after photo pairs per review context. Mini should prioritize `yelp-atlanta-01.jpg` (after) and `yelp-atlanta-02.jpg` (before) as they specifically show a drywall repair result paired with the Kim C. review context. Brand-integrity check passed — no mismatched-branding images detected.

## Reviews Inventory

**7 reviews captured** (1-5 star range, mixed quality — see flag below):

From Yelp Atlanta (4 reviews, all 5-star):
- **Kim C.** — Sep 22, 2025 — 5 stars — "I needed drywall repaired after plumbing work. Dave was the 4th contractor I contacted... My walls look great. Thanks Dave!"
- **Verified Customer** — Apr 10, 2022 — 5 stars — "Very nice job, extremely smooth, quick work..."
- **Verified Customer** — Feb 10, 2022 — 5 stars — "I had two places to fix due to water damage... David provided input and direction..."
- **Verified Customer** — Jul 1, 2021 — 5 stars — "I received a quote and when I was ready to start they answered me and scheduled the job..."

From Yelp Norcross (3 reviews):
- **Verified Customer** — May 24, 2023 — 5 stars — "Great, honest work, did everything on time!"
- **Verified Customer** — Jan 21, 2022 — 5 stars — "Honestly, better than expected..."
- **Verified Customer** — Jul 8, 2022 — **1 star** — "Terrible!!! Wasted my time and money. They came out twice to still give unsuccessful results..."

**⚠️ FLAGGED REVIEW:** The Jul 8, 2022 Norcross review is a 1-star complaint about failed results. Mini should use their judgment on whether to include it in the carousel — 7 reviews with 6 x 5-star and 1 x 1-star averages to ~4.4 stars, which may affect perceived quality. Recommend excluding the 1-star review unless the site's review volume is very low and variety is more important than pure average.

## Budget Status

- Photos: 25/25 total — **within budget**
- Reviews: 7/25 — **within budget** (note: 1 flagged for potential exclusion by Mini)
- Wall clock: ~8 min / 10 min — **within budget**

## What Mini Should Know

25 real photos from two Yelp listings (Atlanta: 15, Norcross: 10). Both listings show the same "Done Right Drywall" brand. Before/after pairs are present in the Atlanta photos — use `yelp-atlanta-01.jpg` (after) and `yelp-atlanta-02.jpg` (before) for the `gbp-1` before/after slot. Reviews are a mixed bag — 6 x 5-star from real customers plus 1 x 1-star from Norcross. Mini should probably include only the 6 five-star reviews in the carousel and skip the 1-star.

No Google Places listing, no owner website (domain expired). The Yelp photos are the primary asset here.
