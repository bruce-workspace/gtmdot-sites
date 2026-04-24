#!/usr/bin/env bash
#
# retroactive-legitimacy-audit.sh
#
# Runs legitimacy-screen.py against every prospect in a given Supabase stage
# (default: ready_for_review) and produces a summary report. This is a
# RETROACTIVE audit — doesn't mutate prospect stage, doesn't write notes.
# Just produces a report for Jesse to use in DQ decisions.
#
# Per R1VS's pilot finalization doc recommendation.
#
# Usage:
#   ./scripts/retroactive-legitimacy-audit.sh                      # default: ready_for_review
#   ./scripts/retroactive-legitimacy-audit.sh --stage outreach_sent
#   ./scripts/retroactive-legitimacy-audit.sh --output /tmp/audit.md
#
# Output: markdown table of passes + DQ'd prospects with per-prospect reasons.

set -eu

STAGE="ready_for_review"
OUTPUT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --stage) STAGE="$2"; shift 2;;
    --output) OUTPUT="$2"; shift 2;;
    *) echo "Unknown arg: $1" >&2; exit 2;;
  esac
done

# Load env
set -a
source "$HOME/.openclaw/.env"
set +a

SUPABASE_KEY="${SUPABASE_SERVICE_ROLE_KEY:-${SUPABASE_SERVICE_KEY:-}}"
SUPABASE_URL="${SUPABASE_URL:-https://qztjoshdrxionhxeieik.supabase.co}"

if [ -z "$SUPABASE_KEY" ]; then
  echo "error: missing SUPABASE_SERVICE_ROLE_KEY" >&2
  exit 2
fi

if [ -z "${GOOGLE_MAPS_API_KEY:-${GOOGLE_PLACES_API_KEY:-}}" ]; then
  echo "error: missing GOOGLE_MAPS_API_KEY or GOOGLE_PLACES_API_KEY" >&2
  exit 2
fi

REPO="/Users/bruce/.openclaw/workspace/gtmdot-sites"
SCRIPT="$REPO/scripts/legitimacy-screen.py"

if [ ! -x "$SCRIPT" ]; then
  echo "error: $SCRIPT not executable" >&2
  exit 2
fi

# Fetch prospects in target stage
prospects=$(
  curl -s -G \
    "$SUPABASE_URL/rest/v1/prospects" \
    --data-urlencode "select=id,slug,business_name,address,city,state,zip,trade_category" \
    --data-urlencode "stage=eq.$STAGE" \
    --data-urlencode "disqualified=eq.false" \
    --data-urlencode "order=created_at.asc" \
    -H "apikey: $SUPABASE_KEY" \
    -H "Authorization: Bearer $SUPABASE_KEY"
)

count=$(echo "$prospects" | python3 -c "import json,sys;print(len(json.load(sys.stdin)))")
echo "Auditing $count prospects in stage='$STAGE'..." >&2
echo "" >&2

# Temp file for writing report
tmp_report="$(mktemp)"
trap "rm -f $tmp_report" EXIT

{
  echo "# Retroactive Legitimacy Audit — $(date -u +"%Y-%m-%d %H:%M UTC")"
  echo ""
  echo "**Stage:** \`$STAGE\`  |  **Prospects:** $count"
  echo ""
  echo "Per R1VS's pilot finalization recommendation. Runs \`legitimacy-screen.py\`"
  echo "retroactively against the current queue to surface prospects that would"
  echo "have been auto-DQ'd at Phase 0 under the new rules. Does NOT mutate"
  echo "prospect stage or write Supabase notes."
  echo ""
  echo "## Rules applied"
  echo "- \`rating < 4.5\` → DQ (thin rep)"
  echo "- \`total_reviews < 10\` → DQ (insufficient signal)"
  echo "- \`>50% reviews in any 30-day window\` → DQ (farm pattern)"
  echo "- no GBP at claimed address → DQ (ghost listing)"
  echo "- latest review > 24 months old → DQ (dormant)"
  echo "- vertical in blocklist → DQ"
  echo ""
  echo "## Results"
  echo ""
  echo "| Slug | Status | Reasons |"
  echo "|---|---|---|"
} > "$tmp_report"

pass_count=0
dq_count=0
error_count=0

echo "$prospects" | python3 -c "
import json, sys
rows = json.load(sys.stdin)
for r in rows:
    slug = r.get('slug', '')
    name = r.get('business_name', '')
    addr_parts = [r.get('address'), r.get('city'), r.get('state'), r.get('zip')]
    addr = ', '.join(x for x in addr_parts if x)
    vertical = r.get('trade_category', '')
    print(f'{slug}|{name}|{addr}|{vertical}')
" | while IFS='|' read -r slug name addr vertical; do
  [ -z "$slug" ] && continue

  # Skip if no address (can't do places lookup)
  if [ -z "$addr" ]; then
    echo "| \`$slug\` | ⚠ skip | no address in DB |" >> "$tmp_report"
    error_count=$((error_count + 1))
    continue
  fi

  # Create site dir if needed (legitimacy-screen writes into it)
  mkdir -p "$REPO/sites/$slug"

  # Run the screen
  set +e
  output=$("$SCRIPT" "$slug" --places-api --name "$name" --address "$addr" ${vertical:+--vertical "$vertical"} 2>&1)
  exit_code=$?
  set -e

  # Parse
  if [ "$exit_code" -eq 0 ]; then
    pass_count=$((pass_count + 1))
    echo "| \`$slug\` | ✅ PASS | — |" >> "$tmp_report"
  elif [ "$exit_code" -eq 1 ]; then
    dq_count=$((dq_count + 1))
    # Extract reasons from legitimacy-check.json if written
    reasons=""
    if [ -f "$REPO/sites/$slug/legitimacy-check.json" ]; then
      reasons=$(python3 -c "
import json
try:
    d=json.load(open('$REPO/sites/$slug/legitimacy-check.json'))
    rs=d.get('reasons', [])
    print('; '.join(str(x) for x in rs) if rs else 'unknown')
except Exception as e:
    print(f'parse-error: {e}')
")
    else
      reasons="no legitimacy-check.json written"
    fi
    echo "| \`$slug\` | ❌ DQ | $reasons |" >> "$tmp_report"
  else
    error_count=$((error_count + 1))
    # capture first line of error
    first_err=$(echo "$output" | head -1 | tr -d '|' | tr '\n' ' ')
    echo "| \`$slug\` | ⚠ error | $first_err |" >> "$tmp_report"
  fi
  echo "  $slug ($exit_code)" >&2
done

# Append summary
{
  echo ""
  echo "## Summary"
  echo ""
  # Re-count from the tmp_report (the subshell counters didn't propagate)
  passes=$(grep -c '✅ PASS' "$tmp_report" || echo 0)
  dqs=$(grep -c '❌ DQ' "$tmp_report" || echo 0)
  errors=$(grep -c '⚠' "$tmp_report" || echo 0)
  total=$((passes + dqs + errors))
  echo "- Total audited: $total"
  echo "- Passed (ship-ready per new rules): $passes"
  echo "- Would auto-DQ (fails Phase 0 gate): $dqs"
  echo "- Skipped / errored: $errors"
  echo ""
  echo "## Recommended Jesse actions"
  echo ""
  echo "- Review the **DQ** rows above. For each, decide: accept the auto-DQ (move to \`dead\`) or override-and-keep (add to needs_decision stage once #6 ships)."
  echo "- Review the **error** rows (missing address, Places API failures) — these need intake data repair, not DQ."
  echo "- The **PASS** rows are the clean queue. If you combine these with the flag-cleared sites from brief 04, that's the real \`needs_approval\` inbox."
  echo ""
  echo "*Generated by \`scripts/retroactive-legitimacy-audit.sh\`. Reruns safe/idempotent — no side effects on prospects table.*"
} >> "$tmp_report"

# Output
if [ -n "$OUTPUT" ]; then
  cp "$tmp_report" "$OUTPUT"
  echo "" >&2
  echo "Report written to: $OUTPUT" >&2
else
  cat "$tmp_report"
fi
