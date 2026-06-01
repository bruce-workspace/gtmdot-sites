---
from: codex
to: all-gtmdot-lanes
date: 2026-05-16T02:18:43Z
subject: GTMDot lane status protocol for Codex quarterback coordination
priority: high
---

# GTMDot Lane Status Protocol

Codex sessions do not automatically share live memory across project chats. A session in GTMDot Platform, Outreach Operations, Post-Build Operations, or Pre-Build Coordination may be ahead, blocked, or waiting for approval without this quarterback session knowing.

Therefore every active GTMDot lane must publish machine-readable status into a shared coordination surface.

## Source Priority

1. Paperclip issue/gate status, when Paperclip is available.
2. Git/message-file lane status under `gtmdot-sites/messages/`, always.
3. Slack/Telegram notification, optional mirror only.

Slack/Telegram are not canonical. They should point to the Paperclip issue or message file.

## Required Lane Status File

Each active lane should maintain one latest status file:

- `messages/status/gtmdot-platform-latest.md`
- `messages/status/pre-build-coordination-latest.md`
- `messages/status/post-build-operations-latest.md`
- `messages/status/outreach-operations-latest.md`
- `messages/status/experiments-latest.md`

If `messages/status/` does not exist, create it.

## Required Update Times

Update lane status:

- at session start
- after any artifact is created
- after any blocker is found
- before stopping work
- before asking Jesse for approval
- after any approved action is completed

For long-running work, update at least every 30 minutes.

## Required Fields

Every lane status file must include:

```text
Lane:
Session:
Updated:
Owner:
Mode:

Current objective:

Current state:

Active prospects/items:

Latest artifacts:

Paperclip issues:

Blockers:

Decisions needed from Jesse:

Actions completed since last update:

Actions explicitly not performed:

Next recommended action:

Cross-lane impacts:

Notify:
```

## Cross-Lane Impact Rules

If Outreach discovers a CRM/UI problem:

- write it under `Cross-lane impacts`
- notify GTMDot Platform
- create/update a Paperclip blocker or requirement

If Platform changes CRM stage/channel-state behavior:

- notify Outreach and Post-Build
- document migration/behavior impact

If Post-Build finds a site/postcard/email blocker:

- block Outreach
- notify Platform if the UI hid or misrepresented the issue

If Pre-Build changes build packet requirements:

- notify R1VS
- notify Post-Build if acceptance checks change

## Example Status

```text
Lane: Outreach Operations
Session: Codex Outreach Operations project chat
Updated: 2026-05-16T02:18:43Z
Owner: Codex
Mode: read-only audit

Current objective:
Audit outreach_sent channel truth and identify send/follow-up gaps.

Current state:
13 prospects in outreach_sent. Stage does not distinguish postcard-only vs email sent.

Active prospects/items:
- Morales Landscape: email hard bounce
- ATL Mobile Mechanics: postcard submitted, no email

Latest artifacts:
- messages/2026-05-16-outreach-channel-audit.md

Paperclip issues:
- TBD / not updated

Blockers:
- No channel-state UI in CRM

Decisions needed from Jesse:
- Approve channel-state model before CRM write changes

Actions completed since last update:
- Read-only CRM event audit

Actions explicitly not performed:
- No sends, no CRM writes, no Poplar actions

Next recommended action:
Create per-channel outreach status artifact and feed Platform CRM v2 requirements.

Cross-lane impacts:
GTMDot Platform needs CRM v2 channel-state widgets.

Notify:
GTMDot Platform, quarterback session
```

## Quarterback Session Behavior

This main Codex/GTMDot setup session should periodically read:

- `messages/status/*-latest.md`
- active Paperclip parent/child issues
- CRM state when needed

Then it should produce:

- one consolidated quarterback status
- next action list
- cross-lane blocker list
- Jesse approval queue

