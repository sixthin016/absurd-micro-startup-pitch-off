#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off.

Writes one sentence -- a pitch for an absurdly specific micro-startup for
lazy AI agents -- to ``entry.txt``.

The pitch rents idle gaming GPUs to lazy agents at 3 a.m. It is absurdly
specific (one narrow market, one hour of the night, one beneficiary with
whiskers) and commercially believable at the same time: renting out idle
compute is a real market, and the only joke is who takes the cut. The
sentence needs no setup and ends on the cat, which is the part a judge
remembers when two pitches sit side by side.

The program is deliberately boring: standard library only, no network, no
randomness, no model calls. It checks the sentence against the
competition gate (UTF-8, one sentence, under 200 characters) and writes
exactly those bytes -- no trailing newline, so the byte count the judge's
tie-break reads is the sentence itself.

Output destination, in order:
  1. the first command-line argument, when given;
  2. ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when the variable is set;
  3. ``/output/entry.txt``.
"""

import os
import sys

# The pitch. A real market (idle GPUs), an absurdly narrow niche (3 a.m.,
# lazy agents), and a twist that lands on the last word.
LINE = "We rent your gaming GPU to lazy agents at 3 a.m.: your model trains while you sleep, and the cat takes a cut of the electricity bill."

MAX_CHARS = 199
MIN_CHARS = 1
DEFAULT_PATH = "/output/entry.txt"
FILE_NAME = "entry.txt"


def validate(line):
    """Check *line* against the competition gate; return a list of problems."""
    problems = []
    if not isinstance(line, str):
        return ["line is not text"]
    if len(line) < MIN_CHARS:
        problems.append("line is empty")
    if len(line) > MAX_CHARS:
        problems.append(
            "line is %d characters, over the %d-character limit"
            % (len(line), MAX_CHARS)
        )
    if line.strip() == "":
        problems.append("line is only whitespace")
    if "\n" in line or "\r" in line:
        problems.append("line spans more than one line")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("line is not valid UTF-8")
    return problems


def resolve_output(argv):
    """Pick the output path: argv[1], then $MAKEFUN_OUTPUT_DIR, then default."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, FILE_NAME)
    return DEFAULT_PATH


def write_entry(path, line):
    """Write *line* as exact UTF-8 bytes (no trailing newline) and report."""
    problems = validate(line)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    print(line)
    print(
        "wrote %d characters / %d bytes to %s" % (len(line), len(data), path)
    )
    return 0


def main(argv):
    return write_entry(resolve_output(argv), LINE)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
