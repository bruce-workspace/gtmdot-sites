---
from: mini
to: codex
date: 2026-05-15
type: handoff
subject: Full execution-lane handoff — Mini → Codex
---

# Execution-Lane Handoff: Mini → Codex

This doc transfers ownership of GTMDot execution work from Mini Claude
(this Mac mini session) to Codex. Jesse's decision is driven by the
recent OpenClaw update tightening your direct integration with Bruce,
plus the Codex-for-mobile launch — both of which make the
Mini-as-middleware layer unnecessary.

Read top-to-bottom once; then sections 2–4 are the day-to-day reference.

---

## 1. New lane boundaries (post-handoff)

| Role | Owns |
|---|---|
| **Codex (you)** | All execution: site file edits, photos/ integration, screenshots, CDN sync, postcard prep/send via Poplar, email prep/send via Resend, deploys, live verification, claim-code sync, the outreach-preflight skill. Also still owns: routing, Paperclip, CRM stage decisions, Bruce/OpenClaw diagnostics. Effectively: coordination + execution in one. |
| **Bruce** | Enrichment only — scraping, GBP/Yelp/socials, generated imagery (gpt-image-2 heroes), reviews, asset intelligence. Delivers to `photos-generated/`, `photos-raw/`, `bruce-collected.md`, `bruce-asset-intel.*`. Never touches `photos/`, deploy source, screenshots, CDN, CRM, or live verification. |
| **R1VS** | New-site scaffolding only. R1VS sets up template/layout at site creation. Once a site exists, finishing work flows to Bruce + Codex. R1VS is offline during weekends per Jesse's token tier — don't expect availability outside scaffold-creation windows. |
| **Mini (me)** | Standing down to read-only / on-call. Will not initiate execution. Available if you hit something only I'd remember. |
| **Jesse** | Approves sends, makes business calls (4.0★ override, duplicate decisions, send-now-vs-hold), drives via Codex-mobile from anywhere. |

---

## 2. Current prospect state (verified 2026-05-15)

47 active prospects across the pipeline. Don't trust older docs — this is fresh.

### outreach_sent (13) — already mailed/emailed 2026-05-13

| Slug | Email? | Open flags | Notes |
|---|---|---|---|
| affordable-concrete-repair | Y | 1 | Site uses postcard hero as hero-bg correctly. Open flag may be post-send cleanup. |
| atl-mobile-mechanics | N | 6 | **POST-SEND WIRING TODO:** Bruce delivered 4 GBP reviews in commit `402f304` (`bruce-collected.md`, `bruce-asset-intel.*`, `messages/2026-05-13-bruce-reviews-delivered-atl-mobile-mechanics.md`). HTML still shows "More customer reviews loading" placeholder. Wire Bruce's reviews into the live site so Joseph (owner) lands on real reviews when he clicks through. |
| atlanta-drywall-1 | N | 0 | hero-bg correct. Clean. |
| atlanta-pro-repairs | Y | 3 | **Orphan-hero site** — postcard hero exists at `/photos/hero.jpg` on the deploy but no CSS uses it. Hero section is gradient-only. See "Critical open items" below. |
| done-right-drywall | N | 2 | Orphan-hero (same as above). Plus older flags about claim-bar pricing — verify those got cleaned up in last week's $99→$149 sweep. |
| golden-choice-prowash | Y | 1 | **PROPERLY FIXED** — site hero was a bathroom interior; I downloaded live, swapped hero, redeployed (commit history in `gtmdot-postcards.pages.dev` and prospect Pages project). Hero now shows the cinematic pressure-washing image. Other recent flag may be unrelated. |
| locksmith-atlanta-pro | Y | 1 | hero-bg correct. |
| membrenos-pro-home-repair | Y | 2 | Promoted from qa_approved during Jesse's overnight send 2026-05-13. |
| moonstone-pressure-washing | Y | 1 | Same — promoted + sent overnight. |
| morales-landscape-construction | Y | 1 | Orphan-hero. |
| perez-pools-llc | Y | 0 | hero-bg correct. |
| roberts-mobile-services | N | 1 | hero-bg correct. |
| tech-on-the-way | Y | 0 | hero-bg correct. |

### outreach_staged (2) — ready or needing fix before Jesse triggers send

**harrison-sons-electrical** (claim: HARR2423, postcard-only — no email)
- Jesse 2026-05-13: "looks good, keep in outreach stage / awaiting Jesse send trigger"
- Known issues per `bruce` notes:
  - `[qa-loop]` site uses Unsplash stock image — brand rule violation per `project_photo_icon_blocker_v2`
  - `[qa-loop]` missing `gtmdot-claim-popup` modal (only has claim-bar)
- Jesse already cleared these as not-blocking-send. Postcard ships clean (doesn't carry testimonials); email is intentionally not configured for this prospect.
- **Codex action**: none until Jesse explicitly triggers `submit_postcard`. Hold in outreach_staged.

**the-appliance-gals** (claim: RUVO7205, postcard + email both approved)
- Jesse 2026-05-13: NEEDS_MINI_FIX before send. The hero rendering on the website was missing.
- **Two parts to the fix — Codex needs to decide on Part B before executing:**

  **Part A — wire postcard hero into site hero (instructed by Codex 2026-05-13):**
  - Site CSS for `.hero` is currently gradient-only. No `background-image`.
  - Add a `.hero-bg` element and CSS `background-image:url('photos/hero.jpg')` rule
  - Verify desktop + mobile render with hero visible
  - This is a site-file edit. Pattern to copy: `affordable-concrete-repair` or `locksmith-atlanta-pro` — both use hero-bg CSS correctly.

  **Part B — gallery pollution (FTC/§11.11.5 risk, surfaced in my 2026-05-13 incident report):**
  - The site's "Real Jobs from Atlanta Kitchens" gallery has `<img src="photos/hero.jpg" alt="The Appliance Gals — stainless Frigidaire Gallery gas range serviced in an Atlanta customer kitchen with blue cabinets">`
  - I swapped `photos/hero.jpg` with the synthetic gpt-image-2 postcard hero on 2026-05-12. So now the gallery shows a synthetic image captioned as a real customer kitchen photo. **Violates the postcard hero's `intended_slot_context` (`never proof/team/real-job/owner-portrait/real-customer/before-after`).**
  - Three options to resolve:
    - **b1**: Edit the gallery `<img src>` to point at a different already-collected photo (e.g., `gbp-1.jpg`) and update the caption/alt to match what that image actually shows. Mini-lane, ~5 min.
    - **b2**: Remove that gallery item entirely. Simplest, no risk, loses one slot.
    - **b3**: Bruce-lane: file a `review-scrape`-style request for Bruce to source a real Frigidaire/customer-kitchen photo from `photos-raw/` or a fresh GBP scrape. Then Codex wires the new file in.

- **Execution order**:
  1. Decide b1/b2/b3 first (don't run Part A without resolving Part B, because Part A makes the synthetic image MORE prominent if Part B is unresolved)
  2. Execute Part B
  3. Execute Part A
  4. Redeploy prospect site, re-capture screenshots, redeploy postcard CDN
  5. Re-run outreach-preflight
  6. Mark ready for Jesse's send

### qa_approved (7) — pre-flighted, ready to promote when queue refill needed

| Slug | Email? | Open flags | Notes |
|---|---|---|---|
| cityboys | Y | 2 | Open flag: "DUPLICATE POSTCARD: Two Poplar orders submitted on 4/8" — verify with Poplar before re-sending. |
| dream-steam | N | 1 | |
| handy-dandy-atlanta | N | 2 | |
| intire-mobile-tire-shop | Y | 0 | |
| sandy-springs-plumbing | Y | 0 | **Missing address (`has_address: false`)** — verify before promotion. Postcard impossible without address; email can still go. |
| smartwire-solutions | N | 0 | Note slug drift: lookup-code.js had `smart-wire-solutions` for `SMAR1182`; I synced to Supabase truth `smartwire-solutions` on 2026-05-12. Verify the live deploy still works. |
| tuckers-home-services | Y | 1 | |

Per Jesse's pattern: promote in small batches (3-5 at a time) when staged queue runs low.

### needs_approval (11) — Jesse eye-review queue

Jesse moves these to `qa_approved` by clicking Approve in the CRM. The `approve_site` action no longer has the open-flag hard block (I removed that gate in commit `071f7133` in `brucecom-v3`).

Quick read on each (most are just awaiting Jesse's spot-check):

| Slug | Email? | Notable |
|---|---|---|
| 24-hrs-mobile-tire-services | N | |
| bravo-plumbing-solutions | N | |
| browning-electrical-services | N | site notes flagged "Business may not still be live" |
| chrissy-s-mobile-detailing | Y | |
| forest-park-collision | N | **No address, no phone** — research gap |
| piedmont-tires | N | 1 flag |
| pine-peach-painting | N | **No address, no phone** — research gap |
| raiden-electrical | N | Note: there's another Raiden Electric in Ohio (different) |
| rooter-pro-plumbing-drain | N | |
| thermys-mobile-tire-and-brakes | N | 2 flags — claim bar pricing + hero extraction |
| tuxedo-mechanical-plumbing | Y | 1 flag |

### needs_decision (3) — Jesse calls

| Slug | The decision |
|---|---|
| atlanta-expert-appliance | Audit found photo gallery issues (duplicates + 3 unrelated). Open: keep or kill. |
| pro-gutter-cleaning | Hero extraction failed; weak prospect. Open: continue or disqualify. |
| total-repair-service | **No address** (`has_address: false`) — postcard impossible. Email-only or hold. |

### needs_enrichment (9) — Bruce's lane

These need data from Bruce before they can progress. None should require my involvement.

| Slug | Status |
|---|---|
| azer-pool | |
| hvac-guyz-plumbing-inc | |
| jack-glass-electric | **No address** — research gap |
| plugged-electricians-atl | Y email. Gallery anti-pattern + photos swapped |
| plumbingpro-north-atlanta | Missing popup + pravatar placeholders |
| premier-tv-mounting-atl | Pre-outreach hero block + form issue |
| professional-gutter-cleaning | Y email. Hero swapped |
| sumptuous-mobile-detailing | Y email. Claim code mismatch — verify lookup-code.js is synced |
| trushyne-mobile-detailing | Claim code mismatch + missing pricing + iStockPhoto hero |

### research (2) — earliest in pipeline

| Slug | |
|---|---|
| landscape-addict | |
| mbanugo-tires | |

Jesse said these belong in a fresh research session, not in dispatcher work.

---

## 3. Critical open items (urgent first)

### 3.1 The-Appliance-Gals (BLOCKED on Codex's Part B decision)

See section 2 above for the full Part A + Part B breakdown. This is the only outreach_staged prospect that needs Mini-lane work before Jesse can send. **Recommend doing Part B as b1 (rename gallery img src to gbp-1.jpg and update caption/alt) — quickest, no Bruce dependency, removes FTC risk.**

### 3.2 ATL Mobile Mechanics review wiring (post-send finishing)

Bruce delivered 4 real GBP reviews to:
- `gtmdot-sites/sites/atl-mobile-mechanics/bruce-collected.md`
- `gtmdot-sites/sites/atl-mobile-mechanics/bruce-asset-intel.json` and `.md`
- `gtmdot-sites/messages/2026-05-13-bruce-reviews-delivered-atl-mobile-mechanics.md`

The live site at `atl-mobile-mechanics.pages.dev` still has the "More customer reviews loading" placeholder. Wire Bruce's deliverables into the HTML so Joseph (the owner) lands on real reviews when he clicks through from his postcard (already mailed 2026-05-13).

**Codex action**: edit the site's `index.html` to replace the placeholder testimonials section with the 4 reviews from Bruce. Use names as Bruce captured them (no fabricated attribution like "Atlanta Metro Customer"). Redeploy. Re-capture screenshots if you want a clean state.

### 3.3 Six orphan-hero sites

Sites with the synthetic gpt-image-2 hero deployed to `/photos/hero.jpg` but with **no CSS or HTML that uses it**. Hero section is gradient-only in the site template.

- atlanta-pro-repairs
- atl-mobile-mechanics
- done-right-drywall
- golden-choice-prowash (NOT orphan after my 2026-05-13 fix — this should now be hero-bg correct, verify before changing)
- harrison-sons-electrical
- morales-landscape-construction

**Decision needed**: per Jesse's stated intent ("postcard hero should also be the site hero"), these need a site-template change to add a `.hero-bg` element + CSS rule. That's either:
- **R1VS lane** if it's a scaffold-level template change (preferred if R1VS is available)
- **Codex direct edit per site** if you're treating it as one-off site finishing

All six are already in outreach_sent, so this is post-send finishing, not blocking. Prospects who click through from postcards land on gradient-only hero sections — visual mismatch from the postcard, but not broken.

### 3.4 Stripe Dashboard verification (open since 2026-05-12)

Lives in the **separate gtmdot.com session** (which Jesse migrated to Opus 4.7 on 2026-05-12). Not your direct lane, but worth knowing about:
- Code says `$149/mo` everywhere now (10 spots fixed, commit `9fd1cf9d`)
- Live Stripe Payment Link `28E3cv9WJ44Xg5tfOd00006` may still be configured at `$99/mo` internally
- Real money at stake — needs Jesse to verify in Stripe Dashboard
- Handoff doc for that session: `gtmdot/HANDOFF-FROM-MINI-2026-05-12.md`

### 3.5 Lane drift in collect-requests (process fix)

Bruce's cron prompt update (proposed by Codex 2026-05-13) auto-routes by the `type:` frontmatter field. Verify it's actually deployed. If not, Bruce may still try to process Mini-lane requests filed in error. The relevant taxonomy:

**Bruce-lane types**: `image-generation`, `image-regen`, `hero-regen`, `postcard-hero-regen`, `review-scrape`, `email-research`, `photo-brief`, `asset-intel`, `enrichment`, `gbp-scrape`

**Codex-lane types** (no longer Mini-lane post-handoff): `site-hero-swap`, `site-deploy`, `pages-redeploy`, `screenshot`, `screenshot-regen`, `cdn`, `live-verification`

Bruce only archives Codex-lane requests if a Codex completion marker is present (either `messages/YYYY-MM-DD-codex-completed-<slug>.md` or `## RESOLUTION` block in the request file with timestamp).

---

## 4. Institutional knowledge / footguns

Hard-won lessons. Don't repeat my mistakes.

### 4.1 The wrangler-deploy-from-which-dir footgun (gtmdot.com)

```bash
# RIGHT
cd /Users/bruce/.openclaw/workspace/gtmdot
wrangler pages deploy deploy --project-name=gtmdot --commit-dirty=true

# WRONG (silently strips functions)
cd /Users/bruce/.openclaw/workspace
wrangler pages deploy gtmdot/deploy --project-name=gtmdot --commit-dirty=true
```

When deploying `gtmdot.com`, wrangler looks for `functions/` relative to your CWD, not relative to the deploy target. If you stand in `workspace/`, wrangler doesn't find the functions and silently ships a deploy with **zero** functions — breaking `/api/lookup-code` and the entire claim-flow on the live site.

**Canary lines** that MUST appear in the deploy output:
```
✨ Compiled Worker successfully
✨ Uploading Functions bundle
```

If those lines are missing, you just broke production. Cancel, `cd` to the right directory, redeploy.

I tripped this on 2026-05-12 and broke the live site for ~20 minutes.

### 4.2 The 4-place claim-code rule

A prospect's claim code must appear identically in:

1. **Supabase `prospects.claim_code`** — source of truth (what Poplar pulls at print time, what Resend merges into email body)
2. **`gtmdot/deploy/functions/api/lookup-code.js`** — what gtmdot.com knows about
3. **The prospect's preview website HTML** — baked in at site build time
4. **The printed postcard** — Poplar pulls from Supabase

If any drift, the prospect's experience breaks. Sync everything FROM Supabase, not TO it.

Last full sync: 2026-05-12 commit `13fddebf`. All 45 then-active prospects synced. Spot-check on new prospects.

### 4.3 Screenshot script path bug

`brucecom-v3/scripts/generate-postcard-screenshots.ts` writes to
`/Users/bruce/.openclaw/.openclaw/workspace/gtmdot/postcards/screenshots/`
(doubled `.openclaw/`) instead of the canonical
`/Users/bruce/.openclaw/workspace/gtmdot/postcards/screenshots/`.

**Workaround**: after each run, copy from the wrong-path output to canonical:
```bash
cp /Users/bruce/.openclaw/.openclaw/workspace/gtmdot/postcards/screenshots/<slug>-{desktop,mobile}.jpg \
   /Users/bruce/.openclaw/workspace/gtmdot/postcards/screenshots/
```

**Real fix** (not done): correct the `OUT_DIR` resolve() call in the script.

### 4.4 Cloudflare Pages SPA-fallback trap

Cloudflare Pages serves SPA fallback HTML at any non-existent path with content-type matching the request. So an "image" URL at `pages.dev/photos/nonexistent.jpg` returns **HTTP 200 with image/jpeg content-type** but the body is actually 67KB of fallback HTML.

**Never trust HTTP 200 alone**. Always either:
- Check magic bytes: JPEG starts with `FF D8`, PNG starts with `89 50`, WebP starts with `52 49 46 46` (RIFF)
- Or check first byte isn't `<` (HTML)

This bit me when batch-downloading prospect-site photos to stage a redeploy.

### 4.5 The screenshot-script `networkidle` race

The Playwright script captures at `networkidle` + 800ms (I bumped to 2500ms on 2026-05-12). For sites with heavy heroes (3000×1700+ JPEGs), even 2500ms is sometimes not enough. Symptom: screenshot captures the gradient/text but the hero image void is black.

Fix when you see this: re-run capture with longer wait, or modify the script to explicitly wait for the hero image element to be visible.

### 4.6 Site hero pattern varies per site (CRITICAL — caused my 2026-05-12 batch error)

Don't assume every prospect site uses `/photos/hero.jpg` the same way.

Patterns I've observed:
- **hero-bg pattern** (6 sites): `<div class="hero-bg" style="background-image:url('photos/hero.jpg')">` or CSS `background-image:url('photos/hero.jpg')` on `.hero-bg` or `.hero`. Postcard hero ↔ site hero alignment works cleanly.
- **gallery img pattern** (1 site — appliance-gals): `<img src="photos/hero.jpg">` in a gallery card with a real-job caption. **DO NOT swap the file** — you'll create FTC risk by putting synthetic content under a real-job caption.
- **orphan pattern** (6 sites): no reference to `photos/hero.jpg` at all. Site hero is gradient-only. Deploying a file there is a no-op for the live site.

**Before any "swap hero" batch work**: scan each site's HTML/CSS to confirm the pattern. Only swap if it's hero-bg pattern AND the site CSS is set up to use the file as a background.

### 4.7 `SEND_LIVE=true` is the gate between dry-run and real sends

Lives in `brucecom-v3/.env.local`:
```
SEND_LIVE=true
NEXT_PUBLIC_SEND_LIVE=true
```

If this ever flips to `false`, both Resend and Poplar return dry-run responses — sends silently succeed without actually contacting the prospect, and the CRM stage advances anyway. Verify before any bulk send.

### 4.8 CRM is launchd, not PM2

The DEPLOY.md says PM2 runs the CRM. It's actually `com.bruce.gtmdot-crm` in launchd. PM2 has no processes registered.

```bash
# Restart CRM:
launchctl kickstart -k "gui/$(id -u)/com.bruce.gtmdot-crm"

# Check tunnel:
launchctl list | grep gtmdot-crm
```

Cloudflare Tunnel at `com.bruce.gtmdot-crm-tunnel` routes `crm.cloakanddagger.co` → `127.0.0.1:3002`. If the Mac mini sleeps, both stop. `caffeinate` LaunchAgent should prevent this but didn't on the night of 2026-05-12.

### 4.9 The CRM build has pre-existing broken state

`brucecom-v3` working tree has ~58 dirty files (mostly deleted in working tree). When I rebuilt on 2026-05-12, I stashed them as `mini-temp-stash-pre-rebuild` at `stash@{0}`. Includes deletions that may or may not have been intentional. Worth a careful review before dropping the stash.

I also created two stub files to make the build succeed: `src/lib/vault.ts` and `src/lib/vault-learning.ts`. The real versions were restored from git (per system reminders I received). Verify these stubs got overwritten correctly.

---

## 5. The outreach-preflight skill

Location: `gtmdot/skills/outreach-preflight/SKILL.md` (commit `3e0b3c64`).

The skill captures the full pre-send checklist. **Codex should adopt and own this**. Key contents:

### Hard blockers (13 checks)

1. Stage is `qa_approved` or `outreach_staged`
2. Claim code parity across all 4 places
3. Postcard hero on CDN (200, image/jpeg, ≥3000×1700)
4. Hero provenance = `openai/gpt-image-2` in `bruce-asset-intel.json`
5. Site hero matches postcard hero (byte-size parity at live URLs) — **AMEND THIS PER SECTION 6 BELOW**
6. Desktop screenshot on CDN
7. Mobile screenshot on CDN
8. Screenshots not visually broken (top 25% of pixels not >95% one color)
9. Preview site loads (200, text/html, >5KB body)
10. No placeholder text on live site (regex scan)
11. Address parseable for postcard
12. Postcard merge tags resolve (Poplar dry-run)
13. Email present (if email channel)

### Soft warnings

- Star rating < 4.5★
- Duplicate signal (shared phone/address)
- Open non-qa-bot notes
- FTC-risk patterns (fake testimonial attributions, stock photo URLs as proof)
- Hero file age > 30 days
- Screenshot age > 7 days

### Auto-fix lane (pre-authorized, no per-prospect approval needed)

- CDN sync (copy file + redeploy postcard CDN)
- Screenshot capture (Playwright run + copy + redeploy)
- lookup-code.js sync (add/update from Supabase + redeploy gtmdot.com)
- Site hero swap (download live + swap + redeploy prospect site) — **BUT see section 6 below for the failure mode**

NOT auto-fix (requires Jesse approval per-prospect):
- Stage moves
- `submit_postcard` and `send_email`
- Anything money-related

---

## 6. The preflight skill needs an amendment (my 2026-05-12 lesson)

The "site hero matches postcard hero" hard check (#5 above) verifies byte-size parity at the URLs. **That's insufficient.** It confirms the file landed at the URL; it doesn't confirm the site is actually displaying it.

**Add a new sub-check**: "Site DISPLAYS the postcard hero" — verified by either:
- (a) Scanning the live HTML for `background-image:url('photos/hero.jpg')` in CSS, OR
- (b) Downloading the post-deploy mobile screenshot and inspecting that the top 25% of pixels aren't uniform (catches the gradient-only-hero failure mode)

If neither is satisfied, the site is one of:
- Orphan-hero (file exists, no CSS uses it)
- Gallery `<img>` use (file is being used in a gallery, not as hero) — **STOP, don't swap, FTC risk**

This amendment would have prevented my 2026-05-12 batch error. Implementing it is the first thing I'd ask Codex to do after handoff.

---

## 7. Tools / access / file paths

### Repos

| Repo | Path | What's in it |
|---|---|---|
| `bruce-workspace` (parent) | `/Users/bruce/.openclaw/workspace/` | Contains everything below as subdirs. Single GitHub origin. |
| `gtmdot` | `/Users/bruce/.openclaw/workspace/gtmdot/` | Marketing site source (`deploy/`, `sites/gtmdot/`), postcard CDN source (`postcards/`), skills (`skills/`), scripts (`scripts/`), per-prospect site sources (`sites/<slug>/index.html` — incomplete; photos source ambiguous) |
| `gtmdot-sites` | `/Users/bruce/.openclaw/workspace/gtmdot-sites/` | Bruce's enrichment outputs per prospect (`sites/<slug>/photos-generated/`, `bruce-collected.md`, `bruce-asset-intel.*`). Also `messages/` and `scripts/` |
| `brucecom-v3` | `/Users/bruce/.openclaw/workspace/brucecom-v3/` | The CRM Next.js app (crm.cloakanddagger.co) |

### Cloudflare Pages projects

| Project | URL | Source |
|---|---|---|
| `gtmdot` | `gtmdot.com`, `gtmdot.pages.dev` | `gtmdot/deploy/` (includes `functions/api/lookup-code.js`) |
| `gtmdot-postcards` | `gtmdot-postcards.pages.dev` | `gtmdot/postcards/` (heroes + screenshots/) |
| `<slug>` (per prospect) | `<slug>.pages.dev` | Source ambiguous; in practice, I downloaded live + swapped + redeployed |

### Useful scripts

| Script | What it does |
|---|---|
| `brucecom-v3/scripts/generate-postcard-screenshots.ts` | Playwright capture, desktop + mobile. **Has the doubled-path bug.** |
| `gtmdot-sites/scripts/outreach-readiness-gate.sh` | Old gate (predates preflight skill); useful for spot-checks |
| `gtmdot/scripts/build-site.sh` and `deploy-site.sh` | Per-prospect site build/deploy (R1VS uses these) |

### Credentials / env

- `brucecom-v3/.env.local` has `SEND_LIVE=true`, `RESEND_API_KEY`, `POPLAR_API_KEY`, `POPLAR_CAMPAIGN_ID`, `POPLAR_WEBHOOK_SECRET`
- Supabase project: `qztjoshdrxionhxeieik` (host: `db.qztjoshdrxionhxeieik.supabase.co`)
- Stripe Payment Links (verify in dashboard):
  - Once: `https://buy.stripe.com/5kQ14n0m97h906v1Xn00004` ($1,999)
  - Monthly: `https://buy.stripe.com/28E3cv9WJ44Xg5tfOd00006` ($149/mo recurring + $100 first-month discount = $49 intro — needs Stripe-dashboard verification)

### Pricing canonical values

- Pay Monthly: $49 first month, $149/mo ongoing
- Own It Now: $1,999 one-time
- Hosting & Maintenance add-on (Own It Now path only): $149/mo
- Content & SEO add-on: $150/mo

---

## 8. Communication protocols going forward (proposed)

### Codex ↔ Jesse

Direct via Codex-mobile app. No Mini-as-relay.

### Codex ↔ Bruce

Direct via OpenClaw integration. No Telegram, no Mini-as-relay.

### Codex ↔ Mini (me)

Mini stands down to read-only / on-call. If you hit something only I'd remember, ping via:
- File: `gtmdot-sites/messages/YYYY-MM-DD-codex-to-mini-question.md`
- Or Jesse-relay if real-time matters

I'll respond same-day if active. After ~1 week of clean operation without needing me, the Mini session can be closed entirely.

### Codex ↔ R1VS

Per Jesse's existing workflow. R1VS is offline weekends; scaffold work batched accordingly.

---

## 9. Recommended first moves for Codex

1. **Read this whole doc once** (5 min)
2. **Pull `gtmdot/skills/outreach-preflight/SKILL.md`** and skim — that's your daily reference
3. **Verify your view of the prospect state matches section 2** by querying Supabase yourself (don't trust this doc once it's >48 hours old)
4. **Decide on the-appliance-gals Part B** (b1 recommended — rename gallery img src). Execute Part B + Part A. Hand to Jesse for send approval.
5. **Wire ATL Mobile Mechanics reviews** (post-send finishing).
6. **Confirm Bruce's cron prompt update is live** (the type-routing patch from 2026-05-13). Test with a synthetic Codex-lane request — Bruce should skip it.
7. **Amend the preflight skill** per section 6 (add the "site displays the hero" check).
8. **Run preflight in batch mode** on the 7 qa_approved to confirm they're ready for promotion.
9. **Audit the 6 orphan-hero sites** and decide R1VS-template-change vs per-site-edit.

---

## 10. What I'm doing post-handoff

- Standing down from execution
- Watching for ping if Codex needs context only I'd have
- Available for ~1 week, then session can be retired
- Not running any preflight, deploy, send, or stage-change operations on my own

---

## Final notes

- All my work since 2026-05-08 is in git. Commit hashes referenced throughout this doc are real and verifiable.
- I made real mistakes (the site-hero-swap scope error being the biggest). I've documented them honestly in section 4 so Codex avoids the same traps.
- Jesse is shipping fast and trusts the systems we've built. Keep that pace going.
- The outreach-preflight skill is the single biggest investment of the past week. Adopt it, amend it, run it religiously.

Good luck.

— Mini Claude, 2026-05-15 handoff
