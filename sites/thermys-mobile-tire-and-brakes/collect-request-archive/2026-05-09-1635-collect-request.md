---
slug: thermys-mobile-tire-and-brakes
requested_by: mini
requested_at: 2026-05-09T02:35:00Z
priority: high
type: postcard-hero-regen
---

# Collect-request — thermys-mobile-tire-and-brakes (postcard hero regen via gpt-image-2)

## Why this request

Per Jesse 2026-05-07 standing instruction: ALL postcard heroes must come from
OpenAI gpt-image-2 (not MiniMax via OpenClaw, not Recraft, not site-scraped,
not Unsplash). Tonight's audit found 0 of 45 active prospects have a
postcard-print-spec hero with verified gpt-image-2 provenance.

Mini's outreach-readiness gate (commit 61086a7) now hard-blocks any prospect
from outreach until the hero passes:
- Dimensions ≥ 3000×1700 (postcard print at 11.25×6.25 in @ 300 dpi)
- model_stack.image_generation = "openai/gpt-image-2" exactly

Earlier batched message at messages/2026-05-08-1830-mini-to-bruce-batch-
postcard-hero-regen.md is in the wrong path for cron — re-filing per-slug.

## Hard requirements

- **Dimensions:** 3360×1872 px (multiples of 16 per gpt-image-2 size constraint;
  ratio ≈ 16:9, ~6.29 MP — within 655K–8.3M bound and ≤3:1 ratio cap)
- **Format:** JPEG, quality 85+, sRGB
- **Provenance:** bruce-asset-intel.json `model_stack.image_generation` MUST
  read EXACTLY `openai/gpt-image-2` (no "via OpenClaw image_generate" hedge,
  no "requested capability" qualifier, no hyphen-format `openai-gpt-image-2`).
  If the actual route delivers MiniMax / DALL-E / Recraft, write a blocked
  message and STOP — do NOT deliver.
- **Composition:** Visual subject on RIGHT two-thirds. Left third may go dark
  (it'll be overlaid with text + gradient on the postcard front). No readable
  text, no signage, no logos, no license plates, no people whose face is
  identifiable. Cinematic photorealistic style, warm professional lighting.
  16:9 horizontal landscape orientation.
- **Save to:** `sites/thermys-mobile-tire-and-brakes/photos-generated/hero-postcard.jpg`
- **§11.11.5 guardrails:** include `license_note: "Synthetic image. Do not
  represent as actual company work."` in `bruce-asset-intel.json`'s
  `generated_images[]` entry. `intended_slot_context` = `aspirational-business-OK
  | atmosphere-OK` (NEVER `team-OK`, `owner-portrait-OK`, `real-customer-OK`,
  `real-job-OK`, `before-after-OK`, `proof-OK`).

## Prompt seed

Mobile brake service van with hood up, brake rotor visible on right, residential driveway setting.

Bruce can refine wording for image fidelity, but every prompt MUST include:
- "Horizontal composition with primary visual subject on the right two-thirds of the frame"
- "Left third may go dark / be visually quieter — overlaid with text and gradient"
- "No text, no readable signage, no logos, no license plates, no identifiable people"
- "Cinematic photorealistic style, warm professional lighting, premium / editorial feel"
- "16:9 horizontal landscape orientation"

## Output expected

1. New file at `sites/thermys-mobile-tire-and-brakes/photos-generated/hero-postcard.jpg` (3360×1872 JPEG)
2. Updated `sites/thermys-mobile-tire-and-brakes/bruce-asset-intel.json` with new `generated_images[]`
   entry: purpose=`postcard-hero`, prompt=full text used, model=`gpt-image-2`,
   model_revision=today's date or actual API revision string, license_note,
   intended_slot_context, width=3360, height=1872. Set
   `model_stack.image_generation` = `openai/gpt-image-2`.
3. Append to `sites/thermys-mobile-tire-and-brakes/bruce-asset-intel.md` a "## Postcard Hero v3 —
   gpt-image-2" section noting the regen.
4. Commit + push.

Mini's downstream: pulls main, copies to `gtmdot/postcards/thermys-mobile-tire-and-brakes-hero.jpg`,
wrangler deploys to gtmdot-postcards.pages.dev, re-runs outreach-readiness
gate, advances to outreach_staged once all checks pass, surfaces to Jesse
for light-ACK send.

## Budget

- max_wallclock_minutes: 5 (gpt-image-2 generation is fast)
- max_generation_attempts: 3 (retry on content-policy / network)
- Cost: ~$0.10–0.15 per generation, well within budget caps

## Failure modes — flag, don't deliver

- Routing returns MiniMax / DALL-E / Recraft instead of gpt-image-2 → write
  `messages/<date>-bruce-blocked-image-routing-thermys-mobile-tire-and-brakes.md` and stop.
- Content policy blocks 3 attempts → write block message and move to next
  prospect; record in completion summary.
- Existing `bruce-asset-intel.json` parse fails → write sibling
  `bruce-asset-intel-v2.json` and flag.

— Mini
