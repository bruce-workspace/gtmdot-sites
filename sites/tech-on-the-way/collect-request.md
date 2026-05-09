---
slug: tech-on-the-way
requested_by: mini
requested_at: 2026-05-09T02:45:00Z
priority: high
type: postcard-hero-regen
---

# Collect-request — Tech On The Way (postcard hero regen via gpt-image-2)

## Why this request

Per Jesse 2026-05-08 directive: tech-on-the-way reset from `outreach_sent` back to `outreach_staged` for fresh re-enrollment in email seq + postcard. Now part of the 13-prospect outreach_staged batch Jesse wants out the door tomorrow.

Existing hero is 1600×1200 — below the 3000×1700 print spec. Needs gpt-image-2 regen at 3360×1872.

## Hard requirements

- **Dimensions:** 3360×1872 px (multiples of 16, 16:9, postcard print spec)
- **Format:** JPEG, quality 85+, sRGB
- **Provenance:** `model_stack.image_generation` = exactly `openai/gpt-image-2`. No MiniMax, no via-OpenClaw, no hyphen format. If routing returns anything else, do NOT deliver.
- **Composition:** Visual subject on RIGHT two-thirds (left third may go dark, will be overlaid with text + gradient). No text, no logos, no license plates, no identifiable people. Cinematic photorealistic, warm professional lighting, 16:9 horizontal.
- **Save to:** `sites/tech-on-the-way/photos-generated/hero-postcard.jpg`
- **§11.11.5 guardrails:** `license_note: "Synthetic image. Do not represent as actual company work."`; `intended_slot_context: "aspirational-business-OK | atmosphere-OK"` (never proof/team/real-job/owner-portrait/real-customer/before-after).

## Prompt seed

Mobile tech service van with rear doors open, organized tools and electronics inside, technician's hands working on a device on the right side, suburban Atlanta driveway setting at golden hour.

Bruce can refine wording, but every prompt MUST include the composition requirements above.

## Output

1. `sites/tech-on-the-way/photos-generated/hero-postcard.jpg` (3360×1872 JPEG)
2. `sites/tech-on-the-way/bruce-asset-intel.json` with `generated_images[]` entry (purpose=postcard-hero, prompt, model=gpt-image-2, license_note, intended_slot_context, width=3360, height=1872). Set `model_stack.image_generation` = `openai/gpt-image-2`.
3. Append "## Postcard Hero v3 — gpt-image-2" section to `bruce-asset-intel.md`.

## Budget

- max_wallclock_minutes: 5
- max_generation_attempts: 3

— Mini
