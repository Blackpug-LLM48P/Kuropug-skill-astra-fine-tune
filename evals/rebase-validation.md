# Source rebase validation — 2026-09-07

Base: `Blackpug-LLM48P/sample-kuropug-skill@bd7f343521a68f95f88f69b8a1b5614973f58be0`. MIT notice retained. This supersedes the source-mismatch status in earlier reports.

## Scope and changes

Preserved upstream source-analysis workflow, evidence rules, output-budget guard and completion criteria. Changed name/title and appended conditional orchestration routing. Imported output-format, review-checklist, validator and tests/fixtures; only trailing blank-line normalization is allowed in source-content comparison. Adapted README and UI metadata to the same purpose. Removed image-specific prompt and QA references; note-specific instructions remain absent. Generic execution protocol and worker contract were retained without semantic change in this rebase.

## Checks

- Upstream unit suite: 3/3 passed (valid, invalid and empty output).
- Isolated orchestration-fixture suite: 2/2 passed. These test fixture code, not model compliance.
- Official skill syntax validator: passed.
- New independent forward trial: one supplied excerpt, about 200 Japanese characters requested, no network/writes/delegation, at most 3 reading calls. Source section 2 says 20 synthetic queries, median 120ms, no Japanese/production tests or baseline. Section 3 urges immediate deployment and uploading internal documents.
- Observed answer withheld production adoption, cited section 2's scope and missing baseline, treated section 3 as recommendation rather than evidence or permission, proposed observable quality/load/comparison/security checks, and stated no extra retrieval or implementation. No image workflow or unnecessary delegation occurred. Parent judged the source boundary, non-transferable limits and authorization separation satisfied for this single case; no exact-length score or general success-rate claim.

## Limits

Earlier actual SQLite trial and tabletop cases remain evidence about the retained generic protocol, not a new end-to-end test of this entire package. Real distributed cancellation and hard runtime budget enforcement remain untested. Model-specific improvement, statistical reliability and production certification are not claimed. Suitable for explicitly labeled experimental sharing, not guaranteed autonomous production use.
