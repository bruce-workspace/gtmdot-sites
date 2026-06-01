Lane: GTMDot Platform / CRM v2
Session: Main GTMDot Codex coordination
Updated: 2026-06-01T11:20:00-04:00
Owner: Codex / GTMDot quarterback
Mode: CRM v2 takeover / control-plane reset

## 2026-06-01 CRM v2 Takeover

Codex is taking practical direction of the CRM rebuild from the main GTMDot thread because the live CRM is now slowing board clearing.

New artifact:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-01-crm-v2-codex-takeover-control-plane-reset.md`

Updated operating direction:

- Keep CRM v2 code in `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/`.
- Do not move CRM v2 into a separate repo/project folder.
- Main Codex/GTMDot thread owns CRM v2 priorities because it has the full context across Outreach, Post-Build, Pre-Build, Paperclip, Poplar, and CRM v1 failures.
- CRM v2's north star: every prospect must show exact next action, owner, supporting evidence, and whether Jesse can approve/send/fix it from the page.
- Immediate live CRM bridge patch already prepared locally: `Approve for Outreach`, `Needs Fix`, and `Run Enrichment`.
- Specific pain now captured as CRM v2 acceptance criteria: Thermys bad hero, Tuxedo missing nav/wrong hero, Raiden preview failure, Browning stage/channel mismatch, Rooter Pro override path.

## 2026-06-01 Live CRM Review Workflow Bridge Deployed

The approved live CRM bridge patch is deployed.

Artifact:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-01-crm-review-workflow-ux-deploy-complete.md`

Worker:

- `gtmdot-crm-v3`
- Version ID: `d93d6a5e-2d2d-4ed1-82af-920fe9cd4052`

Added:

- `Approve for Outreach`
- `Needs Fix`
- `Run Enrichment`

Verification:

- Build and OpenNext build passed.
- Wrangler deploy succeeded.
- Public `/pipeline`, `/lab/crm-v2`, and representative prospect detail pages return `200`.
- Playwright rendered checks confirmed buttons appear on expected stages.

No postcard submit/retry, email/SMS send, prospect contact, Paperclip mutation, git push, DNS/domain/hosting/billing change, or Stripe action was performed.

Still not approved:

- replacing live CRM with CRM v2,
- broad CRM/Supabase writes,
- sends/retries,
- Paperclip mutations,
- git pushes,
- DNS/domain/hosting/billing/Stripe changes.

Current lane status:
CRM v2 is still lab-only at `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/` and should not replace the live CRM while Jesse is remote. The foundation has moved from planning into a real sandbox implementation: the lab route loads current `/api/prospects` data read-only, derives pipeline/channel/stale-note/preflight state locally, and renders a new Kanban-first cockpit plus prospect command sheet.

Current verified state:
- `npm run build` passes in `/Users/bruce/.openclaw/workspace/brucecom-v3`.
- Lab route `/lab/crm-v2` is included in the Next build.
- Recurring build warning remains unrelated to CRM v2: Turbopack traces `next.config.ts -> src/lib/vault.ts -> src/app/api/prospects/[id]/vault/route.ts`.
- No CRM writes, sends, deploys, billing, DNS, prospect contact, or production board replacement performed by this lane.

Active blockers:
- CRM v2 remains an untracked sandbox tree under `src/app/lab/crm-v2/`; main coordinator should decide when/how to commit or PR it.
- Current CRM/API still exposes limited note/task detail; CRM v2 can derive stale-note policy from counts, but true note age, last verified date, evidence link, owner, and blocker status require future API/schema work.
- Reply monitoring to `hello@gtmdot.com` is still not proven end-to-end by this lane; CRM v2 currently models the required UI state and mismatch surfaces only.
- Poplar provider detail is not yet a first-class CRM v2 data feed; UI distinguishes CRM postcard state from provider truth but cannot prove full provider progression without Outreach data.
- Live CRM v1 remains operational source for board clearing until quarterback explicitly approves migration.

Prospects/items closest to revenue:
- Prospects already in `needs_approval`, `qa_approved`, `outreach_staged`, or `outreach_sent` remain closest to revenue because they are near site approval, channel proofing, send readiness, or response tracking.
- Highest-value CRM v2 surfaces for board clearing are the approval queue, contact recovery queue, outreach/channel mismatch queue, and stale-blocker revalidation queue.
- Specific prospect revenue decisions should remain with main coordinator/Paperclip because this lane is intentionally not asserting CRM truth or approving sends.

What can be safely advanced without Jesse present:
- Continue CRM v2 lab-only UX and derivation work.
- Continue splitting CRM v2 sandbox into model, derive, stats, and focused components.
- Improve read-only derived state for pipeline stage, channel state, stale-note handling, preflight gates, R1VS/Bruce/Codex handoffs, and Paperclip coordination visibility.
- Improve visual/UX hierarchy of the Kanban cockpit and clicked-card prospect sheet.
- Draft field-contract recommendations for future note/task/reply/provider APIs.
- Run local `npm run build` and route checks.

What requires explicit Jesse approval:
- Any live CRM write, stage move, status change, or strategic CRM truth decision.
- Replacing or redirecting the production CRM board to CRM v2.
- Outreach sends, resend/resume/pause operational changes, Poplar submissions, prospect/customer contact, or mailbox/reply handling changes.
- Stripe/billing, DNS/domain/hosting, deploys, or production config changes.
- Committing/pushing the CRM v2 sandbox if Jesse/main coordinator wants review through git.
- Decisions about storing full reply bodies vs snippets/metadata/mailbox links.

Files/artifacts changed by this lane:
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-crm-v2-additive-field-api-contract.md`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/page.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/model.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/derive.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/stats.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/AlertBell.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/CockpitHeader.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineBoard.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineCard.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineColumn.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineRail.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectApprovalPanel.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectBuildHandoff.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectChannelOperations.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectChannelSnapshot.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectCommandSummary.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectContactFeedback.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectIssuePresets.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectNoteHealth.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectPaperclipCoordination.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectRoutingPanel.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectSheet.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectStageGuardrails.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectWorkSignals.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/primitives.tsx`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`

CRM v2 foundation currently implemented:
- Kanban-first pipeline cockpit with primary CRM sections kept visible but not over-weighted.
- Saved pipeline views inside the cockpit: approval session, contact recovery, channel mismatches, outreach ops, build handoff, tasks/blockers, etc.
- Pipeline cards show route, readiness, top gate, queue reason, Paperclip state, channel state, and planned command hierarchy.
- Prospect sheet has extracted focused panels:
  - `ProspectCommandSummary`
  - `ProspectRoutingPanel`
  - `ProspectBuildHandoff`
  - `ProspectApprovalPanel`
  - `ProspectStageGuardrails`
  - `ProspectChannelOperations`
  - `ProspectChannelSnapshot`
  - `ProspectPaperclipCoordination`
  - `ProspectNoteHealth`
  - `ProspectWorkSignals`
  - `ProspectContactFeedback`
  - `ProspectIssuePresets`
- Derived model includes route state, build handoff, preflight actions, stage transition policy, queue signals, note health, outreach health, outreach timeline, and channel summaries.
- Derived model now includes `providerTruth` summaries for CRM lifecycle, CRM postcard event state, Poplar provider truth, Resend email truth, and `hello@gtmdot.com` reply monitoring.
- Derived model now includes `payloadPreflight` summaries for local/read-only Poplar postcard payload gaps and Resend email payload gaps.
- Derived model now includes `paperclipCoordination` summaries for parent issue visibility, blocker state, artifact state, next owner, visible links, and exact next action.
- Derived model now includes `labGuardrails` and `labAcceptanceCriteria` so the CRM v2 rail documents what the sandbox is proving and what remains prohibited.
- Board stats now include acceptance coverage counts for routing state, channel truth, provider truth, stale-note policy, and exact next action visibility.
- UI explicitly separates stage from channel truth and distinguishes postcard CRM state from future Poplar provider state.
- Jesse approval gates remain manual and do not auto-pass.
- Stale note policy is represented: old notes should not block work without fresh verification, but the current API lacks note-level fields for full enforcement.

Recommended next 3 actions:
1. Continue CRM v2 lab implementation around the current board-clearing workflow: tighten the Kanban cards, prospect sheet, and saved queues until they are useful enough to test against real v1 pain points.
2. Draft the CRM v2 additive field/API contract for notes, blockers, replies, provider events, claim-code lookup, paperclip links, and per-channel outreach state.
3. Ask main coordinator to identify 5-10 real near-revenue prospects from the current board for CRM v2 validation only; do not write CRM truth from v2 until Jesse approves.

Main coordinator handoff:
GTMDot Platform / CRM v2 can keep advancing safely in the lab while Jesse is remote. It should not block current board clearing in CRM v1. Use CRM v2 as a read-only design/field-contract lab for the next week, with emphasis on pipeline clarity, channel-state visibility, stale-note handling, and Jesse-review speed. Any production switch, stage write, outreach action, or strategic CRM truth decision must route through the main coordinator and require explicit Jesse approval.

2026-05-23 19:00 ET heartbeat update:
- Continued the CRM v2 lab-only foundation by extracting board acceptance coverage from the cockpit header into a focused `BoardAcceptanceCoverage` component.
- This keeps the Kanban cockpit easier to extend while preserving visible acceptance checks for routing, channel truth, provider truth, stale-note policy, and exact next action coverage.
- No CRM writes, sends, deploys, Paperclip mutations, or production CRM replacement were performed.

2026-05-23 20:25 ET heartbeat update:
- Added a focused `ProspectActionBar` component for the prospect sheet footer.
- The footer now uses CRM v2 derived preflight actions so inspection, feedback, rescan, and final approval/send intent are visibly separated instead of appearing as equal random buttons.
- Final approval/send actions remain locked in the read-only lab; this is UI/model wiring only.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-23 21:10 ET heartbeat update:
- Added derived `reviewChecklist` state to the CRM v2 prospect model and a new `ProspectReviewChecklist` sheet section.
- The clicked-card workflow now explicitly surfaces Jesse's review pass: desktop site, mobile site, claim flow/code, hero context, reviews/source-grounded copy, popup/claim bar behavior, postcard proof, email preview, and current blockers.
- Checklist rows are derived from current read-only prospect fields and mark what is ready, waiting for human review, attention-worthy, or blocked.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-23 21:55 ET heartbeat update:
- Added `PipelineCardReviewSummary` so each Kanban card now exposes review load before the prospect sheet is opened.
- Cards now summarize how many checklist items need work vs human review and show the top review/blocker action from the derived `reviewChecklist`.
- This keeps the pipeline board central while making approval complexity visible at a glance.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-23 22:40 ET heartbeat update:
- Added `ProspectStageDropdownPreview` to model Jesse's requested stage dropdown interaction in the clicked-card sheet.
- The sheet now shows current CRM stage and recommended target as dropdown-style controls with CRM write policy visible, while remaining read-only and non-mutating.
- This replaces the static current/recommended stage boxes and better reflects the future approved stage-change workflow.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-23 23:25 ET heartbeat update:
- Added derived `outreachQueue` state and a new `ProspectOutreachOpsQueue` sheet section.
- The clicked-card workflow now rolls channel drift, reply monitor gaps, sequence pauses, next email due state, Poplar/Resend provider needs, and Poplar/Resend payload preflight issues into compact operator action rows.
- This improves the Outreach Ops surface without enabling sends, provider calls, CRM writes, or reply automation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 00:10 ET heartbeat update:
- Added `PipelineCardOutreachSummary` so Kanban cards surface the top derived Outreach Ops queue action before opening the prospect sheet.
- Outreach/staged/sent cards now show compact counts and owners for channel drift, reply monitor, provider, pause, next-due, or payload issues.
- This replaces the older generic card outreach box with the same richer `outreachQueue` model used in the sheet.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 00:55 ET heartbeat update:
- Added derived `noteActions` state and expanded `ProspectNoteHealth` with a Stale Note Action Model.
- CRM v2 now models future controlled actions for old notes/blockers: revalidate, mark stale, convert to current blocker, classify non-blocking UX, resolve, and override.
- These are read-only action rows with explicit write policy; no CRM writes, Paperclip mutations, or note closures were performed.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 01:40 ET heartbeat update:
- Added `PipelineCardNoteSummary` so Kanban cards show stale-note/blocker policy directly on the board.
- The previous generic Paperclip card block is now driven by `noteHealth` and `noteActions`, making it clear that old notes are not automatic blockers unless revalidated with current evidence.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 02:25 ET heartbeat update:
- Added derived `routingContract` state and a new `ProspectRoutingContract` sheet section.
- The clicked-card routing surface now explicitly models the new prospect process: CRM record, Paperclip parent issue, Bruce evidence packet, Codex R1VS packet, R1VS return packet, and Post-Build route.
- This keeps R1VS scoped to structured packet execution and keeps CRM truth/routing with Codex/Paperclip in the lab model.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 03:10 ET heartbeat update:
- Added `PipelineCardRoutingSummary` so Kanban cards now surface the top CRM/Paperclip/Bruce/Codex/R1VS routing contract issue before opening the sheet.
- Cards now expose the next owner and compact routing chips from the same derived `routingContract` model used in the prospect detail.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 03:55 ET heartbeat update:
- Added derived `actionStack` state and a new `ProspectActionStack` sheet section.
- The sheet now merges routing, readiness gates, Jesse review checks, Outreach Ops, stale-note handling, and stage policy into a single prioritized read-only next-action list.
- This reduces operator ambiguity without enabling execution, CRM writes, sends, or Paperclip mutations.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 04:40 ET heartbeat update:
- Extracted action-stack derivation into `src/app/lab/crm-v2/action-stack.ts`.
- This keeps `derive.ts` from absorbing every derived model responsibility as CRM v2 grows and makes the prioritized next-action stack easier to test/refactor independently.
- No behavior change, CRM write, send, deploy, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 05:25 ET heartbeat update:
- Extracted routing-contract derivation into `src/app/lab/crm-v2/routing-contract.ts`.
- This keeps the new-prospect CRM/Paperclip/Bruce/Codex/R1VS/Post-Build handoff model isolated from the main prospect derivation flow.
- No behavior change, CRM write, send, deploy, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 06:10 ET heartbeat update:
- Extracted stale-note action derivation into `src/app/lab/crm-v2/stale-notes.ts`.
- This isolates the 7-day stale-note policy action model from the main prospect derivation flow and keeps note/blocker handling easier to evolve.
- No behavior change, CRM write, send, deploy, note closure, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 06:55 ET heartbeat update:
- Extracted Outreach Ops queue derivation into `src/app/lab/crm-v2/outreach-ops.ts` and shared date formatting into `src/app/lab/crm-v2/format.ts`.
- This isolates reply monitor, sequence pause, provider state, payload preflight, next-due, and half-sent mismatch logic from the main prospect derivation flow.
- No behavior change, CRM write, send, provider call, deploy, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 07:40 ET heartbeat update:
- Extracted Jesse review checklist derivation into `src/app/lab/crm-v2/review-checklist.ts`.
- This isolates desktop/mobile/site/claim/hero/reviews/popup/postcard/email/blocker review logic from the main prospect derivation flow.
- No behavior change, CRM write, send, deploy, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 08:25 ET heartbeat update:
- Extracted provider truth and payload preflight derivation into `src/app/lab/crm-v2/provider-preflight.ts`.
- This isolates Poplar/Resend/hello@gtmdot.com provider truth and Poplar/Resend dry-run payload checks from the main prospect derivation flow.
- No behavior change, CRM write, send, provider call, deploy, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 09:10 ET heartbeat update:
- Extracted build-handoff derivation into `src/app/lab/crm-v2/build-handoff.ts`.
- This isolates the intake/evidence/R1VS packet/R1VS return/Post-Build QA handoff model from the main prospect derivation flow.
- No behavior change, CRM write, send, deploy, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 09:55 ET heartbeat update:
- Moved Outreach timeline and Outreach health derivation into `src/app/lab/crm-v2/outreach-ops.ts` beside the Outreach Ops queue derivation.
- This consolidates outreach stage/channel/provider/reply/pause/next-due state in one module and further reduces the size of `derive.ts`.
- No behavior change, CRM write, send, provider call, deploy, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 10:40 ET heartbeat update:
- Extracted stage transition derivation into `src/app/lab/crm-v2/stage-transition.ts`.
- This isolates CRM stage recommendation, backward-move blocker policy, Jesse approval requirements, and read-only CRM write policy from the main prospect derivation flow.
- No behavior change, CRM write, send, deploy, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 11:25 ET heartbeat update:
- Extracted prospect preflight action derivation into `src/app/lab/crm-v2/preflight-actions.ts`.
- This isolates inspection, feedback, rescan, site approval, and final channel send action policy from the main prospect derivation flow.
- The extracted actions remain read-only lab rows; no approval, CRM write, send, provider call, deploy, or Paperclip mutation occurred.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 12:10 ET heartbeat update:
- Extracted Paperclip coordination derivation into `src/app/lab/crm-v2/paperclip-coordination.ts`.
- This isolates parent issue, blocker, artifact, next-owner, and coordination-link policy from the main prospect derivation flow.
- No behavior change, CRM write, Paperclip mutation, send, deploy, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 12:55 ET heartbeat update:
- Extracted queue signal derivation into `src/app/lab/crm-v2/queue-signals.ts`.
- This isolates next-action/exception queue logic for intake, R1VS packets, Post-Build QA, contact recovery, needs-decision, approval sessions, blocker revalidation, outreach preflight, channel mismatch, and Outreach Ops.
- No behavior change, CRM write, Paperclip mutation, send, deploy, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 13:40 ET heartbeat update:
- Extracted readiness gate derivation into `src/app/lab/crm-v2/readiness-gates.ts`.
- This isolates preview, slug, claim code, contact, blocker, Jesse site approval, postcard, email, and final channel approval gates from the main prospect derivation flow.
- No behavior change, CRM write, Paperclip mutation, send, deploy, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 14:25 ET heartbeat update:
- Extracted channel state derivation into `src/app/lab/crm-v2/channel-state.ts`.
- This isolates email, postcard, reply, and SMS channel-state truth from the main prospect derivation flow while preserving the stage-vs-channel separation that CRM v2 is built around.
- No behavior change, CRM write, Paperclip mutation, send, deploy, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 15:10 ET heartbeat update:
- Extracted note health derivation into `src/app/lab/crm-v2/note-health.ts`.
- This isolates CRM note/task count interpretation, stale-note blocking disposition, last-verified gaps, and evidence-state messaging from the main prospect derivation flow.
- No behavior change, CRM write, note closure, Paperclip mutation, send, deploy, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 15:55 ET heartbeat update:
- Extracted lifecycle state derivation into `src/app/lab/crm-v2/lifecycle-state.ts`.
- This isolates route-state mapping, top-level next-action selection, Paperclip blocker summary text, and stale-note policy text from the main prospect derivation flow.
- No behavior change, CRM write, note closure, Paperclip mutation, send, deploy, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 16:40 ET heartbeat update:
- Extracted board view filters into `src/app/lab/crm-v2/view-filters.ts`.
- This isolates all/new-intake/build/enrichment/approval/decision/blocked/outreach-ready/half-sent/contact-recovery/outreach filtering, channel mismatch detection, and contact-recovery checks from the prospect view builder.
- Updated sandbox, stats, PipelineCard, and PipelineColumn imports to use the new filter module.
- No behavior change, CRM write, Paperclip mutation, send, deploy, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 17:25 ET heartbeat update:
- Extracted readiness summary derivation into `src/app/lab/crm-v2/readiness-summary.ts`.
- This isolates readiness score, readiness label, top gate selection, and prospect attention detection from the prospect view builder.
- No behavior change, CRM write, Paperclip mutation, send, deploy, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 18:10 ET heartbeat update:
- Expanded board acceptance coverage in `src/app/lab/crm-v2/stats.ts` and `src/app/lab/crm-v2/components/BoardAcceptanceCoverage.tsx`.
- The cockpit now tracks coverage for routing, channels, providers, replies, payload preflight, stale notes, next action, action stack, review checklist, and Paperclip coordination.
- No CRM write, Paperclip mutation, send, deploy, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 18:55 ET heartbeat update:
- Added CRM v2 field/API contract modeling in `src/app/lab/crm-v2/field-contract.ts`.
- Added `ProspectFieldContract` to the prospect sheet so preserved CRM v1 fields and additive v2 field groups are visible per prospect.
- The contract explicitly preserves stage/contact/site/claim/email sequence/postcard/note-count fields while marking additive needs for note evidence, Paperclip links, provider events, reply monitor, payload preflight, and claim lookup.
- No CRM write, Paperclip mutation, send, deploy, migration, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 19:40 ET heartbeat update:
- Added field-contract visibility to the CRM v2 cockpit acceptance strip and additive field-gap KPI.
- `stats.ts` now counts field contract coverage and totals additive CRM v2 gaps across visible prospects.
- `BoardAcceptanceCoverage` now includes Field contract coverage; `CockpitHeader` now shows Additive field gaps as a migration-contract KPI.
- No CRM write, Paperclip mutation, send, deploy, migration, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 20:25 ET heartbeat update:
- Added `PipelineCardFieldContractSummary` and wired it into the Kanban card.
- Cards now surface the top additive CRM v2 field gap and preserved/additive field chips before opening the prospect sheet.
- No CRM write, Paperclip mutation, send, deploy, migration, or provider call.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 21:10 ET heartbeat update:
- Added slug/claim integrity modeling in `src/app/lab/crm-v2/slug-claim-integrity.ts`.
- Added `ProspectSlugClaimIntegrity` to the prospect sheet so CRM slug, preview slug alignment, claim code, claim lookup readiness, screenshot asset, and outreach slug proof are visible before approval/outreach.
- Claim lookup remains explicitly read-only/planned; no live claim lookup, CRM write, send, deploy, migration, or Paperclip mutation occurred.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 21:55 ET heartbeat update:
- Added slug/claim visibility to the CRM v2 cockpit and Kanban cards.
- `stats.ts` now counts slug/claim gaps and slug/claim coverage; `BoardAcceptanceCoverage` includes Slug / claim; `CockpitHeader` includes a Slug/claim gaps KPI.
- Added `PipelineCardSlugClaimSummary` so each card surfaces claim lookup, slug alignment, screenshot, and outreach slug proof gaps before opening the sheet.
- No live claim lookup, CRM write, send, deploy, migration, provider call, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 22:40 ET heartbeat update:
- Added approval-session modeling in `src/app/lab/crm-v2/approval-session.ts`.
- Prospect views now derive a 15-minute Jesse approval recommendation: approve site, flag feedback, rescan contact, or hold not ready.
- Updated `ProspectApprovalPanel` with approval-session status, blockers, write policy, and fast feedback prompts for mobile layout, hero context, reviews/content, popup/claim bar, postcard rendering, email copy, claim code, and current blockers.
- Added `PipelineCardApprovalSessionSummary`; cockpit stats now count approval-session coverage and approval-ready prospects.
- No CRM write, Paperclip mutation, send, deploy, migration, provider call, or claim lookup.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-24 23:25 ET heartbeat update:
- Added structured feedback intake modeling in `src/app/lab/crm-v2/feedback-intake.ts`.
- Prospect views now derive feedback presets, severity, owner, evidence requirement, and Paperclip action policy for popup timing, hero mismatch, missing reviews, wrong icon, bad postcard, claim bar, mobile layout, and email copy.
- Added `ProspectFeedbackIntake` with lab-only screenshot/markup drop zone and explicit no-write/no-upload policy.
- Added `PipelineCardFeedbackSummary`; cockpit stats now count feedback attention prompts and feedback intake coverage.
- No CRM write, upload, note write, Paperclip mutation, send, deploy, migration, provider call, or claim lookup.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 00:10 ET heartbeat update:
- Expanded CRM v2 operational alerts in `src/app/lab/crm-v2/stats.ts`.
- Ops bell now includes structured feedback prompts, slug/claim gaps, and field-contract gaps in addition to approval, contact recovery, channel mismatch, outreach exceptions, stale blockers, and build handoffs.
- These alerts only route to existing read-only board filters; no write, upload, send, deploy, migration, provider call, claim lookup, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 00:55 ET heartbeat update:
- Expanded `AlertBell` so the Ops bell now renders up to seven alerts instead of hiding all but three.
- Added scroll handling and a hidden-alert footer so v2-specific alerts such as feedback, slug/claim, and field-contract gaps remain visible without overwhelming the cockpit.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 01:40 ET heartbeat update:
- Added exact read-only saved views for `feedback_attention`, `slug_claim`, and `field_contract`.
- Updated view filtering so feedback prompts, slug/claim integrity gaps, and additive field-contract gaps have dedicated board queues instead of routing through broad approval/blocked views.
- Retargeted Ops bell alerts for feedback, slug/claim, and field-contract gaps to the new exact filters.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 02:30 ET heartbeat update:
- Added first-class intake evidence modeling in `src/app/lab/crm-v2/intake-evidence.ts`.
- Prospect views now derive source-link readiness, grounded intake facts, R1VS packet policy, and exact next action before build handoff.
- Added `ProspectIntakeEvidence` to the prospect sheet and `PipelineCardIntakeEvidenceSummary` to Kanban cards so early-stage evidence gaps are visible without relying on the old opaque intake/enrichment flow.
- Added `intake_evidence` as a read-only saved pipeline view, cockpit operator metric, board acceptance coverage item, and Ops bell alert target.
- The derivation tolerates current CRM string fields and future string-array variants for GBP features/photo highlights.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 03:15 ET heartbeat update:
- Added lab-only R1VS packet preview modeling in `src/app/lab/crm-v2/r1vs-packet.ts`.
- Prospect views now derive required packet inputs, missing packet gap count, packet sections, preview payload lines, next action, and no-write/no-invention policy from existing read-only CRM fields and intake evidence.
- Added `ProspectR1VSPacketPreview` to the prospect sheet and `PipelineCardR1VSPacketSummary` to Kanban cards so the build handoff shows what would be sent before Codex/Paperclip creates an actual packet.
- Added R1VS packet coverage/gap stats, a cockpit KPI, a board acceptance item, an Ops bell alert, and build-view filtering for packet gaps.
- Action stack now includes R1VS packet issues as a first-class `Packet` source before gate/review/outreach work.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 03:55 ET heartbeat update:
- Added approval/audit trail preview modeling in `src/app/lab/crm-v2/approval-audit.ts`.
- Prospect views now derive read-only audit records for stage recommendations, forward gates, backward blocker creation, Jesse approval locks, stale-note disposition, final channel approval, and CRM write lock policy.
- Added `ProspectApprovalAudit` to the prospect sheet and `PipelineCardApprovalAuditSummary` to Kanban cards so manual approval requirements and future Paperclip/CRM write evidence are visible before any live action exists.
- Added audit preview coverage, audit-item cockpit KPI, and Ops bell alerting for audit records that need disposition.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 04:40 ET heartbeat update:
- Added email sequence safety modeling in `src/app/lab/crm-v2/sequence-safety.ts`.
- Prospect views now derive sequence send safety checks for email address, reply monitor proof, reply/pause mismatch, bounce/delivery state, next due date, pause reason, and final email approval.
- Added `ProspectSequenceSafety` to the prospect sheet and `PipelineCardSequenceSafetySummary` to Kanban cards so follow-up safety, pause state, and “do not send” reasons are visible without sending or writing anything.
- Added sequence safety coverage, cockpit KPI, and Ops bell alerting for sequence safety items.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 05:25 ET heartbeat update:
- Added board-clearing priority modeling in `src/app/lab/crm-v2/board-clearance.ts`.
- Prospect views now derive closest-to-revenue rank, operator lane, safe-without-Jesse flag, Jesse approval requirement, reason, and exact next action.
- Added `ProspectBoardClearance` to the prospect sheet and `PipelineCardBoardClearanceSummary` to Kanban cards so each card shows whether it is revenue-adjacent, ops-safe, blocked, build-prep, or outreach-monitoring.
- Pipeline columns now sort cards by board-clearing rank within each CRM stage so the most actionable/revenue-adjacent items appear first without replacing stage truth.
- Added board-clearing coverage, “closest to revenue” operator metric, ops-safe KPI, and Ops bell alerting for final approval candidates.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 06:10 ET heartbeat update:
- Added Jesse review proof-pack modeling in `src/app/lab/crm-v2/review-proof-pack.ts`.
- Prospect views now derive a compact proof bundle for desktop site, mobile site, claim code, hero context, source-grounded copy, popup/claim bar, postcard rendering, email preview, feedback capture, and blocker disposition.
- Added `ProspectReviewProofPack` to the prospect sheet and `PipelineCardReviewProofSummary` to Kanban cards so the 15-minute review flow shows the minimum approval proof before Jesse approves or flags work.
- Added review proof coverage, review proof gap KPI, and Ops bell alerting for incomplete approval proof.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 06:55 ET heartbeat update:
- Added direct-mail/postcard safety modeling in `src/app/lab/crm-v2/postcard-safety.ts`.
- Prospect views now derive postcard safety checks for mailing address, Poplar payload, postcard rendering/proof, final postcard approval, CRM postcard submitted state, Poplar provider state, and slug/claim/QR integrity.
- Added `ProspectPostcardSafety` to the prospect sheet and `PipelineCardPostcardSafetySummary` to Kanban cards so postcard send readiness is visibly separate from viewing proof and from CRM lifecycle stage.
- Added postcard safety coverage, postcard safety KPI, and Ops bell alerting for direct-mail safety items.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, R1VS routing, Poplar submit, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for route verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 07:40 ET heartbeat update:
- Added contact recovery modeling in `src/app/lab/crm-v2/contact-recovery.ts`.
- Prospect views now derive per-field recovery checks for mailing address, email, phone, owner/contact name, and source evidence, including which outreach channel each gap blocks.
- Added `ProspectContactRecovery` to the prospect sheet and `PipelineCardContactRecoverySummary` to Kanban cards so deep rescan candidates are explicit and evidence-based.
- Added contact recovery coverage, contact recovery KPI, and updated Ops bell contact recovery counts from item-level recovery state.
- No CRM write, upload, send, deploy, migration, provider call, claim lookup, R1VS routing, enrichment execution, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 08:25 ET heartbeat update:
- Added CRM v2 migration readiness modeling in `src/app/lab/crm-v2/migration-readiness.ts`.
- Prospect views now derive cutover checks for preserved CRM v1 fields, additive v2 fields, Paperclip links, provider events, reply monitor, payload preflight, claim lookup, and write-lock policy.
- Added `ProspectMigrationReadiness` to the prospect sheet and `PipelineCardMigrationReadinessSummary` to Kanban cards so v2 replacement blockers remain visible while the lab evolves.
- Added migration readiness coverage, migration blocker KPI, and Ops bell alerting tied to field-contract/cutover work.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 09:10 ET heartbeat update:
- Added column workload modeling in `src/app/lab/crm-v2/column-workload.ts`.
- Pipeline columns now derive stage-level workload summaries for revenue candidates, Jesse gates, ops-safe items, build prep, contact recovery, review proof, postcard safety, email safety, channel drift, and migration blockers.
- Updated `PipelineColumn` headers to show the top action and the most relevant workload counts per stage, while keeping stage truth and card-level ranking unchanged.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 09:55 ET heartbeat update:
- Added prospect sheet triage modeling in `src/app/lab/crm-v2/sheet-triage.ts`.
- Added `ProspectSectionTriage` near the top of the prospect sheet so the long detail drawer ranks urgent sections before the operator scrolls.
- The triage index currently ranks board clearing, review proof, contact recovery, postcard safety, email sequence safety, stale notes, approval audit, R1VS packet, migration readiness, and field contract.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for route verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 10:40 ET heartbeat update:
- Added board-level operator handoff modeling in `src/app/lab/crm-v2/board-operator-handoff.ts`.
- Added `BoardOperatorHandoff` above the Kanban so the cockpit ranks the top prospects to open first from current read-only derived state.
- Handoff ranking prioritizes revenue-adjacent prospects, Jesse approval/review proof, postcard/email safety, contact recovery, R1VS packet gaps, stale-note revalidation, and migration blockers.
- Handoff cards open the existing prospect sheet only; no stage move, send, CRM write, provider call, R1VS routing, or Paperclip mutation occurs.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 11:25 ET heartbeat update:
- Added board-level coordinator brief modeling in `src/app/lab/crm-v2/board-coordinator-brief.ts`.
- Added `BoardCoordinatorBrief` above the operator handoff and Kanban so the cockpit summarizes closest-to-revenue prospects, safe-without-Jesse work, Jesse-gated work, active blockers, contact recovery, and migration hold items.
- The brief is read-only and intended for main coordinator/Jesse scanning; it does not open external workflows, write CRM, mutate Paperclip, send outreach, or replace the production board.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 12:10 ET heartbeat update:
- Added `DataSourceHealth` to the CRM v2 cockpit.
- The lab now displays `/api/prospects` read status, loaded prospect count, currently visible/filter count, load timestamp, and API error state before the coordinator brief and Kanban.
- Fetch handling now distinguishes non-OK API responses from a legitimately empty board, reducing the risk of treating data-source failure as CRM truth.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 12:55 ET heartbeat update:
- Added derived prospect search indexing in `src/app/lab/crm-v2/prospect-search.ts`.
- Board search now matches across company, slug, stage, claim code, contact data, channel state, blocker/safety terms, review proof, queue signals, action stack, slug/claim checks, contact recovery checks, and next-action language.
- Updated the cockpit search placeholder to reflect operator use cases beyond company lookup.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 13:40 ET heartbeat update:
- Tightened Kanban card rank explainability in `PipelineCardBoardClearanceSummary`.
- Each card now exposes the board-clearing rank basis, why it is in that lane, operator mode, Jesse-gate vs ops-safe status, and top derived action/signal without opening the prospect sheet.
- This keeps the Kanban-first board closer to the operating need: quickly decide what should be opened, advanced locally, held, or routed for Jesse approval.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 14:25 ET heartbeat update:
- Added `ProspectFooterDecisionStrip` to the prospect sheet footer.
- The drawer now keeps stage decision context visible beside the read-only action bar: current stage, recommended stage, blocker count, Jesse approval count, CRM write-lock status, forward rule, and backward/Paperclip blocker rule.
- This directly supports manual stage review without implying the sandbox can perform live CRM writes.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 15:10 ET heartbeat update:
- Added `channel-command.ts` and `ProspectChannelCommandCenter`.
- The prospect sheet now has a compact channel command center before the detailed channel panels, with one row each for postcard, email, reply, and SMS/future.
- Each row separates CRM truth, provider truth, payload/gate truth, mismatch status, and exact next action so outreach decisions do not depend on pipeline stage alone.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 15:55 ET heartbeat update:
- Added `note-disposition.ts` and `ProspectStaleNoteDisposition`.
- The prospect sheet now surfaces stale-note disposition near the top of the drawer, before slug/claim and channel sections.
- The panel shows note age availability, default blocker status, current evidence state, recommended disposition, and Paperclip blocker rule so old notes do not silently hold the board.
- Current CRM still exposes note/task counts only; v2 continues to flag note-level age, last verified date, evidence link, status, owner, and blocking flag as additive field/API needs.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 16:40 ET heartbeat update:
- Added `review-session.ts` and `ProspectReviewSession`.
- The prospect sheet now surfaces a compact 15-minute review session immediately after the command summary, before the long triage/detail sections.
- The session orders desktop, mobile, claim, content fit, outreach proofs, and decision capture, then separates approve, feedback, and rescan paths.
- This makes the clicked-card workflow closer to Jesse's operating need: quickly inspect, approve if clean, or capture structured feedback/rescan without confusing site approval with outreach send approval.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 17:25 ET heartbeat update:
- Added `board-review-queue.ts` and `BoardReviewQueue`.
- The cockpit now surfaces a Jesse Review Queue between the coordinator brief and general operator handoff.
- The queue ranks prospects that are in/near approval, shows review-ready vs needs-work counts, and opens the existing read-only prospect sheet for the 15-minute review session.
- This keeps approval triage separate from broader ops cleanup and preserves the rule that site approval, stage writes, and channel sends remain locked.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 18:10 ET heartbeat update:
- Added `board-outreach-queue.ts` and `BoardOutreachQueue`.
- The cockpit now surfaces an Outreach Exception Queue after the Jesse Review Queue and before the general operator handoff.
- The queue aggregates prospect-level outreach queue items for reply monitoring, sequence pause risk, half-sent channel drift, Poplar/Resend provider gaps, and payload preflight issues.
- Queue cards open the existing read-only prospect sheet; they do not send, resume sequences, write CRM, or call providers.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 18:55 ET heartbeat update:
- Added `board-intake-queue.ts` and `BoardIntakeQueue`.
- The cockpit now surfaces an Intake / R1VS Routing Queue after the coordinator brief and before review/outreach queues.
- The queue highlights intake evidence gaps, R1VS packet readiness, blocked packet inputs, next owner, and next routing action.
- This reinforces the new prospect contract: Codex/Paperclip owns routing, Bruce produces evidence, and R1VS receives structured packets only.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for route verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 19:40 ET heartbeat update:
- Added `board-stale-note-queue.ts` and `BoardStaleNoteQueue`.
- The cockpit now surfaces a Stale Note Cleanup Queue after outreach exceptions and before the general operator handoff.
- The queue ranks prospects with historical/open note counts, recommended disposition, evidence-state gaps, and revalidation next action.
- This keeps the 7-day stale-note policy operational: old notes do not block by default, and conversion to a current blocker requires fresh evidence.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 20:25 ET heartbeat update:
- Added `board-slug-claim-queue.ts` and `BoardSlugClaimQueue`.
- The cockpit now surfaces a Slug / Claim Integrity Queue after intake routing and before review/outreach queues.
- The queue ranks CRM slug gaps, missing claim codes, preview URL slug drift, claim lookup needs, and outreach QR/CTA proof needs.
- This makes slug/claim drift visible before Jesse review or final channel approval, while keeping claim lookup/register/write behavior read-only and locked in the lab.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 21:10 ET heartbeat update:
- Added `board-contact-recovery-queue.ts` and `BoardContactRecoveryQueue`.
- The cockpit now surfaces a Contact Recovery Queue after intake routing and before slug/review/outreach queues.
- The queue ranks address, email, phone, and source-evidence gaps, identifies blocked channels, and opens the existing read-only prospect sheet for deeper rescan context.
- This supports Jesse's requested “rescan address/email/phone” workflow while preserving the boundary that rescans produce evidence packets only and do not write CRM truth.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 21:55 ET heartbeat update:
- Added `board-proof-queue.ts` and `BoardProofQueue`.
- The cockpit now surfaces a Proof / Asset Preflight Queue before the Jesse Review Queue.
- The queue ranks missing/blocked review proof packs, postcard renderings, email previews, screenshots, postcard safety gates, and email sequence safety gates.
- This keeps proof/rendering gaps visible before Jesse review or outreach approval, without generating assets, calling providers, sending, or writing CRM.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 22:40 ET heartbeat update:
- Added `board-command-index.ts` and `BoardCommandIndex`.
- The cockpit now shows a Command Queue Index after the coordinator brief and before the specialized queues.
- The index summarizes queue order, active counts, owner lane, first queue to start with, and top next action for intake, contact recovery, slug/claim, proof/assets, Jesse review, outreach exceptions, and stale notes.
- This reduces cockpit ambiguity as specialized queues grow and keeps the operator flow explicit without triggering writes, sends, provider calls, R1VS dispatch, or Paperclip mutations.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-25 23:25 ET heartbeat update:
- Added stable in-page queue anchors and jump links to the Command Queue Index.
- Index tiles now jump to Intake/R1VS, Contact Recovery, Slug/Claim, Proof/Assets, Jesse Review, Outreach Exceptions, Stale Notes, or the fallback Pipeline Board.
- Added matching `id`/`scroll-mt` targets to each cockpit queue section and the Kanban board.
- This makes the expanded cockpit easier to operate without adding live writes, sends, provider calls, R1VS dispatch, or Paperclip mutations.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 00:10 ET heartbeat update:
- Added `board-migration-queue.ts` and `BoardMigrationQueue`.
- The cockpit now surfaces a Field Contract / Migration Queue before the general operator handoff.
- The queue ranks cutover risks around preserved CRM v1 behavior, additive v2 field groups, provider event separation, reply monitoring, claim lookup, payload preflight, Paperclip links, and write-lock policy.
- Added this queue to the Command Queue Index as the eighth command surface with a stable anchor.
- This keeps CRM v2 replacement/cutover requirements visible while preserving the lab-only/no-write/no-migration boundary.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 00:55 ET heartbeat update:
- Refined `BoardAcceptanceCoverage` in the CRM v2 cockpit header.
- Acceptance coverage now shows a summary of fully represented, partial, and missing CRM v2 requirement surfaces instead of raw counters only.
- Individual coverage chips now visually distinguish full, partial, and missing representation across the current prospect set.
- This makes lab completeness and migration readiness easier to evaluate without treating the sandbox as production-ready.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for route verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 01:40 ET heartbeat update:
- Added `launch-readiness.ts` and `BoardLaunchReadiness`.
- The cockpit now shows a Launch Readiness Lock immediately after Data Source Health and before coordinator/queue triage.
- The panel explicitly tracks read-only lock, data loading, migration blockers, provider truth, reply monitor, proof gates, manual approval policy, and production cutover approval.
- This makes the sandbox-only boundary visible before any operator uses the board and prevents the current UI progress from being mistaken for production replacement readiness.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 02:30 ET heartbeat update:
- Added `board-owner-workload.ts` and `BoardOwnerWorkload`.
- The cockpit now shows an Owner Workload Split after Launch Readiness and before the coordinator brief/command index.
- The panel derives Jesse, Codex, Bruce, Outreach, Paperclip, R1VS, and Post-Build lane counts from read-only action stacks, review gates, contact recovery, outreach queues, Paperclip state, routing models, and post-build handoff state.
- This gives the main coordinator a fast owner-by-owner split of what needs attention without opening every queue or implying live assignment/mutation.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 03:15 ET heartbeat update:
- Added `board-next-action-queue.ts` and `BoardNextActionQueue`.
- The cockpit now shows a Next Action Worklist immediately after the Command Queue Index.
- The worklist ranks the single next useful action per prospect, with owner, stage, source, reason, safe-ops vs Jesse-gated status, and open-prospect behavior.
- Added the Next Action surface to `BoardCommandIndex` as the first command queue so operators have a clear starting point before drilling into specialized intake/contact/slug/proof/review/outreach/stale-note/migration queues.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 03:55 ET heartbeat update:
- Added `ProspectNextActionPanel` and reused the shared `deriveProspectNextAction` logic inside the prospect drawer.
- The prospect sheet now opens with the current next action, owner, priority, source, stage, safe-ops vs Jesse-gated boundary, and read-only lab policy before the deeper routing/review/outreach sections.
- This aligns the board worklist and prospect detail hierarchy so an operator can open a card and immediately see the same action the cockpit ranked.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 04:40 ET heartbeat update:
- Added `PipelineCardNextActionSummary` and wired it into the Kanban card hierarchy.
- Pipeline cards now use the same shared `deriveProspectNextAction` logic as the Next Action Worklist and the prospect drawer.
- The old generic card-level `Next:` block was removed so card/detail/worklist state now presents one consistent next action with owner, source, priority, and Jesse-gated vs ops-safe boundary.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 05:25 ET heartbeat update:
- Enhanced `column-workload.ts` and `PipelineColumn`.
- Each Kanban stage column now derives a first-prospect-to-open signal from the same shared next-action model used by the worklist, cards, and prospect drawer.
- Column headers now show the highest-priority prospect, owner, source, and next action for that stage, alongside existing workload/category counts.
- This makes the Kanban board more usable for board clearing: the operator can scan a lane and immediately know which card to open first without guessing from stage alone.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 06:10 ET heartbeat update:
- Added `PipelineCardChannelTruthSummary` and wired it into `PipelineCard`.
- Kanban cards now show a compact channel-truth strip for postcard, email, and reply state, plus top provider-source chips for CRM/Postcard/Poplar/Resend/hello@gtmdot.com truth where available.
- This makes the core CRM v2 distinction visible on the card: pipeline stage is not channel truth, and provider truth can differ from CRM event truth.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 06:55 ET heartbeat update:
- Added `ProspectProviderTruthMatrix` and wired it into the prospect sheet immediately after the Channel Command Center.
- The drawer now surfaces CRM stage/event truth, Poplar, Resend, hello@gtmdot.com reply monitoring, and Poplar/Resend payload preflight in one compact pre-decision matrix.
- This keeps provider-vs-CRM drift, reply-monitor proof, and payload validation visible before channel approval or outreach action review.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for route verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 07:40 ET heartbeat update:
- Added `board-feedback-queue.ts` and `BoardFeedbackQueue`.
- The cockpit now surfaces a Feedback Capture Queue between Proof / Asset Preflight and Jesse Review.
- The queue ranks prospects with structured feedback prompts needing attention, including blocking prompts, screenshot/evidence requirements, owner, severity, and recommended Paperclip action.
- Added Feedback Capture to `BoardCommandIndex` so hero mismatch, mobile layout, popup timing, claim bar, postcard rendering, and email-copy issues are visible before opening every card.
- No CRM write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, file upload, feedback submission, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 08:25 ET heartbeat update:
- Added `board-stage-queue.ts` and `BoardStageQueue`.
- The cockpit now surfaces a Stage Recommendation Queue after Jesse Review and before Outreach Exceptions.
- The queue ranks recommendation-only stage movements, showing current stage, recommended stage, forward/backward/hold classification, blocker count, approval count, next action, and CRM write lock.
- Added Stage Recommendations to `BoardCommandIndex`, preserving the policy that backward movement requires a current Paperclip blocker with reason, owner, and evidence, and live CRM writes still require Jesse approval.
- No CRM write, stage write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, feedback submission, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 09:10 ET heartbeat update:
- Added `ProspectStaleNoteActionRail`.
- The prospect sheet now shows a lab-only stale-note action rail directly after stale-note disposition, covering revalidate, mark stale, convert to current blocker, classify non-blocking UX, resolve, and override.
- Each action shows availability, state, evidence/detail guidance, and future write policy so old notes remain preserved but do not block without fresh verification.
- No CRM write, note write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, feedback submission, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 09:55 ET heartbeat update:
- Added `board-reply-monitor-queue.ts` and `BoardReplyMonitorQueue`.
- The cockpit now surfaces a dedicated Reply Monitor Queue after Outreach Exceptions and before Stale Note Cleanup.
- The queue isolates hello@gtmdot.com reply visibility, replied-but-sequence-active mismatch risk, sequence pause reason, bounce/provider state, and next-email due risk from the broader outreach exception queue.
- Added Reply Monitor to `BoardCommandIndex` so reply monitoring is visible as its own operational surface before any future sequence automation can be trusted.
- No CRM write, note write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, feedback submission, sequence resume, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 10:40 ET heartbeat update:
- Added `board-health-analytics.ts` and `BoardHealthAnalytics`.
- The cockpit now surfaces a Board Health Analytics panel immediately after Data Source Health and before Launch Readiness.
- The panel summarizes operating posture across safe ops pool, Jesse gates, blocked prospects, stage/channel drift, reply monitor risk, provider drift, payload preflight risk, and cutover blockers.
- This gives a compact analytics layer for board clearing without implying CRM writes, sends, provider calls, production cutover, or Paperclip mutations.
- No CRM write, note write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, feedback submission, sequence resume, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-26 11:25 ET heartbeat update:
- Added `pipeline-board-focus.ts` and `PipelineBoardFocusStrip`.
- The Kanban board now opens with a dedicated focus strip showing visible prospect count, first card to open, first next action, owner, safe-ops count, Jesse-gated count, channel drift, and stale-note risk.
- Refactored `PipelineBoard` so the focus strip sits above the horizontally scrolling stage columns, keeping Kanban as the primary operating surface even with the expanded cockpit queues.
- No CRM write, note write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, feedback submission, sequence resume, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.

2026-05-31 14:20 ET heartbeat update:
- Added `board-session-plan.ts` and `BoardSessionPlan`.
- The cockpit now surfaces an Operator Session Plan immediately after Board Health Analytics and before Launch Readiness.
- The plan derives a short first-pass work sequence from the shared next-action model, prioritizing blockers, Jesse-gated decisions, and safe ops work with owner, timebox, reason, boundary, and click-to-open behavior.
- Card opening uses prospect IDs rather than business names to avoid ambiguous matches.
- No CRM write, note write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, feedback submission, sequence resume, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for route verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-31 15:05 ET heartbeat update:
- Updated `ProspectCommandSummary`.
- The drawer command summary now uses the shared `deriveProspectNextAction` model instead of the older `prospect.nextAction` field, keeping drawer/card/worklist/session-plan next-action guidance aligned.
- Added an “Open this section first” block derived from `deriveSheetTriage`, so the long prospect drawer points to the most urgent section family before the operator scrolls.
- No CRM write, note write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, feedback submission, sequence resume, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning. The dev server was restarted on port 3001 for route verification, and `/lab/crm-v2` returned HTTP 200.

2026-05-31 15:50 ET heartbeat update:
- Added `getSheetSectionAnchor` to `sheet-triage.ts`.
- Updated `ProspectCommandSummary` and `ProspectSectionTriage` so their first-section/triage cards are real in-drawer links rather than static guidance.
- Added matching scroll anchors around the major prospect-sheet destinations: board clearing, R1VS packet, stale notes, review proof, approval audit, contact recovery, postcard safety, sequence safety, field contract, and migration readiness.
- This improves drawer usability without changing any CRM data, provider state, Paperclip state, or production behavior.
- No CRM write, note write, upload, send, deploy, migration, production replacement, provider call, claim lookup, R1VS routing, feedback submission, sequence resume, or Paperclip mutation.
- Verification: `npm run build` passed with the known unrelated vault trace warning, and `/lab/crm-v2` returned HTTP 200.
