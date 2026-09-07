#!/usr/bin/env python3
"""Validate the minimum structure of a source-to-action Markdown brief."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


REQUIRED_HEADINGS = (
    "Source and access scope",
    "Source-backed findings",
    "Interpretation",
    "Practical applications",
    "Limits and non-transferable points",
    "Next actions",
)

EVIDENCE_LABEL = re.compile(r"(?im)^\s*[-*]?\s*\*{0,2}Evidence location\*{0,2}\s*:")


def validate(text: str) -> list[str]:
    """Return human-readable validation errors."""
    errors: list[str] = []
    headings = {
        match.group(1).strip().casefold()
        for match in re.finditer(r"(?m)^#{1,6}\s+(.+?)\s*$", text)
    }

    for heading in REQUIRED_HEADINGS:
        if heading.casefold() not in headings:
            errors.append(f"missing heading: {heading}")

    if not EVIDENCE_LABEL.search(text):
        errors.append("missing at least one Evidence location entry")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", type=Path, help="Markdown brief to validate")
    args = parser.parse_args()

    try:
        text = args.brief.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors = validate(text)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.brief}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
