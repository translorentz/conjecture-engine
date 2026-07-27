# conjecture-engine

Twenty-five number-theoretic conjectures, each built to the specification in
the accompanying design criteria — *the maximum-strength statement predicted
by a local–global random model, with a computable constant that the data
confirm, embedded in a hierarchy of existing conjectures, whose failure
would require structure nobody can name* — together with programs that
compute every constant from first principles and verify every statement
against exact counts.

* **`CONJECTURES.md`** — the 25 statements with derivations, admissibility
  analyses, hierarchy placement, and Goldilocks notes.
* **`RESULTS.md`** — the outcome of the actual verification runs (auto-built
  from `results/*.json` by `compile_results.py`).
* **`engine/ntlib.py`** — shared machinery: numpy sieves (dense and
  segmented), deterministic Miller–Rabin (< 3.317e24) and BPSW,
  Tonelli–Shanks, Bateman–Horn singular series with programmatic
  admissibility assertion, Hardy–Littlewood tuple constants, twin singular
  series, logarithmic integrals.
* **`verify/cNN_*.py`** — one self-contained verification program per
  conjecture; each accepts its bound(s) on the command line and writes
  `results/cNN.json`.
* **`run_all.py`** — runs the entire suite sequentially with the production
  bounds and rebuilds `RESULTS.md`.

## The 25 at a glance

| # | Statement (short form) | Model / constant | Verified to |
|---|---|---|---|
| C01 | n²+1, n²+3 both prime infinitely often, count ~ C·I(N) | Bateman–Horn | 10⁷ |
| C02 | n³+2 prime infinitely often, count ~ C·I(N) | Bateman–Horn (cubic) | 10⁷ |
| C03 | p, 2p−1, 3p−2 all prime (AP chain), ~ C·I(x) | Bateman–Horn (3 linear) | 3·10⁸ |
| C04 | quintuplet (0,2,6,12,14), ~ C·Li₅(x) | Hardy–Littlewood | 10⁹ |
| C05 | n²+n+1, n²+n+7 both prime, ~ C·I(N) | Bateman–Horn | 10⁷ |
| C06 | p and p²+p+1 both prime (length-3 repunit base p), ~ C·I(x) | Bateman–Horn | 10⁷ |
| C07 | p and p²−2 both prime, ~ C·I(x) | Bateman–Horn | 10⁷ |
| C08 | n²+1, n²+3, n²+7 all prime (refines C01), ~ C·I(N) | Bateman–Horn | 10⁷ |
| C09 | #{p ≤ x: F_p prime} ~ (e^γ/log φ) log x | LPW screening | p ≤ 10⁴ |
| C10 | #{p ≤ x: p#+1 prime} ~ e^γ log x | Mertens boost | p ≤ 4000 |
| C11 | n²+2ⁿ prime infinitely often (n ≡ 3 mod 6), ~ κ-model | exact local densities | n ≤ 4200 |
| C12 | #{n ≤ N: n!+1 prime} ~ e^γ log N | Mertens boost | n ≤ 700 |
| C13 | n = p + k³ (k ≥ 1) has finitely many exceptions | Borel–Cantelli + local | 10⁸ |
| C14 | exactly ten odd n are not p + 2k² (k ≥ 1); largest 5993 | Borel–Cantelli | 10⁸ |
| C15 | every n ≡ 2 (4), n ≥ 6, is p+q with p ≡ q ≡ 3 (4); R₃ ~ ½S(n)I(n) | HL Goldbach | 10⁸ |
| C16 | π_d(x) ~ S(d)Li₂(x) uniformly, all even d ≤ 2000 | HL / de Polignac | 10⁸ |
| C17 | every even n ≥ 4210 is a sum of two twin-pair members (35 exceptions) | Borel–Cantelli on twins | 10⁸ |
| C18 | twin-gap records ~ log³x/(2C₂) | Cramér for thinned process | 10⁹ |
| C19 | log p(g)/√g → √(e^γ/2) = 0.9436 (first gap occurrence) | Cramér–Granville | 10⁹ |
| C20 | prime counts in λ log x windows: Var/mean = 1 − (log h + γ + log 2π − 1)/log x | Gallagher + Montgomery | 1.2·10⁹ |
| C21 | twin race mod 5: class 1 leads via the q²−2 mechanism; bias/noise ~ 1/log x | explicit-formula analog | 10⁹ |
| C22 | Li(p(a,q))/φ(q): Exp(1) tail, Gumbel max at H_φ; mean anomaly ≈ 0.75 | order statistics | q ≤ 3000 |
| C23 | Fermat quotients equidistribute; Wieferich count ~ log log x | uniformity + BC | 10⁷ / 10⁸ |
| C24 | HL Conjecture-F family: C(A) predicts the full ranking of n²+n+A | Bateman–Horn family | 10⁶ × 100 A |
| C25 | ½ − s(x) ~ c·log log x/log x for consecutive primes mod 3 | LOS correlations | 10⁹ |

## Reproduction

```bash
pip install numpy
python3 run_all.py            # full suite, ~15-30 min on 4 cores
python3 verify/c04_quintuplet.py 1e8    # any single conjecture, custom bound
python3 compile_results.py    # rebuild RESULTS.md from results/*.json
```

Every verification prints observed vs predicted counts with
Poisson-normalized z-scores; the JSON files under `results/` are the
machine-readable record of the runs committed here.

## Honesty notes

* Large-integer primality (C09–C12) uses BPSW beyond the deterministic
  Miller–Rabin range — industry standard, no known counterexample, but
  formally "probable prime".
* Singular series for quadratic/cubic systems converge conditionally; the
  engine reports the truncation wobble between cutoffs as an error bar.
* Where the data *refuted* a first-draft statement, the memo says so
  (C20's naive Poisson, C21's first-guess bias direction, C13's naive
  tail model, C22's naive Exp(1) mean).  The surviving statements are the
  corrected ones — that is the engine working as designed.
