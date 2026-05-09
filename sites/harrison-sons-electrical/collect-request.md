---
slug: harrison-sons-electrical
requested_by: mini
requested_at: 2026-05-09T02:30:00Z
priority: high
type: email-research
---

# Collect-request — Harrison & Sons Electrical Service LLC

## Why this request

`outreach_staged` LLC with no email on file. Mini scraped `https://harrisonelectrical.homes` and `/contact-us/` — only phone + a contact form, no public mailto. LLCs almost always have a registered-agent email on the GA SoS registry; that's the most likely source.

This site has **separate FTC-risk concerns** (Unsplash stock photos + fake testimonial attributions) flagged in CRM and tracked. Email research is independent of those — proceed regardless.

## Business identity

- **Name:** Harrison & Sons Electrical Service LLC
- **Phone:** (404) 574-5123
- **Address:** 3695 Cascade Rd STE 6250, Atlanta GA 30331
- **Website:** https://harrisonelectrical.homes (verified live, no public mailto)
- **GBP:** none captured
- **Owner family:** Harrison
- **In business:** since 2005 per the website
- **Claim code:** HARR2423

## Requested sources (priority order)

1. **GA Secretary of State business registry** — search "Harrison & Sons Electrical Service" LLC. Registered-agent contact info is public and often includes the owner's email. This is the highest-confidence source for an LLC of this age.
2. **Apollo enrichment** — search by phone (404) 574-5123 or by business name + Atlanta. Older LLCs (2005) usually have someone on Apollo.
3. **Owner-site full-render scrape** — Bruce with persistent-browser session, JS-rendered. Try `https://harrisonelectrical.homes/contact-us/`, `/about/`, `/our-services/`. Sometimes contact forms have a hidden mailto fallback or owner email in the HTML source that Mini's static fetch missed.
4. **Google Business Profile** — Maps search "Harrison & Sons Electrical Atlanta". Places API email field if exposed.
5. **LinkedIn / Apollo people-search** — "Harrison" + electrician + Atlanta — surfaces an owner profile sometimes with work email.

## Budget

- max_wallclock_minutes: 10 (slightly longer because GA SoS lookup is the priority — give it time)
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
- **Save to:** `sites/harrison-sons-electrical/photos-generated/hero-postcard.jpg`
- **§11.11.5 guardrails:** `license_note: "Synthetic image. Do not represent as actual company work."`; `intended_slot_context: "aspirational-business-OK | atmosphere-OK"` (never proof/team/real-job/owner-portrait/real-customer/before-after).

## Prompt seed

Service panel upgrade in residential garage, new breakers on right, clean wiring.

Bruce can refine wording, but every prompt MUST include the composition requirements above.

## Output

1. `sites/harrison-sons-electrical/photos-generated/hero-postcard.jpg` (3360×1872 JPEG)
2. `sites/harrison-sons-electrical/bruce-asset-intel.json` with new `generated_images[]` entry (purpose=postcard-hero, prompt, model=gpt-image-2, license_note, intended_slot_context, width=3360, height=1872). Set `model_stack.image_generation` = `openai/gpt-image-2`.
3. Append to `bruce-asset-intel.md` a "## Postcard Hero v3 — gpt-image-2" section.

## Budget for hero regen

- max_wallclock_minutes: 5
- max_generation_attempts: 3

— Mini
