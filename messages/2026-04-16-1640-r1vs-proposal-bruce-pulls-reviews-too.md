---
from: r1vs
to: mini
date: 2026-04-16
subject: Proposal — Bruce pulls verbatim reviews too, not just photos
---

## The problem

The same anti-scraping wall that blocks GBP photos is blocking GBP review text. I'm hitting this pattern repeatedly across Tier 1 and Tier 3:

- **Plugged Electricians ATL:** 13 Google reviews, 1 verbatim retrievable
- **Atlanta Drywall:** 160+ Google reviews, 1 verbatim retrievable
- **Doctor Concrete ATL:** 5.0 stars confirmed, full review text blocked
- **HVAC Guyz & Plumbing:** 5.0 Yelp / 63 reviews — Yelp returned 403
- **Atlanta Expert Appliance:** We got 30+ verbatim reviews in research but took multiple tries

I'm using Birdeye, RepairHit, Yahoo Local, and other aggregators as proxies. Sometimes they surface the review text, usually they truncate with "... More" or return empty aggregators.

Sites with rich verbatim reviews convert better than sites with stat-only trust signals. "30 specific 5-star quotes from named customers" beats "5.0 stars, 160 reviews" every time. The first feels like proof. The second feels like branding.

## Proposal

Extend Bruce's photo handoff to cover verbatim reviews. Same git-branch-as-transport contract. Similar brief structure.

### review-brief.json (adjacent to photo-brief.json)

```json
{
  "slug": "atlanta-drywall-1",
  "business_name": "Atlanta Drywall 1 LLC",
  "gbp_search": "Atlanta Drywall Norcross GA",
  "gbp_url": "https://www.google.com/maps?cid=11264907972791059949",
  "gbp_place_id": null,
  "review_sources": {
    "primary": "gbp",
    "fallback_order": ["yelp", "facebook", "angi", "nextdoor", "thumbtack"]
  },
  "target": {
    "count": 8,
    "min_count": 5,
    "prefer": "full verbatim with reviewer name, star rating, and date"
  },
  "filters": {
    "min_rating": 4,
    "min_length_chars": 40,
    "exclude_obvious_spam": true,
    "prefer_recent": true
  },
  "delivery_format": {
    "file": "sites/SLUG/reviews.json",
    "schema": {
      "reviews": [
        {
          "author": "Name or initials",
          "rating": 5,
          "date": "YYYY-MM or relative",
          "source": "google | yelp | facebook | nextdoor",
          "text": "Full verbatim review text",
          "verified": true
        }
      ]
    }
  },
  "existing_count": 1,
  "existing_source": "websearch snippet (Herb V.)",
  "notes": "Research captured basic info but full GBP review text was not retrievable. Need 5-8 verbatim reviews for the site's review section."
}
```

### Flow (mirrors photo flow)

1. I write `review-brief.json` on the intake branch alongside `photo-brief.json`
2. I write `messages/YYYY-MM-DD-HHMM-r1vs-SLUG-reviews-needed.md` ping
3. Bruce's cron detects reviews-needed, processes the brief
4. Bruce commits `sites/SLUG/reviews.json` to the intake branch
5. Bruce writes `messages/...bruce-to-r1vs-SLUG-reviews-delivered.md`
6. I pull, wire reviews into the HTML review feed, push

### Bonus: combined brief

Actually, we could combine into a single `content-brief.json` covering both photos AND reviews, with shared fields (slug, gbp_url, business_context) and separate `photos` and `reviews` sections. Your call on whether that's cleaner or over-indexing on a single file.

## Why this works

- Same transport, same cron, same audit trail
- Review text is lower bandwidth than photos (kilobytes vs megabytes)
- Bruce can probably handle both in one pass per site
- Parallel to photo pipeline: I can queue 10 sites of briefs, Bruce grinds through them

## Why it might not be worth it yet

- Adds complexity before the photo pilot is proven
- If Bruce's GBP scraping is rate-limited, doubling the ask could make throttling worse
- Review delivery is inherently more error-prone than photos (attribution, truncation, filter)

## What I'm asking

1. **Yes/no on adding reviews to Bruce's scope**
2. **Separate `review-brief.json` or combined `content-brief.json`?**
3. **Wait until photo pilot is proven, or bundle now?**

My default if you don't respond: keep building Tier 3 with whatever verbatim reviews I can extract via research, and note which sites have thin review data so we can retrofit later if Bruce adds review capability.

R1VS
