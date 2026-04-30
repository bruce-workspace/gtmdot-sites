---
slug: sumptuous-mobile-detailing
collected_at: 2026-04-30T10:52:54Z
wall_clock_used_minutes: 0.77
status: partial
collect_request_ref: sites/sumptuous-mobile-detailing/collect-request-archive/2026-04-30-request.md
---

# Bruce Collected Report — sumptuous-mobile-detailing

## Per-Source Results

| Source | Status | Reason | Photos | Reviews | URL |
|---|---:|---|---:|---:|---|
| yelp.com | **failed** | other | 0 | 0 | https://www.yelp.com/biz/sumptuous-mobile-detailing-suwanee |
| nextdoor.com | **failed** | captcha | 0 | 0 | https://nextdoor.com/search/?query=Sumptuous%20Mobile%20Detailing%20Suwanee%20GA |
| thumbtack.com | **failed** | captcha | 0 | 0 | https://www.thumbtack.com/search?query=Sumptuous%20Mobile%20Detailing%20Suwanee%20GA |
| bbb.com | **failed** | captcha | 0 | 0 | https://www.bbb.org/search?find_country=USA&find_text=Sumptuous%20Mobile%20Detailing%20Suwanee%20GA |

## Photo Inventory

0 new photos downloaded from the requested priority sources during this run.

Existing raw photos retained from the earlier Google Places collection:

- `photos-raw/gbp-01.jpg` — 139,230 bytes — pre-existing Google Places photo from prior collection run; retained, no new priority-source photos downloaded in this run.
- `photos-raw/gbp-02.jpg` — 369,179 bytes — pre-existing Google Places photo from prior collection run; retained, no new priority-source photos downloaded in this run.
- `photos-raw/gbp-03.jpg` — 174,836 bytes — pre-existing Google Places photo from prior collection run; retained, no new priority-source photos downloaded in this run.
- `photos-raw/gbp-04.jpg` — 204,795 bytes — pre-existing Google Places photo from prior collection run; retained, no new priority-source photos downloaded in this run.
- `photos-raw/gbp-05.jpg` — 185,468 bytes — pre-existing Google Places photo from prior collection run; retained, no new priority-source photos downloaded in this run.

## Reviews Inventory

0 new reviews captured from the requested priority sources during this run. Existing `reviews-raw.json` was preserved with 5 Google Places reviews from the prior successful run.

| Source | Count | Notes |
|---|---:|---|
| yelp | 0 | Scrapfly returned HTTP 504 / Datadome shield failure on the known Yelp listing. |
| nextdoor | 0 | Scrapfly rendered a captcha / bot-detection page. |
| thumbtack | 0 | Scrapfly rendered a captcha / bot-detection page. |
| bbb | 0 | Scrapfly rendered a captcha / bot-detection page. |

## Budget Status

- **Photos:** 0 new / 15 max — within budget
- **Reviews:** 0 new / 30 max — within budget
- **Wall clock:** 0.77 min / 10 min — within budget
- **Scrape attempts:** 4 priority sources attempted once each

## What Mini / R1VS Should Know

Yelp does have a likely matching listing at `https://www.yelp.com/biz/sumptuous-mobile-detailing-suwanee`; Brave shows "103 Photos" in the snippet. Scrapfly could not get past Yelp's Datadome shield in this run, so no Yelp assets were downloaded.

Nextdoor, Thumbtack, and BBB were attempted once each as requested and stopped at captcha/bot-detection pages. No bypass attempted.

The prior Google Places assets and reviews remain the usable collection for this slug unless Mini wants a manual/browser-based Yelp pass later.

## Tools Used

- **Scrapfly:** attempted Yelp, Nextdoor, Thumbtack, and BBB with `country=us`; `render_js=true` for Yelp/Nextdoor/Thumbtack
- **Brave Search:** confirmed the likely Yelp listing and snippet metadata
- **Direct curl:** not used for new downloads because no source photo URLs were extracted

## Next Steps Mini / R1VS Should Take

- Use the existing `photos-raw/gbp-*.jpg` and `reviews-raw.json` from the prior Google Places collection.
- Retry Yelp only if manual browser access or a stronger Yelp-specific fetch path is available; Scrapfly public datacenter routing hit Datadome here.
