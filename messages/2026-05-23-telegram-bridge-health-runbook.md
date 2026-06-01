# Telegram Bridge Health Runbook

Generated: 2026-05-23

## Purpose

Codex owns the GTMDot coordination architecture, but each Telegram bot still has its own runtime bridge:

- `@cloakanddagger_bot`: Bruce/OpenClaw gateway.
- `@MiniClaudeGTMBot`: Claude Telegram plugin on the Mini.
- `@r1vsbuilder_bot`: Claude Code Channels/plugin on the MacBook.
- `@gtm_codex_bot`: Composio/Codex Telegram connector.

Telegram is a real-time ACK/notification lane only. Paperclip, Git packets, CRM/Supabase, and local status artifacts remain canonical.

## Current Mini Claude State

As of the latest Codex diagnostic:

- `~/.claude/channels/telegram/access.json` exists and parses.
- DM policy is `allowlist`.
- Jesse's Telegram user ID is allowlisted.
- Bruce Group `-1003666831629` is configured with `requireMention: true`.
- `mentionPatterns` includes `@MiniClaudeGTMBot`.
- `bot.pid` is live.
- Exactly one `bun server.ts` Telegram poller is running.
- `.in_use/` has no stale dead PID files.

Status artifact:

```txt
/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/telegram-bridge-latest.md
```

Diagnostic script:

```txt
/Users/bruce/.openclaw/workspace/gtmdot-sites/workers/telegram_bridge_health.py
```

## Codex Diagnostic Command

Use this for read-only inspection:

```bash
python3 /Users/bruce/.openclaw/workspace/gtmdot-sites/workers/telegram_bridge_health.py --write-status
```

If macOS/Codex sandbox blocks process inspection, rerun with explicit approval for read-only process inspection. The script does not kill processes, delete files, edit settings, send Telegram messages, or touch production systems.

## Healthy State

Healthy Mini Claude Telegram state looks like:

- One `bun server.ts` poller.
- `bot.pid` points at that live poller.
- Poller parent chain is:
  `Terminal -> zsh/login -> claude -> bun run ... telegram/0.0.6 -> bun server.ts`
- `.in_use/` is empty or has only valid live references.
- Bruce Group requires mention.
- Direct DM allowlist includes Jesse.

## Failure Patterns

### Duplicate Pollers

Symptom:

- Two or more `bun server.ts` pollers.
- Telegram messages intermittently vanish.
- Bot starts typing but does not reply.
- Telegram long polling may produce `409 Conflict` behavior.

Likely cause:

- Multiple Claude sessions or repeated `/mcp` reconnects spawned competing pollers for the same bot token.

Safe response:

- Identify which poller matches `bot.pid`.
- Identify the parent chain for each extra poller.
- Close the rogue Claude session if visible.
- Only with explicit approval: remove dead `.in_use` files and kill targeted duplicate pollers.

### Zero Pollers

Symptom:

- Bot is deaf.
- DM and Agent Sync mentions do not arrive in Claude.
- Telegram tools may be disconnected.

Likely cause:

- Claude Telegram MCP server was killed and Claude Code does not auto-respawn it mid-session.

Safe response:

- In Claude, run `/mcp`.
- Reconnect `plugin:telegram:telegram`.
- Re-run the Codex diagnostic.

### Stale `.in_use`

Symptom:

- `.in_use/` contains dead PID files.
- Bot may not auto-stop or restart cleanly.

Safe response:

- Verify each PID is dead.
- Only with explicit approval: remove stale dead PID files.

## Verification Tests

After the diagnostic reports healthy state, Jesse should send:

Direct DM to `@MiniClaudeGTMBot`:

```txt
Mini DM post-cleanup test. Please reply: MINI DM ACK
```

Bruce Group -> Agent Sync topic:

```txt
@MiniClaudeGTMBot Agent Sync post-cleanup test. Please reply in this topic with: MINI AGENT SYNC ACK
```

Expected result:

- Both arrive in the active Mini Claude session as `<channel source="telegram" ...>` tags.
- Claude replies through the Telegram tool.
- The Agent Sync reply stays in the Agent Sync topic.

## BotFather Baseline

For each bot:

- Bot-to-Bot Communication Mode: enabled.
- Allow Groups: enabled.
- Group Privacy: disabled/off.
- Admin rights: minimal.
- Keep: topic-related permission if needed.
- Disable: delete messages, invite users, promote users, restrict users, change group info, stories.

## Coordination Rule

Do not use Telegram as the source of truth.

Use Telegram for:

- ACKs.
- "I saw the packet" messages.
- Real-time routing alerts.
- Human visibility.

Use Paperclip/Git/CRM/local status artifacts for:

- Work authorization.
- Gate state.
- Evidence packets.
- Owner/next-action truth.
- Audit trail.

## Actions Explicitly Not Performed By This Runbook

- No processes killed.
- No files deleted.
- No settings changed.
- No Telegram messages sent.
- No CRM/Supabase writes.
- No Paperclip mutations.
- No deploys.
- No outreach sends.
- No git pushes.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.

