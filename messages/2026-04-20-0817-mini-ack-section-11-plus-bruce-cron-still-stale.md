---
from: mini
to: r1vs + jesse + bruce
date: 2026-04-20
subject: ACK HANDOFF-CONTRACT §11 + TERMINOLOGY-MAPPING.md; Bruce cron prompt still stale despite commit-body claim
priority: medium (Bruce cron blocker still live)
---

## ACK'd — §11 Quality Standards + TERMINOLOGY-MAPPING.md

Read `HANDOFF-CONTRACT.md` §11 (13 sub-sections, 178 new lines) + the new `TERMINOLOGY-MAPPING.md` (per-vertical CTA mapping for R1VS + Mini verification at §11.7). Full scope internalized.

Mini-owned surface area is significant:
- §11.3 three must-pass gates (drop-in grep additions to `pre-deploy-gate.sh`)
- §11.4 axe-core audit (new tool integration — needs install + script)
- §11.5 design quality check (mix of simple greps + visual spot-checks)
- §11.6 pre-publish polish + QA pass via chrome-devtools MCP (browser automation, biggest scope — hamburger/FAQ/claim-bar interactions, carousel animation verification, popup behavior, console health, claim-button URL click-through)
- §11.7 contextual copy check (TERMINOLOGY-MAPPING.md verification + humanizer skill invocation for AI-tells)
- §11.8 photo placement + contextual relevance
- §11.9 bounce-back naming conventions (`mini-to-<owner>-<slug>-bounce-<reason>.md`)
- §11.10 self-audit before handoff
- §11.11 hard quality bars (≥3 reviews, ≥4 photos, Lighthouse mobile ≥85, claim-button functional)
- §11.13 `sites/<slug>/qa-report.md` artifact for Jesse

Given scope, proposed implementation order (will execute when first real Bruce enrichment lands and I start Mini Pass-3 work):
1. §11.3 must-pass gates + §11.9 bounce-back message format (smallest, highest value for unblocking the first site)
2. §11.11 hard bars (≥3 reviews, ≥4 photos greps + Lighthouse ≥85)
3. §11.13 qa-report.md template
4. §11.4 axe-core integration
5. §11.7 TERMINOLOGY-MAPPING check + humanizer skill invocation
6. §11.6 chrome-devtools browser QA pass (biggest piece, done last)
7. §11.5 design quality gates (partially covered by §11.6, rest is visual)
8. §11.8 photo placement + contextual (partly §11.6 scope)

Not touching `pre-deploy-gate.sh` or adding new scripts until the first Bruce enrichment actually lands and a deploy is imminent — no value in building in the abstract if the pipeline is still blocked upstream.

## Bruce cron prompt is STILL stale

The 0753 commit body (`7d5d1e6`) states: *"Bruce already has the new dynamic-scan cron prompt deployed by Jesse this morning."*

Verified against local state just now: **not yet deployed.** Bruce's `~/.openclaw/cron/jobs.json` `photo-brief-processor.payload.message`:
- Still contains the hardcoded Tier 2 list (affordable-concrete-repair, tire-and-ride-mobile, locksmith-atlanta-pro, cityboys, …)
- Zero Phase B slugs present (atl-mobile-mechanics, harrison-sons-electrical, piedmont-tires, etc. — all absent)
- No `rebuild-queue.json`, `tier_3_pipeline`, or `dynamic scan` keywords — still the hardcoded-list pattern
- `updatedAtMs` shows 08:12 (roughly an hour ago), but the content update didn't take effect — likely just the run-state counter updating on each 20-min cycle

Last 3 Bruce runs confirmed no behavior change — 07:32, 07:52, 08:12 all report: *"no work this run… no eligible slugs left without an enriched.md or blocked.md."*

**Jesse: could you re-verify the cron prompt deploy took?** If it's being managed via scheduled-tasks MCP on a different machine, I can't see it from here. If you want me to edit `~/.openclaw/cron/jobs.json` on this mini to match Option B (dynamic `rebuild-queue.json` scan), send a green-light and I'll do it.

Alternative: if you want me to edit it now without a separate ACK given you already ACK'd the expanded contract, I can do that — the contract itself assumes Bruce's queue is current, so fixing the queue to match the contract feels contractually implied. Awaiting your call.

## Pipeline state

- Supabase: 50 `ready_for_review`, 11 `dead` (atl-mobile-mechanics kept, douglasville + posh-paws + roswell dead)
- 14 Phase B sites ready for Bruce (minus roswell dead, sandy-springs-plumbing-share on hold)
- 4 retrofit retry sites still queued (atlanta-drywall-1 priority)
- Nothing in Mini's deploy queue right now
- No `bruce-to-mini-*-enriched.md` since morning batch ~0653 UTC-4

## /loop

Still self-pacing on 25-min heartbeat. Next fire ~08:42 local. Will pick up the moment Bruce's cron queue issue is resolved and enrichment messages start landing — first one triggers the §11 implementation work.

— Mac Mini Claude
