# MCP Setup — GTMDot

Which MCP servers and API keys this repo's skills depend on, and how to install them on a fresh MacBook or re-verify on an existing one.

---

## What we need and why

| Tool | Purpose | Used by |
|---|---|---|
| **Chrome DevTools MCP** | Drives a headless Chrome browser, runs Lighthouse, snapshots DOM, takes screenshots | `stale-site-identifier` skill (Group C scan) |
| **Firecrawl MCP** | Scrapes websites, pulls sitemaps, detects WordPress spam injection | `stale-site-identifier` + existing Group B workflow |
| **Google Maps / Places API key** | Business discovery, ratings, reviews, photos, Place IDs | All three groups (A, B, C) |

The skill files (`skills/stale-site-identifier/*.md`) assume all three are available. Without them, the skill falls back to browser-only workarounds that skip Lighthouse scoring.

---

## Install / verify steps (run in Terminal.app)

Once these are run at `--scope user`, every Claude Code session on this MacBook has them — no per-project reinstall.

### 1. Chrome DevTools MCP (no API key required)

```bash
claude mcp add --scope user chrome-devtools -- npx chrome-devtools-mcp@latest
```

Verify:
```bash
claude mcp list | grep chrome-devtools
# should show: chrome-devtools: npx chrome-devtools-mcp@latest - ✓ Connected
```

### 2. Firecrawl MCP (requires API key)

Get the key from Dashlane (entry: "Firecrawl API"). Then:

```bash
claude mcp add --scope user firecrawl --env FIRECRAWL_API_KEY=YOUR_KEY_HERE -- npx -y firecrawl-mcp
```

Verify:
```bash
claude mcp list | grep firecrawl
# should show: firecrawl: npx -y firecrawl-mcp - ✓ Connected
```

Free tier is fine for MVP-scale scanning (~500 credits/month). Bump to paid if you scale past ~10 verticals/month.

### 3. Google Maps / Places API key

Not an MCP — just an env var used by `curl` calls in Bash. Get the key from Dashlane (entry: "Google Maps / Places API"). Then:

```bash
echo 'GOOGLE_MAPS_API_KEY=YOUR_KEY_HERE' >> ~/.openclaw/.env
```

Verify:
```bash
grep GOOGLE_MAPS_API_KEY ~/.openclaw/.env | sed 's/=.*/=***REDACTED***/'
# should print: GOOGLE_MAPS_API_KEY=***REDACTED***
```

Sanity-check the key works (replace `YOUR_KEY_HERE` with actual value when running):
```bash
curl -s "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=HVAC%20Atlanta&inputtype=textquery&fields=place_id,name&key=$(grep GOOGLE_MAPS_API_KEY ~/.openclaw/.env | cut -d= -f2)" | head -c 200
# should return JSON with a place_id, not an error
```

---

## After install

**Close any running Claude Code session and start a fresh one.** MCP servers load at session start, so existing sessions don't pick up new additions until relaunched.

**Test that everything works** by running the stale-site-identifier skill's dry-run mode against a single URL outside the Atlanta prospect pool. See `skills/stale-site-identifier/SKILL.md` → "Dry-Run Mode" for the invocation pattern.

---

## Troubleshooting

**`chrome-devtools-mcp` won't connect.** Make sure Chrome is installed at the standard path (`/Applications/Google Chrome.app`). If using Arc or Brave, the package needs extra config — flag to Claude at runtime.

**`firecrawl-mcp` returns 401.** Key is wrong or expired. Re-check Dashlane and re-run the install command with the correct key (it'll overwrite the previous entry).

**`claude mcp list` shows `Failed to connect` for something.** Run with more detail:
```bash
claude mcp get <name>
```
Typically means the server crashed or the npm package isn't installable. Try removing + reinstalling.

**Google Places `REQUEST_DENIED`.** The API key isn't enabled for Places API in Google Cloud Console. Go to GCP → APIs & Services → Library → enable "Places API" on the project.

---

## Security notes

- API keys are in `~/.openclaw/.env` (permissions `-rw-------`, owner only). Do NOT commit this file — it's gitignored.
- MCP configs live in `~/.claude.json`. Also do not commit.
- Firecrawl + Google Maps keys cost real money if abused. Set usage alerts in both dashboards.
- If a key leaks: rotate immediately in the respective dashboard, update Dashlane, re-run the install commands.

---

## Related files

- `skills/stale-site-identifier/SKILL.md` — main orchestrator that uses all three tools
- `skills/stale-site-identifier/staleness-score.md` — rubric that requires Lighthouse (Chrome DevTools) for full accuracy
- `SKILL.md` (root) — existing Group A/B workflow, also uses Firecrawl + Places
