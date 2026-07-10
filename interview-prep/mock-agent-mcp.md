# Mock Interview — Agentic Automation + MCP

> Self-contained practice mock for the **BCG X Lead FDE** loop, focused on the **agent design +
> Model Context Protocol (MCP)** area (your interviewer's home turf). Companion to
> [BCG-X-FDE-prep.md](BCG-X-FDE-prep.md) — see §3.6 (agent architecture), §3.10 (Anthropic/Claude),
> §3.11 (MCP), and Case 2 (agentic support).

---

## How to use this file

**Solo mode (recommended for "try later"):**
1. Start a timer: **25–30 min** for the main case, **5 min** for the warm-up volley.
2. Read the **prompt only**. Do **not** expand any `▸ Reveal` block yet.
3. Speak your answer **out loud** (or type it in the scratchpad at the bottom).
4. Only then expand the collapsed blocks and compare against the model answer + signals.
5. Score yourself with the rubric. Log the attempt in the table at the end.

**Agent mode:** hand this file to an AI agent and say *"run this mock in the interviewer persona,
one prompt at a time, don't reveal answers until I respond."* It should probe with the curveballs
below in order and grade you against the rubric.

> Rule: no peeking. The whole value is answering *before* you see the model answer.

---

## Warm-up — MCP rapid-fire (5 min, answer cold)

Say a crisp 1–2 sentence answer to each, then expand to check.

1. What problem does MCP actually solve?
2. Name MCP's three server primitives and **who controls each**.
3. MCP vs. plain function-calling — what's the difference?
4. What's the #1 risk of adopting MCP, and how do you mitigate it?
5. How do you tier Claude models for cost, and where does an agent escalate?

<details>
<summary>▸ Reveal warm-up answers</summary>

1. **M×N → M+N.** Instead of a custom integration per (app × tool), each system exposes **one**
   MCP server that any MCP-speaking app/model can reuse → standard, reusable, vendor-neutral.
2. **Tools** (model-controlled — the LLM chooses to call), **Resources** (app/host-controlled —
   read-only context the app pulls in), **Prompts** (user-controlled — reusable templates the user
   invokes, e.g. slash commands).
3. Function-calling is *how one app's model invokes a tool*; MCP is *a standard protocol + transport*
   (JSON-RPC over stdio / streamable HTTP) so those tools are reusable across apps and models and can
   run as separate, even remote, servers.
4. **Security** — untrusted servers, prompt injection via tool results, over-broad permissions.
   Mitigate: least-privilege scoped tools, validated I/O, auth (OAuth for remote), sandboxing, audit
   logs, HITL on write/high-risk actions.
5. **Haiku → Sonnet → Opus** cascade: cheap tier handles the bulk; escalate to a stronger tier on
   **low confidence / classifier uncertainty / high-stakes action**. Tie the threshold to the SLA and
   per-request budget.

</details>

---

## Main case — Tier-1 support agent (with MCP)

> **Prompt (read this, then talk for 25–30 min before expanding anything):**
>
> *"A B2B SaaS client wants an agent that resolves Tier-1 customer-support tickets end-to-end: read
> the ticket, look up the account, take an action (e.g., reset, refund, plan change), and reply. They
> want to expose their internal systems to the agent **via MCP**. Walk me through how you'd design,
> ship, and de-risk it — and be specific about the MCP layer."*

Answer first. Then work through the reveals below **in order**, one at a time.

<details>
<summary>▸ Step 1 — Clarify before designing (did you ask these?)</summary>

Strong candidates scope **before** drawing. You should have asked most of:

- **Success metric:** deflection rate? CSAT? handle-time reduction? (drives the whole design)
- **Action risk:** which actions are **reversible** vs. high-risk (refunds, plan changes, deletes)?
- **Volume & latency:** tickets/day, QPS, acceptable response time?
- **Existing tools/APIs:** what systems (CRM, billing, KB) and do they already have APIs?
- **Data residency / compliance:** on-prem/VPC only? PII handling? regulated industry?
- **Escalation policy:** when does it hand off to a human? what's the tolerance for a wrong action?
- **Model/hosting constraint:** hosted API allowed, or self-host required?

> **Senior tell:** naming the SLA, the per-request budget, and the data-residency requirement first.

</details>

<details>
<summary>▸ Step 2 — Reference architecture (compare to yours)</summary>

**Least-agentic design that works** — a mostly-deterministic pipeline with LLM steps, agency added
only where branching genuinely needs it:

```
intake → classify/route (intent) → retrieve policy/KB (RAG)
       → PLAN → call typed tools (via MCP) with validation
       → draft reply → guardrails → HITL gate on risky actions
       → resolve OR escalate → log full trajectory for eval
```

**MCP layer specifically:**
- Each backend (account lookup, billing/refund, KB search) is wrapped as an **MCP server** exposing
  **least-privilege tools** with typed, validated I/O.
- The agent host runs an **MCP client** per server; **read-only** data (account details, policy
  docs) exposed as **Resources**, **executable** operations (refund, reset) as **Tools**.
- Remote servers are **authed (OAuth)**, scoped per tenant, and rate-limited.

**Reliability toolkit (interviewers dig here):** typed tool I/O + schema validation · retries with
backoff · **deterministic fallbacks** · max-steps / budget caps · **idempotency keys** on actions ·
**HITL** on high-risk/irreversible actions · trajectory eval + task-success rate · injection guardrails.

**Trade-offs to name:** single agent vs. supervisor+workers vs. deterministic pipeline (prefer the
least autonomy that works); autonomy vs. safety (HITL gates); latency vs. thoroughness.

> **Senior tell:** you start from a deterministic pipeline and add agency *surgically*, and you treat
> the MCP tools as a **least-privilege, validated** boundary — not "expose everything."

</details>

<details>
<summary>▸ Curveball 1 — "It issued a wrong $10k refund. Now what?"</summary>

- **Prevent:** HITL approval + **spend caps** on the refund tool; mark it high-risk/irreversible.
- **Contain:** **idempotency keys** (no double-refund on retry); post-action verification step.
- **Recover:** reversible-action design + an audit log to trace and roll back.
- **Systemic:** the refund tool's MCP server enforces server-side limits, so a jailbroken prompt
  still can't exceed policy (defense in depth — don't trust the model to self-limit).

</details>

<details>
<summary>▸ Curveball 2 — "How do you evaluate it before go-live?"</summary>

- **Trajectory eval** (was each step/tool call correct?) + **final task success** (ticket resolved?)
  + **tool-call accuracy** + business metric (deflection / CSAT).
- **Offline:** golden set of historical tickets → run agent → grade with metrics + **LLM-as-judge**
  (pairwise, rubric, calibrated vs. human labels — report judge–human agreement).
- **CI gate:** thresholds block a prompt/model/tool change that regresses.
- **Online:** staged rollout, A/B vs. current process, guardrail hit-rate, human review queue.

> This is *your* differentiator (RAGAS + LLM-as-judge) — make it a recurring theme.

</details>

<details>
<summary>▸ Curveball 3 — "The agent loops forever / burns budget."</summary>

- **Max-steps** and **token/cost budget caps** per ticket; hard stop → escalate to human.
- **Loop detection** (repeated identical tool calls / no state progress).
- **Deterministic fallback** path when the agent can't converge.
- Log the trajectory so you can find *why* it looped and fix the plan/tooling.

</details>

<details>
<summary>▸ Curveball 4 — "Prompt injection via the ticket text (or a tool result)."</summary>

- **Never treat retrieved/user text as instructions** — separate instructions from data.
- **Scope tool permissions** (least privilege); the model can't call what it isn't granted.
- **Validate tool outputs**; treat **MCP tool results as untrusted** (injection can arrive *through*
  a tool response, not just the ticket).
- Guardrail classifiers on input/output; sandbox actions; HITL on high-risk; audit everything.

> **Senior tell:** you flag the *tool-result* injection vector, not just the user message.

</details>

<details>
<summary>▸ Curveball 5 (MCP) — "Why MCP here at all, vs. just wiring the APIs directly?"</summary>

- **Reuse / decoupling:** wrap each system as a server once → reusable across this agent, future
  agents, and **different models** (no lock-in). Swap Claude ↔ another model without rewiring tools.
- **Maintainability:** the integration boundary is standardized (JSON-RPC, typed schemas) instead of
  bespoke glue per system — exactly the lever that matters across many client engagements.
- **Be honest about when it's overkill:** for a single agent hitting 2 stable internal APIs, direct
  function-calling may be simpler. MCP pays off with **multiple tools/apps/models** or a reusable
  internal tool catalog.

> **Senior tell:** you justify MCP by *reuse + decoupling*, and admit when direct integration wins.

</details>

<details>
<summary>▸ Curveball 6 (MCP) — "MCP vs. function-calling — aren't they the same?"</summary>

No. **Function-calling** is the model capability of *choosing to invoke a described tool within one
app.* **MCP** is a **protocol + transport standard** that packages those tools behind servers so they
are **reusable across apps and models** and can run **out-of-process / remotely** (with auth). MCP
*uses* function-calling under the hood; it standardizes the plumbing around it.

</details>

<details>
<summary>▸ Curveball 7 — "No data may leave the client's VPC / regulated industry."</summary>

- **Claude via Bedrock/Vertex in-VPC** (or self-hosted open-weight if truly air-gapped); Anthropic
  doesn't train on API data — clean privacy story.
- **MCP servers run inside the VPC**, remote transport authed (OAuth), per-tenant isolation.
- PII detection/redaction, doc-level access control on any retrieval, audit logging, model pinning.

</details>

<details>
<summary>▸ Curveball 8 — "Costs are exploding at scale."</summary>

- **Model cascade** (Haiku first, escalate on low confidence) + **prompt caching** for the stable
  system prompt / tool definitions / policy docs.
- Semantic + exact **caching** of repeated intents; shorter context; batch/async where possible.
- Cap tokens per ticket; route trivial intents to a deterministic path (no LLM at all).

</details>

---

## Senior signals vs. red flags

<details>
<summary>▸ Reveal</summary>

**Senior signals**
- Clarifies metric / SLA / risk / residency **before** designing.
- Starts from a **deterministic pipeline**, adds agency surgically.
- Strong **reliability + HITL** story; **idempotency** and **spend caps** on actions.
- Evaluates **trajectories**, not just final text; CI gate; judge calibrated vs. humans.
- Treats MCP tools as a **least-privilege, validated, untrusted** boundary; justifies MCP by
  **reuse/decoupling** and admits when it's overkill.
- Flags **injection via tool results**, not just the ticket text.

**Red flags**
- "Let the agent figure it out"; multi-agent for its own sake; no guardrails.
- No eval story, or "we'll eyeball outputs."
- Exposes broad/unscoped tools via MCP; trusts tool results blindly.
- Ignores data-residency; no HITL on irreversible actions; no idempotency.

</details>

---

## Self-grading rubric (score 1–5 each; Lead bar = ≥4)

| Dimension | 1–5 | Notes |
|---|---|---|
| Problem framing (clarified before designing) | | |
| Technical depth (agent + MCP specifics) | | |
| Trade-off reasoning (named alternatives + why) | | |
| Production maturity (eval, reliability, HITL, cost, security) | | |
| Communication (top-down, concise) | | |
| Business sense (metric, MVP, phasing, ROI) | | |

**3 concrete fixes for next time:**
1.
2.
3.

---

## Attempt log

| Date | Time taken | Framing | Depth | Trade-offs | Prod. maturity | Comms | Business | Weakest dim → study |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

---

## What to study next (pointers)

- MCP primitives + control model + security → [BCG-X-FDE-prep.md](BCG-X-FDE-prep.md) §3.11
- Anthropic/Claude framing (Building Effective Agents, tiers, caching) → §3.10
- Agent reliability toolkit → §3.6
- Full Case 2 model answer → §4, Case 2

---

## Scratchpad (type your spoken answer here before revealing)

```
(your answer)
```
