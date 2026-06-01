---
from: codex
to: jesse
date: 2026-05-16T04:33:14Z
subject: Morning GTMDot action list
priority: high
---

# Morning GTMDot Action List

## 1. Do not start with new builds

The fastest path to revenue is board clearing, not another new prospect.

Start with:

- `outreach_sent` truth cleanup
- `outreach_staged` launch readiness
- `qa_approved` staging readiness
- `needs_approval` approval audit

Mbanugo and Landscape Addict stay important, but they should not steal the morning from the backlog.

## 2. Outreach Operations: channel-state table

Ask Outreach Operations to create a 13-row `outreach_sent` table with:

- postcard order/status
- email sent/delivered/bounced state
- reply watcher state
- open flags
- stale/resolved flag candidates
- next safe action

No writes yet.

## 3. Post-Build Operations: inspect closest-to-send batch

Ask Post-Build Operations to audit:

- `the-appliance-gals`
- `harrison-sons-electrical`
- `cityboys`
- `sandy-springs-plumbing`
- `dream-steam`
- `handy-dandy-atlanta`
- `tuckers-home-services`
- `intire-mobile-tire-shop`
- `smartwire-solutions`

For each:

- claim code lookup works
- claim bar and popup exist
- pricing is correct
- postcard rendering exists
- mobile screenshot exists
- email sequence exists if email is present
- no stale flags are blocking
- no deceptive/generated-image provenance issue exists

## 4. GTMDot Platform: CRM v2 lab route

Use HeroUI Pro to prototype a safe CRM v2 lab dashboard, not a production replacement.

Best first slice:

- board by CRM stage
- channel-state badges inside each card
- stale flag count
- postcard state
- email state
- next safe action
- Paperclip artifact link placeholder

Recommended safe route:

```text
/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/lab/crm-v2/
```

## 5. Browserbase/Bruce enrichment

Continue Browserbase evidence on:

- `premier-tv-mounting-atl`
- `trushyne-mobile-detailing`
- `sumptuous-mobile-detailing`
- `plugged-electricians-atl`
- `plumbingpro-north-atlanta`

Use Browserbase as default. Use Scrapfly only when Browserbase fails on a specific source.

## 6. Paperclip recovery

Do not rebuild Paperclip casually.

Morning task:

- locate old `gtmdot-sandbox` config/db/backups
- if not found, decide whether to rebuild Paperclip from file artifacts
- keep `messages/status/*.md` as permanent fallback ledger

## 7. Jesse decisions queued

Jesse likely needs to decide:

- whether to authorize CRM cleanup writes for stale/resolved flags
- whether to suppress/pause hard-bounced email addresses automatically
- whether Poplar status should be polled in addition to webhook intake
- whether `outreach_sent` should remain a single stage plus derived channel states, or split into channel-specific substates
- whether HeroUI CRM v2 should proceed as lab-only prototype this week

