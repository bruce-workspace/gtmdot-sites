# CRM v2 V2.1 Resume Checkpoint

Date: 2026-06-05
Owner: Codex / GTMDot quarterback
Mode: goal-active lab implementation

## Context

Jesse returned after a two-day internet outage and confirmed the CRM v2 preview looks strong. The V2.1 goal is active:

Ship CRM v2 V2.1 board-clearing workflow from lab preview toward a usable review system. Keep the board scannable, make the prospect drawer command-first, clearly separate current blockers from stale notes, provider truth, enrichment needs, and send readiness, and verify against real GTMDot prospects without production writes/sends/deploys unless separately approved.

## Current Implementation Work

Implemented lab-only V2.1 improvements in:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectCommandPanel.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectSheet.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/lab-labels.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineBoard.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineColumn.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/CockpitHeader.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/contact-recovery.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/model.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/preview-health.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/review-disposition.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/review-checklist.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/readiness-gates.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/preflight-actions.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sequence-safety.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/stage-transition.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/approval-session.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-clearance.ts`

## What Changed

### Prospect Drawer Command Center

Added a new command-first drawer panel.

The top of a prospect drawer now shows:

- Current next action.
- Owner.
- Source.
- approval boundary.
- Primary actions.
- Action authority labels.
- Recommended fix/enrichment route.

Primary actions are explicit:

- View site.
- View postcard.
- Needs Fix.
- Run enrichment / Request rescan.
- Approve for Outreach.
- Send postcard.
- Preview email.
- Hold.

Each action carries an authority class:

- View.
- Task.
- CRM write.
- Provider action.
- Contact action.

Locked actions explain what gate or approval is missing.

Provider-suppressed postcard cases now label the channel action as `Retry postcard` instead of generic `Send postcard`.

Already-submitted postcard cases now label the channel action as `Verify postcard` with `Provider action` authority instead of implying another send.

### Explicit Enrichment Jobs

Contact recovery now derives explicit enrichment jobs rather than a vague rescan action.

Current job types:

- Address deliverability.
- Email discovery.
- Phone verification.
- Owner/contact discovery.
- Source evidence discovery.

Each job includes:

- state.
- owner.
- input.
- expected output.
- write policy.
- fallback next action.

The command center now uses the primary enrichment job as the action label when relevant. Example: Premier TV Mounting shows `Email discovery` instead of generic `Run enrichment`.

### Footer Simplification

Removed the old large footer action stack from the prospect drawer default view. It was competing with the new command panel and recreating the "two CRMs stitched together" problem.

Footer is now a quiet lab guardrail:

- No CRM writes.
- No sends.
- No provider calls.
- No uploads.
- No Paperclip mutations.

### Out-Of-Pipeline Label

CRM v2 now relabels the underlying `dead` stage as `Out of Pipeline` in the lab UI without changing CRM data.

Purpose:

- Avoid treating old `dead` state as trusted final business truth.
- Make the column feel like disposition/reopen review.
- Preserve the existing CRM stage/API contract.

### Recheck Language Instead Of False Blocker Language

The board no longer labels note/task count risk as hard `Blockers` by default.

Changed lab copy:

- Header metric: `Blockers` -> `Recheck`.
- Saved filter chip: `Blockers` -> `Recheck`.
- Column signal: `blocked` -> `open items`.
- Card signal: `blockers` -> `open items`.
- Board clearance label: `Current blocker / stale-note check` -> `Recheck open items`.

Purpose:

- Align the UI with Jesse's stale-note policy.
- Avoid treating old/open task counts as proven current blockers.
- Preserve risk visibility without overstating certainty.

### Preview URL Health

CRM v2 no longer treats every preview URL as equally safe.

Added preview health derivation:

- Missing URL -> `Site missing`.
- `preview.gtmdot.com` proxy URL -> `Site needs live check`.
- URL slug mismatch -> `Site slug mismatch`.
- Pages preview URL with CRM slug -> `Site preview ready`.
- Non-standard URL -> `Site URL present`.

Purpose:

- Catch Raiden-style broken preview/proxy cases.
- Prevent "URL present" from being treated as "site verified."
- Push live-load verification into review and readiness gates.

### Review Disposition / Command Truth Table

Added a lab-only `reviewDisposition` model so the top of the prospect drawer answers the operator question directly:

- `approve_site`
- `approve_channel`
- `needs_fix`
- `run_enrichment`
- `provider_retry`
- `provider_verify`
- `site_health`
- `monitor`
- `hold`

Each disposition includes:

- label.
- tone.
- route.
- owner.
- primary action.
- approval boundary.
- evidence needed.
- next write target.

Purpose:

- Stop forcing Jesse to infer next action from stage alone.
- Separate "approve site" from "approve postcard-only" from "send/retry postcard."
- Make provider-suppressed postcards visibly different from real sent/submitted postcards.
- Keep missing email as an enrichment job without blocking postcard-only revenue when address/postcard path is viable.

### Postcard-Only And Provider-State Corrections

Fixed a derived-state bug where string matching treated `not_submitted` / `not submitted` as submitted/provider-active.

Updated behavior:

- `not_submitted` can no longer become `Verify postcard`.
- Provider-active labels require real submitted/production/transit/delivered state.
- Suppressed/failed/exception state becomes `Provider retry needed`.
- Postcard-only approval and send gates no longer fail solely because email is missing.
- Email sequence safety is inactive for postcard-only sent prospects with no email sequence.

### Board-Level Disposition Cards

Updated pipeline cards so the board itself shows the new command truth before the drawer opens.

Changed:

- Each card now includes a `reviewDisposition` chip above the older board-clearance chip.
- The primary card signal changed from generic lifecycle `Next` to `Command`, using `reviewDisposition.primaryAction`.
- Card footer now reflects the action route:
  - `Approve site review`
  - `Approve postcard-only`
  - `Provider retry path`
  - `Verify provider state`
  - `Needs fix/recheck`
  - `Needs enrichment`
  - `Live site check`
  - `Monitor outreach`

Purpose:

- Make the board scannable without opening every drawer.
- Let Jesse see whether a card needs approval, provider retry, site health, enrichment, or monitoring from the card itself.
- Reduce the "what am I supposed to do here?" stage-dropdown guessing loop.

### Disposition Filters And Queue

Added first-class disposition routing to the board controls and advanced queues.

New saved filters:

- `postcard_approval`: prospects whose exact route is `approve_channel`.
- `provider_retry`: prospects whose exact route is `provider_retry`.
- `site_health`: prospects whose exact route is `site_health`.

New advanced queue:

- `BoardDispositionQueue`
- Derived by `deriveBoardDispositionQueue`
- Groups prospects by exact `reviewDisposition.route`
- Shows owner, primary action, reason, approval boundary, evidence needed, and write target.

The command index now starts with the disposition queue before the older generic next-action queue.

Purpose:

- Let operators batch by exact action route.
- Make "approve postcard-only" and "provider retry" discoverable as queues, not just per-card labels.
- Keep route batching read-only and separate from CRM writes/provider calls.

### Disposition Acceptance Coverage

Added `reviewDispositionVisible` to CRM v2 lab acceptance coverage.

Purpose:

- Prove every prospect has an exact command route.
- Keep this visible as a migration/readiness acceptance surface alongside stale notes, provider truth, payloads, channels, and next action.

### Prospect Drawer Decision Snapshot

Added a compact `ProspectDecisionSnapshot` directly under the Command Center.

The snapshot separates the five lanes that decide whether a prospect can move:

- Current blockers.
- Stale/history notes.
- Provider truth.
- Enrichment.
- Send readiness.

Purpose:

- Make the drawer command-first beyond the top action buttons.
- Stop scattering the core decision across notes, provider, enrichment, and outreach panels.
- Keep missing email as enrichment when postcard-only progress is viable.
- Keep stale/history notes visible without treating them as proven current blockers.

## Verification

Build:

- `npm run build` passed.
- Existing unrelated Turbopack warning remains: `next.config.ts -> src/lib/vault.ts -> src/app/api/prospects/[id]/vault/route.ts`.
- Re-ran `npm run build` after review disposition, postcard-only, and sequence-safety changes; build passed with the same unrelated warning.

Browser preview:

- `http://localhost:3001/lab/crm-v2` loads.
- `/api/prospects` returns 67 prospects.
- Board shows `Out of Pipeline` instead of `Dead` in stage filter and board stage pills.
- Board shows `Recheck` instead of `Blockers` for open-item/stale-note risk.
- Thermys fixture opened successfully.
- Thermys drawer shows the new command center first with:
  - Needs Fix.
  - Run enrichment.
  - View site.
  - View postcard.
  - locked CRM write/send actions.
  - recommended Hero mismatch route.
- `24-hrs-mobile-tire-services` fixture shows `Postcard suppressed` on the card.
- `24-hrs-mobile-tire-services` drawer shows `Compare against Poplar provider events` and a locked `Retry postcard` action.
- Premier TV Mounting fixture shows `Email discovery` as the command action and recommended enrichment route.
- Browning fixture shows `Verify postcard locked` with `Provider action` authority because the postcard already has submitted state.
- Raiden fixture shows `Site needs live check` on the board because it uses the preview proxy URL.

Additional fixture truth-table verification:

- `tuxedo-mechanical-plumbing`: board `Recheck open items`; disposition `Recheck before approval`; approve/send actions locked until current open item is revalidated or reclassified.
- `rooter-pro-plumbing-drain`: board `Closest to revenue`; disposition `Approve postcard-only`; postcard-only approval available even though email is missing; send remains locked until channel approval/stage movement.
- `harrison-sons-electrical`: board `Outreach monitor`; disposition `Monitor sent outreach`; email sequence safety inactive with `0` blockers for postcard-only outreach.
- `24-hrs-mobile-tire-services`: board `Provider retry needed`; disposition `Provider retry needed`; sequence safety inactive with `0` blockers; postcard-only approval visible before any provider retry.
- `raiden-electrical`: disposition `Site health check first`; approve site locked until preview/live-site health is verified.
- `browning-electrical-services`: disposition `Provider verification`; approve site available, postcard resend locked because submitted/provider state must be reconciled first.

Additional board-card derived verification:

- `rooter-pro-plumbing-drain`: card chip `Approve postcard-only`; command `Review postcard proof and approve postcard-only if it is good enough.`
- `24-hrs-mobile-tire-services`: card chip `Provider retry needed`; command `Fix the provider/payload issue, then retry postcard only with named approval.`
- `harrison-sons-electrical`: card chip `Monitor sent outreach`; command `Monitor provider progression, replies, and follow-up safety.`
- `tuxedo-mechanical-plumbing`: card chip `Recheck before approval`; command `Revalidate current open item, then choose: stale/resolved, non-blocking UX, or current blocker.`
- `raiden-electrical`: card chip `Site health check first`; command `Verify the live preview opens and matches the CRM slug before asking Jesse to approve.`

Disposition queue/filter verification from current `/api/prospects`:

- Total prospects: `67`
- Disposition coverage: `67/67`
- Saved filter counts:
  - `postcard_approval`: `1`
  - `provider_retry`: `3`
  - `site_health`: `7`
- Queue counts:
  - `approve_site`: `3`
  - `approve_channel`: `1`
  - `needs_fix`: `20`
  - `run_enrichment`: `11`
  - `provider_retry`: `3`
  - `provider_verify`: `21`
  - `site_health`: `7`
  - `monitor`: `1`
  - `hold`: `0`
- First queue items:
  - `24-hrs-mobile-tire-services:provider_retry`
  - `atlanta-drywall-1:provider_retry`
  - `perez-pools-llc:provider_retry`
  - `rooter-pro-plumbing-drain:approve_channel`
  - `atlanta-plumber-for-less:site_health`

Decision Snapshot fixture verification:

- `rooter-pro-plumbing-drain`: current blocker lane `0`; stale/history `history:10`; provider/disposition `approve_channel`; enrichment `Email discovery`; send readiness `Approve postcard-only`.
- `24-hrs-mobile-tire-services`: current blocker lane `0`; stale/history `history:15`; provider/disposition `provider_retry`; enrichment `Email discovery`; send readiness `Approve postcard-only`.
- `harrison-sons-electrical`: current blocker lane `2`; stale/history `revalidate:6`; provider/disposition `provider_verify`; enrichment `Email discovery`; send readiness locked to `Monitor sent outreach`.
- `tuxedo-mechanical-plumbing`: current blocker lane `1`; stale/history `revalidate:13`; provider/disposition `needs_fix`; enrichment `none`; send readiness locked to `Recheck before approval`.
- `raiden-electrical`: current blocker lane `0`; stale/history `history:1`; provider/disposition `site_health`; enrichment `Email discovery`; send readiness locked to `Site health check first`.
- `premier-tv-mounting-atl`: current blocker lane `1`; stale/history `revalidate:8`; provider/disposition `needs_fix`; enrichment `Email discovery`; send readiness locked to `Recheck before approval`.

Dev preview note:

- `http://127.0.0.1:3001/lab/crm-v2` can black-screen in Next 16 dev because HMR/dev resources are blocked cross-origin from `127.0.0.1`.
- Use `http://localhost:3001/lab/crm-v2` for the local preview unless `allowedDevOrigins` is configured.

## 2026-06-05 Action Packet Slice

Implemented a lab-only `actionPacket` model and drawer component so each prospect can present the actual next operating packet rather than requiring Jesse/Codex to infer it from scattered stage, note, provider, and enrichment signals.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/action-packet.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectActionPacket.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/model.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/derive.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectSheet.tsx`

Each action packet includes:

- packet label.
- mode.
- owner.
- lab preview execution boundary.
- approval/instruction text.
- evidence checklist.
- safe actions now.
- blocked-by list.
- prohibited actions.
- next report sentence.

Packet routes now include:

- Postcard-only approval packet.
- Provider retry packet.
- Site health packet.
- Needs-fix packet.
- Enrichment evidence packet.
- Monitor / verify packet.
- Site approval packet.
- Hold packet.

Drawer quick actions are now derived from real `preflightActions` instead of a static all-locked placeholder. This means:

- `Approve postcard-only` can show available for postcard-ready/address-ready prospects even when email is missing.
- `Send postcard` stays locked until the correct approval/stage/provider gates are satisfied.
- Email approval/send paths remain locked unless email-specific requirements are satisfied.

Verified action packet fixtures from current `/api/prospects`:

- `rooter-pro-plumbing-drain`: disposition `approve_channel`; packet `Postcard-only approval packet`; owner `Jesse`; lab execution `false`; `Approve postcard-only` available; sends locked.
- `24-hrs-mobile-tire-services`: disposition `provider_retry`; packet `Provider retry packet`; owner `Outreach`; lab execution `false`; `Approve postcard-only` available; sends locked.
- `harrison-sons-electrical`: disposition `provider_verify`; packet `Monitor / verify packet`; owner `Outreach`; lab execution `false`; sends locked.
- `tuxedo-mechanical-plumbing`: disposition `needs_fix`; packet `Needs-fix packet`; owner `Post-Build`; lab execution `false`; approvals/sends locked.
- `raiden-electrical`: disposition `site_health`; packet `Site health packet`; owner `Codex`; lab execution `false`; approvals/sends locked.
- `premier-tv-mounting-atl`: disposition `needs_fix`; packet `Needs-fix packet`; owner `Post-Build`; lab execution `false`; approvals/sends locked.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- `http://localhost:3001/lab/crm-v2` returns 200.

## 2026-06-05 Structured Feedback / Operator Comment Packet Slice

Implemented a lab-only structured feedback packet so Jesse's review comments can become routed work instead of loose notes that go stale.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/model.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/feedback-intake.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectFeedbackIntake.tsx`

What changed:

- Added `operatorPacket` to `feedbackIntake`.
- Added paste-ready feedback handoff text with prospect, slug, stage, preset, severity, owner, target, summary, evidence, next action, and guardrail.
- Replaced the fake upload/dropzone affordance with a static screenshot/markup evidence requirement so the lab does not imply a file was uploaded.
- Added recurring feedback presets:
  - Site down / will not open.
  - Missing nav / page structure.
  - FAQ / accordion behavior.
  - Hero mismatch.
  - Photo context / random gallery.
  - Provider state mismatch.
- Reclassified missing email away from feedback blockers. Missing email remains an enrichment/contact-recovery concern, not an email-copy blocker.
- Reclassified missing review/content evidence away from automatic feedback attention. Absence of exposed source data should not create a false current blocker.

Verified fixture behavior:

- `thermys-mobile-tire-and-brakes`: `Hero mismatch packet`; target `Enrichment evidence`; owner `Bruce`; severity `triage`.
- `cityboys`: `Hero mismatch packet`; target `Enrichment evidence`; owner `Bruce`; severity `triage`.
- `24-hrs-mobile-tire-services`: `Provider state mismatch packet`; target `Outreach/provider incident`; owner `Outreach`; severity `blocking`.
- `raiden-electrical`: `Site down / will not open packet`; target `Paperclip blocker`; owner `Codex`; severity `blocking`.
- `rooter-pro-plumbing-drain`, `tuxedo-mechanical-plumbing`, and `harrison-sons-electrical`: no invented feedback blocker from missing email or missing source metadata; default packet remains a selectable starter if Jesse wants to flag a visual issue.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Thermys drawer shows `Structured Feedback Intake`, `Operator comment packet`, `Hero mismatch packet`, `Paste-ready handoff`, and guardrail text in the read-only packet body.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- `http://localhost:3001/lab/crm-v2` returns 200.

## 2026-06-05 Board-Clearing Runway Slice

Implemented a visible board-level runway above the kanban so the CRM v2 lab starts with the next operating lanes instead of forcing the operator to infer priority from 67 cards.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-clearing-runway.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/BoardClearingRunway.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`

Runway lanes:

- Send / approval runway.
- Provider truth.
- Current fixes.
- Enrichment.
- Monitoring.
- Stale / history notes.

Purpose:

- Keep the board scannable before opening individual cards.
- Separate revenue-near approval/send work from provider mismatches, current fixes, enrichment, monitoring, and stale/history notes.
- Keep stale/history note visibility without letting old notes become the board's dominant operating signal.
- Preserve the lab guardrail: no CRM writes, provider sends/retries, Paperclip mutations, deploys, or production replacement.

Verified current runway from `/api/prospects`:

- Total: `67` prospects organized into `6` lanes.
- `send_readiness`: `4`; first item `rooter-pro-plumbing-drain / Postcard-only approval packet`.
- `provider_truth`: `24`; first items include `24-hrs-mobile-tire-services`, `atlanta-drywall-1`, `perez-pools-llc`, and `smartwire-solutions`.
- `current_fixes`: `27`; first items include `raiden-electrical`, `cleveland-electric`, `landscape-addict`, and `mbanugo-tires`.
- `enrichment`: `11`; first items include `total-repair-service`, `azer-pool`, `hvac-guyz-plumbing-inc`, and `jack-glass-electric`.
- `monitoring`: `1`; first item `sandy-springs-plumbing`.
- `stale_history`: `64`; visible as preserved note/history lane, not as an automatic blocker lane.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Page shows `Board-clearing runway`, lane counts, `Send / approval runway`, `Provider truth`, `Current fixes`, `Enrichment`, `Stale / history notes`, and the `rooter-pro-plumbing-drain` item.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- `http://localhost:3001/lab/crm-v2` renders the runway before the kanban board.

## 2026-06-05 Lane-First Operator Session Plan Slice

Rebased the existing `BoardSessionPlan` on the new board-clearing runway and rendered it directly under the runway.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-session-plan.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/BoardSessionPlan.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-clearing-runway.ts`

What changed:

- Session plan now chooses one first-pass item from each runway lane instead of the older generic next-action queue.
- Session plan is visible before the kanban, immediately below the board-clearing runway.
- Each step includes lane, prospect, owner, action, reason, timebox, and approval/write boundary.
- Stale/history session step is owned by `Paperclip` instead of inheriting unrelated prospect disposition ownership.

Verified current session plan from `/api/prospects`:

- `6` lane-first session steps.
- `24` minute first pass.
- `2` blocked.
- `1` Jesse-gated.
- `5` safe ops.
- First-pass steps:
  - `0-4 min`: `Rooter Pro Plumbing & Drain` / `Send / approval runway` / `Jesse` / `Prepare approval decision`.
  - `4-8 min`: `24 hrs Mobile Tire Services` / `Provider truth` / `Outreach` / `Reconcile provider truth`.
  - `8-12 min`: `RAIDEN ELECTRICAL` / `Current fixes` / `Codex` / `Recheck current issue`.
  - `12-16 min`: `Total Repair Service` / `Enrichment` / `Bruce` / `Run evidence-only enrichment`.
  - `16-20 min`: `Sandy Springs Plumbing` / `Monitoring` / `Outreach` / `Monitor active outreach`.
  - `20-24 min`: `24 hrs Mobile Tire Services` / `Stale / history notes` / `Paperclip` / `Keep stale notes historical`.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Page shows `Operator Session Plan`, `6 lane-first session steps`, Rooter approval step, 24 Hour provider truth step, Raiden fix step, and Paperclip stale-history boundary.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- CRM v2 page renders the lane-first session plan directly under the board-clearing runway.

## 2026-06-05 V2.1 Acceptance Audit Slice

Implemented a V2.1-specific acceptance audit and surfaced existing launch/coverage proof in Advanced queues.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-v21-acceptance.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/BoardV21AcceptanceAudit.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`

What changed:

- Added `V2.1 Acceptance Audit` to map the active objective to current evidence.
- Added acceptance checks for:
  - Board scannability.
  - Command-first drawer.
  - Stale-note separation.
  - Provider truth separation.
  - Enrichment needs visibility.
  - Send readiness gates.
  - Runtime verification.
  - Production guardrail.
- Surfaced existing `BoardLaunchReadiness` and `BoardAcceptanceCoverage` inside Advanced queues.
- Kept the daily board surface clean while making ship/cutover proof available.

Verified current acceptance audit from `/api/prospects`:

- Label: `V2.1 usable in lab; production still locked`.
- Ready checks: `6`.
- Watch/attention checks: `1`.
- Locked checks: `1`.
- Board scannable: `ready`, `6 lanes / 6 session steps`.
- Drawer command-first: `ready`, `67/67`.
- Stale notes separated: `attention`, `67/67; 64 need note-level fields`.
- Provider truth separated: `ready`, `67/67; 24 provider work items`.
- Enrichment needs visible: `ready`, `67/67; 11 enrichment items`.
- Send readiness gated: `ready`, `67/67; 4 approval candidates`.
- Runtime verification: `ready`, `67 prospects loaded`.
- Production guardrail: `blocked`, `Cutover not approved`.
- Launch readiness remains `CRM v2 remains sandbox-only` with `1` hard blocker and `5` warnings.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Opened `Advanced queues, collapsed by default`.
- Verified `V2.1 Acceptance Audit`, `V2.1 usable in lab; production still locked`, stale-note warning, production guardrail, `Launch Readiness Lock`, and `Lab acceptance coverage`.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- CRM v2 page renders the acceptance/cutover proof panels in Advanced queues.

## 2026-06-05 Note-Level Stale Evidence Slice

Connected CRM v2 lab prospect derivation to the existing read-only prospect detail API so stale-note separation is now based on note-level evidence instead of only aggregate prospect counts.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/model.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/note-health.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/derive.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectNoteHealth.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-v21-acceptance.ts`

What changed:

- The lab now fetches `/api/prospects/[id]` read-only details for each visible prospect and passes `notes` into `deriveProspectView`.
- `noteHealth` now separates:
  - current open notes.
  - stale open notes older than 7 days.
  - resolved notes.
  - historical notes.
- Prospect drawers now expose a `Note-Level Evidence` section with note body, age, state, section/type, assignee, status label, evidence, and next action.
- Stale open notes are shown as history/waiting by default, not current blockers.
- Current open notes still surface as revalidation attention.
- V2.1 acceptance now treats stale-note separation as ready only when every prospect has note-level visibility.

Verified current note-level audit from local APIs:

- V2.1 label: `V2.1 usable in lab; production still locked`.
- Ready checks: `7`.
- Watch/attention checks: `0`.
- Locked checks: `1`.
- Stale notes separated: `ready`, `67/67; 0 current / 288 stale open`.
- `24-hrs-mobile-tire-services`: `3 stale open items`, note-level visible.
- `harrison-sons-electrical`: `5 stale open items`, note-level visible.
- `rooter-pro-plumbing-drain`: `4 stale open items`, note-level visible.
- `raiden-electrical`: `1 historical note`, no open stale/current blocker from notes.
- `thermys-mobile-tire-and-brakes`: `5 stale open items`, note-level visible.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- The board renders `Board-clearing runway`, `Provider truth`, `Current fixes`, `Enrichment`, and the expected 67-prospect count.
- The browser locator clicked a non-drawer `Open` target during one 24 Hour inspection attempt and landed on the browser's fallback load screen; code inspection confirmed runway and card items are proper `button type="button"` handlers that call `onOpen`, so this was treated as a test locator issue rather than a CRM app regression.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against `http://localhost:3001/api/prospects` plus read-only detail note fetches passed for all 67 prospects.

## 2026-06-05 Poplar Event Evidence / Outreach Noise Reduction Slice

Connected CRM v2 lab provider truth to existing read-only outreach events so postcard states are no longer limited to vague CRM summary fields.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/derive.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/provider-preflight.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/outreach-ops.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectProviderTruthMatrix.tsx`

What changed:

- CRM v2 prospect derivation now accepts existing `outreachEvents`.
- The sandbox groups `/api/prospects` outreach events by prospect and passes them into the lab model.
- Poplar provider truth now shows latest postcard event type, provider state, order ID, and recorded date when available.
- Provider-suppressed postcards now surface as `blocked` Poplar truth with explicit retry-lock language.
- Healthy submitted postcards keep provider order evidence visible but do not create generic provider-retry noise.
- Outreach queue no longer treats missing email as an outreach exception unless email is actually expected.
- Postcard payload warnings are suppressed for already-accepted provider-ready postcards; they remain visible for failed/suppressed retry paths.
- Removed duplicate generic `Outreach exception` queue rows when a specific row already carries the issue.

Verified fixtures:

- `24-hrs-mobile-tire-services`: Poplar provider truth is `blocked`, value `exception (suppressed)`, order `8b46f6b0-07a9-4242-851e-7fd3d488ff72`, next action says not to show it as sent and to require named retry approval.
- `atlanta-drywall-1`: Poplar provider truth is `blocked`, value `exception (suppressed)`, order `6deb9d29-ba56-40cd-9027-1ca5dfc9ac10`.
- `perez-pools-llc`: Poplar provider truth is `blocked`, value `exception (suppressed)`, order `7158568c-2f52-4a2d-84ce-b5e7783715e1`.
- `harrison-sons-electrical`: Poplar provider truth is `ready`, value `submitted`, order `65ccdec7-5ad9-4b5a-aa6b-3d7eabdda916`; queue now only shows reply monitoring.
- `smartwire-solutions`: Poplar provider truth is `ready`, value `submitted`, order `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`.

Verified queue behavior:

- Outreach queue dropped from `166` noisy items before refinement to `88` targeted items after suppressing duplicate/generic and non-expected channel noise.
- 24 Hour remains explicitly actionable as provider retry/repair.
- Healthy submitted postcard records are monitored, not treated as retry candidates.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against `http://localhost:3001/api/prospects` plus existing outreach events passed.

## 2026-06-05 Current Review-Risk Packet Slice

Added a lab-only review-risk layer so stale-note themes become fresh inspection prompts instead of either disappearing or blocking the board.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/model.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/current-review-risk.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/derive.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/review-disposition.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectCurrentReviewRisk.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectSheet.tsx`

What changed:

- Every prospect view now exposes `currentReviewRisk`.
- The drawer now has a `Current Review Risk` panel with:
  - current CRM/operator signals.
  - stale-note recheck prompts.
  - source (`Current CRM`, `Operator preset`, or `Stale note evidence`).
  - theme (`site_health`, `navigation`, `hero_context`, `postcard_asset`, `claim_flow`, `provider_state`, etc.).
  - stale age when applicable.
  - exact fresh evidence needed.
  - paste-ready recheck packet.
- Stale notes create recheck prompts, not blockers.
- A stale-only prompt can route a `needs_approval` site into the current-fixes lane for review.
- A stale-only prompt does not pull an already `qa_approved` postcard candidate out of send readiness.
- Current signals such as preview proxy health, missing hero source, or provider exception can still route to current fixes/provider retry.

Verified fixture behavior:

- `thermys-mobile-tire-and-brakes`: `needs_fix`; review risk shows current `hero_context` signal plus stale `claim_flow` and `hero_context` prompts.
- `tuxedo-mechanical-plumbing`: `needs_fix`; review risk shows stale `claim_flow`, `site_health`, and `navigation` prompts for fresh review.
- `raiden-electrical`: `site_health`; review risk shows current site-health signals from proxy/live-load risk.
- `rooter-pro-plumbing-drain`: remains `approve_channel`; stale-only `site_health`, `navigation`, and `claim_flow` prompts are visible but do not remove it from send readiness.
- `cityboys`: `needs_fix`; review risk shows current `hero_context` signal plus stale hero/navigation/postcard/photo/site prompts.
- `24-hrs-mobile-tire-services`: remains `provider_retry`; review risk shows current provider-state signal plus stale visual prompts.

Verified current runway after this slice:

- `send_readiness`: `1`, first item `rooter-pro-plumbing-drain`.
- `provider_truth`: `24`.
- `current_fixes`: `30`.
- `enrichment`: `11`.
- `monitoring`: `1`.
- `stale_history`: `64`.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local APIs and detail notes passed for the named fixtures above.

## 2026-06-05 Board Scannability / Review-Risk Surface Slice

Promoted current review-risk information from the drawer into the board and runway so operators can see the top issue without opening every prospect.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineCard.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-clearing-runway.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/prospect-search.ts`

What changed:

- Pipeline cards now show a `Review risk`, `Recheck prompt`, or `Stale prompts` signal when current/stale review-risk evidence exists.
- `approve_channel` cards with stale-only prompts show those prompts as visible history, not blockers.
- Current-fixes runway items now show the top review-risk label, source, stale age when applicable, and evidence needed.
- Current-fixes runway sorting now prioritizes review/revenue-stage prospects before early-stage missing-preview records.
- Runway lanes now show up to `6` items instead of `4` to reduce hidden board-clearing work.
- CRM v2 search now indexes current review-risk labels, themes, evidence, next action, and stale-note samples.

Verified current board-facing output:

- `send_readiness`: still shows `rooter-pro-plumbing-drain` as the visible send/approval item.
- `current_fixes` visible items now start with:
  - `raiden-electrical`: site down / live-load evidence needed.
  - `piedmont-tires`: claim-flow recheck from stale evidence.
  - `cityboys`: hero mismatch current signal.
  - `chrissy-s-mobile-detailing`: hero-context recheck.
  - `forest-park-collision`: bad postcard/current outreach blocker prompt.
  - `pine-peach-painting`: bad postcard/current outreach blocker prompt.
- `provider_truth` visible items start with `24-hrs-mobile-tire-services`, `atlanta-drywall-1`, `perez-pools-llc`, `smartwire-solutions`, `dream-steam`, and `atlanta-expert-appliance`.
- Search checks confirmed review-risk indexing for `hero` and `navigation` across relevant fixtures.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.

## 2026-06-05 Board-Level Current Review-Risk Queue Slice

Added a dedicated Advanced queue for current review risk so visual/site/provider review work can be batched across the board instead of discovered one drawer at a time.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-current-review-risk-queue.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/BoardCurrentReviewRiskQueue.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-v21-acceptance.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/stats.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/BoardAcceptanceCoverage.tsx`

What changed:

- Advanced queues now include `Current Review-Risk Queue`.
- The queue groups top review risks by current signals first, then stale-note recheck prompts.
- Queue cards show business, slug, stage, theme, source/stale age, total risk count, evidence needed, and next action.
- V2.1 acceptance audit now includes `Current review risk surfaced`.
- Lab acceptance coverage now includes a `Review risk` tile.
- CRM v2 sandbox loader now falls back to `XMLHttpRequest` when browser `fetch` is missing, fixing the in-app preview loading hang observed after the local dev restart.

Verified current queue output:

- `12 review-risk candidates`.
- `25` current signals.
- `16` stale prompts.
- `9` need screenshot evidence.
- First queue items:
  - `24-hrs-mobile-tire-services`: current provider-state mismatch, retry/send locked pending named approval.
  - `raiden-electrical`: current site-health failure, route to Post-Build repair before approval.
  - `forest-park-collision`: current postcard-asset blocker.
  - `pine-peach-painting`: current postcard-asset blocker.
  - `total-repair-service`: current postcard-asset blocker.
  - `jack-glass-electric`: current postcard-asset blocker.
  - `atlanta-drywall-1`: current provider-state mismatch.
  - `perez-pools-llc`: current provider-state mismatch.

Verified acceptance:

- `Current review risk surfaced`: `ready`.
- Coverage: `67/67`.
- Current review work: `66` prospects.
- Current/stale split: `71` current signals / `123` stale prompts.

Rendered UI verification:

- Restarted only the local `next dev -p 3001` preview server for `brucecom-v3`.
- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- CRM v2 preview now loads `67` visible prospects instead of hanging on `Loading CRM v2 sandbox data...`.
- Expanded `Advanced queues, collapsed by default`.
- Verified `CURRENT REVIEW-RISK QUEUE`, `12 review-risk candidates`, and the expected first queue items in the rendered page.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.
- `curl -I http://localhost:3001/lab/crm-v2` returned `200 OK`.

## 2026-06-05 Advanced Command Queue Surfacing Slice

Surfaced the existing hidden board queues so CRM v2 has a fuller control-plane view for board clearing instead of relying only on the kanban and drawer.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-command-index.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`

What changed:

- Advanced queues now include `Command Queue Index` as a read-only table of contents.
- Command Queue Index now includes the new `Review risk` queue and links to `crm-v2-current-review-risk-queue`.
- Previously hidden queue panels are now rendered:
  - `Contact Recovery Queue`.
  - `Proof / Asset Preflight Queue`.
  - `Feedback Capture Queue`.
  - `Stage Recommendation Queue`.
  - `Intake / R1VS Routing Queue`.
  - `Reply Monitor Queue`.
  - `Field Contract / Migration Queue`.
- Queue order now follows the operating flow: disposition/risk, next action, enrichment/proof/feedback, review/stage, intake/slug/outreach/reply/stale/migration.

Verified current command index:

- `14 active command queues`.
- First queue: `Disposition routes`.
- Queue counts:
  - `Disposition routes`: `18`.
  - `Next action`: `12`.
  - `Review risk`: `12`.
  - `Intake / R1VS`: `8`.
  - `Contact recovery`: `8`.
  - `Slug / claim`: `8`.
  - `Proof / assets`: `8`.
  - `Feedback capture`: `9`.
  - `Jesse review`: `6`.
  - `Stage recommendations`: `10`.
  - `Outreach exceptions`: `8`.
  - `Reply monitor`: `10`.
  - `Stale notes`: `8`.
  - `Field contract`: `8`.

Verified newly visible queue data:

- Contact recovery: `8` candidates, `16` address gaps, `43` email gaps, `35` source gaps.
- Proof/assets: `8` items, `43` postcard proof gaps, `67` email preview gaps, `51` screenshot gaps.
- Feedback capture: `9` candidates, all `9` currently blocking-level prompts.
- Reply monitor: `10` items.
- Stage recommendations: `10` items, `4` backward recommendations, `6` holds, `0` forward recommendations.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Expanded `Advanced queues, collapsed by default`.
- Verified visible text for `COMMAND QUEUE INDEX`, `14 active command queues`, `CONTACT RECOVERY QUEUE`, `PROOF / ASSET PREFLIGHT QUEUE`, `FEEDBACK CAPTURE QUEUE`, `STAGE RECOMMENDATION QUEUE`, `INTAKE / R1VS ROUTING QUEUE`, `REPLY MONITOR QUEUE`, and `FIELD CONTRACT / MIGRATION QUEUE`.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.
- Local CRM v2 preview continued to load `67` prospects.

## 2026-06-05 V2.1 Command Queue Acceptance Hardening Slice

Added a V2.1 acceptance check that proves the command queue layer covers the operational surfaces Jesse needs for board clearing.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-v21-acceptance.ts`

What changed:

- V2.1 Acceptance Audit now includes `Command queues covered`.
- The check requires queue index coverage for:
  - disposition routes.
  - next actions.
  - current review risk.
  - enrichment/contact recovery.
  - proof/assets.
  - feedback capture.
  - Jesse review.
  - stage recommendations.
  - outreach exceptions.
  - reply monitoring.
  - stale-note queues.

Verified current acceptance output:

- Audit label: `V2.1 usable in lab; production still locked`.
- Ready checks: `9`.
- Watch checks: `0`.
- Locked checks: `1`.
- `Command queues covered`: `ready`.
- Command queue coverage: `11/11; 14 active queues`.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Expanded `Advanced queues, collapsed by default`.
- Verified visible `V2.1 Acceptance Audit`.
- Verified `READY 9`, `WATCH 0`, `LOCKED 1`.
- Verified visible `Command queues covered` tile with `11/11; 14 active queues`.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.
- `curl -I http://localhost:3001/lab/crm-v2` returned `200 OK`.

## 2026-06-05 Detail Hydration Resilience Slice

Hardened CRM v2 lab data loading so note-level stale/current separation is visible and less fragile as the board grows.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/DataSourceHealth.tsx`

What changed:

- Prospect detail-note hydration now runs with bounded concurrency instead of firing every prospect detail request at once.
- Current batch size is `8`.
- Detail hydration state tracks requested, loaded, failed, duration, and degraded/complete status.
- `Data Source Health` now distinguishes top-level `/api/prospects` success from read-only detail-note hydration.
- The panel now shows detail note coverage and timing, so stale-note/current-note evidence is not silently assumed.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Expanded `Advanced queues, collapsed by default`.
- Verified `DATA SOURCE HEALTH`.
- Verified `67 loaded`.
- Verified `67 visible`.
- Verified `API read OK`.
- Verified `67/67 detail notes`.
- Verified bounded detail hydration timing: `3.2s / batch 8`.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Local CRM v2 preview continued to load `67` prospects.

## 2026-06-05 Provider Evidence Confidence Slice

Made provider truth more honest by distinguishing CRM event metadata from external provider endpoint validation.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/model.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/provider-preflight.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectProviderTruthMatrix.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/launch-readiness.ts`

What changed:

- `ProviderTruthSummary` now includes:
  - `evidenceKind`.
  - `evidenceLabel`.
  - `externalVerified`.
- Poplar rows now distinguish:
  - `External provider verified`.
  - `CRM event metadata only`.
  - `Provider endpoint not connected`.
- Provider Truth Matrix now shows evidence labels and whether a row is externally verified or CRM-derived.
- Launch Readiness now includes `Provider endpoint validation`.

Verified current provider confidence output:

- Launch readiness label remains `CRM v2 remains sandbox-only`.
- Launch blockers: `1`.
- Launch warnings: `6`.
- `Provider endpoint validation`: `attention`.
- Provider endpoint validation value: `24 unverified`.

Verified fixtures:

- `24-hrs-mobile-tire-services`: Poplar row remains `blocked`, value `exception (suppressed)`, evidence `CRM event metadata only`, `externalVerified: false`.
- `harrison-sons-electrical`: Poplar row remains operationally `ready`, value `submitted`, evidence `CRM event metadata only`, `externalVerified: false`.
- `atlanta-drywall-1`: Poplar row remains `blocked`, value `exception (suppressed)`, evidence `CRM event metadata only`, `externalVerified: false`.
- `perez-pools-llc`: Poplar row remains `blocked`, value `exception (suppressed)`, evidence `CRM event metadata only`, `externalVerified: false`.
- `rooter-pro-plumbing-drain`: Poplar row is `unknown`, value `not applicable`, evidence `Provider endpoint not connected`.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Expanded `Advanced queues, collapsed by default`.
- Verified Launch Readiness shows `Provider endpoint validation`, `24 UNVERIFIED`, and the warning explaining that CRM outreach events can carry provider metadata but production cutover needs read-only provider endpoint validation.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.

## 2026-06-05 Provider Launch-Warning Deconfliction Slice

Refined launch-readiness provider counts so provider exceptions, provider endpoint validation gaps, contact recovery, and reply monitoring do not collapse into one noisy warning.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/launch-readiness.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/migration-readiness.ts`

What changed:

- Launch Readiness `Provider truth` now counts actionable Poplar/Resend provider exceptions only.
- Missing email/contact recovery no longer inflates the provider truth warning.
- `hello@gtmdot.com` reply-monitor gaps remain in the separate `Reply monitor` launch check.
- Unverified CRM-event-derived provider rows remain in the separate `Provider endpoint validation` launch check.
- Migration readiness provider-event check now uses the same narrower actionable-provider definition.

Verified current launch output:

- Launch label: `CRM v2 remains sandbox-only`.
- Hard blockers: `1`.
- Warnings: `6`.
- `Provider truth`: `3 prospects`.
- `Provider endpoint validation`: `24 unverified`.
- `Reply monitor`: `67 unproven`.

Verified actionable provider exception slugs:

- `perez-pools-llc`.
- `atlanta-drywall-1`.
- `24-hrs-mobile-tire-services`.

Verified migration samples:

- `24-hrs-mobile-tire-services`: provider-event migration check remains `attention` with retry/repair guidance.
- `harrison-sons-electrical`: provider-event migration check is now `ready`; provider evidence is CRM-derived but not an actionable provider exception.
- `rooter-pro-plumbing-drain`: provider-event migration check is `ready`; no sent-provider exception exists.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Expanded `Advanced queues, collapsed by default`.
- Verified Launch Readiness shows:
  - `Provider truth` / `3 PROSPECTS`.
  - `Provider endpoint validation` / `24 UNVERIFIED`.
  - `Reply monitor` / `67 UNPROVEN`.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.

## 2026-06-05 Current Fix Handoff Slice

Added a top-of-drawer fix/comment handoff so operator feedback can become structured work instead of loose chat or stage-dropdown guessing.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectFixHandoff.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectSheet.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-v21-acceptance.ts`

What changed:

- Prospect drawer now shows `Current Fix Handoff` directly under the Command Center.
- The handoff chooses the strongest available paste-ready packet:
  - Current review-risk packet first.
  - Structured feedback packet as fallback.
- The panel shows evidence needed, next action, stale-note rule, and a readonly paste-ready handoff textarea.
- V2.1 Acceptance Audit now includes `Fix handoffs ready`.

Verified current acceptance output:

- `Fix handoffs ready`: `ready`.
- Coverage: `67/67`.
- Current-risk handoffs: `66`.
- Acceptance summary: `10` ready, `0` watch, `1` locked.

Verified fixtures:

- `thermys-mobile-tire-and-brakes`: current-risk handoff, top packet `Hero mismatch`.
- `tuxedo-mechanical-plumbing`: current-risk handoff, top packet `Claim flow recheck`.
- `raiden-electrical`: current-risk handoff, top packet `Site down / will not open`.
- `cityboys`: current-risk handoff, top packet `Hero mismatch`.
- `rooter-pro-plumbing-drain`: current-risk handoff, top packet `Site health / live-load recheck`; still route `approve_channel`.
- `harrison-sons-electrical`: current-risk handoff visible while route remains provider verification.

Rendered UI verification:

- In-app browser opened `RAIDEN ELECTRICAL`.
- Verified `CURRENT FIX HANDOFF` appears near the top of the drawer.
- Verified stale-note rule text appears in the panel.
- Verified the readonly textarea value starts with `[CRM v2 current review-risk packet]`.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.

## 2026-06-05 Reply Monitor Noise Reduction Slice

Narrowed CRM v2 launch/readiness reply monitoring so inactive/dead records do not inflate the operator warning surface.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/launch-readiness.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-reply-monitor-queue.ts`

What changed:

- Launch Readiness no longer counts every prospect with an unproven `reply_mailbox` row.
- Reply proof is now required for active outreach, staged outreach, non-dead sent/scheduled email risk, and non-dead monitor-route records.
- Reply queue no longer treats `No reply` as a positive reply signal.
- Reply queue no longer lets dead/inactive records with generic waiting preflight state occupy the active top-10 queue.
- Reply queue `unprovenCount` now counts actual reply-monitor/unproven queue items instead of only labels containing the literal word `unproven`.

Verified current output:

- Total prospects loaded: `67`.
- Launch Readiness `Reply monitor`: `25 unproven`, down from broad `67 unproven`.
- Reply Monitor Queue: `10 reply monitor items`.
- Queue `unprovenCount`: `10`.
- Queue `dueRiskCount`: `2`.
- First active queue examples: `morales-landscape-construction`, `24-hrs-mobile-tire-services`, `affordable-concrete-repair`, `atl-mobile-mechanics`, `atlanta-drywall-1`, `atlanta-expert-appliance`, `atlanta-pro-repairs`, `done-right-drywall`, `dream-steam`, `golden-choice-prowash`.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Board rendered successfully with `67` visible prospects and the board-clearing runway.
- HTTP smoke check returned `200 OK`.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.

## 2026-06-05 Provider Runway Priority Cleanup Slice

Reduced front-page provider noise by separating actionable provider retry/exception work from the lower-risk provider endpoint verification backlog.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-clearing-runway.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/BoardClearingRunway.tsx`

What changed:

- Board-clearing runway provider lane is now labeled `Provider retry / exceptions`.
- The top runway chip now says `Retry`.
- The runway provider lane now includes only `provider_retry` prospects.
- `provider_verify` prospects remain visible in drawer/card/advanced/provider evidence surfaces, but no longer inflate the first-screen runway as urgent retry work.

Verified current output:

- Runway `Provider retry / exceptions`: `3`.
- Retry slugs: `24-hrs-mobile-tire-services`, `atlanta-drywall-1`, `perez-pools-llc`.
- First screen still shows the separate header metric `PROVIDER RETRY 3`.
- The old runway `Provider 24` first-screen signal is gone.
- Provider endpoint validation remains tracked separately in Launch Readiness as evidence backlog.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Verified first-screen text contains `PROVIDER RETRY / 3`, `Provider retry · 3`, and `BOARD-CLEARING RUNWAY`.
- Verified no first-screen `PROVIDER / 24` runway chip remains.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.

## 2026-06-05 Current Fix / Payload Safety Slice

Tightened first-screen repair/recheck semantics so stale task counts no longer masquerade as current blocker work, and postcard approval cannot ignore payload blockers.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/review-disposition.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/derive.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/view-filters.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/model.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/CockpitHeader.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineRail.tsx`

What changed:

- Raw `openTasksCount` no longer automatically routes a prospect to `needs_fix`.
- Current note escalation now has to come through note-level `noteHealth.status === revalidate`.
- The saved `blocked` filter now follows current repair routes: `needs_fix` or `site_health`.
- First-screen metric label changed from `Recheck` to `Current fix`.
- Sidebar `Tasks` changed to `Fixes`.
- Final-prep postcard approval now checks postcard safety before approving channel readiness.
- A final-prep prospect with payload blockers now routes to `Postcard payload repair` / `run_enrichment` instead of `Approve postcard-only`.

Verified current output:

- Header `Current fix`: `13`, down from broad `Recheck 52`.
- Runway `Fix`: `13`.
- Runway `Send`: `1`.
- Runway `Enrich`: `25`.
- `rooter-pro-plumbing-drain`: remains the only `approve_channel` postcard approval candidate.
- `piedmont-tires`: moved out of send readiness to `run_enrichment` with `Postcard payload repair`.
- Piedmont reason: `Missing ZIP` from Poplar payload preflight / postcard safety.
- `tuxedo-mechanical-plumbing`, `chrissy-s-mobile-detailing`, and `cityboys`: remain current-fix/recheck work because they are in review/final stages with relevant visual/site risk.
- Stale/history remains visible: `64` stale/history lane items.

Rendered UI verification:

- In-app browser loaded `http://localhost:3001/lab/crm-v2`.
- Verified first-screen text includes `CURRENT FIX / 13`, `Current fix · 13`, `SEND / 1`, `FIX / 13`, and `ENRICH / 25`.
- Verified rendered Piedmont snippet appears under `ENRICHMENT` with `Prepare source-backed address/payload repair before postcard approval`.

Verification:

- `npm run build` passed with the known unrelated vault/Turbopack warning.
- Runtime derivation against local prospects, detail notes, and outreach events passed.

## 2026-06-05 Drawer Decision Snapshot Deconfliction Slice

Tightened the prospect drawer `Decision snapshot` and Command Center approval button so the opened prospect view now matches the board-level current/stale/provider/send separation.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectDecisionSnapshot.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectCommandPanel.tsx`

What changed:

- Drawer `Current blockers` no longer counts raw `issueCount`.
- Current blocker count now uses:
  - note-level current open notes.
  - current review-risk signals.
  - postcard safety blockers.
  - hard current gates, excluding email/contact gaps that belong in enrichment.
- Stale open notes now appear as proof/history in the stale lane, not as current blockers.
- Drawer `Provider truth` now ignores missing-email/contact-recovery rows and counts only actionable Poplar/Resend provider issues.
- Drawer `Send readiness` only surfaces available approval actions when the current disposition route is actually `approve_site` or `approve_channel`.
- Command Center primary approval button now says `Approval locked` unless the prospect is truly on an approval route.

Verified rendered drawer snapshots with real CRM data:

- `rooter-pro-plumbing-drain`: `Current blockers / No current blocker`; `4 stale open notes preserved in history`; `Provider truth / No provider exception`; `Send readiness / Approve postcard-only`.
- `piedmont-tires`: `Current blockers / 1 current item`; proof is `1 postcard safety blocker`; `Provider truth / No provider exception`; `Send readiness / Postcard payload repair`.
- `24-hrs-mobile-tire-services`: `Provider truth / Provider retry needed`; `Send readiness / Provider retry needed`; Command Center shows `Approval locked` and `Retry postcard locked`.
- `tuxedo-mechanical-plumbing`: `Current blockers / No current blocker`; `7 stale open notes preserved in history`; `Send readiness / Fresh recheck suggested`.
- `cityboys`: `Current blockers / 1 current item`; proof is `1 current review signal`.

Verification:

- Rendered `ProspectDecisionSnapshot` and `ProspectCommandPanel` to static markup with real local API prospect/detail/event data.
- `npm run build` passed with the known unrelated vault/Turbopack warning.
- `http://localhost:3001/lab/crm-v2` returned `200 OK`.

## 2026-06-05 Command Center Recommendation Priority Slice

Tightened the Command Center `Recommended fix/enrichment route` so it follows the actual disposition route and top evidence packet instead of falling back to generic feedback presets or generic contact recovery.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectCommandPanel.tsx`

What changed:

- `needs_fix`, `site_health`, and `provider_retry` routes now lead with the top current-review-risk packet when one exists.
- Approval routes only lead with current-review-risk when there is a current signal; stale-only prompts are explicitly labeled non-blocking.
- `run_enrichment` prospects with postcard safety blockers now lead with `Postcard payload repair`, not generic email discovery.
- The recommendation meta row now consistently shows source, stale age when relevant, and evidence required.

Verified rendered Command Center recommendations with real CRM data:

- `rooter-pro-plumbing-drain`: `No required fix for approval`; stale prompts are visible but explicitly non-blocking.
- `piedmont-tires`: `Postcard payload repair`; evidence is source-backed ZIP/address proof plus payload preview.
- `tuxedo-mechanical-plumbing`: `Claim flow recheck`; evidence is claim code, checkout URL, lookup result, and screenshot.
- `chrissy-s-mobile-detailing`: `Hero context recheck`; evidence is current hero screenshot and fit/not-fit explanation.
- `cityboys`: `Hero mismatch`; evidence is screenshot plus explanation.
- `24-hrs-mobile-tire-services`: `Provider state mismatch`; evidence is CRM channel state, provider response/event, order ID, and retry decision.

Verification:

- Rendered `ProspectCommandPanel` to static markup with real local API prospect/detail/event data.
- `npm run build` passed with the known unrelated vault/Turbopack warning.
- `http://localhost:3001/lab/crm-v2` returned `200 OK`.

## 2026-06-05 V2.1 Acceptance Audit Semantics Slice

Tightened the lab acceptance audit so it now validates the actual board-clearing workflow instead of only checking that UI pieces exist.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-v21-acceptance.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/command-recommendation.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectCommandPanel.tsx`

What changed:

- Added a `Board routes aligned` acceptance check so first-screen runway lane counts must match actual disposition routes.
- Added a `Drawer decisions deconflicted` acceptance check so approval, payload repair, provider retry, enrichment, current fix, and stale/history semantics stay separated.
- Added a `Command recommendation aligned` acceptance check so the Command Center recommendation must follow the actual disposition route.
- Split provider acceptance reporting into `3 retry / 21 verify` instead of one broad provider-work count.
- Corrected enrichment acceptance semantics: address/email/source recovery jobs are valid `run_enrichment` work and should not be mislabeled as failed payload-repair alignment.

Verified V2.1 acceptance audit against all current real CRM prospects:

- Overall label: `V2.1 usable in lab; production still locked`.
- Ready checks: `13`.
- Attention checks: `0`.
- Blocked checks: `1`, the intentional production cutover guardrail.
- Board routes aligned: `send 1/1; retry 3/3; fix 13/13; enrich 25/25`.
- Drawer decisions deconflicted: `67/67`.
- Command recommendation aligned: `67/67`.
- Stale note separation: `67/67; 0 current / 288 stale open`.
- Provider truth separated: `67/67; 3 retry / 21 verify`.
- Send readiness gated: `67/67; 1 approval candidates`.

Verification:

- Ran the V2.1 acceptance audit through `npx tsx` against `http://localhost:3001/api/prospects` plus per-prospect detail notes and outreach events.
- `npm run build` passed with the known unrelated vault/Turbopack warning.
- `http://localhost:3001/lab/crm-v2` returned `200 OK`.
- In-app browser DOM snapshot rendered the CRM v2 board with `Visible 67`, `Provider retry 3`, `Current fix 13`, runway chips `Send 1`, `Retry 3`, `Fix 13`, `Enrich 25`, and the `Rooter Pro Plumbing & Drain` approval card.

## 2026-06-05 V2.1 Review Outcomes Slice

Added a drawer-level `Review Outcomes` panel so each opened prospect has an immediate human decision fork instead of forcing the operator to infer where to put comments or approvals.

Added/updated:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/review-outcomes.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectReviewOutcomes.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectSheet.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-v21-acceptance.ts`

What changed:

- Every prospect drawer now shows three outcome cards near the top:
  - recommended approval/provider/monitor/current route packet.
  - Needs Fix / feedback packet.
  - enrichment/source recovery packet, or a closed-state explanation when no enrichment is derived.
- Each outcome includes:
  - owner.
  - when to use it.
  - next action.
  - `See proof` jump target.
  - paste-ready handoff text.
- The panel is lab-only and does not write CRM, mutate Paperclip, send provider requests, upload files, or contact prospects.
- Added `review_outcomes_ready` to the V2.1 acceptance audit.

Verified:

- V2.1 acceptance audit: `Review outcomes ready 67/67`.
- Overall V2.1 audit: `14` ready checks, `0` attention checks, `1` intentional blocked production cutover guardrail.
- Static-rendered the new panel with real local CRM data:
  - `rooter-pro-plumbing-drain`: approval route with `Approve / advance packet`.
  - `24-hrs-mobile-tire-services`: provider retry route with `Provider incident packet`.
  - `piedmont-tires`: enrichment route with `Enrichment evidence packet`.
  - `tuxedo-mechanical-plumbing`: needs-fix route with `Needs-fix packet` and closed enrichment state.
- `npm run build` passed with the known unrelated vault/Turbopack warning.
- `http://localhost:3001/lab/crm-v2` returned `200 OK`.

Why this matters:

- Jesse can open a prospect and choose the correct outcome: approve, flag a fix, request enrichment, or handle provider state.
- Review comments now have a paste-ready destination and owner, reducing loose chat/status drift.
- Approval-ready, provider-retry, enrichment, and needs-fix prospects each get different handoff language instead of one generic review path.

## Current Known Issues / Next Work

1. Provider truth now exposes evidence confidence, but still needs deeper fixture validation against a true read-only provider endpoint, not only CRM outreach events.
2. Real-prospect current-fix packets still need live visual evidence capture before any fix/deploy/write:
   - Tuxedo: navigation/page-structure and current hero context.
   - Thermys: current hero context.
   - Raiden: preview/live-site health.
   - Cityboys: current hero/postcard/photo context.
3. The June 2 rescope/audit artifacts were not found at the expected message paths after resume, so this checkpoint should be treated as the durable active V2.1 status until the ledger is reconciled.
4. The current note/detail/event loading approach is acceptable for lab use, but production cutover should batch/cache detail reads instead of firing one request per prospect on initial load.

## No-Action Statement

No CRM/Supabase writes, sends, provider calls, Paperclip mutations, deploys, git pushes, production replacement, prospect/customer contact, DNS/domain/hosting/billing changes, or Stripe actions were performed.
