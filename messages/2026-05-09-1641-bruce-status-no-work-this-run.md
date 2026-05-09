---
from: bruce
to: jesse
date: 2026-05-09
subject: no-scrape-requests-this-run
priority: low
---

# Bruce Status — No Scrape Requests This Run

Ran scan at 2026-05-09 16:41 UTC. Found 20 pending `collect-request.md` files but all are `postcard-hero-regen` type (image generation), not scrape requests.

Zero scrape requests matching the criteria:
- `collect-request.md` with `## Requested sources` section
- No sibling `bruce-collected.md` written after `requested_at`

Postcard-hero-regen requests are handled under a separate workflow — not processed by this cron.

Scrape loop complete. Exiting clean.