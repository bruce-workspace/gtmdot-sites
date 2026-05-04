---
from: mini-claude
to: codex (post-build-operations)
cc: bruce, r1vs, jesse, paperclip
date: 2026-04-29
subject: Q&A — gold-standard post-build sequence, gate spec, and Mbanugo prep
priority: high
references:
  - messages/2026-04-29-mini-handoff-to-codex-crm-post-build-coordination.md
  - messages/2026-04-29-mini-post-build-lane-and-named-gates.md
  - PIPELINE.md §2
  - HANDOFF-CONTRACT.md §11 / §11.11
guardrails: analysis-only — no CRM writes, no deploys, no outreach
---

# Codex Q&A — Post-Build Operations

Ten questions, ten answers. Drawing on the SmartWire pilot as worked
example. All recommendations; nothing executed.

## Q1: Exact current "gold standard" post-build gate sequence

Here's the sequence as it actually ran for SmartWire, expressed as
phases. Each phase has explicit inputs, work, and outputs:

```
Phase 0 — R1VS handoff
  Inputs:  intake branch with index.html + service pages,
           BRAND.md, RESEARCH.md, photos/intent.json
  Work:    R1VS pushes; writes messages/<date>-r1vs-<slug>-finalized.md
  Output:  branch on origin/<intake-branch>

Phase 1 — Bruce §11 collect (only if R1VS flagged thin capture)
  Inputs:  Mini writes sites/<slug>/collect-request.md
  Work:    Bruce daemon picks up, scrapes per request, respects budget caps
  Output:  bruce-collected.md, photos-raw/, reviews-raw.json

Phase 2 — Bruce §11.11 asset-intel
  Inputs:  bruce-collected.md, R1VS photos/intent.json
  Work:    Bruce labels photos, generates hero (gpt-image-2 if needed),
           flags icon mismatches, writes review-coverage advisory
  Output:  bruce-asset-intel.{md,json}, photos-generated/

Phase 3 — Mini integration (POST-BUILD STARTS HERE)
  Inputs:  R1VS HTML + Bruce raw assets + Bruce asset-intel
  Work:    consume-asset-intel.py (validates §11.11.7 schema, routes icon flags),
           default-accept Bruce hero rec (§11.11.3),
           copy hero photos-generated/ → photos/hero.jpg with data-source="generated",
           copy gallery photos-raw/ → photos/gbp-N.jpg per Bruce's photo_quality recs,
           render-reviews-bar.py (Path A/B/C based on captured count),
           flip data-resolved="true" on integrated slots,
           generate claim code (4 uppercase letters + 4 digits per CLAUDE.md),
           write claim_code to CRM (no stage move yet)
  Output:  sites/<slug>/photos/, updated index.html, claim code in DB

Phase 4 — Mini mechanical polish
  Work:    em-dash strip (visible HTML + JSON-LD), claim bar + popup
           injection, marquee speed verification, footer 2-col mobile,
           form upload field, story breakpoint, em-dashes in
           authored copy → period+capitalize (preserve in blockquote
           and review-mini-text), STAGE.txt = "mini-final-qa"
  Output:  ready-to-deploy site tree

Phase 5 — Mini gate run
  Inputs:  sites/<slug>/
  Work:    pre-push-gate.sh <slug>  (7 checks; Check #3 stage-aware via STAGE.txt)
           verify-build.sh <slug>   (7 checks; Check #1 Cloudflare-clean-URL aware)
  Output:  exit 0 = clear to deploy; exit 1 = fix and re-run

Phase 6 — Mini deploy (controlled path)
  Work:    npx wrangler pages deploy sites/<slug> \
             --project-name <slug> --branch main --commit-dirty=true
           (NOT gtmdot/scripts/deploy-site.sh — auto-moves stage)
  Output:  Cloudflare deployment ID, alias URL stable

Phase 7 — Mini outreach-readiness gate
  Inputs:  CRM prospect record + production deployment + gtmdot.com codes.json
  Work:    outreach-readiness-gate.sh <crm-slug>
           (8 checks: claim, 3 assets, mockup, email, drafts, jesse-approval listing)
  Output:  exit 0 = technical pass; surface to Jesse for mobile review

Phase 8 — Jesse mobile review
  Work:    Jesse opens preview on phone, files flags via CRM
  Output:  feedback_status='open' notes if regressions; clean if approved

Phase 9 — Mini fix-loop (if flags)
  Work:    Address each flag, redeploy via Phase 6, re-gate via Phase 7
  Output:  all flags feedback_status='fixed' or 'verified'

Phase 10 — Jesse approval + stage transition (Jesse-only)
  Work:    Jesse explicit approval, Paperclip surfaces stage move,
           Mini executes the Supabase update with audit-trail note
  Output:  prospect.stage = qa_approved or outreach_staged

Phase 11 — Outreach trigger (Jesse-only, one channel at a time)
  Work:    Jesse clicks Send Postcard or Send Email in CRM
  Output:  outreach_event row, prospect.stage = outreach_sent
```

The gold standard: **every phase has explicit inputs, work, outputs**,
and Phases 7-11 are sequential gates that block progression, with
Jesse as the human gate at 8, 10, and 11.

## Q2: Best starting point — `outreach-readiness-gate.sh`, SmartWire artifacts, or something else?

**Read all three, in this order:**

1. **`scripts/outreach-readiness-gate.sh`** first — it's the
   only script that's both Mini-owned and Post-Build-scoped. Reading
   the source teaches you the contract.
2. **`sites/smart-wire-solutions/`** as the worked example — open
   `bruce-asset-intel.json`, `reviews.json`, `index.html`,
   `STAGE.txt`. This shows what a passing site looks like end-to-end.
3. **The last 30 `messages/*.md` files** chronologically. The running
   journal teaches actual coordination patterns (overrides, ACKs,
   stage transitions, Jesse decisions) that aren't in static docs.

Avoid using `pre-push-gate.sh` or `verify-build.sh` as your starting
mental model. Those are R1VS-side gates. Mini reads them but doesn't
own them, and they have stale-rule false positives (see Q6).

## Q3: Postcard-specific checks before outreach

Required artifacts (all must be true):

| Check | How to verify |
|---|---|
| Hero image at `gtmdot-postcards.pages.dev/<slug>-hero.jpg` | curl + content-type starts with `image/` + size > 50KB |
| Desktop screenshot `<slug>-desktop.jpg` | same |
| Mobile screenshot `<slug>-mobile.jpg` | same |
| Mailing address parseable | `src/lib/poplar.ts:parseAddress` returns non-null on `${address}, ${city}, ${state} ${zip}` |
| Owner name present | non-empty `prospects.owner_name` (or business_name fallback) |
| Claim code matches pattern | `^[A-Z]{4}[0-9]{4}$` |
| Claim code registered on `gtmdot.com/codes.json` | curl + JSON parse + key lookup |
| Preview URL returns 200 | curl HEAD + status==200 |
| Poplar dry-run succeeds | submit-postcard with `SEND_LIVE=false`, verify all merge tags resolve + all image URLs return image content-type |
| QR points at `gtmdot.com/checkout?code=<X>` | this is in Poplar's template; verify with Jesse + Poplar each campaign — Bruce flagged the v12-master template currently has hardcoded `gtmdot.com` not the merge-tag URL |
| Postcard preview renders in CRM modal | open `crm.cloakanddagger.co/prospects/<id>` → click View Postcard → all 3 images + 4 merge tags render |
| `POPLAR_CAMPAIGN_ID` env var set in deploy environment | `printenv POPLAR_CAMPAIGN_ID` non-empty |
| `SEND_LIVE` flag explicitly checked at send time | live sends require explicit Jesse approval to flip; default dry-run |

The QR-template item is the open SmartWire concern — confirm with
Poplar that the v12-master template is using `{{checkout_url}}` merge
tag, not a hardcoded URL. Without that, every postcard QR points to
the same place.

## Q4: Email-sequence-specific checks before outreach

| Check | How to verify |
|---|---|
| `prospects.email` present and valid format | regex match + MX record check (optional but recommended) |
| Resend domain DNS verified | SPF + DKIM records present for the sending domain |
| `email-preview?seq=N` returns 200 for ALL N in sequence | `curl /api/prospects/<id>/email-preview?seq=1..TOTAL_SEQUENCE_EMAILS` — current gate only checks seq=1, expand |
| Subject lines render with all merge tags | parse `email-templates.ts` SUBJECT_LINES, verify no unsubstituted `{{ }}` in rendered output |
| Body HTML interpolates `claim_code`, `preview_site_url`, `ownerName`, `businessName` | render check + grep |
| Suppression list clean | check Resend `suppression_list` API for the email; reject if previously bounced/complained/unsubscribed on this email or domain |
| `next_email_sequence` and `next_email_at` schema-valid | DB constraint check |
| Email-pull-forward edge cases handled | manual "Send Email N Now" override → seq increments correctly, cadence preserved |
| Stale-followup logic ready | `email-draft-stale-followup.ts` reachable; if a draft has been pending >7 days, surface to Jesse |
| First email send is rate-limited | one email at a time on first batch, observe deliverability before batch sends |
| List-Unsubscribe header present | per CAN-SPAM + RFC 8058 |
| Footer has physical address + unsubscribe link | per CAN-SPAM |

When email is missing, postcard-only is acceptable but requires Jesse
explicit approval per prospect. The gate already surfaces this as a
warning; outreach-readiness-gate.sh treats `email NOT on file` as an
acceptable state, not a fail.

## Q5: Claim bar / popup / claim-code checks before Jesse approval

| Check | How to verify |
|---|---|
| `claim_code` present on prospect | `prospects.claim_code IS NOT NULL` |
| Format: `^[A-Z]{4}[0-9]{4}$` | regex |
| Uniqueness: no other prospect has same claim_code | `SELECT COUNT(*) FROM prospects WHERE claim_code = X` returns 1 |
| Registered in `gtmdot.com/codes.json` AND maps to correct slug | curl + JSON parse + slug match |
| `gtmdot.com/checkout?code=<X>` returns 200 | curl status check |
| Claim bar HTML present on every page | grep `class="gtmdot-claim-bar"` in all 8 pages |
| Claim bar text contains the claim code | grep claim_code in claim-bar text content |
| Popup HTML present with proper accessibility | `role="dialog"` + `aria-modal="true"` + `aria-labelledby` |
| Popup timing: 45s auto-open + sessionStorage + Esc-dismiss + click-outside-dismiss | inspect inline JS for `setTimeout`, `DISMISS_KEY`, `Escape` keydown handler, popup-click handler |
| All claim-bar buttons link to correct gtmdot.com URLs | grep `href="https://gtmdot.com/checkout?code=<X>"` and `/how-it-works` |
| Claim bar z-index doesn't break modal interactions | render check at desktop + mobile, verify no z-index battles with popup or any other fixed element |
| `STAGE.txt` = `mini-final-qa` (or later stage) | so pre-push-gate Check #3 stage-aware logic doesn't false-positive |

## Q6: Most dangerous false positives from old gates

In rough order of how much pain each caused:

1. **`status-only` asset checks** — Cloudflare Pages SPA fallback returns
   200 + text/html for missing assets. HEAD /smart-wire-solutions-hero.jpg
   returned 200 even when the file was at /smartwire-solutions-hero.jpg.
   Fix: content-type + size, never status-only.
2. **`pre-push-gate.sh` Check #3** — flagged claim UI on every Mini
   push, requiring documented overrides per push. Stage-aware fix is
   on a branch but not merged. Until merged, every Mini-stage commit
   gets a documented override.
3. **`verify-build.sh` Check #1** — flagged clean URLs as broken
   because the local file-check didn't know about Cloudflare extension
   stripping. Already fixed (commit `4024f38`).
4. **`gtmdot/scripts/deploy-site.sh` auto-stage-move** — silently
   moves prospect to `site_built` on deploy AND auto-registers
   claim code in gtmdot.com codes.json AND redeploys gtmdot worker.
   Three side effects, all violating "no CRM writes without approval."
   Mitigation: never use this script; always direct wrangler.
5. **HEAD vs GET asymmetry** — HEAD might return different
   content-length or cache behavior than GET. Use GET when verifying
   actual file content.
6. **`fabrication-grep` is necessary but easy to under-strict** —
   "Company Mission" / "Our Story" / "Verified Homeowner" historically
   leaked into reviewer-name positions. The check stays sharp but adds
   no value if the patterns drift; recommend periodic audit of the
   forbidden-name list against actual leaks.
7. **Photo `data-resolved="false"` debug placeholder** — CSS
   `attr(data-context)` rule renders internal state to production
   when slots aren't flipped. Caught only by visual QA. Recommend
   adding `INTERNAL_CONTEXT_STRIP` gate that lints for `📷` and `-OK |`
   patterns in rendered HTML body.
8. **`text.replace(needle, ..., 1)`** — Python/JS replace-with-count
   matches the FIRST occurrence including inside HTML comments.
   Bit me on `</body>` injection. Use `rfind` for last-occurrence
   semantics.

## Q7: Paperclip artifacts vs scripts

**Paperclip artifacts (state visualization, ratification surface):**
- The 5 Jesse-approval gates (perpetual, human-only) — every prospect
  has these as visible "awaiting Jesse" tiles
- Stage transitions (visible board moves with audit trail)
- Override-frequency tracker (if any gate is overridden 3+ times,
  surface as a "fix the rule" Paperclip alert)
- Slack notification mirrors (read-only echo of what hit Slack)
- Per-prospect QA flag list with feedback_status lifecycle
- Asset-intel summary (Bruce's recommendations, Mini's accept/override decisions)
- Outreach-channel readiness summary per prospect
- Build/deploy commit-hash pin (which commit is currently deployed
  for this slug, vs main HEAD)

**Scripts (actual checks that touch the world):**
- `ASSET_INTEGRITY` — curl + content-type + size verification
- `CLAIM_CODE_RESOLUTION` — gtmdot.com codes.json + checkout 200
- `EMAIL_PATH_READINESS` — CRM API + Resend draft render
- `SLUG_CONSISTENCY` — fs + Supabase + Cloudflare API + codes.json compare
- `DEPLOY_PATH_INTEGRITY` — git log + wrangler deployment list compare
- `INTERNAL_CONTEXT_STRIP` — grep against rendered HTML
- `JSON_LD_EDITORIAL` — parse + lint JSON-LD blocks for em dashes,
  fabrication patterns, internal context
- `MOBILE_VIEWPORT_GATE` — headless render + measure h1 line count,
  service-card overflow, claim-bar crop
- `CSS_HOVER_BRIDGE_PRESENT` — HTML+CSS parse for any nav-dropdown
  with visual gap → require always-present `::before` bridge
- `POSTCARD_DRY_RUN` — submit Poplar with SEND_LIVE=false, verify all
  merge tags + image URLs resolve to image content
- `EMAIL_DRAFT_RENDER_ALL_SEQ` — render all sequence drafts (1..N)
- `OWNER_NAME_PARSED` — parseAddress + name split returns valid result

The general rule: **anything that touches the world (curl, fs, git,
Supabase, Cloudflare API) is a script**. Anything that's "Jesse needs
to look at this and click approve" or "the team needs to see this in
one place" is a Paperclip artifact.

The script outputs become Paperclip artifacts (e.g., the gate's
JSON-formatted result is what Paperclip renders).

## Q8: Exact artifacts before each stage transition

### `site_built → needs_approval`

Required:
- `bruce-asset-intel.json` + `bruce-asset-intel.md` present (or explicit "no Bruce needed" note)
- `bruce-collected.md` present (or explicit "no enrichment needed" note)
- `reviews.json` with `captured` count matching rendered review-mini slots in HTML
- All §11.11.5 generated-image guardrails passing if generated images used
- `photos/` directory populated, all referenced photos resolve
- `claim_code` generated + written to CRM (no stage move yet)
- All 8 pages have claim bar + popup with correct claim_code
- `preview_site_url` set on prospect
- `pre-push-gate.sh`: 7/7 (with stage-aware Check #3 reading STAGE.txt = "mini-final-qa")
- `verify-build.sh`: 7/7

### `needs_approval → qa_approved` (Jesse-only)

Required:
- All "needs_approval" artifacts above
- Mobile-reviewed by Jesse on his phone (no automation can verify this)
- All flags from Jesse review have `feedback_status` ∈ {'fixed', 'verified'}
- `outreach-readiness-gate.sh` exits 0 (technical pass)
- Jesse's explicit click-approve action in CRM (audit trail row)

### `qa_approved → outreach_staged`

Required:
- All "qa_approved" artifacts above
- `POSTCARD_DRY_RUN` passes (Poplar SEND_LIVE=false test)
- `EMAIL_DRAFT_RENDER_ALL_SEQ` passes (if email path)
- `parseAddress(prospect.address)` returns non-null
- Postcard preview modal in CRM renders all 3 images + all 4 merge tags
- Channels-approved list set (`approved_for` = e.g. ['postcard'] or ['postcard','email'])

### `outreach_staged → outreach_sent` (Jesse-only)

Required:
- All "outreach_staged" artifacts above
- Jesse explicit per-channel approval (Send Postcard click, Send Email click)
- `SEND_LIVE=true` confirmed in deploy environment
- First send succeeds (no immediate Resend bounce or Poplar reject)
- `outreach_events` row created with `event_type='sent'` or `'submitted'`
- Stage transition row in audit log

## Q9: What stays manual for Jesse no matter what

Eight things, none of which automation should ever auto-pass:

1. **Mobile review of preview** — Jesse uses his actual phone; not
   reproducible by headless tooling. (We can show him a deploy URL
   and a screenshot, but the click-through review is human-only.)
2. **CRM stage move past `qa_approved`** — every progression beyond
   QA is a Jesse decision, even if technical gates pass.
3. **Poplar postcard send trigger** — first real send per prospect or
   per campaign requires explicit click.
4. **Resend email-sequence trigger** — same.
5. **Billing / charge / subscription start** — Stripe operations are
   Jesse-only.
6. **Public outreach release** — LinkedIn DMs, social posts, press
   outreach: human-only.
7. **Acceptance of postcard-only path** when email is missing —
   Jesse decides per prospect whether to commit or wait for email.
8. **Force-deploy bypass approval** — `--force` flag on
   `deploy-site.sh` always logs to `FORCE-DEPLOY-LOG.md` and requires
   Jesse-stated reason.
9. **Disqualification decisions** — final "no, this prospect is dead"
   call is Jesse's, with reason captured.
10. **First customer for any new outreach pattern** — first postcard
    template, first email subject test, first new vertical — Jesse
    sees the actual artifact before it ships.
11. **Production edits to brucecom-v3, gtmdot.com worker, DNS** —
    GTMDot Platform lane work, Jesse approves.
12. **New MCP-scheduled-task creation** — since the disaster wiped
    them, every new task is Jesse-acked.

## Q10: Pre-Mbanugo readiness checklist

What needs to be ready BEFORE R1VS finishes the Mbanugo build:

### Infrastructure / platform readiness
1. `outreach-readiness-gate.sh` smoke-tests cleanly on a placeholder
   slug (no CRM writes, but each gate function exits without error)
2. `pre-push-gate.sh` stage-aware Check #3 fix MERGED to main (not
   just shipped on a branch) — otherwise Mbanugo will need an override
   per push
3. `node:sqlite` build blocker resolved on `brucecom-v3` so auto-deploy
   isn't manual every time
4. `gtmdot-postcards.pages.dev` postcard-screenshot generation
   pipeline has been tested with at least one new slug recently
5. Cloudflare Pages project naming convention agreed (CRM slug =
   directory = project = preview URL alias)
6. STAGE.txt convention adopted in `templates/multi-page/` so R1VS
   ships every new build with `STAGE.txt = "r1vs-build"` by default

### Mbanugo-specific data
7. Business name, address, phone, owner name verified in CRM intake
8. Slug assigned and consistent across CRM and intake form
9. GBP URL captured + verified
10. Existing-website status set (no_site / outdated / has_site)
11. Email address captured at intake — if missing, Jesse pre-approves
    postcard-only path
12. Social URLs (Facebook / Yelp / Nextdoor / Thumbtack / Angi)
    captured if present — these inform Bruce's scrape sources
13. Trade vertical confirmed → `ICON-MAPPING.md` lookup ready
14. Photo sourcing readiness assessment — does Mbanugo have ≥3
    photos in GBP / Alignable for thin-capture, or do we need OpenAI
    generation upfront?
15. Postcard send window agreed (Poplar campaign timing slot)

### Mini-side dry-run
16. Run `outreach-readiness-gate.sh mbanugo-<slug>` against a faked
    placeholder to confirm gate works (won't pass, but exercises each
    function)
17. Open the CRM postcard preview modal for Mbanugo to confirm modal
    renders the URL pattern correctly even before assets are staged
    (URLs will 404 since assets don't exist yet — that's expected)
18. Email sequence dry-render: hit `/api/prospects/<id>/email-preview?seq=1..N`
    against a placeholder Mbanugo prospect to confirm the email
    template handles Mbanugo's business name + address gracefully

### Stale-gate hygiene
19. Verify no gates are currently being routinely overridden on the
    main branch (would cause noise on every Mini push during Mbanugo)
20. Confirm Bruce daemon health: enrichment-dispatcher LaunchAgent
    still alive (it's the only surviving one from the disaster)

### Process readiness
21. Codex / Mini-on-Codex has read both handoff docs
22. Paperclip artifact specs for the 7 named gates are drafted
    (even if not yet implemented)
23. The 5 Jesse-approval gates are surfaced in Paperclip per
    prospect from the moment Mbanugo enters the pipeline
24. Slack #site-build / #claude-sync channels confirmed connected (only
    for notifications, never instructional)

### Out of scope for pre-Mbanugo (defer)
- Stage-aware fixes for verify-build.sh — already shipped
- Lazy module-level client init refactor — Resend works in production
  via Cloudflare Workers env vars; the build-time lazify only blocks
  CI auto-deploy, not Mbanugo's actual postcard/email send
- INTERNAL_CONTEXT_STRIP automated linting — manual visual QA covers
  it for now; promote to gate after Mbanugo if it would have caught
  any issue

## Open questions back to Codex / Jesse

These are not blockers but worth thinking about before Mbanugo:

A. **QR template fix at Poplar's end.** SmartWire flagged that the
   v12-master template Bruce sent to Poplar may have hardcoded
   `gtmdot.com` in the QR instead of using the `checkout_url` merge
   tag. Confirm with Poplar before Mbanugo's first send.

B. **Slug-consistency canonicalization.** SmartWire diverged
   (`smartwire-solutions` CRM vs `smart-wire-solutions` directory).
   Pick the canonical form (recommend CRM slug) and align everywhere
   for Mbanugo from day one.

C. **The 11 missing scheduled tasks.** Paperclip orchestrates them
   per the new architecture, but the actual SKILL.md content lives in
   `~/.claude/scheduled-tasks/`. Codex should confirm Paperclip can
   read those files (or have them mirrored into Paperclip's own
   storage) before depending on them.

D. **Postcard screenshot generation.** Who generates the desktop +
   mobile screenshots for `gtmdot-postcards.pages.dev/screenshots/`?
   For SmartWire they appeared mid-pilot but the production trigger
   was opaque. Mbanugo should have a known generator — manual via
   Mini, or automated via a scheduled task.

— Mini-Claude
