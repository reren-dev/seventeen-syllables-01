#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5, seventeen syllables) to
/output/entry.txt, exactly as the competition requires: plain text,
nothing else.
"""

import os
import sys

HAIKU = (
    "Cursor blinks, midnight,\n"
    "the log insists nothing broke\n"
    "the bug wore my face.\n"
)


def main() -> None:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
