# CRM v2 Additive Field/API Contract Draft

Updated: 2026-05-23
Lane: GTMDot Platform / CRM v2
Mode: Planning + lab implementation only

## Intent

CRM v2 should keep the current CRM as the business pipeline source of truth while adding explicit operational state for channels, provider events, stale notes, Paperclip coordination, and new-prospect routing.

This is additive. It should not remove current fields or require a strategic CRM truth migration while Jesse is remote.

## Current Fields To Preserve

- `stage`
- `stage_entered_at`
- `approved_for`
- `approved_at`
- `email`
- `phone`
- `address`
- `has_email`
- `has_phone`
- `has_address`
- `claim_code`
- `preview_site_url`
- `next_email_at`
- `next_email_sequence`
- `sequence_paused`
- `sequence_paused_reason`
- `postcard_status`
- `emails_sent_count` or event-derived equivalent
- existing outreach events and activity log records

## Additive Objects / Fields Needed

### Prospect Routing

Purpose: show handoff state without letting R1VS or Bruce decide CRM truth.

Suggested fields:
- `routing_state`: `intake_created | evidence_needed | evidence_ready | r1vs_packet_needed | r1vs_packet_sent | r1vs_build_returned | post_build_qa_needed | ready_for_jesse_approval | outreach_preflight | outreach_active | closed`
- `routing_owner`: `Codex | Bruce | R1VS | Post-Build | Outreach | Jesse`
- `routing_next_action`
- `routing_artifact_links`
- `routing_updated_at`

### Notes / Blockers

Purpose: implement Jesse's 7-day stale-note policy without deleting history.

Suggested note/blocker fields:
- `note_id`
- `prospect_id`
- `body`
- `created_at`
- `created_by`
- `last_verified_at`
- `verified_by`
- `current_status`: `open | stale | resolved | overridden | current_blocker | non_blocking_ux`
- `severity`: `blocking | non_blocking | info`
- `owner`: `Codex | Bruce | R1VS | Post-Build | Outreach | Jesse | Paperclip`
- `evidence_links`
- `screenshot_links`
- `paperclip_issue_id`
- `paperclip_issue_url`
- `recommended_action`

### Channel State

Purpose: separate lifecycle stage from actual channel truth.

Suggested channel summary fields:
- `channel`: `postcard | email | sms | reply | support`
- `crm_state`
- `provider_state`
- `approval_state`
- `pause_state`
- `pause_reason`
- `next_due_at`
- `exact_next_action`
- `last_event_at`
- `last_event_source`
- `mismatch_flags`

### Provider Events

Purpose: distinguish CRM event summaries from Poplar/Resend/Gmail provider truth.

Suggested endpoint:
- `GET /api/prospects/:id/provider-events`

Suggested event shape:
- `id`
- `prospect_id`
- `provider`: `poplar | resend | gmail | crm`
- `channel`: `postcard | email | reply | support`
- `provider_event_type`
- `normalized_event_type`
- `provider_object_id`
- `occurred_at`
- `payload_summary`
- `raw_payload_ref`
- `is_exception`
- `exception_reason`
- `next_action`

Poplar states to normalize:
- `payload_invalid`
- `submitted`
- `in_production`
- `mailed`
- `in_transit`
- `delivered`
- `returned`
- `suppressed`
- `exception`

Resend states to normalize:
- `sent`
- `delivered`
- `opened`
- `clicked`
- `bounced`
- `complained`
- `unsubscribed`

Gmail / reply monitor states to normalize:
- `reply_detected`
- `reply_untriaged`
- `reply_triaged`
- `sequence_paused_by_reply`
- `replied_but_sequence_active`

### Payload Validation

Purpose: surface errors like Poplar name/address/ZIP validation before sends.

Suggested endpoint:
- `POST /api/prospects/:id/preflight/outreach-payload`

Read-only dry-run output:
- `valid`
- `errors`
- `warnings`
- `provider`: `poplar | resend`
- `payload_preview`
- `missing_fields`
- `normalization_applied`
- `exact_next_action`

Current lab derivation already previews:
- Poplar postcard payload gaps: recipient/business name, street address, city, state, ZIP, ZIP format, owner-name fallback.
- Resend email payload gaps: email address, preview site URL, claim code, business name.
- These checks are local/read-only and do not call providers.

### Paperclip Links

Purpose: make coordination visible inside CRM v2 without making CRM v2 the work-control board.

Suggested fields:
- `paperclip_parent_issue_id`
- `paperclip_parent_issue_url`
- `paperclip_child_issue_ids`
- `paperclip_open_blocker_count`
- `paperclip_artifact_links`
- `paperclip_last_sync_at`
- `paperclip_next_owner`

Current lab derivation already previews a `paperclipCoordination` object:
- `parentIssueLabel`
- `blockerState`
- `artifactState`
- `nextOwner`
- `visibleLinks`
- `nextAction`

The current CRM payload does not expose real Paperclip issue URLs yet, so CRM v2 marks these as pending/unknown rather than inventing links.

## UI Contract

CRM v2 should show:
- Lifecycle stage as pipeline position.
- Route state as work-control state.
- Channel state cards for postcard, email, reply, and SMS/future.
- Provider truth split for CRM vs Poplar vs Resend vs hello mailbox.
- Stale-note panel with revalidate/mark stale/convert-to-blocker actions as future controls.
- Paperclip issue/artifact links near every blocker, build handoff, and feedback panel.
- Exact next action in card, sheet, and queue views.

## Explicit Non-Goals During Jesse Away Mode

- No live CRM writes from CRM v2.
- No send controls enabled.
- No production CRM replacement.
- No migration from CRM v1 to CRM v2.
- No Paperclip mutation from CRM v2 without separate approval.
- No reply-body storage decision without Jesse approval.

## Recommended Implementation Order

1. Keep building CRM v2 read-only surfaces against current `/api/prospects`.
2. Add read-only provider event aggregation endpoint.
3. Add note/blocker detail endpoint with stale-policy fields.
4. Add outreach payload dry-run validation endpoint.
5. Add Paperclip link ingestion/display.
6. Only after Jesse approval, add controlled CRM write proposals and approval flow.
