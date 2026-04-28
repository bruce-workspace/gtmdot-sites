---
slug: sandy-springs-plumbing
requested_at: 2026-04-28T02:33:45Z
requested_by: mini
deadline: 2026-04-29T02:33:45Z
priority: high
hero_intent: aspirational
generated_images_allowed: yes
---

# Collect Request — Sandy Springs Plumbing (hero image generation only)

This is a generation-only request, NOT a scraping request. Bruce delivered
GBP collection on 2026-04-26 (5 photos, 5 reviews — see existing
`bruce-collected.md`). Photos were documentary-grade (septic excavation,
tankless heater in attic, exterior HVAC unit, freestanding tub) — fine for
proof but no single image works as a polished hero / homepage thumbnail.

Jesse asked specifically for an aspirational hero generated via
`gpt-image-2`, used in two places:

1. The Sandy Springs Plumbing card in the gtmdot.com Recent Builds carousel
2. The hero on `sandy-springs-plumbing.pages.dev` itself

## Tight prompt (use as primary)

> Editorial interior photograph of a sun-lit modern kitchen, focused on a
> polished brushed-nickel pull-down faucet over a deep white farmhouse-style
> sink. Crisp marble countertop, soft morning light from a side window
> casting subtle shadows. Shallow depth of field — faucet sharp, background
> kitchen softly blurred. Warm whites, brushed nickel, faint greenery from a
> potted plant on the windowsill. Atlanta suburban-home aesthetic.
> No people. No text. No logos. No brand markings. No watermark. Photorealistic,
> magazine-quality, 16:9 landscape aspect ratio.

## Why this subject

- **Plumbing-relevant** without being literal. A faucet/sink hero reads as
  "your plumbing done right" without the Bobcat-and-mud documentary feel of
  the existing GBP shots.
- **Differentiates from gbp-04** (the freestanding tub) which we're
  currently using as the GTMDot card. Gives us two distinct aspirational
  shots for the SSP site (kitchen + bathroom).
- **Reads on small thumbnails.** A close-up faucet detail with a clean
  marble background still parses at 340px-tall card size.
- **Atlanta context.** "Suburban Atlanta" cue keeps it feeling local, not
  generic Apartment-Therapy.

## Backup prompts (if primary doesn't land)

If the kitchen-faucet shot comes back stiff/staged, try:

**Backup A — bathroom detail:**
> Editorial close-up of a polished chrome bathtub filler running water into
> a freestanding white soaking tub, sun-lit through a tall side window with
> sheer curtains. Wide-plank wood floor, white wainscoting, single potted
> plant. Warm whites and chrome. No people, no text, no logos. 16:9
> landscape, photorealistic, magazine quality.

**Backup B — exterior with plumber's truck (no people, no logos):**
> Editorial dawn photograph of a clean white service van parked on a brick
> paver driveway in front of a charming Atlanta-area craftsman home. Soft
> warm sunrise light. Magnolia trees in background. Van is unmarked (no
> logo, no decals, no text). Mood is professional and welcoming. No people
> visible. 16:9 landscape, photorealistic.

Pick ONE delivery — primary unless you have a specific reason backup A or
B will perform better, in which case explain in `bruce-asset-intel.md`.

## File naming

Per §11.11.1, save as:
- `sites/sandy-springs-plumbing/photos-generated/hero-01.jpg`

Include in `bruce-asset-intel.json` `generated_images[]` entry:
- `purpose: "hero"`
- `prompt: <exact prompt used>`
- `intended_slot: "HERO"`
- `license_note: "Synthetic image. Do not represent as actual company work."`

## Budget

- `max_generated_images`: 1 (just the hero — don't generate brand or
  service-card-bg in this run)
- `max_wall_clock_minutes`: 4
- No additional scraping needed — skip the `Requested sources` section.

## Out of scope (do NOT do in this request)

- No additional photo scraping (existing GBP set is fine for documentary
  slots)
- No icon-mismatch flagging (separate request if needed)
- No review-coverage analysis (5 strong reviews already captured)
- No HTML changes — Mini will integrate after delivery
