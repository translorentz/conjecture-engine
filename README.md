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
| C02 | cubic family: mean C(a)=1 exactly, limit law for C(a), uniform over a | derived Euler-product moments | 294 constants; 57 profiles |
| C03 | triplet race (0,2,6) mod 5: doubly-thinned contamination, class 1 leads | contamination calculus | 10⁹ |
| C04 | power-obstruction ladder for mᵏ = p + jᵏ: composite k impossible (thm); prime-k lanes follow BH for Dₖ | factorization + BH | k=4: 10⁸; k=2,3,5 counted |
| C05 | twin cyclotomic bases, complete φ(k)=2 family: k=4 parity-dead, k=6 ≡ k=3; Φ₃(n), Φ₃(n+1) both prime ~ C·I(N) | parity/identity + Bateman–Horn | 10⁷ |
| C06 | alternating cyclotomic chain p, Φ₃(p), Φ₆(Φ₃(p)) all prime ~ C·I(x) | Bateman–Horn (deg 1,2,4) | 10⁷ |
| C07 | sexy-pair contamination matrix: two orientations, drift classes 3 & 1 (mod 5), class 2 clean | contamination calculus | 10⁹ |
| C08 | null-mechanism race: (n²+1, n²+3) class race mod 5 is driftless (no square contamination possible) | contrast control for C21/C25 | 10⁷ |
| C09 | Fibonacci–Lucas twins: rank-disjoint finiteness, no completeness (148091 refutes naive tail) | convergent BC stress test | p ≤ 10⁴ |
| C10 | factorial twins (n!−1, n!+1 both prime): only n = 3 | convergent Borel–Cantelli | n ≤ 700 |
| C11 | n²+2ⁿ prime infinitely often (n ≡ 3 mod 6); κ via CRT-exact joint densities | exact local densities | n ≤ 6000; CRT exact to p ≤ 19 |
| C12 | pair-level MS reduction: window twin-count variance = pinned 4-tuple average G(H) | derived reduction + computation | G exact to H=3000 |
| C13 | boundary trichotomy for polynomial ladders (dead-parity / dead-3-adic / BH lanes) | divisibility + classification | lanes c=4,6 at 10⁶ |
| C14 | Stern lane race: norm-form contamination, provable null classes 5,7 (mod 8) | contamination calculus + genus theory | 2500 samples ≤ 10⁸ |
| C15 | least Goldbach summand: U ⇒ Exp(1), ordering deficit Θ_G ≈ 3.1–3.4 | occupancy anomaly | 2000 samples ≤ 10⁸ |
| C16 | π_d(x) ~ S(d)Li₂(x) uniformly + moving-window residual field with derived covariance kernel | HL + triple-constant kernel | 10⁸, d ≤ 6000; kernel 870 pairs + 2000-window test |
| C17 | orientation-resolved twin-member Goldbach law | 4-tuple singular series per n | 150 samples; shape 0.9993 |
| C18 | race sub-diffusivity: ρ₁ ≈ −0.037 universal; maxima below iid null | LOS repulsion | 4 races at 10⁹ |
| C19 | liminf over realized gaps of log p(g)/√g = √(e^γ/2) = 0.9437; 𝔖\*(g) waiting-time clause (slope −½, measured −0.47) | Cramér–Granville + HL factor | 4·10⁹ |
| C20 | prime counts in λ log x windows: Var/mean = 1 − (log h + γ + log 2π − 1)/log x | Gallagher + Montgomery–Soundararajan | 4·10⁹ |
| C21 | twin races mod 5/8 + contamination calculus; fresh cousin-race predictions verified directionally | explicit-formula analog | 4·10⁹ / 10⁹; cousins 10⁹ |
| C22 | Li(p(a,q))/φ(q): Exp(1)/Gumbel; canonical deficit Θ(q) → Θ > θ_disc^∞ on prime moduli (Θ = 1.67) | order statistics + stratified experiment | q ≤ 6000; 80 strat. moduli |
| C23 | multibase Fermat quotients: subtorus law, joint equidistribution, simultaneous Wieferich | Eisenstein–Lerch + vertical law | 664577 primes |
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
