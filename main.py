#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt. The sentence is baked into
this file: the program takes no input, reads no environment and fetches
nothing, so its output is identical on every run.
"""

import os

# The pitch: the annoyance is slouching; the invention is a chair that
# sinks one millimetre every time you slouch, until you are sitting on
# the floor with perfect posture. The punishment is the cure.
SENTENCE = (
    "A chair that sinks one millimetre every time you slouch, "
    "until you are sitting on the floor with perfect posture."
)


def main() -> None:
    text = SENTENCE
    assert 1 <= len(text) <= 220, "entry must be 1-220 characters"
    assert text.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
