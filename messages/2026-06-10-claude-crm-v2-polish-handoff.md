# Claude Handoff: GTMDot CRM v2 Polish + Paperclip Orchestration

Date: 2026-06-10  
Prepared for: Claude or another model taking over a polish/refinement pass  
Runtime target: `http://127.0.0.1:3001/lab/crm-v2`  
Codebase: `/Users/bruce/.openclaw/workspace/brucecom-v3`  
CRM route: `/lab/crm-v2`  
Current status: read-only lab preview, not production CRM replacement

## Paste-Ready Prompt For Claude

You are taking over a GTMDot CRM v2 polish pass. The user is frustrated because the CRM has become too complex for a simple business workflow: identify local service prospects, research/enrich them, build landing pages, QA/fix them, approve/send direct mail and email sequences, and later manage replies/sites.

Your job is not to add more CRM sections. Your job is to simplify the visible CRM into an operator command surface, while preserving the useful derivation logic already built.

Before editing, read these files:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/GTMDOT-CONTEXT-RESET.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-paperclip-orchestration-model.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-paperclip-orchestration-rollout-plan.md`
- `/Users/bruce/.codex/skills/gtmdot-paperclip-orchestrator/SKILL.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-10-claude-crm-v2-polish-handoff.md`

Then inspect the CRM implementation under:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2`

Your north star:

Make the CRM simpler than HubSpot for this workflow. A card should tell Jesse: "What is this company, who owns the next move, what is the one next action, and do I personally need to decide something?" If Paperclip/Bruce/OpenClaw/Codex can handle it, do not present it as Jesse's work.

## Hard Safety Boundary

This CRM is a lab preview. Do not perform or add code paths that execute real writes or sends unless explicitly approved later.

Forbidden without separate named approval:

- No CRM/Supabase writes.
- No Paperclip mutations.
- No Poplar provider submit/retry/send.
- No Resend/email send.
- No SMS/prospect/customer contact.
- No deploys or production replacement.
- No DNS, billing, Stripe, or irreversible account changes.

Safe work:

- Read local files.
- Refactor lab UI.
- Add read-only derivation helpers.
- Improve labels, grouping, and progressive disclosure.
- Run local build/checks if feasible.

## Product Context

GTMDot builds and manages small local-service prospect sites. The operational workflow should be straightforward:

1. Find/research a prospect.
2. Enrich missing facts and source evidence.
3. Build the site.
4. QA and fix the site.
5. Approve outreach.
6. Send direct mail/email later with separate approval.
7. Monitor provider truth, replies, and customer state.

The current CRM v2 has made progress but is still overbuilt. It exposes too much derived/internal information directly to Jesse. The result is paralysis: every company looks like it needs an hour of review.

The CRM should not ask Jesse to manually handle enrichment, stale-note triage, raw claim codes, raw URLs, or open-item bookkeeping. Those belong to background work routed through Paperclip and agents.

## The Real Operating Model

Collapse the visible process to four queues:

- `Build`: research, enrichment, missing contact facts, site generation, R1VS/build work.
- `Fix`: QA issues, current blockers, bad proof, broken site, current site/postcard/email repair.
- `Send`: postcard/email/provider/reply readiness after approval gates are clear.
- `Needs Jesse`: real human judgment only.

Jesse should only be escalated for:

- Approve site.
- Approve postcard/email/send/retry/contact action.
- Accept risk or override blocker.
- Decide fit/no-fit.
- Resolve conflicting source truths.
- Provide taste/UX judgment when automation cannot decide.

Everything else should route to Paperclip, Bruce/OpenClaw, Codex, or an automated background routine.

## Paperclip's Intended Role

Paperclip should be the orchestration and job-truth layer. The CRM should be prospect/business truth and the operator command surface.

Paperclip should track the work that humans should not have to manually coordinate:

- Enrichment jobs.
- Site build jobs.
- QA/fix jobs.
- Postcard proof/payload checks.
- Provider-state verification.
- Reply follow-up work.
- Learning events from Jesse decisions.

For each prospect, Paperclip should eventually expose a compact summary:

- `prospect_slug`
- `crm_id`
- `queue`: Build / Fix / Send / Needs Jesse
- `owner`: Bruce / Codex / Outreach / Jesse / Watchdog
- `state`: queued / running / blocked / waiting approval / done
- `next_action`
- `required_artifact`
- `done_condition`
- `approval_required`
- `allowed_actions`
- `forbidden_actions`
- `latest_artifact`
- `last_verified_at`

The CRM should show this summary, not a full issue tracker.

Current implementation note:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/paperclip-coordination.ts` exists, but it is still thin. It mainly infers coordination from `vaultFolderPath` and open issue count, and notes that CRM does not expose Paperclip parent issue URL yet.
- Improving the visible CRM can happen before full Paperclip integration by deriving a read-only `operatorQueue` from existing CRM fields.

## Current CRM Implementation Map

Primary files:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/page.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/sandbox.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/model.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/derive.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineBoard.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineColumn.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineCard.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/ProspectSheet.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/CockpitHeader.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/components/PipelineRail.tsx`

Important derivation/support files:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/review-disposition.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-clearance.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/contact-recovery.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/channel-state.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/current-review-risk.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/action-packet.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/routing-contract.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/paperclip-coordination.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/command-recommendation.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/board-command-index.ts`

Current code facts:

- `page.tsx` dynamically loads `./sandbox`.
- `sandbox.tsx` fetches `/api/prospects`, hydrates details from `/api/prospects/:id`, derives `ProspectView`, filters/searches, renders cockpit, rail, board, and company workspace.
- `model.ts` defines a large `ProspectView` with many derived slices: board clearance, review disposition, action packet, routing contract, next action, gates, contact recovery, Paperclip coordination, outreach health, provider truth, payload preflight, note health, stale notes, approval session, and more.
- `derive.ts` composes the derivation model. This is useful. Do not throw it away.
- `PipelineBoard.tsx` currently groups by lifecycle stages, not by the simplified Build/Fix/Send/Needs Jesse operating queues.
- `PipelineCard.tsx` still exposes raw preview URL, claim code, missing email, history-only chips, open item counts, and verbose next-action language.
- `ProspectSheet.tsx` renders too many sections: hero, shortcuts, lifecycle, review outcomes, decision snapshot, approval panel, stage guardrails, assets/outreach, channel truth, notes/fixes, feedback, Paperclip work state, note health, stale note policy, review risk, company, command, advanced diagnostics, and more.

## Current Observed UX Problems

The board:

- Cards show raw website URLs and claim codes even though they are not actionable on the card.
- Cards show labels like `Missing email`, `History only`, and `1 open item`, but they do not explain who owns the work or whether Jesse needs to care.
- "Needs Enrichment" cards tell Jesse "Email discovery" even though Bruce/OpenClaw/Paperclip should handle enrichment automatically.
- "Bad postcard: attach proof screenshot..." appears as if Jesse needs to do something, but the system should route that to a fix/proof job unless Jesse is being asked to approve/flag a proof.
- `Needs Decision` vs `Needs Approval` is unclear. For Jesse, both are really "Needs Jesse" unless there is a meaningful distinction.
- The board is visually cleaner than before but still basically a prettier version of a noisy CRM.

The company sheet:

- Above-the-fold hero/cockpit is the strongest part and should be kept.
- Everything below the fold is too long, too redundant, and too hard to parse.
- There are too many panels that repeat the same idea: decision snapshot, review outcomes, action hierarchy, stage guidance, command center, assets, outreach, note policy, stale notes, Paperclip, contact recovery.
- The page feels like a diagnostic dump instead of a decision cockpit.
- It asks Jesse to inspect mobile layout, hero context, popup behavior, claim bar, postcard rendering, email copy, current blockers, etc. That is too much for each company.

Specific examples from the current UI:

- Rooter Pro Plumbing & Drain is `QA Approved` with route `Approve postcard-only`. Missing email should not block postcard-only approval unless email outreach is part of the requested action.
- Premier TV Mounting is `Needs Enrichment` with `Email discovery`. That should be a Paperclip/Bruce background enrichment job, not Jesse's manual task.
- A stale open note should be historical unless fresh evidence proves it is still current. Do not make stale counts feel like blockers.

## Desired UX After Polish

Board card should show only:

- Company name.
- Trade.
- Operating queue or lifecycle badge.
- Owner of next move.
- One plain-English next action.
- One primary CTA.
- Only true blockers that require Jesse.

Board card should hide by default:

- Raw URL.
- Claim code.
- Stale-note counts.
- `History only`.
- Generic `Missing email` unless the selected queue/action is email.
- Internal route language.
- Long next-action descriptions.

Company sheet should become a one-screen cockpit:

- Header/hero: what this company needs now.
- Panel 1: `Decision needed` or `No Jesse action needed`.
- Panel 2: `Paperclip/background work` with owner, state, artifact, and done condition.
- Panel 3: `Proof & channels` with only actionable channel readiness.
- Advanced details behind tabs or `<details>` sections.

If it cannot fit on one screen, it is probably too much.

## Recommended Implementation Plan

### Step 1: Add a read-only operator summary

Add a derived helper, likely one of:

- `operator-queue.ts`
- `paperclip-command.ts`
- `work-orchestration.ts`

It should derive a compact shape from the existing `ProspectView` inputs:

```ts
type OperatorQueue = "build" | "fix" | "send" | "needs_jesse";

type OperatorSummary = {
  queue: OperatorQueue;
  label: string;
  owner: "Bruce" | "Codex" | "Outreach" | "Jesse" | "Paperclip";
  state: "ready" | "queued" | "running" | "waiting_approval" | "blocked";
  nextAction: string;
  primaryCta: string;
  requiresJesse: boolean;
  reason: string;
  hiddenDetails: string[];
};
```

Suggested routing logic:

- Missing email/address/phone/source evidence -> `Build`, owner `Bruce` or `Paperclip`, unless conflicting evidence requires Jesse.
- Site down, current visual bug, bad postcard, provider mismatch -> `Fix`, owner `Codex`/`Outreach`/`Paperclip`.
- QA approved with postcard/email proof ready and no current blocker -> `Send`, owner `Jesse` only for approval, `Outreach` for execution after approval.
- Needs approval, fit decision, risk acceptance, conflicting truth -> `Needs Jesse`.
- Stale open notes alone -> not a blocker; mention only in hidden details.

### Step 2: Simplify `PipelineCard.tsx`

Remove or hide:

- Preview URL text.
- Claim code text.
- `History only`.
- Raw open item counts unless current and blocking.
- Missing email unless email is the active channel decision.
- Long `NEXT` block.

Replace with:

- Queue chip: `Build`, `Fix`, `Send`, or `Needs Jesse`.
- Owner chip: `Bruce`, `Codex`, `Outreach`, `Paperclip`, or `Jesse`.
- One action line: e.g. `Paperclip should run email discovery`, `Jesse: approve postcard-only`, `Codex: fix current site issue`.
- One CTA: `Open`, `Review`, `Approve`, `Track`.

### Step 3: Simplify board grouping

Do not overbuild this. Two acceptable options:

- Safer pass: keep lifecycle columns but add a visible `Work queue` filter/strip for Build/Fix/Send/Needs Jesse and simplify cards.
- Better pass: show primary lanes as Build/Fix/Send/Needs Jesse, with lifecycle stage as a small secondary badge.

The user's mental model now favors the second option, but avoid a risky rewrite if time is short.

### Step 4: Collapse `ProspectSheet.tsx`

Keep the top hero. Then create a simple cockpit body:

- `What happens next`
- `Paperclip/background work`
- `Proof & channels`
- `Company facts`

Move everything else into `Advanced diagnostics` or tabs:

- Review outcomes.
- Decision snapshot.
- Approval panel.
- Stage guardrails.
- Action hierarchy.
- Stale note policy.
- Full note evidence.
- Payload preflight.
- Provider truth matrix.
- Migration/readiness diagnostics.

Do not delete useful components unless necessary. Hide them behind progressive disclosure.

### Step 5: Improve language

Replace internal CRM language with operator language:

- `Missing email` -> `Paperclip/Bruce should find email before email outreach`.
- `History only` -> hide by default.
- `1 open item` -> `Current blocker` only if fresh/current; otherwise hide or `Old note preserved`.
- `Needs Enrichment` -> `Build queue: enrich automatically`.
- `Needs Decision` and `Needs Approval` -> present as `Needs Jesse` when viewed by Jesse.
- `Approve postcard-only` -> `Jesse: approve postcard proof. This does not send.`

### Step 6: Preserve lab read-only behavior

All actions should remain recommendation/preview controls unless explicitly wired later with approval gates.

## Acceptance Criteria

The pass is successful if:

- Jesse can scan the board and understand the next 3 things requiring him in under 30 seconds.
- A card no longer requires decoding URL/claim/history/open-item jargon.
- Missing email is routed to background enrichment unless Jesse is explicitly choosing whether to pursue email.
- Needs Decision vs Needs Approval no longer creates confusion; the UI makes clear whether Jesse is needed.
- The company sheet's primary decision state is visible above the fold.
- Diagnostics are still available but no longer dominate the page.
- Paperclip appears as the orchestration layer, not as another pile of notes.
- No new write/send/deploy/provider side effects are introduced.

## Anti-Goals

Do not:

- Add more permanent sections.
- Expose every derivation just because it exists.
- Turn Paperclip into a second CRM interface.
- Make Jesse manually run enrichment.
- Treat stale notes as blockers without fresh evidence.
- Optimize for data completeness over operator clarity.
- Build final send/retry/write paths in this pass.
- Move folders or reorganize the repository as part of this CRM polish.

## Suggested Verification

From `/Users/bruce/.openclaw/workspace/brucecom-v3`:

```bash
npm run build
```

Local preview target:

```text
http://127.0.0.1:3001/lab/crm-v2
```

Current package scripts:

- `npm run dev`
- `npm run build`
- `npm run start`
- `npm run check:gtmdot-outreach-reply-to`

If the dev server is already running on port `3001`, inspect the UI there instead of starting another server.

## Related Context Files

Read these for the broader simplification model:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/START-HERE.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/GTMDOT-CONTEXT-RESET.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-ops-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-gtmdot-simplification-audit.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-paperclip-orchestration-model.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-paperclip-orchestration-rollout-plan.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-new-chat-structure-and-transfer-briefs.md`
- `/Users/bruce/.codex/skills/gtmdot-paperclip-orchestrator/SKILL.md`

## Current Paperclip Health Context

Paperclip local health endpoint has been observed as available:

```text
http://127.0.0.1:3199/api/health
```

Observed response:

```json
{
  "status": "ok",
  "version": "2026.428.0",
  "deploymentMode": "local_trusted",
  "deploymentExposure": "private",
  "authReady": true,
  "bootstrapStatus": "ready",
  "bootstrapInviteActive": false,
  "features": {
    "companyDeletionEnabled": true
  }
}
```

Do not mutate Paperclip from this pass. Treat Paperclip as an intended orchestration source and surface a read-only summary in CRM.

## Learning Loop To Preserve

Every Jesse decision should eventually become a learning event:

```ts
type GtmdotLearningEvent = {
  prospect_slug: string;
  queue: "build" | "fix" | "send" | "needs_jesse";
  decision_type: "approval" | "rejection" | "override" | "fit" | "copy" | "visual" | "source_truth";
  evidence: string[];
  decision: string;
  rationale: string;
  next_time_rule: string;
  process_update: string;
  approved_to_apply: boolean;
};
```

The CRM does not need to fully implement this now. But the UX should leave room for it by making decisions explicit and structured:

- What did Jesse decide?
- What evidence was used?
- What should the system do automatically next time?

## Final Product Principle

This business is not building a rocket ship. It is building websites for local service businesses, moving them through QA, and sending outreach.

The CRM should feel like:

```text
Here are the companies.
Here is who owns the next step.
Here is what will happen automatically.
Here are the few things Jesse must decide.
Nothing else is in the way.
```

If a detail does not help that, hide it.
