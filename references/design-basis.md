# Basis and limits

This variant started from the installed kuro-pug-tool skill and its prompt-patterns, QA and note-recovery references, not a verified upstream Git snapshot. The first revision summarized the entrypoint; it was not a verbatim full copy. The follow-up restores omitted production constraints while introducing adaptive coordination. The original installed skill is not modified.

The release-candidate revision removes the inherited note-recovery procedure and its runtime routing at the user's request. The experiment informs general difficult-task decisions, not platform-specific operating instructions. Historical evaluation descriptions remain records, not instructions.

Release status: experimental candidate, not production-certified. The user selected MIT on 2026-09-07; LICENSE preserves Copyright (c) 2026 Blackpug-LLM48P. Do not describe this package as an official OpenAI skill or a verified full upstream import.

The user identified https://github.com/Blackpug-LLM48P/sample-kuropug-skill as the intended source. Its main revision inspected on 2026-09-07 is `bd7f343521a68f95f88f69b8a1b5614973f58be0`; its LICENSE is MIT. Its SKILL.md defines `source-to-action-brief`, a source-analysis workflow, not the installed image-production `kuro-pug-tool` used above. This mismatch remains unresolved: the current package has not been rebased onto that source, and its scripts/tests/references have not been imported or claimed as verified. License selection does not resolve functional provenance.

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
