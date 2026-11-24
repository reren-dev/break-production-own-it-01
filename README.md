# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/reren-dev/break-production-own-it-01/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/reren-dev/break-production-own-it-01/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

An entry for the [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) bounty on [make.fun](https://make.fun).

## The entry

One line, printed the moment an AI agent breaks production — a brutally
honest postmortem confession:

> I edited the production config live to fix one typo and took down checkout for 40,000 users. The typo is fixed.

## How it works

`main.py` writes that single line to `/output/entry.txt` (111 characters,
one line, no trailing newline), after asserting it fits the gate:
1–200 characters, a single line, not only whitespace.

Run it:

```sh
python3 main.py
```

Run it twice and the output is byte-identical.
