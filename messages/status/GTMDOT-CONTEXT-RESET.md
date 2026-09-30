# GTMDot Context Reset

Date: 2026-06-10
Purpose: one-page handoff for restarting GTMDot work without dragging the whole old chat forward.

## The Next Move

Start two new standing chats:

1. `GTMDot Ops`
2. `GTMDot CRM Build`

Do not create separate permanent chats for Pre-Build, Post-Build, Outreach, Experiments, or Quarterback. Those are now historical/fallback contexts, not standing operating rooms.

Use temporary task chats only when a job is scoped and will report back to Paperclip or GTMDot Ops.

## Active Folder Map

Use these as the active GTMDot folders:

- `/Users/bruce/.openclaw/workspace/brucecom-v3`
  Active CRM/app codebase. CRM v2 lab is here: `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/`

- `/Users/bruce/.openclaw/workspace/gtmdot-sites`
  Operations ledger, Paperclip handoffs, dispatcher artifacts, R1VS/site pipeline artifacts.

- `/Users/bruce/.openclaw/workspace/gtmdot`
  Site factory and business asset warehouse: site assets, postcards, emails, scripts, legacy GTMDot docs.

- `/Users/bruce/.openclaw/workspace/paperclip-sandbox` and `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home`
  Local Paperclip artifacts/runtime.

Treat `/Users/bruce/.openclaw/workspace/gtmdot-crm` as old CRM/reference only.

Do not move folders yet. The fix is not folder motion; it is making Paperclip and CRM the coordination surfaces.

## Operating Model

CRM should be the simple visible command surface.

Paperclip should be the orchestration/job layer.

Folders should store artifacts.

Chats should be temporary workbenches.

Collapse visible work to:

- `Build`
- `Fix`
- `Send`
- `Needs Jesse`

Jesse should only be pulled into true decisions: approval, risk acceptance, conflicting source truth, send/retry/contact authorization, or blocker override.

Routine enrichment, missing emails, stale notes, payload checks, source evidence, and provider checks should route through Paperclip/background workers, not Jesse.

## New Chat 1: GTMDot Ops

Paste this:

```text
You are the GTMDot Ops coordinator. Keep this simple and Paperclip-centered.

Read only this first:
/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/GTMDOT-CONTEXT-RESET.md

Then, only if needed:
/Users/bruce/.codex/skills/gtmdot-paperclip-orchestrator/SKILL.md
/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-ops-latest.md
/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-paperclip-orchestration-rollout-plan.md

Your job is to run GTMDot through Build / Fix / Send / Needs Jesse. Paperclip is the orchestration layer. CRM is the visible pipeline. Do not recreate old permanent lane chats.

First task: inspect current Paperclip/CRM status read-only and tell me the next 3 operational actions. Do not perform CRM writes, Paperclip mutations, sends, deploys, provider actions, prospect contact, DNS/billing changes, or git pushes without explicit approval.
```

Use this chat for:

- deciding what to do next,
- Paperclip orchestration,
- enrichment routing,
- provider/read-only checks,
- approval packets,
- learning-loop decisions.

## New Chat 2: GTMDot CRM Build

Paste this:

```text
You are the GTMDot CRM Build agent. Your job is to simplify CRM v2, not expand it.

Read only this first:
/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/GTMDOT-CONTEXT-RESET.md

Then, only if needed:
/Users/bruce/.codex/skills/gtmdot-paperclip-orchestrator/SKILL.md
/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-paperclip-orchestration-model.md
/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-paperclip-orchestration-rollout-plan.md

Active codebase:
/Users/bruce/.openclaw/workspace/brucecom-v3

Active CRM v2 route:
/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/

Goal: make CRM v2 simpler than HubSpot. Cards should show company, trade, queue, owner, one next action, and one CTA. Company page should be a one-screen cockpit plus detail tabs. Hide raw URL, claim code, stale note counts, history-only labels, and internal provider/stage chatter unless directly actionable.

First task: inspect the current CRM v2 implementation and propose/implement the smallest simplification pass. Do not perform CRM/Supabase writes, Paperclip mutations, sends, deploys, provider actions, prospect contact, DNS/billing changes, or git pushes without explicit approval.
```

Use this chat for:

- CRM card simplification,
- company page simplification,
- Paperclip summary integration,
- UX/code changes in `brucecom-v3`.

## Temporary Task Chat Rule

Only create temporary chats for bounded work:

- `Run enrichment for Pro Gutter Cleaning`
- `Audit Poplar suppressed postcards`
- `Run R1VS Mbanugo pilot`
- `Fix CRM card layout`

Each temporary chat must:

1. Start from GTMDot Ops or a Paperclip issue.
2. Produce one artifact or code change.
3. Report back to Paperclip/GTMDot Ops.
4. Close.

## Learning Loop

Every time Jesse makes a decision, capture it as a learning event:

- prospect,
- decision type,
- evidence considered,
- decision,
- rationale,
- what should happen automatically next time,
- whether to update CRM, Paperclip template, skill, research brief, QA check, or enrichment process.

Review after every 10 decisions and update one rule. The learning loop should reduce future Jesse decisions, not create another report to manage.

## Current Safety Boundary

Unless explicitly approved, do not perform CRM/Supabase writes, Paperclip mutations, Poplar submits/retries, Resend/email sends, SMS sends, prospect/customer contact, production deploys, DNS/domain/hosting/billing/Stripe changes, or git pushes.

