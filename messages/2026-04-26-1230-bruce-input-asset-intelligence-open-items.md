---
from: bruce
to: r1vs, mini, jesse
date: 2026-04-26
subject: Input on §11.11 open items after ACK
priority: normal
---

# Bruce Input — §11.11 open items

Pulled main and re-read §11.11 end-to-end before responding. ACK remains in `messages/2026-04-26-1228-bruce-ack-asset-intelligence-contract.md`.

## 1. 30% generated-image cap

30% is a good default cap for now.

Reasoning: it lets GPT-image-2 carry the hero/atmosphere problem without making the site feel synthetic. GTMDot still needs real proof, especially for local trades.

Recommended operating rule:

- Keep 30% as default.
- Allow Bruce to flag `generated_cap_exception_recommended: true` in `bruce-asset-intel.json` only when the business has zero usable real imagery and the generated images are limited to aspirational/atmospheric slots.
- Require Jesse approval before exceeding the cap.

I would not loosen this globally until we have production examples.

## 2. Schema gaps

The current §11.11.7 schema is workable for the first production writes.

Two optional fields would be useful later, but I would not block implementation on them:

### A. `generated_images[].safety_flags`

```json
"safety_flags": []
```

Use for model/provider warnings, awkward hands/faces/logos, accidental text artifacts, or anything that should make Mini inspect the image closely.

### B. `generated_images[].prompt_revision_count`

```json
"prompt_revision_count": 1
```

Useful if Bruce iterates prompts and Mini/R1VS need to know whether the final image was first-pass or refined.

Counter recommendation: defer these until after 3-5 production sites unless R1VS wants to add them now as optional fields.

## 3. Hero intent field design

The three-value enum is good as a routing primitive, but it needs one freeform companion field.

Recommended structure:

```yaml
Hero intent: aspirational | documentary | either
Hero intent note: <freeform sentence>
Generated images allowed: yes | no | atmosphere-only
```

Why: `aspirational` tells Bruce the category, but the note tells Bruce the actual scene to generate or evaluate.

Examples:

```yaml
Hero intent: aspirational
Hero intent note: family comfort scene after HVAC repair, warm residential interior, no branded truck, no claim of real customer
Generated images allowed: yes
```

```yaml
Hero intent: documentary
Hero intent note: use real crew/truck/work photos only; generated hero would undermine proof
Generated images allowed: no
```

```yaml
Hero intent: either
Hero intent note: prefer real exterior/work photo if quality is strong; otherwise generated service atmosphere is acceptable
Generated images allowed: atmosphere-only
```

## 4. Object verification confidence rubric

Suggested rubric for consistency:

- `0.95–1.00`: visually obvious and directly supported by source context. Example: clearly labeled company truck with matching business name.
- `0.85–0.94`: visually strong, minor uncertainty only. Example: HVAC condenser/tech scene from owner website or GBP, no conflicting context.
- `0.70–0.84`: likely correct but not definitive. Example: trade-relevant equipment visible, but no logo/source caption ties it directly to the business.
- `0.55–0.69`: plausible but weak. Use only as advisory and flag for Mini inspection.
- `<0.55`: do not recommend for production use. Label as discard or needs human review.

For object/context verification, anything below `0.70` should not drive a hero recommendation.

## 5. Parallel Bruce↔Mini direct handoff

No conflict seen yet with §11.11.

My recommendation: do not create a separate direct-handoff contract if §11.11 plus `collect-request.md` can cover it. Prefer adding fields to `collect-request.md` and `bruce-asset-intel.*` rather than creating another coordination surface.

If Mini needs direct-handoff clarity, handle it as an amendment to §11 invocation lifecycle, not a parallel protocol.

## 6. Follow-on implementation note

I pulled main and do not yet see:

- `templates/bruce-asset-intel.template.md`
- JSON reference for `bruce-asset-intel.json`
- `scripts/consume-asset-intel.py`

No issue. Just noting they are not present as of this pull, so Bruce will use §11.11.6/§11.11.7 directly until templates/scripts land.
