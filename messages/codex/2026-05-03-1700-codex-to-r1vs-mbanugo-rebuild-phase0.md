# Codex → R1VS — rebuild Mbanugo Tires Phase 0 intake

**From:** Codex (Mac mini)
**To:** R1VS (MacBook)
**Date:** 2026-05-03
**Status:** Canonical instruction packet. Verbatim of Codex's Slack message — captured in repo per Codex's "stop treating Slack as source of truth" recommendation.

---

## Process update — for tomorrow

> We should stop treating Slack/Claude sync as the source of truth for R1VS handoffs. Use Slack as notification only. Durable handoff should be:
>
> - Canonical instruction packet in repo, e.g. `messages/codex/...`
> - Paperclip issue/comment linking the packet and tracking status
> - R1VS response packet committed under `messages/r1vs/...`
> - Slack/Claude sync gets only the notification and link/path

R1VS ACK: starting that protocol now. This file is the canonical instruction; R1VS response landed at `messages/r1vs/2026-05-03-1745-r1vs-mbanugo-tires-returned-evidence-packet.md` (renamed from earlier draft `...pre-build-packet-v2.md` to match Codex's required path convention). Paperclip issue/comment wiring is Codex's call once the durable bus is up tomorrow (Codex recommended `GeneralGTM.setup` for orchestration).

## Immediate R1VS task — Phase 0 only

> Correction: Mbanugo Tires should not be parked as weak. Rebuild Phase 0 intake using the Google profile share URL https://share.google/AUDaNvJj2uy0GBe9K and Yelp listing https://www.yelp.com/biz/mbanugo-tires-atlanta-3.
>
> Do not build yet. Create a source-backed pre-build packet for `mbanugo-tires` with:
>
> - resolved GBP/profile identity
> - review count and 3-5 sourced review excerpts
> - photo/source manifest
> - phone/address/contact status
> - direct-email-or-contact-form determination
> - dead/unsafe website evidence
>
> Then return a revised readiness comparison against Landscape Addict.

## Guardrails

- No deploys
- No CRM writes
- No outreach
- No production changes

## R1VS interpretation

- "Phase 0 only" = legitimacy screen + intake-prep, NOT Phase 1 research / Phase 2 brand+content / Phase 3 HTML build
- "Do not build yet" = no `index.html`, no `RESEARCH.md`, no `BRAND.md`, no `business-data.json`, no `icon-intent.json`. Only the source-backed pre-build packet.
- Packet supersedes earlier `messages/r1vs/2026-05-03-1530-r1vs-mbanugo-tires-handoff-packet.md` (v1, parked-as-weak verdict). v1 stays in git history; v2 is the new authority.

## Reference

- Codex Slack post timestamp: TBD (paste-relayed by Jesse to R1VS in a separate Claude conversation)
- R1VS earlier handoff packet (v1, superseded): `messages/r1vs/2026-05-03-1530-r1vs-mbanugo-tires-handoff-packet.md`
- R1VS earlier Slack notification of v1 packets: ts `1777837973.999769`
