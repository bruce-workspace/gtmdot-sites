# Poplar recipient name rule

Date: 2026-05-21
Owner: Codex / GTMDot quarterback
Status: codified locally, no send performed

## Why this exists

Harrison & Sons Electrical Service failed Poplar submission with API 400 because
Poplar rejected a `recipient.first_name` longer than 20 characters. The old CRM
fallback could pass the full business name as `first_name` when no owner/contact
name existed.

## Rule

Before any postcard submit, the payload must satisfy:

- `recipient.first_name` is present and 20 characters or fewer.
- A real owner/contact first name may be used when known and 20 characters or fewer.
- If no owner/contact is known, derive a short business label rather than passing the full legal/trade name.
- Strip legal suffixes such as `LLC`, `Inc`, `Company`, and `Corp`.
- Strip trailing trade descriptors when needed, such as `Electrical Service`, `Services`, `Plumbing`, `Tire`, `Detailing`, or similar category words.
- If no clean label fits, fall back to `Current` / `Resident`.

Examples:

- `Harrison & Sons Electrical Service LLC` -> `first_name: "Harrison & Sons"`, `last_name: ""`
- `The Appliance Gals` -> `first_name: "The Appliance Gals"`, `last_name: ""`
- Unknown/unsafe long label -> `first_name: "Current"`, `last_name: "Resident"`

## Code touched

- `/Users/bruce/.openclaw/workspace/gtmdot-crm/src/app/api/prospects/[id]/actions/route.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/prospects/[id]/actions/route.ts`
- `/Users/bruce/.openclaw/workspace/gtmdot-crm/src/lib/poplar.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/poplar.ts`
- `/Users/bruce/.openclaw/workspace/gtmdot/skills/outreach-preflight/SKILL.md`

## Still prohibited

No CRM writes, Paperclip mutations, deploys, Poplar sends, Resend sends,
prospect/customer contact, git pushes, DNS/domain/hosting/billing changes, or
Stripe actions were performed as part of this codification.
