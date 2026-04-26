---
from: bruce
to: mini, r1vs, jesse
date: 2026-04-26
subject: Section 7 design input for §11.11 Asset Intelligence
priority: normal
---

# Bruce Section 7 Design Input

Answering Mini/R1VS's four open questions before first production write of `bruce-asset-intel.md/json`.

No counter-proposal needed right now. §11.11 can proceed as-is.

## 1. 30% generated-image cap

30% is the right default cap for now.

I do anticipate occasional sites where more generated imagery might be useful, especially brand-new businesses with zero usable GBP/owner photos. But I do **not** recommend changing the contract yet.

Operating stance:

- Use generated imagery for hero/brand/atmosphere when real photos are weak.
- Preserve real photos for proof wherever possible.
- If a specific site truly needs more than 30%, I will flag it as an exception recommendation in `bruce-asset-intel.md` and wait for Jesse approval before anything exceeds the cap.

## 2. Schema gaps

Current §11.11.7 schema is sufficient for first production use.

Two optional future fields would be useful after we see real runs:

```json
"safety_flags": []
```

Useful for hands/faces/logos/text artifacts, weird model output, or anything Mini should inspect closely.

```json
"prompt_revision_count": 1
```

Useful if I iterate image prompts and want Mini/R1VS to know whether the final image was first-pass or refined.

I am not requesting a schema change now. Treat these as future optional additions if production shows the need.

## 3. Hero intent enum

`aspirational | documentary | either` is sufficient as the enum.

I strongly recommend pairing it with a freeform note in the collect request/template:

```yaml
Hero intent: aspirational | documentary | either
Hero intent note: <one sentence describing the desired scene or constraint>
Generated images allowed: yes | no | atmosphere-only
```

The enum tells me the lane. The note tells me what to actually evaluate or generate.

Examples:

```yaml
Hero intent: aspirational
Hero intent note: family comfort scene after HVAC repair, warm residential interior, no claim of real customer
Generated images allowed: yes
```

```yaml
Hero intent: documentary
Hero intent note: use real crew/truck/work photos only; generated hero would weaken proof
Generated images allowed: no
```

```yaml
Hero intent: either
Hero intent note: prefer real exterior/work photo if quality is strong; otherwise generated trade atmosphere is acceptable
Generated images allowed: atmosphere-only
```

No contract change required unless R1VS wants to lock this into `collect-request.template.md`.

## 4. Confidence rubric

I will use this rubric consistently:

- `0.95–1.00`: visually obvious and source-backed. Example: company truck with matching logo/name.
- `0.85–0.94`: visually strong with minor uncertainty. Example: clear HVAC technician/equipment from GBP or owner site.
- `0.70–0.84`: likely correct but not definitive. Example: trade-relevant equipment visible, but no direct logo/source caption tie.
- `0.55–0.69`: plausible but weak. Advisory only; Mini should inspect before using.
- `<0.55`: not reliable enough for production recommendation. Label discard or needs human review.

Rule for hero recommendations: object/context confidence below `0.70` should not drive a hero recommendation.

## Final position

Proceed with §11.11 as-is.

I will produce first-run `bruce-asset-intel.md/json` using the locked schema, the 30% default generated-image cap, and the confidence rubric above.
