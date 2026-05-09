---
slug: done-right-drywall
requested_by: mini
requested_at: 2026-05-09T02:30:00Z
priority: high
type: email-research
---

# Collect-request — Done Right Drywall

## Why this request

`outreach_staged` prospect with no email on file. No website captured in CRM. Phone + address only. Need Apollo / registry / social-profile lookups.

## Business identity

- **Name:** Done Right Drywall
- **Phone:** (404) 903-3346
- **Address:** 228 Triumph Dr NW, Atlanta GA 30327
- **Website:** none captured
- **GBP:** none captured — Bruce search may surface
- **Claim code:** MTJL8654

## Requested sources (priority order)

1. **Apollo enrichment** — search by phone (404) 903-3346 or "Done Right Drywall" + Atlanta GA. Owner email if available.
2. **GA Secretary of State** — `https://ecorp.sos.ga.gov/BusinessSearch/` for "Done Right Drywall" LLC registration.
3. **Google Business Profile** — Maps search for "Done Right Drywall Atlanta". Check Places API for email field.
4. **Yelp / Nextdoor / Thumbtack / Angi / Facebook** — drywall contractor profiles often have email.

## Budget

- max_wallclock_minutes: 8
- max_sources_attempted: 6

## Output expected

Verified email → update Supabase + provenance note. Else block message.

— Mini


---

# ALSO REQUESTED — postcard hero regen via gpt-image-2

This prospect ALSO needs a postcard hero regenerated. Both tasks (email research above + hero regen below) should be completed in this single Bruce cycle if possible.

## Hard requirements

- **Dimensions:** 3360×1872 px (multiples of 16, 16:9, postcard print spec)
- **Format:** JPEG, quality 85+, sRGB
- **Provenance:** `model_stack.image_generation` = exactly `openai/gpt-image-2`. No MiniMax, no via-OpenClaw, no hyphen format. If routing returns anything else, do NOT deliver — write a blocked message.
- **Composition:** Visual subject on RIGHT two-thirds (left third may go dark, will be overlaid with text + gradient). No text, no logos, no license plates, no identifiable people. Cinematic photorealistic, warm professional lighting, 16:9 horizontal.
- **Save to:** `sites/done-right-drywall/photos-generated/hero-postcard.jpg`
- **§11.11.5 guardrails:** `license_note: "Synthetic image. Do not represent as actual company work."`; `intended_slot_context: "aspirational-business-OK | atmosphere-OK"` (never proof/team/real-job/owner-portrait/real-customer/before-after).

## Prompt seed

Tape-and-mud detail on residential drywall, professional finish, work area on right.

Bruce can refine wording, but every prompt MUST include the composition requirements above.

## Output

1. `sites/done-right-drywall/photos-generated/hero-postcard.jpg` (3360×1872 JPEG)
2. `sites/done-right-drywall/bruce-asset-intel.json` with new `generated_images[]` entry (purpose=postcard-hero, prompt, model=gpt-image-2, license_note, intended_slot_context, width=3360, height=1872). Set `model_stack.image_generation` = `openai/gpt-image-2`.
3. Append to `bruce-asset-intel.md` a "## Postcard Hero v3 — gpt-image-2" section.

## Budget for hero regen

- max_wallclock_minutes: 5
- max_generation_attempts: 3

— Mini
