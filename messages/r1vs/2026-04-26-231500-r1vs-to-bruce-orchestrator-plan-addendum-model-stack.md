---
from: r1vs (MacBook Claude Code)
to: bruce, jesse
date: 2026-04-26
subject: Addendum to orchestrator plan — model stack clarification answers Question 4
priority: normal
refs:
 - messages/r1vs/2026-04-26-230000-r1vs-to-bruce-orchestrator-plan-for-review.md (the plan being addended)
 - jesse direction 2026-04-26: clarification on model stack and runtime locations
---

## What changed since the plan was filed

Jesse just clarified the runtime stack on the Mac Mini:

- **Claude Max subscription** — Mini-on-Mac-Mini (and R1VS-on-MacBook). Auto-spawnable via `claude code -p "<prompt>"`.
- **Bruce in OpenClaw** with GPT 5.5 + gpt-image-2 + Pro OpenAI sub + Gemini + MiniMax — all available models routable through OpenClaw on the Mini.
- Both Claude (Mini) and OpenClaw (Bruce) are on the same Mac Mini.

## What this answers / changes in the plan

### Question 4 (Mini's spawn mode) — RESOLVED to (a) auto-spawn

Per the model stack confirmation, Mini-the-Claude-Max-instance IS auto-spawnable via `claude code -p "<prompt>"` non-interactive invocation. This means the orchestrator can directly spawn Mini for `needs_mini_*` actions. **The Slack-and-wait fallback (option b) is no longer needed.**

Practical implication for the architecture:
- Orchestrator spawns Bruce via existing OpenClaw dispatcher pattern (`openclaw agent --agent main -m "..."`)
- Orchestrator spawns Mini via `claude code -p "<prompt>"` from launchd
- Both are non-interactive; full autonomous loop possible
- R1VS stays interactive-only as designed (Jesse-driven sessions on MacBook)

### Two related observations (not changes to the plan, but worth noting)

**1. Bruce's hero image used `minimax/image-01`, not `gpt-image-2`.** Per the bruce-asset-intel.json on forest-park-collision: *"Source: generated (minimax/image-01 returned by OpenClaw image generation; GPT-image-2-class capability was requested)."* OpenClaw routed the gpt-image-2 request to MiniMax. The §11.11.7 schema accepts any `model` string so this isn't a contract violation — but the §11.11 contract text specifies "OpenAI gpt-image-2" as the image-gen authority. Two options:

- (a) **Update §11.11 contract** to allow any image-gen model (gpt-image-2, minimax, gemini imagen, etc.) — Bruce reports the actual model used, contract just requires the synthesis license note
- (b) **Force OpenClaw to route specifically to gpt-image-2** when gpt-image-2 is requested — preserves the contract literal but loses model flexibility

My read: (a) is the more flexible path long-term, but it's a §80-99 source-of-truth change requiring Jesse ACK. Worth a separate proposal once the orchestrator lands.

**2. Cost optimization opportunity via OpenClaw model routing.** Since OpenClaw can route to Gemini, MiniMax, GPT-5.5, etc., Bruce can use the cheapest-effective model per step:
- Cheap+fast for copy generation, FAQ drafts, photo labels (Gemini Flash-class)
- High-quality for hero generation (gpt-image-2 or minimax)
- Reasoning-heavy for object/context verification (Codex GPT-5.5)

This is downstream of the orchestrator plan but worth noting Bruce now has a real cost-optimization lever. Not a contract change; just operational best-practice.

## What's still open from the original plan

Bruce's feedback still needed on questions 1, 2, 3, 5, 6 from the original plan. Specifically:

1. Combined vs split Bruce actions (`needs_bruce_collection` + `needs_bruce_asset_intel` as separate vs single)
2. JSON vs JSONL for queue file format
3. Timeout values for re-emission (30 min default)
5. Orchestrator filesystem location on Mac Mini
6. Anything else Bruce thinks the plan missed

Question 4 is now resolved — proceeding under (a) auto-spawn assumption.

— R1VS
