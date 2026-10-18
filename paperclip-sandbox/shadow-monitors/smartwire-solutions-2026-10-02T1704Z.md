## Follow-Up Run

- Run: 2026-10-13T12:33Z / 2026-10-13 05:33 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form - needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were absent from this response.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox is connection-refused again, unchanged from the latest recorded runs, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T11:31Z / 2026-10-13 04:31 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form - needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were absent from this response.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox is connection-refused again, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T10:30Z / 2026-10-13 03:30 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form - needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T09:28Z / 2026-10-13 02:28 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T08:27Z / 2026-10-13 01:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and included SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were absent from this response.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T07:26Z / 2026-10-13 00:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T06:56Z / 2026-10-12 23:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T06:26Z / 2026-10-12 23:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T05:56Z / 2026-10-12 22:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T05:26Z / 2026-10-12 22:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T04:56Z / 2026-10-12 21:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T04:26Z / 2026-10-12 21:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the search summary says `submitted`; detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T04:09Z / 2026-10-12 21:09 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T03:08Z / 2026-10-12 20:08 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T02:06Z / 2026-10-12 19:06 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T00:04Z / 2026-10-12 17:04 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and still returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T23:03Z / 2026-10-12 16:03 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action from prior search summaries, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T22:01Z / 2026-10-12 15:01 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and still returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T21:01Z / 2026-10-12 14:01 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and still returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- Detail `bridgeState` and `paperclipSummary` were `null`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect with HTTP status `000`.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T19:58Z / 2026-10-12 12:58 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and still included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T18:57Z / 2026-10-12 11:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and still included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T17:56Z / 2026-10-12 10:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and still included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T17:26Z / 2026-10-12 10:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action from the search summary, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T16:56Z / 2026-10-12 09:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action from the search summary, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T15:56Z / 2026-10-12 08:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `141`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action from the search summary, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T15:27Z / 2026-10-12 08:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and still included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the search summary and outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `141`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T14:26Z / 2026-10-12 07:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and still included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status remains inconsistent with the outreach event: `prospect.postcardStatus` is `not_submitted`, while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `141`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action from the search summary, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T13:56Z / 2026-10-12 06:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the summary trail: latest detail wrapper still exposes `prospect.postcardStatus` as `not_submitted` while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `141`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` failed to connect.
- `lsof -iTCP:3199 -sTCP:LISTEN -n -P` returned no listener.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T13:26Z / 2026-10-12 06:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the summary trail: latest detail wrapper still exposes `prospect.postcardStatus` as `not_submitted` while the detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `141`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` failed to connect.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T13:02Z / 2026-10-12 06:02 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the summary trail: latest detail wrapper still exposes outreach event postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`, while the detail `prospect.postcardStatus` is `not_submitted`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `141`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` failed to connect.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T12:31Z / 2026-10-12 05:31 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields under the `prospect` wrapper plus notes and outreach events.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status remains inconsistent with the summary trail: latest detail wrapper still exposes outreach event postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `141`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` failed to connect.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox remains connection-refused, unchanged from the latest recorded run, so sandbox issue/comment coordination could not be maintained through the API. Existing process-stall indicators, postcard/detail mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to the latest trail entry. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T12:01Z / 2026-10-12 05:01 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable, though the payload returned a broad prospect set and was filtered locally by SmartWire's known id.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `141`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` failed to connect.
- `GET http://127.0.0.1:3199/api/health` failed to connect.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` failed to connect.
- Sandbox issue/comment API was not used because the sandbox service is not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox condition worsened from reachable-but-unhealthy (`database_unreachable`) in the latest recorded trail to connection refused on this run, so sandbox issue/comment coordination could not be maintained through the API. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T09:26Z / 2026-10-10 02:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable, though the payload still returned a broad prospect set and was filtered locally by SmartWire's known id.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Search summary postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Next action from search summary: `Send Email 1`, no date, overdue `true`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1` next action, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T08:56Z / 2026-10-10 01:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T08:26Z / 2026-10-10 01:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T07:56Z / 2026-10-10 00:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T07:26Z / 2026-10-10 00:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T06:56Z / 2026-10-09 23:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T06:26Z / 2026-10-09 23:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T05:56Z / 2026-10-09 22:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail fields.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T04:56Z / 2026-10-09 21:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable, but returned a broad prospect payload; SmartWire detail was checked by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T04:26Z / 2026-10-09 21:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable, but returned a broad prospect payload; SmartWire detail was checked by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T03:56Z / 2026-10-09 20:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form -- needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T03:26Z / 2026-10-09 20:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T02:56Z / 2026-10-09 19:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T02:26Z / 2026-10-09 19:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T01:56Z / 2026-10-09 18:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T01:26Z / 2026-10-09 18:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T00:56Z / 2026-10-09 17:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `null`
- Pipeline/list next action overdue: `null`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form - needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T00:26Z / 2026-10-09 17:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T23:56Z / 2026-10-09 16:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T22:56Z / 2026-10-09 15:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and the broader payload still included SmartWire's postcard event.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T22:26Z / 2026-10-09 15:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T21:26Z / 2026-10-09 14:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned the broader prospects/outreach payload containing the known SmartWire postcard event.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T20:56Z / 2026-10-09 13:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T20:26Z / 2026-10-09 13:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T19:56Z / 2026-10-09 12:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and the broader payload still included SmartWire's postcard event.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T18:27Z / 2026-10-09 11:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable but returned no filtered SmartWire rows in this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T17:26Z / 2026-10-09 10:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable but returned no filtered SmartWire rows in this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T16:56Z / 2026-10-09 09:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and the broader prospects/outreach payload still included SmartWire's postcard event.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T16:26Z / 2026-10-09 09:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T14:56Z / 2026-10-09 07:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable but returned no filtered SmartWire rows in this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and prior QA/process concerns remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T14:26Z / 2026-10-09 07:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable; the returned broader prospects payload included the known SmartWire outreach event.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and prior QA/process concerns remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T13:56Z / 2026-10-09 06:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable but returned no filtered SmartWire rows in this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and prior QA/process concerns remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T13:26Z / 2026-10-09 06:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Pipeline/list next action label: `null`
- Pipeline/list next action overdue: `null`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and prior QA/process concerns remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T12:56Z / 2026-10-09 05:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3` in the broader prospects payload.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T11:26Z / 2026-10-09 04:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T10:56Z / 2026-10-09 03:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T10:26Z / 2026-10-09 03:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T09:56Z / 2026-10-09 02:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false` in list response; `null` in detail wrapper.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T09:26Z / 2026-10-09 02:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T08:56Z / 2026-10-09 01:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T07:56Z / 2026-10-09 00:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3` when matching `businessName`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T07:26Z / 2026-10-09 00:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable but returned no SmartWire row in the filtered jq pass on this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T06:56Z / 2026-10-08 23:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable but returned no SmartWire row in the filtered jq pass on this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain visible from the detail wrapper in legacy field checks: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T06:26Z / 2026-10-08 23:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T05:56Z / 2026-10-08 22:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable, but returned the broader prospects payload rather than a tightly filtered SmartWire-only result on this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1` from the broader list payload when present, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T05:26Z / 2026-10-08 22:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T04:56Z / 2026-10-08 21:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable, but again returned the broader prospects payload rather than a tightly filtered SmartWire-only result.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T03:56Z / 2026-10-08 20:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T03:26Z / 2026-10-08 20:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T02:56Z / 2026-10-08 19:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable, but returned the broader prospects payload rather than a tightly filtered SmartWire-only result on this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T02:26Z / 2026-10-08 19:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable but the filtered SmartWire search command did not return a list object for SmartWire on this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T01:56Z / 2026-10-08 18:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable but the filtered SmartWire search command did not return a list object for SmartWire on this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T00:56Z / 2026-10-08 17:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable but the filtered SmartWire search command did not return a list object for SmartWire on this run.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T00:27Z / 2026-10-08 17:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T23:56Z / 2026-10-08 16:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Direct detail subpaths checked for `notes` and `outreach-events` returned HTTP `404` on this run.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T23:27Z / 2026-10-08 16:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false` in list response; detail response omitted/null.
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail response returned no outreach events on this run.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T22:56Z / 2026-10-08 15:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable but the filtered list command did not return SmartWire.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T22:26Z / 2026-10-08 15:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T21:27Z / 2026-10-08 14:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable; the plain list response did not return SmartWire in the filtered command used this run, while the unfiltered list endpoint still included SmartWire by known prospect ID.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Detail subpaths checked for `notes`, `tasks`, `outreach-events`, and `activity` returned the app HTML shell rather than JSON API payloads on this run.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T20:56Z / 2026-10-08 13:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T20:26Z / 2026-10-08 13:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable but did not return SmartWire in the list response used by this monitor.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T19:56Z / 2026-10-08 12:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T18:56Z / 2026-10-08 11:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T18:26Z / 2026-10-08 11:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `null`
- Pipeline/list next action overdue: `null`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T17:56Z / 2026-10-08 10:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T17:26Z / 2026-10-08 10:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable but did not return SmartWire in the filtered list response used by this monitor.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T16:56Z / 2026-10-08 09:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `null`
- Pipeline/list next action overdue: `null`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T16:26Z / 2026-10-08 09:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T15:56Z / 2026-10-08 08:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T14:56Z / 2026-10-08 07:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T14:26Z / 2026-10-08 07:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned an array including SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `null`
- Pipeline/list next action overdue: `null`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T13:56Z / 2026-10-08 06:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T13:26Z / 2026-10-08 06:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T12:56Z / 2026-10-08 05:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T12:26Z / 2026-10-08 05:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`; detail response did not include sequence/order ID on this run.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T11:56Z / 2026-10-08 04:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and still includes SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T11:26Z / 2026-10-08 04:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3` under `.prospects`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T10:56Z / 2026-10-08 03:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3` under `.prospects`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T10:26Z / 2026-10-08 03:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3` under `.prospects`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T09:56Z / 2026-10-08 02:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T09:26Z / 2026-10-08 02:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label remains `Send Email 1` and overdue.
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T09:01Z / 2026-10-08 02:01 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T08:00Z / 2026-10-08 01:00 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T06:59Z / 2026-10-07 23:59 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T05:57Z / 2026-10-07 22:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T04:56Z / 2026-10-07 21:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T04:26Z / 2026-10-07 21:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T03:56Z / 2026-10-07 20:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, and postcard status mismatch remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T03:26Z / 2026-10-07 20:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T02:56Z / 2026-10-07 19:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T02:26Z / 2026-10-07 19:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T01:56Z / 2026-10-07 18:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T01:26Z / 2026-10-07 18:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T01:04Z / 2026-10-07 18:04 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-08T00:02Z / 2026-10-07 17:02 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: none returned
- Pipeline/list next action overdue: none returned
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form - needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators and the list/detail postcard status mismatch remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T23:00Z / 2026-10-07 16:00 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T21:59Z / 2026-10-07 14:59 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T20:58Z / 2026-10-07 13:58 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T19:26Z / 2026-10-07 12:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T18:56Z / 2026-10-07 11:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T18:26Z / 2026-10-07 11:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T17:56Z / 2026-10-07 10:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T17:26Z / 2026-10-07 10:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T16:26Z / 2026-10-07 09:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: not present in the list payload this run
- Pipeline/list next action overdue: not present in the list payload this run
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T15:57Z / 2026-10-07 08:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T14:56Z / 2026-10-07 07:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: not present in the list payload this run
- Pipeline/list next action overdue: not present in the list payload this run
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T13:56Z / 2026-10-07 06:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T13:26Z / 2026-10-07 06:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable with HTTP 200.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue next email sequence, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T12:56Z / 2026-10-07 05:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T12:26Z / 2026-10-07 05:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable with HTTP 200.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue next email sequence, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T11:56Z / 2026-10-07 04:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` remained read-only reachable for notes/outreach context.
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T11:26Z / 2026-10-07 04:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` remained read-only reachable for notes/outreach context.
- CRM notes remain: intake note `Added via intake form — needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T10:56Z / 2026-10-07 03:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` remained read-only reachable for notes/outreach context.
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T10:26Z / 2026-10-07 03:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` remained read-only reachable for notes/outreach context.
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T09:56Z / 2026-10-07 02:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` remained read-only reachable for notes/outreach context.
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T09:26Z / 2026-10-07 02:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` remained read-only reachable for notes/outreach context.
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T08:56Z / 2026-10-07 01:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` remained read-only reachable for notes/outreach context.
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T08:26Z / 2026-10-07 01:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` remained read-only reachable for notes/outreach context.
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T07:56Z / 2026-10-07 00:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire notes and outreach event detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T06:26Z / 2026-10-06 23:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T07:27Z / 2026-10-07 00:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T05:56Z / 2026-10-06 22:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T05:26Z / 2026-10-06 22:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T04:26Z / 2026-10-06 21:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T03:56Z / 2026-10-06 20:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1` from the list view on prior runs, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T03:26Z / 2026-10-06 20:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T03:04Z / 2026-10-06 20:04 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T02:02Z / 2026-10-06 19:02 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T01:01Z / 2026-10-06 18:01 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T23:57Z / 2026-10-06 16:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T22:56Z / 2026-10-06 15:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T22:27Z / 2026-10-06 15:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T21:56Z / 2026-10-06 14:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T21:26Z / 2026-10-06 14:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`
- Open CRM note remains present from `qa-bot`: site_built/no-site QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue/no-email sequence state, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T20:56Z / 2026-10-06 13:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T19:27Z / 2026-10-06 12:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T18:56Z / 2026-10-06 11:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T18:27Z / 2026-10-06 11:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T17:56Z / 2026-10-06 10:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T17:26Z / 2026-10-06 10:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T16:56Z / 2026-10-06 09:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T16:26Z / 2026-10-06 09:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T15:56Z / 2026-10-06 08:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T15:27Z / 2026-10-06 08:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T14:56Z / 2026-10-06 07:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entry and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue/outstanding email sequence state, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T14:26Z / 2026-10-06 07:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable; response shape is an object containing `prospects`, `outreachEvents`, `kpis`, and `trades`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entry and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue/outstanding email sequence state, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T14:01Z / 2026-10-06 07:01 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue/outstanding email sequence state, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T13:00Z / 2026-10-06 06:00 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T11:57Z / 2026-10-06 04:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue/outstanding email sequence state, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T10:56Z / 2026-10-06 03:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue/outstanding email sequence state, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T10:26Z / 2026-10-06 03:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T09:56Z / 2026-10-06 02:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T09:26Z / 2026-10-06 02:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T08:56Z / 2026-10-06 01:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T08:26Z / 2026-10-06 01:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T07:56Z / 2026-10-06 00:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T06:56Z / 2026-10-05 23:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T06:26Z / 2026-10-05 23:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T05:56Z / 2026-10-05 22:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing stale-stage/process-stall indicators remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T05:26Z / 2026-10-05 22:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: unavailable in detail response
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing stale-stage indicators remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T04:56Z / 2026-10-05 21:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T04:26Z / 2026-10-05 21:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T03:56Z / 2026-10-05 20:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T03:26Z / 2026-10-05 20:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.## Follow-Up Run

- Run: 2026-10-09T12:26Z / 2026-10-09 05:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Days in stage: `138`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-09T11:56Z / 2026-10-09 04:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Pipeline/list next action label: `Send Email 1`
- Pipeline/list next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- CRM notes remain visible from the detail wrapper: intake note `Added via intake form — needs research.` and QA failure note about missing local site/403 preview.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-09T08:26Z / 2026-10-09 01:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- List next action: `Send Email 1`, overdue `true`
- List postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue list next action remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-09T01:26Z / 2026-10-08 18:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Next action label: `Send Email 1`
- Next action overdue: `true`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-08T15:26Z / 2026-10-08 08:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T19:56Z / 2026-10-07 12:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event remains postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`
- CRM notes remain: intake note `Added via intake form -- needs research.` created `2026-04-28T02:19:50.995369+00:00`, and QA failure note created `2026-04-29T01:08:47.832092+00:00`.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, overdue `Send Email 1`, postcard status mismatch, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-07T14:26Z / 2026-10-07 07:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-07T06:56Z / 2026-10-06 23:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-07T04:56Z / 2026-10-06 21:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T20:27Z / 2026-10-06 13:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard channel `postcard`, event type `submitted`, sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `136`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. Existing process-stall indicators, postcard status mismatch, overdue `Send Email 1`, and open QA note remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T02:56Z / 2026-10-05 19:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T02:26Z / 2026-10-05 19:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T01:26Z / 2026-10-05 18:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T00:56Z / 2026-10-05 17:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The overdue email/postcard mismatch signals remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-06T00:26Z / 2026-10-05 17:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell and did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T23:56Z / 2026-10-05 16:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T23:26Z / 2026-10-05 16:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T22:56Z / 2026-10-05 15:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` was read-only reachable and returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `null`
- Next action overdue from list endpoint: `null`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-06T01:56Z / 2026-10-05 18:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T22:26Z / 2026-10-05 15:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T21:56Z / 2026-10-05 14:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `null`
- Next action overdue from list endpoint: `null`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503`; the response body was not printed by `curl -f`, but this matches the prior `database_unreachable` failure path.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T21:26Z / 2026-10-05 14:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T20:56Z / 2026-10-05 13:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T20:26Z / 2026-10-05 13:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T19:56Z / 2026-10-05 12:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T19:26Z / 2026-10-05 12:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T18:56Z / 2026-10-05 11:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T18:26Z / 2026-10-05 11:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T17:26Z / 2026-10-05 10:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T16:56Z / 2026-10-05 09:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T16:26Z / 2026-10-05 09:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T15:56Z / 2026-10-05 08:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T15:30Z / 2026-10-05 08:30 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T14:29Z / 2026-10-05 07:29 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T13:26Z / 2026-10-05 06:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T12:56Z / 2026-10-05 05:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and contained SmartWire data by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and overdue `Send Email 1` remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T12:26Z / 2026-10-05 05:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and contained SmartWire data by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T11:56Z / 2026-10-05 04:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and contained SmartWire data by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T11:26Z / 2026-10-05 04:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and contained SmartWire data by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The previously observed overdue next action remains present and unchanged. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T10:56Z / 2026-10-05 03:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and contained SmartWire data by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T10:26Z / 2026-10-05 03:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; browser view loaded the pipeline and confirmed SmartWire appears under `Outreach Sent`, not `Research`.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200, but browser snapshot showed no rendered app content.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T09:57Z / 2026-10-05 02:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML still did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T08:56Z / 2026-10-05 01:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML still did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T08:26Z / 2026-10-05 01:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML still did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T07:26Z / 2026-10-05 00:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML still did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T06:58Z / 2026-10-04 23:58 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T05:56Z / 2026-10-04 22:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T05:26Z / 2026-10-04 22:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T04:56Z / 2026-10-04 21:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T04:26Z / 2026-10-04 21:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T03:56Z / 2026-10-04 20:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T03:26Z / 2026-10-04 20:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T02:57Z / 2026-10-04 19:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T02:26Z / 2026-10-04 19:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T01:26Z / 2026-10-04 18:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T00:56Z / 2026-10-04 17:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T00:26Z / 2026-10-04 17:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T23:56Z / 2026-10-04 16:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T23:26Z / 2026-10-04 16:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T22:56Z / 2026-10-04 15:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T22:26Z / 2026-10-04 15:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T21:56Z / 2026-10-04 14:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T21:41Z / 2026-10-04 14:41 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T20:40Z / 2026-10-04 13:40 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T19:37Z / 2026-10-04 12:37 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T18:36Z / 2026-10-04 11:36 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T17:34Z / 2026-10-04 10:34 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T16:33Z / 2026-10-04 09:33 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T13:29Z / 2026-10-04 06:29 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Postcard status: pipeline list remains `submitted`; detail endpoint prospect field remains `not_submitted` while exposing the submitted postcard event.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T09:26Z / 2026-10-05 02:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML still did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label from list endpoint: `Send Email 1`
- Next action overdue from list endpoint: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-05T07:56Z / 2026-10-05 00:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T15:31Z / 2026-10-04 08:31 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T14:30Z / 2026-10-04 07:30 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T12:27Z / 2026-10-04 05:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` reachable read-only.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Postcard status: pipeline event remains `submitted`; detail endpoint prospect field remains `not_submitted` while exposing the submitted postcard event.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T11:26Z / 2026-10-04 04:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted` in pipeline list; detail endpoint reports prospect `postcardStatus` as `not_submitted` while still exposing the submitted postcard event.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T10:56Z / 2026-10-04 03:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted` in pipeline list; detail endpoint reports prospect `postcardStatus` as `not_submitted` while still exposing the submitted postcard event.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T10:26Z / 2026-10-04 03:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted` in pipeline list; detail endpoint still includes the submitted outreach event but reports prospect `postcardStatus` as `not_submitted`.
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch was noted in the sandbox trail only because the detail endpoint still exposes the submitted event and the pipeline list remains consistent with prior observations. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T09:56Z / 2026-10-04 02:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T07:57Z / 2026-10-04 00:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T09:26Z / 2026-10-04 02:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T08:56Z / 2026-10-04 01:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T08:26Z / 2026-10-04 01:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T06:57Z / 2026-10-03 23:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T06:26Z / 2026-10-03 23:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T05:56Z / 2026-10-03 22:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T05:26Z / 2026-10-03 22:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T03:29Z / 2026-10-03 20:29 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

# SmartWire Solutions Shadow Monitor

- Run: 2026-10-02T17:04Z / 2026-10-02 10:04 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Scope: read-only CRM check plus local Paperclip sandbox check
- Production writes: none
- Outreach/deployments: none

## Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Disqualified: `false`

## Expected Context

The cron payload said SmartWire Solutions was currently in the live CRM Research stage. The read-only CRM API now reports `outreach_sent`, so this run should surface to Jesse under the "SmartWire moves stage" rule.

## Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `database_unreachable`.
- Sandbox issue/comment API was not used because the sandbox health check was unhealthy.

## Action Taken

Created this sandbox-only shadow coordination trail. No CRM writes, production file changes, deployments, or outreach were performed.

## Follow-Up Run

- Run: 2026-10-04T00:56Z / 2026-10-03 17:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T02:28Z / 2026-10-03 19:28 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T01:26Z / 2026-10-03 18:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T23:26Z / 2026-10-03 16:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T23:56Z / 2026-10-03 16:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T20:56Z / 2026-10-03 13:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T22:56Z / 2026-10-03 15:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/issues` returned `{"error":"Missing companyId in path. Use /api/companies/{companyId}/issues."}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T22:26Z / 2026-10-03 15:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T21:56Z / 2026-10-03 14:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T21:26Z / 2026-10-03 14:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T17:56Z / 2026-10-03 10:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T14:56Z / 2026-10-03 07:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T20:27Z / 2026-10-03 13:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T09:26Z / 2026-10-03 02:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from prior shadow runs and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T09:56Z / 2026-10-03 02:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entry and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T06:56Z / 2026-10-02 23:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions under `.prospects[]`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T10:26Z / 2026-10-03 03:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entry and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T08:56Z / 2026-10-03 01:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the prior shadow run and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T08:26Z / 2026-10-03 01:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T07:56Z / 2026-10-03 00:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T06:26Z / 2026-10-02 23:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T02:26Z / 2026-10-02 19:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions under the current `businessName` payload shape.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T00:26Z / 2026-10-02 17:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T05:56Z / 2026-10-02 22:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T05:26Z / 2026-10-02 22:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T04:56Z / 2026-10-02 21:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T04:26Z / 2026-10-02 21:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T03:56Z / 2026-10-02 20:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T03:26Z / 2026-10-02 20:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The CRM `nextActionLabel`/`nextActionOverdue` fields now returned `null` in the read-only API response. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T02:56Z / 2026-10-02 19:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T01:56Z / 2026-10-02 18:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions under the current `businessName` payload shape.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T01:26Z / 2026-10-02 18:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions under the current `businessName` payload shape.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T00:56Z / 2026-10-02 17:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T23:56Z / 2026-10-02 16:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T21:26Z / 2026-10-02 14:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T23:26Z / 2026-10-02 16:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T22:56Z / 2026-10-02 15:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T22:27Z / 2026-10-02 15:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions using the current object-shaped payload under `prospects`.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T21:56Z / 2026-10-02 14:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T17:27Z / 2026-10-02 10:27 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `database_unreachable`.
- `GET http://127.0.0.1:3199/api/issues` returned HTTP `400` requiring a company-scoped path.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. This remains reportable to Jesse under the "SmartWire moves stage" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T17:57Z / 2026-10-02 10:57 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/a67ce81f-9799-4ef0-b217-76bc39c19f9f/issues?limit=200` returned HTTP `500`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T20:56Z / 2026-10-02 13:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T20:26Z / 2026-10-02 13:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T19:56Z / 2026-10-02 12:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T18:26Z / 2026-10-02 11:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/a67ce81f-9799-4ef0-b217-76bc39c19f9f/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T18:56Z / 2026-10-02 11:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-02T19:26Z / 2026-10-02 12:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

The live CRM record still conflicts with the cron context: SmartWire is not in Research, it is in `outreach_sent`. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "SmartWire moves stage" and "process fails/stalls" rules. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T07:26Z / 2026-10-03 00:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `null`
- Next action overdue: `null`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This remains reportable to Jesse under the "process fails/stalls" rule. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T10:56Z / 2026-10-03 03:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T17:26Z / 2026-10-03 10:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T16:56Z / 2026-10-03 09:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T16:26Z / 2026-10-03 09:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T15:56Z / 2026-10-03 08:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `null`
- Next action overdue: `null`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T15:26Z / 2026-10-03 08:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T14:26Z / 2026-10-03 07:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T13:56Z / 2026-10-03 06:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T13:26Z / 2026-10-03 06:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T18:26Z / 2026-10-03 11:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T12:56Z / 2026-10-03 05:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T18:56Z / 2026-10-03 11:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T12:26Z / 2026-10-03 05:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T11:56Z / 2026-10-03 04:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T11:26Z / 2026-10-03 04:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `132`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T19:26Z / 2026-10-03 12:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-03T19:56Z / 2026-10-03 12:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T00:26Z / 2026-10-03 17:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T04:30Z / 2026-10-03 21:30 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-04T04:56Z / 2026-10-03 21:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Postcard status: `submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `133`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-05T01:56Z / 2026-10-04 18:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `134`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. This is not a new condition relative to the latest shadow trail entries, so no Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-05T17:56Z / 2026-10-05 10:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-06T07:26Z / 2026-10-06 00:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `135`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-07T16:56Z / 2026-10-07 09:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Next action label: `Send Email 1`
- Next action overdue: `true`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `137`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-08T19:26Z / 2026-10-08 12:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-08T21:56Z / 2026-10-08 14:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell but did not expose SmartWire text directly.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
## Follow-Up Run

- Run: 2026-10-09T04:26Z / 2026-10-08 21:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T15:26Z / 2026-10-09 08:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`
- Existing open CRM note remains the 2026-04-29 QA failure about site-built/no-site/preview-403.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and open QA failure remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-13T01:05Z / 2026-10-12 18:05 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `142`
- Sequence paused: `false`
- Existing open CRM note remains the 2026-04-29 QA failure about site-built/no-site/preview-403.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` returned connection refused.
- `GET http://127.0.0.1:3199/api/health` returned connection refused.
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned connection refused.
- Sandbox issue/comment API was not used because the local Paperclip sandbox was unreachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox was unreachable on this run, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and open QA failure remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-12T16:26Z / 2026-10-12 09:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `141`
- Sequence paused: `false`
- Existing open CRM note remains the 2026-04-29 QA failure about site-built/no-site/preview-403.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` connection refused.
- `GET http://127.0.0.1:3199/health` connection refused.
- `GET http://127.0.0.1:3199/api/health` connection refused.
- Sandbox issue/comment API was not used because the sandbox service was not reachable.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox service was connection-refused on this run, so sandbox issue/comment coordination could not be maintained through the API. The pipeline/detail postcard status mismatch, overdue `Send Email 1` next action, and open QA failure remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-10T05:26Z / 2026-10-09 22:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Existing open CRM note remains the 2026-04-29 QA failure about site-built/no-site/preview-403.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/issues` returned HTTP `400` with API guidance `Missing companyId in path. Use /api/companies/{companyId}/issues.`
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and open QA failure remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T23:26Z / 2026-10-09 16:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Preview site URL: `https://smart-wire-solutions.pages.dev/`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/issues` returned HTTP `400` with API guidance `Missing companyId in path. Use /api/companies/{companyId}/issues.`
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch remains present but is not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T21:56Z / 2026-10-09 14:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects?search=SmartWire%20Solutions` was read-only reachable; the response contained the broader prospects/outreach payload and still included SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Existing open CRM note remains the 2026-04-29 QA failure about site-built/no-site/preview-403.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/issues` returned HTTP `400` with API guidance `Missing companyId in path. Use /api/companies/{companyId}/issues.`
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and open QA failure remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T18:56Z / 2026-10-09 11:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Existing open CRM note remains the 2026-04-29 QA failure about site-built/no-site/preview-403.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/issues` returned HTTP `400` with API guidance `Missing companyId in path. Use /api/companies/{companyId}/issues.`
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and open QA failure remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T15:56Z / 2026-10-09 08:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `138`
- Sequence paused: `false`

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/issues` returned HTTP 200 with API guidance `Missing companyId in path. Use /api/companies/{companyId}/issues.`
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and open QA failure remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T17:56Z / 2026-10-09 10:56 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Existing open CRM note remains the 2026-04-29 QA failure about site-built/no-site/preview-403.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/issues` returned HTTP `400` with API guidance `Missing companyId in path. Use /api/companies/{companyId}/issues.`
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and open QA failure remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.

## Follow-Up Run

- Run: 2026-10-09T19:26Z / 2026-10-09 12:26 America/Los_Angeles
- Source: `paperclip-smartwire-shadow-overnight`
- Production writes: none
- Outreach/deployments: none

### Read-Only CRM Observation

- `crm.cloakanddagger.co/pipeline` reachable with HTTP 200; static HTML loaded the pipeline shell.
- `GET https://crm.cloakanddagger.co/api/prospects` was read-only reachable and returned SmartWire Solutions by known prospect ID `8b21c05b-605b-410d-9b5c-bc66d78a9bf3`.
- `GET https://crm.cloakanddagger.co/api/prospects/8b21c05b-605b-410d-9b5c-bc66d78a9bf3` returned SmartWire detail under the `prospect` wrapper.
- Observed SmartWire CRM stage: `outreach_sent`
- Stage entered at: `2026-05-23T16:55:07.151+00:00`
- Updated at: `2026-05-23T16:55:07.316+00:00`
- Trade category: `Electrician`
- Owner name: `Terry Henry`
- Notes count: `2`
- Open tasks count: `0`
- Prospect next email sequence: `1`
- Pipeline/list postcard status: `submitted`
- Detail postcard status: `not_submitted`
- Detail outreach event: postcard sequence `1`, order ID `3a7ae7b1-9bef-4f90-92c3-2b49fe59976a`, created `2026-05-23T16:55:07.041044+00:00`
- Emails sent count: `0`
- Disqualified: `false`
- Existing site status: `outdated`
- Days in stage: `139`
- Sequence paused: `false`
- Existing open CRM note remains the 2026-04-29 QA failure about site-built/no-site/preview-403.

### Local Paperclip Sandbox Observation

- `http://127.0.0.1:3199/` reachable with HTTP 200.
- `GET http://127.0.0.1:3199/api/health` returned HTTP `503` with `{"status":"unhealthy","version":"2026.428.0","error":"database_unreachable"}`.
- `GET http://127.0.0.1:3199/api/issues` returned HTTP `400` with API guidance `Missing companyId in path. Use /api/companies/{companyId}/issues.`
- `GET http://127.0.0.1:3199/api/companies/8b21c05b-605b-410d-9b5c-bc66d78a9bf3/issues?limit=200` returned HTTP `500` with `{"error":"Internal server error"}`.
- Sandbox issue/comment API was not used because the sandbox health check remains unhealthy.

### Monitor Decision

No new CRM stage movement was observed on this run: SmartWire remains in `outreach_sent`, unchanged from the latest shadow trail entries and still conflicting with the cron context that expected live CRM Research. The local Paperclip sandbox API remains stalled by `database_unreachable`, so no sandbox issue/comment write was attempted. The pipeline/detail postcard status mismatch and open QA failure remain present but are not new relative to prior trail entries. No Jesse-facing escalation was sent. No CRM writes, production file changes, deployments, outreach, or sandbox issue/comment writes were performed.
