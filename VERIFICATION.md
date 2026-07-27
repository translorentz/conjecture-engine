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
| C02 | (b) | A067200/A144953 bare sequences; constant unpublished |
| C03 | (a) | A174734; for p ≥ 5 this is Chernick's Carmichael triple (6m+1)(12m+1)(18m+1): Dubner, J. Integer Seq. 5 (2002) quantifies it |
| C04 | (b) | A078946 (consecutive-primes variant) bare; constant unpublished |
| C05 | (b), family analysis new | no OEIS entry, no literature trace found for the pair; the complete φ(k)=2 family analysis (k=4 parity-dead, Φ₆(x)=Φ₃(x−1) collapse) added in v6, no prior trace |
| C06 | replaced in v6 | alternating chain p, Φ₃(p), Φ₆(Φ₃(p)): no OEIS entry, no literature trace (searched Cunningham-chain and repunit-prime literature at abstract depth); retained sub-chain: A053182 + **A188596 is literally the sub-chain constant** (1.5217315...) |
| C07 | (b) | A062326 bare sequence; constant 3.3832 unpublished |
| C08 | replaced in v6 | null-mechanism race over (n²+1, n²+3) mod 5: no prior statement found; retired triple n²+{1,3,7}: family in OEIS since 2000 (3rd review), singular series plausibly new |
| C09 | (a) | Grantham–Granville arXiv:2307.07894 (Lucas-sequence e^γ log-count heuristics); Wagstaff's Mersenne analogue |
| C10 | replaced in v6 | **primorial twins: PRIORITY FAILURE — Lillie arXiv:2110.04302 (2021) states both the O(n⁻²) joint law and the three-instance prediction; our snippet-depth search missed it (4th review caught it)**. Factorial twins (n!±1, unique n=3): searched at abstract depth incl. Lillie and the factorial-prime literature, no prior statement found |
| C11 | (b), upgraded v6 | A064539 has the sequence and the n ≡ 3 (mod 6) note; the κ-quantified count unstated; v6 restates κ via CRT-exact joint densities (entanglement-aware) — factorization verified exact through p ≤ 19 |
| C12 | (a) | Caldwell–Gallot 2002, verbatim for n!±1 |
| C13 | (a)-core | finiteness for non-cubes is Hardy–Littlewood (Partitio Numerorum III, E_3(X) = O(1)); our census + decay quantification unstated; **as first stated, false — see above** |
| C14 | (a) | OEIS A060003 verbatim (k ≥ 1, ten terms); Stern primes A042978 |
| C15 | (a) | Kimball Martin, Exp. Math. 31 (2022), arXiv:1806.00946: the (3,3) mod-4 lane, incl. exceptionless threshold |
| C16 | (a)-core, kernel new | uniform HL-B is standard (Goldston–Ledoan); Brent 1975, Korevaar–te Riele 2010 did profile verifications; the derived triple-constant covariance kernel of (ii) (v6) appears unstated |
| C17 | (a) | **Dubner's conjecture (2000)**; A007534, verified by Dubner to ~2·10^10 |
| C18 | (a) | Kourbatov arXiv:1309.4053 etc.: same constant 1/(2C2) ≈ 0.76, richer corrections, larger tables |
| C19 | (b) | Shanks/Wolf/Nicely endorse limit slope 1; our Granville-corrected 0.9436 appears unstated — a genuinely different constant on the books |
| C20 | (b) | constant γ+log 2π−1 is Montgomery–Soundararajan (mesoscopic); the microscopic finite-x Var/mean law + test appears unstated |
| C21 | (b) | no prior twin-race-mod-5 statement or q²−2 mechanism found (closest: arXiv:2111.09053; Brent's "twins more random") |
| C22 | (b), stratified v6 | Exp(1) limit is Haddad–Leung–Sabuncu arXiv:2408.11781; Wagstaff 1979/Fiori 2404.02329 for the max; the 1/log q deficit law and ordering anomaly appear unstated; v6 defines θ_disc by a named control and differentiates θ_corr from Leung's smooth-q effects by the prime/smooth stratified experiment |
| C23 | (a) | Crandall–Dilcher–Pomerance 1997; Dorais–Klyve 2011 (incl. tail-uniformity census) |
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

The gated bibliography (27 entries, 20 with DOIs verified to resolve to
the exact works, 5 verified to legitimately lack DOIs, plus 2 arXiv
companion pointers) is identical in `paper/conjectures.tex` and the
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
