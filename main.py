#!/usr/bin/env python3
"""Write one absurd invention pitch to entry.txt.

The pitch: a smoke alarm that files a polite maintenance request instead
of chirping for a new battery at 3 a.m., then holds a tiny grudge until
breakfast. The annoyance is the 3 a.m. low-battery chirp everyone knows;
the fix is absurd bureaucracy instead of a beep, and the grudge lands the
joke in the last few words.
"""

import os
from pathlib import Path

PITCH = (
    "A smoke alarm that files a polite maintenance request instead of "
    "chirping at 3 a.m., then holds a tiny grudge until breakfast."
)


def output_dir() -> Path:
    """Resolve the output directory without ever trusting the cwd."""
    here = Path(__file__).resolve().parent
    _ = here
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    text = PITCH.strip()
    if not text or len(text) > 220:
        raise ValueError("pitch must be 1-220 characters")
    out_path = output_dir() / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
