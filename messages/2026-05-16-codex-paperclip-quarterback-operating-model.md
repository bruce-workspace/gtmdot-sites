---
from: codex
to: jesse
date: 2026-05-16T02:14:56Z
subject: Paperclip quarterback operating model for GTMDot lanes
priority: high
---

# Paperclip Quarterback Operating Model

Jesse direction: Codex should act as the main quarterback for GTMDot execution. Paperclip should be the orchestration/control layer that keeps all GTMDot lanes coordinated, auditable, and stage-aware.

## Working Metaphor

- Codex = quarterback / execution coordinator
- Paperclip = playbook + scoreboard + referee
- CRM = customer/prospect database and visible pipeline
- Bruce = enrichment/photo/review/image-generation player
- R1VS = scaffold/build-structure player
- Browserbase = default browser/scraping execution layer
- Composio/Telegram/Slack = communication and notification pipes, not source of truth
- GTMDot project lanes = specialized units that all report through Paperclip

Paperclip should not be a passive note pile. It should answer:

- What prospect is active?
- What stage is it in?
- Who owns the next action?
- What artifact is required?
- What condition marks the step done?
- What blockers exist?
- What is allowed next?
- What is forbidden until approval?

## Lane Relationships

### GTMDot Platform

Owns CRM, dashboard, admin UI, pipeline UX, channel-state model, analytics surfaces, pricing/product site, and future CRM v2.

Platform consumes:

- Outreach results and channel state
- Post-build QA/preflight state
- Pre-build/R1VS source-of-truth status
- Paperclip issue/gate status

Platform emits:

- CRM stage/state changes after approved actions
- dashboard/analytics needs
- UI gaps discovered during operations
- CRM v2 requirements

### Pre-Build Coordination

Owns prospect intake quality, Browserbase evidence packets, source validation, R1VS build packet creation, and build-return acceptance criteria.

Pre-build consumes:

- CRM research-stage prospects
- Browserbase enrichment results
- Bruce enrichment judgment where needed
- Jesse strategic decisions

Pre-build emits:

- R1VS build packets
- known-unknowns packets
- source-of-truth packets
- initial Paperclip issue trees

### Post-Build Operations

Owns built-site readiness after R1VS returns: source reconciliation, deploy readiness, claim code, claim UI, screenshots, postcard assets, email previews, preflight gates, and QA artifacts.

Post-build consumes:

- R1VS returned site/source
- Bruce asset intelligence
- Browserbase evidence where source gaps remain
- CRM claim/prospect fields

Post-build emits:

- QA packets
- deploy recommendations
- blocker packets
- needs_approval readiness packets
- outreach_staged readiness packets

### Outreach Operations

Owns channel readiness and channel execution state: postcards, emails, future SMS, replies, bounces, follow-ups, inbox monitoring, and customer/prospect response workflow.

Outreach consumes:

- Post-build outreach-ready assets
- CRM contact fields
- approved postcard/email/SMS channels
- Poplar/Resend/Gmail event state

Outreach emits:

- channel-state updates
- send/readiness gaps
- bounce/reply/follow-up alerts
- analytics requirements for Platform
- customer/prospect response packets

### Experiments

Owns non-production exploration: chatbot, voice/call features, retail verticals, new add-ons, and unproven vendor/tooling experiments.

Experiments consume:

- operational pain points from live lanes
- Jesse strategic direction
- vendor/API capability tests

Experiments emit:

- proposals
- prototypes
- graduation criteria
- explicit production handoff requirements

Experiments must not silently become production.

## Paperclip As The Connector

Every cross-lane handoff should be represented in Paperclip as either:

- a child issue
- a required artifact
- a blocker
- a next-action comment
- a status transition

Examples:

- Outreach finds emails are bouncing -> Paperclip blocker informs Platform that CRM needs bounce/channel-state UI.
- Platform adds channel-state UI -> Paperclip links the product change to Outreach’s original operational pain.
- Post-build finds missing postcard renderings -> Paperclip blocks Outreach from send execution.
- Pre-build finds weak source evidence -> Paperclip blocks R1VS build packet or marks known unknowns.
- Bruce returns new gpt-image-2 asset intel -> Paperclip records artifact and unlocks post-build preflight.

## Source Of Truth Boundaries

Paperclip should track workflow truth:

- owner
- gate
- artifact
- blocker
- approval
- next action
- audit trail

CRM should track prospect/business truth:

- prospect fields
- stage
- channel readiness fields/events
- contact data
- approval fields
- outreach event history

Git/messages should track durable technical packets:

- R1VS build packet
- Bruce enrichment packet
- Browserbase evidence packet
- Post-build QA packet
- Outreach/preflight packet

Slack/Telegram should track notification and live coordination only:

- ACKs
- urgent routing
- human-visible alerts
- "go read this canonical artifact" messages

When they disagree:

1. Do not guess.
2. Freeze the affected action.
3. Create or update a Paperclip blocker.
4. Reconcile against CRM + git artifacts.
5. Only then proceed.

## Minimum Paperclip Gate Shape

Each meaningful stage/gate should have:

- owner
- input artifacts
- allowed actions
- forbidden actions
- done condition
- verification command/check
- next stage
- rollback/blocked path

## Immediate Implementation Priority

1. Use this operating model for board clearing immediately.
2. Treat Browserbase evidence packets as first-class Paperclip artifacts.
3. Make Outreach channel-state gaps feed Platform CRM v2 requirements.
4. Make Post-build preflight outputs feed Outreach readiness.
5. Make Pre-build packets feed R1VS without Slack/manual relay as canonical state.
6. Keep Codex as the active quarterback until Jesse changes the operating model.

