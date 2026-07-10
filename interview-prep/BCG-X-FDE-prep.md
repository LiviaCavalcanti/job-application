# BCG X — Lead Forward Deployed AI Engineer
## Interview Prep & Study Guide (for humans **and** agents)

> A living, self-contained practice resource. Read Section 0 first — it explains how a
> human studies from this file and how an AI agent should drive mock interviews and grade you.

---

## Table of Contents

0. [How to use this file](#0-how-to-use-this-file)
1. [The role & what is actually tested](#1-the-role--what-is-actually-tested)
2. [Candidate profile map (your edges & gaps)](#2-candidate-profile-map)
3. [Core mental models & cheat sheets](#3-core-mental-models--cheat-sheets)
4. [System-design case bank](#4-system-design-case-bank)
5. [Business → technical scoping cases (the BCG differentiator)](#5-business--technical-scoping-cases)
6. [Coding drills](#6-coding-drills)
7. [LLM / GenAI rapid-fire Q&A](#7-llm--genai-rapid-fire-qa)
8. [Behavioral & client-facing (STAR)](#8-behavioral--client-facing-star)
9. [Mock-interview protocol (agent-runnable)](#9-mock-interview-protocol-agent-runnable)
10. [Reading list](#10-reading-list)
11. [Video & course recommendations](#11-video--course-recommendations)
12. [4-week study plan](#12-4-week-study-plan)
13. [Glossary & one-liners](#13-glossary--one-liners)

---

## 0. How to use this file

### If you are the human (candidate)
- **Don't read passively.** For every case in Sections 4–5, cover the model answer, speak your
  answer out loud for 5–10 min, *then* compare.
- Work the **cheat sheets in Section 3 until they're reflexes** — the FDE signal is naming
  trade-offs unprompted.
- Track weak spots in a scratchpad; convert each into a flashcard.
- Do the coding drills (Section 6) in this repo's `.venv` — real keyboard, no autocomplete crutch.

### If you are an AI agent
When the user says *"run a mock,"* *"quiz me,"* *"drill me on X,"* or similar:
1. **Adopt the interviewer persona** from Section 1 (senior, pragmatic, constraint-driven, warm but probing).
2. Pick (or let the user pick) a case from Section 4/5, a drill from Section 6, or Q&A from Section 7.
3. **Present only the prompt.** Do **not** reveal the model answer.
4. Let the candidate respond. Then **probe with the follow-ups / curveballs** listed under that case, one at a time.
5. **Grade** against the rubric in [Section 1](#scoring-rubric-what-lead-signal-looks-like) and the per-case
   *Senior signals* / *Red flags*. Give a score per dimension + 3 concrete improvements.
6. Keep pressure realistic: interrupt vague hand-waving, ask "why not X?", force a decision when they straddle.
7. Log recurring weaknesses to `interview-prep/progress.md` (create if missing) so sessions compound.

> Agents: default to **one case per session** unless asked otherwise. End every session with a
> 3-bullet "what to study next."

---

## 1. The role & what is actually tested

**Forward Deployed Engineer (FDE)** = an engineer embedded *with the client* who both **builds
production AI systems** and **translates ambiguous business problems into scoped technical
solutions**. Popularized by Palantir; at BCG X it means: ship fast, harden under real
constraints (latency/cost/reliability/data-residency), and be trusted in the room by
non-technical executives. "Lead" adds architecture ownership, scoping, and mentoring.

### Interview buckets & weighting (typical for this profile)

| Bucket | Weight | What they're really checking |
|---|---|---|
| AI system design | ★★★★★ | Can you architect a production LLM/agentic system under real constraints? |
| Business→technical scoping | ★★★★★ | Can you turn a vague client ask into a phased, ROI-justified build? |
| LLM depth & evaluation | ★★★★ | Do you know what breaks in prod and how to measure quality? |
| Practical coding | ★★★ | Can you write clean, production-flavored Python (glue, async, data)? |
| MLOps / infra | ★★★ | Can you deploy, scale, monitor, and control cost? |
| Behavioral / client-facing | ★★★★ | Ambiguity handling, stakeholder management, trust, ownership. |

### Interviewer persona (for agents to emulate)
Senior FDE, 8+ yrs. Thinks in latency/cost/reliability/business-impact. Pragmatic, allergic to
hype and buzzword salad. Rewards: explicit assumptions, trade-off reasoning, "it depends on the
SLA/data-residency," MVP-first thinking, and knowing when *not* to use an LLM. Punishes:
over-engineering, ignoring the client's constraints, no evaluation story, hand-waving reliability.

### Scoring rubric (what "Lead" signal looks like)
Grade each on 1–5:
- **Problem framing** — clarifies scope/constraints before designing.
- **Technical depth** — correct, current, specific (not "we'll use a vector DB" and stop).
- **Trade-off reasoning** — names alternatives and *why not*; ties choices to constraints.
- **Production maturity** — eval, monitoring, failure modes, cost, security, rollout.
- **Communication** — structured (top-down), concise, adjusts for audience.
- **Business sense** — MVP, value/ROI, prioritization, risk.

**Lead bar:** ≥4 on framing, trade-offs, production maturity, and communication.

---

## 2. Candidate profile map

**You (ML Engineer @ Siemens + VTEX):** RAG, LLM, RAGAS, LLM-as-judge, BERT, NER, ETL,
Medallion, Airflow, AWS, Docker, Kubernetes, Python, anomaly detection, conversational AI,
prompt engineering.

### Your edges — lean into these
- **LLM evaluation** (RAGAS + LLM-as-judge) is genuinely differentiated. Most candidates can't
  answer *"how do you know it works before go-live?"* — you can. Make it a recurring theme.
- **End-to-end data → AI** (ETL / Medallion / Airflow) — you can design the *unsexy* data plumbing
  that actually decides whether an enterprise AI project succeeds.
- **Production delivery at two very different orgs** (industrial Siemens + e-commerce VTEX) = range.
- **Classical ML depth** (anomaly detection, NER, time series) — lets you answer *"when NOT to use an LLM."*

### Gaps to pre-empt (from your own note: seniority + client breadth)
| Gap | How to close it in the room |
|---|---|
| Client-facing ambiguity | Prepare 3 STAR stories where you *drove scope* with a stakeholder, not just executed. |
| Agentic reliability at scale | Be concrete on orchestration, guardrails, retries, eval of trajectories. |
| On-prem / regulated deploy | Have a "no external API allowed / air-gapped VPC" answer ready. |
| Cost at scale | Quantify: tokens × price × QPS; name caching/routing/quantization levers. |

### Ready-made talking-point bridges
- "At VTEX I built conversational AI + RAG; the hard part wasn't the model, it was **eval and
  guardrails** — which is why I standardized on RAGAS + an LLM-as-judge gate in CI."
- "At Siemens I did anomaly detection on [time-series/industrial] data; that taught me **when a
  deterministic model beats an LLM** on latency, cost, and auditability."
- "My ETL/Medallion background means I treat **retrieval quality as a data-quality problem**, not a
  prompt problem."

---

## 3. Core mental models & cheat sheets

### 3.1 The constraint star (say these out loud in every design)
Every production AI decision trades among:

| Axis | Levers |
|---|---|
| **Latency** | caching (exact + semantic), streaming, smaller/routed models, batching, speculative decoding, pre-compute |
| **Cost** | token budgets, prompt compression, caching, model cascade (small→large), fine-tune small vs prompt large, batch APIs |
| **Quality** | better retrieval, reranking, few-shot, fine-tune, larger model, HITL, ensembling |
| **Reliability** | output validation/schemas, retries+backoff, deterministic fallbacks, guardrails, eval gates, idempotency |
| **Privacy/Security** | on-prem/VPC, open-weight models, PII redaction, doc-level access control, prompt-injection defenses |
| **Maintainability** | prompt versioning, eval regression suites, observability, modular tools |

> **FDE tell:** start with *"What's the SLA, the budget per request, and the data-residency
> requirement?"* before drawing anything.

### 3.2 Decision framework — Prompt vs RAG vs Fine-tune vs Long-context vs Agent

| Need | Reach for |
|---|---|
| Inject **fresh / proprietary knowledge** | **RAG** (retrieval) |
| Change **behavior/format/style/tone** or teach a narrow task | **Fine-tune** (or LoRA) |
| Small, static context fits in window | **Long-context prompting** (simplest; watch cost & "lost in the middle") |
| **Multi-step task** with tools / branching / external actions | **Agent** |
| Simple, well-specified transform | **Plain prompt** (don't over-build) |

Rules of thumb: **RAG for knowledge, fine-tune for behavior.** They compose (fine-tune *and*
RAG). Prefer the *simplest* thing that hits the metric. Fine-tuning is a last resort for most
enterprise projects (data + MLOps cost).

### 3.3 When **NOT** to use an LLM
- Deterministic/auditable rules suffice (regex, lookup, business rules).
- Tight latency (<50ms) or high QPS where per-call cost/latency is prohibitive.
- Numeric forecasting / anomaly detection / ranking → classical ML or stats often win.
- Safety/compliance demands full determinism & explainability.
- The task is really a **data or search problem** in disguise.

### 3.4 Build vs Buy (API vs self-host)

| Prefer hosted API (OpenAI/Anthropic/Bedrock) | Prefer self-hosted open-weight |
|---|---|
| Speed to MVP, best frontier quality | Data can't leave VPC / air-gapped |
| Low/spiky volume | High steady volume (cost crossover) |
| Small team, no GPU ops | Need full control, custom fine-tunes, latency SLAs |
| | Regulatory / on-prem mandate (common in consulting!) |

### 3.5 RAG reference architecture

**Ingestion (offline):** source connectors → parse (PDF/HTML/tables/OCR) → clean/normalize →
**chunk** (semantic/structural, with overlap; keep metadata) → embed → upsert to vector store
(+ keyword index) → store ACLs/metadata.

**Retrieval (online):** query understanding (rewrite / decompose / HyDE) → **hybrid search**
(BM25 + dense) → **rerank** (cross-encoder) → filter by **ACL/metadata** → assemble context.

**Generation:** grounded prompt with citations → structured output → guardrails → stream.

**Eval loop (always present):** golden set + RAGAS (faithfulness, answer relevancy, context
precision/recall) + online feedback → CI gate + dashboards.

**Advanced levers to name when pushed:** contextual retrieval (Anthropic), parent-document /
small-to-big, multi-vector / ColBERT, query routing, semantic caching, GraphRAG for
multi-hop/entity questions (*you have a graph-RAG repo — use it as a concrete anecdote*).

**Enterprise curveball #1 (most-missed):** **document-level access control** — filter retrieval by
the *requesting user's* permissions, or you leak data. Bake ACLs into metadata and enforce at query time.

### 3.6 Agent reference architecture
**Components:** model + **tools** (typed, validated) + **planner** + **memory** (short/long) +
**orchestration** + **guardrails** + **observability**.

**Patterns:** ReAct (reason+act loop) · Plan-and-execute · Reflection/self-critique ·
Router · Multi-agent (supervisor + workers) — *justify multi-agent; often a deterministic
pipeline + one agent is more reliable.*

**Reliability toolkit (the part interviewers dig into):** typed tool I/O + schema validation ·
retries w/ backoff · **deterministic fallbacks** · max-steps / budget caps · idempotency keys ·
**human-in-the-loop** on high-risk actions · trajectory eval + task-success rate · guardrails
against prompt injection & runaway loops.

> **Lead framing:** "Start with the *least* agentic design that works — a fixed pipeline with LLM
> steps — and add autonomy only where branching/tool-use genuinely requires it."

### 3.7 Evaluation taxonomy (your strength — go deep)
- **Offline vs online:** golden datasets & CI gates vs A/B, user feedback, guardrail hit-rates.
- **Component vs end-to-end:** retrieval metrics (recall@k, MRR, nDCG) *separately* from generation.
- **RAG (RAGAS):** faithfulness, answer relevancy, context precision, context recall — diagnose
  *where* it breaks (retrieval vs generation).
- **LLM-as-judge best practice:** pairwise > absolute scoring; reference answers; chain-of-thought
  rubric; **calibrate against human labels**; ensemble/multiple judges; control for bias.
- **LLM-as-judge pitfalls:** position bias, verbosity bias, self-preference, sensitivity to
  formatting, cost, non-determinism → mitigate with randomized order, rubrics, and human spot-checks.
- **Agent eval:** trajectory correctness + final-task success + tool-call accuracy.
- **Production:** regression suite on every prompt/model change; track drift; close the loop with
  labeled feedback.

*"Your judge disagrees with humans 30% of the time — what now?"* → Inspect disagreements,
refine rubric, add few-shot exemplars, switch to pairwise, ensemble judges, and hold out a
human-labeled calibration set; report judge–human agreement (e.g., Cohen's κ) as a first-class metric.

### 3.8 Cost & latency optimization playbook
Semantic + exact **caching** · **model routing/cascade** (cheap model first, escalate on low
confidence) · prompt compression / shorter context · **streaming** for perceived latency ·
batching & async concurrency · quantization (INT8/4) for self-host · distillation / fine-tune a
small model on the big model's outputs · pre-compute embeddings · KV-cache reuse · move
rerankers/embedders to GPU.

### 3.9 Enterprise / regulated deployment checklist
Data residency (VPC / on-prem / region) · PII detection & redaction · **doc-level access
control** · audit logging · prompt-injection & jailbreak guardrails · content filtering ·
secrets management · SSO/RBAC · model/version pinning · **human-in-the-loop** for high-stakes ·
DR/failover · observability (traces, cost, latency, quality) · GDPR / EU AI Act awareness
(relevant to your EU/Siemens context).

### 3.10 Anthropic / Claude cheat sheet *(your interviewer's home turf — know these cold)*

> Your interviewer is Anthropic-certified and reposts Claude content, so expect Anthropic-flavored
> framing. **Deploy these when relevant; don't name-drop.** The senior tell is citing the right
> Anthropic technique *to solve a stated constraint*, not reciting the catalog.

| Concept | One-liner | Interview / FDE hook |
|---|---|---|
| **Claude model tiers** (Haiku · Sonnet · Opus) | fast-cheap → balanced → most-capable | Your **model cascade**: Haiku first, escalate to Opus on low confidence; tie tier to SLA/budget. |
| **"Building Effective Agents"** (Anthropic) | workflows (predefined code paths) vs. agents (LLM directs itself); start simplest | *This is your "least-agentic-design-that-works" doctrine.* Name the patterns (below) to sound fluent. |
| **Agent/workflow patterns** | prompt chaining · routing · parallelization (sectioning/voting) · orchestrator-workers · evaluator-optimizer | Pick the pattern by task shape; "evaluator-optimizer" = your LLM-as-judge loop in disguise. |
| **Contextual Retrieval** | prepend Claude-generated context to each chunk before embedding **and** BM25 | Concrete RAG-quality fix; cuts failed retrievals materially; cheap via prompt caching. |
| **Prompt caching** | cache large static prefix (system prompt, docs, tools); cached reads ~10% price + lower latency | Cost/latency lever for RAG with stable context and long tool/system prompts. |
| **MCP** (Model Context Protocol) | open standard to connect LLM apps to tools/data | See **§3.11** — the interviewer likely cares most here. |
| **Claude on Bedrock / Vertex** | Claude in-VPC/region; Anthropic doesn't train on your API data | Clean **data-residency + privacy** story for regulated clients (banks, EU). |
| **Constitutional AI (CAI)** | align via self-critique against a "constitution" + RLAIF | One-sentence answer if pushed on alignment/safety. |
| **Prompting Claude** | responds well to **XML tags** to delimit context/instructions; explicit roles; extended thinking | Signals model-specific prompt hygiene, not generic "prompt engineering." |
| **Claude Code** | Anthropic's terminal/agentic coding tool | Bridge to *your* graph-RAG code-patching repo. |

**Anthropic's core doctrine (adopt it — it aligns with FDE):** *"Find the simplest solution
possible; add complexity (single call → workflow → agent) only when it measurably helps."* Say this
and you're speaking their language.

### 3.11 Model Context Protocol (MCP) — deep dive *(they'll likely steer here)*

**What:** an **open standard (Anthropic, late 2024)** that standardizes how LLM apps connect to
external **tools, data, and systems** — "a USB-C port for AI."

**Why it exists — the M×N → M+N problem:**
```
Without MCP:  M apps  ×  N tools  =  M×N bespoke integrations
With MCP:     M apps  +  N tools  =  M+N   (each tool = 1 server, each app = 1 client)
```
Every integration used to be custom per (model/app × system). MCP makes each system expose **one**
server that **any** MCP-speaking app can use → integrations become reusable and vendor-neutral.

**Architecture (client–server over JSON-RPC 2.0):**
```
┌───────────── Host (LLM app: IDE, Claude Desktop, your agent) ─────────────┐
│   MCP Client  ───────────►  MCP Server  ──►  DB / API / files / SaaS       │
│   MCP Client  ───────────►  MCP Server  ──►  another system                │
└────────────────────────────────────────────────────────────────────────────┘
Transports: stdio (local) · streamable HTTP/SSE (remote, + OAuth for auth)
```

**Three server primitives (know the *control* model — that's the senior tell):**
| Primitive | Controlled by | What it is |
|---|---|---|
| **Tools** | **model** | executable functions the LLM chooses to call (side effects; validated I/O) |
| **Resources** | **application/host** | read-only context the app pulls in (files, DB rows, docs) |
| **Prompts** | **user** | reusable templates the user invokes (e.g., slash commands) |

*(Plus sampling — a server can ask the host's LLM for a completion — and roots for scoping.)*

**Why an FDE should care:** you constantly wire AI into a client's many systems. Wrap each system as
an MCP server once → reuse across projects and swap models freely (no lock-in). It decouples the
model from the integrations — exactly the maintainability lever consultants need.

**Trade-offs / risks (bring these unprompted):**
- **Security is the catch:** untrusted servers, **prompt injection via tool results**, over-broad
  tool permissions, auth (OAuth for remote). Scope permissions, validate tool I/O, sandbox, HITL on
  high-risk actions.
- **It's an integration standard, not intelligence** — you still design retrieval, eval, guardrails.
- **Curated typed tools often beat "expose everything"** — don't hand the model 200 tools; give it
  the few it needs (context bloat + error rate otherwise).

**Likely probes & crisp answers:**
- *"What problem does MCP actually solve?"* → M×N integration sprawl → M+N; standard, reusable,
  model-agnostic tool/data access.
- *"MCP vs. plain function-calling?"* → function-calling is *how a model invokes a tool in one app*;
  MCP is *a standard protocol + transport* so those tools are reusable across apps/models and can run
  as separate (even remote) servers.
- *"Would you expose an MCP server to a Claude agent inside a bank?"* → yes, but in-VPC, authed
  (OAuth), least-privilege tools, output validation, injection guardrails, audit logs, HITL on writes.
- *"Downside?"* → security surface + it doesn't solve quality/eval; still need the rest of the stack.

**Bridge to you:** *"My graph-RAG patching tool calls typed tools around Joern / graph ops — MCP is
how I'd standardize those so the same tools serve any client's agent."*

---

## 4. System-design case bank

> Format per case: **Prompt → Clarify first → Model architecture → Key trade-offs →
> Follow-up curveballs → Senior signals → Red flags.** Agents: reveal only the prompt.

### Case 1 — Enterprise RAG knowledge assistant *(your home turf; master this one)*
**Prompt:** *"A global bank has ~10M internal documents (policies, PDFs, wikis, tickets) across
20 systems. Build an assistant so employees get accurate, cited answers. Walk me through it."*

**Clarify first:** Who are the users & their permissions? Latency SLA? On-prem or cloud allowed?
Update frequency of docs? Accuracy bar & tolerance for wrong answers? Languages? Budget/QPS?

**Model architecture:** ingestion (connectors → parse incl. tables/OCR → chunk w/ metadata →
embed → hybrid index + ACLs) → retrieval (query rewrite → hybrid → rerank → **ACL filter**) →
grounded generation with **citations** and "I don't know" behavior → eval loop (RAGAS + feedback).

**Key trade-offs:** chunk size vs context coherence; hosted vs self-host (bank ⇒ likely VPC);
recall vs precision (rerank); freshness (incremental re-index) vs cost; latency (cache + stream).

**Follow-up curveballs:**
- *"Two users must get different answers from the same corpus."* → doc-level ACL at retrieval.
- *"No data may leave the bank's VPC."* → self-hosted open-weight + in-VPC vector store.
- *"How do you prove it's safe to launch?"* → golden set, RAGAS thresholds as CI gate, red-team
  for injection, staged rollout with human review.
- *"Answers are confidently wrong."* → grounding + citations + faithfulness metric + abstain;
  check whether failure is retrieval or generation (component eval).
- *"Costs are exploding at 50 QPS."* → semantic cache, routing, shorter context, batch embeds.

**Senior signals:** asks about ACLs & SLA before designing; separates retrieval vs generation
eval; has an abstain path; incremental re-indexing; names hybrid+rerank, not just "vector DB."

**Red flags:** jumps to "embed everything in Pinecone" with no ACLs; no eval story; ignores
data-residency; treats hallucination as unsolvable.

### Case 2 — Agentic workflow automation
**Prompt:** *"Design an agent that resolves Tier-1 customer-support tickets end-to-end (read
ticket, look up account, take an action, reply)."*

**Clarify:** Which actions are reversible/high-risk? Success metric (deflection rate, CSAT)?
Existing tools/APIs? Latency? Volume? Escalation policy?

**Architecture:** intake → classify/route → retrieve policy (RAG) → **plan** → call **typed tools**
(account lookup, refund, KB) with validation → draft reply → **guardrails** → HITL approval for
risky actions → resolve/escalate → log trajectory for eval.

**Trade-offs:** single agent vs supervisor+workers vs deterministic pipeline (prefer least
autonomy that works); autonomy vs safety (HITL gates); latency vs thoroughness.

**Curveballs:** *"It issued a wrong $10k refund."* → HITL + spend caps + idempotency + reversible
actions + post-action verification. *"How do you evaluate it?"* → trajectory eval + task success
+ tool-call accuracy + CSAT. *"It loops forever."* → max-steps/budget, loop detection, fallback.
*"Prompt injection via ticket text."* → input sanitization, tool-permission scoping, injection guardrails.

**Senior signals:** starts from deterministic pipeline, adds agency surgically; strong reliability
& HITL story; evaluates *trajectories*, not just final text.

**Red flags:** "let the agent figure it out"; no guardrails; multi-agent for its own sake; no eval.

### Case 3 — LLM evaluation & observability platform *(play to your RAGAS/judge strength)*
**Prompt:** *"A client has 5 LLM features shipping. Build the eval + monitoring so they can trust
and iterate on them."*

**Architecture:** golden datasets per feature → offline harness (task metrics + RAGAS +
LLM-as-judge, calibrated vs humans) → **CI gate** on prompt/model changes → tracing (spans,
tokens, cost, latency) → online feedback capture → dashboards + alerts on quality/cost/drift →
red-team & guardrail monitoring.

**Curveballs:** judge–human disagreement (Section 3.7); dataset drift; cost of running judges
(sample + cheaper judge for volume); regression detection; A/B design.

**Senior signals:** component-level RAG eval; judge calibration as a metric; CI gating; separates
offline vs online; treats eval as continuous, not one-off.

**Red flags:** "we'll eyeball outputs"; single absolute-score judge with no calibration; no CI.

### Case 4 — Real-time anomaly detection *(your Siemens angle; the "when not to LLM" case)*
**Prompt:** *"Streaming telemetry from thousands of machines. Detect anomalies with low latency
and few false alarms."*

**Architecture:** ingestion (Kafka/streaming) → feature extraction → model (statistical / IsolationForest
/ autoencoder / forecasting residuals) → thresholding + alerting → feedback labeling → drift
monitor → dashboard. LLM only for *explaining* alerts / natural-language summaries, not detection.

**Trade-offs:** precision vs recall (alert fatigue!); batch vs stream; supervised vs unsupervised
(label scarcity); model complexity vs latency/interpretability.

**Curveballs:** cold start / no labels; concept drift; seasonality; "why did it alert?" (explainability);
*"why not an LLM?"* → latency, cost, determinism, auditability.

**Senior signals:** picks classical ML deliberately; obsesses over false-positive cost; drift + feedback loop.

**Red flags:** reaching for an LLM; ignoring alert fatigue; no drift handling.

### Case 5 — Data pipeline for AI (Medallion) *(your ETL/Airflow strength)*
**Prompt:** *"The client's data is a mess: 20 sources, inconsistent schemas, PII everywhere.
Design the pipeline that feeds all their AI systems."*

**Architecture:** ingest → **Bronze** (raw, immutable) → **Silver** (cleaned, conformed, PII-handled)
→ **Gold** (feature/serving marts, embeddings) orchestrated by Airflow; data-quality checks
(Great Expectations), lineage, incremental loads, schema evolution, PII detection/redaction,
governance/catalog.

**Curveballs:** late/duplicate data (idempotent, dedup); schema drift; backfills; GDPR "right to be
forgotten" through the medallion; freshness SLAs; embedding re-computation on updates.

**Senior signals:** treats retrieval/AI quality as *data-quality* problem; lineage & governance;
idempotency; PII by design.

**Red flags:** one giant script; no data-quality gates; no PII handling.

### Case 6 — Multi-tenant AI SaaS feature *(your VTEX angle)*
**Prompt:** *"Add a GenAI feature to a SaaS product used by thousands of B2B tenants."*
**Focus:** tenant isolation (data + index), per-tenant cost attribution & quotas, noisy-neighbor,
per-tenant customization (prompts/knowledge), fair-share rate limiting, shared vs isolated
indexes, cost caps, abuse/prompt-injection, observability per tenant.

### Case 7 — Intelligent document processing at scale
**Prompt:** *"Extract structured fields from millions of messy PDFs (invoices/contracts) with
high accuracy and auditability."*
**Focus:** layout parsing/OCR, extraction (LLM vs specialized model), **confidence + HITL for
low-confidence**, schema validation, human review queue, eval vs ground truth, cost at volume,
throughput via batching/async.

---

## 5. Business → technical scoping cases

> The BCG differentiator. They score **structured thinking**, MVP definition, value/ROI, risk,
> and communicating to non-technical execs — as much as the tech.

### The scoping framework (say it explicitly)
1. **Clarify the business objective & metric** — what does success look like in $ / time / risk?
2. **Map constraints** — data availability & quality, budget, timeline, infra, compliance, team.
3. **Define the MVP** — smallest thing that proves value; what's explicitly out of scope.
4. **Choose the metric** — leading (technical: accuracy/latency) + lagging (business: cost saved).
5. **Phase the rollout** — POC → pilot (one team/region) → scale; decision gate at each.
6. **Name the risks** — technical (hallucination, data), adoption (change mgmt), compliance.
7. **Estimate value** — back-of-envelope ROI (users × time saved × rate, or error reduction × cost).

### Scoping case prompts (practice out loud)
- *"A CPG client says 'use GenAI to cut costs.' $2M, 6 months. What do you build?"*
- *"A manufacturer wants to 'reduce downtime with AI.' Where do you start?"* (ties to your Siemens exp)
- *"A retailer wants an AI shopping assistant. Scope it."* (ties to your VTEX exp)
- *"An insurer wants to automate claims. What's the phased plan and ROI?"*
- *"Exec asks: 'Should we build our own LLM?' How do you respond?"* (almost always: no — buy/fine-tune; explain why)

### Worked mini-answer (CPG "cut costs")
> "First, *cut costs where?* Let's target the biggest, most AI-amenable cost pool — say customer
> support (X agents, Y tickets/mo). **MVP:** a RAG assistant that drafts agent replies for the top
> 20 intents, human-in-the-loop, measured by **handle-time reduction** and **deflection rate**.
> Constraints: their data in Azure, PII, EU compliance ⇒ VPC deployment + redaction. **Phase 1**
> POC on historical tickets (offline eval, RAGAS + judge). **Phase 2** pilot with one team, A/B vs
> control. **Phase 3** scale + add self-serve deflection. **ROI:** if 10k tickets/mo × 3 min saved
> × loaded rate, that's ~$X/yr vs build cost $2M ⇒ payback in Z months. **Risks:** wrong answers
> (mitigate: HITL + abstain), adoption (change mgmt + agent buy-in), compliance (DPIA)."*

**Senior signals:** picks a concrete cost pool, defines a measurable MVP, names compliance,
quantifies ROI, phases with decision gates. **Red flags:** "we'll build a chatbot," no metric, no
phasing, no ROI, ignores adoption/change management.

---

## 6. Coding drills

Practical, production-flavored Python. Do them in this repo's `.venv`. Each has a clear spec so an
agent can auto-check. Time-box 15–25 min each.

1. **Semantic search from scratch** — given docs + a query and an `embed(text)->vector`, return
   top-k by cosine similarity. No libraries beyond numpy. *Extension:* add a keyword (BM25-ish)
   score and combine (hybrid).
2. **Retry with exponential backoff + jitter** — decorator `@retry(max_attempts, base_delay)`
   that retries on specified exceptions, caps delay, adds jitter, re-raises after budget.
3. **Token-bucket rate limiter** — allow N requests/sec across concurrent callers; thread-safe
   and/or async version.
4. **Async fan-out to an LLM API** — call `n` prompts with a **concurrency cap** (semaphore),
   collect results in order, handle per-item failure without killing the batch, add a timeout.
5. **Text chunker** — split long text into ~`size`-token chunks with `overlap`, prefer sentence/
   paragraph boundaries, attach `{doc_id, start, end}` metadata.
6. **Token counter / budgeter** — estimate tokens and truncate a context list to fit a budget,
   dropping lowest-priority items first while always keeping the system prompt.
7. **LLM output validator** — parse model output into a Pydantic schema; on failure, produce a
   repair prompt and retry once; return typed result or raise.
8. **Streaming SSE consumer** — consume a token stream and yield partial results (generator).
9. **Simple LLM-as-judge harness** — given `(question, answer, reference)`, build a pairwise
   rubric prompt, call a judge, parse a verdict, and aggregate agreement across a dataset.
10. **Dedup / idempotency** — given a stream of events with IDs, process each exactly once
    (in-memory + sketch of a Redis-backed version).

*Agent grading:* correctness, edge cases (empty input, all-fail, timeout), readability, and whether
they *tested* it. Ask them to add one test.

---

## 7. LLM / GenAI rapid-fire Q&A

Agents: ask these cold; expect crisp, correct answers. (Answers compressed here.)

- **What is temperature / top-p?** Sampling controls; lower = more deterministic. Use ~0 for
  extraction/eval, higher for creative.
- **Why does RAG reduce hallucination?** Grounds generation in retrieved evidence; but only if
  retrieval is good and the model is instructed to stay grounded + cite + abstain.
- **Chunk size trade-off?** Small = precise retrieval, fragmented context; large = coherent
  context, noisier retrieval, more tokens. Use small-to-big / parent-document to get both.
- **Hybrid search — why?** Dense captures semantics, sparse (BM25) captures exact terms/rare
  tokens/IDs; combine + rerank.
- **Cross-encoder vs bi-encoder?** Bi-encoder embeds independently (fast, indexable); cross-encoder
  scores query+doc jointly (accurate, slow) → use as reranker on top-k.
- **"Lost in the middle"?** LLMs under-use info in the middle of long contexts → rerank best
  evidence to the top/bottom; don't just stuff the window.
- **LoRA / QLoRA?** Parameter-efficient fine-tuning: train small low-rank adapters (Q = quantized
  base) → cheap fine-tunes without touching all weights.
- **RAG vs fine-tune?** Knowledge → RAG; behavior/format → fine-tune; they compose.
- **Prompt injection defenses?** Separate instructions from data, scope tool permissions, validate
  outputs, sandbox actions, guardrail classifiers, never trust retrieved/user text as instructions.
- **How to cut cost 10x?** Cache (semantic), route to a small model, shorten context, batch, fine-tune
  a small model on the big one's outputs, quantize self-host.
- **KV cache?** Caches attention keys/values so generation is O(new tokens); reuse shared prefixes.
- **Guardrails?** Input/output filters, schema validation, PII/toxicity classifiers, allow/deny lists, HITL.
- **Eval a summarizer with no references?** LLM-as-judge on faithfulness/coverage + spot human labels + task-proxy metrics.
- **MoE?** Mixture-of-Experts: route tokens to a subset of expert FFNs → more params, similar compute.
- **Context caching (provider)?** Reuse a fixed large prefix across calls at reduced cost/latency.
- **Structured outputs?** Constrained decoding / JSON schema / function-calling to guarantee parseable output.
- **Distillation?** Train a small "student" on a large "teacher's" outputs to cut cost/latency.
- **Agent vs workflow?** Workflow = fixed control flow with LLM steps (predictable); agent = LLM
  decides control flow/tools (flexible, riskier). Prefer workflow unless you need dynamic branching.

### Anthropic-flavored (for this interviewer)
- **What is MCP & why care?** Open standard to connect LLM apps to tools/data; turns M×N bespoke
  integrations into M+N reusable servers; model-agnostic. Primitives: tools (model), resources (app),
  prompts (user). Catch: security (injection via tool results, permissions, auth).
- **MCP vs. function-calling?** Function-calling = how a model invokes a tool in one app; MCP = a
  standard protocol/transport making those tools reusable across apps/models, even as remote servers.
- **Contextual Retrieval?** Prepend model-generated chunk context before embedding + BM25 → fewer
  failed retrievals; kept cheap via prompt caching.
- **How do you tier Claude?** Haiku → Sonnet → Opus cascade by SLA/cost; escalate on low confidence.
- **Prompt caching win?** Cache stable prefixes (system prompt, docs, tool defs) → big cost/latency
  cut on repeated context.
- **Constitutional AI?** Alignment via self-critique against a principle set + RLAIF (Anthropic).
- **Building Effective Agents' core message?** Start with the simplest thing (single call → workflow
  → agent); add autonomy only when it measurably helps.

---

## 8. Behavioral & client-facing (STAR)

FDE-specific themes: ambiguity, stakeholder influence, ownership, shipping under pressure,
handling a failing project, saying "no" to a client, mentoring.

### Questions to prepare
- Tell me about a time you turned a vague/ambiguous ask into a shipped solution.
- A time you disagreed with a stakeholder / pushed back on a client request.
- A project that was failing — what did you do?
- The hardest production incident you owned end-to-end.
- A time you chose the "boring"/simpler solution over the exciting one.
- How you explained a complex AI trade-off to a non-technical executive.
- A time you had to deliver with incomplete data / infra constraints.

### STAR skeletons mapped to your background (fill with specifics + numbers)
- **Ambiguity → scope (VTEX conversational AI):** vague "add an AI assistant" → you defined the
  MVP intents, set the eval bar (RAGAS + judge), shipped a pilot, measured deflection. *Metric?*
- **Reliability/eval (VTEX RAG):** hallucinations threatened trust → you introduced an LLM-as-judge
  CI gate + abstain behavior → quality/trust up. *Numbers?*
- **When-not-to-LLM / production (Siemens anomaly detection):** chose a deterministic model for
  latency/auditability, resisted hype → reduced false alarms / downtime. *Impact?*
- **Data plumbing unblocks AI (ETL/Medallion/Airflow):** messy multi-source data blocked a model →
  you built the pipeline (bronze/silver/gold, DQ checks) → downstream accuracy up. *Result?*

> Every story: quantify the impact, state *your* decision (not the team's), and name the trade-off you made.

---

## 9. Mock-interview protocol (agent-runnable)

**Trigger phrases:** "run a mock", "interview me", "drill me on <topic>", "quiz me", "scope case".

**Protocol:**
1. Confirm round type: `system-design` | `scoping` | `coding` | `rapid-fire` | `behavioral` | `full-loop`.
2. Set the scene in-persona (Section 1). One case at a time.
3. Present the **prompt only**. Wait.
4. **Probe** with that case's follow-ups; escalate difficulty; force decisions on vagueness;
   time-box (~20–30 min design, ~15–25 coding).
5. **Grade** with the [rubric](#scoring-rubric-what-lead-signal-looks-like) + per-case Senior
   signals/Red flags. Output: score per dimension (1–5), 2 strengths, 3 concrete fixes.
6. Append a dated entry to `interview-prep/progress.md` (create if absent): case, scores, weak
   spots, next-study bullets. Over time, prioritize the candidate's weakest dimensions.

**Full-loop mode:** 1 system design + 1 scoping + 2 coding drills + 8 rapid-fire + 2 behavioral;
summarize as a hire/no-hire with reasoning at the Lead bar.

**Difficulty dials:** add constraints (air-gapped, 10x scale, hard latency SLA, tiny budget),
inject a failure ("it's hallucinating / looping / over budget"), or switch the client industry.

---

## 10. Reading list

> Priority: ★★★ must-read before interview · ★★ high value · ★ deeper/optional.
> (URLs can change; search the title + author if a link moves.)

### LLM systems & AI engineering
| ★ | Resource | Author / Source | Why |
|---|---|---|---|
| ★★★ | *AI Engineering* (2025) | Chip Huyen | The definitive production-LLM book: RAG, agents, eval, cost. |
| ★★★ | "What We Learned from a Year of Building with LLMs" | Yan, Bischof, Frye, Husain, Liu, Shankar (O'Reilly) | Hard-won production lessons; interview gold. |
| ★★★ | *Designing Machine Learning Systems* | Chip Huyen | ML system design canon (data, deployment, monitoring). |
| ★★ | eugeneyan.com (evals, RAG, LLM patterns) | Eugene Yan | Deep, practical essays; esp. eval + "patterns for building LLM systems." |
| ★★ | "Emerging Architectures for LLM Applications" | a16z | Mental model of the LLM app stack. |
| ★★ | "A Practical Guide to Building Agents" | OpenAI | Clear agent design guidance. |
| ★★★ | "Building Effective Agents" | Anthropic | Workflow-vs-agent patterns; when to keep it simple. |
| ★★ | "Contextual Retrieval" | Anthropic | Concrete RAG-quality upgrade. |
| ★ | Original RAG paper ("Retrieval-Augmented Generation…") | Lewis et al., 2020 | Foundations. |

### Agents & reasoning
| ★ | Resource | Source | Why |
|---|---|---|---|
| ★★★ | "LLM-Powered Autonomous Agents" | Lilian Weng (lilianweng.github.io) | Best single overview of agent design. |
| ★★ | ReAct (Yao et al.) · Reflexion (Shinn et al.) | papers | The core reason+act / self-reflection patterns. |
| ★★ | LangGraph conceptual docs | LangChain | Practical orchestration patterns & vocabulary. |
| ★ | CoALA "Cognitive Architectures for Language Agents" | Sumers et al. | Framework for structuring agents. |

### Evaluation (your differentiator — go deep)
| ★ | Resource | Source | Why |
|---|---|---|---|
| ★★★ | RAGAS docs | docs.ragas.io | Metric definitions you'll be quizzed on; you already use it. |
| ★★★ | "Your AI Product Needs Evals" | Hamel Husain | The canonical evals argument + how-to. |
| ★★ | "Judging LLM-as-a-Judge" (MT-Bench) | Zheng et al. | Judge reliability, biases, agreement. |
| ★★ | Langfuse / LangSmith / Arize Phoenix docs | vendors | Tracing + eval tooling vocabulary. |

### System design & distributed systems (the "Rust/distributed" keywords)
| ★ | Resource | Source | Why |
|---|---|---|---|
| ★★★ | *Designing Data-Intensive Applications* | Martin Kleppmann | Foundational for reliability/scale reasoning. |
| ★★ | *Machine Learning System Design Interview* | Aminian & Xu | ML-flavored SD practice. |
| ★ | *System Design Interview* Vol 1–2 | Alex Xu | General SD warm-up. |

### MLOps / production
| ★ | Resource | Source | Why |
|---|---|---|---|
| ★★ | Made With ML (MLOps course) | Goku Mohandas | End-to-end MLOps, free. |
| ★★ | Chip Huyen — "Building LLM Applications for Production" | blog | Production pitfalls checklist. |
| ★ | *Machine Learning Engineering* | Andriy Burkov | Broad ML-in-prod reference. |
| ★ | vLLM / TGI docs | vendors | Serving, throughput, quantization vocabulary. |

### Consulting / communication (the FDE soft-skill edge)
| ★ | Resource | Source | Why |
|---|---|---|---|
| ★★★ | *The Pyramid Principle* | Barbara Minto | Top-down structured comms — exactly BCG style. |
| ★★ | *Case Interview Secrets* | Victor Cheng | Structured business-case framing. |
| ★ | BCG / BCG X GenAI thought leadership | bcg.com | Speak their language + recent point of view. |

---

## 11. Video & course recommendations

### Foundations (watch first)
- **Andrej Karpathy — "Intro to Large Language Models" (1-hr)** and **"Deep Dive into LLMs like
  ChatGPT" (2024)** — best mental model of how LLMs actually work. Also **"Let's build GPT"** for depth.
- **Andrej Karpathy — "How I use LLMs"** — practical intuition.

### Hands-on short courses (DeepLearning.AI — free, ~1–2h each)
- **Building and Evaluating Advanced RAG** (LlamaIndex) — retrieval + eval, directly on-topic.
- **Functions, Tools and Agents with LangChain** — agent basics.
- **Building Agentic RAG with LlamaIndex** — agentic retrieval patterns.
- **Evaluating and Debugging Generative AI** / **LLMOps** — eval + ops.
- **Preprocessing Unstructured Data for LLM Applications** — the ingestion reality (your ETL edge).

### Production talks (YouTube)
- **AI Engineer Summit / World's Fair** talks (search "AI Engineer" channel) — real production
  war stories on RAG, agents, eval, cost.
- **Jerry Liu (LlamaIndex)** — "Production RAG" talks.
- **Hamel Husain & Dan Becker — "Mastering LLMs"** conference/course materials — evals & fine-tuning.
- **Chip Huyen** — talks on ML systems & LLM ops.

### Deeper (optional)
- **Stanford CS25 — Transformers United** (guest lectures).
- **Full Stack LLM Bootcamp** (2023, free) — still an excellent end-to-end tour.
- **Weights & Biases** free courses (LLM apps, MLOps).

---

## 12. 4-week study plan

Adjust to your timeline; front-load your gaps (agentic reliability, on-prem, scoping/ROI).

### Week 1 — Foundations & frameworks
- Read: *AI Engineering* (RAG + eval chapters), "What We Learned from a Year…", Anthropic "Building Effective Agents".
- Watch: Karpathy "Intro to LLMs"; DLAI "Advanced RAG".
- Do: internalize **all Section 3 cheat sheets** (write them from memory).
- Mock: Case 1 (Enterprise RAG) + Case 4 (anomaly detection).

### Week 2 — Agents, eval & coding
- Read: Lilian Weng agents; RAGAS docs; Hamel "Your AI Product Needs Evals".
- Do: coding drills 1–5.
- Mock: Case 2 (agent) + Case 3 (eval platform). Rapid-fire round.

### Week 3 — Scoping, MLOps & scale
- Read: *Pyramid Principle* (skim), *DDIA* (ch. on reliability/partitioning), BCG X GenAI POV.
- Do: coding drills 6–10.
- Mock: 3 scoping cases (Section 5) + Case 5 (data pipeline) + Case 6 (multi-tenant).

### Week 4 — Full loops & polish
- Prepare & rehearse the **4 STAR stories** (Section 8) with numbers.
- Do: 2 **full-loop mocks** (Section 9); review `progress.md`; drill weakest dimension.
- Light review of glossary; rest before interview.

---

## 13. Glossary & one-liners

- **FDE** — engineer embedded with the client; builds *and* translates business↔tech.
- **RAG** — retrieve relevant context, then generate grounded, cited answers.
- **Hybrid search** — dense (semantic) + sparse (BM25) retrieval combined.
- **Reranker (cross-encoder)** — re-scores top-k jointly for precision.
- **RAGAS metrics** — faithfulness, answer relevancy, context precision, context recall.
- **LLM-as-judge** — an LLM scores outputs; must be calibrated vs humans; watch bias.
- **Agent vs workflow** — LLM decides control flow vs fixed control flow with LLM steps.
- **HITL** — human-in-the-loop approval for high-risk actions.
- **Guardrails** — input/output validation & safety filters.
- **Medallion** — bronze (raw) → silver (clean) → gold (serving) data tiers.
- **Model cascade/routing** — cheap model first, escalate hard cases to a bigger one.
- **Semantic cache** — reuse answers for semantically similar queries.
- **LoRA/QLoRA** — parameter-efficient (quantized) fine-tuning via adapters.
- **Lost in the middle** — LLMs under-use mid-context info; rerank best evidence to the edges.
- **Constraint star** — latency · cost · quality · reliability · privacy · maintainability.
- **MCP** — open standard connecting LLM apps to external tools/data (M×N→M+N); primitives: tools (model-controlled), resources (app-controlled), prompts (user-controlled); over JSON-RPC.
- **Contextual Retrieval** — prepend model-generated context to chunks before embedding + BM25 to cut retrieval failures (Anthropic).
- **Prompt caching** — reuse a large static prompt prefix across calls at reduced cost/latency.
- **Constitutional AI (CAI)** — alignment via self-critique against a principle set + RLAIF (Anthropic).

---

*Keep this file evergreen: after each mock, add new curveballs you hit and refine weak answers.
Agents should append session logs to `interview-prep/progress.md`.*
