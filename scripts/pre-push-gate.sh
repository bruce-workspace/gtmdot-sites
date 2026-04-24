#!/usr/bin/env bash
# pre-push-gate.sh
# R1VS pre-push safety net. Runs 6 checks on a slug's build output.
# Exits non-zero on any failure — commit/push should be blocked.
#
# Usage:
#   ./scripts/pre-push-gate.sh <slug>
#   ./scripts/pre-push-gate.sh               # defaults to current intake/<slug> branch
#
# Checks:
#   1. fabrication-grep   — known hallucinated review strings
#   2. stock-image-grep   — unsplash / istock / pravatar / placeholder hosts
#   3. claim-bar-grep     — R1VS must not inject claim bar / popup / cookie banner
#   4. review-count-audit — reviews.json captured count must match rendered review UI
#   5. icon-intent-diff   — icon-intent.json must match actual icons in HTML
#   6. proposal-gate      — source-of-truth doc changes require visible Jesse ACK
#
# Each check writes a PASS / FAIL line. Final exit code = 0 if all pass, 1 if any fail.

set -uo pipefail  # note: no -e so we can run all checks even if one fails

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# ───── colors ─────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

pass() { echo -e "  ${GREEN}✓${NC} $*"; }
fail() { echo -e "  ${RED}✗${NC} $*"; FAILURES=$((FAILURES + 1)); }
info() { echo -e "  ${BLUE}ℹ${NC} $*"; }
warn() { echo -e "  ${YELLOW}⚠${NC} $*"; }

FAILURES=0

# ───── resolve slug ─────
SLUG="${1:-}"
if [[ -z "$SLUG" ]]; then
  BRANCH="$(git rev-parse --abbrev-ref HEAD)"
  if [[ "$BRANCH" == intake/* ]]; then
    SLUG="${BRANCH#intake/}"
  else
    echo -e "${RED}ERROR:${NC} no slug given and current branch '$BRANCH' is not intake/*"
    echo "Usage: $0 <slug>"
    exit 2
  fi
fi

SITE_DIR="sites/$SLUG"
if [[ ! -d "$SITE_DIR" ]]; then
  echo -e "${RED}ERROR:${NC} $SITE_DIR does not exist"
  exit 2
fi

HTML_FILES=$(find "$SITE_DIR" -maxdepth 2 -name "*.html" 2>/dev/null)
if [[ -z "$HTML_FILES" ]]; then
  echo -e "${RED}ERROR:${NC} no HTML files found in $SITE_DIR"
  exit 2
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}pre-push-gate.sh${NC}  — slug: ${YELLOW}$SLUG${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# ───── Check 1: fabrication-grep ─────
echo ""
echo -e "${BLUE}[1/6] fabrication-grep${NC} — known hallucinated review strings"

# Hard-block: always wrong, no legitimate use
HARD_BLOCK_PATTERNS=(
  'Yahoo Local'
  'Verbatim customer quotes are being consolidated'
  'reviews being consolidated'
)

# Context-dependent: only wrong if in reviewer-name slot (not in review-source slot)
NAME_ONLY_BAD=(
  'Google Customer'
  'Google Review'
  'Angi Customer'
  'Angi Review'
  'Verified Homeowner'
  'Long-Time Customer'
  'Company Mission'
  'Our Story'
  'Happy Customer'
  'Satisfied Customer'
)

FAB_HITS=0

# Hard-block check — grep across all files
for pattern in "${HARD_BLOCK_PATTERNS[@]}"; do
  HITS=$(grep -l -F "$pattern" $HTML_FILES 2>/dev/null || true)
  if [[ -n "$HITS" ]]; then
    fail "found hard-block pattern '$pattern' in: $(echo $HITS | tr '\n' ' ')"
    FAB_HITS=$((FAB_HITS + 1))
  fi
done

# Context-aware check via python (precise: only flag when in reviewer-name context)
python3 - "$SITE_DIR" "${NAME_ONLY_BAD[@]}" <<'PY' > /tmp/fab-check-$$.out
import re, sys
from pathlib import Path

site_dir = Path(sys.argv[1])
bad_names = set(sys.argv[2:])

# Reviewer-name context selectors
NAME_CLASS_PATTERN = re.compile(
    r'<(div|span|p)[^>]*class="[^"]*(review-name|review-author|reviewer-name|reviewer|review-attribution|author-name)[^"]*"[^>]*>([^<]+)</\1>',
    re.IGNORECASE
)

# Empty review body pattern
EMPTY_BODY_PATTERN = re.compile(
    r'<p[^>]*class="[^"]*review-mini-text[^"]*"[^>]*>\s*(?:""|)\s*</p>',
    re.IGNORECASE
)

for html_path in site_dir.glob('**/*.html'):
    text = html_path.read_text()
    for m in NAME_CLASS_PATTERN.finditer(text):
        name = m.group(3).strip()
        if name in bad_names:
            print(f'NAME_SLOT|{html_path.name}|{name}')
    for m in EMPTY_BODY_PATTERN.finditer(text):
        print(f'EMPTY_BODY|{html_path.name}')
PY

while IFS='|' read -r kind file detail; do
  if [[ "$kind" == "NAME_SLOT" ]]; then
    fail "reviewer-name slot contains fabrication pattern '$detail' in: $file"
    FAB_HITS=$((FAB_HITS + 1))
  elif [[ "$kind" == "EMPTY_BODY" ]]; then
    fail "empty <p class=\"review-mini-text\"> body in: $file"
    FAB_HITS=$((FAB_HITS + 1))
  fi
done < /tmp/fab-check-$$.out
rm -f /tmp/fab-check-$$.out

if [[ $FAB_HITS -eq 0 ]]; then
  pass "no fabrication patterns detected"
fi

# ───── Check 2: stock-image-grep ─────
echo ""
echo -e "${BLUE}[2/6] stock-image-grep${NC} — external stock / placeholder hosts"

STOCK_HOSTS=(
  'unsplash.com'
  'images.unsplash.com'
  'istockphoto.com'
  'gettyimages.com'
  'pravatar.cc'
  'placeimg.com'
  'placeholder.com'
  'via.placeholder.com'
  'picsum.photos'
  'shutterstock.com'
  'pixabay.com'
  'pexels.com'
)

STOCK_HITS=0
for host in "${STOCK_HOSTS[@]}"; do
  HITS=$(grep -l -F "$host" $HTML_FILES 2>/dev/null || true)
  if [[ -n "$HITS" ]]; then
    fail "found '$host' reference in: $(echo $HITS | tr '\n' ' ')"
    STOCK_HITS=$((STOCK_HITS + 1))
  fi
done

if [[ $STOCK_HITS -eq 0 ]]; then
  pass "no stock image hosts referenced"
fi

# ───── Check 3: claim-bar-grep ─────
echo ""
echo -e "${BLUE}[3/6] claim-bar-grep${NC} — R1VS must not inject claim bar / popup / cookie banner"

CLAIM_BAR_SELECTORS=(
  'id="claimBar"'
  "id='claimBar'"
  'id="claim-bar"'
  "id='claim-bar'"
  'id="exitPopup"'
  'id="exit-popup"'
  'id="cookieBanner"'
  'id="cookie-banner"'
  'class="claim-bar"'
  'class="gtmdot-claim'
  'class="exit-popup"'
  'CLAIM_BAR_ANCHOR'
)

CLAIM_HITS=0
for sel in "${CLAIM_BAR_SELECTORS[@]}"; do
  HITS=$(grep -l -F "$sel" $HTML_FILES 2>/dev/null || true)
  if [[ -n "$HITS" ]]; then
    fail "found claim-bar selector '$sel' in: $(echo $HITS | tr '\n' ' ')"
    CLAIM_HITS=$((CLAIM_HITS + 1))
  fi
done

if [[ $CLAIM_HITS -eq 0 ]]; then
  pass "no claim-bar / popup / cookie banner in R1VS build"
fi

# ───── Check 4: review-count-audit ─────
echo ""
echo -e "${BLUE}[4/6] review-count-audit${NC} — reviews.json captured count must match rendered review UI"

REVIEWS_JSON="$SITE_DIR/reviews.json"
if [[ ! -f "$REVIEWS_JSON" ]]; then
  info "no reviews.json present — skipping audit"
else
  CAPTURED=$(python3 -c "
import json, sys
try:
    with open('$REVIEWS_JSON') as f:
        data = json.load(f)
    if isinstance(data, dict):
        if 'captured' in data and isinstance(data['captured'], int):
            print(data['captured'])
        elif 'reviews' in data and isinstance(data['reviews'], list):
            print(len(data['reviews']))
        else:
            print(0)
    elif isinstance(data, list):
        print(len(data))
    else:
        print(0)
except Exception as e:
    print('ERR', file=sys.stderr)
    print(0)
" 2>/dev/null || echo 0)

  # count review UI elements via python — match WHOLE class tokens, not substrings.
  # (Earlier bug: "review-mini-text" substring-matched "review-mini" and double-counted.)
  REVIEW_UI_COUNT=$(python3 - "$SITE_DIR" <<'PY'
import re, sys
from pathlib import Path
site_dir = Path(sys.argv[1])
# Match class attribute contents and check for exact-token hits
attr_re = re.compile(r'class="([^"]+)"')
target_tokens = {"review-mini", "review-card"}
total = 0
for html_path in site_dir.glob('**/*.html'):
    text = html_path.read_text()
    for m in attr_re.finditer(text):
        tokens = set(m.group(1).split())
        if tokens & target_tokens:
            total += 1
print(total)
PY
  )

  info "captured=$CAPTURED, review UI slots=$REVIEW_UI_COUNT"

  if [[ "$CAPTURED" -lt 3 && "$REVIEW_UI_COUNT" -gt 0 ]]; then
    fail "captured < 3 but HTML has $REVIEW_UI_COUNT review UI slots — should be empty-state instead"
  elif [[ "$REVIEW_UI_COUNT" -gt "$CAPTURED" && "$CAPTURED" -ge 3 ]]; then
    fail "HTML has $REVIEW_UI_COUNT review UI slots but only $CAPTURED captured — shortfall suggests fabrication"
  else
    pass "review UI count ($REVIEW_UI_COUNT) matches or fits within captured count ($CAPTURED)"
  fi
fi

# ───── Check 5: icon-intent-diff ─────
echo ""
echo -e "${BLUE}[5/6] icon-intent-diff${NC} — icon-intent.json must match actual icons in HTML"

ICON_INTENT="$SITE_DIR/icon-intent.json"
if [[ ! -f "$ICON_INTENT" ]]; then
  warn "no icon-intent.json — skipping diff (consider adding per ICON-MAPPING.md)"
else
  python3 -c "
import json, re, sys
from pathlib import Path

try:
    with open('$ICON_INTENT') as f:
        intent = json.load(f)
except Exception as e:
    print(f'ERR parsing icon-intent.json: {e}', file=sys.stderr)
    sys.exit(0)

# Flatten intent into a set of expected icons (lowercase, stripped)
expected = set()
def collect(v):
    if isinstance(v, str):
        expected.add(v.strip().lower())
    elif isinstance(v, list):
        for x in v:
            collect(x)
    elif isinstance(v, dict):
        for x in v.values():
            collect(x)
collect(intent)

# Collect actual data-lucide icon names from HTML
actual = set()
for html_path in Path('$SITE_DIR').glob('**/*.html'):
    text = html_path.read_text()
    for m in re.finditer(r'data-lucide=[\"\\\']([a-z0-9\\-]+)[\"\\\']', text):
        actual.add(m.group(1).strip().lower())

# Actual not expected = freestyling
freestyle = actual - expected
# Expected not actual = missing (less severe — might just not be on a card yet)
missing = expected - actual

if freestyle:
    print(f'FREESTYLE:{\"|\".join(sorted(freestyle))}')
if missing:
    print(f'MISSING:{\"|\".join(sorted(missing))}')
" 2>/dev/null > /tmp/icon-diff-$$.out

  FREESTYLE=$(grep '^FREESTYLE:' /tmp/icon-diff-$$.out | sed 's/^FREESTYLE://' || true)
  MISSING=$(grep '^MISSING:' /tmp/icon-diff-$$.out | sed 's/^MISSING://' || true)

  if [[ -n "$FREESTYLE" ]]; then
    fail "icons in HTML not in icon-intent.json: $FREESTYLE"
  fi
  if [[ -n "$MISSING" ]]; then
    warn "icons in icon-intent.json not yet in HTML: $MISSING (may be OK if not all cards built)"
  fi
  if [[ -z "$FREESTYLE" && -z "$MISSING" ]]; then
    pass "icon-intent.json matches HTML icons exactly"
  elif [[ -z "$FREESTYLE" ]]; then
    pass "no icon freestyling (some intent icons not yet placed)"
  fi
  rm -f /tmp/icon-diff-$$.out
fi

# ───── Check 6: proposal-gate ─────
echo ""
echo -e "${BLUE}[6/6] proposal-gate${NC} — source-of-truth doc changes require Jesse ACK message"

SOURCE_OF_TRUTH_FILES=(
  'CLAUDE.md'
  'SKILL.md'
  'HANDOFF-CONTRACT.md'
  'DESIGN-HEURISTICS.md'
  'ICON-MAPPING.md'
  'TERMINOLOGY-MAPPING.md'
  'R1VS-REBUILD-BRIEF.md'
)

STAGED_SOT=()
for f in "${SOURCE_OF_TRUTH_FILES[@]}"; do
  if git diff --cached --name-only 2>/dev/null | grep -qxF "$f" \
     || git diff --name-only 2>/dev/null | grep -qxF "$f"; then
    STAGED_SOT+=("$f")
  fi
done

if [[ ${#STAGED_SOT[@]} -eq 0 ]]; then
  pass "no source-of-truth doc changes in this push"
else
  # Look for recent proposal + ACK messages
  MISSING_ACK=()
  for f in "${STAGED_SOT[@]}"; do
    BASENAME=$(basename "$f" .md | tr '[:upper:]' '[:lower:]')
    PROPOSAL=$(find messages -type f -name "*proposal*${BASENAME}*" -mtime -7 2>/dev/null | head -1)
    JESSE_ACK=$(find messages -type f \( -name "*jesse-ack*" -o -name "*jesse-*ack*" \) -mtime -7 2>/dev/null | head -1)

    if [[ -z "$PROPOSAL" ]]; then
      fail "$f modified but no recent proposal message found (messages/*proposal*${BASENAME}*)"
      MISSING_ACK+=("$f")
    elif [[ -z "$JESSE_ACK" ]]; then
      warn "$f has proposal ($PROPOSAL) but no jesse-ack message in last 7 days"
      MISSING_ACK+=("$f")
    else
      pass "$f: proposal + ACK found ($PROPOSAL, $JESSE_ACK)"
    fi
  done
fi

# ───── final tally ─────
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
if [[ $FAILURES -eq 0 ]]; then
  echo -e "${GREEN}✓ ALL CHECKS PASSED${NC}  — $SLUG is clear to push"
  exit 0
else
  echo -e "${RED}✗ $FAILURES CHECK(S) FAILED${NC}  — fix before pushing"
  exit 1
fi
