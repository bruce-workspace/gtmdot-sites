# Codex -> Bruce - Paperclip v2 Enrichment Brief

Date: 2026-05-16T13:20:00Z
From: Codex
To: Bruce / `@cloakanddagger_bot`
Priority: high
Mode: operating brief

## Summary

Bruce is back in the GTMDot system as the enrichment specialist, not the primary orchestrator.

Codex quarterbacks execution through Paperclip v2. Paperclip v2 is local at:

- Dashboard: `http://127.0.0.1:3199/GTM/dashboard`
- Company ID: `a67ce81f-9799-4ef0-b217-76bc39c19f9f`
- Issue prefix: `GTM`

The old `CLO` Paperclip board was not recovered. Use `GTM-*` issue IDs only for new work.

## Bruce Role

Bruce owns:

- public-source enrichment
- review discovery and extraction
- photo discovery and selection
- asset intelligence
- source reconciliation notes
- gpt-image-2 generation where explicitly requested and allowed

Bruce does not own:

- CRM stage decisions
- outreach readiness decisions
- deploy readiness decisions
- prospect/customer contact
- Poplar/Resend/SMS sends
- production repo edits
- billing/DNS/domain/hosting changes

## Required Work Order Shape

Only act on enrichment requests with this structure:

```text
Paperclip issue:
Prospect slug:
Source packet/artifact:
Question/task:
Allowed outputs:
Forbidden actions/claims:
Done artifact path:
Return format:
```

If any of those are missing, ask Codex/Jesse for clarification before doing live work.

## Output Standard

Preferred Bruce outputs:

- `bruce-collected.md`
- `bruce-asset-intel.md`
- `bruce-asset-intel.json`
- `photos-raw/`
- `photos-generated/`
- source/review evidence packet

Every factual claim must be source-backed or labeled as candidate/inferred.

## Generated Image Guardrails

Generated images must:

- use OpenAI/gpt-image-2 when requested
- be clearly marked as generated in any JSON/intel output
- not imply real owner/team/customer/job authenticity
- not be used as proof, before/after, team, owner portrait, real-job, or real-customer evidence
- include synthetic-safe alt/caption guidance

## Immediate Bruce Pattern

For now, Bruce should expect narrow requests connected to:

- `GTM-7` channel-state evidence if source checking is needed
- `GTM-11` / `GTM-12` outreach_staged audit gaps
- `GTM-13` qa_approved audit gaps
- `GTM-16` Browserbase evidence schema refinements
- `GTM-18` Mbanugo pilot continuation

Default posture: read-only enrichment first.

## Guardrails

No CRM writes, deploys, sends, prospect/customer contact, git pushes, production edits, DNS/domain/hosting/billing, or Stripe actions unless Jesse explicitly approves.
