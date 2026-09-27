# Konichiwa (こんにちは) 🌸

[![CI](https://github.com/Sahni-Daksh07/Konichiwa/actions/workflows/ci.yml/badge.svg)](https://github.com/Sahni-Daksh07/Konichiwa/actions)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-success.svg)](pyproject.toml)

> **Konichiwa** is a lightweight, zero-dependency Japanese conversational toolkit, time-aware greeting generator, and phrasebook designed for developers, terminal enthusiasts, and learners.

```text
+---------------------------------------------------------------+
|  こんにちは (Konnichiwa)
+---------------------------------------------------------------+
|  English:       Good afternoon / Hello
|  Time of Day:   Afternoon (11:00 - 17:59)
|  Bow Etiquette: Eshaku (会釈, 15°)
|  Culture:       Derived from 'Konnichi wa gokigen ikaga desu ka'.
+---------------------------------------------------------------+
```

---

## ✨ Features

- ⏰ **Time-Aware Greetings**: Automatically detects the time of day and returns the culturally appropriate greeting (*Ohayou gozaimasu*, *Konnichiwa*, *Konbanwa*, or *Oyasumi nasai*) with proper bowing etiquette guidance.
- 💻 **Developer & Teamwork Phrases**: Japanese expressions frequently used in collaborative engineering teams (PR reviews, bug reports, and work gratitude like *Otsukaresama deshita*).
- 📖 **Curated Phrasebook**: Explore phrases across categories including Daily Life, Gratitude, Politeness, and Food culture with Hiragana, Kanji, Romaji, and English translations.
- 🎯 **Interactive Terminal Quiz**: Test your Japanese vocabulary directly in the terminal.
- ⚡ **Zero External Dependencies**: Implemented entirely with Python's standard library. Works out-of-the-box anywhere Python is installed.

---

## 🚀 Quickstart & Installation

Clone and install locally in editable mode:

```bash
git clone https://github.com/Sahni-Daksh07/Konichiwa.git
cd Konichiwa
pip install -e .
```

---

## 💻 CLI Usage

Once installed, use the `konichiwa` command:

### 1. Contextual Greeting Banner
```bash
konichiwa greet
```

### 2. Random Phrase
Get an inspiring or daily Japanese phrase:
```bash
konichiwa random
konichiwa random --category "Dev & Work"
```

### 3. Search Phrases
Look up phrases by Romaji, Kanji, Hiragana, or English meaning:
```bash
konichiwa search "review"
konichiwa search "arigatou"
```

### 4. Interactive Quiz
Sharpen your vocabulary with a 4-option multiple-choice challenge:
```bash
konichiwa quiz
```

Or non-interactive mode for automated testing/scripts:
```bash
konichiwa quiz --non-interactive
```

---

## 🐍 Python API

Integrate `konichiwa` into your own Python applications, scripts, or Slack/Discord bots:

```python
from datetime import datetime
from konichiwa import get_greeting, search_phrases, get_phrases_by_category

# 1. Get greeting for current time
greeting = get_greeting()
print(greeting.hiragana)  # 'こんにちは'
print(greeting.meaning)   # 'Good afternoon / Hello'
print(greeting.cultural_note)

# 2. Search phrases
dev_phrases = search_phrases("bug")
for p in dev_phrases:
    print(f"{p.romaji}: {p.english}")
    # Bagu o mitsukemashita: I found a bug
```

---

## 🎎 Cultural Etiquette Guide

In Japanese culture, bowing (*ojigi*, お辞儀) conveys respect and humility:

| Angle | Name | Japanese | Usage Context |
|---|---|---|---|
| **15°** | **Eshaku** | 会釈 | Casual greeting among colleagues and peers |
| **30°** | **Keirei** | 敬礼 | Polite greeting to clients, mentors, and senior partners |
| **45°** | **Saikeirei** | 最敬礼 | Deepest reverence, formal gratitude, or profound apology |

---

## 🧪 Running Tests

Run the test suite using Python's built-in `unittest` runner:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 🤝 Contributing

Contributions are welcome! Whether adding new phrases, improving cultural notes, or enhancing CLI capabilities:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-phrase`)
3. Commit your changes (`git commit -m 'feat: add travel category phrases'`)
4. Push to your branch (`git push origin feature/amazing-phrase`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).