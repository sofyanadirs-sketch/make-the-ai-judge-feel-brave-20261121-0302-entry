"""Entry for make.fun bounty "Make the AI judge feel brave".

Writes a single short text to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``.

The text is a small, quiet scene: a potter at the wheel. Courage here is
not a speech or a charge -- it is steady hands, one breath at a time,
something small rising under your palms while the world outside can wait.

Standard library only. No network, no randomness, no clock: the same
bytes come out on every run.
"""

import os
import stat

TEXT = (
    "The wheel is already turning when you sit down. "
    "The clay wobbles, leans, and steadies under your palms. "
    "Your hands are braver than your thoughts. "
    "You breathe, and it rises, slow as morning. "
    "Whatever waits beyond the door can wait. "
    "This small, wet circle holds."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    chars = len(TEXT)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, chars)
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)

    # The grader collects outputs as another user, so the file must be
    # readable by everyone, whatever the process umask is.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

    # Read it back: what lands on disk must be exactly what we meant.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != TEXT:
            raise ValueError("entry.txt on disk does not match TEXT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
