# Codex -> GTMDot - Paperclip v2 Rehydration Summary

Date: 2026-05-16T12:50:00Z
From: Codex
To: GTMDot lanes
Priority: high
Mode: local Paperclip rebuild from file ledger/artifacts

## Summary

Jesse approved rebuilding the local Paperclip sandbox because the old `gtmdot-sandbox` database/config/backups were not recoverable from this filesystem.

Paperclip v2 is now running locally:

- API: `http://127.0.0.1:3199/api`
- UI: `http://127.0.0.1:3199`
- Dashboard: `http://127.0.0.1:3199/GTM/dashboard`
- Instance path: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox`
- GTMDot company ID: `a67ce81f-9799-4ef0-b217-76bc39c19f9f`
- New issue prefix: `GTM`
- Historical old prefix: `CLO`, not recovered

This is a v2 rebuild, not historical continuity with the old CLO issue database.

## Issues Rehydrated

- `GTM-1` - GTMDot recovered control plane / board clearing
- `GTM-2` - Outreach Operations channel-state cleanup
- `GTM-3` - Post-Build Operations closest-to-send audit
- `GTM-4` - Pre-Build Coordination evidence-to-packet lane
- `GTM-5` - GTMDot Platform CRM v2 / pipeline clarity lab
- `GTM-6` - Paperclip Recovery v2 rebuilt from file ledger
- `GTM-7` - Audit 13 outreach_sent channel states
- `GTM-8` - Verify Poplar postcard progression after submit
- `GTM-9` - Verify GTMDot email/reply watcher
- `GTM-10` - Suppress or resolve Morales hard bounce
- `GTM-11` - Audit outreach_staged: The Appliance Gals
- `GTM-12` - Audit outreach_staged: Harrison & Sons Electrical
- `GTM-13` - Audit qa_approved batch for staging readiness
- `GTM-14` - Define claim UI / postcard / email preflight artifacts
- `GTM-15` - Turn pre-build notes into reusable Paperclip template
- `GTM-16` - Browserbase evidence packet schema
- `GTM-17` - R1VS build packet template
- `GTM-18` - Mbanugo pilot continuation
- `GTM-19` - CRM v2 lab route / dashboard spec
- `GTM-20` - Paperclip links in CRM/Pipeline views
- `GTM-21` - Record unrecoverable old Paperclip state
- `GTM-22` - Verify automatic backups in Paperclip v2
- `GTM-23` - Create permanent file-ledger fallback rule

## Source Artifacts

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-overnight-quarterback-consolidation.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-outreach-channel-state-rollup.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-morning-action-list.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/gtmdot-paperclip-readonly-recovery-snapshot-2026-05-16.md`
- `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md`

## New Rebuild Artifacts

- `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/gtmdot-paperclip-v2-rebuild-log-2026-05-16.md`
- `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/gtmdot-paperclip-v2-rehydration-result-2026-05-16.json`

## Guardrails Observed

- No CRM writes.
- No deploys.
- No Poplar, Resend, SMS, or outreach sends.
- No prospect/customer contact.
- No DNS, domain, hosting, billing, or Stripe changes.
- No git pushes.
- No production site edits.

## Next Action

Start with `GTM-7` because `outreach_sent` currently hides channel-level truth. Then clear the closest-to-send work in `GTM-11`, `GTM-12`, and `GTM-13`.

Keep the file ledger alive even though Paperclip is back. `GTM-22` and `GTM-23` exist specifically so we do not repeat the “missing database means missing board” failure.
