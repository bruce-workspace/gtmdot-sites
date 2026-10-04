Lane: Paperclip Runtime
Owner: Codex / GTMDot quarterback
Updated: 2026-10-04T08:01:16-04:00
Mode: proactive control-plane runtime status

Current state:
- Paperclip health: not ok
- Dashboard tasks: `unavailable`
- Dashboard agents: `unavailable`
- Paperclip LaunchAgent: loaded (path = /Users/bruce/Library/LaunchAgents/com.gtmdot.paperclip.plist)
- Dispatcher LaunchAgent: not loaded (Bad request.)

Latest backup:
- BLOCKED: backup directory missing at `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/data/backups`

Dispatcher:
- Last run: 2026-06-02T08:34:07-07:00
- Latest digest: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-06-02-0834-dispatcher-digest.md`

Blockers:
- Paperclip API is not healthy: {'status': 'unhealthy', 'version': '2026.428.0', 'error': 'database_unreachable'}
- Backup problem: backup directory missing
- Dispatcher LaunchAgent is not loaded.

Actions explicitly not performed:
- No CRM/Supabase writes.
- No Paperclip mutations.
- No deploys.
- No Poplar/Resend/SMS sends.
- No prospect/customer contact.
- No git pushes.
- No production site edits.
- No DNS/domain/hosting/billing/Stripe actions.

Next recommended action:
Use Paperclip runtime status plus the dispatcher digest as the first stop before asking Jesse to relay lane updates manually.
