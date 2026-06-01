---
from: codex
to: jesse
date: 2026-05-16
type: audit
subject: GTMDot re-entry board audit and channel-state split
---

# GTMDot Re-Entry Board Audit

Codex resumed active GTMDot execution ownership after the Mini -> Codex handoff.
This is a read-only board snapshot, not a stage move, approval, deploy, send, or
CRM mutation.

## Snapshot

Source: CRM API, read-only.

Total CRM records: 67.

Active operating board:

- outreach_sent: 13
- outreach_staged: 2
- qa_approved: 7
- needs_approval: 11
- needs_decision: 3
- needs_enrichment: 9
- research: 2
- dead: 20

## Confirmed Structural Issue

The CRM stage currently blends multiple outreach channels into one stage.

Example: a prospect can move to `outreach_sent` even if only one channel has
actually been sent. The true state is channel-specific:

- postcard
- email
- SMS later
- phone/call later

`outreach_sent` should therefore not be treated as proof that every channel has
been completed. It currently means "at least one outreach path was sent or the
prospect entered a sent-state workflow."

## Current outreach_sent Channel State

- atlanta-drywall-1: postcard submitted, no email
- membrenos-pro-home-repair: postcard submitted, email 1 sent/delivered
- moonstone-pressure-washing: postcard submitted, email 1 sent/delivered
- atlanta-pro-repairs: postcard submitted, email 1 sent/delivered
- tech-on-the-way: postcard submitted, email 1 sent/delivered
- atl-mobile-mechanics: postcard submitted, no email
- affordable-concrete-repair: postcard submitted, no email sent yet
- morales-landscape-construction: postcard submitted, email 1 sent, hard bounced
- done-right-drywall: postcard submitted, no email
- perez-pools-llc: postcard submitted, email 1 sent/delivered
- locksmith-atlanta-pro: postcard submitted, email 1 sent/delivered
- roberts-mobile-services: postcard submitted, no email
- golden-choice-prowash: postcard submitted, email 1 sent/delivered

## outreach_staged

- the-appliance-gals: postcard already submitted; email present; known site hero
  and synthetic-gallery risk still needs resolution before further action.
- harrison-sons-electrical: postcard already submitted; no email; Jesse previously
  accepted send despite known site/popup caveats.

## qa_approved Queue

These are the next candidates for outreach staging, but they need full preflight
before promotion:

- cityboys: email present, address present, open tasks: 2
- sandy-springs-plumbing: email present, missing address/phone, postcard impossible
  until address is resolved; email-only may be possible with Jesse approval
- dream-steam: postcard-only candidate, open tasks: 1
- handy-dandy-atlanta: postcard-only candidate, open tasks: 2
- tuckers-home-services: email present, open tasks: 1
- intire-mobile-tire-shop: email present, no open tasks
- smartwire-solutions: postcard-only candidate, no open tasks; known historic slug
  drift must remain watched

## needs_approval Queue

These are Jesse eye-review candidates, not outreach-ready:

- thermys-mobile-tire-and-brakes
- 24-hrs-mobile-tire-services
- piedmont-tires
- forest-park-collision
- bravo-plumbing-solutions
- chrissy-s-mobile-detailing
- rooter-pro-plumbing-drain
- tuxedo-mechanical-plumbing
- pine-peach-painting
- raiden-electrical
- browning-electrical-services

## Immediate Operating Recommendation

1. Do not bulk-send from `outreach_sent`; audit channel state first.
2. Build or amend CRM UI so each prospect displays per-channel state:
   postcard status, email sequence status, SMS status, and support/reply status.
3. Run outreach-preflight on the `qa_approved` queue before moving anything into
   `outreach_staged`.
4. Treat The Appliance Gals as the first active fix before further send work.
5. Treat ATL Mobile Mechanics review wiring as post-send finishing.
6. Keep Bruce monitoring the GTMDot Gmail label once OpenClaw Gmail watch is
   configured.

## Guardrails

No CRM writes were performed.
No deploys were performed.
No postcards were submitted.
No emails were sent.
No DNS, billing, hosting, or domain changes were performed.
