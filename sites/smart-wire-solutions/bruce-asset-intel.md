---
slug: smart-wire-solutions
generated_at: 2026-04-28T15:58:48Z
status: partial_success
collect_type: Bruce §11.11 asset-intel pass
---

# Bruce Asset Intelligence — SmartWire Solutions

## Result

Asset pass complete. OpenAI `gpt-image-2` is now the preferred hero-generation path for this SmartWire handoff; Google image generation was attempted first only because that was the prior plan, and it was blocked by the project monthly spend cap. Google KP confirms 5.0★ across 17 reviews, but direct Place Details via `cid:4706905946096216564` returned `INVALID_REQUEST` from Bruce's runtime, so I captured real verbatim secondary recommendations and left the Google-verbatim gap explicit.

## Hero Recommendation

**Preferred:** `photos-generated/hero-01.png`

Generated editorial residential-electrician hero: panel/tools, warm residential light, no people, no logos, no text requested. Mini should visually QA it during integration, but it is the best hero candidate. Real photos are owner-controlled proof/service photos, not hero-grade.

**Fallback:** `photos-raw/alignable-service-01.jpg` only if generated hero is rejected. It is real/owner-controlled but too service-specific and compressed for hero.

## Real Photos Pulled

Source: SmartWire Alignable profile and service pages. These are owner-controlled public assets.

- `photos-raw/alignable-service-01.jpg` — **proof-candidate**, electrical repair/troubleshooting. Strongest real service proof.
- `photos-raw/alignable-service-02.jpg` — **gallery-candidate**, ceiling fan installation. Direct service match.
- `photos-raw/alignable-service-03.jpg` — **gallery-candidate**, recessed lighting. Direct service match.
- `photos-raw/alignable-service-04.jpg` — **gallery-candidate**, electrical panel upgrade. Use carefully: it proves panel work, but R1VS did not make panel upgrades a primary service page.
- `photos-raw/alignable-service-05.jpg` / `06.jpg` — extra gallery candidates, lower confidence, compressed.
- `photos-raw/alignable-brand-01.jpg` / `02.jpg` / `03.jpg` — logo/business-card references only; avoid gallery use because of text/design artifacts.

## Reviews

`reviews.json` now contains 3 real verbatim secondary recommendations plus the verified Google aggregate rating/count.

Use caution: these are **not Google review verbatims**. Google aggregate is verified at 5.0★ / 17, but Google review text still needs direct browser extraction if Jesse wants Path A specifically labeled as Google reviews.

Captured quotes:

1. Dr. Troye Washington-Clanton, Alignable: “Experienced and knowledgeable, prompt and hard working. Terry Henry @ SmartWire Solutions LLC can fix your electrical problem when all other can’t!”
2. LinkedIn snippet: “Terry has great work ethics, integrity, and gives great customer service. I have known him for 10+ years, and he is the only electrician I would hire, or recommend.”
3. LinkedIn snippet: “Over the last ten years I have hired Terry for any and all electrical needs. He has done everything from rewiring houses to trouble shooting small electrical problems. I have found him to be fast accurate and very fair with his pricing.”

## Mini Integration Notes

- Use `photos-generated/hero-01.png` for hero with `data-source="generated"`.
- Use Alignable service images as gallery/service proof, not as claims of Google photos.
- Keep Google review count/rating visible, but don't label the three verbatim quotes as Google reviews unless Mini extracts true Google review text later.
- If Mini can access the Google share URL interactively, try extracting Google reviews directly from `https://share.google/odJwB0uvcD08lbYxb` before final deploy.
- Apply electrician photo filter: `brightness(0.85) contrast(1.08) saturate(0.85)` plus dark overlays where text/captions sit on images.

## Blockers / Caveats

- OpenAI `gpt-image-2` hero is preferred going forward. Google Image Gen 2/3 failed due monthly spending cap: `RESOURCE_EXHAUSTED`, but no replacement is needed unless Jesse dislikes the OpenAI hero.
- Google Place Details lookup by `cid:<decimal>` failed from Bruce runtime even though KP confirms the listing. SAB/KP path remains brittle.
- Browser navigation to Google share URL is blocked by Bruce runtime policy, so Google verbatim review extraction needs Mini/browser or a patched collector.
