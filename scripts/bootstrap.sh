#!/usr/bin/env bash
# bootstrap.sh
# R1VS session-start state reconciliation. Replaces hand-written resume briefs.
#
# Run this as the first thing in a new session to understand:
#   - What's new on main since we last synced
#   - What messages are waiting for R1VS attention
#   - What sites are in-flight (have BUILD-STATE.md with unchecked boxes)
#   - What pending contract proposals exist
#
# Usage:
#   ./scripts/bootstrap.sh                  # last 48h window (default)
#   ./scripts/bootstrap.sh --hours 24       # shorter window
#   ./scripts/bootstrap.sh --since <date>   # explicit date (ISO 8601)

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# default: 48h window
HOURS=48
SINCE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --hours) HOURS="$2"; shift 2 ;;
    --since) SINCE="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 2 ;;
  esac
done

if [[ -z "$SINCE" ]]; then
  # derive a git --since argument from HOURS
  if date -u -v-"${HOURS}"H +'%Y-%m-%dT%H:%M:%SZ' >/dev/null 2>&1; then
    # BSD date (macOS)
    SINCE=$(date -u -v-"${HOURS}"H +'%Y-%m-%dT%H:%M:%SZ')
  else
    # GNU date
    SINCE=$(date -u -d "${HOURS} hours ago" +'%Y-%m-%dT%H:%M:%SZ')
  fi
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}bootstrap.sh${NC} — R1VS session state as of $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "Window: last ${YELLOW}${HOURS}${NC} hours (since ${YELLOW}${SINCE}${NC})"

# ───── git sync ─────
echo ""
echo -e "${CYAN}[1/5] git sync${NC}"
LOCAL_HEAD=$(git rev-parse HEAD 2>/dev/null || echo "?")
git fetch origin main --quiet 2>&1
REMOTE_HEAD=$(git rev-parse origin/main 2>/dev/null || echo "?")

if [[ "$LOCAL_HEAD" == "$REMOTE_HEAD" ]]; then
  echo -e "  ${GREEN}✓${NC} local main in sync with origin/main ($LOCAL_HEAD)"
else
  BEHIND=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo "?")
  AHEAD=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "?")
  echo -e "  ${YELLOW}⚠${NC} local: $LOCAL_HEAD"
  echo -e "  ${YELLOW}⚠${NC} remote: $REMOTE_HEAD"
  echo -e "  ${YELLOW}⚠${NC} behind by $BEHIND, ahead by $AHEAD — run: git pull --rebase origin main"
fi

# ───── new messages ─────
echo ""
echo -e "${CYAN}[2/5] new messages in last ${HOURS}h${NC}"

# Find messages newer than the window, grouped by sender
MSG_COUNT=$(find messages -type f -name "*.md" -newermt "$SINCE" 2>/dev/null | wc -l | tr -d ' ')

if [[ "$MSG_COUNT" == "0" ]]; then
  echo -e "  ${BLUE}ℹ${NC} no new messages"
else
  echo -e "  ${BLUE}ℹ${NC} $MSG_COUNT new message(s)"
  # Group by sender (mini, bruce, r1vs, jesse)
  for sender in mini bruce r1vs jesse; do
    SENDER_MSGS=$(find messages -type f -name "*.md" -newermt "$SINCE" 2>/dev/null \
      | xargs -I {} basename {} \
      | grep -i "$sender" \
      | grep -v "bruce-status-no-work" \
      | sort -r \
      | head -8)
    if [[ -n "$SENDER_MSGS" ]]; then
      echo ""
      echo -e "  ${YELLOW}${sender}${NC}:"
      echo "$SENDER_MSGS" | sed 's/^/    /'
    fi
  done

  # Bruce no-work noise count (suppressed above, shown as number)
  NO_WORK_COUNT=$(find messages -type f -name "*.md" -newermt "$SINCE" 2>/dev/null \
    | xargs -I {} basename {} \
    | grep -c "bruce-status-no-work" || true)
  if [[ "${NO_WORK_COUNT:-0}" != "0" ]]; then
    echo ""
    echo -e "  ${YELLOW}bruce-no-work${NC}: $NO_WORK_COUNT heartbeat(s) (suppressed — see Mini's finding #13)"
  fi
fi

# ───── in-flight sites ─────
echo ""
echo -e "${CYAN}[3/5] in-flight sites (BUILD-STATE.md with unchecked boxes)${NC}"

INFLIGHT=$(find sites -maxdepth 2 -name "BUILD-STATE.md" 2>/dev/null)
if [[ -z "$INFLIGHT" ]]; then
  echo -e "  ${BLUE}ℹ${NC} no BUILD-STATE.md files found"
else
  for state_file in $INFLIGHT; do
    slug=$(basename "$(dirname "$state_file")")
    UNCHECKED=$(grep -c '^\s*- \[ \]' "$state_file" 2>/dev/null || echo 0)
    CHECKED=$(grep -c '^\s*- \[x\]' "$state_file" 2>/dev/null || echo 0)
    UNCHECKED="${UNCHECKED:-0}"
    CHECKED="${CHECKED:-0}"
    TOTAL=$((UNCHECKED + CHECKED))
    if [[ "$UNCHECKED" != "0" ]]; then
      NEXT_STEP=$(grep -m1 '^\s*- \[ \]' "$state_file" | sed 's/^\s*- \[ \]\s*//')
      echo -e "  ${YELLOW}${slug}${NC}: $CHECKED/$TOTAL complete — next: $NEXT_STEP"
    else
      echo -e "  ${GREEN}${slug}${NC}: all $TOTAL steps checked ✓"
    fi
  done
fi

# ───── pending proposals ─────
echo ""
echo -e "${CYAN}[4/5] pending contract proposals (proposal messages without matching ACK)${NC}"

PROPOSALS=$(find messages -type f -name "*proposal*" -mtime -14 2>/dev/null | sort)
if [[ -z "$PROPOSALS" ]]; then
  echo -e "  ${BLUE}ℹ${NC} no proposals in last 14 days"
else
  UNRESOLVED=0
  for prop in $PROPOSALS; do
    PROP_BASE=$(basename "$prop" .md)
    # Extract the topic from filename (e.g., 'proposal-skill-restructure' → 'skill-restructure')
    TOPIC=$(echo "$PROP_BASE" | sed 's/.*proposal[_-]//' | sed 's/^-//')
    # Look for ACK message newer than the proposal
    PROP_DATE=$(date -r "$prop" -u +%s 2>/dev/null || echo 0)
    ACK_FOUND=""
    for ack in $(find messages -type f \( -name "*jesse-ack*" -o -name "*jesse*ack*" -o -name "*ack*jesse*" \) -mtime -14 2>/dev/null); do
      ACK_DATE=$(date -r "$ack" -u +%s 2>/dev/null || echo 0)
      if [[ "$ACK_DATE" -gt "$PROP_DATE" ]] && basename "$ack" | grep -qi "$(echo $TOPIC | head -c 10)"; then
        ACK_FOUND="$ack"
        break
      fi
    done
    if [[ -z "$ACK_FOUND" ]]; then
      echo -e "  ${RED}⚠${NC} unresolved: $(basename $prop)"
      UNRESOLVED=$((UNRESOLVED + 1))
    fi
  done
  if [[ "$UNRESOLVED" == "0" ]]; then
    echo -e "  ${GREEN}✓${NC} all recent proposals have matching ACK messages"
  fi
fi

# ───── git state summary ─────
echo ""
echo -e "${CYAN}[5/5] git state${NC}"

BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo -e "  ${BLUE}ℹ${NC} current branch: ${YELLOW}${BRANCH}${NC}"

MODIFIED=$(git status --short 2>/dev/null | grep -c '^.M' || true)
UNTRACKED=$(git status --short 2>/dev/null | grep -c '^??' || true)
STAGED=$(git status --short 2>/dev/null | grep -c '^M' || true)
MODIFIED="${MODIFIED:-0}"
UNTRACKED="${UNTRACKED:-0}"
STAGED="${STAGED:-0}"

if [[ "$MODIFIED" == "0" && "$UNTRACKED" == "0" && "$STAGED" == "0" ]]; then
  echo -e "  ${GREEN}✓${NC} working tree clean"
else
  [[ "$STAGED" != "0" ]]    && echo -e "  ${YELLOW}⚠${NC} $STAGED staged file(s) — ready to commit"
  [[ "$MODIFIED" != "0" ]]  && echo -e "  ${YELLOW}⚠${NC} $MODIFIED modified but unstaged file(s)"
  [[ "$UNTRACKED" != "0" ]] && echo -e "  ${YELLOW}⚠${NC} $UNTRACKED untracked file(s) (most likely .claude/ worktree junk — safe to ignore)"
fi

# Local intake branches not on remote
LOCAL_INTAKE=$(git branch | grep 'intake/' | sed -E 's/^[* ]+//' || true)
if [[ -n "$LOCAL_INTAKE" ]]; then
  echo ""
  echo -e "  ${BLUE}ℹ${NC} local intake branches:"
  while IFS= read -r b; do
    [[ -z "$b" ]] && continue
    REMOTE_EXISTS=$(git ls-remote --heads origin "$b" 2>/dev/null | wc -l | tr -d ' ')
    if [[ "$REMOTE_EXISTS" == "0" ]]; then
      echo -e "    ${YELLOW}${b}${NC} (local only — not on origin)"
    fi
  done <<< "$LOCAL_INTAKE"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}bootstrap complete${NC} — ready for work"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
