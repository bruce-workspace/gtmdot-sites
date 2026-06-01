# GTM-24 Phase 1 Reply-To Update

Date: 2026-05-17 America/New_York
Lane: Outreach Operations
Mode: approved implementation, Phase 1 only

## Scope completed

Updated current active GTMDot prospect outreach reply-to paths to `hello@gtmdot.com`.

Removed/replaced `jesse@cloakanddagger.co` from GTMDot prospect outreach send helpers/docs in scope.

Added a static regression check so the old address fails verification if it reappears in the GTMDot outreach send paths.

## Files changed

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/resend.ts`
  - Changed active CRM Resend helper from `replyTo: 'jesse@cloakanddagger.co'` to `replyTo: 'hello@gtmdot.com'`.

- `/Users/bruce/.openclaw/workspace/gtmdot/email-sequences/resend/send-gtmdot-email.js`
  - Changed legacy sender `REPLY_TO` from `jesse@cloakanddagger.co` to `hello@gtmdot.com`.

- `/Users/bruce/.openclaw/workspace/gtmdot/email-sequences/resend/BRUCE-HANDOFF.md`
  - Updated handoff documentation to list `hello@gtmdot.com` as reply-to.

- `/Users/bruce/.openclaw/workspace/brucecom-v3/scripts/assert-gtmdot-outreach-reply-to.mjs`
  - Added static regression check.

- `/Users/bruce/.openclaw/workspace/brucecom-v3/package.json`
  - Added `check:gtmdot-outreach-reply-to` script.

## Verification run

Static guard:

`npm run check:gtmdot-outreach-reply-to`

Result:

`GTMDot outreach reply-to check passed: hello@gtmdot.com`

Canonical address search:

Confirmed `hello@gtmdot.com` in:

- active CRM helper
- legacy sender
- legacy handoff

Forbidden address search:

Confirmed no `jesse@cloakanddagger.co` remains in the active helper, legacy sender, or legacy handoff.

Dry-run/static preview:

`node send-gtmdot-email.js --preview --email 1`

Result:

- Rendered Email 1 HTML only.
- No Resend API call.
- No prospect send.
- No CRM write.

## Guardrails honored

- No prospect sends.
- No production email sends.
- No CRM writes.
- No deploys.
- No Paperclip mutations.
- No git push.
- No customer/prospect contact.

## Notes

The new static check intentionally contains the forbidden address as a string to detect it. Verification searches for the forbidden address in actual outreach send helper/docs separately, excluding the guard's own detector string.

The workspace had unrelated pre-existing dirty files. This Phase 1 change was limited to the files listed above.

## CRM v2 coordination

CRM v2 should preserve this contract: GTMDot prospect outreach replies route to `hello@gtmdot.com`. Future CRM v2 schema/UI should model reply state independently from lifecycle stage and should not rely on `jesse@cloakanddagger.co` for GTMDot outreach reply handling.
