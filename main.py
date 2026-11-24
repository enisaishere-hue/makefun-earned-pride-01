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


def main(argv):
    if len(argv) > 1:
        out_dir = argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
