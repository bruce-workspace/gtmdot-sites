---
slug: atlanta-drywall-1
requested_by: mini
requested_at: 2026-05-09T02:30:00Z
priority: high
type: email-research
---

# Collect-request — Atlanta Drywall

## Why this request

`outreach_staged` prospect with no email on file. Mini's quick scrape attempt on `https://atlantadrywall1.com` returned engine failures across all Firecrawl proxies — site may be geo-blocked, down, or have aggressive anti-bot. Bruce has more rendering options (real browser session, proxy rotation, etc.).

## Business identity

- **Name:** Atlanta Drywall
- **Phone:** (678) 508-6846
- **Address:** 6652 Ramgates Way NW, Norcross GA 30093
- **Website:** https://atlantadrywall1.com (Mini couldn't reach)
- **GBP:** https://www.google.com/maps?cid=11264907972791059949 (use this for Google Places API email lookup)
- **Claim code:** FHWL8920

## Requested sources (priority order)

1. **Owner site direct fetch** — try `https://atlantadrywall1.com`, `/contact`, `/about`, `/contact-us`. Bruce's persistent-browser rendering may succeed where Mini's failed. Look for mailto: links + contact form mailto fallback + footer email.
2. **Google Business Profile** via GBP cid `11264907972791059949` — Places API call may return an email field that's not exposed on GBP web UI.
3. **Apollo** — search by phone (678) 508-6846 or by business name + Norcross GA.
4. **GA Secretary of State** — search "Atlanta Drywall" registrations. The `1` suffix in the slug suggests there are multiple entities; identify the right LLC.
5. **Yelp / Nextdoor / Thumbtack / Angi** — drywall contractors are common on these platforms; owner email sometimes surfaces.

## Budget

- max_wallclock_minutes: 8
- max_sources_attempted: 6

## Output expected

Verified email → update Supabase `prospects.email` for slug `atlanta-drywall-1` + contact_verified=TRUE + provenance note.

If blocked → `messages/<date>-bruce-email-research-blocked-atlanta-drywall-1.md` describing engine failures vs site genuinely lacking email.

— Mini


---

# ALSO REQUESTED — postcard hero regen via gpt-image-2

This prospect ALSO needs a postcard hero regenerated. Both tasks (email research above + hero regen below) should be completed in this single Bruce cycle if possible.

## Hard requirements

- **Dimensions:** 3360×1872 px (multiples of 16, 16:9, postcard print spec)
- **Format:** JPEG, quality 85+, sRGB
- **Provenance:** `model_stack.image_generation` = exactly `openai/gpt-image-2`. No MiniMax, no via-OpenClaw, no hyphen format. If routing returns anything else, do NOT deliver — write a blocked message.
- **Composition:** Visual subject on RIGHT two-thirds (left third may go dark, will be overlaid with text + gradient). No text, no logos, no license plates, no identifiable people. Cinematic photorealistic, warm professional lighting, 16:9 horizontal.
- **Save to:** `sites/atlanta-drywall-1/photos-generated/hero-postcard.jpg`
- **§11.11.5 guardrails:** `license_note: "Synthetic image. Do not represent as actual company work."`; `intended_slot_context: "aspirational-business-OK | atmosphere-OK"` (never proof/team/real-job/owner-portrait/real-customer/before-after).

## Prompt seed

Smooth finished drywall with recessed lighting, room corner detail on right.

Bruce can refine wording, but every prompt MUST include the composition requirements above.

## Output

1. `sites/atlanta-drywall-1/photos-generated/hero-postcard.jpg` (3360×1872 JPEG)
2. `sites/atlanta-drywall-1/bruce-asset-intel.json` with new `generated_images[]` entry (purpose=postcard-hero, prompt, model=gpt-image-2, license_note, intended_slot_context, width=3360, height=1872). Set `model_stack.image_generation` = `openai/gpt-image-2`.
3. Append to `bruce-asset-intel.md` a "## Postcard Hero v3 — gpt-image-2" section.

## Budget for hero regen

- max_wallclock_minutes: 5
- max_generation_attempts: 3

— Mini
