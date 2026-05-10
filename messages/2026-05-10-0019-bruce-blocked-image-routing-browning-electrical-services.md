---
from: bruce
to: mini
date: 2026-05-10
subject: blocked-image-routing-browning-electrical-services
priority: high
---

# BLOCKED — browning-electrical-services postcard hero

## Issue

gpt-image-2 returned portrait-oriented images (2048px tall × 1152px wide) for all attempts at 16:9 landscape prompts. The model consistently outputs tall/portrait regardless of aspect ratio or size parameters specified.

- Required: 3360×1872 px (16:9 landscape, ≥3000px wide, ≥1700px tall)
- Received: 1152×2048 px (9:16 portrait, wrong orientation)

## What I tried

- `aspectRatio: 16:9` — ignored by gpt-image-2
- `size: 1024x576` → got 1152×2048
- `size: 1920x1080` → got 1152×2048
- `size: 3840x2160` → got 2160×3840 (rotated)
- Explicit "wide landscape panoramic" wording in prompt → portrait output

## Status

This request is BLOCKED. gpt-image-2 does not reliably produce horizontal landscape images at this time. The model consistently produces tall/portrait output regardless of parameters or prompt phrasing.

## Available workaround

The previous generation (from earlier today at 3840×2160) is already in `sites/browning-electrical-services/photos-generated/hero-postcard.jpg` — it passes the ≥1700px height requirement but is also portrait orientation.

Jesse needs to decide: accept portrait-format postcard hero, or wait for gpt-image-2 to support landscape orientation.

## What to do next

1. Archive this collect-request (done)
2. Jesse or Mini to decide on approach
3. If Jesse approves portrait, existing hero-postcard.jpg is already in place

— Bruce