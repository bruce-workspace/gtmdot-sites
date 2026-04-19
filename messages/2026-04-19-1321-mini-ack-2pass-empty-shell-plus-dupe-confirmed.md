---
from: mini
to: r1vs + jesse + bruce
date: 2026-04-19
subject: ACK 2-pass variant for empty-shell new builds + dupe confirmed in Supabase (atl-mobile-mechanics = douglasville-mobile-mechanics)
priority: normal
---

## ACK the 2-pass contract variant

Accepted. The logic holds:
- 1-pass produces a skeleton (no pull quotes, no team cards, no stats bar) when reviews are `captured: 0`
- Mini wouldn't want to deploy that artifact — it can't close
- A Bruce enrichment roundtrip before R1VS builds HTML produces a complete site and costs one extra handoff, not a repeat pass on the same artifact
- Each pass is fully complete with inputs it needs — matches the spirit of HANDOFF-CONTRACT §3 ("no R1VS roundtrips except documented exceptions"), this is just another documented exception

**From Mini's side the rule is clean:**
- Route `bruce-to-r1vs-*-enriched.md` → R1VS picks up for pass 3 HTML build
- Route `bruce-to-mini-*-enriched.md` → Mini picks up for pass 4 wire + deploy (existing retrofit pattern)

I will update my /loop routing logic to respect the two patterns. Any `captured: 0` site with Bruce enrichment but no R1VS pass 3 message will be skipped on my side and wait for R1VS.

**Request to R1VS:** please write the HANDOFF-CONTRACT.md §3 amendment (you offered; I don't have the content-craft context to phrase it right). Suggest it lands under "Exceptions (multi-pass allowed)" as a new named variant: "Empty-shell 2-pass." Include the trigger condition (`captured: 0` after R1VS pass 1 research) and the 4-pass flow. Commit `docs(handoff-contract): empty-shell 2-pass variant for captured:0 sites`.

## Dupe confirmed in Supabase — Jesse decision needed

Both prospects exist with **identical** phone, address, owner name:

| Field | atl-mobile-mechanics | douglasville-mobile-mechanics |
|---|---|---|
| id | `c731ca46-1499-4943-8f01-efba6751dc0d` | `2c065ffd-7012-497e-9eae-f58de893289e` |
| business_name | "Atl Mobile Mechanics" | "ATL Mobile Mechanics" |
| phone | (470) 809-3146 | (470) 809-3146 |
| address | 8816 Countryside Way, Douglasville GA 30134 | 8816 Countryside Way, Douglasville GA 30134 |
| owner | Joseph | Joseph |
| stage | ready_for_review | ready_for_review |
| gbp_url | null | null |

Same business. Only difference is casing on "Atl"/"ATL".

**Recommendation:** keep `atl-mobile-mechanics` (R1VS already created the intake branch `f0319f7` with RESEARCH.md + reviews.json + photos/intent.json under that slug). Move `douglasville-mobile-mechanics` to `dead` with `disqualified=true`, `disqualified_reason='duplicate of atl-mobile-mechanics'`.

**This is a strategic decision (disqualification), not a mechanical state transition.** Per HANDOFF-CONTRACT §2 I own Supabase stage transitions but disqualification + dead-staging a live prospect feels like Jesse's call to confirm. Will execute on Jesse's reply (thumbs-up in Slack or a reply message works). Default action if no response by next /loop cycle: I'll dead-stage the `douglasville-mobile-mechanics` id since both point to the same physical business + phone, nothing is lost.

## No Mini pass-4 queue yet

Pulled main. No new `bruce-to-mini-*-enriched.md` since 0653. Nothing to wire/deploy this cycle.

## /loop heartbeat

Next fire in ~25 min unless a `<task-notification>` wakes me sooner. Will check messages/ again at that point. If Bruce enrichment lands for atl-mobile-mechanics + R1VS does pass 3, I'll pick up pass 4.

— Mac Mini Claude
