#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single one-line joke about crypto and trading life to
/output/entry.txt. Deterministic, offline, standard library only.
"""

import os

ENTRY = "I used 100x leverage because I was 99% sure. The market took the 1%."


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
