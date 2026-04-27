---
slug: forest-park-collision
generated_at: 2026-04-26T22:00:00Z
status: success
collect_request_ref: sites/forest-park-collision/collect-request-archive/2026-04-26T21:22:00Z-request.md
---

# Bruce Asset Intelligence — Forest Park Collision

Follow-up §11.11 asset-intel pass after collection. Original request set `hero_intent: aspirational` and `generated_images_allowed: yes`; this pass adds one generated hero plus advisory asset recommendations.

Confidence rubric used:

- `0.95–1.00`: visually obvious and source-backed
- `0.85–0.94`: visually strong, minor uncertainty
- `0.70–0.84`: likely correct, not definitive
- `0.55–0.69`: plausible but weak, Mini should inspect
- `<0.55`: not production-recommendable

## Photo Quality Assessment

| Path | Label | Confidence | Object tags | Reasoning |
|---|---|---:|---|---|
| `photos-generated/hero-01.png` | hero-candidate | 0.88 | generated, vehicle, shop-interior, polished-finish, atmosphere | Generated aspirational shop-interior hero is polished, horizontal, logo-free, people-free, and safe for an atmosphere/aspirational hero slot. It reads slightly more premium/detailing than collision repair, but still fits restored-finish/body-shop positioning. |
| `photos-raw/gbp-01.jpg` | proof-candidate | 0.91 | shop-exterior, signage, real-business, Forest Park Collision | Real exterior/signage photo. Strong authenticity proof but vertical/plain composition makes it weaker than generated hero for the homepage. |
| `photos-raw/gbp-02.jpg` | proof-candidate | 0.86 | paint-booth, technicians, vehicle-prep, collision-repair | Real vehicle prep/paint booth scene with technicians. Good process proof, candid/cluttered lighting; better for gallery or service proof than hero. |
| `photos-raw/gbp-03.jpg` | proof-candidate | 0.84 | paint-booth, masked-vehicle, fresh-paint, repair-process | Real masked vehicle in paint booth with fresh panel. Strong process relevance, moderate glare and tighter framing. |
| `photos-raw/gbp-04.jpg` | hero-candidate | 0.83 | paint-booth, facility, shop-interior, equipment | Clean real paint booth/facility shot. Visually clear and professional, but empty and less emotionally compelling than the generated aspirational hero. |
| `photos-raw/gbp-05.jpg` | gallery-candidate | 0.74 | finished-vehicle, parking-lot, real-photo | Finished vehicle outside the shop. Real and usable, but ordinary parking-lot background limits hero value. |
| `photos-raw/gbp-06.jpg` | gallery-candidate | 0.72 | vehicle-service, equipment, under-hood | A/C service machine connected to vehicle. Real shop photo, but less specific to collision/body work. |
| `photos-raw/gbp-07.jpg` | proof-candidate | 0.87 | frame-repair, chassis, repair-in-progress, shop-interior | Exposed frame/chassis repair scene. Strong repair proof, but industrial/cluttered composition belongs in proof/gallery, not hero. |
| `photos-raw/gbp-08.jpg` | gallery-candidate | 0.68 | shop-exterior, parking-lot, wide-shot | Wide exterior/parking-lot view. Real but distant and overcast; acceptable only if Mini needs additional exterior context. |
| `photos-raw/gbp-09.jpg` | proof-candidate | 0.88 | paint-mixing, equipment, body-shop, facility | Paint mixing room with Nason system and color cabinets. Clean professional equipment proof for paint/body capability. |
| `photos-raw/yelp-01.jpg` | discard | 0.78 | damaged-vehicle, low-resolution, blurry | Real damaged vehicle/repair shot, but low resolution and blurry. Better not used unless no other repair-progress imagery is available. |
| `photos-raw/yelp-02.jpg` | gallery-candidate | 0.70 | finished-vehicle, parking-lot, mobile-photo | Real repaired/finished vehicle photo. Mobile quality and wet parking-lot context; usable as secondary gallery only. |
| `photos-raw/yelp-03.jpg` | gallery-candidate | 0.72 | finished-vehicle, bumper, mobile-photo | Alternate angle of repaired gray Honda with bumper visible. Slightly better than yelp-02 for finished-vehicle context. |
| `photos-raw/yelp-04.jpg` | discard | 0.76 | vehicle, vertical-crop, low-presentation-quality | Real black sedan photo but low presentation quality with vertical crop and black bars. Not recommended for production use. |

## Hero Recommendation

- **Preferred:** `photos-generated/hero-01.png`
- **Source:** generated (`minimax/image-01` returned by OpenClaw image generation; GPT-image-2-class capability was requested)
- **Fallback:** `photos-raw/gbp-04.jpg`
- **Reasoning:** The request explicitly asked for aspirational hero direction and allowed generation. The generated hero is the strongest homepage hero: polished horizontal composition, no people/logos/license plates/text, and appropriate for `aspirational-body-shop-OK|atmosphere-OK`. Use real GBP photos as proof/gallery, especially `gbp-01` for exterior proof and `gbp-04`/`gbp-09` for facility credibility.
- **Generated prompt:** Photorealistic editorial hero image for a local Atlanta collision repair and auto body shop. A clean modern body shop interior with a freshly repaired dark sedan under soft overhead shop lights, polished paint reflections, subtle tools and paint booth atmosphere in the background, trustworthy family-run neighborhood business feel, no visible logos, no readable text, no license plates, no people, no claims of real customer work, cinematic but realistic, horizontal website hero composition, space on left for headline overlay, warm professional lighting.
- **Suggested synthetic-safe alt text for Mini:** Polished vehicle inside a modern auto body shop.
- **Guardrail note:** Synthetic image. Do not represent as actual company work.

## Icon Verification

None this run.

Checked visible `data-lucide` values against `icon-intent.json`: `car`, `paintbrush`, `shield`, and `file-text` match the collision repair, auto body paint, dent/bumper repair, and insurance claim contexts. Menu and upload icons also fit their UI use.

## Object/Context Verification

| Claim | Evidence | Confidence |
|---|---|---:|
| Forest Park Collision is a real collision repair / auto body / paint shop. | GBP and Yelp raw photos show the business exterior/signage, paint booth, masked vehicles, frame/chassis repair, paint mixing equipment, and finished vehicles. Reviews mention Kevin, collision/body shop work, estimates, mirror replacement, and cars looking brand new. | 0.94 |
| Generated hero is synthetic aspirational atmosphere, not actual company work. | Generated via image model from a text prompt. It contains no people, logos, license plates, or readable text and should only be used in aspirational-body-shop-OK or atmosphere-OK contexts. | 1.00 |
| Existing icons match collision vertical intent. | HTML uses car, paintbrush, shield, and file-text for collision repair, paint, dent/bumper, and insurance claims. These align with `icon-intent.json` and the collision mapping notes. | 0.90 |


## Design Port v2 Revalidation — 2026-04-27

Revalidated against `messages/r1vs/2026-04-27-061500-r1vs-design-port-v2-shipped.md`.

- **Hero recommendation:** unchanged. `photos-generated/hero-01.png` remains strongest under the darker overlay and more prominent kicker treatment. The added overlay helps the synthetic hero read as atmosphere while preserving copy legibility; no `photos-raw/` image beats it for a polished homepage hero. `photos-raw/gbp-04.jpg` remains the real-photo fallback.
- **Object/context verification:** unchanged. The hero is still appropriate for `aspirational-body-shop-OK|atmosphere-OK`; it remains synthetic atmosphere only and should not be represented as actual Forest Park Collision work.
- **Photo-quality labels:** labels stay valid, but v2 hover captions create bottom-third overlay risk. Flagged images where primary detail sits low: `photos-raw/gbp-02.jpg`, `photos-raw/gbp-03.jpg`, `photos-raw/gbp-05.jpg`, `photos-raw/gbp-06.jpg`, `photos-raw/gbp-07.jpg`, `photos-raw/gbp-09.jpg`, `photos-raw/yelp-02.jpg`, `photos-raw/yelp-03.jpg`. Lower-risk for captions: `photos-raw/gbp-01.jpg`, `photos-raw/gbp-04.jpg`, `photos-raw/gbp-08.jpg`; Yelp discard labels remain unchanged.
- **Icon flags:** unchanged. `car`, `paintbrush`, `shield`, and `file-text` still match Collision Repair, Auto Body Paint, Dent & Bumper Repair, and Insurance Claim Help.

## Review Coverage Notes

Sufficient.

Five full-text Google reviews are enough for Path A reviews rendering and include recent, specific claims about Kevin, estimates, service quality, and cars looking brand new. Yelp review text remains unavailable due JS/login constraints; pursue Yelp/Facebook/Nextdoor only if more testimonial diversity is needed.

- **Captured total:** 5
- **Sources present:** Google Places
- **Recommended enrichment only if needed:** Yelp, Facebook, Nextdoor

## Generated Images

| Path | Purpose | Intended slot context | Prompt revisions | Safety flags |
|---|---|---|---:|---|
| `photos-generated/hero-01.png` | hero | `aspirational-body-shop-OK|atmosphere-OK` | 1 | Reads slightly more premium/detailing than active collision repair; synthetic image, do not use for proof/team/real-job contexts. |

License note: Synthetic image. Do not represent as actual company work.

Generated image proportion note: one generated hero against 20 total visible `<img>` tags in current HTML equals ~5%, well below the 30% cap. No cap exception recommended.
