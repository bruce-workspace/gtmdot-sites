# GTMDot Paperclip Orchestration Rollout Plan

Date: 2026-06-09
Purpose: turn the simplified Paperclip operating model into an actual workflow.

## Decision

Adopt the simplified model:

- Two standing chats: `GTMDot Ops` and `CRM Build`.
- Four visible queues: `Build`, `Fix`, `Send`, `Needs Jesse`.
- Paperclip becomes the orchestration/job layer.
- CRM becomes the simple visible command surface.
- Bruce/OpenClaw, R1VS, Codex, provider watchers, and enrichment routines operate behind Paperclip.
- Human decisions become learning events that improve the workflow.

## Next Steps

### 1. Stop Expanding The Current CRM Model

Freeze the current CRM v2 direction that exposes every note, stale item, provider nuance, missing field, claim code, and internal packet on the card/company page.

New CRM direction:

- card = company + trade + queue + owner + one next action + one CTA;
- company page = one-screen cockpit + detail tabs;
- Paperclip summary visible, internals hidden.

### 2. Make Paperclip The Work Router

Map every active prospect/job to a Paperclip parent issue or a structured Paperclip summary.

Each issue needs:

- queue,
- owner,
- state,
- next action,
- required artifact,
- done condition,
- approval boundary,
- latest proof.

Start in dry-run. Do not mutate Paperclip until the proposed mapping is reviewed.

### 3. Replace Lane Reading With One Ops Status

Use:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-ops-latest.md`

This file should become the human-readable bridge while CRM catches up.

Old lane files remain historical/fallback context, not the daily operating model.

### 4. Change Dispatcher Output

Current dispatcher output is lane-oriented and creates a lot of outbox noise.

New dispatcher output should be one GTMDot Ops digest:

- what changed,
- which background worker handled it,
- which prospects are blocked,
- which exact Jesse decisions are needed,
- what can be ignored.

### 5. Start With Enrichment Automation

The first useful Paperclip-backed workflow should be enrichment because it is clearly agent-owned.

When CRM/Paperclip says "missing email" or "needs source evidence":

1. Paperclip queues `research-enrichment-agent`.
2. Bruce/OpenClaw or Browserbase collects evidence.
3. Output is an evidence packet: candidate fact, source URL, confidence, known unknowns.
4. Paperclip updates job state.
5. CRM only asks Jesse if the evidence is conflicting or approval is required to write fields.

Jesse should not manually enrich routine missing data.

### 6. Then Wire Build/Fix/Send

Order:

1. Enrichment routing.
2. R1VS build job routing.
3. QA/fix routing.
4. Postcard/email preflight routing.
5. Provider state watchers.
6. CRM v2 reads Paperclip summary and hides internals.

Avoid broad autonomous agents. Each worker should have a narrow job, a done condition, and hard guardrails.

## Learning Loop

Every human decision should create a small learning event.

### Capture Shape

```json
{
  "timestamp": "2026-06-09T...",
  "prospect_slug": "example-slug",
  "queue": "build|fix|send|needs_jesse",
  "decision_type": "fit|source_truth|qa|approval|send|retry|override|close",
  "evidence": ["artifact-path-or-url"],
  "decision": "what Jesse chose",
  "rationale": "why",
  "next_time_rule": "what should be automatic or clearer next time",
  "process_update": "none|skill|crm_rule|paperclip_template|build_template|qa_check",
  "approved_to_apply": false
}
```

### Weekly Or Per-10-Decision Review

Batch learning events and ask:

- Which decisions repeated?
- Which should become automatic?
- Which need better evidence before Jesse sees them?
- Which CRM labels/cards confused the operator?
- Which Paperclip template needs a new field?
- Which build/QA rule would have prevented this?

Then update one of:

- GTMDot Paperclip orchestrator skill,
- CRM UI rule,
- Paperclip issue template,
- build/research brief template,
- QA checklist,
- enrichment source strategy.

### Rule

Do not let learning become more bureaucracy.

The learning loop should reduce future Jesse decisions, not create a new report Jesse has to manage.

## Chat Usage

### Use GTMDot Ops For

- What should happen next?
- Which prospects are blocked?
- What does Paperclip say?
- Approve/reject work packets.
- Review Build/Fix/Send/Needs Jesse.
- Run provider/enrichment/read-only checks.

### Use CRM Build For

- Changing `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/`.
- Simplifying cards/company pages.
- Integrating Paperclip summary into CRM.
- Removing noise from the operator UI.

### Temporary Task Chats

Allowed only when scoped:

- "Run enrichment for Pro Gutter Cleaning"
- "Fix CRM card simplification"
- "Audit Poplar suppressed postcards"
- "Run R1VS Mbanugo pilot"

Temporary chat rule:

1. Start from a Paperclip issue or GTMDot Ops directive.
2. Produce one artifact or code change.
3. Report back to Paperclip/GTMDot Ops.
4. Close.

## Implementation Order

1. Use the new `gtmdot-paperclip-orchestrator` skill for future GTMDot ops sessions.
2. Add a Paperclip dry-run classifier for active prospects/issues.
3. Make dispatcher produce one simplified GTMDot Ops digest.
4. Update CRM v2 cards/company page around Paperclip summary.
5. Route missing enrichment through Bruce/OpenClaw evidence packets.
6. Add learning-event capture whenever Jesse makes a decision.

## Guardrails

No CRM/Supabase writes, Paperclip mutations, provider sends/retries, email/SMS sends, prospect contact, production deploys, DNS/domain/hosting/billing/Stripe changes, or git pushes without explicit approval.

