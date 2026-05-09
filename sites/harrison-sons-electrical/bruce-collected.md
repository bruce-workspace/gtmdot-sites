---
slug: harrison-sons-electrical
request_id: 2026-05-09T02:30:00Z
collected_at: 2026-05-09T02:31:58Z
collector: bruce
status: partial
---

# Bruce Collected — Harrison & Sons Electrical Service LLC

## Summary

Completed the email research waterfall and generated the postcard hero. No verified email was found. The postcard hero was generated with `openai/gpt-image-2`, resized to the required print spec, and saved in `photos-generated/`.

## Email research results

### GA Secretary of State business registry — FAILED
- Reason code: `blocked-by-robots-txt`
- Detail: Direct registry lookup returned HTTP 403; browser navigation was blocked by policy. No retry or bypass attempted.

### Apollo enrichment — FAILED
- Reason code: `login-wall`
- Detail: No authenticated Apollo enrichment surface/API available in runtime. Public exact-match search did not surface an email.

### Owner-site full-render scrape — FAILED
- Reason code: `not-found`
- Detail: Firecrawl JS rendering and static fetch found phone, address, and contact form only across `/contact-us/`, `/about/`, and `/our-services/`. No email or mailto.

### Google Business Profile / Places API — FAILED
- Reason code: `not-found`
- Detail: Places API confirmed the business listing and details, but no email was exposed. Place ID: `ChIJG6FR32Mf9YgRP06hlpa90jg`.

### LinkedIn / Apollo people-search — FAILED
- Reason code: `not-found`
- Detail: Public LinkedIn search returned unrelated/weak Harrison electrician results; no confident owner profile or email.

## Email handoff

- Verified email: none found
- Supabase write: not performed by Bruce

## Postcard hero

- Status: success
- File: `sites/harrison-sons-electrical/photos-generated/hero-postcard.jpg`
- Dimensions: 3360×1872 px
- Format: JPEG, quality 92, RGB/sRGB-compatible
- Model stack: `openai/gpt-image-2`
- Guardrail license note: Synthetic image. Do not represent as actual company work.
- Intended slot context: aspirational-business-OK | atmosphere-OK
- QA: Vision check passed against composition and exclusion requirements.

## Files written

- `sites/harrison-sons-electrical/email-research.md`
- `sites/harrison-sons-electrical/photos-generated/hero-postcard.jpg`
- `sites/harrison-sons-electrical/bruce-asset-intel.json`
- `sites/harrison-sons-electrical/bruce-asset-intel.md`
- `sites/harrison-sons-electrical/bruce-collected.md`
