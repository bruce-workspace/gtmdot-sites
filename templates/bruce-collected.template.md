---
slug: REPLACE_ME_SLUG
collected_at: REPLACE_ME_ISO_TIMESTAMP
wall_clock_used_minutes: REPLACE_ME
status: REPLACE_ME  # one of: success | partial | failed
collect_request_ref: REPLACE_ME  # path to the collect-request.md that triggered this run
---

# Bruce Collected Report — REPLACE_ME_SLUG

Drop-in template. Bruce writes this after a collect-request.md run.

## Per-Source Results

| Source | Status | Reason |
|---|---|---|
| REPLACE_ME (yelp.com) | success / failed / not-attempted / partial | (if failed) one of: login-wall, site-blocked, not-found, captcha, rate-limit, timeout, other |
| REPLACE_ME (nextdoor.com) | ... | ... |
| REPLACE_ME (thumbtack.com) | ... | ... |
| ... | ... | ... |

`status` per source values:
- **success** — assets were extracted
- **failed** — source blocked, login-walled, business not found, captcha, etc. Always include a `reason` string.
- **not-attempted** — source listed in collect-request but Bruce didn't try (budget exhausted, deadline hit, or higher-priority source already met targets)
- **partial** — some assets extracted but expected count not hit

## Photo Inventory

REPLACE_ME photos downloaded to `sites/<slug>/photos-raw/`:

- `photos-raw/<source>-01.jpg` — REPLACE_ME bytes — REPLACE_ME (one-line content description if visually inspected)
- `photos-raw/<source>-02.jpg` — REPLACE_ME bytes — REPLACE_ME
- ... etc ...

Naming convention: `<source-slug>-NN.jpg` where source-slug is `yelp`, `nextdoor`, `thumbtack`, `bbb`, `google-cid`, etc.

## Reviews Inventory

REPLACE_ME reviews captured. Full bodies written to `sites/<slug>/reviews-raw.json`.

| Source | Count | Notes |
|---|---|---|
| yelp | REPLACE_ME | REPLACE_ME |
| nextdoor | REPLACE_ME | REPLACE_ME |
| ... | ... | ... |

If 0 reviews captured, state explicitly why (login wall, JS-rendered behind auth, etc.) so the next request knows what to try differently.

## Budget Status

- **Photos:** REPLACE_ME / max — within / over budget
- **Reviews:** REPLACE_ME / max — within / over budget
- **Wall clock:** REPLACE_ME min / max min — within / over budget
- **Scrape attempts (total across all sources):** REPLACE_ME

## What Mini / R1VS Should Know

Free-form notes. Examples of what to surface:

- Photos that don't match the intent contexts (e.g., "yelp-04 through yelp-08 are stock images of generic vehicles, not this business")
- Identity-confirmation issues (e.g., "Yelp listing for the right business name but at a different address — could be wrong business")
- Sources that should be retried with different tooling (e.g., "Nextdoor needs Scrapfly render_js=true — Firecrawl alone returned the loading skeleton")
- Anything that should change the next collect-request

## Tools Used

- **Firecrawl:** REPLACE_ME (e.g., "scraped Yelp biz page; works for Yelp HTML")
- **Scrapfly:** REPLACE_ME (e.g., "render_js=true for Nextdoor; needed country=us routing")
- **Brave Search:** REPLACE_ME (e.g., "snippet-only for review fragments")
- **Direct curl:** REPLACE_ME (e.g., "Google Maps CID lookup")

## Next Steps Mini / R1VS Should Take

- Run `scripts/reviews-merge.py <slug>` to dedupe Bruce's `reviews-raw.json` against existing `reviews.json`
- Run `scripts/render-reviews-bar.py <slug>` to update homepage if review count changed paths (e.g., went from path C empty-state to path A reviews-track)
- Review `photos-raw/*.jpg` and pick the best fit per `data-slot-id` + `data-context` in the HTML (Mini owns this picking + caption-writing per §11)
