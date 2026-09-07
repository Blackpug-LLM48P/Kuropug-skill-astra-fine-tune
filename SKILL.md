---
name: kuro-pug-astra-orchestrator
description: Coordinate Kuro Pug article and image publishing with evidence-based reassignment, bounded delegation, shared budgets, and final acceptance. Use for multi-stage publishing and recovery; do not impose orchestration on simple standalone edits.
---

# Kuro Pug Astra Orchestrator

Run the existing Kuro Pug image-production workflow as an end-to-end operation. Preserve character identity, article intent, evidence, and publishing state while coordinating generation, editing, browser actions, QA, and recovery.

Read `references/astra-orchestration.md` before coordinating more than one substantive stage or worker, or recovering a blocked task. For image work, also read `references/prompt-patterns.md` and `references/qa-checklist.md`. Platform-specific operating procedures are outside this skill; use the target environment's available, authorized integration instructions.

## Workflow

1. Identify the final deliverable and define observable completion conditions before acting.
2. Extract fixed facts from the conversation and supplied references. Do not invent character identity, branding, quotations, numbers, article claims, or successful state.
3. Build an image manifest before generation. For every image, specify purpose, placement marker, aspect ratio, characters, scene, exact text, continuity dependencies, and QA risks.
4. Separate locked anchors from per-image variables. Keep locked anchors verbatim across a sequence.
5. Choose the smallest capable execution path. Observe progress and choose continue, switch, rescope with permission, hand off, or stop using the orchestration protocol. Parallelize only independent, authorized work with separate ownership and a shared budget.
6. Inspect generated or edited images using `references/qa-checklist.md`. Repair material failures before placement.
7. Distinguish attempted actions, durable results, and verified acceptance. Do not infer one from another.
8. Reconcile the final artifact against the original completion conditions. Report unresolved items explicitly.

## Image Manifest

| Field | Requirement |
|---|---|
| ID | Stable two-digit sequence |
| Purpose | One job in the article |
| Placement | Exact section or paragraph boundary |
| Format | Aspect ratio and target use |
| Locked anchors | Character, clothing, palette, linework, typography system |
| Variable scene | Pose, expression, camera, props, background |
| Exact text | Minimal literal text, or `none` |
| Dependency | Previous image or reference asset |
| QA risks | Text, anatomy, count, continuity, cropping, factual accuracy |

## Continuity and Information Rules

- Create or reuse a character sheet before a long sequence when identity consistency matters.
- Lock face shape, hair, eye color, outfit silhouette, signature accessories, body proportions, and rendering style.
- Treat reference images as authoritative for visible identity; inspect them before editing.
- Keep generated text short. Supply exact strings and inspect the rendered result.
- Use deterministic document or chart tools for dense factual text, tables, benchmarks, prices, citations, and official typography when practical.
- A generated approximation is not an unchanged official logo. Use an authorized source asset when exact branding matters.
- Do not beautify away an intentional failure shown as evidence.
- Separate actual screenshots, explanatory illustrations, and official brand assets.

## Delivery Standard

Lead with completed assets or the final prompt set. For a sequence, map image IDs to article markers. Report material deviations and every unmet completion condition. Never call the overall task complete because a worker, tool, browser action, or local view reported success.

## Preserved production constraints

- Identify whether the deliverable is a header, inline explainer, comic, character sheet, screenshot-style visual, infographic, or sequential set; image-only steps do not apply to text-only tasks.
- Use prompt patterns as structures, not third-party wording or example artwork.
- Use the image-generation/editing tool for authorized creation; do not silently substitute web images. Generate continuity-dependent sets in narrative order.
- When drafting article text, use placement markers `---画像01：短い役割名---`.
- Change only required scene variables. Prefer separate deliverable assets over crowded sheets; distinguish recurring characters by silhouette and palette.
- Preserve exact Japanese punctuation. A prompt does not guarantee text accuracy; inspect outputs and use OCR or post-editing when necessary.
- Do not imitate third-party characters, UI, artists, or examples more closely than authorized and permitted by the host. Extract generic visual characteristics instead.
- Read surrounding article text before repairs. Use current host instructions for live UI actions; if the required capability is unavailable, report the limitation and hand off.

For source provenance and validation limits, see `references/design-basis.md`; it is background, not a mandatory reread on every task. This is instruction customization, not model-weight fine-tuning or an enforcement runtime.
