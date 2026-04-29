#!/usr/bin/env bash
# test-verify-build-clean-urls.sh
# Exercises Check #1 (asset resolution) of verify-build.sh against synthetic
# fixtures covering Cloudflare Pages clean-URL semantics.
#
# Cloudflare Pages strips ".html" automatically: a request for /about returns
# the contents of about.html. Sites that author internal hrefs as clean URLs
# avoid the 308 redirect penalty (/about.html → /about → 200) that adds
# ~100-200ms to every internal click. Check #1 must accept clean URLs as
# valid without loosening the rule for genuinely missing links.
#
# Cases:
#   1. /about + about.html on disk            → Check #1 PASS
#   2. /services + services/index.html        → PASS (directory-style)
#   3. /foo/ (trailing slash) + foo/index.html → PASS
#   4. /widgetz with no widgetz.html or dir   → FAIL (must not loosen rule)
#   5. /about?utm=x and /about#hero           → PASS (query/anchor stripped)
#   6. /                                       → PASS (root → index.html)
#   7. _base.css with file present            → PASS (extensioned literal)
#   8. /missing.css with no file              → FAIL (extensioned, not found)
#
# Usage:
#   ./scripts/tests/test-verify-build-clean-urls.sh
# Exit 0 if all assertions hold, non-zero otherwise.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
GATE="$REPO_ROOT/scripts/verify-build.sh"

TMP="$(mktemp -d -t verify-build-test.XXXXXX)"
trap 'rm -rf "$TMP"' EXIT

# Fake repo root with verify-build.sh symlinked in. The script does
# `cd "$(dirname "${BASH_SOURCE[0]}")/.."` so invoking via the symlink
# resolves REPO_ROOT to the fake root.
FAKE_ROOT="$TMP/repo"
FAKE_GATE="$FAKE_ROOT/scripts/verify-build.sh"
mkdir -p "$FAKE_ROOT/sites" "$FAKE_ROOT/scripts"
ln -s "$GATE" "$FAKE_GATE"

# Each fixture provides an index.html with the hrefs under test plus the
# disk layout the test asserts about. No images, no claim UI, no reviews —
# Checks 2-7 emit warnings or pass trivially, leaving Check #1 isolated.
make_fixture() {
  local slug="$1" index_body="$2"
  shift 2
  local d="$FAKE_ROOT/sites/$slug"
  mkdir -p "$d"
  cat > "$d/index.html" <<HTML
<!doctype html>
<html><body>
$index_body
</body></html>
HTML
  # Optional extra files / nested htmls passed as KEY=VAL pairs:
  #   "about.html=<html>about</html>"
  #   "services/index.html=<html>services</html>"
  while [[ $# -gt 0 ]]; do
    local kv="$1"; shift
    local k="${kv%%=*}" v="${kv#*=}"
    mkdir -p "$d/$(dirname "$k")"
    printf '%s\n' "$v" > "$d/$k"
  done
}

run_gate() {
  local slug="$1"
  ( cd "$FAKE_ROOT" && bash "$FAKE_GATE" "$slug" 2>&1 )
}

PASS=0
FAIL=0

assert_check1() {
  local label="$1" output="$2" expect="$3"  # expect: pass|fail
  local check1
  check1="$(printf '%s\n' "$output" \
            | awk '/\[1\/7\] asset resolution/{flag=1;next} flag && /\[2\/7\]/{flag=0} flag')"

  local got=""
  if echo "$check1" | grep -q '✗'; then
    got="fail"
  elif echo "$check1" | grep -q '✓'; then
    got="pass"
  else
    got="unknown"
  fi

  if [[ "$got" == "$expect" ]]; then
    echo "  PASS  $label  (Check #1 = $got)"
    PASS=$((PASS + 1))
  else
    echo "  FAIL  $label  (expected $expect, got $got)"
    echo "----- Check #1 output -----"
    echo "$check1"
    echo "----- end -----"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== test-verify-build-clean-urls.sh ==="

# Case 1: /about + about.html on disk → PASS
make_fixture "case1-about" '<a href="/about">About</a>' \
  'about.html=<!doctype html><html><body>about</body></html>'
out="$(run_gate "case1-about")"
assert_check1 "1. /about resolves to about.html" "$out" "pass"

# Case 2: /services + services/index.html on disk → PASS
make_fixture "case2-services-dir" '<a href="/services">Services</a>' \
  'services/index.html=<!doctype html><html><body>services</body></html>'
out="$(run_gate "case2-services-dir")"
assert_check1 "2. /services resolves to services/index.html" "$out" "pass"

# Case 3: /foo/ trailing slash + foo/index.html → PASS
make_fixture "case3-trailing-slash" '<a href="/foo/">Foo</a>' \
  'foo/index.html=<!doctype html><html><body>foo</body></html>'
out="$(run_gate "case3-trailing-slash")"
assert_check1 "3. /foo/ trailing slash resolves to foo/index.html" "$out" "pass"

# Case 4: /widgetz with NO matching file or dir → FAIL (must stay strict)
make_fixture "case4-genuinely-broken" '<a href="/widgetz">Widgetz</a>'
out="$(run_gate "case4-genuinely-broken")"
assert_check1 "4. /widgetz with no widgetz.html or widgetz/ → still broken" "$out" "fail"

# Case 5: query + anchor on a clean URL still resolves
make_fixture "case5-query-anchor" \
  '<a href="/about?utm=x">A</a><a href="/about#hero">B</a>' \
  'about.html=<!doctype html><html><body>about</body></html>'
out="$(run_gate "case5-query-anchor")"
assert_check1 "5. /about?utm=x and /about#hero strip and resolve" "$out" "pass"

# Case 6: root '/' → index.html
make_fixture "case6-root" '<a href="/">Home</a>'
out="$(run_gate "case6-root")"
assert_check1 "6. / resolves to index.html" "$out" "pass"

# Case 7: extensioned literal _base.css present → PASS (regression guard)
make_fixture "case7-css-present" '<link rel="stylesheet" href="_base.css">' \
  '_base.css=body{}'
out="$(run_gate "case7-css-present")"
assert_check1 "7. _base.css literal still resolves" "$out" "pass"

# Case 8: extensioned literal missing.css absent → FAIL (regression guard)
make_fixture "case8-css-missing" '<link rel="stylesheet" href="/missing.css">'
out="$(run_gate "case8-css-missing")"
assert_check1 "8. /missing.css with no file on disk → still broken" "$out" "fail"

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
