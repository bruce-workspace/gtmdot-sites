# GTMDot Paperclip Orchestration Model

Date: 2026-06-09
Purpose: simplify GTMDot operations so Jesse is not the router between chats, agents, folders, CRM, and provider tools.

## Executive Take

The current GTMDot workflow is overbuilt for the actual business.

The business is not complicated:

1. Find a real local business.
2. Build a preview site.
3. Fix obvious issues.
4. Get approval when judgment is required.
5. Send postcard/email, later SMS.
6. Watch replies/provider state.
7. Convert, retry, or close.

The system became complicated because there was no trusted orchestration layer. Chats, lane files, dispatcher outboxes, CRM lab panels, and status ledgers started filling the gap. That helped avoid mistakes, but now it is making Jesse do coordination work that should be invisible.

Paperclip should be that orchestration layer.

Not a second CRM. Not another place Jesse has to manage. Paperclip should be the background job router that knows:

- what prospect/job is active,
- what queue it belongs to,
- who or what owns the next action,
- what artifact proves completion,
- whether Jesse actually needs to decide anything.

## Keep The Folder Structure, Change The Mental Model

Do not move folders right now. The existing scripts and artifacts use absolute paths, and moving them would create risk without solving the real problem.

Keep these roles:

- `/Users/bruce/.openclaw/workspace/gtmdot`: site factory and business asset warehouse.
- `/Users/bruce/.openclaw/workspace/gtmdot-sites`: operating ledger, R1VS/Paperclip handoffs, dispatcher artifacts.
- `/Users/bruce/.openclaw/workspace/brucecom-v3`: active CRM/app codebase.
- `/Users/bruce/.openclaw/workspace/gtmdot-crm`: old CRM/reference only.
- `/Users/bruce/.openclaw/workspace/paperclip-sandbox`: local Paperclip dry-run/artifact space.

Visibility should come from Paperclip issue IDs, CRM IDs, prospect slugs, and artifact links, not from folder layout.

Every durable artifact should include:

- `prospect_slug`
- `crm_id` when known
- `paperclip_issue`
- `queue`: `build`, `fix`, `send`, or `needs_jesse`
- `owner`
- `done_condition`
- `latest_artifact`

## Two Standing Chats, Not Five

### 1. GTMDot Ops

Default chat for running the business.

Use for:

- deciding the next highest-leverage GTMDot action,
- reading Paperclip/CRM/provider state,
- approving or rejecting work packets,
- asking "what is blocked and why?",
- reviewing the simplified Build / Fix / Send / Needs Jesse queues.

This replaces permanent Pre-Build, Post-Build, Outreach, Quarterback, and general setup chats as daily operating surfaces.

### 2. CRM Build

Only for changing CRM code/UX.

Use for:

- simplifying CRM v2 cards and company pages,
- making CRM read Paperclip orchestration state,
- implementing Build / Fix / Send / Needs Jesse,
- removing noisy fields from the operator UI.

### Temporary Task Chats

Temporary chats are allowed only for bounded work, then they report back and close.

Examples:

- "Implement CRM card simplification"
- "Audit Poplar suppressed postcards"
- "Run Mbanugo build pilot"
- "Fix email reply watcher"

Temporary chats must start from a Paperclip issue or create a result artifact that Paperclip links back to.

## The Four Visible Queues

The CRM and GTMDot Ops should collapse everything to four queues:

### Build

Agent-owned by default.

Includes:

- intake validation,
- source research,
- enrichment,
- R1VS build packet,
- site generation,
- initial build return.

Jesse should not touch this unless legitimacy, source truth, business fit, or a tradeoff needs human judgment.

### Fix

Agent-owned by default.

Includes:

- broken site/build gates,
- visual repair,
- postcard asset repair,
- missing screenshot/proof,
- stale-note recheck,
- provider payload repair before send.

Stale notes do not block by themselves. Paperclip should turn them into recheck tasks only if the prospect is otherwise near approval/send.

### Send

Approval-gated.

Includes:

- postcard proof/payload preflight,
- email payload/copy preflight,
- Poplar/Resend read-only provider state,
- reply/bounce/sequence safety,
- named send/retry approval packets.

Agents can prepare evidence. Jesse approves real sends/retries/contact.

### Needs Jesse

Human judgment only.

Examples:

- approve site/outreach,
- accept risk,
- choose between conflicting source truths,
- approve provider retry/send/contact,
- decide a business is not a fit,
- override a current blocker.

Missing email, missing proof, "history only", raw claim code, raw URL, or old open-item counts should not show here unless the background work already failed and the exact human decision is clear.

## Paperclip As The Work Engine

Paperclip should track workflow truth:

- queue,
- owner,
- state,
- current blocker,
- allowed actions,
- forbidden actions,
- required artifact,
- done condition,
- latest evidence,
- next owner,
- Jesse approval requirement.

CRM should track prospect/business truth:

- company/contact fields,
- stage,
- site URL,
- claim code,
- channel state,
- approval state,
- outreach history.

Supabase/job tables should track machine execution truth:

- R1VS job phase,
- watcher status,
- provider snapshots,
- retry counts,
- timestamps.

Git/files should track artifact truth:

- research packet,
- build packet,
- site files,
- QA screenshots,
- postcard proof,
- enrichment evidence,
- provider snapshots.

Chats should not be truth. Chats are temporary workbenches.

## Recommended Paperclip Issue Shape

For each prospect, create one parent orchestration issue.

Required fields, whether native fields, labels, or structured body:

```json
{
  "prospect_slug": "rooter-pro-plumbing-drain",
  "crm_id": "optional-crm-id",
  "queue": "build|fix|send|needs_jesse",
  "owner": "codex|bruce|r1vs|outreach|provider|jesse",
  "state": "queued|running|blocked|needs_review|done",
  "next_action": "one sentence",
  "required_artifact": "path or description",
  "done_condition": "one sentence",
  "approval_required": "none|jesse_site|jesse_send|jesse_retry|crm_write",
  "allowed_actions": ["read", "inspect", "write-evidence-packet"],
  "forbidden_actions": ["crm-write", "send", "deploy", "prospect-contact"],
  "latest_artifact": "/Users/bruce/...",
  "last_verified_at": "2026-06-09T..."
}
```

Child issues should be used only when parallel work is real:

- Bruce enrichment needed,
- R1VS build/fix needed,
- Codex CRM implementation needed,
- Outreach provider verification needed.

Do not create child issues for every tiny note. That is how the airplane turned into the airport.

## Paperclip Agents And Routines

Start with narrow agents/routines. Do not create a broad "do everything" agent.

### `runtime-watchdog`

Keeps Paperclip health, backup, and dispatcher status fresh.

Allowed:

- read health,
- write status artifact,
- alert if down.

Forbidden:

- CRM writes,
- sends,
- deploys,
- provider mutations.

### `dispatcher`

Reads CRM/Paperclip/files/provider snapshots and produces one simplified GTMDot Ops digest.

Allowed:

- read state,
- classify work into Build/Fix/Send/Needs Jesse,
- write digest/outbox artifacts,
- in dry-run, propose Paperclip updates.

Later, with approval:

- add Paperclip comments/labels through a safe mutator.

### `research-enrichment-agent`

Runs evidence collection for missing email/address/source/photo/review facts.

Allowed:

- public/source discovery,
- Browserbase/Bruce evidence packets,
- confidence/source URLs,
- known unknowns.

Forbidden:

- CRM field writes without approval,
- invented contact facts,
- prospect contact.

### `r1vs-build-runner`

Starts or monitors R1VS build jobs from Paperclip/Supabase job specs.

Allowed:

- run one build job at a time,
- write phase artifacts,
- update machine-readable job status,
- report blocked source/build quality.

Forbidden:

- CRM promotion,
- deployment,
- outreach release,
- parallel builds against the same working tree until worktree isolation exists.

### `qa-fix-router`

Turns current QA failures into fix work and routes them to the right owner.

Allowed:

- create current fix packet,
- link screenshot/proof,
- classify stale notes as historical unless revalidated.

Forbidden:

- treating stale notes as blockers without fresh evidence,
- deploying fixes without approval.

### `postcard-preflight-agent`

Checks postcard payload/assets/proof readiness.

Allowed:

- read-only payload checks,
- proof existence checks,
- provider dry-run when available,
- send approval packet.

Forbidden:

- Poplar submit/retry/send without named approval.

### `provider-watch-agent`

Reads Poplar, Resend, and Gmail/Workspace state.

Allowed:

- detect submitted/in-production/delivered/returned/suppressed,
- detect delivered/bounced/replied,
- create provider evidence packet.

Forbidden:

- provider mutation,
- sequence resume,
- resend/retry,
- prospect contact.

## End-To-End Flow

### Build Flow

1. CRM marks prospect approved for build.
2. Paperclip creates/updates parent issue with `queue=build`.
3. Paperclip writes or references a job spec.
4. R1VS/job runner builds and reports phase status.
5. Bruce/enrichment agent fills source/photo/review gaps if needed.
6. If blocked by judgment, Paperclip moves to `needs_jesse`.
7. If built, Paperclip moves to `fix` or `needs_jesse` depending on QA state.

### Fix Flow

1. Paperclip detects current issue or revalidated stale issue.
2. Routes to Codex, Bruce, R1VS, or Outreach.
3. Owner produces a proof artifact.
4. Paperclip updates latest artifact and done condition.
5. If fixed, moves forward; if judgment needed, moves to `needs_jesse`.

### Send Flow

1. Paperclip confirms site approval and channel preflight.
2. Postcard/email provider checks produce evidence.
3. CRM shows only "Ready for postcard approval" or "Blocked: exact reason."
4. Jesse gives named send/retry approval.
5. Provider action runs separately.
6. Provider watcher records state and surfaces exceptions.

## What CRM Should Show

CRM should feel simpler than HubSpot, not more complex.

Each card should show:

- company,
- trade,
- queue,
- owner,
- one next action,
- one CTA.

Do not show on cards:

- raw claim code,
- raw URL,
- "history only",
- stale open-item counts,
- missing email unless the agent search failed and Jesse must decide,
- long provider/internal state explanations.

Company page should be:

- one-screen cockpit,
- short Paperclip job state,
- current proof/artifact links,
- exact approval boundary,
- details hidden behind tabs.

If the operator needs to scroll for an hour, the page has failed.

## Immediate Implementation Plan

### Phase 1: Consolidate The Operating Surface

Create and use:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-ops-latest.md`

Sections:

- Now
- Build
- Fix
- Send
- Needs Jesse
- Background Agents
- Guardrails

This becomes the human-readable bridge until CRM v2 is simplified.

### Phase 2: Re-map Paperclip

Keep existing GTM issues for history, but add the new queue model.

First dry-run:

- classify existing GTM issues into Build/Fix/Send/Needs Jesse,
- propose labels/structured comments,
- do not mutate Paperclip until approved.

### Phase 3: Make Dispatcher Emit One Digest

Change the dispatcher output from lane-oriented outboxes to one GTMDot Ops digest:

- what changed,
- what agents handled,
- what is blocked,
- what Jesse must decide,
- what is safe to ignore.

### Phase 4: CRM Reads Paperclip Summary

CRM v2 should read or ingest Paperclip summary state and show it as:

- queue,
- owner,
- status,
- next action,
- latest proof,
- approval required.

### Phase 5: Add Safe Mutations

Only after the dry-run output is trusted:

- add Paperclip comments,
- set labels,
- update owner/status,
- never send/deploy/write CRM unless explicitly approved.

## Bottom Line

The winning model is not more chats.

It is:

- one GTMDot Ops chat,
- one CRM Build chat,
- Paperclip as the orchestration layer,
- CRM as the simple visible command surface,
- agents doing background work,
- Jesse only handling true judgment and approval.

The goal is not to build a prettier version of the old CRM. The goal is to make most prospects move from research to build to fix to send without Jesse touching them until a real decision exists.

