---
slug: sandy-springs-plumbing
generated_at: 2026-04-28T02:45:00Z
status: success
collect_request_ref: sites/sandy-springs-plumbing/collect-request.md
---

# Bruce Asset Intelligence — Sandy Springs Plumbing

## Photo Quality Assessment

### photos-raw/gbp-01.jpg — proof-candidate (confidence: 0.72)
Septic/excavation work — documentary but real job. Adequate for SERVICE_GALLERY or proof slots. Some ground-level visual noise. Low caption-overlay risk — subject is centered.

### photos-raw/gbp-02.jpg — proof-candidate (confidence: 0.70)
Tankless water heater in attic — confirms actual plumbing work. SERVICE_GALLERY candidate. Some background clutter from attic environment. Low caption-overlay risk.

### photos-raw/gbp-03.jpg — gallery-candidate (confidence: 0.75)
Exterior HVAC unit — not strictly plumbing but confirms这家business does exterior service work. Good atmosphere photo. Low caption-overlay risk.

### photos-raw/gbp-04.jpg — proof-candidate (confidence: 0.82)
Freestanding tub — strongest real photo in the set. Bathroom context, clean install, aspirational-adjacent. Currently in use as GTMDot card per collect-request. Works for SERVICE_GALLERY or proof slots. Low caption-overlay risk.

### photos-raw/gbp-05.jpg — gallery-candidate (confidence: 0.68)
Kitchen or bathroom fixture. Adequate but not distinctive. Low caption-overlay risk.

## Hero Recommendation

**Preferred path:** `photos-generated/hero-01.jpg`

Per collect-request, Jesse specifically asked for an editorial kitchen-faucet shot for the hero. The generated hero is a polished brushed-nickel pull-down faucet over a white farmhouse sink — warm morning light, marble countertop, shallow DOF. Exactly per Jesse's tight prompt. Reads well at thumbnail sizes (340px card) and serves both the gtmdot.com carousel and the SSP pages.dev hero.

**Fallback:** `photos-raw/gbp-04.jpg` (freestanding tub, currently the GTMDot card) — still a strong bathroom proof shot but less aspirational for a hero than the kitchen-faucet composition.

## Icon Verification

No icon mismatch detected — no HTML read this run per §11.1 scope.

## Object/Context Verification

| Claim | Evidence | Confidence |
|---|---|---|
| Plumbing services business | 5 Google reviews referencing main water line replacement, sewer line, bathroom plumbing, faucet repair; gbp-01..05.jpg show real plumbing work (excavation, tankless heater, tub) | 0.92 |
| Atlanta-area service | Reviews reference Dunwoody, Sandy Springs; address confirms Georgia service area | 0.90 |

## Review Coverage Notes

**Sufficiency: sufficient**

5 strong Google reviews already captured. Reviews mention named plumbers (Bryan, Jay, Levi, Todd) with specific project details. No enrichment needed — per collect-request, "5 strong reviews already captured" and review analysis is explicitly out of scope.

## Generated Images

| File | Purpose | Prompt | Slot |
|---|---|---|---|
| `photos-generated/hero-01.jpg` | hero | "Editorial interior photograph of a sun-lit modern kitchen, focused on a polished brushed-nickel pull-down faucet over a deep white farmhouse-style sink. Crisp marble countertop, soft morning light from a side window casting subtle shadows. Shallow depth of field — faucet sharp, background kitchen softly blurred. Warm whites, brushed nickel, faint greenery from a potted plant on the windowsill. Atlanta suburban-home aesthetic. No people. No text. No logos. No brand markings. No watermark. Photorealistic, magazine-quality, 16:9 landscape aspect ratio." | HERO — used in both gtmdot.com Recent Builds carousel card AND sandy-springs-plumbing.pages.dev hero |
