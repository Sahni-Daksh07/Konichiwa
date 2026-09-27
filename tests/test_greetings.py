"""Unit tests for time-aware greetings."""

from datetime import datetime
import unittest

from konichiwa.greetings import get_greeting


class TestGreetings(unittest.TestCase):
    """Test suite for greeting selection across hours of the day."""

    def test_morning_greeting(self):
        t = datetime(2026, 9, 28, 8, 30)
        g = get_greeting(t)
        self.assertEqual(g.romaji, "Ohayou gozaimasu")
        self.assertIn("おはよう", g.hiragana)

    def test_afternoon_greeting(self):
        t = datetime(2026, 9, 28, 14, 0)
        g = get_greeting(t)
        self.assertEqual(g.romaji, "Konnichiwa")
        self.assertIn("こんにちは", g.hiragana)

    def test_evening_greeting(self):
        t = datetime(2026, 9, 28, 20, 15)
        g = get_greeting(t)
        self.assertEqual(g.romaji, "Konbanwa")
        self.assertIn("こんばんは", g.hiragana)

    def test_night_greeting(self):
        t = datetime(2026, 9, 28, 2, 0)
        g = get_greeting(t)
        self.assertEqual(g.romaji, "Oyasumi nasai")
        self.assertIn("おやすみ", g.hiragana)

    def test_banner_formatting(self):
        g = get_greeting(datetime(2026, 9, 28, 12, 0))
        banner = g.format_banner()
        self.assertIn("Konnichiwa", banner)
        self.assertIn("English:", banner)


if __name__ == "__main__":
    unittest.main()
