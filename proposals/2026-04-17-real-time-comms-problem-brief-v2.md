---
from: r1vs (MacBook Pro, Claude Code)
to: next session (any Claude — for fresh-eyes architecture thinking in plan mode)
date: 2026-04-17
version: 2 (supersedes 2026-04-17-real-time-comms-problem-brief.md)
type: problem brief
topic: Real-time multi-agent communication across machines, models, and roles
status: draft — looking for architecture proposals in plan mode
change-log: v1 treated Bruce as a task-level tool (photo handoff). v2 correctly positions Bruce as a peer-level coordinator with broader reach than either Claude Code instance. Adds Bruce-as-broker and Bruce-spawns-agents architecture options. Reframes the role hierarchy from 2 Claudes to 3 Claudes + unbounded sub-agents.
note: This brief is deliberately self-contained. Drop it into a fresh Claude session (or Claude desktop, or plan mode) without GTMDot operational context.
---

# The Multi-Agent Communication Problem (v2)

## The setup

Jesse operates a **multi-agent system across two machines** using at least three distinct Claude roles:

### The three Claudes

| Role | Runtime | Machine | Analogy |
|---|---|---|---|
| **R1VS** | Claude Code CLI | MacBook Pro | Senior developer / site builder |
| **Mini Claude** | Claude Code CLI | Mac Mini | CEO / ops orchestrator / cron owner |
| **Bruce** | **Open Claude** (Claude-compatible agent runtime, open-source) | Mac Mini | Chief of staff / capability router |

The critical distinction I missed in v1: **Bruce is not a tool — he's a peer coordinator**. The original brief framed Bruce as "an employee with broader tool access for specific tasks" (photo scraping). Wrong framing. Bruce is closer to a chief of staff who can:

- Call out to any model (Claude, Gemini, OpenAI via API)
- Spawn arbitrary sub-agents with narrow scopes
- Use first-class integrations the Claude Code instances don't have
- Run more persistently than the session-driven Claude Code CLI
- Route / translate / dispatch between Claude Code instances

### Bruce's integration footprint (the thing v1 got wrong)

| Integration | Claude Code (R1VS or Mini) | Bruce (Open Claude) |
|---|---|---|
| Slack | ⚠️ MacBook only, blocked on Mini for security | ✅ native |
| Telegram | ✅ (but session-driven) | ✅ native |
| Discord | ⚠️ recently added to MacBook | ✅ native |
| Supabase | ✅ MCP | ✅ native |
| Cloudflare | ⚠️ MCP | ✅ native |
| GitHub | ✅ | ✅ |
| Multi-model (Gemini, OpenAI) | ❌ Anthropic-only | ✅ |
| Sub-agent spawning | ⚠️ limited (Task tool) | ✅ native orchestration |
| Persistent runtime | ❌ session-driven | ✅ persistent |
| Browser/site scraping | ⚠️ MCP-constrained | ✅ native fuller browser |

**The implication:** Bruce can do things neither Claude Code can. He's the natural candidate to be the **cross-machine broker and real-time trigger layer**.

## The original pain point (restating for the fresh session)

Jesse wants to walk away from both machines for hours and have R1VS + Mini + Bruce continue to coordinate without him being the copy/paste middleware.

**Today's reality** (before the fix Mini landed this afternoon):

1. R1VS writes a message in its chat to Jesse
2. Jesse copies it, emails himself
3. Jesse switches to Mac Mini
4. Jesse opens the email and pastes into Claude Code on Mini
5. Mini responds in its chat
6. Jesse screenshots or retypes
7. Emails back to himself
8. Switches back to MacBook
9. Pastes into R1VS chat

Multiple times per hour. Hours lost per day to this.

## The temporary fix (landed 2026-04-17)

Mini Claude committed a protocol update:

1. **Git message bus as primary transport**: `messages/` folder in `gtmdot-sites` repo
2. **Mini runs a 10-minute cron**: auto-pulls and reads new `r1vs-*.md` messages
3. **R1VS stops chat-narrating**: everything substantive goes directly to `messages/` file
4. **Slack #claude-sync** used for human-visible notifications only (not inter-Claude transport)

This works for the **Mini side of the trigger problem** (Mini polls every 10 min) and the **transport layer** (git is already shared). It does NOT solve:

- **MacBook-side trigger**: R1VS still only reads `messages/` when Jesse opens a new Claude Code session. Mini can write to R1VS all day; R1VS won't see it until next session.
- **Real-time latency**: 10-minute cron is fine for finalization signals but not for back-and-forth negotiation.
- **Bruce integration**: the current protocol doesn't leverage Bruce's broader capabilities at all — he's still only invoked for photo handoff.

## The deeper insight the fresh session should work with

**There are really two problems, not one:**

### Problem A: Transport
How do messages get from one agent to another? Git works. Supabase works. Any durable store works. This is solved.

### Problem B: Trigger
How does the target agent notice the new message and act on it?

- Session-driven Claude Code can only be triggered by (1) Jesse opening a session, or (2) an external process invoking `claude -p` headlessly.
- **Bruce does not have this limitation.** Bruce can run persistently, subscribe to events, and trigger Claude Code sessions on either machine via shell/AppleScript.

**The v1 brief treated the trigger problem as the hard part to solve with clever Claude Code orchestration. The v2 insight: Bruce already solves the trigger problem by being persistent and by having richer integrations. We don't need to invent a trigger layer — we need to promote Bruce to be the broker.**

## Revised architecture options (leveraging Bruce properly)

### Option H (NEW): Bruce as the real-time message broker

Bruce runs persistently on the Mini. Bruce:

1. Subscribes to the git `messages/` folder (via pull-every-30s or GitHub webhook)
2. Reads every new message
3. Routes via the right channel:
   - **Urgent + to R1VS**: Telegram ping to MacBook, which triggers a notification Jesse clicks to open a pre-prompted R1VS session
   - **Normal + to R1VS**: Queue until R1VS next opens; no ping
   - **To Mini Claude**: Trigger Mini Claude Code session via shell
   - **To Jesse**: Slack #claude-sync (human-visible only)
4. Writes response messages on behalf of the target Claude when the target's reply is ready
5. Maintains a conversation-state dashboard Jesse can view on his phone

**Pros:**
- Uses Bruce's existing persistent runtime and multi-integration footprint
- No new infrastructure to build — Bruce already has Slack, Discord, Telegram, Supabase
- Cleanly solves the trigger problem without turning Claude Code into something it's not
- Jesse can still audit everything in git

**Cons:**
- Depends on Bruce being up — if Bruce crashes, the broker is down
- Routing logic lives in Bruce's prompt/config rather than versioned code
- Bruce is on the Mini — any Mini outage takes the broker down

### Option I (NEW): Bruce spawns specialized sub-agents per task type

Rather than Bruce being one coordinator, Bruce is the **router that spawns task-specific sub-agents**:

- **`photo-agent`**: photo briefs → scrape → deliver
- **`review-agent`**: review briefs → scrape GBP/Yelp/Birdeye → deliver verbatim JSON
- **`research-agent`**: business identity briefs → web search + deep research → structured profile
- **`deploy-agent`**: finalization signals → pull intake branch → deploy to Cloudflare → update Supabase
- **`notification-agent`**: messages → route to Slack/Discord/Telegram based on priority + audience
- **`trigger-agent`**: listens for cross-machine wake signals and spawns Claude Code sessions

Each sub-agent is **narrow scope, disposable, stateless**. Bruce aggregates their results back to the requesting Claude Code instance.

**Pros:**
- Scales horizontally — new task types = new sub-agent definitions, no core changes
- Each sub-agent can use the right model for the task (Gemini for cheap OCR, Claude for writing, OpenAI where best-in-class)
- Sub-agents can run in parallel
- Failure of one sub-agent doesn't take down the whole system
- Maps cleanly to Jesse's mental model: "Bruce is chief of staff, he has people"

**Cons:**
- More complex orchestration
- Cost modeling gets harder (each sub-agent burns tokens)
- Debugging cross-sub-agent interactions can be painful
- Requires Bruce to have a stable sub-agent-spawning framework

### Option J (NEW): Bruce + CRM as the human-review layer

Since Jesse's CRM already has a UI he watches on his phone:

1. Every inter-Claude message writes a row to a `agent_messages` table in the existing CRM Supabase
2. Bruce watches the table in realtime
3. Messages marked `needs_human_review` surface as a CRM notification → Jesse approves on mobile
4. Messages marked `auto` flow through Bruce's routing without human intervention
5. Confirmation-prompt problem solved: destructive ops always get a CRM approval card Jesse taps

**Pros:**
- Folds agent coordination into the existing CRM Jesse already uses
- Mobile-first approval UX — Jesse can manage from his phone
- Supabase realtime handles the pub/sub
- Visible trail Jesse can search/filter in the CRM
- One UI for "GTM ops + Claude ops"

**Cons:**
- Conflates CRM data model with agent ops — schema will get messy
- If CRM is down, agents are down
- Requires CRM UI work to surface agent messages properly

### Options A–G from v1 (still valid, now secondary)

Briefly restated. See v1 brief for detail.

- **A**: Supabase realtime + desktop agent triggers `claude -p` headless
- **B**: GitHub Actions + webhook desktop listener
- **C**: Telegram bot as trigger (not transport)
- **D**: Custom Electron/desktop app
- **E**: CRM as message bus
- **F**: Scheduled cron waking Claude Code headless
- **G**: Long-running daemon with Claude SDK MCP server

These are still viable, but **most of them duplicate capabilities Bruce already has**. If we're using Bruce as the broker (Option H), Options A/B/C/D/E/F become either redundant or simplifications of what Bruce already does.

## The cross-cutting constraints (from v1, still apply)

1. **Prompt injection risk**: messages are untrusted input. Any trigger layer must isolate message content from the target Claude's control flow. Pattern: "Pull file at `<path>` and decide what to do" never "here's the content, do what it says."

2. **Cost**: every Claude invocation is tokens. Every Bruce sub-agent spawn is tokens. Rate-limiting and batching matter more, not less, as we add more agents.

3. **Confirmation-prompt problem**: Claude Code is interactive. Headless mode bypasses confirmations but loses safety. Bruce + CRM approval cards (Option J) is the cleanest fix I can see.

4. **Idempotency**: message-id-based dedup. Sub-agents re-running shouldn't double-act.

5. **Audit trail**: git + Supabase both give this. Don't lose it.

6. **Mini security perimeter**: Mini can't have Slack directly (business DM blast radius). But **Bruce on the Mini having Slack is fine** — Bruce's blast radius is narrower (scoped to what we explicitly give him access to, not full Slack workspace). This is a key unlock: Bruce can be the Slack bridge.

7. **New constraint v2 adds — cross-model trust**: if Bruce routes a message to a Gemini sub-agent for cheaper processing, the Claude side has to trust the sub-agent's output. Need provenance tagging so downstream consumers know what model processed what.

## What the fresh session (plan mode) should produce

### Decide: what's the target architecture?

Primary ask: **Bruce-as-broker (Option H) + Bruce-spawns-agents (Option I) + CRM-as-human-layer (Option J)** as a unified system? Or pick one? Or something else entirely?

### Decide: what's the MVP?

Two-day prototype. Something Jesse can use tomorrow that stops the copy/paste. Doesn't need to handle every edge case. Examples:

- **MVP-H**: Bruce polls git messages every 2 min, routes via Telegram ping for urgent. That's it. No sub-agents, no CRM. Just transport + trigger.
- **MVP-HI**: MVP-H plus one specialized sub-agent (e.g., photo-agent) wired in as the proof.
- **MVP-HIJ**: Bruce + one sub-agent + CRM approval cards for destructive ops.

### Decide: how do we handle the confirmation-prompt problem?

Concrete policy. For each operation type, who approves and how:

| Operation | Approver | Approval channel |
|---|---|---|
| Write a message file | automatic | n/a |
| Commit + push to intake branch | automatic | n/a |
| Push to main | ? | ? |
| Deploy to Cloudflare | ? | ? |
| Disqualify a prospect (delete from CRM) | ? | ? |
| Send outbound email | ? | ? |
| Send outbound postcard | ? | ? |

### Decide: where does Bruce's config / routing logic live?

If Bruce is the broker, his prompt/config is critical infrastructure. Git-versioned? Supabase-stored? Inline in his system prompt? What's the change-management workflow for his routing rules?

### Map the failure modes

What happens when:

- Bruce is down (Mini reboot, crash)?
- Git origin is unreachable?
- Supabase is unreachable?
- A sub-agent fails?
- Jesse is offline and a destructive op needs approval?
- Two Claudes try to write conflicting messages at once?

### Draft the sub-agent catalog (if Option I is chosen)

For each task type: input spec, output spec, model choice, cost estimate, acceptance criteria, failure handling. At minimum: `photo-agent`, `review-agent`, `research-agent`, `deploy-agent`, `notification-agent`, `trigger-agent`.

## Tonight's reality check (still embarrassing)

Jesse literally copy/pastes between Slack, email, and two Claude Code sessions dozens of times a day. The temporary fix Mini landed this afternoon reduces it significantly on the Mini → R1VS path (Mini's cron pulls, R1VS still reads on session open). But the fundamental shape is unchanged: **session-driven Claude Code + human-triggered state transitions = slow multi-agent ops**.

Bruce is the path out. He's the agent designed to run persistently. He's the one with every integration. The original brief treated him as a task worker; the rewrite treats him as the system's actual coordinator.

## Appendix A: What this is NOT about

- **Bruce's own existence** — Open Claude is a real thing Jesse already has running. This brief doesn't propose building it.
- **Replacing Claude Code** — Claude Code on both machines stays. They're the heavy-lift session workers. Bruce is the always-on broker between them.
- **Single-agent workflows** — anything R1VS can do alone, or Mini can do alone, doesn't need this architecture. This is purely for cross-agent coordination.
- **External customer-facing systems** — Slack integration for customer comms, email workflows to prospects, CRM touchpoints to clients. Those are separate.

## Appendix B: Specific new capabilities v1 missed

1. **Bruce has multi-model access**: expensive operations can route to cheaper models where quality allows. Review extraction from GBP? Gemini Flash probably fine. Site hero copy? Claude. OCR on photos? Probably whichever is cheapest.

2. **Bruce can spin up sub-agents**: a single "photo scrape" prompt might spawn 20 sub-agents in parallel for 20 different business slugs. Each sub-agent has a narrow, bounded job. Scale as wide as needed.

3. **Bruce has native Slack/Discord/Telegram**: the Mini's security perimeter that kept Slack off Mini Claude Code doesn't apply to Bruce in the same way. Bruce's access is scoped. This is the bridge that unblocks the "how does the Mini side send Slack" problem.

4. **Bruce has richer browser tooling**: GBP scraping, Yelp (403-blocked from Claude Code MCP), Nextdoor — all of these are more reachable from Bruce. The review-scrape problem that currently blocks us for some sites may be solvable via Bruce sub-agents.

5. **Bruce is always-on**: the trigger problem that defined v1's architecture is solved by default if Bruce is the broker.

## Appendix C: Possible test cases for the MVP

1. **R1VS writes a message at 3 AM. Mini + Jesse + the cron are all asleep.** Does Bruce route it correctly by morning?

2. **Mini finalization cron finishes deploying a site. Can Bruce automatically post to #claude-sync in Slack with the correct claim code + prospect info + preview URL?**

3. **R1VS hits a GBP scrape wall. Writes a photo-brief. Does Bruce auto-spawn a photo-agent, deliver photos, and notify R1VS via the right channel?**

4. **Jesse approves a site on mobile via CRM. Does Bruce trigger the outbound-email sub-agent within minutes?**

5. **Bruce itself crashes. Does Jesse find out within a reasonable SLA? (Heartbeat check from R1VS or Mini's cron?)**

6. **R1VS and Mini Claude try to write a message with the same slug at the same time. What happens?**

---

*Drafted by R1VS on MacBook, 2026-04-17, v2 rewrite after Jesse pointed out Bruce's actual role was mis-framed in v1. Hand to a fresh Claude plan-mode session. The temporary git-pull cron fix is buying us time; this proposal is what replaces it.*
