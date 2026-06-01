# Outreach Channel Truth And Decision Queue

Date: 2026-05-23
Lane: Outreach Operations
Source files: `2026-05-23-away-mode-coordinator-roadmap.md`, `status/quarterback-latest.md`, public CRM read-only API, Poplar read-only API

## Summary

Harrison's postcard retry is verified as successful in CRM and Poplar. The next Outreach decision queue should not be "send more"; it should be "record channel truth, decide follow-up risk, and prepare approval packets."

No sends, CRM writes, Paperclip mutations, deploys, prospect contact, or git pushes were performed.

## 1. Harrison Postcard State

Prospect: `harrison-sons-electrical`  
Business: Harrison & Sons Electrical Service LLC  
CRM stage: `outreach_sent`  
Email: none on file  
Postcard event: `submitted`  
CRM postcard event ID: `d88d72c3-2522-4f23-a7c3-14ec10c69abb`  
Poplar order ID: `65ccdec7-5ad9-4b5a-aa6b-3d7eabdda916`  
CRM event time: `2026-05-23T02:57:10.741021+00:00`  
Poplar created time: `2026-05-23T02:57:10Z`  
Provider state: `production`  
Expected delivery: `2026-05-30`  
Provider cost: `$0.92`  

Provider-normalized address:

```text
Current Resident
3695 CASCADE RD SW
6250
ATLANTA, GA 30331
```

Postcard merge tags confirmed:

```text
business_name: Harrison &amp; Sons Electrical Service LLC
claim_code: HARR2423
preview_site_url: https://harrison-sons-electrical.pages.dev?utm_source=postcard&utm_medium=direct_mail&utm_campaign=gtmdot
desktop_screenshot_url: https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-desktop.jpg
mobile_screenshot_url: https://gtmdot-postcards.pages.dev/screenshots/harrison-sons-electrical-mobile.jpg
hero_image_url: https://gtmdot-postcards.pages.dev/harrison-sons-electrical-hero.jpg
```

Decision: no further Harrison send action is needed right now. Track provider progression from `production` to mailed/delivered when Poplar exposes it.

## 2. Important CRM Mismatch

The public prospect detail endpoint returns raw `prospect.postcardStatus: "not_submitted"` for Harrison, even while the same detail response includes the submitted postcard event. The list endpoint derives Harrison as `postcardStatus: "submitted"`.

Diagnosis from local code:

- `/src/app/api/prospects/route.ts` derives postcard status from `outreachEvents`.
- `/src/app/api/prospects/[id]/route.ts` returns raw `prospect` plus `outreachEvents` and does not derive `postcardStatus`.

Safe fix proposal: make the detail endpoint derive and return the same `postcardStatus`, `emailsSentCount`, and `nextAction` fields as the list endpoint, ideally through a shared helper to avoid future drift.

## 3. InTire Decision Packet

Prospect: `intire-mobile-tire-shop`  
Business: InTire Mobile Tire Shop  
CRM stage: `outreach_sent`  
Postcard: submitted, order ID `26b0cd0f-3a07-4101-8d6d-cfd629cc55ae`  
Email 1: sent and delivered  
Email 2: sent and delivered  
Next email: sequence 3 scheduled at `2026-05-25T17:00:03.814+00:00`  
Sequence paused: `false`  
Reply monitoring: not proven end-to-end  

Recommendation: main coordinator should ask Jesse one explicit remote-week question:

```text
Approved: InTire follow-up policy while I am remote.

Choose one:
1. Let the scheduled Email 3 send on May 25, accepting manual reply-monitoring risk.
2. Pause InTire follow-ups until hello@gtmdot.com reply monitoring and pause-on-reply are proven.

Still prohibited unless separately approved:
new sends outside this sequence decision, CRM edits beyond the pause/continue decision, Paperclip mutations, deploys, prospect contact, SMS, Poplar sends, git push, DNS/domain/hosting/billing, and Stripe actions.
```

## 4. QA-Approved Send-Readiness Queue

These are not approved sends. They are the next candidates for send-readiness packets.

| Prospect | Stage | Email | Postcard payload preview | Asset URL checks | Outreach recommendation |
| --- | --- | --- | --- | --- | --- |
| `smartwire-solutions` | `qa_approved` | none | valid | desktop/mobile/hero all HTTP 200 | postcard-only packet; note stale open QA note says old 403/no site, likely stale against current QA-approved state |
| `cityboys` | `qa_approved` | `info@cityboysrus.com` | valid | desktop/mobile/hero all HTTP 200 | packet for postcard + possible Email 1; open notes include stale/old concerns and data hygiene issue (`General Services` vs appliance repair) |
| `dream-steam` | `qa_approved` | none | valid | desktop/mobile/hero all HTTP 200 | postcard-only packet |
| `handy-dandy-atlanta` | `qa_approved` | none | valid | desktop/mobile/hero all HTTP 200 | postcard-only packet |
| `piedmont-tires` | `qa_approved` | none | blocked | not checked in this pass | repair packet first: ZIP missing, payload preview returns missing mailing address fields |

Payload preview findings:

- SmartWire recipient: Terry Henry, `730 Peachtree St NE, Ste 570`, Atlanta GA 30308.
- City Boys recipient: Curtis, `3348 Peachtree Rd NE #700, Atlanta GA 30326`.
- Dream Steam recipient: Reuben, `2250 N Druid Hills Rd Ste 265, Atlanta GA 30329`.
- Handy Dandy recipient: Ruslan, `296 Possum Trot Rd, Barnesville GA 30204`.
- Piedmont Tires blocked: missing `zip`.

## 5. Reply-Monitoring Acceptance Criteria

Before scaling email follow-ups, Outreach and Platform should prove:

1. Canonical reply-to for GTMDot outreach is `hello@gtmdot.com`.
2. A controlled internal reply to a GTMDot outreach message lands in an accessible monitored inbox/path.
3. The reply creates a durable CRM/provider event equivalent to `email/replied`.
4. The related prospect's sequence pauses automatically on reply.
5. A human-facing queue shows replied prospects before any later follow-up can send.
6. Hard bounces suppress future email sends for that address.
7. The UI distinguishes postcard state, email state, bounce state, reply state, and CRM stage.

## Recommended Next 3 Actions

1. Coordinator records Harrison as postcard submitted/provider `production`, expected delivery `2026-05-30`, no further Harrison send action.
2. Coordinator asks Jesse the InTire follow-up policy question before Email 3 on May 25.
3. Outreach prepares full send packets for SmartWire, City Boys, Dream Steam, and Handy Dandy, and a repair packet for Piedmont ZIP.
