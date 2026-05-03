#!/usr/bin/env bash
# =====================================================================
# r1vs-watcher.sh — Stage 1 MVP watcher for R1VS Trade Builder pipeline
# =====================================================================
#
# Polls Supabase r1vs_jobs every 15 minutes (via launchd StartInterval),
# atomically claims the oldest queued job via a Postgres RPC, spawns
# `claude code -p` with the job spec, lets R1VS run Phase 0–3 and update
# the row itself, and exits. Slack-mirrors phase transitions if
# SLACK_WEBHOOK_URL is set.
#
# Designed to be invoked by ~/Library/LaunchAgents/com.gtmdot.r1vs-watcher.plist
# (or manually for testing — `bash scripts/r1vs-watcher.sh`).
#
# Stage 1 only:
#   - launchd + bash + Supabase RPC claim + Slack mirror
#   - NO Paperclip API integration
#   - NO Bruce / Mini automation
#   - NO CRM mutation / deploys / outreach
#   - NO parallel builds (single working tree)
#
# Refs:
#   docs/r1vs-trade-builder-contract.md (commit f7426d8)
#   proposals/2026-04-28-r1vs-watcher-implementation.md (commit d523c87)
#   proposals/2026-04-28-r1vs-jobs-schema-migration.sql (commit 5cf301d)
#
# Prerequisites on R1VS-MacBook:
#   - bash 4+ (Homebrew bash recommended; system bash 3.x may work)
#   - jq installed (`brew install jq`)
#   - curl installed (system default OK)
#   - claude binary in $PATH (Claude Code installed + Jesse signed in)
#   - git working tree at $REPO_DIR (default: ~/GTMDot)
#   - $GTMDOT_DIR/.env populated with SUPABASE_URL + SUPABASE_R1VS_WATCHER_KEY
#
# To pause:    touch $GTMDOT_DIR/r1vs-watcher.pause
# To resume:   rm    $GTMDOT_DIR/r1vs-watcher.pause
# =====================================================================

# Note: deliberately NOT using `set -e` — the watcher should self-recover
# from individual command failures rather than die mid-tick. We use
# `set -u` and explicit error handling instead.

set -u

# ---- Config (overridable via env) ----
GTMDOT_DIR="${GTMDOT_DIR:-$HOME/.gtmdot}"
REPO_DIR="${REPO_DIR:-$HOME/GTMDot}"
LOCK_DIR="$GTMDOT_DIR/r1vs-watcher.lock.d"
PAUSE_FILE="$GTMDOT_DIR/r1vs-watcher.pause"
LOG_DIR="$GTMDOT_DIR/logs"
LOG_FILE="$LOG_DIR/r1vs-watcher-$(date +%Y-%m-%d).log"
CLAIMER="r1vs-macbook-watcher"

# Ensure dirs exist
mkdir -p "$LOG_DIR"

# ---- Logging ----
log() {
  printf "[%s] %s\n" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" >> "$LOG_FILE"
}

slack_post() {
  local msg="$1"
  if [ -n "${SLACK_WEBHOOK_URL:-}" ]; then
    # Use --fail-with-body to surface non-2xx in stderr; suppress success output.
    curl -fSs -X POST -H "Content-Type: application/json" \
      --data "$(jq -n --arg t "$msg" '{text: $t}')" \
      "$SLACK_WEBHOOK_URL" > /dev/null 2>>"$LOG_FILE" || \
      log "WARN: slack post failed (non-blocking)"
  fi
}

# ---- Reconcile-on-exit (always log tick end, release lock) ----
cleanup() {
  rmdir "$LOCK_DIR" 2>/dev/null || true
  log "tick end"
}
trap cleanup EXIT

# ---- 1. Pause check ----
if [ -f "$PAUSE_FILE" ]; then
  log "paused (sentinel present)"
  exit 0
fi

# ---- 2. Atomic single-tick lock (mkdir is portable + atomic on macOS) ----
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  log "tick skipped (lock held — long phase still running from previous tick)"
  exit 0
fi

log "tick start ($CLAIMER)"

# ---- 3. Load env ----
if [ ! -f "$GTMDOT_DIR/.env" ]; then
  log "ERROR: $GTMDOT_DIR/.env not found"
  slack_post ":rotating_light: r1vs-watcher: missing $GTMDOT_DIR/.env — exiting"
  exit 1
fi

# Source the env file (allowing comments + blank lines)
set -a
# shellcheck disable=SC1091
source "$GTMDOT_DIR/.env"
set +a

if [ -z "${SUPABASE_URL:-}" ] || [ -z "${SUPABASE_R1VS_WATCHER_KEY:-}" ]; then
  log "ERROR: SUPABASE_URL or SUPABASE_R1VS_WATCHER_KEY not set in env"
  slack_post ":rotating_light: r1vs-watcher: env incomplete (SUPABASE_URL or SUPABASE_R1VS_WATCHER_KEY missing)"
  exit 1
fi

# ---- 4. Atomic claim via Supabase RPC ----
JOB_JSON=$(curl -fsS -X POST "$SUPABASE_URL/rest/v1/rpc/r1vs_claim_next_job" \
  -H "apikey: $SUPABASE_R1VS_WATCHER_KEY" \
  -H "Authorization: Bearer $SUPABASE_R1VS_WATCHER_KEY" \
  -H "Content-Type: application/json" \
  --data "$(jq -n --arg c "$CLAIMER" '{claimer: $c}')" 2>>"$LOG_FILE")

if [ -z "$JOB_JSON" ]; then
  log "ERROR: claim RPC returned empty — Supabase unreachable?"
  slack_post ":rotating_light: r1vs-watcher: Supabase unreachable on tick"
  exit 1
fi

# ---- 5. Parse claim result ----
SLUG=$(echo "$JOB_JSON" | jq -r '.[0].slug // empty' 2>/dev/null)
if [ -z "$SLUG" ]; then
  log "no queued jobs"
  exit 0
fi

JOB_ID=$(echo "$JOB_JSON" | jq -r '.[0].id')
INPUT_SPEC=$(echo "$JOB_JSON" | jq -c '.[0].input_spec')
log "claimed job: slug=$SLUG id=$JOB_ID"
slack_post ":gear: r1vs-watcher: claimed \`$SLUG\`"

# ---- helper: mark a job blocked + Slack-notify ----
mark_blocked() {
  local status="$1"
  local reason="$2"
  log "marking $JOB_ID as $status — $reason"
  curl -fsS -X PATCH "$SUPABASE_URL/rest/v1/r1vs_jobs?id=eq.$JOB_ID" \
    -H "apikey: $SUPABASE_R1VS_WATCHER_KEY" \
    -H "Authorization: Bearer $SUPABASE_R1VS_WATCHER_KEY" \
    -H "Content-Type: application/json" \
    -H "Prefer: return=minimal" \
    --data "$(jq -n --arg s "$status" --arg r "$reason" \
              '{status: $s, blocked_reason: $r}')" >> "$LOG_FILE" 2>&1 || \
    log "WARN: failed to PATCH blocked status (non-blocking)"
  slack_post ":warning: r1vs-watcher: \`$SLUG\` blocked — $status (\`$reason\`)"
}

# ---- 6. Repo + working tree checks ----
if [ ! -d "$REPO_DIR" ]; then
  mark_blocked "blocked_runner_unavailable" "REPO_DIR ($REPO_DIR) not found"
  exit 1
fi

cd "$REPO_DIR" || {
  mark_blocked "blocked_runner_unavailable" "cd to REPO_DIR failed"
  exit 1
}

# Confirm we're in a git repo
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  mark_blocked "blocked_runner_unavailable" "$REPO_DIR is not a git repo"
  exit 1
fi

# Working tree must be clean — never clobber Jesse's interactive work
if [ -n "$(git status --porcelain)" ]; then
  mark_blocked "blocked_runner_unavailable" "dirty working tree on MacBook"
  exit 1
fi

# Confirm we're on main
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" != "main" ]; then
  mark_blocked "blocked_runner_unavailable" "current branch is $CURRENT_BRANCH, expected main"
  exit 1
fi

# ---- 7. Pull latest ----
if ! git fetch origin main >> "$LOG_FILE" 2>&1; then
  mark_blocked "blocked_runner_unavailable" "git fetch failed"
  exit 1
fi

if ! git reset --hard origin/main >> "$LOG_FILE" 2>&1; then
  mark_blocked "blocked_runner_unavailable" "git reset --hard failed"
  exit 1
fi

# ---- 8. Build the prompt ----
PROMPT="You are R1VS Trade Builder, woken up by the Stage 1 watcher because a job was claimed from the Supabase r1vs_jobs queue.

Job:
  id:    $JOB_ID
  slug:  $SLUG
  input_spec: $INPUT_SPEC

Run Phase 0-3 per docs/r1vs-trade-builder-contract.md. On every phase transition, update the Supabase r1vs_jobs row (id=$JOB_ID) with the new status + commit SHA + relevant artifact paths. The watcher's role is over once you take this prompt — it will not babysit you. You write status to Supabase yourself per phase.

Smoke-test short-circuit: if input_spec._smoke_test is true, write status=phase_0_passed and exit. Do NOT run any actual research or build. Do NOT touch sites/, do NOT spawn WebFetch.

Env vars available to you (inherited from this watcher process):
  SUPABASE_URL                  — project URL
  SUPABASE_R1VS_WATCHER_KEY     — API key for r1vs_watcher Postgres role
  SLACK_WEBHOOK_URL             — optional, post to #claude-sync on phase transitions

NEVER write a service-role JWT into any file or prompt. The r1vs_watcher role is least-privilege by design.

After all phases complete (or a blocking gate is hit), exit cleanly. The watcher's tick will read the final status from Supabase and Slack-mirror it."

# ---- 9. Spawn claude code -p ----
log "spawning claude code -p for $SLUG"
if claude code -p "$PROMPT" >> "$LOG_FILE" 2>&1; then
  EXIT_CODE=0
else
  EXIT_CODE=$?
fi
log "claude exited with code $EXIT_CODE for $SLUG"

# ---- 10. Reconcile final status (R1VS already wrote it; we just observe) ----
FINAL_STATUS=$(curl -fsS "$SUPABASE_URL/rest/v1/r1vs_jobs?id=eq.$JOB_ID&select=status" \
  -H "apikey: $SUPABASE_R1VS_WATCHER_KEY" \
  -H "Authorization: Bearer $SUPABASE_R1VS_WATCHER_KEY" 2>>"$LOG_FILE" \
  | jq -r '.[0].status // "unknown"' 2>/dev/null)

log "final status for $SLUG: $FINAL_STATUS (claude exit=$EXIT_CODE)"

# ---- 11. Slack mirror per terminal state ----
case "$FINAL_STATUS" in
  phase_3_finalized_ready_for_bruce)
    slack_post ":white_check_mark: r1vs-watcher: \`$SLUG\` finalized — Bruce's gate"
    ;;
  phase_0_dq_recommended)
    slack_post ":no_entry: r1vs-watcher: \`$SLUG\` Phase 0 DQ recommended"
    ;;
  phase_0_passed)
    # Smoke-test rows + happy-path Phase 0 both land here when claude exits early
    if [ "$SLUG" = "smoke-test-r1vs-watcher" ]; then
      slack_post ":hourglass: r1vs-watcher: smoke test \`$SLUG\` round-trip OK (claimed → phase_0_passed)"
    else
      slack_post ":hourglass: r1vs-watcher: \`$SLUG\` Phase 0 passed (waiting for next tick to continue)"
    fi
    ;;
  blocked_*)
    slack_post ":warning: r1vs-watcher: \`$SLUG\` ended in $FINAL_STATUS"
    ;;
  unknown)
    slack_post ":rotating_light: r1vs-watcher: \`$SLUG\` final status unreadable from Supabase (claude exit=$EXIT_CODE)"
    ;;
  *)
    log "unrecognized terminal status: $FINAL_STATUS"
    slack_post ":hourglass: r1vs-watcher: \`$SLUG\` tick complete (status=$FINAL_STATUS, exit=$EXIT_CODE)"
    ;;
esac

# Cleanup runs via trap on EXIT
exit 0
