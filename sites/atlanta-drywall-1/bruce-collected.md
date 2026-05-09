---
slug: atlanta-drywall-1
collected_at: 2026-05-09T02:30:43Z
wall_clock_used_minutes: 9
status: partial
collect_request_ref: sites/atlanta-drywall-1/collect-request-archive/collect-request.md
---

# Bruce Collected Report — atlanta-drywall-1

## Per-Source Results

| Source | Status | Reason |
|---|---|---|
| Owner site direct fetch | failed | not-found — homepage/contact/about/contact-us fetched HTTP 200, no email found |
| Google Business Profile / Places API | failed | not-found — matched Places record, but Places Details exposes no email field |
| Apollo | failed | login-wall — no Apollo API key/session available |
| GA Secretary of State | failed | unknown — SOS endpoint returned HTTP 404 on single attempt |
| Yelp / Nextdoor / Thumbtack / Angi | failed | unknown — Brave API directory search returned HTTP 422 on single attempt |
| Postcard hero generation | success | `photos-generated/hero-postcard.jpg` generated with `openai/gpt-image-2` |

## Email Research Summary

Email found: **none**.

Details written to `sites/atlanta-drywall-1/email-research.md`.

## Photo Inventory

Generated postcard hero:

- `photos-generated/hero-postcard.jpg` — 3360×1872 JPEG, quality 90, synthetic aspirational finished-drywall interior with recessed lighting and room-corner detail on the right two-thirds.

No raw business photos were requested or downloaded in this run.

## Reviews Inventory

0 reviews captured. Review collection was not part of this collect-request.

## Budget Status

- **Email research:** 5 source groups attempted / 5 requested — within budget
- **Generated images:** 1 / max 3 attempts — within budget
- **Wall clock:** ~9 min / max 13 min — within budget
- **Scrape/search attempts:** 5 source groups, one attempt each

## What Mini / R1VS Should Know

No email was found. Do not write an email to Supabase from this run.

The postcard hero is synthetic and should only be used as aspirational atmosphere. Do not represent it as Atlanta Drywall 1 project work.

`bruce-asset-intel.json` has `model_stack.image_generation` set exactly to `openai/gpt-image-2` and includes the generated image entry requested.

## Tools Used

- **Direct fetch:** owner site pages and GA SOS endpoint
- **Google Places API:** business match and details lookup
- **Brave Search API:** attempted directory/email search
- **OpenAI image generation:** `openai/gpt-image-2` for postcard hero
- **Pillow:** resized/cropped generated image to 3360×1872 JPEG

## Next Steps Mini / R1VS Should Take

- Use `photos-generated/hero-postcard.jpg` for the postcard hero slot only.
- Keep the synthetic-image license note attached wherever this asset is tracked.
- If email is still required, try a logged-in Apollo account or manual GA SOS interactive search next.
