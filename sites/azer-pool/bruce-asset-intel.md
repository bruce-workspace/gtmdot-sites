---
slug: azer-pool
generated_at: 2026-05-09T03:14:00Z
status: success
collect_request_ref: sites/azer-pool/collect-request.md
---

# Bruce Asset Intelligence — Azer Pool

## Postcard Hero v3 — gpt-image-2

**Status:** SUCCESS
**Generated:** 2026-05-09T03:14:00Z
**model_stack.image_generation:** `openai/gpt-image-2` ✓

**Output file:** `photos-generated/hero-postcard.jpg` (3360×1872 JPEG)
**Alternative candidates:** 2 additional variants stored in `photos-generated/` with full UUID filenames.

**Guardrails applied (§11.11.5):**
- `data-source="generated"` must be added by Mini at HTML integration time
- `intended_slot_context` = `aspirational-business-OK | atmosphere-OK` — does NOT include any proof-required context flags
- `license_note` = "Synthetic image. Do not represent as actual company work." included in JSON
- No identifiable people, no text, no logos in image ✓

**Prompt used:**
> Sparkling clean residential pool at dusk with light reflections rippling across the water surface, pool equipment visible on the right side. Horizontal composition with primary visual subject on the right two-thirds of the frame. Left third may go dark or be visually quieter — overlaid with text and gradient. No text, no readable signage, no logos, no license plates, no identifiable people. Cinematic photorealistic style, warm professional lighting, premium editorial feel. 16:9 horizontal landscape orientation.

**Routing verification:** gpt-image-2 confirmed via `image_generate` tool response (`openai/gpt-image-2` in output). NOT MiniMax, NOT DALL-E. ✓
