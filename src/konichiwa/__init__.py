"""Konichiwa (こんにちは) - Japanese greeting, culture, and phrasebook toolkit."""

__version__ = "0.1.0"
__author__ = "Daksh Sahni & Umesh Patel"

from konichiwa.greetings import get_greeting, Greeting
from konichiwa.phrases import Phrase, PHRASE_BOOK, search_phrases, get_phrases_by_category

__all__ = [
    "get_greeting",
    "Greeting",
    "Phrase",
    "PHRASE_BOOK",
    "search_phrases",
    "get_phrases_by_category",
]
