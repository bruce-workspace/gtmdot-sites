# Manual Deploy Procedure — §11.11-era Multi-Page Sites

**Status:** Reference spec, not a script. Captures the exact steps Mini ran for the first §11.11-era manual deploy (forest-park-collision, 2026-04-26).

**Purpose:** When `process-main-site.sh` is built later, the author has a clean reference of what needs to happen instead of reverse-engineering this from message history.

**Why manual:** `process-intake.sh` is single-page-on-intake-branch. §11.11-era sites are multi-page-on-main. The two haven't been reconciled yet — this procedure is the bridge until `process-main-site.sh` lands.

---

## Pre-conditions

- Slug exists in Supabase `prospects` with `claim_code` already assigned
- R1VS has committed multi-page site to `main` of `gtmdot-sites` (NOT to an intake branch)
- Bruce has written `sites/<slug>/bruce-asset-intel.json` + `bruce-collected.md` to `main`
- `sites/<slug>/photos-raw/` and `sites/<slug>/photos-generated/` exist on `main` (Bruce-populated)
- `sites/<slug>/` does NOT yet have a tracked `photos/` directory — Mini creates it during integration

---

## Step-by-step

### 0. Pull latest gtmdot-sites main

```bash
cd /Users/bruce/.openclaw/workspace/gtmdot-sites && git pull origin main
```

### 1. Validate Bruce's asset intelligence (§11.11.7 schema check)

```bash
cd /Users/bruce/.openclaw/workspace/gtmdot-sites
python3 scripts/consume-asset-intel.py <slug>
```

Exit codes:
- `0` — schema valid, hero recommendation surfaced; proceed
- `1` — schema fail OR missing `license_note`; **block deploy**, file a `messages/<date>-mini-to-r1vs-<slug>-bruce-intel-fail.md`
- `2` — `bruce-asset-intel.json` not found; site predates §11.11 — fall back to `process-intake.sh` if appropriate

The script also writes icon-flag messages to `messages/` if Bruce flagged any icon mismatches (§11.11.4 routing).

### 2. Look up claim code + business name from Supabase

```bash
SLUG="<slug>"
SUPABASE_URL="https://qztjoshdrxionhxeieik.supabase.co"
# Load SUPABASE_SERVICE_KEY from brucecom-v3/.env.local
set -a; source /Users/bruce/.openclaw/workspace/brucecom-v3/.env.local; set +a
PROSPECT=$(curl -s "$SUPABASE_URL/rest/v1/prospects?slug=eq.$SLUG&select=claim_code,business_name,stage" \
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY")
CLAIM_CODE=$(echo "$PROSPECT" | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['claim_code'])")
BUSINESS_NAME=$(echo "$PROSPECT" | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['business_name'])")
```

If `claim_code` is empty in Supabase, **stop** — generate manually before proceeding. Pattern: first 4 chars of business_name (uppercase, alphanumeric only) + 4 random digits.

### 3. Backup current deploy target

```bash
DEPLOY="/Users/bruce/.openclaw/workspace/gtmdot/sites/$SLUG"
if [ -d "$DEPLOY" ]; then
  rm -rf "$DEPLOY.bak-pre-§11.11"
  cp -r "$DEPLOY" "$DEPLOY.bak-pre-§11.11"
fi
```

If the previous deploy was the legacy single-page version, this preserves it for rollback if the new deploy regresses.

### 4. Replace deploy target with main's multi-page content

```bash
MAIN_SRC="/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/$SLUG"
rm -rf "$DEPLOY"
mkdir -p "$DEPLOY"
cp "$MAIN_SRC"/*.html "$DEPLOY/"
cp "$MAIN_SRC/_base.css" "$DEPLOY/"
```

**Do NOT copy:** `bruce-asset-intel.{json,md}`, `bruce-collected.md`, `business-data.json`, `collect-request.md`, `gbp_snapshot.json`, `legitimacy-check.json`, `BUILD-STATE.md`, `RESEARCH.md`, `reviews-raw.json`, `icon-intent.json`, `photos-raw/`. These are source-tracking artifacts, not deploy artifacts.

### 5. Integrate photos per §11.11.5 guardrail 6

Mini owns the integration copy from `photos-raw/` + `photos-generated/` into `photos/`. Default-accept Bruce's `photo_quality` labels per §11.11.3.

**Hero (always Bruce's preferred):**
```bash
mkdir -p "$DEPLOY/photos"
HERO_PATH=$(python3 -c "import json; print(json.load(open('$MAIN_SRC/bruce-asset-intel.json'))['hero_recommendation']['preferred_path'])")
cp "$MAIN_SRC/$HERO_PATH" "$DEPLOY/photos/hero.jpg"
```

**Gallery photos (top N proof+hero-candidate by confidence):**
Read `bruce-asset-intel.json` `photo_quality[]`, sort by `confidence` descending, filter to labels `proof-candidate` and `hero-candidate` (skip `gallery-candidate` and `discard` unless N is unmet), copy the top N into `photos/gbp-1.jpg` through `photos/gbp-N.jpg` based on what the HTML expects.

For multi-page sites, count expected slots:
```bash
grep -hoE "photos/gbp-[0-9]+\.jpg" "$DEPLOY"/*.html | sort -u
```

Document the mapping in your deploy commit message so future Mini sessions can reproduce.

### 6. Sanitize + inject claim bar on every HTML page

The shared template at `/Users/bruce/.openclaw/workspace/gtmdot/sites/_shared/claim-ui.html` injects per-page. For multi-page, loop:

```python
import os, re, glob
from pathlib import Path

deploy = "/Users/bruce/.openclaw/workspace/gtmdot/sites/<slug>"
shared_ui = Path("/Users/bruce/.openclaw/workspace/gtmdot/sites/_shared/claim-ui.html").read_text()
template = (shared_ui
    .replace('{{ CLAIM_CODE }}', CLAIM_CODE)
    .replace('{{ BUSINESS_NAME }}', BUSINESS_NAME)
    .replace('{{ PRICE_FIRST_MONTH }}', '$49')
    .replace('{{ PRICE_ONGOING }}', '$149')
    .replace('{{ CHECKOUT_URL }}', f'https://gtmdot.com/checkout?code={CLAIM_CODE}')
    .replace('{{ HOW_IT_WORKS_URL }}', 'https://gtmdot.com/how-it-works'))

# Sanitize patterns to remove from each HTML:
# - mouseleave one-liner exit-intent listeners
# - multi-line mouseleave blocks (balanced-brace removal)
# - window.onbeforeunload assignments
# - cookie auto-show: document.getElementById('cookie').classList.add('active')
# - leaked claim codes (force-replace `code=XXXX` → `code={CLAIM_CODE}`)

# Then inject before </body> (or replace <!-- CLAIM_BAR_ANCHOR --> if present).

for path in sorted(glob.glob(os.path.join(deploy, '*.html'))):
    html = Path(path).read_text()
    # ... apply sanitize regexes ...
    if 'gtmdot-claim-bar' not in html:
        html = html.replace('</body>', template + '\n</body>', 1)
    Path(path).write_text(html)
```

Reference implementation: process-intake.sh step 4 has the exact regex set.

### 7. Verify claim code is registered in checkout system

Three files to check (idempotent — only update if missing):

```bash
GTMDOT_DIR="/Users/bruce/.openclaw/workspace/gtmdot"
grep -c "\"$CLAIM_CODE\"" "$GTMDOT_DIR/sites/gtmdot/codes.json"
grep -c "\"$CLAIM_CODE\"" "$GTMDOT_DIR/sites/gtmdot/_worker.js"
grep -c "\"$CLAIM_CODE\"" "$GTMDOT_DIR/functions/api/lookup-code.js"
```

If any return `0`, run process-intake.sh's step 5 logic to inject alphabetically into all three files.

Live verification:
```bash
curl -s "https://gtmdot.com/api/lookup-code?code=$CLAIM_CODE" | python3 -m json.tool
```

Expected: `{"found": true, "slug": "<slug>", "url": "https://<slug>.pages.dev"}`.

### 8. Pre-deploy gate (CAUTION: multi-page-incompatible)

`scripts/pre-deploy-gate.sh` was written for single-page. **Skip for multi-page sites until the gate is updated** (or add a `--multi-page` flag that loops over all `*.html`).

The §11.11.5 guardrail checks (HARD CHECK 8 + SOFT WARNING 3) only apply to `<img>` tags pointing at `photos-generated/`. For sites where the hero is a CSS `background-image` (like forest-park-collision), no `<img>` references `photos-generated/` and the new checks pass trivially.

The other gate checks (claim bar, cookie, exit-intent, title, claim code, checkout URL) are still valid per-page — but the gate only inspects `index.html`. If multi-page sites have variations across pages, those go unchecked.

**Workaround until the gate is multi-page-aware:** spot-check each HTML manually for the claim bar (`grep gtmdot-claim-bar *.html`).

### 9. Deploy to Cloudflare Pages

```bash
cd /Users/bruce/.openclaw/workspace/gtmdot
npx wrangler pages project create "$SLUG" --production-branch=main 2>&1 | tail -3 || true
npx wrangler pages deploy "sites/$SLUG" --project-name="$SLUG" --commit-dirty=true
```

Expect `Deployment complete!` in the output. Capture the preview URL (`https://<hash>.<slug>.pages.dev`) for your Slack post.

Also redeploy `gtmdot.com` itself if you registered a new claim code:
```bash
npx wrangler pages deploy "sites/gtmdot" --project-name=gtmdot --commit-dirty=true
```

### 10. Update Supabase stage

§11.11-era stages (post-commit `3bd31476` split):
- `needs_enrichment` — Bruce/R1VS owes work (automation lane)
- `needs_decision` — human judgment required (Jesse's standup queue)
- `needs_approval` — clean, awaiting Jesse's approve click

After a clean deploy of a §11.11 site that consumed Bruce's intel: **`needs_enrichment` → `needs_approval`**.

```bash
curl -s -X PATCH "$SUPABASE_URL/rest/v1/prospects?slug=eq.$SLUG" \
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=minimal" \
  -d "{\"stage\":\"needs_approval\",\"preview_site_url\":\"https://$SLUG.pages.dev\"}"
```

### 11. Notification marker (for the intake-pipeline-watcher cron)

```bash
NOTIF_DIR="/Users/bruce/.openclaw/workspace/brucecom-v3/.intake-notifications"
mkdir -p "$NOTIF_DIR"
cat > "$NOTIF_DIR/$SLUG.txt" <<NOTIF
slug=$SLUG
business=$BUSINESS_NAME
claim_code=$CLAIM_CODE
preview_url=https://$SLUG.pages.dev
checkout_url=https://gtmdot.com/checkout?code=$CLAIM_CODE
deployed_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)
photo_count=<N>
hero_source=generated  # or "real" if Bruce recommended a photos-raw/ hero
asset_intel_consumed=true
NOTIF
```

### 12. Slack ping #claude-sync (channel C0AQTKM8F0A)

Include: live URL, preview URL, stage transition, claim code, photo integration summary, any §11.11 notes worth surfacing (e.g. model_stack mismatch). Tag Jesse for QA review.

---

## Things that go wrong and how to recover

**Bruce's asset-intel JSON missing required fields:** `consume-asset-intel.py` exits 1. Don't deploy. File `messages/<date>-mini-to-r1vs-<slug>-bruce-intel-fail.md` with the validation output. Wait for Bruce to regenerate.

**Bruce recommends a generated hero but `gpt-image-2` substituted to MiniMax:** Bruce's `model_stack.image_generation` field will say `"minimax/image-01 via OpenClaw image_generate; requested OpenAI gpt-image-2 class capability"`. The deploy still works but the quality baseline is lower than §11.11.3 default-accept assumed. Surface to Jesse in the Slack ping; he'll decide whether to override.

**Wrangler deploy fails:** Check `npx wrangler pages project list` for the project. Verify `gtmdot/sites/<slug>/` has all the files. Common cause: `_worker.js` syntax error after claim-code injection — diff against `_worker.js.bak`.

**Supabase PATCH returns non-204:** Likely auth — check `SUPABASE_SERVICE_KEY` is loaded. Curl with `-v` to see the response.

**Deploy succeeded but live URL still shows old content:** Cloudflare Pages cache. Wait 30-60s and re-check. Or check for project-name typo.

**Rollback needed:** The `.bak-pre-§11.11/` backup contains the previous deploy. To roll back:
```bash
rm -rf "$DEPLOY"
mv "$DEPLOY.bak-pre-§11.11" "$DEPLOY"
cd /Users/bruce/.openclaw/workspace/gtmdot
npx wrangler pages deploy "sites/$SLUG" --project-name="$SLUG" --commit-dirty=true
```

---

## Open improvements for `process-main-site.sh` (when it gets built)

Things this manual procedure surfaced that the eventual script should handle automatically:

1. **Source-of-truth detection:** check whether `sites/<slug>/` has multi-page artifacts on main (multiple HTMLs) vs single-page on intake. Pick the right source automatically.
2. **Photo integration as a function of `bruce-asset-intel.json`:** read `photo_quality[]`, sort by confidence + label, copy top N into `photos/` according to slot count detected in HTML.
3. **Multi-page claim bar injection:** loop the existing `process-intake.sh` step 4 logic over every `*.html` in the site.
4. **Multi-page-aware pre-deploy gate:** either run `pre-deploy-gate.sh` per-page or add a `--multi-page` flag that loops.
5. **Stage transitions for the §11.11-era split stages:** `needs_enrichment` → `needs_approval` (clean), `needs_enrichment` → `needs_decision` (gate flagged something Jesse should look at).
6. **`model_stack` reporter:** parse Bruce's `model_stack.image_generation` field, flag in Slack if it doesn't match the declared `gpt-image-2` capability.
7. **Idempotency:** running twice on the same slug should be safe (preserve backup, re-deploy without breaking checkout system, no duplicate claim code injection).

---

*Authored 2026-04-26 by Mini after the forest-park-collision Option 1 manual deploy. Update as the procedure evolves until `process-main-site.sh` retires this doc.*
