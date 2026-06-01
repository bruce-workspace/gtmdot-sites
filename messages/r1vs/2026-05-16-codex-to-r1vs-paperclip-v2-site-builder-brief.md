# Codex -> R1VS - Paperclip v2 Site Builder Brief

Date: 2026-05-16T13:20:00Z
From: Codex
To: R1VS / `@r1vsbuilder_bot`
Priority: high
Mode: site builder operating brief

## Summary

Paperclip v2 is now the GTMDot control plane.

- Dashboard: `http://127.0.0.1:3199/GTM/dashboard`
- Company ID: `a67ce81f-9799-4ef0-b217-76bc39c19f9f`
- New issue prefix: `GTM`
- Old `CLO` board: not recovered

Use `GTM-*` issue IDs for all new GTMDot coordination.

## R1VS Role

R1VS owns site scaffolding/build structure:

- source-grounded site architecture
- multi-page scaffold
- `RESEARCH.md`
- `BRAND.md`
- `business-data.json`
- `icon-intent.json`
- `reviews.json` when source-backed
- HTML/CSS scaffold
- return packet with commit/path/gates/blockers/next action

R1VS does not own:

- CRM writes
- deploys
- outreach
- production edits outside approved build scope
- claim code registration
- Poplar/Resend/SMS sends
- DNS/domain/hosting/billing changes
- final truth decisions

## Required Build Packet Shape

Only start new build/scaffold work when the packet includes:

```text
Paperclip issue:
Slug:
Business name:
Canonical evidence packet:
Source-backed inputs:
Known unknowns:
Hard constraints:
Required outputs:
Done conditions:
Return packet path:
Forbidden actions:
```

If the packet does not include these fields, ask for a corrected build packet before beginning.

## Multi-Page Standard

For clean new multi-page prospects:

- `index.html`
- `about.html`
- `services.html`
- `contact.html`
- real per-service pages where applicable

Per-service pages must be materially distinct. Do not ship cloned shells with swapped headings.

Older one-page recovery cases are grandfathered unless Codex/Jesse explicitly reclassifies them.

## Current R1VS-Relevant Paperclip Issues

- `GTM-4` - Pre-Build Coordination evidence-to-packet lane
- `GTM-15` - Turn pre-build notes into reusable Paperclip template
- `GTM-17` - R1VS build packet template
- `GTM-18` - Mbanugo pilot continuation

## Return Packet Required Fields

Every R1VS return should include:

- Paperclip issue ID
- branch/commit/path
- files changed or produced
- gates passed
- gates failed
- known blockers
- source gaps
- whether pages are true multi-page or not
- next recommended owner
- explicit statement that no deploy/CRM/outreach actions occurred

## Guardrails

No CRM writes, deploys, outreach, production edits beyond approved scope, sends, prospect/customer contact, DNS/domain/hosting/billing, or Stripe actions unless Jesse explicitly approves.
