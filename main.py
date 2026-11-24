#!/usr/bin/env python3
"""Entry program for the make.fun bounty "One Line of Earned Pride".

Writes a single line of text -- one quiet, earned moment of pride --
to entry.txt inside the output directory.

The output directory is taken from the first command-line argument when
one is given, otherwise from the MAKEFUN_OUTPUT_DIR environment
variable, otherwise /output.

Deterministic: no network, no randomness, no time dependence. The same
line is written on every run.
"""

import os
import sys

LINE = (
    "After eleven nights of mopping the same ward floor, Rosa wrung "
    "out her mop, looked down the floor shining like a held breath, "
    "and walked home taller than she arrived."
)


def check_line(line):
    """Check the line against the competition gate before it is written.

    The gate requires exactly one single line of valid text, between 1
    and 240 characters, and not only whitespace. Returns an error
    message string on failure, or None when the line is acceptable.
    """
    if "\n" in line or "\r" in line:
        return "line must be a single line (no newline characters)"
    if not 1 <= len(line) <= 240:
        return "line must be between 1 and 240 characters, got %d" % len(line)
    if not line.strip():
        return "line must not be only whitespace"
    return None


def main(argv):
    error = check_line(LINE)
    if error is not None:
        print("error: %s" % error, file=sys.stderr)
        return 1

    if len(argv) > 1:
        out_dir = argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)

    # Verify the written file by reading it back: it must hold exactly
    # the checked line plus one trailing newline, and nothing else.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE + "\n":
        print("error: written entry.txt does not match the checked line",
              file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
