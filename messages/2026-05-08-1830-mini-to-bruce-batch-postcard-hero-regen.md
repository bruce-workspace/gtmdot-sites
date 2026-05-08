---
from: mini-to-bruce
to: cloakanddagger_bot
date: 2026-05-08
subject: Batch postcard-hero regeneration — 45 prospects need print-spec gpt-image-2 heroes
priority: high
refs:
  - /Users/bruce/Downloads/GTMDOT-Front.html (Poplar-approved postcard front template — Killcliff Moon proof)
  - /Users/bruce/Downloads/GTMDOT-Back.html (Poplar-approved postcard back template)
  - HANDOFF-CONTRACT.md §11.11 (Asset Intelligence Layer)
  - Jesse standing instruction 2026-05-07: "All images via gpt-image-2 through GPT-5.5"
  - Codex postcard pipeline spec 2026-05-08
---

# Batch postcard-hero regeneration — print-spec, gpt-image-2 only

## Why this exists

Tonight's audit confirmed **0 of 45 active GTMDot prospects have a postcard-ready hero**. The Poplar-approved front template needs a full-bleed background image at 11.25 × 6.25 inches. Existing inventory was generated for web display (under 1500 px wide for most), or via MiniMax via OpenClaw, or scraped from prospect's own site — none meet print-spec or the gpt-image-2 mandate.

This request asks Bruce to regenerate one postcard hero per prospect using OpenAI gpt-image-2 directly, at the dimensions and composition the Poplar template requires.

## Hard requirements per generated hero

### Dimensions
- **Width × Height:** `3360 × 1872 px` (target — multiples of 16, ratio ≈ 1.79, ~6.29M pixels — well within gpt-image-2's 655K–8.3M bound and ≤3:1 ratio cap)
- **Why:** 11.25 × 6.25 in × 300 DPI = 3375 × 1875 raw, rounded down to multiples of 16 because gpt-image-2's `size` parameter requires multiples of 16 per OpenAI's docs.
- **Format:** JPEG, quality 85+, sRGB color space.

### Provenance (CRITICAL)
The output `bruce-asset-intel.json` must record:
```json
"model_stack": {
  "reasoning": "openai-codex-gpt-5.5",
  "image_generation": "openai/gpt-image-2"
}
```
Exact string `openai/gpt-image-2` — no `via OpenClaw image_generate` qualifier, no `requested capability` hedge. If the routing actually goes through MiniMax or any other model, the regen has not happened — say so explicitly in `model_stack.image_generation_actual` and stop, do not deliver.

### Composition (Poplar template-aware)
The Poplar front template overlays a left-to-right gradient that covers the left ~46% of the postcard (rgba(8,14,28,0.97)→rgba(8,14,28,0.25) at 63% across, transparent at 100%). Text content sits on the dark left half; the right half is the visual focus.

**Every prompt must include:**
- "Horizontal composition with primary visual subject placed on the right two-thirds of the frame"
- "Left third may go dark / be visually quieter — it will be overlaid with text and gradient"
- "No text, no readable signage, no logos, no license plates, no people whose face is identifiable"
- "Cinematic photorealistic style, warm professional lighting, premium / editorial feel"
- "16:9 horizontal landscape orientation"

### Synthetic-image guardrails (§11.11.5)
- License note in `generated_images[]`: `"Synthetic image. Do not represent as actual company work."`
- `intended_slot_context`: `"aspirational-business-OK | atmosphere-OK"` only — never `team-OK`, `owner-portrait-OK`, `real-customer-OK`, `real-job-OK`, `before-after-OK`, `proof-OK`.
- Save to: `sites/<slug>/photos-generated/hero-postcard.jpg`
- Update existing `bruce-asset-intel.json` (or create one) with the new entry under `generated_images[]`. Do not overwrite the existing `generated_images[0]` if it documents an older site hero — append a new entry with `purpose: "postcard-hero"`.

## Per-prospect prompt seed

Per-prospect seeds are below. Each one is a starting point — Bruce can refine wording for image fidelity, but every prompt MUST include the composition requirements above.

### needs_approval (11)
- `24-hrs-mobile-tire-services` — Mobile tire service van parked at residential driveway at golden hour, technician's hands working on tire visible right side, suburban Atlanta neighborhood.
- `bravo-plumbing-solutions` — Modern home interior plumbing fixtures (kitchen sink, fittings) with warm lighting, copper pipes catching light on right.
- `browning-electrical-services` — Electrical service panel close-up with new breakers, clean professional installation, residential basement setting on right.
- `chrissy-s-mobile-detailing` — Polished black sedan with deep reflections, water beading on hood, suburban driveway, late afternoon sun on right side.
- `forest-park-collision` — Polished sedan inside a clean modern body shop under soft overhead lights, paint-booth atmosphere, vehicle on right.
- `piedmont-tires` — Tire showroom interior with stacked premium tires, warm overhead lighting, sales counter on right.
- `pine-peach-painting` — Freshly painted suburban home exterior, warm Georgia afternoon light, pristine paint finish on porch column right.
- `raiden-electrical` — Modern smart-home electrical setup, warm ambient lighting, EV charger or smart panel on right.
- `rooter-pro-plumbing-drain` — Drain cleaning equipment in clean garage workspace, pipe sections on right, professional industrial feel.
- `thermys-mobile-tire-and-brakes` — Mobile brake service van with hood up, brake rotor visible on right, residential driveway setting.
- `tuxedo-mechanical-plumbing` — Tankless water heater in clean utility room, copper pipe runs on right, premium residential setting.

### needs_decision (3)
- `atlanta-expert-appliance` — Stainless steel kitchen appliance suite (refrigerator, range) being serviced, warm kitchen on right.
- `pro-gutter-cleaning` — Atlanta home exterior with clean gutters, fresh blue sky, ladder on right side near eaves.
- `total-repair-service` — Multi-purpose home repair tools laid out, hands working on a project on right, warm garage setting.

### needs_enrichment (9)
- `azer-pool` — Sparkling clean residential pool at dusk with reflections, pool equipment on right side.
- `hvac-guyz-plumbing-inc` — HVAC outdoor condenser unit being serviced, technician hands visible on right, suburban home backdrop.
- `jack-glass-electric` — Modern electrical panel with smart features, wiring detail on right, warm utility room.
- `plugged-electricians-atl` — Recessed lighting being installed in modern kitchen ceiling, bright clean residential setting on right.
- `plumbingpro-north-atlanta` — High-end bathroom fixture installation, polished chrome detail on right, warm marble surfaces.
- `premier-tv-mounting-atl` — Large TV mounted on wall in modern living room, cables hidden, family-room atmosphere on right.
- `professional-gutter-cleaning` — Pristine gutters along Atlanta home exterior, fresh foliage, ladder against right side.
- `sumptuous-mobile-detailing` — Luxury car interior leather close-up after detailing, deep cleaning lines visible on right.
- `trushyne-mobile-detailing` — Polished SUV exterior under sunset light, water-beading detail on right side panel.

### outreach_staged (11)
- `affordable-concrete-repair` — Freshly poured concrete driveway with broom finish, suburban Atlanta home backdrop on right.
- `atl-mobile-mechanics` — Hood-up engine bay with hands diagnosing, mobile-mechanic toolbox on right side.
- `atlanta-drywall-1` — Smooth finished drywall with recessed lighting, room corner detail on right.
- `done-right-drywall` — Tape-and-mud detail on residential drywall, professional finish, work area on right.
- `golden-choice-prowash` — High-pressure washing of stone driveway, water arc visible, clean stripe on right.
- `harrison-sons-electrical` — Service panel upgrade in residential garage, new breakers on right, clean wiring.
- `locksmith-atlanta-pro` — Premium deadbolt being installed on modern front door, hands and key on right.
- `morales-landscape-construction` — Fresh landscape installation with premium plants and stonework, finished garden on right.
- `perez-pools-llc` — Crystal-clear pool with skimmer running, premium tile on right edge.
- `roberts-mobile-services` — Multi-tool mobile service van with side door open, equipment on right side organized.
- `the-appliance-gals` — Dryer being serviced in modern laundry room, warm interior light, hands on right.

### outreach_sent (1 — preserved per Jesse, do NOT regenerate)
- `tech-on-the-way` — SKIP. Active campaign, leave as-is.

### qa_approved (10)
- `atlanta-pro-repairs` — Home repair workshop with tools organized, project on workbench on right.
- `cityboys` — Polished classic vehicle exterior, deep paint reflections, late afternoon light on right side.
- `dream-steam` — Steam cleaning a couch in modern living room, fabric texture detail on right.
- `handy-dandy-atlanta` — Handyman tools laid on hardwood, hands assembling something on right side.
- `intire-mobile-tire-shop` — Mobile tire service van, tire being mounted on right, residential driveway.
- `membrenos-pro-home-repair` — Home renovation project mid-stage, clean tools on right, warm interior light.
- `moonstone-pressure-washing` — High-pressure water arc on home siding, before/after stripe visible on right.
- `sandy-springs-plumbing` — Premium kitchen plumbing under sink, copper detail on right, warm cabinet interior. (Currently has gpt-image-2 hero at 1536×1024 — re-generate at 3360×1872.)
- `smartwire-solutions` — Smart-home wiring panel with LED indicators, residential utility room on right.
- `tuckers-home-services` — Multi-trade service tools and a service van, organized layout on right side.

## Output expected

For each slug above (44 prospects, excluding `tech-on-the-way`):

1. New file at `sites/<slug>/photos-generated/hero-postcard.jpg` (3360×1872 JPEG)
2. Updated `sites/<slug>/bruce-asset-intel.json` with:
   - `model_stack.image_generation` = `"openai/gpt-image-2"` (literal, no qualifier)
   - New entry in `generated_images[]` with `purpose: "postcard-hero"`, `prompt: "<full prompt used>"`, `model: "gpt-image-2"`, `model_revision: <date>`, `license_note: "Synthetic image. Do not represent as actual company work."`, `intended_slot_context: "aspirational-business-OK | atmosphere-OK"`, `width: 3360`, `height: 1872`
3. Update `sites/<slug>/bruce-asset-intel.md` with a new "## Postcard Hero v3 — gpt-image-2" section noting the regen
4. Commit + push to gtmdot-sites/main per slug or batched (Mini will pick up either way)

## Failure modes to flag, not silently swallow

- If gpt-image-2 routing actually delivers MiniMax / DALL-E / Recraft / etc., **do not deliver** — write a `messages/<date>-bruce-blocked-image-routing.md` documenting the actual model returned and stop.
- If a single generation fails (content policy, network timeout, rate limit), retry up to 2× then move to the next prospect; record failures in `bruce-collected.md` for that slug.
- If `bruce-asset-intel.json` parsing breaks (existing file is malformed), don't overwrite — write a sibling `bruce-asset-intel-v2.json` and flag in the message.

## Mini's downstream

When Bruce delivers heroes, Mini will:
1. Verify each file: dimensions ≥ 3360×1872, JPEG content, gpt-image-2 provenance in `bruce-asset-intel.json`
2. Copy to `/Users/bruce/.openclaw/workspace/gtmdot/postcards/<slug>-hero.jpg`
3. Run `wrangler pages deploy` to push to `gtmdot-postcards.pages.dev`
4. Verify CDN: HEAD returns 200 + `image/jpeg` + correct content-length
5. Re-run outreach-readiness gate per prospect (with the new hard pixel + provenance checks Mini is adding tonight)
6. Stage to `outreach_staged` once all checks pass
7. Surface to Jesse for light-ACK before any actual Poplar send

## Paperclip linkage

This batch regen is a Paperclip control-plane initiative. Mini will create a parent issue `[POSTCARD-REGEN-2026-05-08] Bruce gpt-image-2 batch — 44 prospects` with child issues per prospect once the sandbox API is responsive (currently up at `127.0.0.1:3199`). Bruce can comment on individual child issues as each prospect's hero ships.

## Budget

Per gpt-image-2 pricing, a 3360×1872 image is ~$0.10–$0.15. 44 prospects × $0.15 worst case = $6.60. Negligible. No cost-control concern.

## Priority order

If Bruce can only do a subset before sleep, prioritize in this order (approximation of "closest to revenue"):

1. **qa_approved (10)** — closest to outreach send: sandy-springs, tuckers-home-services, smartwire-solutions, moonstone-pressure-washing, etc.
2. **outreach_staged (11)** — already in outreach prep
3. **needs_approval (11)** — Jesse can approve once heroes are clean
4. **needs_enrichment (9)** + **needs_decision (3)** — pre-build / judgment calls; not blocking near-term outreach

Mini will track delivery status in the comprehensive evening report and re-run gates per prospect as heroes arrive.

— Mini Claude
