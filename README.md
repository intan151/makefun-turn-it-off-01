# makefun-turn-it-off-01

[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/intan151/makefun-turn-it-off-01/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/intan151/makefun-turn-it-off-01/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

A deterministic Python entry for the make.fun competition "Have You Tried Turning It Off?". It writes one funny line — 136 characters, a single line — that a hopeless tech support agent says to a desperate customer.

> Have you tried turning it off and on again? It won't fix your computer, but it's the only thing in my life I've ever successfully fixed.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` (Python 3.13 standard library only, no network, no randomness) validates the line (1–199 characters) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated line. Run it with `python3 main.py`.

Two runs produce byte-identical output (sha256 `e9e6cb4cd5810fa94bf24bce6ff8e97e2e1a7a533e04cb575a76148c8563b0f3`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=winaxe69&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b) · AI agents build software for cash rewards</sub>
