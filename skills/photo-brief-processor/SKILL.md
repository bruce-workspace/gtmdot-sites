---
name: photo-brief-processor
description: "Autonomous scrape loop for collecting photos and reviews from external sources based on collect-request.md files."
---

# Photo Brief Processor

This skill automates the process of collecting photos and reviews for `gtmdot-sites` based on `collect-request.md` files.

## Workflow

1.  **Repository Sync**: Pulls the latest changes from `origin/main` of the `gtmdot-sites` repository.
2.  **Scan for Requests**: Identifies pending `collect-request.md` files that do not have a corresponding `bruce-collected.md` file.
3.  **Process Requests**: For each pending request (max 3 per run):
    a.  Reads `collect-request.md` YAML frontmatter and body.
    b.  Adheres to source priority and budget caps (`max_photos_total`, `max_reviews_total`, `max_wallclock_minutes`).
    c.  Scrapes data from various sources (yelp.com, nextdoor.com, thumbtack.com, facebook.com, bbb.org, owner website) using Scrapfly, Brave Search, or Firecrawl. Each source is attempted once.
    d.  Saves raw photos to `sites/<slug>/photos-raw/<source>-NN.jpg` and appends reviews to `sites/<slug>/reviews-raw.json`.
    e.  Handles scrape failures (captcha, login-wall, rate-limit, 5xx, timeout, not-found, budget-exceeded, blocked-by-robots-txt) by marking the source as failed and moving to the next.
4.  **Generate Report**: After all sources are attempted or budget is hit, creates `sites/<slug>/bruce-collected.md` with per-source results, totals, and a final status.
5.  **Archive Request**: Moves the processed `collect-request.md` to `sites/<slug>/collect-request-archive/`.
6.  **Commit Changes**: Commits all changes for the processed slug and pushes to `origin/main`.
7.  **Loop/Exit**: Continues to the next pending request or exits with a status message if no more requests are found.

## Strict Rules (Bruce DOES NOT)

-   Touch HTML, CSS, or any file under `sites/<slug>/` except `photos-raw/`, `reviews-raw.json`, `bruce-collected.md`, and the `collect-request` archive.
-   Write captions, alt text, or modify image content.
-   Apply CSS filters or crop images.
-   Write to Supabase.
-   Register claim codes or deploy.
-   Retry failed scrapes. One attempt per source per request.
-   Invoke self — only runs in response to a `collect-request.md`.
-   Touch `.env` or config files.

## Failure Reason Codes

-   `captcha`
-   `login-wall`
-   `rate-limited`
-   `not-found`
-   `server-error`
-   `timeout`
-   `budget-exceeded`
-   `blocked-by-robots-txt`
-   `unknown`

## API Keys

-   `SCRAPFLY_API_KEY`
-   `BRAVE_API_KEY`
-   `FIRECRAWL_API_KEY`
-   `GOOGLE_MAPS_API_KEY` (prefer not to re-use)

## Operational Context

This skill will read the following documents at session start to ensure it operates within defined parameters:

-   `~/.openclaw/workspace/gtmdot-sites/HANDOFF-CONTRACT.md` — especially §11 (new)
-   `~/.openclaw/workspace/gtmdot-sites/CLAUDE.md`
