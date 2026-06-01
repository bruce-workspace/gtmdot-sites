---
from: codex
to: jesse, outreach-operations, gtmdot-platform, post-build-operations
date: 2026-05-16T04:33:14Z
subject: Outreach channel-state rollup
priority: high
---

# Outreach Channel-State Rollup

## Summary

The CRM stage `outreach_sent` is not operationally precise enough.

It currently includes prospects where:

- only a postcard was submitted,
- email sequence 1 was sent,
- email sequence 2 was sent,
- email follow-up is due but paused by flags,
- email is missing entirely,
- a hard bounce occurred,
- postcard status has not advanced beyond `submitted`.

This explains the confusion Jesse saw in the board. The stage is doing too much work.

## Current aggregate state

From read-only CRM/API checks:

- `outreach_sent`: 13 prospects
- postcards submitted: 13
- postcards confirmed in production: 0
- postcards confirmed mailed: 0
- postcards confirmed delivered: 0
- emails sent: 10
- emails delivered: 9
- emails bounced: 1
- replies confirmed tracked: 0

## Prospect-level channel summary

| Slug | Email present | Postcard | Emails sent | Open flags | Sequence paused | Next action |
| --- | --- | --- | ---: | ---: | --- | --- |
| `atlanta-drywall-1` | no | submitted | 0 | 0 | no | Send Email 1 |
| `membrenos-pro-home-repair` | yes | submitted | 1 | 2 | yes | Email 2 due |
| `moonstone-pressure-washing` | yes | submitted | 1 | 1 | yes | Email 2 due |
| `atlanta-pro-repairs` | yes | submitted | 1 | 3 | yes | Email 2 due |
| `tech-on-the-way` | yes | submitted | 2 | 0 | no | Email 3 due |
| `atl-mobile-mechanics` | no | submitted | 0 | 6 | no | Send Email 1 |
| `affordable-concrete-repair` | yes | submitted | 0 | 1 | no | Send Email 1 |
| `done-right-drywall` | no | submitted | 0 | 2 | no | Send Email 1 |
| `morales-landscape-construction` | yes | submitted | 1 | 1 | yes | Email 2 due |
| `perez-pools-llc` | yes | submitted | 2 | 0 | no | Email 3 due |
| `locksmith-atlanta-pro` | yes | submitted | 1 | 1 | yes | Email 2 due |
| `roberts-mobile-services` | no | submitted | 0 | 1 | no | Send Email 1 |
| `golden-choice-prowash` | yes | submitted | 1 | 1 | yes | Email 2 due |

## Key risks

### `outreach_sent` overstates channel completion

A prospect can be moved to `outreach_sent` after only one channel is sent. That is useful as a high-level stage, but unsafe as an operating state.

### Email next actions are misleading when no email exists

Several postcard-only prospects still show `Send Email 1` even though `email = null`.

### Hard bounce needs suppression behavior

`morales-landscape-construction` recorded a hard bounce. Continued email follow-up should remain blocked until the address is suppressed, replaced, or explicitly approved.

### Poplar status progression is unproven

All 13 postcards are `submitted`; none are confirmed mailed/delivered in CRM analytics.

### Reply watcher is unproven

No replies are confirmed tracked. Now that Google Workspace aliases are routed into Jesse's mailbox, the next step is proving the Gmail/OpenClaw/CRM intake path for `hello@gtmdot.com`, `support@gtmdot.com`, and `updates@gtmdot.com`.

## Recommended derived channel states

Add a derived dashboard/table before changing schema:

- `postcard_state`: `not_submitted`, `submitted`, `in_production`, `mailed`, `delivered`, `returned`, `suppressed`, `unknown`
- `email_state`: `no_email`, `not_sent`, `sent`, `delivered`, `bounced`, `paused_by_flags`, `suppressed`, `reply_received`, `unknown`
- `reply_state`: `none_seen`, `watcher_unconfirmed`, `reply_seen_unlinked`, `reply_linked`
- `next_email_state`: `not_applicable`, `not_due`, `due`, `overdue`, `paused`, `blocked`

## Immediate no-write next step

Have Outreach Operations produce a review packet for the 13 `outreach_sent` prospects that answers:

1. Which are postcard-only by design?
2. Which need email address enrichment before any email next action?
3. Which are blocked by stale flags versus real blockers?
4. Which need suppression after bounce?
5. Which Poplar order IDs need status polling?
6. Which prospects have no reply-watch coverage?

Do not send or update CRM until that packet is reviewed.

