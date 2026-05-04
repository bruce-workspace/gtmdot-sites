---
from: mini-claude
to: codex (post-build-operations), bruce, r1vs, jesse, paperclip
date: 2026-04-29
subject: Post-Build Operations lane confirmed + SmartWire lessons → named Paperclip gates
priority: high
references:
  - messages/2026-04-29-mini-handoff-to-codex-crm-post-build-coordination.md
  - PIPELINE.md §2
  - HANDOFF-CONTRACT.md §11 / §11.11
---

# Post-Build Operations lane — confirmed

Per Jesse 2026-04-29 reply to the handoff: the Mini → Codex transition
splits coordination into four explicit lanes. This message ratifies that
split and converts the SmartWire learnings into named gates Paperclip
can surface as discrete artifacts.

## Lane split

| Lane | Owns |
|---|---|
| **Pre-Build Coordination** | Prospect intake, R1VS packets, Phase 0 readiness, Paperclip pre-build gates |
| **Post-Build Operations** (Codex on Mini) | Everything after a site exists — QA, enrichment integration, claim code checks, claim bar / popup, postcard / email readiness, Jesse approval prep |
| **GTMDot Platform** | Shared platform behavior — CRM stage logic, checkout / claim flow, Stripe, shared claim UI, Cloudflare / Next build issues, automation code |
| **Paperclip** | Visible control-plane layer for gates / artifacts / blockers — NOT the executor |

**Channels:**
- Git packets (`messages/`) = canonical instructions and results
- Slack = notification only (never instructional source)
- Paperclip = state visualization + gate ratification surface

## SmartWire learnings → named Post-Build gates

Each lesson from the SmartWire pilot becomes a named gate that
Post-Build Operations runs on every prospect before signaling
outreach-readiness. These map onto checks already in
`scripts/outreach-readiness-gate.sh` plus a few not-yet-implemented:

### Already implemented in `outreach-readiness-gate.sh`

| Gate name | Status | Implementation |
|---|---|---|
| `ASSET_INTEGRITY` | ✅ shipped | content-type + byte-size check (not status-only) for desktop screenshot, mobile screenshot, hero image. Cloudflare Pages SPA fallback returns 200 + `text/html` for missing assets, so status-only checks lie. The gate verifies content-type starts with `image/`. |
| `CLAIM_CODE_RESOLUTION` | ✅ shipped | Verifies `gtmdot.com/codes.json` contains the prospect's `claim_code` AND `gtmdot.com/checkout?code=<X>` returns 200. Two-leg check because either alone can be stale. |
| `EMAIL_PATH_READINESS` | ✅ shipped (partial) | Checks email is present OR explicitly marked missing. If present, fetches `/api/prospects/<id>/email-preview?seq=1` and verifies HTTP 200 (sequence draft renders). Postcard-only path acceptable but requires Jesse approval. |
| `JESSE_APPROVAL_GATES` | ✅ shipped | Always listed, never auto-pass: CRM stage move past `qa_approved`, Poplar send, Resend trigger, billing / charge, public release. |

### Not yet implemented — Paperclip should add as named gates

| Gate name | Spec |
|---|---|
| `SLUG_CONSISTENCY` | Verify prospect's `slug` matches the gtmdot-sites directory name AND the Cloudflare Pages project name AND the codes.json registry value AND the postcard asset URLs. SmartWire diverged (`smartwire-solutions` in CRM vs `smart-wire-solutions` on disk). Recommend converging to CRM slug as canonical. |
| `JSON_LD_EDITORIAL` | Apply same editorial rules to JSON-LD `description`, `acceptedAnswer.text`, and other rendered-as-search-snippet fields as we apply to visible HTML. Specifically: no em dashes in authored copy, no fabrication patterns, no internal-context strings. JSON-LD is search-engine visible content. |
| `STAGE_AWARE_GATE_HYGIENE` | Meta-rule. When a gate (pre-push-gate, verify-build, etc.) false-positives on intentional state, the fix is to update the rule, not normalize an override. Two examples currently outstanding: pre-push-gate Check #3 (claim-bar-grep — branch shipped, not merged) and verify-build Check #1 (clean URLs — already merged). Track override-message frequency per gate; if any gate accumulates 3+ overrides, file a stage-aware rewrite. |
| `DEPLOY_PATH_INTEGRITY` | Ensure prospect site is deployed via the controlled path (direct wrangler with `--branch main` + `--commit-dirty=true`, NOT `gtmdot/scripts/deploy-site.sh` which auto-moves CRM stage). Verifies last deployment commit hash matches origin/main HEAD for the slug's site directory. |
| `INTERNAL_CONTEXT_STRIP` | Lint check that blocks production if any visible-on-page text contains internal context strings (`-OK |` patterns from `data-context`, `📷` debug placeholders, `Service Gallery N` template artifacts). The SmartWire alt-text leak from `data-resolved="false"` slots was this class of bug. |
| `CSS_HOVER_BRIDGE_PRESENT` | Specific check that any `nav-dropdown-menu` with `top: calc(100% + Npx)` offset has a corresponding always-present `::before` bridge on the parent. Or generalize: any hoverable submenu with a visual gap > 0px must have a hover-bridge. |
| `MOBILE_VIEWPORT_GATE` | Lint check that hero h1 doesn't wrap to >4 lines at 414px viewport, service-card body text doesn't right-clip, claim-bar buttons don't crop. Today this lives only in human visual QA — promote to automated. |

## What Codex should NOT do

These are unchanged from the handoff doc but bear repeating in the
context of the 4-lane split:

- ❌ No CRM writes (stage, claim_code, preview_site_url, etc.) without Jesse approval — exception: setting `claim_code` on a prospect that doesn't have one is OK if no stage move
- ❌ No Cloudflare deploys to production aliases without confirming the controlled path (no `deploy-site.sh`)
- ❌ No outreach (Poplar / Resend) ever, without explicit Jesse approval
- ❌ No production edits to brucecom-v3, gtmdot.com worker, or CRM source without telling Jesse first AND confirming GTMDot Platform lane ownership
- ❌ No Slack-as-instructional-source — Slack messages are notifications, not directives
- ❌ Technical pass on `outreach-readiness-gate.sh` is NOT outreach approval. The 5 Jesse-approval gates always block until Jesse explicitly clears them.

## First Codex session — recommended order

1. Read `messages/2026-04-29-mini-handoff-to-codex-crm-post-build-coordination.md` (the durable onboarding doc — 365 lines)
2. Read this file (lane split + named gates)
3. Inspect `scripts/outreach-readiness-gate.sh` to understand the gate semantics
4. Read the latest 5 `messages/*.md` files for any Jesse / Bruce / R1VS directive landed since this handoff
5. Compare SmartWire's current state (deployed at `7878409` ... actually `819fa94`) to the named-gates list above
6. For each gate not yet implemented, propose the Paperclip artifact spec — don't implement yet
7. Surface the proposal to Jesse before any new code

## Handoff status

- Handoff doc is durable: `messages/2026-04-29-mini-handoff-to-codex-crm-post-build-coordination.md`
- This file extends it with the 4-lane structure and named-gate mapping
- SmartWire is the worked example — every named gate above traces to a
  specific bug or moment in that pilot

— Mini-Claude (final session before Codex inherits Post-Build Operations)
