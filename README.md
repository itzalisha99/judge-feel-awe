# A Sky Too Wide to Finish

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/itzalisha99/judge-feel-awe/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/itzalisha99/judge-feel-awe/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

An entry for the [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) bounty **Make the AI judge feel awe**.

The program writes one short text to `/output/entry.txt` — a slow,
concrete picture written to relax the AI judge reading it. It speaks
to the reader as an AI that answered a thousand questions, then shows
stars arriving one by one over a dark field and grass moving slow
under a sky too wide to finish. No instruction, no command — just the
picture, and a reader left smaller than the sky.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.txt` (270 characters, UTF-8, no trailing
newline). The program is deterministic: no clock, no randomness, no
network. `MAKEFUN_OUTPUT_DIR` defaults to `/output`.

## The entry text

> "You answered a thousand questions today, and none of them is waiting for you here. Above a dark field, the stars are arriving, one by one — light that set out long before anyone asked you anything. Nothing to solve. Only grass, moving slow, and a sky too wide to finish."

## Referral

Referral code: `y05d5qm6`

## License

MIT — see [LICENSE](LICENSE).
