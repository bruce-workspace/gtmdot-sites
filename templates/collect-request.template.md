---
slug: REPLACE_ME_SLUG
requested_at: REPLACE_ME_ISO_TIMESTAMP
requested_by: REPLACE_ME_REQUESTER  # one of: r1vs | mini
deadline: REPLACE_ME_ISO_TIMESTAMP  # abandon after this; pipeline assumes failed if Bruce hasn't responded
priority: normal  # one of: normal | high
---

# Collect Request — REPLACE_ME_BUSINESS_NAME

Drop-in template. Copy to `sites/<slug>/collect-request.md` when R1VS or Mini
needs Bruce to scrape additional sources beyond Google Places API.

## Business context

Fill in everything Bruce needs to find the business on alternative sources.

- **Name:** REPLACE_ME (full legal name as it appears on Yelp / Nextdoor / etc.)
- **Trade:** REPLACE_ME (HVAC / plumbing / drywall / etc. — helps disambiguate)
- **Owner:** REPLACE_ME (if known — speeds up identity confirmation)
- **Address:** REPLACE_ME (full street address)
- **Phone:** REPLACE_ME (E.164 format, e.g. +14045551234)
- **Website:** REPLACE_ME (or "none" — Bruce uses this to cross-confirm identity)
- **Key differentiator:** REPLACE_ME (one phrase that uniquely identifies this business — "fire-truck specialist" is better than "auto repair")
- **GBP place_id (if known):** REPLACE_ME (skip if Google Places returned ZERO_RESULTS — explicitly note that)

## Current state — what we have and what's missing

| Artifact | Status | Notes |
|---|---|---|
| photos/hero.jpg | missing / present | what's referenced in HTML |
| photos/gbp-1.jpg ... gbp-6.jpg | missing N / present N | which slots are unfilled |
| reviews.json | captured 0 / 1-2 / >=3 | path A/B/C currently rendered |
| RESEARCH.md | written / skipped | optional |
| gbp_snapshot.json | present | Bruce can read for cross-reference |

State the **specific slot targets** Bruce should focus on (use the `data-slot-id` and `data-context` from the index.html / per-service pages):
- `HERO`: REPLACE_ME (e.g., "technician in action — owner-portrait-OK | service-van-OK")
- `GALLERY_1`: REPLACE_ME
- ... etc through `GALLERY_6` and `ABOUT_PHOTO` ...

## Why we need Bruce (what we've already tried)

Be explicit so Bruce doesn't re-scrape the same dead sources.

- **Google Places API:** REPLACE_ME (e.g., "ZERO_RESULTS for name+address — likely unclaimed GBP" OR "captured 5 reviews + 6 photos but need more")
- **Owner website:** REPLACE_ME (e.g., "GoDaddy template with stock imagery only" OR "no website")
- **Direct Firecrawl scrape:** REPLACE_ME (e.g., "Yelp returned login wall" OR "not attempted")
- **Other sources:** REPLACE_ME

## Requested sources (priority order)

Bruce should attempt these in order. Skip ones we've already exhausted.

1. **REPLACE_ME (e.g., yelp.com)** — REPLACE_ME (search hint, e.g., "search 'BizName City' or phone NNN-NNN-NNNN. Expected count per source if known.") — **primary target**
2. **REPLACE_ME (e.g., nextdoor.com)** — REPLACE_ME
3. **REPLACE_ME (e.g., thumbtack.com)** — REPLACE_ME
4. **REPLACE_ME (e.g., bbb.org)** — REPLACE_ME (note: BBB usually has reviews + complaints, not photos)
5. **Google Maps CID lookup via Scrapfly** — only if Places API returned ZERO_RESULTS

## What to collect

### Photos
- Target count: REPLACE_ME (e.g., 6 — minimum to fill all slots)
- Match against intent: see `Current state` table above for slot-specific contexts
- Skip: blurry, screenshots of documents, irrelevant images, other businesses' work, stock images

### Reviews
- Target count: REPLACE_ME (e.g., 5 minimum to clear the captured>=3 threshold)
- Verbatim only: NEVER summarize, paraphrase, or fabricate
- Required fields per review: `author`, `rating`, `date` (ISO), `source`, `text`
- Reviewer-name slot must NEVER contain: "Google Customer", "Angi Customer", "Verified Homeowner", "Company Mission", "Our Story" (pre-push-gate enforces — fabrication detected on the build side will reject the build)

## Budget caps (HARD LIMITS)

Bruce stops at the first cap hit and reports `status: partial`.

- **max_photos:** REPLACE_ME (default: 15 — covers 6 slots with backups)
- **max_reviews:** REPLACE_ME (default: 20 — easily exceeds the captured>=3 threshold)
- **max_wall_clock_minutes:** REPLACE_ME (default: 10 — keeps Bruce queue moving)
- **max_scrape_attempts_per_source:** REPLACE_ME (default: 2 — retry once on transient failure, then move on)

## Success criteria

- **success:** every requested source attempted, both targets met (>= target_photos and >= target_reviews), no budget exceeded
- **partial:** at least 1 source returned usable assets but at least one target missed
- **failed:** all requested sources blocked / not-found / login-walled

Even `partial` is useful — Mini can decide whether to ship as-is or escalate to Recraft/manual.

## Output expected from Bruce

Bruce writes `sites/<slug>/bruce-collected.md` with the standard format
(frontmatter + per-source table + photo inventory + reviews inventory + budget
status + free-form notes for Mini). See `templates/bruce-collected.template.md`.

Photos drop into `sites/<slug>/photos-raw/<source>-NN.jpg`.
Reviews append to `sites/<slug>/reviews-raw.json` with full schema.

## After Bruce returns

R1VS or Mini runs `scripts/reviews-merge.py <slug>` to dedupe + rank Bruce's
raw output against existing `reviews.json` and produce a unified file. Then
re-run `scripts/render-reviews-bar.py <slug>` to update the homepage with
the now-larger review count.
