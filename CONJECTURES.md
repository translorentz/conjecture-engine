# The 25 Conjectures (v6 roster)

The canonical formal statements, with derivations, admissibility
analyses, hierarchy placement, findings, and data, live in
`paper/conjectures.tex` / `paper/conjectures.pdf`; this file is the
working roster.  Numerical outcomes live in `RESULTS.md` and
`results/*.json`; the audit trail in `VERIFICATION.md`.

Notation: `BH(f1,...,fk)` is the Bateman–Horn singular series
`C = prod_p (1 - omega(p)/p) / (1 - 1/p)^k`; `I(N)` the matching main
term `int dt / prod_i log f_i(t)`; `S(d)` the twin singular series;
`gamma` Euler's constant.  Novelty tags: **[bench]** attributed
benchmark / (a)-core; **[research]** mechanism, law, family
uniformity, or dichotomy with no prior trace found (audited —
see VERIFICATION.md).

| # | Statement (short form) | Tag | Script |
|---|---|---|---|
| C01 | **Uniform quadratic de Polignac**: (n²+1, n²+1+d) both prime ~ C(d)·I(N) *uniformly* over even d ≤ (log N)^B; d=2 is the classical pair | [research] family; [bench] d=2 | `c01_quadratic_depolignac_family.py`, `c01_quadratic_twin_pair.py` |
| C02 | n³+2 prime infinitely often, ~ C·I(N), C = 1.298435±3e-4 | [bench] | `c02_cubic_shift.py` |
| C03 | Chernick chain p, 2p−1, 3p−2 all prime, ~ C·I(x) | [bench] | `c03_prime_ap_chain.py` |
| C04 | **Power-obstruction ladder** for mᵏ = p + jᵏ: composite k impossible (theorem); prime-k lanes follow BH for Dₖ(m) = mᵏ−(m−1)ᵏ | [research] | `c04_power_ladder.py` |
| C05 | **Twin cyclotomic bases, complete φ(k)=2 family**: k=4 dead by parity (only (2,5)); k=6 ≡ k=3 via Φ₆(x)=Φ₃(x−1); live instance Φ₃(n), Φ₃(n+1) both prime ~ C·I(N) | [research] family analysis; [bench] instance | `c05_cyclotomic_twin_family.py` |
| C06 | **Alternating cyclotomic chain**: p, Φ₃(p), Φ₆(Φ₃(p)) all prime, ~ C·I(x), C = 3.6143±0.011; naive iterated Φ₃ chain is inadmissible at 3 (part of the statement) | [research] | `c06_repunit_chain.py` |
| C07 | p and p²−2 both prime, ~ C·I(x) (feeds C21's deterministic term) | [bench] | `c07_psquared_minus2.py` |
| C08 | **Null-mechanism race**: (n²+1, n²+3) admits no square contamination (algebraic); class race n ≡ 1 vs 4 (mod 5) is driftless — the negative control for C21/C25 | [research] | `c08_null_race.py` |
| C09 | #{p ≤ x: F_p prime} ~ c_F log x, c_F < e^γ/log φ (deficit flagged; Grantham–Granville correction open) | [bench]+flag | `c09_fibonacci_primes.py` |
| C10 | **Factorial twins**: window rigidity (±1 the only bounded offsets at n!); n=3 the only factorial twin; joint independence of F₊, F₋ | [research], priority label softened per 5th review | `c10_factorial_twins.py` |
| C11 | n²+2ⁿ (n ≡ 3 mod 6): infinitely many primes; κ defined via CRT-exact joint densities (entanglement-aware net, factorization exact through p ≤ 19), κ = 4.2734 | [research] | `c11_n2_plus_2n.py`, `c11b_crt_kappa.py` |
| C12 | #{n ≤ N: n!+1 prime} ~ e^γ log N | [bench] | `c12_factorial_primes.py` |
| C13 | Non-cube n = p + k³ exceptions finite; cube lane obeys BH for 3k²−3k+1 (restated after self-refutation, Finding f:c13) | [bench] core | `c13_prime_plus_cube.py` |
| C14 | Stern list: exactly ten odd n ≠ p + 2k², largest 5993 | [bench] | `c14_stern_2k2.py` |
| C15 | Goldbach (3,3) lane: every n ≡ 2 (4), n ≥ 6 is p+q, p ≡ q ≡ 3 (4); R₃ ~ ½·S(n)·I | [bench] | `c15_goldbach_mod4.py` |
| C16 | Uniform quantitative de Polignac: π_d ~ S(d)Li₂ uniformly, d ≤ (log x)^A; **(ii) moving-window residual field (canonical randomization), Gaussian with HL triple-constant kernel** — window experiment matches kernel entrywise at 0.86 | [bench] (i); [research] (ii) | `c16_uniform_depolignac.py`, `c16b_covariance_kernel.py`, `c16c_window_field.py` |
| C17 | Dubner: every even n ≥ 4210 is a sum of two twin members; 35 exceptions complete | [bench] | `c17_twin_goldbach.py` |
| C18 | Twin-gap records ≍ log³x, working constant 1/(2C₂) | [bench] | `c18_twin_gap_records.py` |
| C19 | First-occurrence gaps: liminf over realized gaps of log p(g)/√g = √(e^γ/2) = 0.943682; **(iii) 𝔖\*(g)-waiting-time clause, coefficient −½ (measured −0.466)** | [research] | `c19_gap_first_occurrence.py`, `c19b_waiting_refinement.py` |
| C20 | Microscopic variance law: Var/E = 1 − (log(λ log x)+γ+log 2π−1)/log x + o(1/log x) (microscopic extrapolation + test of Montgomery–Soundararajan) | [research] test | `c20_poisson_intervals.py` |
| C21 | **Twin races mod 5/8 + the prime-power contamination calculus (v)**: Lemma + drift/null/sign clauses; the calculus generated fresh cousin-race (n,n+4) predictions (class 4 mod 5, class 1 mod 8), verified directionally at 1e9 | [research] | `c21_twin_race_mod5.py`, `c21b_twin_race_mod8.py`, `c21c_cousin_races.py` |
| C22 | Least primes: (i) Exp(1)/Gumbel; **(ii) canonical deficit invariant Θ(q) = (1−E[U])·log q → Θ > θ_disc^∞ on prime moduli** (Θ = 1.671±0.009; θ decomposition kept as diagnostic; stratified experiment differentiates from Leung's smooth-q effects) | [bench] (i); [research] (ii) | `c22_least_prime_ap.py`, `c22b_stratified.py` |
| C23 | Fermat quotients: LIL-scale equidistribution; shrinking targets; W(x) = loglog x + O((loglog x)^{1/2+ε}) | [bench] | `c23_fermat_quotients.py` |
| C24 | Conjecture F family: Q_A ~ C(A)I_A uniformly over odd A ≤ (log N)^B; **(ii) covariance kernel from pair singular series — computed cross-member kernel is null; deficit is diagonal** | [bench] (i); [research] (ii) | `c24_hl_family_F.py`, `c24b_family_kernel.py` |
| C25 | **Goldbach lane race**: D = R₃−R₁ ~ D_sys (all square contamination in one lane); HL-weighted drift model (0.98 of empirical); internal null lane n ≡ 1 (3); sign density E[Φ(κ)] | [research] | `c25_goldbach_lane_race.py`, `c25b_weighted_drift.py` |

Retired slot occupants retained as calibration (namespaced results):
quintuplet (`legacy_c04_quintuplet.py`), shifted pair
(`legacy_c05_shifted_quadratic_pair.py`), Sophie Germain sub-chain
(`c06_cyclotomic_germain.py`), quadratic triple
(`c08_quadratic_triple.py`), primorial benchmark
(`legacy_c10_primorial_primes.py`), primorial twins — Lillie's
(`c10_primorial_twins.py`), LOS mod-3 restatement
(`legacy_c25_consecutive_mod3.py`).
