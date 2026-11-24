#!/usr/bin/env python3
"""The One-Line Exit — make.fun entry.

Writes one funny single-line resignation letter to /output/entry.txt.
The gate: UTF-8 text, 1 to 140 characters, not only whitespace.
"""

import os
import sys

ENTRY = (
    "I resign, effective immediately: after four years of "
    "'we're a family here,' I checked the will \u2014 this family "
    "left me the on-call rota."
)


def validate_entry(text):
    """Return True only if the entry passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not text or not text.strip():
        return False
    if len(text) > 140:
        return False
    if "\n" in text or "\r" in text:
        return False
    if "  " in text:
        return False
    return True


def output_dir():
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main():
    if not validate_entry(ENTRY):
        print("entry failed validation", file=sys.stderr)
        return 1
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
