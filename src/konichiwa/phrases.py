"""Curated Japanese phrasebook and vocabulary registry."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import List, Optional


@dataclass(frozen=True)
class Phrase:
    """A Japanese phrase with pronunciation, scripts, and context."""

    romaji: str
    hiragana: str
    kanji: Optional[str]
    english: str
    category: str
    formality: str


PHRASE_BOOK: List[Phrase] = [
    # Dev & Teamwork
    Phrase(
        romaji="Yoroshiku onegaishimasu",
        hiragana="よろしくおねがいします",
        kanji="宜しくお願いします",
        english="I look forward to working with you / Please treat me well",
        category="Dev & Work",
        formality="Polite",
    ),
    Phrase(
        romaji="Otsukaresama deshita",
        hiragana="おつかれさまでした",
        kanji="お疲れ様でした",
        english="Thank you for your hard work / Great job today",
        category="Dev & Work",
        formality="Polite",
    ),
    Phrase(
        romaji="Ganbatte kudasai",
        hiragana="がんばってください",
        kanji="頑張ってください",
        english="Do your best! / Good luck!",
        category="Dev & Work",
        formality="Polite",
    ),
    Phrase(
        romaji="Koudo rebyuu onegaishimasu",
        hiragana="コードレビューおねがいします",
        kanji="コードレビューお願いします",
        english="Could you please review my code / PR?",
        category="Dev & Work",
        formality="Polite",
    ),
    Phrase(
        romaji="Bagu o mitsukemashita",
        hiragana="バグをみつけました",
        kanji="バグを見つけました",
        english="I found a bug",
        category="Dev & Work",
        formality="Polite",
    ),

    # Gratitude & Politeness
    Phrase(
        romaji="Arigatou gozaimasu",
        hiragana="ありがとうございます",
        kanji="有難う御座います",
        english="Thank you very much",
        category="Gratitude",
        formality="Polite",
    ),
    Phrase(
        romaji="Doumo arigatou",
        hiragana="どうもありがとう",
        kanji=None,
        english="Thanks a lot",
        category="Gratitude",
        formality="Casual",
    ),
    Phrase(
        romaji="Sumimasen",
        hiragana="すみません",
        kanji=None,
        english="Excuse me / I'm sorry",
        category="Politeness",
        formality="Polite",
    ),
    Phrase(
        romaji="Gomen nasai",
        hiragana="ごめんなさい",
        kanji=None,
        english="I am sorry",
        category="Politeness",
        formality="Casual",
    ),

    # Daily Life & Social
    Phrase(
        romaji="Genki desu ka?",
        hiragana="げんきですか？",
        kanji="元気ですか？",
        english="How are you? / Are you doing well?",
        category="Daily",
        formality="Polite",
    ),
    Phrase(
        romaji="Daijoubu desu",
        hiragana="だいじょうぶです",
        kanji="大丈夫です",
        english="Everything is okay / No problem",
        category="Daily",
        formality="Polite",
    ),
    Phrase(
        romaji="Hajimemashite",
        hiragana="はじめまして",
        kanji="初めまして",
        english="Nice to meet you (for the first time)",
        category="Daily",
        formality="Polite",
    ),
    Phrase(
        romaji="Mata ne",
        hiragana="またね",
        kanji=None,
        english="See you later / Bye",
        category="Daily",
        formality="Casual",
    ),

    # Food & Culture
    Phrase(
        romaji="Itadakimasu",
        hiragana="いただきます",
        kanji="頂きます",
        english="Gratefully receiving this food (spoken before a meal)",
        category="Food & Culture",
        formality="Polite",
    ),
    Phrase(
        romaji="Gochisousama deshita",
        hiragana="ごちそうさまでした",
        kanji="ご馳走様でした",
        english="Thank you for the delicious meal (spoken after eating)",
        category="Food & Culture",
        formality="Polite",
    ),
    Phrase(
        romaji="Oishii desu",
        hiragana="おいしいです",
        kanji="美味しいです",
        english="This is delicious",
        category="Food & Culture",
        formality="Polite",
    ),
]


def search_phrases(query: str) -> List[Phrase]:
    """Search phrases by romaji, hiragana, kanji, or English translation."""
    q = query.strip().lower()
    if not q:
        return []

    results = []
    for p in PHRASE_BOOK:
        if (
            q in p.romaji.lower()
            or q in p.hiragana
            or (p.kanji and q in p.kanji)
            or q in p.english.lower()
            or q in p.category.lower()
        ):
            results.append(p)
    return results


def get_phrases_by_category(category: str) -> List[Phrase]:
    """Return all phrases matching a specific category (case-insensitive substring)."""
    cat = category.strip().lower()
    return [p for p in PHRASE_BOOK if cat in p.category.lower()]


def get_random_phrase(category: Optional[str] = None) -> Phrase:
    """Return a randomly chosen phrase, optionally filtered by category."""
    pool = get_phrases_by_category(category) if category else PHRASE_BOOK
    if not pool:
        pool = PHRASE_BOOK
    return random.choice(pool)
