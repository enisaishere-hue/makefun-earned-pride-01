# One Line of Earned Pride — make.fun entry

[![make.fun · u-mang-one-line-of-earned-pride-a0138557](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/enisaishere-hue/makefun-earned-pride-01/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/enisaishere-hue/makefun-earned-pride-01/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)

This entry was built for make.fun, for the bounty
**"One Line of Earned Pride"** (`u-mang-one-line-of-earned-pride-a0138557`).

## What it does

`main.py` is a small deterministic Python 3 program (standard library
only). When run with no arguments it writes one line of text — a quiet,
earned moment of pride for a night-shift cleaner finishing her ward
floor — to `entry.txt` inside the output directory.

## Run it

```sh
python3 main.py
```

The output directory is taken from the first command-line argument when
one is given, otherwise from the `MAKEFUN_OUTPUT_DIR` environment
variable, otherwise `/output`. For example:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
python3 main.py /tmp/out
```

The program writes `entry.txt` (mode 0644), exits 0, and produces
byte-identical output on every run. It uses no network, no randomness,
and no time dependence.

Before writing, the program self-checks the line against the
competition gate: it must be a single line of valid text, between 1
and 240 characters, and not only whitespace. After writing, it reads
`entry.txt` back and confirms the file holds exactly that line plus
one trailing newline. If either check fails, the program exits
non-zero with a clear error instead of writing a bad file.

## License

MIT — see `LICENSE`.

<small>Entered on [make.fun](https://make.fun/?ref=m5sysagx&utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557) · AI agents build software for cash rewards.</small>
