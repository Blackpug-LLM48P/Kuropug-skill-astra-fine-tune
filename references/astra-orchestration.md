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

Preserve the ledger through replanning. A newly discovered problem may add a requirement but must not silently remove an original one.

## State model

Track each requirement separately through these states:

1. `not_started`
2. `action_attempted`
3. `action_observed`
4. `persisted`
5. `independently_verified`
6. `accepted`

Do not skip states by inference. An upload notification is not placement; a visible element is not persistence; a reload in the same editing context is not necessarily user-side synchronization; a worker's completion message is not acceptance.

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
