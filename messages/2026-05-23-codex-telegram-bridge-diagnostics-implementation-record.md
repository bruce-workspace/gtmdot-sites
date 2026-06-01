# Codex Telegram Bridge Diagnostics Implementation Record

Generated: 2026-05-23

## Scope

Jesse authorized Codex to inspect and build read-only Telegram bridge diagnostics after Claude cleaned up the Mini Claude Telegram plugin state.

Allowed scope was limited to:

- Reading Claude Telegram plugin config/status files.
- Inspecting process lists for Claude, Telegram plugin, Composio, and `bun server.ts` pollers.
- Creating read-only diagnostic scripts/artifacts under `gtmdot-sites/workers` and `gtmdot-sites/messages/status`.
- Reporting duplicate pollers, stale `.in_use` files, bot policy config, and recommended cleanup.

## Files Created

```txt
/Users/bruce/.openclaw/workspace/gtmdot-sites/workers/telegram_bridge_health.py
/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/telegram-bridge-latest.md
/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-telegram-bridge-health-runbook.md
```

## Current Diagnostic Result

The Codex health check reports the Mini Claude Telegram bridge is currently healthy:

- Telegram env file exists.
- `access.json` parses.
- DM policy is `allowlist`.
- Jesse's DM sender ID is allowlisted.
- Bruce Group `-1003666831629` is configured with `requireMention: true`.
- `mentionPatterns` includes `@MiniClaudeGTMBot`.
- `bot.pid` points at live PID `42616`.
- Exactly one `bun server.ts` poller is running.
- Exactly one Telegram plugin process is running.
- `.in_use` has no live or stale PID refs.

The live poller lineage is:

```txt
Terminal -> zsh/login -> claude PID 36633 -> bun loader PID 42614 -> bun server.ts PID 42616
```

## Read-Only Command

Run:

```bash
python3 /Users/bruce/.openclaw/workspace/gtmdot-sites/workers/telegram_bridge_health.py --write-status
```

If Codex/macOS blocks Python from inspecting processes, rerun with explicit permission for read-only process inspection. The script is intentionally non-mutating.

## Next Human Test

Jesse should now test inbound routing:

Direct DM to `@MiniClaudeGTMBot`:

```txt
Mini DM post-cleanup test. Please reply: MINI DM ACK
```

Bruce Group -> Agent Sync topic:

```txt
@MiniClaudeGTMBot Agent Sync post-cleanup test. Please reply in this topic with: MINI AGENT SYNC ACK
```

Expected:

- Both messages arrive in the active Mini Claude session as Telegram channel tags.
- Mini Claude replies through the Telegram tool.
- Agent Sync reply stays in the Agent Sync topic.

## Actions Explicitly Not Performed

- No processes killed by Codex.
- No files deleted by Codex.
- No Claude/Telegram/Composio settings changed by Codex.
- No Telegram messages sent by Codex.
- No CRM/Supabase writes.
- No Paperclip mutations.
- No deploys.
- No outreach sends.
- No git pushes.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.

## Follow-Up If Test Fails

If the DM or Agent Sync test fails:

1. Re-run `telegram_bridge_health.py --write-status`.
2. Check whether poller count is still exactly one.
3. If duplicate pollers appear, identify the non-`bot.pid` poller parent chain before killing anything.
4. If zero pollers appear, reconnect Telegram in Claude with `/mcp`.
5. If one poller remains and messages still do not arrive, investigate Telegram plugin access policy or OpenClaw/Bruce token overlap.

