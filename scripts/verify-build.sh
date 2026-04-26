#!/usr/bin/env bash
# verify-build.sh
# R1VS post-build verification. Proves the build actually works before declaring done. Runs 7 checks.
#
# Usage:
#   ./scripts/verify-build.sh <slug>                    # local file-tree mode
#   ./scripts/verify-build.sh <slug> --live <url>       # fetch deployed URL and verify
#
# Checks:
#   1. every <img src=>, <link href=>, <a href=> resolves (no 404s, no broken relative paths)
#   2. reviews.json "captured" count matches count of rendered review UI elements
#   3. claim code in HTML is a plausible code (matches pattern if expected; flags mismatches)
#   4. no stock image hosts referenced
#   5. no fabrication patterns (calls pre-push-gate.sh under the hood)
#   6. hero image exists at referenced path (catches broken-hero pattern Mini flagged)
#   7. generated-image proportion <= 30% per §11.11.5 guardrail 5
#
# Exit 0 on full pass, 1 on any failure.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

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
SLUG="${1:-}"
MODE="local"
LIVE_URL=""

if [[ -z "$SLUG" ]]; then
  echo "Usage: $0 <slug> [--live <url>]"
  exit 2
fi
shift

while [[ $# -gt 0 ]]; do
  case "$1" in
    --live)
      MODE="live"
      LIVE_URL="${2:-}"
      shift 2
      ;;
    *)
      echo "Unknown option: $1"
      exit 2
      ;;
  esac
done

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
echo -e "${BLUE}verify-build.sh${NC}  — slug: ${YELLOW}$SLUG${NC}  — mode: ${YELLOW}$MODE${NC}"
if [[ "$MODE" == "live" ]]; then
  echo -e "${BLUE}━━━━━━${NC}  live URL: ${YELLOW}$LIVE_URL${NC}"
fi
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# ───── Check 1: asset resolution ─────
echo ""
echo -e "${BLUE}[1/7] asset resolution${NC} — every src/href must resolve"

python3 - "$SITE_DIR" "$MODE" "$LIVE_URL" <<'PY' > /tmp/verify-assets-$$.out
import re, sys, os
from pathlib import Path

site_dir = Path(sys.argv[1])
mode = sys.argv[2]
live_url = sys.argv[3] if len(sys.argv) > 3 else ''

broken = []
slot_held = []   # photos/ files that don't exist but are legitimate slots in local mode
checked = 0

for html_path in site_dir.glob('**/*.html'):
    text = html_path.read_text()
    # extract src="..." and href="..."
    for attr in ('src', 'href'):
        for m in re.finditer(rf'{attr}=["\']([^"\'#]+)["\']', text):
            url = m.group(1).strip()
            if not url or url.startswith('#') or url.startswith('javascript:') or url.startswith('mailto:') or url.startswith('tel:'):
                continue
            # data URIs are inline, always "resolve"
            if url.startswith('data:'):
                continue
            # external URLs — skip in local mode
            if url.startswith('http://') or url.startswith('https://'):
                # only flag stock hosts here (dedicated check elsewhere)
                continue
            # relative URL — check file exists
            checked += 1
            # strip query string / anchor
            clean = url.split('?')[0].split('#')[0]
            rel = Path(clean.lstrip('/'))
            candidates = [
                html_path.parent / rel,
                site_dir / rel,
            ]
            if not any(c.exists() for c in candidates):
                # In LOCAL mode: photos/* slots are legitimately empty until Master Site
                # Builder fills them post-handoff. Track separately; don't fail.
                if mode == 'local' and clean.startswith('photos/'):
                    slot_held.append(f'{html_path.name}: {url}')
                else:
                    broken.append(f'{html_path.name}: {url}')

print(f'CHECKED:{checked}')
print(f'SLOT_HELD:{len(slot_held)}')
for b in broken:
    print(f'BROKEN:{b}')
for s in slot_held:
    print(f'HELD:{s}')
PY

CHECKED=$(grep '^CHECKED:' /tmp/verify-assets-$$.out | sed 's/^CHECKED://' | head -1)
CHECKED="${CHECKED:-0}"
SLOT_HELD=$(grep '^SLOT_HELD:' /tmp/verify-assets-$$.out | sed 's/^SLOT_HELD://' | head -1)
SLOT_HELD="${SLOT_HELD:-0}"
BROKEN_COUNT=$(grep -c '^BROKEN:' /tmp/verify-assets-$$.out 2>/dev/null | head -1)
BROKEN_COUNT="${BROKEN_COUNT:-0}"

if [[ "$BROKEN_COUNT" == "0" ]]; then
  if [[ "$SLOT_HELD" != "0" ]]; then
    pass "all $CHECKED relative assets resolve ($SLOT_HELD photos/ slots held open for Master Site Builder — OK in local mode)"
  else
    pass "all $CHECKED relative assets resolve"
  fi
else
  fail "$BROKEN_COUNT broken asset(s) out of $CHECKED checked:"
  grep '^BROKEN:' /tmp/verify-assets-$$.out | sed 's/^BROKEN:/    /' | head -20
fi
rm -f /tmp/verify-assets-$$.out

# ───── Check 2: reviews.json vs review UI ─────
echo ""
echo -e "${BLUE}[2/7] reviews.json vs review UI${NC} — captured count must match rendered count"

REVIEWS_JSON="$SITE_DIR/reviews.json"
if [[ ! -f "$REVIEWS_JSON" ]]; then
  warn "no reviews.json present — skipping"
else
  CAPTURED=$(python3 -c "
import json
try:
    with open('$REVIEWS_JSON') as f:
        data = json.load(f)
    if isinstance(data, dict):
        print(data.get('captured', len(data.get('reviews', []))))
    elif isinstance(data, list):
        print(len(data))
    else:
        print(0)
except Exception:
    print(0)
" 2>/dev/null || echo 0)

  # count rendered review UI — match whole class tokens, not substrings.
  # (Earlier bug: "review-mini-text" double-counted against "review-mini".)
  REVIEW_UI=$(python3 - "$SITE_DIR" <<'PY'
import re, sys
from pathlib import Path
site_dir = Path(sys.argv[1])
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

  info "reviews.json captured=$CAPTURED, HTML review UI slots=$REVIEW_UI"

  if [[ "$CAPTURED" -lt 3 && "$REVIEW_UI" -gt 0 ]]; then
    fail "captured < 3 but HTML has $REVIEW_UI review UI slots (fabrication risk)"
  elif [[ "$REVIEW_UI" -gt "$CAPTURED" ]]; then
    fail "HTML has $REVIEW_UI slots but only $CAPTURED captured (shortfall = fabrication risk)"
  else
    pass "review UI count matches captured count"
  fi
fi

# ───── Check 3: claim code presence + pattern ─────
echo ""
echo -e "${BLUE}[3/7] claim code${NC} — present in HTML, plausible pattern, single value"

# Claim codes in GTMDot follow pattern: 3-7 uppercase letters + 3-4 digits (e.g., RSWPL847, POSH3847)
# Extract unique codes via python for reliability
CLAIM_CODES=$(python3 - "$SITE_DIR" <<'PY'
import re, sys
from pathlib import Path
site_dir = Path(sys.argv[1])
# Look for claim codes only in a claim-code context (URL or attribute).
# Using a simple delimiter char class: space, equals, quotes, colon, slash, end-of-attr.
context_pattern = re.compile(
    r'(?:claim_?code|CLAIM_?CODE|code=|\?code=)[^A-Za-z0-9]{0,4}([A-Z]{3,7}[0-9]{3,4})',
    re.IGNORECASE
)
found = set()
for html_path in site_dir.glob('**/*.html'):
    text = html_path.read_text()
    for m in context_pattern.finditer(text):
        found.add(m.group(1))
for code in sorted(found):
    print(code)
PY
)

CODE_COUNT=$(echo "$CLAIM_CODES" | grep -c '^[A-Z]' 2>/dev/null || true)
CODE_COUNT="${CODE_COUNT:-0}"

if [[ "$CODE_COUNT" == "0" ]]; then
  warn "no claim code found in HTML (OK if Mini injects at deploy time)"
elif [[ "$CODE_COUNT" == "1" ]]; then
  CODE=$(echo "$CLAIM_CODES" | head -1)
  pass "single consistent claim code in HTML: $CODE"
else
  fail "multiple distinct claim codes in HTML — only one should be present:"
  echo "$CLAIM_CODES" | sed 's/^/    /'
fi

# ───── Check 4: stock image hosts ─────
echo ""
echo -e "${BLUE}[4/7] stock image hosts${NC} — no external stock / placeholder"

STOCK_HOSTS=(unsplash.com images.unsplash.com istockphoto.com gettyimages.com pravatar.cc placeimg.com placeholder.com via.placeholder.com picsum.photos shutterstock.com pixabay.com pexels.com)
STOCK_HITS=0
for host in "${STOCK_HOSTS[@]}"; do
  HITS=$(grep -l -F "$host" $HTML_FILES 2>/dev/null || true)
  if [[ -n "$HITS" ]]; then
    fail "'$host' found in: $(echo $HITS | tr '\n' ' ')"
    STOCK_HITS=$((STOCK_HITS + 1))
  fi
done
if [[ $STOCK_HITS -eq 0 ]]; then
  pass "no stock hosts referenced"
fi

# ───── Check 5: fabrication patterns ─────
echo ""
echo -e "${BLUE}[5/7] fabrication patterns${NC} — no known hallucination strings"

# Hard-block: always wrong (Yahoo Local shut down in 2017; placeholder copy is always wrong)
HARD_BLOCK=(
  'Yahoo Local'
  'Verbatim customer quotes are being consolidated'
  'reviews being consolidated'
)

# Context-aware: only flag when in reviewer-name slot (not review-source)
NAME_ONLY_BAD=('Google Customer' 'Google Review' 'Angi Customer' 'Angi Review' 'Verified Homeowner' 'Long-Time Customer' 'Company Mission' 'Our Story' 'Happy Customer' 'Satisfied Customer')

FAB_HITS=0
for pattern in "${HARD_BLOCK[@]}"; do
  HITS=$(grep -l -F "$pattern" $HTML_FILES 2>/dev/null || true)
  if [[ -n "$HITS" ]]; then
    fail "hard-block '$pattern' found in: $(echo $HITS | tr '\n' ' ')"
    FAB_HITS=$((FAB_HITS + 1))
  fi
done

python3 - "$SITE_DIR" "${NAME_ONLY_BAD[@]}" <<'PY' > /tmp/verify-fab-$$.out
import re, sys
from pathlib import Path
site_dir = Path(sys.argv[1])
bad = set(sys.argv[2:])
name_pat = re.compile(r'<(div|span|p)[^>]*class="[^"]*(review-name|review-author|reviewer-name|reviewer|review-attribution|author-name)[^"]*"[^>]*>([^<]+)</\1>', re.IGNORECASE)
empty_pat = re.compile(r'<p[^>]*class="[^"]*review-mini-text[^"]*"[^>]*>\s*(?:""|)\s*</p>', re.IGNORECASE)
for html_path in site_dir.glob('**/*.html'):
    t = html_path.read_text()
    for m in name_pat.finditer(t):
        name = m.group(3).strip()
        if name in bad:
            print(f'NAME|{html_path.name}|{name}')
    for m in empty_pat.finditer(t):
        print(f'EMPTY|{html_path.name}')
PY
while IFS='|' read -r kind file detail; do
  [[ -z "$kind" ]] && continue
  if [[ "$kind" == "NAME" ]]; then
    fail "reviewer-name slot has '$detail' in: $file"
    FAB_HITS=$((FAB_HITS + 1))
  elif [[ "$kind" == "EMPTY" ]]; then
    fail "empty review-mini-text body in: $file"
    FAB_HITS=$((FAB_HITS + 1))
  fi
done < /tmp/verify-fab-$$.out
rm -f /tmp/verify-fab-$$.out

if [[ $FAB_HITS -eq 0 ]]; then
  pass "no fabrication patterns"
fi

# ───── Check 6: hero image exists ─────
echo ""
echo -e "${BLUE}[6/7] hero image${NC} — referenced hero must exist at path"

HERO_PATHS=()
for html in $HTML_FILES; do
  # Find hero image references — common patterns
  HEROES=$(grep -oE '(src|href|content)="[^"]*hero[^"]*\.(jpg|jpeg|png|webp|avif)"' "$html" 2>/dev/null | sed -E 's/^[^"]*"([^"]+)".*/\1/' | sort -u || true)
  while IFS= read -r h; do
    [[ -n "$h" ]] && HERO_PATHS+=("$h")
  done <<< "$HEROES"
done

UNIQUE_HEROES=$(printf '%s\n' "${HERO_PATHS[@]:-}" | sort -u | grep -v '^$' || true)

if [[ -z "$UNIQUE_HEROES" ]]; then
  warn "no hero image reference found in HTML (OK if hero is a section background only)"
else
  BAD_HEROES=0
  HELD_HEROES=0
  while IFS= read -r h; do
    [[ -z "$h" ]] && continue
    [[ "$h" =~ ^https?:// ]] && continue  # external, skip
    clean=$(echo "$h" | sed 's/[?#].*//')
    rel="${clean#/}"
    if [[ ! -f "$SITE_DIR/$rel" ]] && [[ ! -f "$rel" ]]; then
      # In local mode: photos/ hero is a slot for Master Site Builder; not a failure.
      if [[ "$MODE" == "local" && "$clean" == photos/* ]]; then
        HELD_HEROES=$((HELD_HEROES + 1))
      else
        fail "hero image referenced but not found: $h"
        BAD_HEROES=$((BAD_HEROES + 1))
      fi
    fi
  done <<< "$UNIQUE_HEROES"
  if [[ $BAD_HEROES -eq 0 ]]; then
    HERO_COUNT=$(echo "$UNIQUE_HEROES" | grep -c '^' || echo 0)
    if [[ $HELD_HEROES -gt 0 ]]; then
      pass "$HERO_COUNT hero reference(s) — $HELD_HEROES held for Master Site Builder (local mode OK)"
    else
      pass "$HERO_COUNT hero image(s) resolve"
    fi
  fi
fi

# ───── Check 7: generated-image proportion (§11.11.5 guardrail 5) ─────
echo ""
echo -e "${BLUE}[7/7] generated-image proportion${NC} — §11.11.5 guardrail 5: <=30% generated"

GEN_PROPORTION_OUT=$(python3 - "$SITE_DIR" <<'PY'
import re, sys
from pathlib import Path

site_dir = Path(sys.argv[1])

# Match <img ...> tags
IMG_RE = re.compile(r'<img\b([^>]*)/?>', re.IGNORECASE | re.DOTALL)
ATTR_RE = re.compile(r'(\w[\w-]*)\s*=\s*"([^"]*)"')

total_imgs = 0
generated_imgs = 0

for html_path in site_dir.glob('**/*.html'):
    text = html_path.read_text()
    for img_match in IMG_RE.finditer(text):
        attrs_text = img_match.group(1)
        attrs = dict((m.group(1).lower(), m.group(2)) for m in ATTR_RE.finditer(attrs_text))
        # Skip imgs with no src (e.g., open template slot still empty)
        if not attrs.get('src'):
            continue
        total_imgs += 1
        if attrs.get('data-source', '').strip().lower() == 'generated':
            generated_imgs += 1
        # Also count imgs whose src points at photos-generated/ regardless of attribute
        elif 'photos-generated/' in (attrs.get('src') or ''):
            generated_imgs += 1

if total_imgs == 0:
    print("TOTAL:0")
    print("GENERATED:0")
    print("PCT:0")
else:
    pct = (generated_imgs / total_imgs) * 100
    print(f"TOTAL:{total_imgs}")
    print(f"GENERATED:{generated_imgs}")
    print(f"PCT:{pct:.1f}")
PY
)

GEN_TOTAL=$(echo "$GEN_PROPORTION_OUT" | grep '^TOTAL:' | sed 's/^TOTAL://' | head -1)
GEN_GEN=$(echo "$GEN_PROPORTION_OUT" | grep '^GENERATED:' | sed 's/^GENERATED://' | head -1)
GEN_PCT=$(echo "$GEN_PROPORTION_OUT" | grep '^PCT:' | sed 's/^PCT://' | head -1)
GEN_TOTAL="${GEN_TOTAL:-0}"
GEN_GEN="${GEN_GEN:-0}"
GEN_PCT="${GEN_PCT:-0}"

info "total <img> with src: $GEN_TOTAL — generated: $GEN_GEN ($GEN_PCT%)"

# Compare GEN_PCT to 30 — use python because bash can't do float comparison reliably
OVER=$(python3 -c "print(1 if float('$GEN_PCT') > 30.0 else 0)")
if [[ "$OVER" == "1" ]]; then
  fail "generated-image proportion $GEN_PCT% exceeds 30% cap (§11.11.5 guardrail 5). Reduce generated count or get Jesse approval per §11.11.7 generated_cap_exception_recommended field."
else
  pass "generated-image proportion within 30% cap"
fi

# ───── optional: live URL check ─────
if [[ "$MODE" == "live" && -n "$LIVE_URL" ]]; then
  echo ""
  echo -e "${BLUE}[live]${NC} HEAD check on deployed URL"
  if command -v curl >/dev/null; then
    HTTP_CODE=$(curl -sI -o /dev/null -w '%{http_code}' "$LIVE_URL")
    if [[ "$HTTP_CODE" == "200" ]]; then
      pass "live URL returns 200: $LIVE_URL"
    else
      fail "live URL returned HTTP $HTTP_CODE: $LIVE_URL"
    fi
  else
    warn "curl not available — skipping live check"
  fi
fi

# ───── final tally ─────
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
if [[ $FAILURES -eq 0 ]]; then
  echo -e "${GREEN}✓ BUILD VERIFIED${NC}  — $SLUG ready to mark complete"
  exit 0
else
  echo -e "${RED}✗ $FAILURES CHECK(S) FAILED${NC}  — do NOT mark build complete"
  exit 1
fi
