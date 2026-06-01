# GTMDot Remote-Week Cadence Protocol - 2026-05-23

Owner: Codex / GTMDot quarterback  
Mode: scheduled coordination protocol  
Applies through: 2026-05-30 unless revoked or replaced  

## Purpose

Keep GTMDot moving while Jesse is remote without requiring manual copy/paste between folders. Each lane should produce fresh, useful state at the right interval, with hard stop-lines around sends, CRM truth, deploys, billing, and prospect contact.

## Existing Local Cadence

The Mac already has scheduled local control-plane jobs:

- `com.gtmdot.dispatcher-bridge`: slowed for remote-week operations to every 2 hours (`StartInterval=7200`) on 2026-05-23.
- Dispatcher script: `/Users/bruce/.openclaw/workspace/gtmdot-sites/workers/dispatcher_scheduled_run.sh`
- Dispatcher output: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/`
- `com.gtmdot.enrichment-dispatcher`: configured every 30 minutes.
- Enrichment script: `/Users/bruce/.openclaw/workspace/gtmdot-sites/scripts/enrichment-dispatcher-cron.sh`

The dispatcher is already producing regular digests under:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/`

## Recommended Lane Cadence

- Main Coordinator / Codex: every 2-3 hours during waking/active remote windows, plus ad hoc when Jesse approves a live action or a scheduled email deadline is near.
- Dispatcher bridge: remote-week interval is every 2 hours (`StartInterval=7200`) unless an active incident requires tighter monitoring.
- Post-Build Operations: every 2-3 hours while board-clearing work remains; recheck gates, repair packets, ready/held queues.
- Outreach Operations: every 2-3 hours while active outreach events or scheduled follow-ups exist; increase to every 45-60 minutes only within 6 hours of a scheduled email or known provider incident.
- CRM v2 / Platform: 45-minute lab-only build loop is acceptable because it is local sandbox work; update status after meaningful build/test cycles, not every loop if nothing changed.
- Pre-Build Coordination: 1-2 times daily unless board clearing needs a template/schema; GTM-15/16/17 infrastructure only.
- Experiments: daily or spare bandwidth only; local-only R&D and graduation criteria.
- Bruce / Enrichment: on routed packets only; source-backed evidence packets only.

## Standard Status Shape

Each lane should write or reply with:

1. Current state.
2. What changed since last run.
3. Closest-to-revenue item.
4. Current blocker.
5. Safe action performed.
6. Exact approval needed, if any.
7. Artifact/status path updated.
8. Explicit no-action statement.

## Prompt For Active Lanes

```text
Continue GTMDot remote-week cadence work for your lane.

Start from:
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-remote-week-cadence-protocol.md
- /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md
- your lane status file under /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/
- the latest dispatcher digest under /Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/

Operate under the high-autonomy approval through 2026-05-30, but preserve hard approval boundaries.

Allowed:
- read-only audits,
- local-only checks/fixes,
- artifact/status updates,
- repair packets,
- readiness packets,
- provider/CRM read-only verification,
- exact approval text.

Still prohibited unless separately approved:
CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends, prospect/customer contact, git pushes, DNS/domain/hosting/billing changes, Stripe actions, production-impacting edits, or destructive cleanup.

Respond with:
1. Current state.
2. What changed since last run.
3. Closest-to-revenue item.
4. Current blocker.
5. Safe action performed.
6. Exact approval needed, if any.
7. Artifact/status path updated.
8. Explicit no-action statement.
```

## Stop Conditions

Stop and write a blocker artifact if:

- A live gate fails.
- A provider returns an error.
- CRM/list/detail/provider truth conflicts.
- Dirty repo blast radius is unclear.
- Another session is editing the same area and there is a conflict.
- A proposed action would send, write CRM truth, deploy, contact a prospect, mutate Paperclip, spend money, or alter production.

## Coordinator Note

The cadence should make Jesse's mobile check-ins simple: one digest, one current queue, and one approval ask at a time. If a lane has nothing meaningful to update, it should say so briefly and avoid generating noise.
