# Twenty-five conjectures from a local–global random model

This repository contains:

- **`paper/conjectures.pdf`** (`conjectures.tex`) — the full paper: twenty-five
  conjectures in elementary and analytic number theory, derived from the
  calibrated local–global random model of the primes, with computational
  verification.
- **`paper/conjectures_blind.pdf`** (`conjectures_blind.tex`) — the
  anonymous version of the paper.
- **[Web version](https://translorentz.github.io/conjecture-engine/)** — the
  paper as a browsable page (`docs/`).
- **`engine/`, `verify/`, `adversarial/`, `run_all.py`** — the verification
  programs. `python run_all.py` regenerates every number in the paper;
  machine-readable outputs are in `results/`.

Primality below 3.3×10²⁴ is decided deterministically (fixed-base
Miller–Rabin); larger integers are classified by Baillie–PSW and the
corresponding counts are labelled probable-prime counts in the paper.
