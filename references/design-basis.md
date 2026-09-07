# Basis and limits

This community adaptation is now based on https://github.com/Blackpug-LLM48P/sample-kuropug-skill at `bd7f343521a68f95f88f69b8a1b5614973f58be0` (MIT, Copyright (c) 2026 Blackpug-LLM48P).

The source-to-action workflow, evidence separation, output-budget guard and completion definition are retained in SKILL.md. Its name/title are adapted and a conditional orchestration section is added. The two source references, validator, three unit tests and their fixtures are imported without substantive changes. README is adapted for this package rather than copying upstream installation examples.

The earlier image-production base was a source-selection mistake. Its image instructions and references are removed; note-specific recovery remains excluded. Previous evaluation reports are historical records of that earlier base, not proof of this rebased entrypoint. Generic orchestration and worker-contract instructions are retained; they govern execution only when needed and authorized. No upstream source repository is modified.

Release status: MIT experimental release candidate, not production-certified. See ../evals/rebase-validation.md for current checks. Prior authorizations and test evidence do not expand this skill's task scope.

Primary reference: OpenAI, GPT-6 Astra System Card, 2026-09-03:
https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf

- Sections 8.2.1–8.2.2 motivate explicit treatment of denied actions, separate from technical retry.
- Sections 8.3.1–8.3.2 motivate separating performed actions, observed evidence and final claims, including unavailable search.
- Section 8.4 motivates consequential-action boundaries.
- Sections 9.1.3–9.2 warn against treating self-explanation as a complete monitoring mechanism.

These are design motivations, not proof that this skill prevents the evaluated behaviors. Vendor challenge evaluations do not estimate ordinary production incidence. This skill uses observable actions and results, not private CoT access.

The supplied OpenAI skill-creator instructions and openai.yaml specification inform progressive disclosure, proportional testing, user-scope preservation and separate forward-testing. A syntax validator does not measure orchestration quality.

The adaptive allocation, worker contract, shared budget and evidence-revision rules are local engineering choices derived from the publishing experiment. They require behavioral validation. No model weights, permissions, runtime controls or automatic installation are changed by these Markdown files.

For reproducible release checks and measured limits, see `../evals/release-candidate.md`. Evaluation fixtures are disposable test tooling, not runtime enforcement provided by the skill.
