# OpenClaw Capability Radar

Last checked: 2026-10-12T13:30:00Z

## Snapshot

- Latest public release: v2026.10.2, published 2026-10-12T05:34:44Z, release SHA `b8952d477f0c932d8ddc6da5c89cab5a169b6ff1`.
- Release-watch comparison: matches `/Users/bruce/.openclaw/workspace/openclaw-release-watch.md`; no newer release than the current watch marker.
- Local CLI: `OpenClaw 2026.6.1 (2e08f0f)`, so the local install is still several trains behind the latest public release.
- Plugin inventory: 132 plugins total. Enabled: active-memory, anthropic, brave, browser, codex, google, memory-core, minimax, ollama, openai, openrouter, telegram, lossless-claw.
- Dormant but relevant local capabilities include device-pair, talk-voice, voice-call, workboard, memory-lancedb, memory-wiki, Slack/WhatsApp/Signal/iMessage/Discord/Teams channels, Exa/Firecrawl/Tavily/Perplexity/SearXNG search, and multiple model routing providers.
- Plugin registry diagnostic: persisted registry points at a different bundled plugin tree; `openclaw plugins registry --refresh` is a maintenance action to run only after Jesse approves.
- Doctor lint: plaintext secret-bearing config fields remain; Telegram `groupPolicy="open"` remains; Slack skill is allowed but unavailable.

## Capability Picks

| Capability | Classification | Why it matters | Suggested next step |
| --- | --- | --- | --- |
| v2026.10.2 upgrade rehearsal | Test in sandbox | Latest release fixes first-upgrade and in-place update completion, Gateway freezes, cron/plugin-registry access, Telegram delivery, session/subagent truncation, provider-native compaction, prompt-cache stability, and cross-chunk secret redaction. | Stage a sandbox upgrade from 2026.6.1 to v2026.10.2. Verify startup, Gateway UI, plugin inventory, Telegram, cron, Codex sessions, browser, and memory before touching the main install. |
| SecretRefs and Telegram policy cleanup | Adopt now | Doctor still flags plaintext `gateway.auth.token` and provider keys in config, plus open Telegram group policy. v2026.10.2 improves secret redaction, but config hygiene is still the higher-value local action. | Plan a SecretRefs migration with `openclaw secrets configure` or `openclaw secrets apply`, then run `openclaw secrets audit --check`. Consider `channels.telegram.groupPolicy="allowlist"` with explicit allowed senders. |
| Cron, heartbeat, and Telegram delivery regression test | Test in sandbox | v2026.10.2 specifically fixes scheduled cron runs losing the Gateway plugin registry, manual cron runs losing tool access, max thinking drops on cron/hook turns, and Telegram reply/delivery edge cases. | Create a harmless sandbox cron that sends to Telegram, run one manual cron, restart Gateway, and confirm one clean delivery with tools available. |
| Memory/context/compaction path | Test in sandbox | OpenAI and Anthropic API-key routes now default to provider-native compaction, compaction recovers during auth cooldown, and memory/tool context advancement fixes landed. Local active-memory, memory-core, and lossless-claw are already enabled. | Run a long multi-turn task with memory_search plus a subagent/session handoff; compare compaction behavior, prompt-cache stability, and recall quality before and after sandbox upgrade. |
| Subagents, ACP, and session continuity | Test in sandbox | v2026.10.2 fixes truncated subagent/ACP answers, late child receipts, requester turns stopping after delivery expiry, and Codex sessions stopping after thread unloads. The dormant ACPX runtime is present but disabled. | In sandbox, spawn a Codex subagent and one long ACP/Codex session, interrupt/reload once, then confirm final answers are complete and history provenance stays sane. |
| Browser, nodes, and workboard surfaces | Watch | Browser is enabled locally, while device-pair and workboard are installed but disabled. v2026.10.2 fixes repeated browser replies, tab eviction, Gateway title/catalog freezes, and Control UI reconnects. | After upgrade rehearsal, test browser automation and node/device pairing paths only if there is a concrete workflow. Keep workboard disabled until Bruce/Jesse want an agent issue/session dashboard. |
| Voice/Talk and provider routing | Watch | OpenAI/Google realtime voice are enabled via providers; dormant talk-voice, voice-call, Azure/ElevenLabs/local TTS, xAI, Bedrock, Vercel AI Gateway, LiteLLM, Qwen, Groq, DeepSeek, and others are available. | Avoid broad provider churn. Pick one real voice or routing use case first, then test the smallest required plugin in sandbox. |

## Backlog

- Sandbox upgrade rehearsal from 2026.6.1 to v2026.10.2 with current config copied and secrets protected.
- SecretRefs migration plan for `gateway.auth.token` and provider API keys flagged by Doctor.
- Telegram allowlist design for Jesse/Bruce, including allowed group IDs and senders.
- Plugin registry refresh approval item: run `openclaw plugins registry --refresh` only when Jesse explicitly approves.
- Slack skill cleanup: configure Slack or disable the stale allowed skill after confirming it is unused.
- Sandbox cron matrix: scheduled run, manual run, Gateway restart, tool access check, Telegram delivery check.
- Context stress test: long Codex task, subagent handoff, memory_search, compaction, and session recovery.
- Optional dormant plugin trials: `device-pair`, `workboard`, `talk-voice`, `voice-call`, `memory-lancedb`, or one alternate search/provider plugin only when tied to a workflow.

## Next Tests

1. Build a v2026.10.2 sandbox and run `openclaw plugins list --json`, `openclaw --version`, and `openclaw doctor --lint --json`.
2. Run the cron/Telegram regression: scheduled cron, manual cron, Gateway restart, and delivery confirmation.
3. Run a long context task with memory_search, subagent/session handoff, and post-turn compaction.
4. Test browser automation after a Gateway restart and check for repeated replies or lost reconnect state.
5. Draft the SecretRefs and Telegram allowlist config change for Jesse approval.

## Sources Checked

- GitHub release API: `https://api.github.com/repos/openclaw/openclaw/releases/latest`
- GitHub release notes: v2026.10.2 body from the latest release API response.
- Local files: `/Users/bruce/.openclaw/workspace/openclaw-release-watch.md`
- Local commands: `openclaw plugins list --json`, `openclaw --version`, `openclaw doctor --lint --json`
