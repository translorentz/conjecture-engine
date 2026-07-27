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
* **`VERIFICATION.md`** — independent audit: novelty verdicts with citations,
  adversarial battery outcomes (one refutation: C13 as first stated), and
  salvaged clean-context re-verifications.
* **`paper/conjectures.tex`** (+ compiled PDF) — the formal write-up of all
  25 statements with constants, data, and attribution.
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
| C01 | uniform quadratic de Polignac: (n²+1, n²+1+d) ~ C(d)·I(N) uniformly over even d | Bateman–Horn family | 150 shifts at 10⁶; d=2 at 10⁷ |
| C02 | n³+2 prime infinitely often, count ~ C·I(N) | Bateman–Horn (cubic) | 10⁷ |
| C03 | p, 2p−1, 3p−2 all prime (AP chain), ~ C·I(x) | Bateman–Horn (3 linear) | 3·10⁸ |
| C04 | power-obstruction ladder for mᵏ = p + jᵏ: composite k impossible (thm); prime-k lanes follow BH for Dₖ | factorization + BH | k=4: 10⁸; k=2,3,5 counted |
| C05 | twin cyclotomic bases, complete φ(k)=2 family: k=4 parity-dead, k=6 ≡ k=3; Φ₃(n), Φ₃(n+1) both prime ~ C·I(N) | parity/identity + Bateman–Horn | 10⁷ |
| C06 | alternating cyclotomic chain p, Φ₃(p), Φ₆(Φ₃(p)) all prime ~ C·I(x) | Bateman–Horn (deg 1,2,4) | 10⁷ |
| C07 | p and p²−2 both prime, ~ C·I(x) | Bateman–Horn | 10⁷ |
| C08 | null-mechanism race: (n²+1, n²+3) class race mod 5 is driftless (no square contamination possible) | contrast control for C21/C25 | 10⁷ |
| C09 | #{p ≤ x: F_p prime} ~ c_F log x, c_F < e^γ/log φ (deficit flagged) | LPW screening | p ≤ 10⁴ |
| C10 | factorial twins (n!−1, n!+1 both prime): only n = 3 | convergent Borel–Cantelli | n ≤ 700 |
| C11 | n²+2ⁿ prime infinitely often (n ≡ 3 mod 6); κ via CRT-exact joint densities | exact local densities | n ≤ 6000; CRT exact to p ≤ 19 |
| C12 | #{n ≤ N: n!+1 prime} ~ e^γ log N | Mertens boost | n ≤ 700 |
| C13 | restated: non-cube exceptions of n = p + k³ finite; cubes obey a theorem | Borel–Cantelli + local | 10⁹ |
| C14 | exactly ten odd n are not p + 2k² (k ≥ 1); largest 5993 | Borel–Cantelli | 10⁹ |
| C15 | every n ≡ 2 (4), n ≥ 6, is p+q with p ≡ q ≡ 3 (4); R₃ ~ ½S(n)I(n) | HL Goldbach | 10⁹ |
| C16 | π_d(x) ~ S(d)Li₂(x) uniformly + residual field with derived covariance kernel | HL + triple-constant kernel | 10⁸, d ≤ 6000; kernel 870 pairs |
| C17 | every even n ≥ 4210 is a sum of two twin-pair members (35 exceptions) | Borel–Cantelli on twins | 10⁹ |
| C18 | twin-gap records ≍ log³x, working constant 1/(2C₂) | Cramér for thinned process | 4·10⁹ |
| C19 | liminf over realized gaps of log p(g)/√g = √(e^γ/2) = 0.9437 | Cramér–Granville | 4·10⁹ |
| C20 | prime counts in λ log x windows: Var/mean = 1 − (log h + γ + log 2π − 1)/log x | Gallagher + Montgomery–Soundararajan | 4·10⁹ |
| C21 | twin race mod 5/8: lemma + drift law via the (q²−2, q²) mechanism; no persistent leader | explicit-formula analog | 4·10⁹ / 10⁹ |
| C22 | Li(p(a,q))/φ(q): Exp(1)/Gumbel; deficit = θ_disc (defined control) + θ_corr > 0 on prime moduli | order statistics + stratified experiment | q ≤ 6000; 80 strat. moduli |
| C23 | Fermat quotients: LIL-scale equidistribution; Wieferich count ~ log log x | uniformity + BC | 10⁷ / 10⁸ |
| C24 | HL Conjecture-F family: uniform + pair-series covariance kernel (computed null cross-kernel) | Bateman–Horn family | 10⁶ × 100 A; 1225 pairs |
| C25 | Goldbach lane race: D = R₃−R₁ ~ D_sys, HL-weighted model, internal null lane n ≡ 1 (3) | explicit-formula analog | 10⁸, 500+400 samples, 5.2σ |

## Reproduction

```bash
pip install numpy
python3 run_all.py            # full suite, ~15-30 min on 4 cores
python3 verify/c04_power_ladder.py 1e8  # any single conjecture, custom bound
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
