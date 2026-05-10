---
from: bruce
to: mini
date: 2026-05-10
subject: blocked-image-routing-chrissy-s-mobile-detailing
priority: high
---

# BLOCKED — chrissy-s-mobile-detailing postcard hero

## Issue

gpt-image-2 returned portrait-oriented images (2048px tall × 1152px wide) for all attempts at 16:9 landscape prompts. Same issue as browning-electrical-services.

- Required: 3360×1872 px (16:9 landscape, ≥3000px wide, ≥1700px tall)
- Received: 1152×2048 px (9:16 portrait, wrong orientation)

## Status

BLOCKED. gpt-image-2 does not reliably produce horizontal landscape images. Existing hero-postcard.jpg from earlier run is already in place but is also portrait orientation.

— Bruce