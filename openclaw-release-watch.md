# OpenClaw Release Watch

Last checked: 2026-10-12T12:06:00Z
Latest seen release: v2026.10.2
Published: 2026-10-12T05:34:44Z
Release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.10.2
Release SHA: b8952d477f0c932d8ddc6da5c89cab5a169b6ff1

Notes:
- 2026-10-12 radar check: detected v2026.10.2 as latest. It is a stability-heavy release after 2026.10.1, with fixes for in-place updates, Gateway freezes, cron/plugin-registry access, Telegram delivery, subagent/session truncation, provider-native compaction, prompt-cache stability, and chunk-boundary secret redaction. Android APK was skipped because apps/android/version.json stayed at 2026.8.2.
- 2026-10-08 radar check: detected v2026.9.9 as latest. It adds GPT-6.1 Sol support in the managed Codex runtime/model catalog and focuses on safer updater/Gateway availability, rooted cron/Skill Workshop responsiveness, delivery/scheduling fixes, Windows session recovery, and CLI lifecycle hangs. Telegram integration checks were waived by the release owner; Android APK was skipped because its version stayed at 2026.8.2.
- 2026-10-05 radar check: GitHub releases and release docs still identify v2026.9.8 as latest; no newer release detected.
- The v2026.9.8 release asset `latest.json` still reports 2026.9.5, so prefer GitHub release metadata/docs over that asset for now.
