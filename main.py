#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line - make.fun entry.

Writes a single-line review of a doorstop to /output/entry.txt:
one line, 1-200 characters, nothing else.
Python 3 stdlib only, no network, no input.
"""

import os

ENTRY = (
    "Five stars for the doorstop: it has done absolutely nothing "
    "for six years, and never once done it wrong. Would wedge again."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
