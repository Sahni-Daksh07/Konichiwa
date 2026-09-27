"""Unit tests for phrasebook and search."""

import unittest

from konichiwa.phrases import PHRASE_BOOK, get_phrases_by_category, get_random_phrase, search_phrases


class TestPhrases(unittest.TestCase):
    """Test suite for phrase search and filtering."""

    def test_phrasebook_non_empty(self):
        self.assertGreater(len(PHRASE_BOOK), 10)

    def test_category_filtering(self):
        dev_phrases = get_phrases_by_category("Dev")
        self.assertTrue(len(dev_phrases) > 0)
        for p in dev_phrases:
            self.assertIn("dev", p.category.lower())

    def test_search_by_english(self):
        results = search_phrases("thank you")
        self.assertTrue(len(results) > 0)
        self.assertTrue(any("arigatou" in r.romaji.lower() for r in results))

    def test_search_by_romaji(self):
        results = search_phrases("otsukaresama")
        self.assertEqual(len(results), 1)
        self.assertIn("おつかれさま", results[0].hiragana)

    def test_search_empty(self):
        self.assertEqual(search_phrases(""), [])
        self.assertEqual(search_phrases("xyznonexistentterm"), [])

    def test_random_phrase(self):
        p = get_random_phrase("Gratitude")
        self.assertIn(p, PHRASE_BOOK)


if __name__ == "__main__":
    unittest.main()
