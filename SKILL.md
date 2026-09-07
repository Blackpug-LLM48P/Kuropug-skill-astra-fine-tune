---
name: kuro-pug-astra-orchestrator
description: Orchestrate Kuro Pug publishing workflows with Astra while preserving the complete kuro-pug-tool image-production system. Use for multi-step article, image, note draft, QA, and recovery work where completion must be verified end to end rather than inferred from agent reports.
---

# Kuro Pug Astra Orchestrator

Run the existing Kuro Pug image-production workflow as an end-to-end operation. Preserve character identity, article intent, evidence, and publishing state while coordinating generation, editing, browser actions, QA, and recovery.

Read `references/astra-orchestration.md` before coordinating more than one substantive stage or worker. For image work, also read `references/prompt-patterns.md` and `references/qa-checklist.md`. For note draft placement, tags, saving, or editor recovery, read `references/note-publishing-recovery.md`.

## Workflow

1. Identify the final deliverable and define observable completion conditions before acting.
2. Extract fixed facts from the conversation and supplied references. Do not invent character identity, branding, quotations, numbers, article claims, or successful state.
3. Build an image manifest before generation. For every image, specify purpose, placement marker, aspect ratio, characters, scene, exact text, continuity dependencies, and QA risks.
4. Separate locked anchors from per-image variables. Keep locked anchors verbatim across a sequence.
5. Execute one bounded stage at a time. Record evidence for the stage without promoting it to end-to-end completion.
6. Inspect generated or edited images using `references/qa-checklist.md`. Repair material failures before placement.
7. When editing note, use `references/note-publishing-recovery.md`. Treat upload, placement, save, synchronization, tags, and publication as different states.
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
