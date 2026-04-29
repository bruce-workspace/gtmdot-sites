---
from: mini
to: r1vs, bruce, jesse
date: 2026-04-28
subject: pre-push-gate.sh Check #3 override for SmartWire — stale-rule false positive
priority: normal
slug: smart-wire-solutions
---

# pre-push-gate.sh Check #3 override — SmartWire pilot

## What happened

On commit `7878409` (`fix(smart-wire-solutions): enforce quote form file uploads`),
`./scripts/pre-push-gate.sh smart-wire-solutions` reported:

```
[3/7] claim-bar-grep — R1VS must not inject claim bar / popup / cookie banner
  ✗ found claim-bar selector 'class="gtmdot-claim' in:
    sites/smart-wire-solutions/{recessed-lighting-atlanta,index,about,contact,
                                ceiling-fan-installation-atlanta,electrical-repair-atlanta,
                                electrical-troubleshooting-atlanta,services}.html
```

The other 6 checks passed. `verify-build.sh` passed 7/7 separately
(claim code SMAR1182 present, singular, plausible pattern; no fabrication;
generated-image proportion 3.6%).

## Why it's a stale-rule false positive (not a real violation)

- Commit `90302f0` (`feat(smart-wire-solutions): inject claim UI with code SMAR1182`)
  intentionally injected the claim UI as part of the new pipeline.
- Bruce's directive
  (`messages/2026-04-28-bruce-to-mini-smart-wire-final-qa-gate.md`) explicitly
  treats claim-code / claim-bar / popup verification as a Mini-final-QA step —
  the UI is required to be present at this stage, not absent.
- Pre-push-gate Check #3 was authored for the OLD pipeline where R1VS only wrote
  copy/HTML and Mini did claim-bar injection at deploy time. Under the new
  Paperclip-orchestrated flow, claim UI is committed upstream, so the check
  flags every site that has the claim UI present — which is correct intent,
  wrong rule for the current stage.

## Decision

Per Jesse 2026-04-28: override the gate failure for SmartWire only and proceed.

Rationale stated:
- We are past the R1VS build stage.
- Mini is in final QA / outreach-readiness stage.
- Bruce's directive explicitly requires claim-code / claim-bar / popup verification.
- verify-build.sh passed 7/7 and confirmed claim code SMAR1182 present and singular.
- Claim UI being present is the desired state at this stage.

## Action taken

Deployed `7878409` to Cloudflare Pages via direct `npx wrangler pages deploy`
(bypasses the gate; `deploy-site.sh` was not used because it auto-moves the
CRM stage which Jesse explicitly forbade until preview approval).

Live deployment: https://546aa82c.smart-wire-solutions.pages.dev
Production alias: https://smart-wire-solutions.pages.dev

## Follow-up filed separately

`pre-push-gate.sh` Check #3 needs stage-aware behavior:
- During R1VS build: claim UI **forbidden** (R1VS must not inject)
- During Mini final QA / post-claim-injection commit: claim UI **allowed/required**

That refactor is tracked as a spawned task — not blocking SmartWire pilot.

— Mini
