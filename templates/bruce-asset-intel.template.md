---
slug: REPLACE_ME_SLUG
generated_at: REPLACE_ME_ISO_TIMESTAMP
status: success | partial | failed
collect_request_ref: REPLACE_ME_PATH_TO_TRIGGERING_collect-request.md
---

# Bruce Asset Intelligence — REPLACE_ME_BUSINESS_NAME

Drop-in template per HANDOFF-CONTRACT.md §11.11.6. Bruce writes this as a
companion to `bruce-asset-intel.json` whenever §11.11 capabilities are
exercised. Mini consumes it during QA (with `scripts/consume-asset-intel.py`
parsing the JSON and surfacing flags from this MD).

Sections below are required, in this order. If a section has nothing to
report, write "None this run." rather than removing the heading.

---

## Photo Quality Assessment

Per-photo labels with reasoning. One row per assessed image.

| Path | Label | Confidence | Object tags | Reasoning |
|---|---|---|---|---|
| `photos-raw/yelp-01.jpg` | hero-candidate | 0.85 | technician, service-van, residential-driveway | Sharp, well-lit, shows real fleet vehicle in customer context. Could anchor the homepage. |
| `photos-raw/yelp-02.jpg` | gallery-candidate | 0.7 | tools, equipment | OK quality, narrow context. Use for service-cards or recent-work grid. |
| `photos-raw/gbp-04.jpg` | discard | 0.9 | logo-watermark, low-resolution | Heavy watermark + < 800px wide. Not usable. |

Labels: `hero-candidate`, `proof-candidate`, `gallery-candidate`, `discard`.

## Hero Recommendation

Single recommendation. State whether real or generated, the path, and the reasoning Mini needs to default-accept (per §11.11.3).

- **Preferred:** `photos-generated/hero-aspirational.jpg`
- **Source:** generated (gpt-image-2)
- **Fallback:** `photos-raw/yelp-01.jpg` (real, hero-candidate, confidence 0.85)
- **Reasoning:** GBP photos are documentary (truck-in-driveway, panel-close-up) and don't carry the aspirational tone the homepage hero needs. Generated image targets the brand atmosphere from the design system: "modern, trustworthy, not loud." Fallback is usable if Mini overrides.
- **Generated prompt** (if applicable): `<the literal prompt sent to gpt-image-2>`

## Icon Verification

Mismatches between current `data-lucide` values in the site HTML and the business context. Bruce flags only — R1VS owns the fix per §11.11.4.

| HTML file | Current icon | Service context | Recommended | Confidence | Reasoning |
|---|---|---|---|---|---|
| `services.html` | hammer | electrical-repair | zap | 0.9 | Generic-tool icon doesn't match electrical vertical. Per ICON-MAPPING.md, electrical = zap. |

If none, write "None this run."

## Object/Context Verification

Confirms photos depict the claimed business, not unrelated imagery (the Samsung-vs-monitor failure mode from prior Bruce era).

| Claim | Evidence | Confidence |
|---|---|---|
| HVAC vertical | photos-raw/yelp-01.jpg through yelp-05.jpg show real condenser units, ductwork, and branded service van. No appliance-store or computer-monitor imagery detected. | 0.95 |

## Review Coverage Notes

Sufficiency of review capture against the site's display needs.

- **Captured total:** 5
- **Sources present:** google
- **Sources recommended for enrichment:** yelp, nextdoor
- **Sufficiency:** sufficient | borderline | insufficient
- **Reasoning:** 5 verbatim Google reviews clears the captured>=3 threshold for full reviews-track rendering. Yelp listing exists with 12 reviews unscraped — recommend a follow-up `collect-request.md` if Mini wants richer cross-source signal before postcard send.

## Generated Images

List every file Bruce wrote to `photos-generated/`. Include purpose, prompt, intended slot context, license note (mirrors JSON entry).

| Path | Purpose | Intended slot context | Prompt summary |
|---|---|---|---|
| `photos-generated/hero-aspirational.jpg` | hero | `any-aspirational-OK\|atmosphere-OK` | "Modern HVAC service in residential setting, warm afternoon light, technician carrying tools toward customer home, no faces visible. Photoreal, editorial composition." |

All entries carry the canonical `license_note` ("Synthetic image. Do not represent as actual company work.") in the corresponding JSON record per §11.11.5 guardrail 4.

If none, write "None this run."

---

*Schema: HANDOFF-CONTRACT.md §11.11.6. Companion JSON at `bruce-asset-intel.json` per §11.11.7.*
