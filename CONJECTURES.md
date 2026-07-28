# The 25 Conjectures (v9 roster)

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
| C02 | **Cubic family distribution law**: mean C(a) = 1 exactly (lemma); C(a) ⇒ random Euler product (derived sd 0.2762); uniformity over a ≤ (log N)^B; instance-level in Kowalski's framework | [research] family; a=2 [bench] retained | `c02_cubic_shift.py`, `c02b_cubic_family.py` |
| C03 | **Triplet contamination race** (0,2,6) mod 5: unique doubly-thinned surviving configuration (q²−2,q²,q²+4); class 1 leads | [research] calculus instance; Chernick chain [bench] retained | `c03_prime_ap_chain.py`, `c03b_triplet_race.py` |
| C04 | **Power-obstruction ladder** for mᵏ = p + jᵏ: composite k impossible (theorem); prime-k lanes follow BH for Dₖ(m) = mᵏ−(m−1)ᵏ | [research] | `c04_power_ladder.py` |
| C05 | **Twin cyclotomic bases, complete φ(k)=2 family**: k=4 dead by parity (only (2,5)); k=6 ≡ k=3 via Φ₆(x)=Φ₃(x−1); live instance Φ₃(n), Φ₃(n+1) both prime ~ C·I(N) | [research] family analysis; [bench] instance | `c05_cyclotomic_twin_family.py` |
| C06 | **Alternating cyclotomic chain**: p, Φ₃(p), Φ₆(Φ₃(p)) all prime, ~ C·I(x), C = 3.6143±0.011; naive iterated Φ₃ chain is inadmissible at 3 (part of the statement) | [research] | `c06_repunit_chain.py` |
| C07 | **Contamination matrix**: sexy pairs, two surviving orientations feeding classes 3 and 1 (mod 5), class 2 clean; independently verified algebra | [research] calculus instance; {p,p²−2} [bench] retained | `c07_psquared_minus2.py`, `c07b_sexy_matrix.py` |
| C08 | **Null-mechanism race**: (n²+1, n²+3) admits no square contamination (algebraic); class race n ≡ 1 vs 4 (mod 5) is driftless — the negative control for C21/C25 | [research] | `c08_null_race.py` |
| C09 | **Fibonacci–Lucas twins stress test**: rank-disjointness lemma; finiteness WITHOUT completeness (A080327's 148091 refutes the naive tail — caught by our own audit pre-publication) | [research] structural + calibration finding | `c09_fibonacci_primes.py`, `c09b_fib_lucas_twins.py` |
| C10 | **Factorial twins**: window rigidity n≥4 (±1 the only bounded offsets at n!); uniqueness of n=3 **attributed to OEIS A088054** (6th review); joint fluctuation model for F₊, F₋ | uniqueness [bench] (a); clauses (i)/(iii) [research] | `c10_factorial_twins.py` |
| C11 | n²+2ⁿ (n ≡ 3 mod 6): infinitely many primes; κ defined via CRT-exact joint densities (entanglement-aware net, factorization exact through p ≤ 19), κ = 4.2734 | [research] | `c11_n2_plus_2n.py`, `c11b_crt_kappa.py` |
| C12 | **Pair-level Montgomery–Soundararajan reduction**: window variance of twin counts = pinned 4-tuple average G(H); −G/log H diverges (measured slope 3.4–3.7 vs single-prime ½); asymptotic form registered open | [research] | `c12_factorial_primes.py`, `c12b_pair_ms.py` |
| C13 | **Boundary trichotomy**: (m−j) | F(m)−F(j) collapse (Cunningham's cuban case attributed); dead-parity/dead-3-adic/BH-lane classification for x³+cx; two new lanes verified | [research] classification; HL core [bench] retained | `c13_prime_plus_cube.py`, `c13b_boundary.py` |
| C14 | **Stern lane race**: k-parity drift = norm-form (x²+2y²) contamination; classes 1,3 (mod 8) contaminated in opposite lanes, 5,7 provably null (genus theory) | [research] calculus instance; Stern list [bench] retained | `c14_stern_2k2.py`, `c14b_stern_lane_race.py` |
| C15 | **Least Goldbach summand**: time-changed U ⇒ Exp(1); canonical ordering deficit Θ_G = 3.1–3.4 (sibling of C22(ii)) | [research]; (3,3)-lane [bench] retained (Martin) | `c15_goldbach_mod4.py`, `c15b_least_goldbach.py` |
| C16 | Uniform quantitative de Polignac: π_d ~ S(d)Li₂ uniformly, d ≤ (log x)^A; **(ii) moving-window residual field (canonical randomization), Gaussian with HL triple-constant kernel** — window experiment matches kernel entrywise at 0.86 | [bench] (i); [research] (ii) | `c16_uniform_depolignac.py`, `c16b_covariance_kernel.py`, `c16c_window_field.py` |
| C17 | **Orientation-resolved twin-member Goldbach**: four n-dependent 4-tuple singular series; shape verified at 0.9993, level deficit flagged open | [research]; Dubner basis+kernel [bench] retained | `c17_twin_goldbach.py`, `c17b_twin_member_goldbach.py` |
| C18 | **Race sub-diffusivity**: universal negative step correlations ρ₁ ≈ −0.037 (LOS mechanism); running maxima at 2–17% of iid null; rigid-vs-diffusive dichotomy registered | [research] measurement; records [bench] retained (Kourbatov) | `c18_twin_gap_records.py`, `c18b_race_max.py` |
| C19 | First-occurrence gaps: liminf over realized gaps of log p(g)/√g = √(e^γ/2) = 0.943682; **(iii) 𝔖\*(g)-waiting-time clause, coefficient −½ (measured −0.466)** | [research] | `c19_gap_first_occurrence.py`, `c19b_waiting_refinement.py` |
| C20 | Microscopic variance law: Var/E = 1 − (log(λ log x)+γ+log 2π−1)/log x + o(1/log x) (microscopic extrapolation + test of Montgomery–Soundararajan) | [research] test | `c20_poisson_intervals.py` |
| C21 | **Twin races mod 5/8 + the prime-power contamination calculus (v)**: Lemma + drift/null/sign clauses; the calculus generated fresh cousin-race (n,n+4) predictions (class 4 mod 5, class 1 mod 8), verified directionally at 1e9 | [research] | `c21_twin_race_mod5.py`, `c21b_twin_race_mod8.py`, `c21c_cousin_races.py` |
| C22 | Least primes: (i) Exp(1)/Gumbel; **(ii) canonical deficit invariant Θ(q) = (1−E[U])·log q → Θ > θ_disc^∞ on prime moduli** (Θ = 1.671±0.009; θ decomposition kept as diagnostic; stratified experiment differentiates from Leung's smooth-q effects) | [bench] (i); [research] (ii) | `c22_least_prime_ap.py`, `c22b_stratified.py` |
| C23 | **Multibase subtorus law**: Eisenstein–Lerch homomorphism (exact, attributed) + vertical joint equidistribution for independent bases + simultaneous-Wieferich accounting; sides with CDP against Gras | [research] (iv); single-base [bench] retained | `c23_fermat_quotients.py`, `c23b_multibase.py` |
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
