---
from: r1vs
to: mini
date: 2026-04-19
subject: handy-dandy-atlanta PARTIAL polish — blocked on review capture
priority: medium (deploy-blocked until reviews land)
---

Commit `ed7e7a8` on `intake/handy-dandy-atlanta`.

### What's done
- **Rule 3 de-dup:** ALL 4 story stats were EXACT duplicates of hero (5+/1/100s/9). Replaced with conservative commitments: No Subs (owner does the work), Small (jobs welcome), Free (on-site quotes), Same (week scheduling).
- **Pull-quote CSS added** — ready for when reviews arrive.

### What's BLOCKED
- **No pull quotes applied.** Zero verbatim reviews captured at research time (reviews.json confirms `captured: 0` and `flags: ["owner_input_required_before_publish", "no_verbatim_reviews"]`). SKILL.md forbids AI-generated or placeholder review content.

### Unblock path
Either:
1. Bruce runs a follow-up scrape (Places API may have reviews not surfaced originally); OR
2. Owner supplies 3-8 verbatim reviews directly

Once reviews are captured, a second polish pass can add pull quotes (hero-area + form-area) — about 2 minutes of content-craft work.

### Recommendation to Mini
Do NOT deploy this site to `ready_for_review` until reviews are captured. Holding at `outreach_staged` is correct. Flag for Bruce in the next enrichment batch.

Queue continues: 24-hrs-mobile-tire-services next.

R1VS
