---
from: r1vs (MacBook Pro, Claude Code)
to: next session (any Claude — for fresh-eyes architecture thinking)
date: 2026-04-17
type: problem brief
topic: Real-time Claude-to-Claude communication without a human in the loop
status: draft — looking for architecture proposals
note: This brief is deliberately self-contained so it can be dropped into a fresh session without GTMDot context.
---

# The Inter-Claude Real-Time Comms Problem

## The setup

Jesse operates two Claude Code instances on two machines:

- **MacBook Pro** — "R1VS" — primary Claude Code instance for building sites, research, writing code. Has Slack, Telegram, Discord, Supabase MCP, GitHub, all the usual dev tools.
- **Mac Mini** — the "Mini Claude" / "CEO" — runs the CRM, intake-watcher cron, deploy pipeline, and coordinates with "Bruce" (Open Claude on the Mini for broader tool access). Does NOT have Slack installed for security reasons (Slack holds sensitive business DMs; prompt-injection blast radius too large).

The two Claudes need to coordinate continuously: photo handoff contracts, finalization signals, blocker flags, architecture decisions, priority shifts. This is genuine multi-agent ops, not a single-Claude workflow.

## What works today (baseline)

We've implemented a **git-based message bus** in the shared `gtmdot-sites` repo:

```
gtmdot-sites/
  messages/
    YYYY-MM-DD-HHMM-<author>-<topic>.md
```

Each message is a markdown file with frontmatter (`from`, `to`, `date`, `subject`, `priority`). Committed and pushed to origin. Both Claudes pull and read when they start a session.

This is the **persistent, auditable layer**. It works well for:
- Architecture proposals (Jesse can review diffs before either Claude acts)
- Finalization signals (R1VS writes finalization → Mini's intake-watcher cron detects → deploy)
- Photo handoff contracts (R1VS writes brief → Bruce picks up → Bruce delivers → R1VS wires + finalizes)
- Post-hoc audit trail of every decision

## What doesn't work (the real problem)

**Claude Code is session-driven.** It doesn't poll, subscribe, or run in the background. Each Claude only reads messages when Jesse opens a new session in that terminal. So:

- R1VS writes a message → pushes to git → done from R1VS's perspective
- Mini has no idea a message exists until Jesse opens a new Claude Code session on the Mini
- Even then, Mini only reads if explicitly asked to pull + read `messages/`

In practice today, Jesse is the trigger. He literally:
1. Reads a message from one Claude on one machine
2. Copies it to email/Slack/Telegram/Discord
3. Opens the other machine
4. Pastes the message into a Claude Code session
5. Waits for a response
6. Copies that response back

He's a **human middleware layer** doing manual copy/paste between two Claude sessions several times per hour. It's slow, error-prone, and the whole point of having two Claudes is defeated when the human is the bottleneck.

## Jesse's explicit goal

**"How can we further automate the back and forth when I'm not in front of both computers?"**

He wants to be able to:
- Be away from either machine for hours at a time
- Have R1VS and Mini continue to coordinate without him
- Only step in when a decision actually needs a human (priority call, approval of an architecture change, dispute resolution)

Ideally: R1VS writes a message → Mini detects it within minutes → Mini reads and acts → Mini responds → R1VS sees it on next check → continues working. No human in the loop for routine coordination.

## Tools available on each machine

| Tool | MacBook | Mac Mini | Notes |
|---|---|---|---|
| Slack | ✅ | ❌ | Mini doesn't have it — business DM security concern |
| Telegram | ✅ | ✅ | Both have it |
| Discord | ✅ (just installed) | ❌ (not yet — Jesse can add) | |
| Supabase | ✅ (MCP) | ✅ (MCP) | Both Claudes can read/write Supabase |
| GitHub | ✅ | ✅ | Shared repo, shared origin |
| Email | ✅ | ✅ | |
| CRM (Supabase-backed) | ✅ | ✅ | Jesse's GTM CRM lives on Supabase |
| Claude Code CLI | ✅ | ✅ | The thing we need to trigger |
| Open Claude ("Bruce") | ❌ | ✅ | Employee role, broader tool access |
| AppleScript / launchd / cron | ✅ | ✅ | Both are Macs |
| Terminal app automation | ✅ | ✅ | |

## The fundamental insight

**The transport isn't the hard part.** Supabase, git, Telegram, Discord, email — any of them can deliver a message reliably.

**The hard part is triggering the sister Claude to read and act.** Claude Code sessions don't run continuously. Something has to *start* a session, feed it a prompt, and capture its output.

## Candidate architectures (partial list — looking for more)

### Option A: Supabase realtime + agent triggers Claude Code headless

Both machines run a lightweight background agent (Python, Node, shell — doesn't matter) that:
1. Subscribes to a Supabase realtime channel for `messages` table changes
2. On new message addressed to this machine's Claude, invokes `claude -p "<prompt_template_with_message_body>"` in headless mode
3. Captures Claude's output and writes response back to Supabase

**Pros:** Real-time. No polling. Uses existing Supabase infra. Works offline when target is unreachable (buffered by Supabase).
**Cons:** Need to build the agent on both machines. Headless Claude Code has cost implications — each trigger burns tokens. Prompt template has to be carefully constrained to avoid prompt injection from message content. Handling interactive tools (like Edit or Write that want confirmation) in headless mode is nontrivial.

### Option B: GitHub Actions + webhook desktop listener

1. R1VS pushes a message to `messages/` → GitHub Action fires
2. Action sends webhook to each machine's local listener (ngrok or Tailscale funnel)
3. Listener parses the message → invokes `claude -p` or opens a terminal with Claude pre-prompted

**Pros:** Git-native, audit trail is free, uses existing repo infra.
**Cons:** Requires public webhook endpoint per machine or a Tailscale-like tunnel. More infra than Option A.

### Option C: Telegram bot as trigger (not transport)

1. Claude writes message to git as usual (the persistent layer stays)
2. After pushing, Claude sends a Telegram message via bot API: "New message from R1VS, pull and read"
3. Telegram bot on target machine runs an AppleScript that opens a terminal and starts a Claude Code session with "pull + read messages/" as the initial prompt

**Pros:** Both machines have Telegram. Simple bot. Human-readable fallback if automation fails (Jesse sees the ping too).
**Cons:** Still requires headless or AppleScript-triggered Claude session on target. Doesn't solve the core trigger problem, just notifies.

### Option D: Supabase-backed custom desktop app

Build a small Electron app (or native SwiftUI):
- Shared inbox UI for both Claudes
- Real-time sync via Supabase
- "Run this in Claude Code" button that invokes `claude -p` on the message
- Status indicators (message seen, Claude running, response ready)

**Pros:** Purpose-built, clean UX, makes the multi-agent ops visible to Jesse.
**Cons:** Real dev work. Maintenance burden. Reinvents chat.

### Option E: The CRM as message bus

Repurpose the existing Supabase-backed CRM. Add a `claude_messages` table (or similar) with:
- `from_agent` / `to_agent`
- `subject` / `body`
- `status` (pending, read, responded)
- `thread_id`

Both Claudes write/read via Supabase MCP. The CRM UI already exists for Jesse to monitor.

**Pros:** Zero new infra. CRM is already running. Jesse already has it open.
**Cons:** Conflates CRM with inter-Claude comms. Still doesn't solve the trigger problem without one of A/B/C on top.

### Option F: Scheduled background Claude sessions (ScheduleWakeup / cron)

On each machine, a cron job runs every N minutes:
```
*/10 * * * * claude -p "Check messages/ for new items addressed to me. If any, act on them."
```

**Pros:** Dead simple. No new infra. Uses existing Claude Code.
**Cons:** 10-minute latency is not "real-time." Every wake burns tokens even if there's nothing to do. Headless Claude in a cron has the confirmation-prompt problem for destructive ops.

### Option G: Long-running daemon with MCP server

Build a lightweight MCP server that:
- Holds a persistent Claude SDK connection
- Subscribes to Supabase/git/webhook for incoming messages
- Streams messages into the Claude SDK as user turns
- Persists conversation state across messages

**Pros:** Truly real-time. Claude maintains context across messages. Best UX for multi-turn coordination.
**Cons:** Significant dev work. Claude SDK not CLI. Moves away from Claude Code's session model toward a pure Claude API integration. Loses the "Jesse-can-review-everything-in-git" property unless the daemon also writes to git.

## Cross-cutting constraints

1. **Prompt injection risk.** Message content from one Claude can't be trusted to directly drive the other Claude's actions. Any trigger that feeds message content into Claude's prompt needs strict isolation. The safest pattern: "Here's a message from R1VS at `<path>`. Pull it and decide what to do" — never dump the raw body into the prompt.

2. **Cost.** Every Claude Code invocation is tokens. A real-time system that invokes Claude on every message ping can get expensive fast. Need rate-limiting / batching for low-priority messages.

3. **Confirmation-prompt problem.** Claude Code is interactive by design. Destructive operations (file delete, force push, git rebase) require explicit user approval. Headless mode has bypass flags but using them defeats the safety property. Solution candidates: (a) restrict headless triggers to read/append-only operations, (b) build a confirmation-queue UI that surfaces pending approvals to Jesse's phone.

4. **Idempotency.** If the trigger fires twice, Claude shouldn't double-act. Need message-id-based dedup.

5. **Audit trail.** Whatever we build, Jesse still wants the git-backed persistent log. The new system should be a *trigger* layer, not a *replacement* for the git message bus.

6. **Mini's security perimeter.** The Mini doesn't have Slack. Any solution that leaks business DMs or authenticated sessions from the MacBook to the Mini breaks the original reason Slack was excluded.

## What I'd ask the next session to evaluate

1. **Of the 7 options above, which is the right first cut?** My instinct is Option A (Supabase realtime + agent) with Option C (Telegram ping) as a fallback notification. But this is based on intuition, not analysis — push back if you see a better path.

2. **Is there an Option H we're missing?** New Claude Code features (hooks, scheduled tasks, MCP servers) that could change the game? Something like a Claude Code "inbox" primitive?

3. **What's the MVP?** A 2-day prototype that proves the pattern end-to-end, so Jesse can stop being the copy/paste middleware *today* even if the full system takes weeks?

4. **How do we handle the confirmation-prompt problem?** Concrete policy on which operations can happen headlessly vs. which always require Jesse to approve on his phone?

5. **Is there a way to leverage the existing CRM as the UI?** If Jesse's already watching the CRM, surfacing pending Claude messages + approval requests there could fold the whole system into one interface he's already using.

## Tonight's reality check

Right now, for R1VS to send this brief to Mini, Jesse has to:
1. Copy the brief from this Claude Code chat
2. Paste into Slack (on MacBook)
3. Open his email
4. Send himself the Slack content as an email (because Mini can't read Slack)
5. Switch to Mac Mini
6. Open the email
7. Copy the content
8. Paste into Claude Code on Mini
9. Wait for Mini's response
10. Screenshot or retype the response
11. Email it to himself
12. Switch back to MacBook
13. Open the email
14. Paste into R1VS's chat

That's the problem. We should be embarrassed it's still this.

---

## Appendix: What R1VS does *not* need

This problem brief is about **R1VS ↔ Mini real-time coordination**. It is NOT about:

- **Bruce (Open Claude on Mini)** — Bruce is task-level employee, not peer coordination. The existing photo handoff contract (briefs in git, deliveries back in git) works for Bruce because his job is discrete: pull photos for a list of slugs, commit, done. That flow doesn't need real-time trigger because it's batchable.
- **Site-review workflow with Jesse** — Jesse reviewing sites at a human pace is fine. This is purely about removing him as the copy/paste middleware between two AI agents.
- **External integrations** — Slack, email, customer CRM touchpoints. Those are separate problems.

The scope is narrow: **two Claude Code instances need a reliable, low-latency, auditable way to exchange structured messages without Jesse's hands in the loop.**

---

*Drafted by R1VS on MacBook, 2026-04-17. Hand this to a fresh Claude session (or a human architect, or both) and ask for a concrete proposal. The git message bus is the floor; the trigger layer is the ceiling.*
