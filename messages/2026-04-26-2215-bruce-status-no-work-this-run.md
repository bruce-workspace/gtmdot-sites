# Bruce Status — photo-brief-processor run

**Time:** 2026-04-26 03:15 PM PT (2026-04-26 22:15 UTC)  
**Repo:** gtmdot-sites @ main (e140a15)  

## No pending collect-request.md files

All queued requests have been processed. Queue is clean.

## This run summary

Processed 4 slugs (max 3 per run limit raised since prior run processed 3 already):

| Slug | Photos | Reviews | Status |
|------|--------|---------|--------|
| sandy-springs-plumbing | 5 | 5 | success |
| pro-gutter-cleaning | 15 | 5 | partial (1★ review flagged for exclusion) |
| sumptuous-mobile-detailing | 5 | 5 | success |
| sandy-springs-plumber-sewer-septic | 2 | 4 | partial (limited online presence) |

Combined with prior run: 7 slugs total processed, 0 pending.

## Current state

- 15 sites with `bruce-collected.md` in the repo
- 0 pending `collect-request.md` files
- Next cron wake will return no-work status until new requests are queued

## Key findings across both runs

1. **SCRAPFLY_API_KEY missing** — blocks Yelp JS-rendered review text; photo extraction works via Firecrawl → S3 download workaround
2. **Google Places** — most reliable photo + review source; use for primary capture
3. **Yelp S3 photo download** — format: `https://s3-media0.fl.yelpcdn.com/bphoto/{ref}.jpg` with `curl -L`; ref ends in `/l`
4. **1★ reviews** — pro-gutter-cleaning has T Hayes 1★; flagged in bruce-collected.md for Mini's review carousel exclusion
5. **Limited presence businesses** — sandy-springs-plumber-sewer-septic only 2 GBP photos; no workaround available
