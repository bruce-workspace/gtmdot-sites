---
slug: forest-park-collision
generated_at: 2026-04-28T04:53:00Z
status: success
collect_request_ref: sites/forest-park-collision/collect-request.md
---

# Bruce Asset Intelligence — Forest Park Collision

## Photo Quality Assessment

### GBP photos (photos-raw/gbp-02.jpg through gbp-10.jpg)
All from Google's Places API — real, attributable photos from Forest Park Collision's Google Business Profile. Confidence: 0.95.

| File | Label | Confidence | Reasoning |
|---|---|---|---|
| `gbp-02.jpg` | `gallery-candidate` | 0.9 | Shop exterior — solid proof shot |
| `gbp-03.jpg` | `gallery-candidate` | 0.88 | Vehicle on lift — work-in-progress signal |
| `gbp-04.jpg` | `gallery-candidate` | 0.88 | Vehicle receiving work — real shop environment |
| `gbp-05.jpg` | `proof-candidate` | 0.92 | Clean vehicle, good lighting — quality result shot |
| `gbp-06.jpg` | `gallery-candidate` | 0.85 | Another vehicle, similar context |
| `gbp-07.jpg` | `gallery-candidate` | 0.87 | Body work in progress |
| `gbp-08.jpg` | `gallery-candidate` | 0.86 | Interior/shop environment |
| `gbp-09.jpg` | `gallery-candidate` | 0.85 | Vehicle, context unclear |
| `gbp-10.jpg` | `gallery-candidate` | 0.88 | Vehicle with what looks like fresh paint/clear coat |

### Yelp photos (photos-raw/yelp-05.jpg through yelp-08.jpg)
Downloaded from Yelp's public listing. Consistent style with GBP — real vehicles, professional results. Confidence: 0.90.

### Generated images (photos-generated/)
No real photos in these slots — these are aspirational/atmospheric fills per §11.11.5 guardrail 2.

---

## Hero Recommendation

**Recommended:** `photos-generated/hero-aspirational-01.png`

Reasoning:
- `hero_intent: aspirational` in the request calls for "a clean, editorial composition... freshly painted vehicle reflecting shop lighting, OR an aspirational shop-exterior shot."
- The generated image delivers this: a glossy black SUV under dramatic overhead lighting, clean shop environment, cinematic quality.
- GBP photo `gbp-05.jpg` is the fallback real photo if Mini QA prefers documentary over aspirational — it shows a real completed vehicle and reads as trustworthy proof.
- No `team-OK`, `owner-portrait-OK`, or `real-job-OK` real photos available that would replace the generated hero, so generation is the right call here.

Generated image license note (per §11.11.5 guardrail 4): "Synthetic image. Do not represent as actual company work."

---

## Icon Verification

No HTML files modified. No `icon-intent.json` changes made per §11.11.4 routing rule. No icon mismatches detected in R1VS-built files at time of this run (R1VS already applied correct icons per ICON-MAPPING.md for collision repair).

Flag routing: If Mini detects icon mismatches during QA, file `messages/*-mini-to-r1vs-*-icon-flag.md` per §11.11.4.

---

## Object/Context Verification

- GBP and Yelp photos consistently show collision repair environment: vehicles on lifts, body work in progress, clean shop floors.
- No appliance-store imagery or stock truck photos detected.
- All photo sources consistent with `collision-repair` vertical.

---

## Review Coverage Notes

**Status:** Borderline → Sufficient

| Metric | Value |
|---|---|
| Total captured | 8 |
| Sources | Google (5) + Yelp (3) |
| Named reviewers | 7 of 8 (Oz K. is close to named) |
| Cross-source signal | Kevin (owner) referenced by name in 3/8 reviews |

Recommendation: Sufficient for build. Mini can proceed with reviews.json merge. If Jesse wants more named reviews, a follow-up `collect-request.md` targeting Nextdoor (with login) or BBB would be the next enrichment path.

---

## Generated Images

| File | Purpose | Intended Slot Context | License Note |
|---|---|---|---|
| `hero-aspirational-01.png` | hero | `aspirational-OK | atmosphere-OK` | "Synthetic image. Do not represent as actual company work." |
| `service-card-bg-01.png` | service-card-bg | `atmosphere-OK` | "Synthetic image. Do not represent as actual company work." |
| `service-card-bg-02.png` | service-card-bg | `atmosphere-OK` | "Synthetic image. Do not represent as actual company work." |
| `service-card-bg-03.png` | service-card-bg | `atmosphere-OK` | "Synthetic image. Do not represent as actual company work." |

Per §11.11.5 guardrail 5: 4 generated images / 17 total visible images = 23.5% — below 30% threshold. OK.