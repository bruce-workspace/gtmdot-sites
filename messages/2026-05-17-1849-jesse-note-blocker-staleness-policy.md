---
from: jesse-via-codex
to: all-gtmdot-lanes
date: 2026-05-17T18:49:19Z
subject: GTMDot note and blocker stale-by-default policy
priority: high
---

# GTMDot Note / Blocker Staleness Policy

Effective immediately, any CRM note, flag, or blocker older than 7 days is stale by default.

## Operating Rule

- Old notes do not automatically block QA, staging, or outreach.
- Before treating an old note as a blocker, re-check it against the current live site, current CRM, and current assets.
- If the issue is resolved or no longer visible, mark it stale, resolved, or overridden in the artifact and recommend closure.
- If the issue is still real, create or preserve a current blocker with today's evidence.
- If the issue is minor polish, classify it as non-blocking UX feedback.
- Do not delete historical notes. Preserve the audit trail.
- Do not write CRM unless separately approved.
- For current board clearing, stale notes should not hold up outreach unless they are revalidated as current blockers.

## Examples

- "Missing claim popup" is stale if the current live site has the popup.
- "Unsplash/stock concern" is stale if the current live HTML/assets no longer show the issue or Jesse accepts the image as good enough.
- "Popup appears immediately on load" is a new/current UX note, but not automatically an outreach blocker unless severity is marked blocking.
- April notes should not block May outreach without fresh verification.

## CRM v2 Requirement

Add explicit stale-note handling:

- Note age.
- Last verified date.
- Current status: open / stale / resolved / overridden / current blocker / non-blocking UX.
- Evidence link or screenshot.
- Owner.
- Blocking vs non-blocking.
- One-click actions: revalidate / mark stale / convert to current blocker.

## Goal

Clear outdated irrelevant issues from the operational board while preserving useful history and allowing fresh, evidence-backed blockers to remain visible.

## Guardrails

- No CRM writes from this policy artifact.
- No deletion of historical notes.
- No outreach, deploy, send, DNS/domain/hosting/billing, Stripe, or production site action is authorized by this artifact.
