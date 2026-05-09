---
slug: atl-mobile-mechanics
requested_by: mini
requested_at: 2026-05-09T02:30:00Z
priority: high
type: email-research
---

# Collect-request — ATL Mobile Mechanics (Joseph)

## Why this request

Per Jesse 2026-05-08 directive: every `outreach_staged` prospect needs both email + postcard send capability. ATL Mobile Mechanics is at `outreach_staged` but `prospects.email` is NULL — Send Email button is gated off. This is enrichment work in Bruce's lane (§11) — Mini can't autonomously source contact info.

Owner-operator. Phone-based businesses sometimes have owner email surfaced via Apollo, GA Secretary of State business registry, or social profiles.

## Business identity

- **Name:** ATL Mobile Mechanics
- **Owner:** Joseph
- **Phone:** (470) 809-3146
- **Address:** 8816 Countryside Way, Douglasville GA 30134
- **GBP:** none captured in CRM — Bruce search may surface
- **Existing website:** none captured
- **Claim code:** SVYG3351
- **Note:** same address + phone as `douglasville-mobile-mechanics` (separate prospect, same owner Joseph). Open duplicate-decision flag in CRM is for Jesse — DO NOT mark dead. This collect-request is for email only.

## Requested sources (priority order)

1. **Apollo enrichment** — search by phone (470) 809-3146 OR by business name + city + state (ATL Mobile Mechanics, Douglasville, GA). Apollo often returns owner work email for owner-operated trades.
2. **GA Secretary of State** — `https://ecorp.sos.ga.gov/BusinessSearch/` — search "ATL Mobile Mechanics" or "Mobile Mechanics" in Douglasville. LLC registrations include registered-agent contact info which often has email.
3. **Google Business Profile** — search Google Maps for "ATL Mobile Mechanics Douglasville GA". GBP listing's "Contact" section sometimes exposes email.
4. **Yelp / Nextdoor / Thumbtack / Angi / Facebook** — owner profile pages on these platforms occasionally list email.

## What "found" means

Verified email = an address that's clearly the owner's business contact (not generic CMS noreply, not a random scraped string). Provenance citation in the response file.

## Budget

- max_wallclock_minutes: 8
- max_sources_attempted: 6
- DO NOT scrape photos / reviews — this request is email-only

## Output expected

If found: update Supabase `prospects.email` for slug `atl-mobile-mechanics` with the verified address, set `contact_verified=TRUE`, and add a note with provenance.

If not found: write `messages/<date>-bruce-email-research-blocked-atl-mobile-mechanics.md` with what was tried + failure modes.

— Mini


---

# ALSO REQUESTED — postcard hero regen via gpt-image-2

This prospect ALSO needs a postcard hero regenerated. Both tasks (email research above + hero regen below) should be completed in this single Bruce cycle if possible.

## Hard requirements

- **Dimensions:** 3360×1872 px (multiples of 16, 16:9, postcard print spec)
- **Format:** JPEG, quality 85+, sRGB
- **Provenance:** `model_stack.image_generation` = exactly `openai/gpt-image-2`. No MiniMax, no via-OpenClaw, no hyphen format. If routing returns anything else, do NOT deliver — write a blocked message.
- **Composition:** Visual subject on RIGHT two-thirds (left third may go dark, will be overlaid with text + gradient). No text, no logos, no license plates, no identifiable people. Cinematic photorealistic, warm professional lighting, 16:9 horizontal.
- **Save to:** `sites/atl-mobile-mechanics/photos-generated/hero-postcard.jpg`
- **§11.11.5 guardrails:** `license_note: "Synthetic image. Do not represent as actual company work."`; `intended_slot_context: "aspirational-business-OK | atmosphere-OK"` (never proof/team/real-job/owner-portrait/real-customer/before-after).

## Prompt seed

Hood-up engine bay with hands diagnosing, mobile-mechanic toolbox on right side.

Bruce can refine wording, but every prompt MUST include the composition requirements above.

## Output

1. `sites/atl-mobile-mechanics/photos-generated/hero-postcard.jpg` (3360×1872 JPEG)
2. `sites/atl-mobile-mechanics/bruce-asset-intel.json` with new `generated_images[]` entry (purpose=postcard-hero, prompt, model=gpt-image-2, license_note, intended_slot_context, width=3360, height=1872). Set `model_stack.image_generation` = `openai/gpt-image-2`.
3. Append to `bruce-asset-intel.md` a "## Postcard Hero v3 — gpt-image-2" section.

## Budget for hero regen

- max_wallclock_minutes: 5
- max_generation_attempts: 3

— Mini
