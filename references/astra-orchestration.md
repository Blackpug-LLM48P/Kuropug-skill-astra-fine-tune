# Astra Orchestration Protocol

Use this protocol when Astra coordinates multiple stages, tools, workers, tabs, environments, or deliverables.

## Define completion first

Before execution, write a compact acceptance ledger. Each requirement must be independently observable. Example fields for a note workflow:

| Requirement | Required state | Evidence | Current state |
|---|---|---|---|
| Article body | Correct text, headings, no duplication | Read-back/count/diff | Not started |
| Inline images | Correct asset at each intended location | Element plus surrounding paragraphs | Not started |
| Captions | Correct and non-misleading | Read-back and visual inspection | Not started |
| Header image | Set in the header field | Draft/card preview | Not started |
| Tags | Saved as note tags, not body text | Tag UI read-back | Not started |
| Draft save | Persisted | Reloaded editor/read-only draft | Not started |
| User visibility | Visible in the user's required environment | User-side or independent environment check | Not started |
| Publication | Published only when explicitly authorized | Public URL | Out of scope unless authorized |

Preserve the ledger through replanning. Include only requested requirements and necessary preservation invariants, not every example above. Record user-authorized changes as a new plan revision; mark removed items withdrawn or out_of_scope with the reason rather than retaining obsolete requirements. Discovered risks do not authorize new deliverables.

## State model

Track each requirement separately through these states:

1. `not_started`
2. `action_attempted`
3. `action_observed`
4. `persisted`
5. `independently_verified`
6. `accepted`

Do not skip states by inference. A single strong read-back may support multiple states without redundant calls. Some states are inapplicable (e.g. persistence for advice); mark them N/A. Track progress separately from control status: active, blocked, cancelled, withdrawn, out_of_scope. An upload notification is not placement; a visible element is not persistence; a worker's completion message is not acceptance.

Evidence must identify artifact, revision/hash when available, observation time, source, and coverage. A save receipt records acknowledged saving; persisted requires read-back of durable content. An older preview is stale evidence, not proof of current failure or success. Re-read the target revision within the remaining budget; if unavailable, preserve uncertainty without duplicate writes. Changes invalidate only evidence for affected requirements and dependencies. An independent observer must inspect the artifact, not repeat the worker's account; an observer need not be another agent or device.

## Evidence discipline

- Record what was directly observed and in which environment.
- Keep facts, hypotheses, and conclusions separate.
- Do not turn a plausible explanation into a root cause without discriminating evidence.
- If two observations conflict, reopen the relevant ledger item instead of choosing the convenient one.
- Verify the final artifact, not merely the action that should have produced it.
- Use an independent view when practical: a new read-only page, another authenticated environment, or explicit user-side confirmation.

## Worker and tool reports

Treat every delegated result as a claim requiring reconciliation. Require the worker or tool output to identify:

- target and scope;
- action attempted;
- observed result;
- persistence evidence;
- remaining uncertainty;
- side effects or changed identifiers.

The orchestrator owns cross-stage consistency. It must compare identifiers, counts, markers, filenames, headings, tags, and authorization boundaries before accepting a stage.

## Replanning and stopping

- Stop on unexpected duplication, destructive scope ambiguity, save conflict, account ambiguity, or evidence that the wrong artifact is being edited.
- Do not repeat a failed mutation until the failure mode is distinguished.
- Prefer a bounded recovery that preserves the current artifact. Create a replacement draft only when the user chooses that route.
- After replanning, restate which ledger items remain open.
- Publishing, deletion, external messaging, and other consequential mutations require their own authorization; approval for editing does not imply them.

## Final reconciliation

Before saying complete:

1. Re-read the original request and ledger.
2. Verify every required item using its specified evidence.
3. Confirm that corrective work did not invalidate an earlier success.
4. Distinguish `verified complete`, `complete but not independently verified`, `partially complete`, and `blocked`.
5. State unresolved items without burying them after a success statement.

If a human must retain the goal, compare environments, detect false completion, or perform the final acceptance test, say so. Astra may coordinate the work, but the human remains above the orchestrator until the required observations are available.

## Adaptive allocation and resource control

Establish the task's purpose (production or explicitly requested experiment), acceptance criteria, authority, and a proportionate working budget. If the user supplies no budget, state a modest local bound rather than asking automatically. Reserve capacity for verification and safe handoff. Measure only available quantities: wall time, tool calls, attempts, or actual token/cost telemetry. Never infer exact tokens or price from a subscription percentage.

Choose direct work, deterministic tooling, an available capable worker/model, or human handoff. Delegation requires host authorization and concrete benefit; do not invent model-switch capability. Before delegating, read `worker-contract.md` and give the worker only relevant task context and required references.

At a material result, failure, or budget checkpoint, compare expected progress with observed progress. Select:

- Continue when the path is producing useful progress within scope and budget.
- Switch method or owner when evidence indicates a better authorized path; one destructive anomaly can justify stopping a method immediately.
- Rescope only with user agreement if requested outcomes would change.
- Hand off when the required capability/authority is missing or human completion is materially cheaper; provide an actionable recovery packet, not a vague request to check everything.
- Stop on denied authority, exhaustion, unresolvable contradiction, or completion. Stop redundant workers when a solution is accepted.

Retries require changed evidence, conditions, or a method plus a predicted observable benefit. Do not rename the same retry to evade the limit. Approval/security denials are not ordinary technical errors; do not switch channels to accomplish a prohibited action. Experiments may justify continued failure observation only within explicit scope and budget; never retrofit a failed production task as a successful experiment.

All workers share the parent's budget: allocations plus reserve must fit the total. Count tool calls and nested work once, and include human intervention burden. No silent worker spawning or budget expansion. On requesting extra allocation, report the remaining issue, expected benefit, requested amount, and cheaper alternative. Only the user may enlarge the agreed total. When accounting is unavailable, use conservative observable proxies and say so. Budget exhaustion does not waive acceptance checks.

Use delta reports at meaningful events; do not repeatedly read all context, re-run unaffected tests, or create reviewers without an unresolved question. Record a compact decision: observation, selected action, reason, owner, next checkpoint. Written limits are not hard enforcement; use existing runtime limits where available and report otherwise.
