# Independent verification: novelty audit + adversarial testing

Three independent layers were run against the 25 conjectures after the
primary verification suite:

1. **Novelty audit** — five search agents combed OEIS, arXiv, MathWorld,
   PrimePages and the literature for prior art, one batch of five
   conjectures each.
2. **Adversarial battery** (`adversarial/battery.py`) — scripted refutation
   attempts pushing every falsifiable-by-instance conjecture a decade or
   more past its original bound (exception hunts in (10^8, 10^9], the
   statistical laws re-tested at 4·10^9, uniformity stressed at 3x the
   d-range and 2x the q-range).  Machine-readable outcomes in
   `results/adversarial.json`.
3. **Clean-context adversarial agents** — five independent agents (Opus),
   given only the bare statements and told to refute them with their own
   code.  All five were killed mid-run by a session usage limit, but their
   working artifacts (independent sieves, constants, exception lists)
   survive and are summarized below where they reached conclusions.

## Headline outcomes

* **C13 was REFUTED as originally stated — by our own battery.** Every
  exception it found in (10^8, 10^9] is a perfect cube: n = k^3 escapes
  only through n − (k−1)^3, since n − j^3 factors as
  (k−j)(k^2+kj+j^2), so k^3 is representable iff 3k^2−3k+1 is prime.
  The exception set is therefore infinite (~x^{1/3}).  The conjecture was
  restated for non-cube n (memo C13), the cube criterion is now
  machine-checked as a theorem in-range, and the cube lane yields a fresh
  Bateman–Horn instance.  The original overreach and its correction are
  kept on record.
* **One memo claim was falsified by the novelty audit**: C14's ten-term
  exception list for p + 2k^2 (k ≥ 1) is OEIS A060003 verbatim, and 1493
  is the well-known largest Stern prime — the memo's novelty note said
  otherwise and has been corrected.
* **No other conjecture was refuted** by any layer.

## Novelty verdicts

(a) = previously stated essentially verbatim; (b) = classical family, this
quantified instance apparently unstated; no (c)/(d) verdicts occurred.

| # | Verdict | Prior art found |
|---|---|---|
| C01 | (a) for d=2; family law unstated | OEIS A080149 (with Cloitre's c≈2.9 asymptotic); Carella arXiv:1710.07827 (unrefereed) has the BH form for d=2; no statement of the uniform-over-d quadratic family found (v6 lift) |
| C02 | replaced v9: family law ADJACENT (Kowalski framework, attributed) | Kowalski Acta Arith. 148 (2011) owns the random-Euler-product limit mechanism (k-tuples); Browning–Sofos–Teräväinen own height-averaged BH; the one-parameter cubic-shift law, exact mean-one lemma, and short-range uniformity appear unstated |
| C03 | replaced v9: triplet race ADJACENT-CLEAR | mechanism classical (RS 1994); tuple-level biases exist (LOS, Meng, Wu); the binary mod-5 triplet race with unique surviving orientation unstated; algebra independently verified; Chernick chain retained [bench] (Dubner 2002) |
| C04 | (b) | A078946 (consecutive-primes variant) bare; constant unpublished |
| C05 | (b), family analysis new | no OEIS entry, no literature trace found for the pair; the complete φ(k)=2 family analysis (k=4 parity-dead, Φ₆(x)=Φ₃(x−1) collapse) added in v6, no prior trace |
| C06 | replaced in v6 | alternating chain p, Φ₃(p), Φ₆(Φ₃(p)): no OEIS entry, no literature trace (searched Cunningham-chain and repunit-prime literature at abstract depth); retained sub-chain: A053182 + **A188596 is literally the sub-chain constant** (1.5217315...) |
| C07 | replaced v9: contamination matrix ADJACENT-CLEAR | no sexy-pair residue race found; two-orientation complementary structure + certified null class 'genuinely unstated' per audit; algebra independently verified; {p,p²−2} retained [bench] |
| C08 | replaced in v6 | null-mechanism race over (n²+1, n²+3) mod 5: no prior statement found; retired triple n²+{1,3,7}: family in OEIS since 2000 (3rd review), singular series plausibly new |
| C09 | replaced v9: PRIOR ART on object + draft REFUTED by audit | OEIS A080327 catalogues F/L joint primality incl. 148091, destroying the draft completeness list; slot now: rank-disjointness lemma + finiteness without completeness + quantified naive-constant refutation; single-sided laws retained [bench] (GG arXiv:2307.07894) |
| C10 | replaced in v6 | **primorial twins: PRIORITY FAILURE — Lillie arXiv:2110.04302 (2021) states both the O(n⁻²) joint law and the three-instance prediction; our snippet-depth search missed it (4th review caught it)**. Factorial twins: **second priority correction (6th review)** — the uniqueness conjecture is on record as OEIS A088054's intersection comment; clause (ii) attributed there, claimed content = window-rigidity (i) and joint-fluctuation (iii) clauses |
| C11 | (b), upgraded v6 | A064539 has the sequence and the n ≡ 3 (mod 6) note; the κ-quantified count unstated; v6 restates κ via CRT-exact joint densities (entanglement-aware) — factorization verified exact through p ≤ 19 |
| C12 | replaced v9: pair-level MS reduction — 'best novelty, prosecute' per audit | MS own the single-prime reduction; Kowalski has first-order Poisson for twins in intervals; Kuperberg's singular-series sums never pin a sub-tuple; the pinned average G(H) and its super-log growth appear unevaluated anywhere; factorial-prime law retained [bench] (Caldwell–Gallot) |
| C13 | upgraded v9: boundary trichotomy | divisibility principle textbook; cubic case is Cunningham 1923 (cuban primes A002407) — attributed; the dead-parity/dead-3-adic/BH-lane family classification and reducible-boundary link to C04 appear unstated; HL core retained (a) \[HL1923\]; **as first stated in v1, false — see above** |
| C14 | replaced v9: Stern lane race CLEAR | no k-parity lane race found; null classes = classical genus theory of disc −8 (attributed); ψ-weighting mechanism stated per audit flag; Stern list retained [bench] (A060003) |
| C15 | replaced v9: least-summand law ADJACENT | extremal theory worked (Granville–van de Lune–te Riele; Oliveira e Silva–Herzog–Pardi Math. Comp. 83 (2014), cited); the time-changed Exp(1) law and deficit Θ_G appear unstated (OeSHP §5 could not be fully accessed — stated in paper); (3,3) lane retained [bench] (Martin) |
| C16 | (a)-core, kernel new | uniform HL-B is standard (Goldston–Ledoan); Brent 1975, Korevaar–te Riele 2010 did profile verifications; the derived triple-constant covariance kernel of (ii) (v6) appears unstated |
| C17 | replaced v9: orientation decomposition ADJACENT near prior art | Dubner's own text has the log⁻⁴ integral kernel (μ₄) — attributed; claim narrowed to the four orientation-resolved singular series and n-profile; level deficit flagged open; basis conjecture retained [bench] (Dubner 2000, A007534) |
| C18 | replaced v9: race sub-diffusivity CLEAR (as measurement) | audit warned the naive Darling–Erdős claim contradicts RS almost-periodicity (Montgomery/Ng (logloglog)^α class) — heeded: slot states the measured finite-x law (universal ρ₁ ≈ −0.037, suppressed maxima) with the rigid-vs-diffusive dichotomy registered open; records retained [bench] (Kourbatov) |
| C19 | (b) | Shanks/Wolf/Nicely endorse limit slope 1; our Granville-corrected 0.9436 appears unstated — a genuinely different constant on the books |
| C20 | (b) | constant γ+log 2π−1 is Montgomery–Soundararajan (mesoscopic); the microscopic finite-x Var/mean law + test appears unstated |
| C21 | (b) | no prior twin-race-mod-5 statement or q²−2 mechanism found (closest: arXiv:2111.09053; Brent's "twins more random") |
| C22 | (b), stratified v6 | Exp(1) limit is Haddad–Leung–Sabuncu arXiv:2408.11781; Wagstaff 1979/Fiori 2404.02329 for the max; the 1/log q deficit law and ordering anomaly appear unstated; v6 defines θ_disc by a named control and differentiates θ_corr from Leung's smooth-q effects by the prime/smooth stratified experiment |
| C23 | upgraded v9: multibase subtorus law | homomorphism = Eisenstein–Lerch (attributed); simultaneous-Wieferich folklore (Conrad) attributed; horizontal joint studies (Ostafe–Shparlinski; Cobeli–Zaharescu FQM statistics) attributed — the VERTICAL multibase torus law appears unstated; conflict with Gras's model cited and a side taken; single-base heuristic retained [bench] (CDP 1997, Dorais–Klyve) |
| C24 | (a)-core, kernel new | Hardy–Littlewood Conjecture F (1923); Fung–Williams 1990, Jacobson–Williams 2003 run the same constants-predict-density program; the pair-singular-series covariance kernel with computed null cross-correlation (v6) appears unstated |
| C25 | replaced v4, matured v6 | slot originally held an LOS restatement (arXiv:1603.03720); the Goldbach lane race has no prior trace; v6 adds the HL-weighted drift, the n≡1(3) internal null lane, and the sign-density clause |

Net (v6 roster): the research group is C01 (family law), C04, C06, C08,
C09–C11, C16(ii), C19–C22, C24(ii), C25, with the square-contamination
mechanism family (C21, C25, null control C08), C22(ii)'s stratified
ordering anomaly, and the derived kernels (C16(ii)/C24(ii)) the strongest
claims to new content; the remainder are re-derivations/verifications of
statements already on the record — which the criteria document counts as
a feature (family membership) but which we attribute explicitly.

## Adversarial battery outcomes (results/adversarial.json)

| Target | Test | Outcome |
|---|---|---|
| C13 | exception census (10^8, 10^9] | **REFUTED as stated** — 412 new exceptions, all cubes; conjecture restated |
| C14 | hunt for an 11th exception to 10^9 | none — 5993 stands a decade past the original bound |
| C15 | hunt for a (3,3)-lane Goldbach failure to 10^9 | none |
| C17 | hunt for a 36th Dubner exception to 10^9 | none (independently re-verified by a dead agent's sumset code — same 35-element list) |
| C16 | uniformity at d ≤ 6000, x = 10^8 | holds; max |z| = 2.01 over 3000 values of d |
| C18 | records to 4·10^9 | new record gap 5292 after twin 2,466,641,069; G/log³x = 0.49, order intact |
| C19 | first occurrences to 4·10^9 | slope 1.307 → 1.297, falling as required; 11 of 12 previously-missing gaps filled |
| C20 | variance law at 4·10^9 | Var/mean = 0.7998 vs predicted 0.7960 (λ=1); 0.7670 vs 0.7646 (λ=2) |
| C21 | race to 4·10^9 | D1 = −2196 vs noise 2444: no persistent leader, exactly as conjectured (bias/noise ~ 1/log x) |
| C22 | mean U at q ∈ (3000, 6000] | 0.7707 → 0.7758: recovery toward 1 continues; θ ≈ 1.92 |
| C25 | ĉ at 4·10^9 | ĉ = 0.3703 (from 0.3752 at 10^9): slow drift, consistent with o(1) term; symmetry 0.99989 |
| C04 | count at 4·10^9 | obs 15236 vs pred 15230.3 — ratio 1.0004, z = +0.05 |

## Salvaged clean-agent evidence (agents killed by session limits)

* **C06/C07/C08**: independent singular-series computation with primes to
  10^9 gave 1.521730 / 3.383227 / 10.647706 (ours: 1.52166 / 3.38322 /
  10.64599, each within stated truncation wobble; C06 agrees with OEIS
  A188596 to 6 digits).  Independent presieve+MR counts to 3·10^7:
  final ratios 0.9962 / 0.9965 / 1.0059, all |z| < 1.6.  (The agent first
  got z ≈ −22 from a bug in its own sieve — every prime n ≤ Q was killed
  by its own modulus — diagnosed and fixed by the agent itself; the
  corrected run agrees with ours.)
* **C09**: independent fast-doubling + BPSW scan reproduced exactly our 25
  Fibonacci prime exponents ≤ 10^4 and the persistent ~27% deficit against
  e^γ/log φ (z ≈ −1.5 at every scale — consistent with Grantham–Granville's
  warning that the naive constant needs O(1) corrections).
* **C11**: independent congruence sweep to n = 3000: zero primes off the
  n ≡ 3 (mod 6) lane, hits {3,9,15,21,33,2007,2127} as ours.
* **C12**: independent scan to n = 500: 15 hits, z ≤ +1.2 against e^γ log N.
* **C17**: independent sumset algorithm to 10^9: identical 35 exceptions.
* **C19**: independent first-occurrence table to 10^9 matches ours
  (e.g. p(282) = 436,273,009).
* **C23**: KS at x = 10^5, 10^6, 10^7, 10^8: √N·KS = 0.82, 0.82, 0.52,
  0.63 — bounded with no drift (square-root discrepancy confirmed at four
  scales); Wieferich = {1093, 3511} at 10^8; small-quotient census
  K=100: 169 obs vs 161.2 model, K=1000: 1133 vs 1143.9.
* **C24**: independent two-method constants (Euler product vs direct)
  agree to 4-5 digits; spot ratios at N = 10^6 within 0.3% of 1.
* **C22**: independent per-q statistics for q ≤ 300 reproduce the mean-U
  anomaly (0.71–0.82, fraction of classes with U < 1 ≈ 0.73).

## What remains open / flagged

* C09's constant: data sit ~27% below e^γ/log φ at two independent scans;
  the memo's humility clause is now a quantified flag — the mod-5
  divisor-structure correction is the suite's most concrete "needs a
  Granville patch" candidate.
* C25's ĉ drifts slowly (0.40 → 0.37 over three decades): the leading-order
  form survives, but a secondary term is visible; the constant should be
  treated as ĉ(∞) ∈ [0.30, 0.40] until the LOS secondary terms are put in.
* C22's θ is measured (≈1.9 and slowly rising at q ~ 6000), not derived —
  the deepest unexplained number produced by the suite.

## Twin-citation gate (bibliography certification)

Protocol: two independent Opus verifiers must unanimously agree every
reference (1) exists, (2) has correct authors, titles, venue data and
DOI; any flag fails the gate, references are remediated, and the gate is
re-run with a FRESH pair until a unanimous pass is obtained on the final
text.

* **Round 1** (verifiers A, B — 27 entries): both independently found the
  same three failures — HLS author initials (corrected to T. Haddad,
  S.-K. Leung, C. Sabuncu), PairBias missing author (W. Puszkarz), Fiori
  paraphrased title (replaced by arXiv's literal metadata, typo marked
  [sic]).  A additionally could not verify Dubner2000's page range; B
  confirmed it via the OEIS-hosted article.  Remediation: 3 fixes, 2
  cosmetic title normalizations, DOIs added to every entry possessing one.
* **Round 2** (fresh verifiers C, D): zero FAILs; both independently
  flagged only Dubner2000's page range as unverifiable (non-indexed
  journal).  Remediation: unverifiable pages dropped, leaving only
  fields positively confirmed by prior verifiers.
* **Round 3** (fresh verifiers E, F): **27/27 PASS from both, zero FAIL,
  zero UNVERIFIED — gate passed unanimously.**
* **Round 4** (fresh verifiers G, H; triggered by adding S.-K. Leung,
  arXiv:2402.07941 during the third-review revisions): **28/28 PASS from
  both, zero FAIL, zero UNVERIFIED — gate passed unanimously on the
  final (v5) bibliography.**
* **Round 6** (fresh verifiers K, L; triggered by adding Kowalski,
  Acta Arith. 148 (2011), and Oliveira e Silva-Herzog-Pardi, Math.
  Comp. 83 (2014), during the v9 replacement round): **32/32 PASS
  from both, zero FAIL, zero UNVERIFIED — gate passed unanimously.**
* **Round 5** (fresh verifiers I, J; triggered by adding Lillie
  arXiv:2110.04302 and Rubinstein–Sarnak, Exp. Math. 3 (1994), during
  the fourth-review revisions): **30/30 PASS from both, zero FAIL,
  zero UNVERIFIED — gate passed unanimously on the v6 bibliography.**
  Both independently confirmed the Lillie entry against the arXiv
  record, the Rubinstein–Sarnak DOI against the publisher, and that
  the Fiori title's [sic] typo is genuinely present in the source.

The gated bibliography (30 entries; every DOI verified to resolve to
the exact work, every DOI-less entry verified to legitimately lack
one) is identical in `paper/conjectures.tex` and the
provenance-stripped `paper/conjectures_blind.tex`.

## Wholesale replacements (post-second-review)

On the operator's instruction, four conjectures judged "novelty:
none/very low" by the external review were replaced wholesale with
novelty-checked, mechanism-backed statements (paper v4); the retired
originals' scripts are retained as verify/legacy_*.py and their results
in git history:

| Slot | Retired | Replacement | Verification |
|---|---|---|---|
| C04 | quintuplet (0,2,6,12,14) | power-obstruction ladder (CORRECTED by 3rd review: prime-vs-composite, not even/odd — odd composite k also obstructed) | k=4 sweep to 1e8; k=9/15/25 direct; k=2/3/5 ratios 0.9998/1.0015/0.9983 |
| C05 | arbitrary pair n²+n+{1,7} | twin cyclotomic bases Φ₃(n), Φ₃(n+1) | C=2.964239; 1e7 ratio 1.0090 (z +1.64) |
| C10 | Caldwell–Gallot p#+1 count | primorial twins finite, list = {3,5,11} | exhaustive p ≤ 4000; model tail 7.3e-3 |
| C25 | LOS mod-3 restatement | Goldbach lane race: D = R₃−R₁ ~ D_sys (square contamination, all in lane (1,1)) | 500 samples ≤ 1e8: ratio 1.19±0.2, lead at 5.2σ, sign frac 0.592 |

Each replacement was novelty-searched before implementation (no prior
trace found for any of the four) and verified before entering the paper.


## Third external review (paper v4 -> v5)

The third review refuted C4 as stated (odd composite k: D_k never
prime — verified k=9,15,21,25,27,33), caught a stale attribution table
(retired C10/C25 occupants' citations), and flagged the C8 prior-art
overstatement and the missing Leung comparison at C22.  All accepted
and fixed in v5; C21 gained the mod-8 companion clause (entire bias on
class 7), verified at 1e9 (D7=+212 vs T=+254, noise ~1068, controls
symmetric).  Full review: paper/EXTERNAL_REVIEW_3.md; response:
paper/EXTERNAL_REVIEW_3_RESPONSE.md.

## Fourth external review (paper v5 -> v6)

The fourth review was assessed in `paper/REVISION_PLAN.md` (verdict:
substantially fair; both priority claims verified against primary
sources before conceding).  Executed changes:

**Priority/correctness fixes.** C10's primorial twins found already
stated by Lillie arXiv:2110.04302 (our own earlier search had surfaced
the preprint but read it only at snippet depth — recorded in the paper
as Finding f:c10, with the audit protocol hardened to abstract-depth
reads).  C19 restricted to realized gaps; C23(i) recalibrated to the
Chung–Smirnov LIL scale and (ii)'s quantifier fixed; C13's
"Chebyshev bounds" corrected to an upper-bound sieve; C20 demoted to a
microscopic extrapolation/test of Montgomery–Soundararajan with the
quantitative-uniform hypothesis spelled out.

**Replacements (novelty-searched at abstract depth, verified before
admission).**
| Slot | New occupant | Verification |
|---|---|---|
| C06 | alternating cyclotomic chain p, Φ₃(p), Φ₆(Φ₃(p)) (naive iterate is inadmissible at 3 — part of the statement) | C=3.6143±0.011; five decades to 1e7, final z=+0.13 (`verify/c06_repunit_chain.py`) |
| C08 | null-mechanism race: (n²+1,n²+3) has no square contamination; class race 1 vs 4 (mod 5) driftless | 1e7: D=−64 (−0.43 noise units), log-mean drift −0.46, lead fraction 0.21 (`verify/c08_null_race.py`) |
| C10 | factorial twins: n=3 unique | exhaustive n≤700; tail 4.5e-3 (`verify/c10_factorial_twins.py`) |

**Family lifts.**
| Slot | Lift | Verification |
|---|---|---|
| C01 | uniform quadratic de Polignac over all even d | 150 shifts d≤300 at 1e6: corr 0.99976, slope 1.0022, max\|z\|=2.28 (`verify/c01_quadratic_depolignac_family.py`) |
| C05 | complete φ(k)=2 twin-base family: k=4 parity-dead (only (2,5)); k=6 ≡ k=3 via Φ₆(x)=Φ₃(x−1); one live instance | both-odd check to 1e6; k=6 counts identical to k=3 as the identity requires (`verify/c05_cyclotomic_twin_family.py`) |

**Derivational upgrades.**
* C16(ii): covariance kernel derived from HL triple constants
  (4 overlap configurations); evaluated over 870 pairs d,d'≤60 at 1e8:
  mean ρ=0.43, predicted spread ≤0.59 before the diagonal deficit;
  observed 0.27 ⇒ diagonal factor ≈0.5, MS-mechanism sign and order
  (`verify/c16b_covariance_kernel.py`).
* C24(ii): family kernel from pair singular series; 1,225 pairs
  (289 locally exclusive): positive and negative correlations cancel,
  mean ρ=−0.003 — cross-member kernel is NULL; observed profile
  variance 0.37 must be diagonal (`verify/c24b_family_kernel.py`).
* C22(ii): θ_disc now defined by the parity-aware Cramér–Bernoulli
  control; stratified experiment q∈[1500,6000]: prime moduli
  θ_disc=0.847, θ_corr=+0.824±0.009 (persists where Leung's smooth-q
  effects are absent); 7-smooth moduli θ_disc=4.32±0.22,
  θ_corr=−2.32±0.22 (`verify/c22b_stratified.py`).
* C11(ii): κ restated via CRT-exact joint densities; factorization
  exact to 1e-15 through p≤19 (joint period 1.16e8); scan extended to
  n=6000, no new hits, z=−0.19 (`verify/c11b_crt_kappa.py`).
* C21: split into provable Lemma (orientation elimination, class
  assignment) + conjecture clauses with a defined logarithmic-mean
  functional; O*-notation replaced by M_x-clauses; zero-oscillation
  caveat (Rubinstein–Sarnak) added.
* C25: explicit log-sampling measure; HL-weighted drift computed in
  presieve-exact form — model mean 66.3 vs empirical 67.8 (ratio
  0.98); internal null lane n≡1(3) predicted and verified (null
  stratum D=31±23 ≈ 0 vs live stratum 88±21 against predicted 96);
  sign-density clause E[Φ(κ)]=0.572 vs observed 0.588
  (`verify/c25b_weighted_drift.py`).
* C04 reframed as "an elementary structural proposition with a
  Bateman–Horn corollary" (reviewer's words); content unchanged.
* C09 kept with the deficit flag: the Grantham–Granville
  rank-of-apparition computation for the corrected c_F is beyond this
  framework's scope and remains the flagged open component.

**Serendipitous findings during v6 verification.**
* The k=4 twin-base branch is inadmissible at p=2 (caught by the
  admissibility engine at singular-series time) — promoted into C05's
  statement.
* The k=6 branch collapses to k=3 (Φ₆(x)=Φ₃(x−1)) — first seen as
  identical counts, then proved; promoted into C05's statement.
* The naive iterated chain p, Φ₃(p), Φ₃(Φ₃(p)) is inadmissible at 3 —
  promoted into C06's statement.
* For n≡1 (mod 3), 3 | n−q² for every prime q>3: the Goldbach lane
  race carries its own null control on n≡10 (mod 12) — promoted into
  C25's statement and verified.

## Fifth external review (paper v6 -> v7)

A constructive novelty assessment ("what does each statement add
beyond its background heuristic?").  Response: `paper/EXTERNAL_REVIEW_5_RESPONSE.md`.
Implemented, with three new derive-first-test-second runs:

* **Canonical random fields (C16(ii), C24(ii), C8).** The review
  correctly noted Cov of deterministic cumulative counts is undefined.
  Both kernels restated on an explicit moving-window probability
  space; C8's "arcsine" clause replaced by a defined occupation-time
  law plus a missing-drift-sources caveat.  Verified:
  `verify/c16c_window_field.py` (x=1e8, H=1e5, 2000 windows, 190
  pairs): empirical vs predicted correlation matrix matches entrywise
  at 0.86; mean off-diag 0.33 vs 0.37; Var/mean 0.94 (diagonal
  deficit visible).
* **Contamination calculus (new C21(v)).** General drift-vector rule
  for any (n, n+d) race mod m; applied blind to cousins d=4:
  (q²−4,q²) dead algebraically; drift predicted in class 4 (mod 5)
  and class 1 (mod 8).  Verified at 1e9
  (`verify/c21c_cousin_races.py`): leadership log-densities 0.99 /
  0.92 on the predicted sides, controls null, endpoint drift inside
  noise as the 1/log x law requires — directional support, so
  labeled.
* **C19(iii) singular-series waiting times.** New clause
  log p(g) = √g + ½log g − ½log S*(g) + O(1); tested on the full
  first-occurrence table to 1e9 (`verify/c19b_waiting_refinement.py`):
  regression coefficient −0.466 vs predicted −0.5 (100 gaps).
* **C22 canonical invariant.** Θ(q) = (1 − E_a U) log q, model-free;
  conjectured → Θ > θ_disc^∞ along prime moduli (measured
  1.671 ± 0.009); θ decomposition demoted to explicit diagnostic.
* **Targeted strengthenings.** C1 explicit uniform error clause +
  open range/constant-distribution questions; C20 interpolation
  clause across H = λ(log x)^α; C23 sharpened to the exact
  Chung–Smirnov LIL constant 2^{−1/2} (upper AND lower); C6
  uniqueness claim made over a specified construction space with the
  pure-Φ₆ sibling acknowledged; C10 novelty label softened to
  "explicit prior statement not found" + new window-rigidity and
  joint-independence clauses; C15 cross-pointer to C25.
* **Declined for scope** (recorded in the paper's open-programme
  note): C2/C3/C14/C17 classification programmes, C18 Gumbel
  centering (Kourbatov's ground), C9 exact entanglement constant,
  C11 full net-convergence theory.

No bibliography changes: twin-citation gate round 5 (30/30 unanimous)
remains in force.

## Sixth external review (paper v7 -> v8)

The most technically exacting round; every checkable correction claim
held up under our verification and is implemented.  Response:
`paper/EXTERNAL_REVIEW_6_RESPONSE.md`.

* **C8 clock error (real).** Arcsine occupation is a natural-clock
  law; under dt/t averaging the Lamperti/OU reduction is ergodic and
  the log-occupation -> 1/2 a.s., fluctuation scale
  2 sqrt(log2/log x).  Clause rewritten; cousin-race leaderships
  requantified against the corrected null (+1.3σ / +1.1σ).
* **C21(iii)** sign-excess scale corrected to loglog x/log x;
  **C21(v)** restricted to balanced races with explicit hypotheses.
* **C16(ii)/C24(ii)** Gaussian regime requires mean count per window
  -> infinity (H/log²x resp. H/log N); Poisson laws in the critical
  regime; kernel reframed as first-order correction to independence.
* **C10:** window rigidity restricted to n>=4 (2!-2=0, 3!-3=3 are
  real counterexamples); **second priority correction** — the exact
  uniqueness conjecture is OEIS A088054 ("3 is the intersection of
  A002981 and A002982"); clause (ii) attributed, claimed content now
  clauses (i)/(iii); joint at-common-index factor derived
  (twin-coupling x sieve-reciprocal cancellation); cross-index
  dependence flagged open.  Finding f:c10 extended: search the
  NEIGHBOURHOOD (derived sequences, comments), not just defining
  sequences.
* **C25** null lane corrected: exceptional family n-q^2=3 recorded
  alongside the q=3 term (numerics were already exact; prose was
  not).
* **C23(iii)** sharpened to CLT + LIL envelope
  sqrt(2 loglog x * loglogloglog x) — the O_ε(V^{1/2+ε}) bound was
  weaker than the model's own prediction.
* **C11:** kappa_S defined over p>=5; factorization is now an EXACT
  RATIONAL IDENTITY (verified in exact arithmetic at every level,
  `verify/c11b_crt_kappa.py`); review-reported OEIS candidates
  29355/34653/57285/99069/1933695 (not independently re-verified,
  so labeled) extend the kappa-model consistency by two decades
  (predicted 2.9 vs 4 in (6e3,1e5]; 5.9 vs 5 to 1.94e6).
* **C19(ii)** labeled explicitly as the dual of the maximal-gap
  limsup; **(iii)** measure specified (uniform over realized gaps in
  dyadic blocks), O(1) -> O_P(1) with conjectured first-passage law.
* **C22(ii)** weakened to dyadic-average form with spread clause;
  the review's occupancy-expansion derivation route (V_q
  inclusion-exclusion, first correction from prime pairs with gap
  divisible by q, weighted by sum_k S(kq)) adopted as the stated
  programme.
* **New: C1(iii) moment law for C(d)** — derived Euler-product mean
  2.7447 / sd 1.6835 vs empirical 2.7434 / 1.6726 over 150 shifts
  (`verify/c01b_family_moments.py`); registered rate clause
  separated from the (1+o(1)) core.
* Declined: restructuring to a 5-6 conjecture paper (brief is 25;
  layering already explicit).

No bibliography changes; gate round 5 (30/30 unanimous) remains in
force.

## Replacement round (paper v8 -> v9): no standalone benchmarks remain

On the operator's instruction ("remove any that are not at least
structurally novel and replace them with genuinely novel conjectures"),
the eleven remaining benchmark slots (C02, C03, C07, C09, C12, C13,
C14, C15, C17, C18, C23) were replaced or upgraded.  Design rule: grow
each replacement from mechanisms this paper already owns (contamination
calculus, derived kernels, entanglement densities, occupancy anomaly,
convergent-BC rigidity, family moment laws) so each new slot makes
fresh predictions.  Every retired benchmark is retained inside its
successor slot as an attributed calibration remark.

**Protocol:** two independent Opus search agents audited all eleven
candidates at neighbourhood depth BEFORE admission; ten new verifiers
ran at production scale.  Verdicts and consequences:

* **One candidate refuted pre-publication** (the audit working as
  designed): the Fibonacci–Lucas twin completeness list dies on OEIS
  A080327's catalogued index 148091 — rebuilt as the convergent-BC
  stress test C09 with no completeness clause and the refutation
  quantified in-statement.
* **One candidate redesigned on theoretical warning**: the naive
  Darling–Erdős race-maximum law contradicts the RS almost-periodicity
  picture (Montgomery/Ng (logloglog)^alpha class) — rebuilt as the
  measured sub-diffusivity law C18 (universal step correlations
  rho1 = -0.037 +- 0.001 across four races; maxima at 2–17% quantiles
  of the simulated iid null; dichotomy registered open).
* **One candidate found classical at its core**: the boundary
  divisibility principle's cubic case is Cunningham 1923 (cuban
  primes) — C13 rebuilt around the (attributed) principle's family
  trichotomy, with two new BH lanes verified (c=4: z=+0.27; c=6:
  z=-0.92 at 1e6).
* **Framework attributions added where audits demanded**: Kowalski
  (C02's limit-law mechanism, new bibitem), Oliveira e Silva–Herzog–
  Pardi (C15's extremal antecedent, new bibitem), Dubner's own mu_4
  kernel (C17), Eisenstein–Lerch + Conrad folklore + the Gras conflict
  (C23), Korevaar–te Riele mean-value-one (C01(iii)/C02(i)).

**Run outcomes (all derive-first, test-second):**
| Slot | Result |
|---|---|
| C02 | derived mean C(a) = 1 EXACTLY (one-line lemma) + sd 0.2762 vs empirical 1.0215 / 0.2481 over 294 shifts; uniformity mean z +0.09, max 2.31 over 57 profiles (`c02b_cubic_family.py`) |
| C03 | 1e9: D=+167 predicted side (T3=+25, noise 616); leadership 0.65 (+0.4 null sd) (`c03b_triplet_race.py`) |
| C07 | 1e9: all four matrix components and 5-7 control within one noise unit; leaderships (0.48,0.56,0.53,0.73) vs null 1/2 +- 0.37 — registered, sharp only at ~1e14 (`c07b_sexy_matrix.py`) |
| C09 | joint {5,7,11,13,17,47} to 1e4, naive tail 1.6e-3 — vs A080327's 148091 (`c09b_fib_lucas_twins.py`) |
| C12 | G(H) exact to H=3000: G(3000)=-20.9, local slope 3.4→3.7 (single-prime slope: 1/2); window Var/E observed 0.815 bracketed by log-form (0.97) and log²-form (0.72) extrapolations (`c12b_pair_ms.py`) |
| C13 | collapse algebraically empty for x³+cx; trichotomy verified c<=12; lanes c=4,6 at 1e6 (`c13b_boundary.py`) |
| C14 | 2500 samples <= 1e8: contaminated strata pooled D=+0.27+-0.33 vs pred +0.30; null strata -0.22+-0.33 (`c14b_stern_lane_race.py`) |
| C15 | E[U]=0.796; Theta_G = 3.12+-0.35 and 3.42+-0.45 in dyadic blocks (`c15b_least_goldbach.py`) |
| C17 | shape log-log corr 0.9993 over two decades; level 0.87→0.81 deficit flagged open (`c17b_twin_member_goldbach.py`) |
| C18 | rho1 in [-0.040,-0.036] on all four races (~50 s.e.); maxima quantiles 0.02–0.17 vs simulated null (`c18b_race_max.py`) |
| C23 | homomorphism exact on all spot-checks; corr +0.0023+-0.0012; chi2 441/399; joint census z=+0.75; simultaneous Wieferich: NONE to 1e7 (`c23b_multibase.py`) |

Bibliography gained Kowalski and OSHP (32 entries) -> twin-citation
gate round 6 triggered and **PASSED: 32/32 PASS from both fresh
verifiers, zero FAIL, zero UNVERIFIED — unanimous on the v9
bibliography.** Both independently confirmed the two new entries
against publisher records (OSHP's page range 2033-2060 resolved
against an erroneous aggregator listing in favour of the
authoritative AMS record; Kowalski's DOI omission noted as a style
choice, entry unambiguous), re-confirmed the Fiori [sic] typo in the
original, and re-verified all 28 carried-over entries.
