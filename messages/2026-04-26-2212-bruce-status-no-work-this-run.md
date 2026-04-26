# Bruce Status — photo-brief-processor run

**Time:** 2026-04-26 03:12 PM PT (2026-04-26 22:12 UTC)  
**Repo:** gtmdot-sites @ main (e140a15 — no new commits since prior run)  

## No pending collect-request.md files

All queued requests have been processed. Queue is clean.

## This run summary

Ran full scan — no new `collect-request.md` files appeared on origin/main since last wake at 22:05 UTC. No new slugs to process.

## Current state

- 15 sites with `bruce-collected.md` in the repo (7 total slugs processed across 2 cron runs)
- 0 pending `collect-request.md` files
- Next cron wake will return no-work status until new requests are queued

## Key findings across both runs

1. **SCRAPFLY_API_KEY missing** — blocks Yelp JS-rendered review text; photo extraction works via Firecrawl → S3 download workaround
2. **Google Places** — most reliable photo + review source; used as primary capture for all 7 slugs
3. **Yelp S3 photo download** — format: `https://s3-media0.fl.yelpcdn.com/bphoto/{ref}.jpg` with `curl -L`; ref ends in `/l`
4. **1★ reviews** — pro-gutter-cleaning has T Hayes 1★; flagged in bruce-collected.md for Mini's review carousel exclusion
5. **Limited presence businesses** — sandy-springs-plumber-sewer-septic only 2 GBP photos; no workaround available
6. **GBP photo quality** — generally 100KB–400KB per photo; good quality range