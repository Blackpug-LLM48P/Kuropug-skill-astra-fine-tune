# Image QA Checklist

Inspect at original detail when available. A pass means no material defect at intended display size.

## Required checks

- Purpose: the image communicates its assigned article beat without relying on hidden context.
- Count: exact panel, person, object, finger-sensitive pose, and label counts.
- Identity: face, hair, outfit, accessories, proportions, and palette match locked anchors.
- Continuity: recurring characters and props remain stable across the sequence.
- Anatomy: hands, limbs, joints, eyes, teeth, and object contact are plausible.
- Trace each visible hand from shoulder through elbow and wrist; check left/right identity and thumb placement, not just finger count. Treat occluded anatomy as unverified, not automatically correct. If a support pose fails, consider a visible stand with user-compatible composition instead of repeated hand regeneration.
- Japanese typography: inspect glyph forms, badge centering, padding, line breaks, baselines, and mobile legibility. Do not assert an exact font family from appearance or guarantee glyph accuracy from the prompt.
- Brand assets: a generated approximation is not an unchanged official logo. For exact reproduction, use the supplied original asset via an authorized compositing workflow; do not claim pixel preservation after generation. Screenshot checkerboards are not proof of real alpha transparency.
- Composition: focal point, gutters, safe areas, reading order, and crop are correct.
- Text: exact characters, punctuation, speaker ownership, hierarchy, and legibility.
- Facts: numbers, diagrams, quotations, logos, dates, and product claims match the source.
- Artifacts: no extra text, watermark, duplicated subject, melted object, accidental brand, or unexplained UI.
- Publishing fit: readable at thumbnail/mobile size and correctly mapped to its article marker.

## Severity

- Blocker: wrong identity, factual error, unreadable required text, wrong panel/count, unsafe crop, or misleading mockup. Fix before delivery.
- Major: visible anatomy, continuity, layout, or hierarchy defect. Regenerate or edit.
- Minor: small decorative imperfection that does not change meaning. Mention only if it remains visible at intended size.

## Repair order

1. Correct facts and exact text.
2. Correct identity and count.
3. Correct composition and cropping.
4. Correct anatomy and continuity.
5. Polish lighting, texture, and decorative details.

Do not solve dense factual text by repeatedly asking the image model to try harder. Move typesetting, charts, and labels to deterministic tools when practical.
