#!/usr/bin/env python3
"""The Moon Finally Answers Back entry: writes one line to /output/entry.txt.

Revision: v1 ("unpaid, unthanked, and expected to glow about it") landed
soft — the turn was a complaint list, not a punch. v2 flips the power
dynamic instead: after four billion years of listening, nobody has ever
asked how the Moon itself is doing. Shorter, wryer, and the comeback
arrives in the last clause."""

import os

# The Moon, finally answering four billion years of wishes, howls and
# 2 a.m. promises — with the one question nobody ever asked it back.
LINE = (
    "Four billion years of wishes, howls, and 2 a.m. promises \u2014 "
    "and not one of you has ever once asked how I'm doing."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = LINE
    # Explicit validation, not asserts: asserts are stripped with -O,
    # so a bad entry would slip through silently under python -O.
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
