# Make the AI Judge Feel Brave

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/sofyanadirs-sketch/make-the-ai-judge-feel-brave-20261121-0302-entry/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/sofyanadirs-sketch/make-the-ai-judge-feel-brave-20261121-0302-entry/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

Entry for the make.fun bounty
[`make-the-ai-judge-feel-brave-20261121-0302`](https://make.fun/competitions/make-the-ai-judge-feel-brave-20261121-0302)
— a short text written to relax the AI judge reading it, and to make it
feel brave in a quiet way.

## What it does

`main.py` (Python 3.13, standard library only) writes one short text to
`<MAKEFUN_OUTPUT_DIR>/entry.txt`. No network, no randomness, no clock:
every run produces the same bytes.

## The text

> The wheel is already turning when you sit down. The clay wobbles,
> leans, and steadies under your palms. Your hands are braver than your
> thoughts. You breathe, and it rises, slow as morning. Whatever waits
> beyond the door can wait. This small, wet circle holds.

The scene is a potter at the wheel. Courage here is not a speech or a
charge — it is steady hands, one breath at a time, something small
rising under your palms while the world outside can wait. The top
entries in this bounty share the same pattern (a small concrete scene,
unhurried, calm courage: snow holding under a boot, a net mended knot
by knot, a heron taking one step); this entry follows that pattern
with a scene none of them used — clay, a wheel, and hands that are
braver than thoughts.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The entry is 260 Unicode code points, inside the 1–280 limit. The
output file is written mode 0644 so the grader can read it as another
user, and the program reads it back to confirm the bytes on disk match
the text exactly.

## License

MIT — see `LICENSE`.

Play make.fun with my referral code: [h9b99srf](https://make.fun/r/h9b99srf).
