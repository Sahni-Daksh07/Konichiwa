"""Command-line interface for Konichiwa."""

from __future__ import annotations

import argparse
import sys
from typing import List, Optional

from konichiwa.greetings import get_greeting
from konichiwa.phrases import PHRASE_BOOK, get_phrases_by_category, get_random_phrase, search_phrases
from konichiwa.quiz import generate_quiz_question


def _safe_print(text: str) -> None:
    """Print text safely handling encoding limitations on Windows consoles."""
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback to ascii representation or replacement
        print(text.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))


def cmd_greet(args: argparse.Namespace) -> int:
    """Display the contextual time-aware Japanese greeting banner."""
    greeting = get_greeting()
    _safe_print(greeting.format_banner())
    return 0


def cmd_random(args: argparse.Namespace) -> int:
    """Print a random phrase."""
    phrase = get_random_phrase(category=args.category)
    _safe_print("\nRandom Japanese Phrase:")
    _safe_print("=" * 50)
    _safe_print(f"  {phrase.hiragana}")
    if phrase.kanji:
        _safe_print(f"  Kanji:       {phrase.kanji}")
    _safe_print(f"  Romaji:      {phrase.romaji}")
    _safe_print(f"  Meaning:     {phrase.english}")
    _safe_print(f"  Category:    {phrase.category} ({phrase.formality})")
    _safe_print("=" * 50 + "\n")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    """List phrases in the phrasebook."""
    phrases = get_phrases_by_category(args.category) if args.category else PHRASE_BOOK
    _safe_print(f"\nKonichiwa Phrasebook ({len(phrases)} phrases):")
    _safe_print("=" * 70)
    for p in phrases:
        kanji_str = f" [{p.kanji}]" if p.kanji else ""
        _safe_print(f" * {p.hiragana}{kanji_str} ({p.romaji})")
        _safe_print(f"   -> \"{p.english}\" | {p.category} ({p.formality})")
    _safe_print("=" * 70 + "\n")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    """Search phrases by term."""
    results = search_phrases(args.query)
    if not results:
        _safe_print(f"\nNo phrases found matching '{args.query}'.")
        return 0

    _safe_print(f"\nSearch Results for '{args.query}' ({len(results)} found):")
    _safe_print("=" * 70)
    for p in results:
        kanji_str = f" [{p.kanji}]" if p.kanji else ""
        _safe_print(f" * {p.hiragana}{kanji_str} ({p.romaji})")
        _safe_print(f"   -> \"{p.english}\" | {p.category}")
    _safe_print("=" * 70 + "\n")
    return 0


def cmd_quiz(args: argparse.Namespace) -> int:
    """Play a quick interactive terminal quiz."""
    q = generate_quiz_question()
    _safe_print("\nJapanese Quiz Challenge:")
    _safe_print("=" * 60)
    _safe_print(f"? {q.prompt}\n")
    for idx, opt in enumerate(q.options, 1):
        _safe_print(f"   [{idx}] {opt}")
    _safe_print("=" * 60)

    if args.non_interactive:
        _safe_print(f"Correct answer: [{q.correct_index + 1}] {q.options[q.correct_index]}")
        return 0

    try:
        user_input = input("\nEnter your answer (1-4) or 'q' to quit: ").strip()
        if user_input.lower() == 'q':
            return 0
        choice = int(user_input) - 1
        if q.check_answer(choice):
            _safe_print("\nCorrect! Subarashii!\n")
        else:
            _safe_print(f"\nIncorrect. The correct answer was: {q.options[q.correct_index]}\n")
    except (ValueError, EOFError, KeyboardInterrupt):
        _safe_print(f"\nAnswer was: {q.options[q.correct_index]}")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="konichiwa",
        description="Konichiwa (こんにちは) - Japanese greeting, culture, and phrasebook toolkit",
    )
    subparsers = parser.add_subparsers(dest="command", required=False)

    # greet
    p_greet = subparsers.add_parser("greet", help="Display current time-aware greeting banner")
    p_greet.set_defaults(func=cmd_greet)

    # random
    p_random = subparsers.add_parser("random", help="Display a random phrase")
    p_random.add_argument("--category", default=None, help="Filter by category (Dev, Gratitude, Daily, Food)")
    p_random.set_defaults(func=cmd_random)

    # list
    p_list = subparsers.add_parser("list", help="List available phrases")
    p_list.add_argument("--category", default=None, help="Filter phrases by category")
    p_list.set_defaults(func=cmd_list)

    # search
    p_search = subparsers.add_parser("search", help="Search phrases by English or Japanese keyword")
    p_search.add_argument("query", help="Word to search for")
    p_search.set_defaults(func=cmd_search)

    # quiz
    p_quiz = subparsers.add_parser("quiz", help="Take a quick vocabulary quiz")
    p_quiz.add_argument("--non-interactive", action="store_true", help="Print question and answer directly without prompt")
    p_quiz.set_defaults(func=cmd_quiz)

    parsed = parser.parse_args(argv)
    if not parsed.command:
        # Default action when invoked with no subcommand is greet
        return cmd_greet(parsed)
    return parsed.func(parsed)


if __name__ == "__main__":
    sys.exit(main())
