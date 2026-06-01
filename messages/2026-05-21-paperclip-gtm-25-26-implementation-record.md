# Paperclip proactive control-plane GTM-25/GTM-26 implementation record

Date: 2026-05-21
Owner: Codex / GTMDot quarterback
Status: implemented locally; no Paperclip/CRM/send/deploy mutations

## Scope

Implemented the approved local runtime foundation for:

- `GTM-25` - Paperclip runtime reliability service.
- `GTM-26` - Dispatcher loop B1.2 scheduled dry-run.

## Files created

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/workers/paperclip_run.sh`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/workers/dispatcher_scheduled_run.sh`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/workers/paperclip_runtime_health.py`
- `/Users/bruce/Library/LaunchAgents/com.gtmdot.paperclip.plist`
- `/Users/bruce/Library/LaunchAgents/com.gtmdot.dispatcher-bridge.plist`

## Runtime behavior

### `com.gtmdot.paperclip`

- Runs Paperclip from the existing local sandbox home.
- Keeps Paperclip alive on `127.0.0.1:3199`.
- Uses the existing instance:
  `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox`
- Logs:
  - stdout: `/private/tmp/gtmdot-paperclip.out.log`
  - stderr: `/private/tmp/gtmdot-paperclip.err.log`

### `com.gtmdot.dispatcher-bridge`

- Runs every 900 seconds.
- Runs dispatcher dry-run only.
- Writes health before and after dispatcher.
- Writes:
  - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/paperclip-runtime-latest.md`
  - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/paperclip-runtime-latest.json`
  - dispatcher digests under `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/`
  - lane outbox files under `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/outbox/`
  - dispatcher state at `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/state.json`
- Logs:
  - stdout: `/private/tmp/gtmdot-dispatcher.out.log`
  - stderr: `/private/tmp/gtmdot-dispatcher.err.log`

## Verification

LaunchAgents loaded:

- `launchctl print gui/501/com.gtmdot.paperclip` reports `state = running`.
- `launchctl print gui/501/com.gtmdot.dispatcher-bridge` reports loaded, scheduled, last exit code `0`.

Health artifact:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/paperclip-runtime-latest.md`
- Current verdict: Paperclip health `ok`; no runtime blockers detected.

Latest dispatcher digest:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-05-21-0631-dispatcher-digest.md`

## Important caveat

When `paperclip_runtime_health.py` is run inside the Codex command sandbox,
Python/curl subprocess access to localhost can be blocked even though normal
shell `curl` works. The LaunchAgent run is the source of truth for the runtime
health artifact because it executes outside that sandbox.

## Guardrails preserved

- No CRM/Supabase writes.
- No Paperclip issue mutations.
- No deploys.
- No Poplar/Resend/SMS sends.
- No prospect/customer contact.
- No git pushes.
- No production site edits.
- No DNS/domain/hosting/billing/Stripe actions.

## Next recommended step

Move from scheduled dry-run to `GTM-27`: lane inbox/outbox acknowledgement
protocol. This should still avoid CRM/send/deploy authority, but it will reduce
Jesse copy/paste by giving each lane a stable file to read and a required
acknowledgement file to write.
