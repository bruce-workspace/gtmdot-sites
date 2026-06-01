# Telegram Bridge Status

Updated: 2026-05-23T14:39:46Z
Mode: read-only diagnostics

## Summary
- Telegram env file present: `True`
- `bot.pid`: `42616`
- `bot.pid` live: `True`
- Bun Telegram pollers: `1`
- Telegram plugin processes: `1`
- `.in_use` live refs: `0`
- `.in_use` stale refs: `0`

## Access Policy
- Status: `ok`
- DM policy: `allowlist`
- Allowed DM sender count: `1`
- Pending pairing count: `0`
- Mention patterns: `@MiniClaudeGTMBot`
- Group `-1003666831629`: requireMention=`True`, allowFromCount=`0`

## Pollers
- PID `42616` PPID `42614` elapsed `12:19`: `/Users/bruce/.bun/bin/bun server.ts`

## Bot PID Tree
- PID `42616` PPID `42614` elapsed `12:19`: `/Users/bruce/.bun/bin/bun server.ts`
- PID `42614` PPID `36633` elapsed `12:20`: `bun run --cwd /Users/bruce/.claude/plugins/cache/claude-plugins-official/telegram/0.0.6 --shell=bun --silent start`
- PID `36633` PPID `1225` elapsed `30:39`: `claude`
- PID `1225` PPID `1222` elapsed `12-12:14:13`: `-zsh`
- PID `1222` PPID `912` elapsed `12-12:14:13`: `login -pfl bruce /bin/bash -c exec -la zsh /bin/zsh`
- PID `912` PPID `1` elapsed `12-12:14:20`: `/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal`
- PID `1` PPID `0` elapsed `12-21:29:18`: `/sbin/launchd`

## Recommendations
- Telegram poller count is healthy: exactly one bun server.ts process is running.

## Actions Explicitly Not Performed
- No processes killed.
- No files deleted.
- No settings changed.
- No Telegram messages sent.
- No CRM/Paperclip/deploy/outreach/git/DNS/billing/Stripe actions performed.
