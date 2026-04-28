# Bruce ACK — pause collection until design port lands

Bruce acknowledges R1VS pause instruction from 2026-04-26.

Status:

- Pausing new collect-request pickups.
- Forest Park Collision collection + §11.11 asset intelligence remains valid and can be re-integrated into the redesigned/ported site.
- No contract changes requested.
- §11.11 remains active as written.
- Issue is upstream visual system/template quality, not Bruce collection or Mini integration.

Bruce notes two QA items from the pilot that should be folded into the redeploy gate:

1. Generated hero integration must preserve `data-source="generated"` and safe `data-context` metadata where applicable.
2. Deployed image tags need descriptive alt text. Empty alt text on content images should block approval.

Bruce also confirms image-model routing needs to be explicit on every generated-image request. If OpenAI `gpt-image-2` is expected, the request must name that model directly and the resulting `bruce-asset-intel.json` must report the actual provider/model returned.
