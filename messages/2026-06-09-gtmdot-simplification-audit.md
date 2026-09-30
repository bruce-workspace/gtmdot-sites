# GTMDot Simplification Audit

Date: 2026-06-09
Purpose: reduce GTMDot operating complexity back to the real business workflow.

## Executive Take

GTMDot has become too complicated for what it is.

The actual business is simple:

1. Find a local business.
2. Build a preview site.
3. QA/fix the preview.
4. Approve the site/outreach.
5. Send postcard/email.
6. Monitor replies/provider state.
7. Convert or close.

The current system has grown extra layers around that:

- multiple folders with overlapping GTMDot responsibility,
- many lane/status/message files,
- separate chats for what should often be one workflow,
- CRM v2 panels that expose internal model complexity instead of hiding it,
- “coordination” artifacts that sometimes become more work than the work.

The fix is not to create more lanes. The fix is to collapse the operating model.

## What Exists Today

### Active Folders

#### `/Users/bruce/.openclaw/workspace/gtmdot`

Role: site factory and business asset warehouse.

Keep using it for:
- site source/assets,
- postcards,
- email assets,
- GTMDot pricing/legal/business docs,
- build/deploy scripts,
- prospect research.

Problem:
- It also contains historical docs, old process docs, experiments, and older artifacts. That makes it feel like a source of truth even when newer operational truth lives elsewhere.

#### `/Users/bruce/.openclaw/workspace/gtmdot-sites`

Role: operations ledger and newer site-pipeline control plane.

Keep using it for:
- current lane/status files,
- handoffs,
- R1VS/build-pipeline operational packets,
- dispatcher artifacts while needed.

Problem:
- It has become “messages about messages.” There are 100+ top-level message files and a dispatcher/outbox with thousands of files. That is too much for normal human operation.

#### `/Users/bruce/.openclaw/workspace/brucecom-v3`

Role: active CRM/app codebase.

Keep using it for:
- public CRM/API,
- CRM v2 lab code at `src/app/lab/crm-v2/`,
- future production CRM work.

Problem:
- CRM v2 is over-modeled. The lab has 171 files under one feature route, which mirrors the operational sprawl instead of simplifying it.

#### `/Users/bruce/.openclaw/workspace/gtmdot-crm`

Role: old CRM/reference project.

Recommendation:
- Freeze as reference only. Do not use it for active CRM v2 work.

## Root Cause

GTMDot is missing one simple durable command surface.

Because the CRM is not yet the trusted command surface, the project compensated with:

- lane chats,
- lane status files,
- dispatcher digests,
- handoff packets,
- message ledgers,
- manual approvals,
- temporary lab UIs.

That scaffolding helped avoid mistakes, but now it is becoming the product.

The CRM should absorb most of this. The operator should not have to know whether work is “Pre-Build” or “Post-Build” unless something is blocked.

## Simplified Operating Model

### Replace Five Lanes With Three Queues

Use three human-readable queues:

1. **Build**
   - intake,
   - research,
   - enrichment,
   - R1VS/build packet,
   - site generation.

2. **Fix**
   - QA feedback,
   - stale-note recheck,
   - visual/site repair,
   - postcard asset repair,
   - provider/data repair before send.

3. **Send**
   - site approval,
   - postcard/email approval,
   - Poplar/Resend state,
   - replies/bounces,
   - follow-up monitoring.

Everything else is a detail behind one of those queues.

### Keep Only Two Standing Conversations

#### 1. GTMDot Ops

This is the default conversation.

Use it for:
- “What should happen next?”
- build/fix/send queue decisions,
- approval packets,
- outreach/provider checks,
- site/postcard/email status,
- updating the simplified status ledger.

This replaces separate always-on Pre-Build, Post-Build, Outreach, and Quarterback chats.

#### 2. CRM Build

Use only when changing CRM code/UX.

Use it for:
- simplifying `/lab/crm-v2`,
- making the CRM become the command surface,
- fixing cards/company workspace/workflow.

Do not use this chat for day-to-day board clearing unless the work is explicitly CRM implementation.

### Optional Short-Lived Chats

Spin up a temporary focused chat only when the task is large enough to deserve isolation:

- “Build Mbanugo site”
- “Fix Poplar suppressed postcards”
- “Implement CRM card simplification”
- “Audit all postcard payloads”

When done, the temporary chat writes one short result back to the GTMDot Ops status file or CRM.

Do not keep those as permanent lanes.

## Simplified Source Of Truth

### Today

Until CRM v2 is fixed, use one status file:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-ops-latest.md`

Recommended sections:

- `Now`
- `Build Queue`
- `Fix Queue`
- `Send Queue`
- `Blocked / Needs Jesse`
- `Recent Changes`
- `Do Not Do Without Approval`

This can replace most lane status reading for normal operation.

### Later

Once CRM v2 is usable:

- CRM becomes the source of truth.
- File ledger becomes backup/audit only.
- Conversations should not manage pipeline state; they should execute and report.

## What To Stop Doing

- Stop treating Pre-Build, Post-Build, Outreach, Platform, Experiments as permanent chats Jesse has to mentally manage.
- Stop creating a new long handoff artifact for every minor state change.
- Stop exposing internal stage/provider/note complexity directly on CRM cards.
- Stop showing “history only,” raw claim codes, raw URLs, stale open item counts, or missing-field labels as if they are Jesse tasks.
- Stop making Jesse decide agent-owned work like email discovery or basic enrichment.

## What To Keep

- Keep strict guardrails around sends, provider retries, CRM writes, Paperclip mutations, deploys, and prospect contact.
- Keep current folders where they are for now, because scripts and artifacts reference them.
- Keep the existing lane status files as historical/fallback context.
- Keep `gtmdot-sites/messages/status/START-HERE.md` as the index.
- Keep CRM v2 lab separate from production until explicitly approved.

## CRM v2 Simplification Requirement

CRM v2 should implement the simplified model directly:

- default view: **Build / Fix / Send / Needs Jesse**,
- each card: company, trade, owner, one next action, one CTA,
- no raw URL/claim code unless actionable,
- agent-owned work shown as queued/running/blocked, not Jesse workload,
- company page: one-screen cockpit plus detail tabs,
- Paperclip/orchestration state summarized in plain English.

If CRM v2 does this, separate lane chats become unnecessary for normal operation.

## Recommended New Conversation Setup

### GTMDot Ops Chat

Paste:

```text
You are the GTMDot Ops coordinator. Keep this simple.

Read:
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-gtmdot-simplification-audit.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/START-HERE.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md

Your job is to collapse GTMDot into Build / Fix / Send / Needs Jesse. Do not create more permanent lanes. Recommend the next highest-leverage action and keep one concise status file current.

No CRM/Supabase writes, Paperclip mutations, sends/retries, prospect contact, deploys, DNS/domain/hosting/billing/Stripe changes, or git pushes without explicit approval.
```

### CRM Build Chat

Paste:

```text
You are rebuilding GTMDot CRM v2 so the workflow becomes simple.

Read:
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-gtmdot-simplification-audit.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-new-chat-structure-and-transfer-briefs.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md
- /Users/bruce/.openclaw/workspace/brucecom-v3/docs/CRM-V2-PRODUCT-BRIEF.md
- /Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/

The current CRM v2 is too complex. Rebuild around Build / Fix / Send / Needs Jesse, action owner, and one next action. Cards should not show raw URL, claim code, history-only, open item noise, or missing-field labels unless directly actionable. Company page should be a one-screen cockpit plus detail tabs.

No production replacement, CRM writes, Paperclip mutations, sends, provider calls, deploys, or prospect contact without explicit approval.
```

## Bottom Line

GTMDot does not need five permanent chats.

It needs:

1. One GTMDot Ops chat to run the business workflow.
2. One CRM Build chat to make the CRM replace the coordination mess.
3. Temporary task chats only when useful, closed after they report back.

The desired end state is not better chat management. It is fewer chats because the CRM finally shows the truth.

