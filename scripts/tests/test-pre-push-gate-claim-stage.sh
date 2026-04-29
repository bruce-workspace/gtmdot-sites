#!/usr/bin/env bash
# test-pre-push-gate-claim-stage.sh
# Exercises Check #3 (claim-bar-grep) of pre-push-gate.sh against synthetic
# fixtures covering the four stage states.
#
# Cases:
#   1. STAGE.txt missing             → fail-closed (r1vs-build rules)
#                                       claim UI present → Check #3 FAIL
#   2. STAGE.txt = r1vs-build        → claim UI present → Check #3 FAIL
#   3. STAGE.txt = mini-final-qa     → claim UI present → Check #3 PASS
#                                       claim UI absent  → Check #3 FAIL
#                                       (catches missed-injection bug)
#   4. STAGE.txt = bogus-value       → fail-closed (r1vs-build rules)
#
# This test only asserts on Check #3's result line. It does not require the
# rest of the gate to pass — fixtures are minimal HTML and skip irrelevant
# checks via missing optional inputs.
#
# Usage:
#   ./scripts/tests/test-pre-push-gate-claim-stage.sh
# Exit 0 if all assertions hold, non-zero otherwise.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
GATE="$REPO_ROOT/scripts/pre-push-gate.sh"

TMP="$(mktemp -d -t pre-push-gate-test.XXXXXX)"
trap 'rm -rf "$TMP"' EXIT

# Stand up a fake repo root and symlink the gate script in. We must invoke
# the gate via the symlink path so its internal REPO_ROOT resolves to the
# fake root (the script does `cd "$(dirname "${BASH_SOURCE[0]}")/.."`).
FAKE_ROOT="$TMP/repo"
FAKE_GATE="$FAKE_ROOT/scripts/pre-push-gate.sh"
mkdir -p "$FAKE_ROOT/sites" "$FAKE_ROOT/scripts" "$FAKE_ROOT/messages"
ln -s "$GATE" "$FAKE_GATE"

# Minimal HTML body: legitimate review block (so Check #4 doesn't trip),
# plus optional claim UI. No icons, no images.
make_site() {
  local slug="$1" stage_value="$2" with_claim="$3"
  local d="$FAKE_ROOT/sites/$slug"
  mkdir -p "$d"
  if [[ "$stage_value" != "__none__" ]]; then
    printf '%s\n' "$stage_value" > "$d/STAGE.txt"
  fi
  # Two captured reviews (matches review UI slots; keeps Check #4 quiet)
  cat > "$d/reviews.json" <<JSON
{"captured": 2, "reviews": [{"name":"A","text":"good"},{"name":"B","text":"great"}]}
JSON
  local claim_block=""
  if [[ "$with_claim" == "yes" ]]; then
    claim_block='<div class="gtmdot-claim-bar" id="claimBar">claim</div>'
  fi
  cat > "$d/index.html" <<HTML
<!doctype html>
<html><body>
$claim_block
<div class="review-card"><span class="review-name">Real Person</span><p>good work</p></div>
<div class="review-card"><span class="review-name">Other Person</span><p>great</p></div>
</body></html>
HTML
}

run_gate() {
  local slug="$1"
  ( cd "$FAKE_ROOT" && bash "$FAKE_GATE" "$slug" 2>&1 )
}

PASS=0
FAIL=0

assert_check3() {
  local label="$1" output="$2" expect="$3"  # expect: pass|fail
  local check3
  check3="$(printf '%s\n' "$output" \
            | awk '/\[3\/7\] claim-bar-grep/{flag=1;next} flag && /\[4\/7\]/{flag=0} flag')"

  local got=""
  if echo "$check3" | grep -q '✗'; then
    got="fail"
  elif echo "$check3" | grep -q '✓'; then
    got="pass"
  else
    got="unknown"
  fi

  if [[ "$got" == "$expect" ]]; then
    echo "  PASS  $label  (Check #3 = $got)"
    PASS=$((PASS + 1))
  else
    echo "  FAIL  $label  (expected $expect, got $got)"
    echo "----- Check #3 output -----"
    echo "$check3"
    echo "----- end -----"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== test-pre-push-gate-claim-stage.sh ==="

# Case 1: missing STAGE.txt + claim UI → fail-closed (r1vs rules) → FAIL
make_site "case1-missing-with-claim" "__none__" "yes"
out="$(run_gate "case1-missing-with-claim")"
assert_check3 "1. missing STAGE.txt + claim UI present" "$out" "fail"

# Case 2a: r1vs-build + claim UI → FAIL
make_site "case2a-r1vs-with-claim" "r1vs-build" "yes"
out="$(run_gate "case2a-r1vs-with-claim")"
assert_check3 "2a. STAGE=r1vs-build + claim UI present" "$out" "fail"

# Case 2b: r1vs-build, no claim UI → PASS
make_site "case2b-r1vs-no-claim" "r1vs-build" "no"
out="$(run_gate "case2b-r1vs-no-claim")"
assert_check3 "2b. STAGE=r1vs-build, no claim UI" "$out" "pass"

# Case 3a: mini-final-qa + claim UI → PASS
make_site "case3a-final-qa-with-claim" "mini-final-qa" "yes"
out="$(run_gate "case3a-final-qa-with-claim")"
assert_check3 "3a. STAGE=mini-final-qa + claim UI present" "$out" "pass"

# Case 3b: mini-final-qa + no claim UI → FAIL (missed-injection inverse)
make_site "case3b-final-qa-no-claim" "mini-final-qa" "no"
out="$(run_gate "case3b-final-qa-no-claim")"
assert_check3 "3b. STAGE=mini-final-qa, no claim UI (missed injection)" "$out" "fail"

# Case 3c: outreach-staged + claim UI → PASS
make_site "case3c-outreach-staged" "outreach-staged" "yes"
out="$(run_gate "case3c-outreach-staged")"
assert_check3 "3c. STAGE=outreach-staged + claim UI present" "$out" "pass"

# Case 4: bogus stage value → fail-closed (r1vs rules) → claim UI present → FAIL
make_site "case4-bogus" "totally-made-up" "yes"
out="$(run_gate "case4-bogus")"
assert_check3 "4. STAGE=bogus value + claim UI present (fail-closed)" "$out" "fail"

echo ""
echo "=== summary ==="
echo "  passed: $PASS"
echo "  failed: $FAIL"
if [[ $FAIL -eq 0 ]]; then
  echo "OK"
  exit 0
else
  echo "FAIL"
  exit 1
fi
