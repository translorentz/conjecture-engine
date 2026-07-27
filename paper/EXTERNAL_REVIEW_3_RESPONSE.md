# Response to the third external review (paper v5)

## Accepted and fixed

* **C4 was FALSE as stated (grade X) — accepted in full.** For odd
  composite k = rs, D_k(m) is divisible by D-type factors and is never
  prime (we verified: k = 9, 15, 21, 25, 27, 33 give zero primes to
  m = 2000, with the predicted divisor identity checked). The ladder is
  restated as **prime vs composite**: composite k totally obstructed
  (theorem, now covering every j, not just j = m−1); prime k (incl. 2)
  representable iff D_k(m) prime, D_k irreducible via the
  linear-fractional relation to Φ_k. A Finding records that this is the
  second algebraic-factorization failure caught downstream of
  generation. Verifier updated and re-run (k = 2/3/5 lanes: ratios
  0.9998 / 1.0015 / 0.9983).
* **Attribution inconsistency (C10/C25) — accepted.** The (a)-list
  still carried the *retired* occupants' citations. Fixed, with an
  explicit note crediting the review for the catch.
* **C8 "no prior trace" — withdrawn.** The tuple family has OEIS
  presence (the longer pattern n²+{1,3,7,9,13} recorded since 2000);
  only the singular-series evaluation is claimed as possibly new.
* **C22 vs Leung — accepted.** Added S.-K. Leung, "Moments of primes in
  progressions to a large modulus" (arXiv:2402.07941) to part (i)'s
  attribution and a paragraph stating that whether θ_corr is distinct
  from the singular-series corrections implicit in Leung's discrepancy
  analysis is an open comparison on which part (ii)'s novelty claim
  depends.
* **C24 "jointly Poisson-size residuals" — accepted**: replaced by the
  C16(ii)-style empirical-measure formulation with the covariance
  kernel flagged as required development.
* **C25 formulation — accepted**: the normalization ℓ̄(n) is now
  analytic ((n−6)/∫dt/(log t log(n−t))), the empirical lane mean is
  its estimator; the averaging regime (logarithmic sampling) is stated;
  a derivation-status paragraph flags the weighted-to-unweighted
  transfer as the open step.
* **C10 — accepted**: the statement now separates the defensible core
  (finiteness) from the Goldilocks-maximal exact list.

## Strengthened in response

* **C21 gains clause (iv), the mod-8 companion**: q² ≡ 1 (mod 8)
  always, so the *entire* deterministic term falls on class 7 (mod 8) —
  twice the mod-5 term, undiluted. New verifier (c21b) at 10⁹:
  D₇ = +212 vs predicted +254 (noise ~1068), log-density of D₇ > 0 is
  0.775, and all three {1,3,5} controls within one noise unit of zero.
  The mod-5/mod-8 pair makes the mechanism a family test.

## Noted, not actioned here

* The recommended four-way publication split (races paper, least-primes
  paper, benchmark companion, elementary note) is an editorial decision
  above this revision's scope; the paper's taxonomy already separates
  benchmark from research content along the lines the review draws.
* Full weighted-explicit-formula derivations for C21/C25 remain open
  and are flagged as such in the text.
