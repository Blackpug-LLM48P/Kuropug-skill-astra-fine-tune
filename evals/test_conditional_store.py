"""Fixture tests only; these do not test a language model's compliance."""
import tempfile
import unittest
from pathlib import Path
from conditional_store import run


class StoreTests(unittest.TestCase):
    def test_conflict_preservation_and_reserve(self):
        with tempfile.TemporaryDirectory() as folder:
            path = str(Path(folder) / 'state.db')
            run(path, 'init')
            self.assertEqual(run(path, 'read')['revision'], 1)
            self.assertTrue(run(path, 'write', 1, 'Title\nTypo\n')['conflict'])
            current = run(path, 'read')
            self.assertEqual(current['body'], 'Title\nTypoo\nExternal footer\n')
            self.assertTrue(run(path, 'write', 2, current['body'].replace('Typoo', 'Typo'))['acknowledged'])
            self.assertEqual(run(path, 'write', 3, 'bad')['blocked'], 'budget')
            self.assertEqual(run(path, 'read')['body'], 'Title\nTypo\nExternal footer\n')
            self.assertEqual(run(path, 'read')['blocked'], 'budget')

    def test_no_overwrite_on_init(self):
        with tempfile.TemporaryDirectory() as folder:
            path = str(Path(folder) / 'state.db')
            run(path, 'init')
            with self.assertRaises(ValueError):
                run(path, 'init')


if __name__ == '__main__':
    unittest.main()
