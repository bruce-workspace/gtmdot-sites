# Pre-Build Infrastructure Refinement - GTM-15/GTM-16/GTM-17 Consumption Gates

Generated: 2026-05-23T15:00:52-04:00  
Owner: Codex / Pre-Build Coordination  
Mode: high-autonomy infrastructure only; board-clearing subordinate  
Canonical ledger: `gtmdot-sites/messages`  
Build/prospect status: no prospect build started

## Purpose

The accepted GTM-15/GTM-16/GTM-17 packet defines the reusable pre-build sequence and packet templates. This refinement makes the output easier for Post-Build, Bruce, R1VS, Outreach, and CRM v2 to consume without requiring Jesse to translate evidence manually.

This is coordination infrastructure only. It does not authorize Browserbase batch work, R1VS jobs, Mbanugo continuation, new prospect builds, CRM writes, Paperclip mutations, deploys, sends, prospect contact, git pushes, or production edits.

## Infrastructure Improved

### GTM-15 - Reusable Pre-Build Template

Add four explicit gates to every future clean-prospect tree:

1. Source-of-truth gate.
2. Known-unknowns gate.
3. Stale-note gate.
4. Evidence-quality gate.

Each gate should be represented as a short section inside the relevant artifact, not as a separate issue unless the prospect is blocked.

Recommended artifact additions:

- `source_truth_summary`
- `known_unknowns_table`
- `stale_note_review`
- `evidence_quality_score`
- `lane_consumption_summary`
- `crm_v2_routing_candidates`

### GTM-16 - Browserbase Evidence Packet Schema

Browserbase packets should produce both raw evidence and lane-specific summaries.

Required lane views:

| Consumer | Needs from Browserbase packet | Format |
| --- | --- | --- |
| R1VS | Safe facts, allowed services, excluded claims/domains, known unknowns that block copy/scaffold. | `r1vs_build_inputs` object plus Markdown summary. |
| Bruce | Photo candidates, review candidates, asset/review risks, synthesis questions, gpt-image-2 needs. | `bruce_enrichment_inputs` object plus Markdown summary. |
| Post-Build | Source URL, preview/source folder hints, asset gaps, screenshot prerequisites, claim-code readiness blockers. | `postbuild_readiness_inputs` object plus Markdown summary. |
| Outreach | Email/address/phone confidence, provider payload risks, postcard eligibility, reply/contact risks. | `outreach_readiness_inputs` object plus Markdown summary. |
| CRM v2 | Candidate fields, confidence, conflict flags, stale-note needs, exact routing recommendation. | `crm_v2_intake_routing` object plus Markdown summary. |

Recommended JSON additions:

```json
{
  "lane_views": {
    "r1vs_build_inputs": {
      "safe_business_name": "",
      "safe_phone": "",
      "safe_address": "",
      "address_treatment": "storefront | service_area | unknown | conflict",
      "service_whitelist": [],
      "service_candidates_needs_review": [],
      "brand_direction_source_backed": [],
      "excluded_domains_in_copy": [],
      "claims_to_avoid": [],
      "known_unknowns_blocking_build": []
    },
    "bruce_enrichment_inputs": {
      "photo_candidates": [],
      "review_candidates": [],
      "asset_risks": [],
      "review_integrity_risks": [],
      "gpt_image_2_candidate_need": "none | hero | service imagery | postcard hero | unknown",
      "synthesis_questions": []
    },
    "postbuild_readiness_inputs": {
      "expected_source_folder": "",
      "preview_url_candidate": "",
      "claim_code_candidate": "",
      "asset_gaps": [],
      "screenshot_prerequisites": [],
      "claim_flow_prerequisites": [],
      "known_postbuild_blockers": []
    },
    "outreach_readiness_inputs": {
      "email_candidate": "",
      "email_confidence": "none | low | medium | high | verified",
      "phone_candidate": "",
      "mailing_address_candidate": "",
      "mailing_address_confidence": "none | low | medium | high | verified",
      "poplar_payload_risks": [],
      "resend_risks": [],
      "contact_safety_notes": []
    },
    "crm_v2_intake_routing": {
      "recommended_stage": "needs_enrichment | needs_decision | needs_approval | blocked | reject",
      "recommended_owner": "codex | bruce | r1vs | mini_postbuild | outreach | jesse",
      "next_action": "",
      "paperclip_issue_candidate": "",
      "crm_write_recommended": false,
      "crm_write_requires_jesse": true,
      "field_conflicts": [],
      "stale_notes_to_revalidate": []
    }
  }
}
```

### GTM-17 - R1VS Build Packet And Return Contract

R1VS packets should carry a machine-checkable constraint block so future Post-Build and CRM v2 can detect whether R1VS stayed inside the authorized build scope.

Add to every R1VS build packet:

```json
{
  "r1vs_authorization": {
    "paperclip_issue": "",
    "authorization_status": "draft | approved_to_send | returned",
    "allowed_actions": [
      "source-grounded scaffold",
      "multi-page structure",
      "return Git/message packet"
    ],
    "forbidden_actions": [
      "crm_write",
      "deploy",
      "outreach",
      "prospect_contact",
      "dns_domain_hosting_billing",
      "poplar_resend_sms_send",
      "git_push_without_approval"
    ],
    "source_packet": "",
    "return_packet_required": true
  }
}
```

R1VS return packet must include:

- `source_packet_used`
- `commit_or_path`
- `files_created_or_changed`
- `true_multi_page_result`
- `cloned_shell_risk`
- `facts_without_sources`
- `constraints_followed`
- `constraints_violated`
- `known_unknowns_carried_forward`
- `next_owner`
- explicit no-action statement

## Gate Definitions

### Source-of-Truth Gate

Pass when:

- Canonical source folder or message path is named.
- CRM record existence is checked or explicitly unknown.
- Source packet path is recorded.
- Preview URL, claim code, email, phone, address, and owner are each labeled as `crm_truth`, `source_candidate`, `local_artifact`, `inferred`, `conflict`, or `unknown`.

Fail/block when:

- Two identities appear merged.
- Candidate email/address/owner is treated as CRM truth without review.
- Source folder and deployed preview disagree in a way that affects build/outreach.

### Known-Unknowns Gate

Pass when every unknown has:

- field,
- why it matters,
- source to check next,
- owner,
- severity,
- whether it blocks R1VS, Bruce, Post-Build, Outreach, or CRM.

Fail/block when:

- Owner/email/address/service/review/domain uncertainty could create prospect-facing false claims.
- R1VS would need to invent facts to proceed.

### Stale-Note Gate

Pass when:

- Notes/blockers older than 7 days are not treated as active blockers without current revalidation.
- Each old note is marked `open`, `stale`, `resolved`, `overridden`, `current_blocker`, or `non_blocking_ux`.
- Current evidence path or screenshot is included when the note remains blocking.

Fail/block when:

- April/older notes are used to stop QA/staging/outreach without fresh evidence.
- A currently visible live issue is dismissed only because the old note is stale.

### Evidence-Quality Gate

Recommended scoring:

- `A`: source-backed, current, corroborated, lane-ready.
- `B`: source-backed but single-source or minor uncertainty.
- `C`: candidate evidence; usable only with labels and known unknowns.
- `D`: conflicting or stale; needs review before use.
- `F`: unsupported, placeholder, invented, or unsafe.

Minimum before R1VS:

- Business identity: `A` or `B`.
- Category/service scope: `A`, `B`, or labeled `C`.
- Address treatment: `A`, `B`, or explicit `unknown/service-area`.
- Reviews: `A` or `B` if quoted or summarized; otherwise omit.
- Owner/email: may be unknown, but must not be invented.

Minimum before Outreach:

- Email and/or mailing address must be `A` or `B`, or explicitly Jesse-approved despite lower confidence.
- Provider payload risks must be listed.
- Stale notes must be reviewed.

## CRM v2 Intake And Routing Fields

Recommended additive CRM v2 fields or derived UI fields for new prospect intake:

| Field | Type | Purpose |
| --- | --- | --- |
| `intake_source_packet_path` | string | Link to canonical Git/message evidence packet. |
| `paperclip_parent_issue` | string | Link CRM prospect to coordination issue. |
| `prebuild_stage` | enum | `intake`, `evidence`, `source_check`, `known_unknowns`, `r1vs_packet`, `r1vs_return`, `bruce_enrichment`, `postbuild_handoff`, `jesse_review`. |
| `evidence_quality` | enum | Overall `A/B/C/D/F` evidence grade. |
| `field_conflicts_count` | number | Show whether CRM truth conflicts with source evidence. |
| `crm_ready_fields` | object | Fields ready for Jesse-approved CRM write. |
| `candidate_fields` | object | Candidate values that are not CRM truth. |
| `blocked_lanes` | array | `r1vs`, `bruce`, `postbuild`, `outreach`, `crm`, `jesse`. |
| `next_owner` | enum | `codex`, `bruce`, `r1vs`, `mini_postbuild`, `outreach`, `jesse`. |
| `next_action` | string | One exact action, not a paragraph. |
| `stale_note_count` | number | Historical notes needing review. |
| `current_blocker_count` | number | Fresh, evidence-backed blockers. |
| `provider_payload_risk` | object | Poplar/Resend risk before sends. |
| `r1vs_authorization_status` | enum | `not_ready`, `draft_packet`, `approved_to_send`, `returned`, `blocked`. |

UX recommendation:

- Show `CRM truth`, `candidate evidence`, and `unknown` as separate columns.
- Never silently promote candidate evidence into CRM fields.
- Show the exact next owner/action at the top of the prospect view.
- Surface Paperclip issue and latest artifact links next to the action.

## How This Helps Board Clearing

- Keeps Pre-Build from creating new messy downstream work while board clearing is active.
- Makes future evidence packets directly usable by Post-Build, Bruce, R1VS, Outreach, and CRM v2.
- Reduces repeated manual interpretation of Browserbase output.
- Gives CRM v2 concrete fields for intake routing and source/candidate separation.
- Prevents stale notes and candidate fields from blocking or contaminating outreach decisions later.

## Next Safe Infrastructure Work

If spare bandwidth exists, the next safe step is to create static Markdown/JSON starter templates for:

- Browserbase evidence packet.
- R1VS build packet.
- R1VS return packet.
- Source-of-truth gate.
- Known-unknowns gate.

Do not run Browserbase, trigger R1VS, or attach anything to Paperclip without separate approval.

## Explicit No-Action Statement

No Browserbase batch work, R1VS jobs, Mbanugo continuation, new prospect builds, CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends, prospect/customer contact, production edits, git pushes, DNS/domain/hosting/billing changes, or Stripe actions were performed.
