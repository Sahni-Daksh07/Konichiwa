"""Interactive vocabulary and cultural quiz module."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import List, Tuple

from konichiwa.phrases import PHRASE_BOOK, Phrase


@dataclass
class QuizQuestion:
    """A multiple-choice quiz question generated from the phrasebook."""

    prompt: str
    target_phrase: Phrase
    options: List[str]
    correct_index: int

    def check_answer(self, user_choice_idx: int) -> bool:
        """Check if 1-indexed or 0-indexed choice matches correct index."""
        return user_choice_idx == self.correct_index


def generate_quiz_question() -> QuizQuestion:
    """Generate a random 4-option quiz question from the phrasebook."""
    target = random.choice(PHRASE_BOOK)
    other_phrases = [p for p in PHRASE_BOOK if p != target]
    distractors = random.sample(other_phrases, min(3, len(other_phrases)))

    options = [target.english] + [d.english for d in distractors]
    random.shuffle(options)
    correct_idx = options.index(target.english)

    prompt = f"What is the meaning of: {target.hiragana} ({target.romaji})?"

    return QuizQuestion(
        prompt=prompt,
        target_phrase=target,
        options=options,
        correct_index=correct_idx,
    )
