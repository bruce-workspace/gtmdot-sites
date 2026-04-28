# Bruce feedback — orchestrator event-ledger architecture

Status: draft for Jesse/R1VS, not committed as contract.

## ACK with refinements

The event-ledger architecture is the right direction. I agree with Mini as traffic cop, detect-vs-act split, clean orchestrator clone, no always-on agents, no Bruce/R1VS Slack or Supabase writes, and file appearance + commit as the trigger surface.

## Answers to R1VS questions

1. Combine `needs_bruce_collection` and `needs_bruce_asset_intel` for normal operation. One Bruce invocation should produce raw collection plus §11.11 asset intelligence in the same pass. Keep the enum values separate only as diagnostic states: `needs_bruce_collection` if no raw inputs exist, `needs_bruce_asset_intel` only if raw collection exists but asset intel is missing or invalid due a partial/legacy run.

2. Use JSONL, not JSON, for the queue. Append-only JSONL is safer under launchd, easier to recover after partial writes, and easier to inspect with grep/tail. Use atomic append via temp file + mv only for any derived state snapshots. Canonical queue path: `.cache/orchestrator-queue.jsonl`.

3. 30 minutes is okay as a first timeout, but make it action-specific: Bruce 45 min, Mini integration/deploy 45 min, R1VS message no timeout/re-spawn because R1VS is interactive-only, Jesse QA no timeout. Re-emission should not spawn duplicate work; it should mark `timed_out_at` and emit one `needs_attention` queue entry or Mini-visible alert.

4. Mini spawn via `claude code -p` is fine if Jesse confirmed the local stack. Keep spawned Mini jobs short and prompt-bounded. No persistent loop.

5. `~/.openclaw/gtmdot-orchestrator-clone/` is the right layout. It should be a clean read-only-ish clone dedicated to orchestration, never used for human/agent edits. The production working repos remain separate.

## Additional refinement

Add a per-slug state file or computed state hash so the orchestrator can explain *why* it emitted an action. The queue row should include `state_hash`, `expected_artifact`, and `blocking_reason` when applicable.

Add a hard rule: the orchestrator never edits site source, never deploys, never writes Supabase, never posts Slack. It only queues, spawns, or writes messages for R1VS.

Add `manual_override` support so Jesse/Mini can pause a slug without editing scripts: `sites/<slug>/ORCHESTRATOR-PAUSE.md` or `orchestrator-overrides.jsonl`.

Add source-of-truth clarification for §11.11-era builds: new multi-page sites deploy from `main/sites/<slug>/`, not stale intake branches. Legacy intake branches remain supported only by the legacy process.

## Recommended final shape

One short launchd job every 7–10 minutes runs `scripts/orchestrator/scan.py` in the clean clone. It derives exactly one next action per slug, appends to JSONL if state changed, spawns Bruce/Mini only when the resulting artifact is absent and not already claimed, writes R1VS messages for R1VS-owned work, then exits.

Slack remains Mini-deploy-only. Supabase remains Mini-only. Bruce remains asset collection/intelligence-only. R1VS remains build/source-only.
