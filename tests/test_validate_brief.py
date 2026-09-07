from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_brief import REQUIRED_HEADINGS, validate  # noqa: E402


class ValidateBriefTests(unittest.TestCase):
    def test_valid_fixture(self) -> None:
        text = (ROOT / "tests/fixtures/valid-brief.md").read_text(encoding="utf-8")
        self.assertEqual(validate(text), [])

    def test_invalid_fixture(self) -> None:
        text = (ROOT / "tests/fixtures/invalid-brief.md").read_text(encoding="utf-8")
        errors = validate(text)
        self.assertGreaterEqual(len(errors), 2)
        self.assertTrue(any("Evidence location" in error for error in errors))

    def test_empty_output_is_invalid(self) -> None:
        errors = validate("")
        self.assertGreaterEqual(len(errors), len(REQUIRED_HEADINGS) + 1)
        self.assertTrue(any("Evidence location" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
