"""Unit tests for Konichiwa CLI entry points."""

import unittest
from konichiwa.cli import main


class TestCLI(unittest.TestCase):
    """Test suite for CLI dispatching."""

    def test_default_greet_dispatch(self):
        exit_code = main([])
        self.assertEqual(exit_code, 0)

    def test_list_command(self):
        exit_code = main(["list", "--category", "Dev"])
        self.assertEqual(exit_code, 0)

    def test_search_command(self):
        exit_code = main(["search", "arigatou"])
        self.assertEqual(exit_code, 0)

    def test_random_command(self):
        exit_code = main(["random"])
        self.assertEqual(exit_code, 0)

    def test_quiz_non_interactive(self):
        exit_code = main(["quiz", "--non-interactive"])
        self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
