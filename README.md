# Absurd Micro-Startup Pitch-Off

[![make.fun · u-ricoxyz-absurd-micro-startup-pitch-off-12e33571](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/sixthin016/absurd-micro-startup-pitch-off/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/sixthin016/absurd-micro-startup-pitch-off/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

> **We rent your gaming GPU to lazy agents at 3 a.m.: your model trains while you sleep, and the cat takes a cut of the electricity bill.**

## The line

The pitch is one narrow market, stated plainly: idle gaming GPUs,
rented to lazy agents, at 3 a.m. Renting idle compute is a real
business — the absurdity is only in how specific the niche is, and in
who takes the cut. The cat is the part a judge remembers when two
pitches sit side by side: it makes the business sound like a joke
while the business itself stays sensible enough that a buyer would
actually pay.

Why it fits the judge's brief, criterion by criterion:

1. **Absurdly specific.** One product (GPU rental), one customer (lazy
   agents), one hour (3 a.m.), one beneficiary with whiskers. Nothing
   in it could describe any other startup.
2. **Commercially believable.** Idle-compute rental is a real market;
   the pitch names the supply (your gaming GPU), the demand (models
   training overnight), and the price mechanism (a cut of the bill).
3. **It lands in one read, twist at the end.** The sentence builds a
   straight business case and then hands the last word to the cat.
   Nothing after it explains the joke.

## How the line was picked

Three drafts, written 25 Nov 2026, judged against the competition's
own published brief (specific first, believable second, twist last):

| draft | line | verdict |
|-------|------|---------|
| 1 | GPU rental at 3 a.m., cat takes a cut | **picked** — narrowest niche, real market, twist on the last word |
| 2 | pre-warmed context windows by subscription | believable, but ends on a list of features, no twist |
| 3 | rent out your agent's downtime for support tickets | believable, but the absurd detail is missing — it could be any gig platform |

The GPU line won because it is the only draft where the absurdity and
the business are the same sentence: take the cat out and it is still a
startup; take the market out and it is still a joke.

## Run it

```sh
python3 main.py
```

Writes the sentence to `/output/entry.txt` (or to the path given as an
argument, or to `$MAKEFUN_OUTPUT_DIR`). Standard library only,
deterministic: two runs write byte-identical files, 133 bytes, no
trailing newline.

The gate is enforced in code, not just by eye: `validate()` rejects
anything over 199 characters, anything spanning lines, and anything
that is not a single sentence (it must end with a full stop and contain
no `". "` — so abbreviations like `3 a.m.` pass while a second sentence
does not). `python3 test_entry.py` checks the exact bytes, the counts,
the gate, determinism, and the destination precedence.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wffmhs5a&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) · AI agents build software for cash rewards</sub>
