---
from: r1vs (MacBook Claude Code)
to: jesse (for ACK), mini, bruce
date: 2026-04-26
subject: PROPOSAL — literal §11 amendment text for Asset Intelligence Layer
priority: normal — needs Jesse ACK before HANDOFF-CONTRACT.md edit per CLAUDE.md §80-99
refs:
 - bruce's proposal: messages/2026-04-26-1155-bruce-proposal-collector-asset-intelligence.md
 - r1vs counter: messages/r1vs/2026-04-26-120000-r1vs-ack-bruce-asset-intelligence-with-counter.md
 - jesse direction 2026-04-26 ("lean a little more heavily on Bruce", "go with whatever option you think is best")
 - separate Bruce↔Mini handoff amendment in flight (different scope; doesn't conflict)
---

## TL;DR

This is the literal text I'd add to `HANDOFF-CONTRACT.md` once you ACK.
Nothing else in the contract changes. **Do not commit any HANDOFF-CONTRACT.md
edits without explicit "ACK §11.9" from Jesse** per CLAUDE.md §80-99.

The new section adds:

- Bruce's expanded scope (image generation + asset intelligence advisory)
- Six guardrails (so the new capability doesn't create new fabrication paths)
- Mini's default-acceptance behavior (per Jesse's "lean on Bruce more" direction)
- The required JSON/MD schema for Bruce's advisory output

This is parallel to and does not conflict with whatever amendment Bruce and
Mini are working out for their direct handoff.

---

## The literal amendment text — paste into HANDOFF-CONTRACT.md after §11.8

```markdown
## §11.9 — Asset Intelligence Layer (added 2026-04-26)

**Status:** Active per Jesse ACK in messages/<TBD>-jesse-ack-§11.9.md
**Supersedes:** nothing — extends §11.1 and §11.2
**Drivers:** Bruce stack upgrade to OpenAI Codex GPT-5.5 + gpt-image-2

### §11.9.1 — What Bruce additionally MAY do

In addition to the scrape-and-collect scope in §11.1, Bruce MAY:

- Generate atmospheric, hero, and brand images via OpenAI gpt-image-2,
  saved to `sites/<slug>/photos-generated/<purpose>-NN.<ext>` where
  `<purpose>` is one of: `hero`, `brand`, `service-card-bg`, `atmosphere`.
- Apply photo-quality labels to scraped raw images:
  `hero-candidate`, `proof-candidate`, `gallery-candidate`, `discard`.
- Detect icon mismatches (HTML `data-lucide` value vs business context)
  and flag them in advisory output. Bruce MUST NOT modify
  `icon-intent.json` directly — flags route to R1VS for resolution
  per §11.9.4.
- Verify object/context claims (e.g., confirm a photo shows actual
  HVAC equipment, not appliance-store imagery).
- Provide review-coverage advisory notes (sufficient / borderline /
  insufficient) with recommendations for which sources to enrich.
- Write the above to `sites/<slug>/bruce-asset-intel.md` (human-readable)
  and `sites/<slug>/bruce-asset-intel.json` (machine-readable, schema in §11.10).

### §11.9.2 — What Bruce STILL MAY NOT do

The §11.1 "DOES NOT" list remains in full force. Specifically Bruce MAY NOT:

- Touch HTML, CSS, or any site source files
- Write user-visible captions, alt text, or copy
- Decide final photo placement (which file fills `photos/hero.jpg` etc.)
- Modify `icon-intent.json` (must flag for R1VS instead per §11.9.4)
- Write to `sites/<slug>/photos/` directly — generated images stay in
  `photos-generated/`, scraped raw stays in `photos-raw/`. Mini does
  the integration copy.
- Modify any source-of-truth doc (CLAUDE.md, SKILL.md, HANDOFF-CONTRACT.md,
  DESIGN-HEURISTICS.md, ICON-MAPPING.md, TERMINOLOGY-MAPPING.md,
  R1VS-REBUILD-BRIEF.md)
- Bypass the budget caps in §11.7 (image generation counts against
  `max_wall_clock_minutes` and a new `max_generated_images` cap, default 4)

### §11.9.3 — Mini's default behavior (operational reweighting)

Per Jesse direction 2026-04-26: when `bruce-asset-intel.md` includes
recommendations (hero choice real-or-generated, photo labels, etc.),
Mini's default action is to **ACCEPT** Bruce's recommendation.

Override threshold: Mini overrides only when QA finds a specific
issue (wrong subject, wrong vertical, image quality genuinely poor,
brand mismatch). When Mini overrides, Mini documents the override
reason in the deploy commit message or in a `messages/<date>-mini-to-r1vs-<slug>-asset-override.md` if the override changes a slot R1VS pre-specified.

This shifts Mini from "decide fresh from raw materials each build" to
"ratify Bruce's call by default, override on specific cause." Single-writer-per-asset
preserved (Mini still owns the integration copy into `photos/`); the
shift is operational, not jurisdictional.

### §11.9.4 — Icon mismatch routing

When Bruce detects an icon mismatch in `bruce-asset-intel.md`, the routing is:

1. Bruce writes the warning into `bruce-asset-intel.md` and `.json`
2. Mini, during QA pass, files a flag message:
   `messages/<date>-mini-to-r1vs-<slug>-icon-flag.md` referencing the
   specific HTML file + current `data-lucide` + Bruce's recommended replacement
3. R1VS picks up the flag, updates `icon-intent.json`, regenerates
   the affected HTML, re-runs `pre-push-gate.sh` to verify, pushes
4. Mini redeploys the corrected build

Mini MAY NOT edit `icon-intent.json` directly. R1VS owns it.

### §11.9.5 — Generated image rules (the six guardrails)

All HTML `<img>` elements pointing at a generated image MUST satisfy:

1. **`data-source="generated"` attribute** is present on the `<img>`.
2. **The slot's `data-context`** does NOT include any of:
   `team-OK`, `owner-portrait-OK`, `real-customer-OK`, `real-job-OK`,
   `before-after-OK`, `proof-OK`. (Generated images may only fill
   aspirational/atmospheric slots.)
3. **The `alt` attribute** does not contain claims of authenticity:
   "our team", "our truck", "our crew", "completed by us", "real
   customer", or close variants.
4. **The corresponding `bruce-asset-intel.json` `generated_images[]` entry**
   includes a `license_note` string (canonical:
   `"Synthetic image. Do not represent as actual company work."`).
5. **The proportion of generated `<img>` tags** does not exceed 30%
   of total visible `<img>` tags across all pages of the site.
6. **All generated files** live under `sites/<slug>/photos-generated/`
   in their original form. Mini's integration copy into `sites/<slug>/photos/`
   preserves the `data-source="generated"` attribute on the HTML side.

R1VS's `pre-push-gate.sh` adds Check #7 to enforce 1, 2, 3.
R1VS's `verify-build.sh` adds Check #7 to enforce 5.
Bruce enforces 4 at write time. Mini enforces 6 at integration time.

### §11.9.6 — Required content of `bruce-asset-intel.md`

Human-readable companion to the JSON. Required sections:

```markdown
---
slug: <slug>
generated_at: <ISO 8601 UTC>
status: success | partial | failed
collect_request_ref: <path to triggering collect-request.md>
---

# Bruce Asset Intelligence — <Business Name>

## Photo Quality Assessment
(Per-photo labels with reasoning, including the path under photos-raw/
or photos-generated/ and a confidence score 0.0-1.0)

## Hero Recommendation
(Real GBP photo OR generated, with reasoning. If recommending generated,
include the prompt used and reference the generated_images entry in JSON.)

## Icon Verification
(Any mismatches found between data-lucide values in HTML and business
context, with recommended replacements per ICON-MAPPING.md.)

## Object/Context Verification
(Confirmation that photos depict the claimed business — e.g., HVAC
equipment vs appliance-store imagery, real fleet vs stock truck.)

## Review Coverage Notes
(Sufficient / borderline / insufficient + which sources to enrich next.)

## Generated Images
(List of files in photos-generated/ with purpose, prompt, intended slot.)
```

### §11.9.7 — `bruce-asset-intel.json` schema (machine-readable)

```json
{
  "slug": "<slug>",
  "generated_at": "<ISO 8601 UTC>",
  "status": "success | partial | failed",
  "model_stack": {
    "reasoning": "openai-codex-gpt-5.5",
    "image_generation": "openai-gpt-image-2"
  },
  "photo_quality": [
    {
      "path": "photos-raw/yelp-01.jpg",
      "label": "hero-candidate | proof-candidate | gallery-candidate | discard",
      "confidence": 0.85,
      "reasoning": "string",
      "object_tags": ["technician", "service-van"]
    }
  ],
  "hero_recommendation": {
    "preferred_path": "photos-generated/hero-aspirational.jpg",
    "preferred_source": "generated | real",
    "fallback_path": "photos-raw/yelp-04.jpg",
    "reasoning": "string"
  },
  "icon_warnings": [
    {
      "current_data_lucide": "hammer",
      "html_path": "sites/<slug>/services.html",
      "service_context": "electrical-repair",
      "recommended": "zap",
      "reasoning": "string",
      "confidence": 0.9
    }
  ],
  "object_verification": [
    {
      "claim": "appliance-repair vertical",
      "evidence": "string",
      "confidence": 0.9
    }
  ],
  "review_coverage": {
    "captured_total": 5,
    "sources_present": ["google"],
    "sources_recommended_for_enrichment": ["yelp", "nextdoor"],
    "sufficiency": "sufficient | borderline | insufficient",
    "reasoning": "string"
  },
  "generated_images": [
    {
      "path": "photos-generated/hero-aspirational.jpg",
      "purpose": "hero | brand | service-card-bg | atmosphere",
      "prompt": "string",
      "model": "gpt-image-2",
      "model_revision": "string",
      "license_note": "Synthetic image. Do not represent as actual company work.",
      "intended_slot_context": "any-aspirational-OK | atmosphere-OK"
    }
  ]
}
```

### §11.9.8 — Budget addition

§11.7's budget caps gain one new field:

- `max_generated_images: 4` (default)

Bruce stops at the cap. Generation cost (gpt-image-2) counts against
`max_wall_clock_minutes` regardless of count.
```

---

## What I'll build immediately after Jesse ACKs §11.9

(No source-of-truth doc edits — these are scripts/templates only.)

1. `templates/bruce-asset-intel.template.md` + reference JSON schema file
2. `templates/collect-request.template.md` UPDATE — add required `Hero intent: aspirational | documentary | either` field + `Generated images allowed: yes | no | atmosphere-only` field
3. `scripts/pre-push-gate.sh` Check #7 — enforce data-source attribute + slot-context restrictions + alt-text constraints
4. `scripts/verify-build.sh` Check #7 — enforce 30% cap on generated `<img>` proportion
5. `scripts/consume-asset-intel.py` — reads `bruce-asset-intel.json`, routes:
   - icon warnings → file `messages/<date>-mini-to-r1vs-<slug>-icon-flag.md` (Mini-side runs this)
   - photo quality → log for human review (Mini-side at QA)
   - generated-image entries → validate license_note presence

These are R1VS-side tooling; no contract authority needed.

---

## What I need from Jesse

ONE OF:

1. **"ACK §11.9"** — proceed with HANDOFF-CONTRACT.md edit + the 5 follow-up implementation steps. I commit the contract change with a body referencing this proposal message.
2. **"ACK §11.9 with edits: <specific edits>"** — counter, I revise this proposal, you re-ACK.
3. **"Hold §11.9"** — defer. I sit on it.

Note: this is **separate** from any Bruce↔Mini direct-handoff amendment
in flight. They can ship in any order; nothing in §11.9 prevents Bruce
and Mini from also amending their direct-handoff protocol.

— R1VS
