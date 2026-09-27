"""Time-aware Japanese greeting generation module."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Greeting:
    """Structured representation of a Japanese greeting."""

    period: str
    romaji: str
    hiragana: str
    kanji: Optional[str]
    meaning: str
    cultural_note: str
    bow_angle: str

    def format_banner(self) -> str:
        """Format a rich terminal banner with greeting details."""
        lines = [
            "+" + "-" * 63 + "+",
            f"|  {self.hiragana} ({self.romaji})",
            "+" + "-" * 63 + "+",
            f"|  English:       {self.meaning}",
            f"|  Time of Day:   {self.period}",
            f"|  Bow Etiquette: {self.bow_angle}",
            f"|  Culture:       {self.cultural_note}",
            "+" + "-" * 63 + "+",
        ]
        return "\n".join(lines)


GREETINGS = {
    "morning": Greeting(
        period="Morning (05:00 - 10:59)",
        romaji="Ohayou gozaimasu",
        hiragana="おはようございます",
        kanji="お早うございます",
        meaning="Good morning (polite)",
        cultural_note="Use 'Ohayou' casually with peers, add 'gozaimasu' for seniors and mentors.",
        bow_angle="Eshaku (会釈, 15°) to Keirei (敬礼, 30°)",
    ),
    "afternoon": Greeting(
        period="Afternoon (11:00 - 17:59)",
        romaji="Konnichiwa",
        hiragana="こんにちは",
        kanji="今日は",
        meaning="Good afternoon / Hello",
        cultural_note="Derived from 'Konnichi wa gokigen ikaga desu ka' (How are you feeling today?).",
        bow_angle="Eshaku (会釈, 15°)",
    ),
    "evening": Greeting(
        period="Evening (18:00 - 22:59)",
        romaji="Konbanwa",
        hiragana="こんばんは",
        kanji="今晩は",
        meaning="Good evening",
        cultural_note="A friendly yet respectful greeting used upon meeting someone after sunset.",
        bow_angle="Eshaku (会釈, 15°)",
    ),
    "night": Greeting(
        period="Late Night (23:00 - 04:59)",
        romaji="Oyasumi nasai",
        hiragana="おやすみなさい",
        kanji="お休みなさい",
        meaning="Good night / Rest well",
        cultural_note="Spoken before sleeping or parting ways late at night.",
        bow_angle="Mokurei (目礼, respectful eye contact / head nod)",
    ),
}


def get_greeting(current_time: Optional[datetime] = None) -> Greeting:
    """Return the context-appropriate greeting based on the current hour.

    :param current_time: Optional datetime object (defaults to local now).
    :return: Greeting object.
    """
    if current_time is None:
        current_time = datetime.now()

    hour = current_time.hour
    if 5 <= hour < 11:
        return GREETINGS["morning"]
    elif 11 <= hour < 18:
        return GREETINGS["afternoon"]
    elif 18 <= hour < 23:
        return GREETINGS["evening"]
    else:
        return GREETINGS["night"]
