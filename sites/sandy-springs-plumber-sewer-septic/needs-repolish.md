---
slug: sandy-springs-plumber-sewer-septic
signaled_by: mini-integrate-bruce-collected
signaled_at: 2026-04-24T03:33:29.460815+00:00
bruce_collected_at: unknown
reviews_added: 3
photos_added: 2
---

# needs-repolish

Bruce enrichment landed. Mini integrated:
- 3 new reviews into reviews.json
- 2 new photos into photos/inbox/

On your next polish pass, please:
1. Re-render review UI section of index.html per the new counts.captured
   (if previously showing empty-state and now >=3, swap to full track)
2. Decide which photos/inbox/*.* move into gallery slots per intent.json;
   rename appropriately (e.g. photos/inbox/yelp-01.jpg → photos/gbp-4.jpg
   if it fills the 4th gallery slot)
3. Run scripts/pre-push-gate.sh + scripts/verify-build.sh
4. Delete this file when done

Safe to ignore if the site is already shipping at quality. Mini will
re-scan and re-signal on Bruce's next delivery.
