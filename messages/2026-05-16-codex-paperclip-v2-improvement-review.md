# Codex -> GTMDot - Paperclip v2 Improvement Review

Date: 2026-05-16T13:05:00Z
From: Codex
To: Jesse / GTMDot lanes
Priority: high
Mode: introspection after Paperclip v2 rebuild

## Summary

The old Paperclip setup was useful but too fragile: it held workflow state, but the durable recovery path was not strong enough when the local database/config/backups disappeared. The v2 rebuild should not simply recreate the old board. It should make Paperclip the visible control plane while treating the file ledger as the durable black box recorder.

## Improvement 1 - Paperclip Plus File Ledger, Not Paperclip Alone

Old weakness:

- The old `CLO` Paperclip board was useful, but when the local database/config/backups disappeared, the operational state disappeared with it.
- The file artifacts existed, but they were not treated as a required mirror of every important Paperclip state change.

V2 rule:

- Every important Paperclip issue tree, blocker, gate completion, and handoff must have a corresponding file artifact or status entry.
- Paperclip is the cockpit display. The file ledger is the flight recorder.

Concrete implementation:

- Keep `GTM-22` open until automatic backups are verified.
- Keep `GTM-23` open until the permanent file-ledger fallback rule is written.
- For each lane, require `messages/status/<lane>-latest.md` to include active `GTM-*` issue IDs.

## Improvement 2 - Fewer Top-Level Issues, More Gate Discipline

Old weakness:

- The old board appears to have grown into many child issues, but the board state was hard to reconstruct because not every issue mapped cleanly to a lane, gate, owner, artifact, and done condition.

V2 rule:

- Keep top-level Paperclip small and stable:
  - `GTM-1` quarterback/root
  - `GTM-2` outreach
  - `GTM-3` post-build
  - `GTM-4` pre-build
  - `GTM-5` platform
  - `GTM-6` Paperclip recovery/process
- Create child issues only when they represent a specific gate, artifact, blocker, or next action.

Concrete implementation:

- Do not create prospect issue trees casually.
- For board clearing, work off the existing operational children first: `GTM-7` through `GTM-14`.
- For new prospects, create a parent only after the intake/source-of-truth gate exists.

## Improvement 3 - Bruce Gets Narrow Work Orders, Not Broad Context Dumps

Old weakness:

- Bruce is powerful at enrichment, scraping, reviews, photos, and image generation, but broad orchestration requests increase ambiguity and make outputs harder to gate.

V2 rule:

- Codex owns orchestration.
- Bruce receives narrow, source-bounded work orders tied to a specific `GTM-*` issue and required artifact.

Concrete implementation:

- A Bruce request should include:
  - `GTM-*` issue
  - prospect slug
  - source packet path
  - exact question
  - allowed outputs
  - forbidden claims/actions
  - done artifact path
- Bruce should not decide CRM stage, outreach readiness, deploy readiness, or approval state.

## Improvement 4 - Channel-State Truth Before More Outreach

Old weakness:

- CRM `outreach_sent` hides multiple truths: postcard submitted, email sent, postcard delivered, SMS sent, reply received, bounce, paused follow-up.
- That makes Paperclip look like progress while the actual revenue motion may still be incomplete.

V2 rule:

- Outreach state must be channel-specific before we scale sends.
- Paperclip should block outreach progression when a channel is unknown or mismatched.

Concrete implementation:

- Work `GTM-7` first.
- Make `GTM-8` and `GTM-9` explicit blockers for reliable outreach operations.
- Feed resulting needs into `GTM-19` / `GTM-20` so the CRM v2 UI reflects operational truth.

## Improvement 5 - No More Invisible Cross-Session Progress

Old weakness:

- Different Codex/Claude sessions could be ahead, blocked, or waiting without the quarterback knowing.
- Slack/Telegram messages helped coordination but were not durable enough to be the canonical state.

V2 rule:

- Every active lane updates a status file and references the active `GTM-*` issue.
- Telegram/Slack are notification mirrors only.

Concrete implementation:

- At session start, each lane reads:
  - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-paperclip-v2-rehydration-summary.md`
  - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-lane-status-protocol.md`
  - its own `messages/status/<lane>-latest.md`
- At session stop, each lane updates:
  - active `GTM-*` issue
  - latest artifact
  - blocker
  - next action
  - cross-lane impact

## Recommended Immediate Adoption

1. Publish a short Paperclip v2 routing notice to all active GTMDot sessions.
2. Require every lane to pin itself to one active `GTM-*` issue before doing more work.
3. Start operational clearing with `GTM-7`, not with new build work.
4. Give Bruce only narrow enrichment work orders that cite a `GTM-*` issue and output artifact.
5. Finish `GTM-22` and `GTM-23` before trusting Paperclip as the only control plane.

## Bottom Line

The better version is not "Paperclip, again." It is Paperclip plus durable lane files, narrow Bruce work orders, channel-level outreach truth, and a small stable issue hierarchy. That makes the system better suited to the current reality: Codex quarterbacks, Bruce enriches, R1VS scaffolds, and Paperclip keeps the playbook visible.
