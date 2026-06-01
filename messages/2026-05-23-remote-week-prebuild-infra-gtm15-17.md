# Remote-Week Pre-Build Infrastructure Packet - GTM-15/GTM-16/GTM-17

Generated: 2026-05-23T12:48:39-04:00  
Owner: Codex / Pre-Build Coordination  
Mode: coordination artifact only; board-clearing subordinate  
Canonical ledger: `gtmdot-sites/messages`  
Source template: `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md`

## Scope

This packet advances reusable pre-build infrastructure only:

- `GTM-15` - reusable pre-build Paperclip template.
- `GTM-16` - Browserbase evidence packet schema.
- `GTM-17` - R1VS build packet template.

It does not start a new prospect build, authorize R1VS work, write CRM, mutate Paperclip, deploy, send outreach, contact a prospect, or change production files.

## Current State

Pre-Build remains subordinate to board clearing. The active remote-week queue says the closest revenue path is already-built or near-ready prospects, especially Harrison, InTire, and the QA-approved/send-packet batch. Pre-Build should stay ready by improving packet quality, not by adding new active prospects.

The existing template already defines the right ten-stage flow:

1. Intake validation.
2. Browserbase evidence.
3. Source-of-truth check.
4. Known unknowns / decisions.
5. R1VS build packet.
6. R1VS return packet.
7. Multi-page structure check.
8. Bruce asset / review enrichment handoff.
9. Mini/Post-Build QA handoff.
10. Jesse review / CRM-ready summary.

The remote-week action is to freeze the reusable contract so future lanes do not need Slack/Telegram copy-paste.

## GTM-15 - Reusable Paperclip Template

Recommended child issue stages for future clean pre-build prospects:

| Stage | Required artifact | Done condition | Stops for Jesse |
| --- | --- | --- | --- |
| 01 Intake validation | `<slug>-01-intake-validation.md` | Name, slug, vertical, CRM existence state, source paths, duplicate/recovery status, and no-write/no-send guardrails recorded. | CRM record creation, CRM stage movement, duplicate merge/identity decision. |
| 02 Browserbase evidence | `<slug>-02-browserbase-evidence.md` and optional `browserbase-evidence.json` | Public sources checked or blocked; URLs, timestamps, screenshots, candidates, confidence, and known unknowns recorded. | Paid non-approved API use, captcha/login bypass, treating candidates as CRM-ready truth. |
| 03 Source-of-truth check | `<slug>-03-source-of-truth.md` | Canonical workspace path, branch, CRM/Paperclip/Git state, and case type recorded. | Production repo edits, reclassifying old one-page recovery work. |
| 04 Known unknowns / decisions | `<slug>-04-known-unknowns-decisions.md` | Unknown owner/email/address/review/service/photo/domain claims listed with owner, severity, next source, and blocker status. | Identity flags, risky claims, tenure, warranties, financing, awards, guarantees, licenses. |
| 05 R1VS build packet | `<slug>-05-r1vs-build-packet.md` | Git/message packet exists with inputs, constraints, source links, done conditions, output path, and forbidden actions. | Creating/sending executable R1VS job. |
| 06 R1VS return packet | `<slug>-06-r1vs-return-packet.md` | Return commit/path, files, gates, blockers, source gaps, and next owner recorded. | Advancing to deploy or CRM changes; treating partial return as complete. |
| 07 Multi-page structure check | `<slug>-07-multi-page-structure-check.md` | True page structure checked; cloned shell pages flagged; old one-page cases exempted when applicable. | Approving shallow cloned shell as true multi-page pilot. |
| 08 Bruce enrichment handoff | `<slug>-08-bruce-enrichment-handoff.md` | Photo/review/source needs routed to Bruce with Browserbase inputs and generated-image guardrails. | Prospect contact, paid enrichment, authenticity-implying image generation. |
| 09 Mini/Post-Build handoff | `<slug>-09-mini-post-build-handoff.md` | R1VS return, Bruce enrichment status, claim UI, responsive/accessibility, asset and QA expectations clear. | Deploys, claim-code registration, preview promotion, production changes. |
| 10 Jesse review / CRM-ready summary | `<slug>-10-jesse-review-crm-ready-summary.md` | Copy/paste CRM note, recommended CRM action, unresolved gates, and exact human decision prepared. | CRM writes, outreach, sends, production release. |

Standing guardrails for every issue:

- No CRM/Supabase writes.
- No Paperclip mutations unless separately approved.
- No deploys.
- No Poplar/Resend/SMS sends.
- No outreach or prospect/customer contact.
- No production GTMDot repo edits.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.
- Git/message packet is canonical instructions/results.
- Paperclip is state/gates/audit trail.
- Telegram/Slack are notification mirrors only.

## GTM-16 - Browserbase Evidence Packet Schema

Browserbase should be the default public browser/enrichment layer, but its output is evidence, not CRM truth.

Required Markdown packet:

```md
# <Prospect> Browserbase Evidence Packet

Generated:
Runner:
Slug:
Paperclip issue:
Mode: read-only public-source evidence

## Guardrails
- No CRM writes.
- No deploys.
- No outreach or prospect contact.
- No login/captcha bypass.
- No paid non-approved API use.
- Candidate facts are not CRM-ready truth until reviewed.

## Sources Checked
| Source | URL | Status | Screenshot/path | Notes |
| --- | --- | --- | --- | --- |

## Sourced Facts
| Fact | Value | Source URL | Confidence | Notes |
| --- | --- | --- | --- | --- |

## Candidate Fields
- Business name:
- Owner/contact:
- Email:
- Phone:
- Address:
- Website/domain:
- Service area:
- Services:
- Hours:
- Social profiles:

## Contact Evidence

## Review Evidence

## Photo Evidence

## Conflicts

## Blocked Sources

## Known Unknowns

## Recommendation
```

Required JSON packet:

```json
{
  "slug": "prospect-slug",
  "generated_at": "ISO-8601",
  "runner": "browserbase",
  "status": "success | partial | failed",
  "guardrails": {
    "crm_writes": false,
    "deploys": false,
    "outreach": false,
    "prospect_contact": false,
    "login_or_captcha_bypass": false
  },
  "sources": [
    {
      "type": "website | gbp | yelp | facebook | bbb | nextdoor | thumbtack | angi | sos | other",
      "url": "",
      "fetched_at": "ISO-8601",
      "status": "ok | blocked | captcha | login_required | tls_error | not_found | failed",
      "screenshot_path": "",
      "notes": ""
    }
  ],
  "candidates": {
    "business_name": [],
    "owner_name": [],
    "email": [],
    "phone": [],
    "address": [],
    "hours": [],
    "services": [],
    "website": [],
    "social_profiles": []
  },
  "reviews": [
    {
      "source": "google | yelp | facebook | bbb | other",
      "reviewer": "",
      "date": "",
      "rating": null,
      "text": "",
      "source_url": "",
      "confidence": 0.0
    }
  ],
  "photos": [
    {
      "source": "google | yelp | website | facebook | other",
      "url": "",
      "local_path": "",
      "caption_or_context": "",
      "license_or_tos_note": "",
      "recommended_use": "hero-candidate | proof-candidate | gallery-candidate | discard",
      "confidence": 0.0
    }
  ],
  "known_unknowns": [
    {
      "field": "owner_name | email | reviews | services | address | other",
      "reason": "",
      "needed_decision_or_source": "",
      "blocks_r1vs": false
    }
  ],
  "blocked_sources": [
    {
      "source": "",
      "url": "",
      "reason": "login_required | captcha | tls_error | not_found | access_control"
    }
  ]
}
```

Default path:

- If canonical prospect source exists: `/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/<slug>/`
- If not reconciled yet: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/`

## GTM-17 - R1VS Build Packet Template

R1VS trigger remains: Paperclip issue plus Git/message build packet. Telegram alone is never enough.

```md
# Codex/Paperclip -> R1VS - <Prospect> Build Packet

Status: draft | approved-to-send | returned
Paperclip parent:
Paperclip stage:
Canonical evidence packet:
CRM prospect ID:
Slug:
Business name:
Vertical/category:
Return packet path:

## Approval Boundary

Allowed:
- Prepare source-grounded multi-page build packet or build artifacts exactly as approved.
- Return Git/message packet only.

Still prohibited:
- No CRM writes.
- No deploys.
- No outreach or prospect contact.
- No production GTMDot repo edits unless explicitly approved.
- No DNS/hosting/billing/domain changes.
- No Poplar/Resend/SMS sends.
- No claim-code, preview URL, email, owner, accreditation, warranty, financing, award, guarantee, tenure, or license invention.

## Source-Backed Inputs

- Name:
- Phone candidate:
- Address candidate:
- Address treatment:
- GBP identity:
- Website:
- Service area:
- Service whitelist:
- Brand direction:
- Review sources:
- Photo sources:
- Known safe URLs:
- Excluded/risky URLs:

## Known Unknowns

| Unknown | Why it matters | Blocks R1VS? | Required owner/source |
| --- | --- | --- | --- |

## Hard Constraints

- Do not invent owner, email, claim code, preview URL, CRM reconciliation, tenure, awards, guarantees, warranties, financing, licenses, or accreditations.
- Do not use excluded domains in prospect-facing copy.
- Do not surface identity flags without Jesse approval.
- Do not convert inferred services into primary claims.
- Do not use placeholder reviews as source truth.

## Required Output

- `legitimacy-check.json`
- `RESEARCH.md`
- `BRAND.md`
- `business-data.json`
- `icon-intent.json`
- `reviews.json` if source-backed
- Multi-page HTML/CSS artifacts
- R1VS return packet with commit SHA, files, gates, blockers, source gaps, and next action

## Done Conditions

- Every factual claim cites a source URL or is labeled inferred.
- Every service page is materially distinct.
- No cloned shell pages.
- Known unknowns are carried forward.
- R1VS gates pass or blockers are explicitly reported.
- Return packet states no deploy, CRM write, outreach, send, prospect contact, DNS/domain/hosting/billing, Stripe, or git push occurred unless separately approved.
```

## Safe Next Action

Use this packet as the working draft for `GTM-15`, `GTM-16`, and `GTM-17`. The next non-production step is to convert it into Paperclip issue comments/status updates only if Jesse approves Paperclip mutations, or keep it as the file-ledger source until that approval exists.

## Jesse Approval Needed

No approval is needed to keep this file as a coordination artifact.

Approval is needed before:

- Mutating Paperclip issues.
- Sending an executable R1VS build job.
- Starting any new prospect build.
- Writing CRM/Supabase.
- Deploying.
- Sending Poplar/Resend/SMS.
- Contacting a prospect/customer.
- Pushing git.

## Explicit No-Action Statement

No CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends, prospect/customer contact, production edits, DNS/domain/hosting/billing changes, Stripe actions, git pushes, or new prospect build starts were performed.
