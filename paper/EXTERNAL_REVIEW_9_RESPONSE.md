# Response to the ninth external review (paper v11 -> v12)

Protocol unchanged: every mathematical claim was re-derived before
being conceded.  This review's central criticism is correct and
produced the largest single revision since the benchmark replacement
round.  No bibliography changes — twin-citation gate round 6 (32/32
unanimous) remains in force.

## The central defect: race normalization (C3, C7, C8, C21) — CONFIRMED

The review is right that M_x((D - T)/sqrt(pi)) -> 0 is vacuous for
the drift coefficient: T/sqrt(pi) ~ 1/log t has logarithmic mean
~ loglog x / log x -> 0, so the condition is invariant under
T -> cT for any fixed c and never expressed "exactly the removed
mass."  We verified this and went one step further than the review:
its own suggested replacements (M_x(D)/M_x(T) -> 1, or the smoothed
regression form) are ALSO not consistent statistics under a pure
random-walk noise model — the log-averaged noise at drift scale has
variance growing like log x, so no trajectory functional identifies
the coefficient unless the race has Rubinstein–Sarnak-type
almost-periodic structure.  That observation dictated the repair:

* All drift clauses are restated at the DRIFT-scale normalization:
  M_x(D(t) log^2 t / sqrt t) -> c_T, where c_T is an explicit
  Bateman–Horn constant — C(x, x^2-2)/2 for the twin mod-5 race,
  2c_T for mod 8 (the factor 2 is now falsifiable), the (q, q^2+4)
  constant for cousins, c_A/c_B for the sexy matrix, the triple
  constant at log^3-normalization for C3, and 0 for C8 and all
  symmetric differences (now genuinely distinct claims from the
  drift clauses).
* Convergence of the logarithmic mean at this normalization is
  itself declared part of each conjecture: it would FAIL under a
  random-walk model, so it encodes exactly the almost-periodicity
  that the zero-oscillation hypothesis names.  The two conjectural
  layers (structure + value) are now separated in-statement.
* C8(i) is restated at the same scale, making it a true negative
  control at the contamination scale (the review correctly noted
  the old form was too weak to be one); its invariance principle
  now defines the event-indexed process explicitly.
* The Notation section carries the general rule and the reason.

## Confirmed formula errors — fixed

* **C12 (missing Bernoulli diagonal).**  Verified: with
  p = S(2)/log^2 x, Var X = Hp(1-p) + 2p^2 H G(H), so
  Var/E = 1 - p + 2pG — the -S(2)/log^2 x term is exactly the order
  of the stated error and was missing.  Display corrected to
  1 + S(2)(2G(H) - 1)/log^2 x.  As a consistency check we
  re-derived the single-prime case and confirmed that the analogous
  -p merges into Montgomery–Soundararajan's gamma + log 2pi - 1
  (which is why C20 needed no change).  `c12b` patched and rerun:
  predicted window Var/E moves 0.757 -> 0.753; every quoted bracket
  is unchanged at two decimals.  The divergence clause already
  carried the round-7 caveat the review asks for.
* **C24 (off-index covariance order).**  Verified: the joint event
  is two SINGLE prime values at distinct indices, probability
  ~ 1/(4 log^2 N); the extra log^{-2} N factor was copied from
  C16's pair-of-pairs setting where log^{-4} is correct.  Display
  corrected — and the inference reversed: at the correct order the
  off-index sum generically DOMINATES the same-index term, so the
  observed same-index cancellation no longer supports asymptotic
  independence of family members or a diagonal-only deficit.  Both
  conclusions are downgraded to open questions in the prose, as the
  review demanded.
* **C23(iii) (sampling law, second failure).**  Verified via
  Brownian scaling: with u = Ls, B(Ls)/sqrt(Ls) =d B~(s)/sqrt(s),
  so the uniform-u empirical distribution converges to the random
  occupation functional int_0^1 1{B(s)/sqrt(s) <= z} ds, not Phi —
  round 8's uniform-u fix was itself wrong.  Replaced by the
  classical ASCLT weighting du/u (log u = logloglog x uniform), for
  which the model predicts a.s. convergence to Phi.  Both failed
  drafts and their failure modes are recorded in-statement, since
  the two errors are instructive in opposite directions (window too
  short; weighting too flat).  The p | a exclusion was added to the
  definition.

## Other implemented repairs

* **C10(iii)**: probability model declared (Caldwell–Gallot marginal
  hazards, unspecified dependence); the Gaussian limit now carries
  BOTH the covariance bound and the higher-cumulant condition
  kappa_r = o((log N)^{r/2}), r >= 3 — the review is right that
  pairwise control alone is not a CLT hypothesis.
* **C14(ii)**: fully rewritten to the C25 ensemble template the
  review holds up as the model: explicit log-sampling measure per
  residue class, explicit per-class sign of D, analytic definition
  of lambda(n) with the empirical estimator labeled as such, and the
  coefficient-identifying law E_X[D - D_sys] = o(E_X[D_sys]) with a
  null-class companion.  C14 is now a precise conjecture.
* **C18**: the head-sum gap is closed — summability hypotheses
  sum c_k < infinity, sum |d_k| < infinity added (uniform per-lag
  decay does not control the growing head sum, as the review
  showed); the event-index process is defined; the sigma^2 formula
  is now a consequence of stated hypotheses.
* **C3**: the q = 3 exceptional configuration (3,5,9) is recorded
  (q^2 - 4 = 5 is prime there); one bounded term, no asymptotic
  effect.
* **C9(iii)**: the 148091 contradiction is now conditional on the
  Fibonacci PRP being prime, and the "order of magnitude" language
  is replaced by the three competing explanations one event cannot
  separate.
* **C15**: the p | n exclusion is explained in-statement (it removes
  the p | n-p obstruction and the diagonal n = 2p).
* **C16**: dominance range restated as the explicit class
  H = lambda (log x)^alpha, alpha >= 1.
* **C17**: the n-uniformity of the required 4-form HL hypothesis is
  stated; the dual twin-role of 5 is addressed.
* **C11**: clause (ii-b) is relabeled an open question and expressly
  not counted among the paper's conjectural assertions.
* **C19(iii)**: selection caveat added (sampling realized gaps
  conditions on realization; the clause conjectures this does not
  shift the law).

## Points already covered in earlier rounds

C1/C2's L^2/uniform-integrability layer (round 8; the mean-one
lemma is labeled a lemma and the martingale ingredients are stated),
C4's r > 1 (round 8), C13's positivity (round 8), C22's injective
baseline (round 8, which this review independently re-derives and
confirms as ~1/log q — the two assessments now agree), C12's
divergence caveat (round 7), C6's construction-space-limited
uniqueness and language programme (rounds 5-7).

## Declined

Consolidation to 8-12 principal conjectures with the remainder
reclassified — the same scope decision as the seventh and eighth
reviews' versions of this recommendation.  The operating brief fixes
25 slots; the honesty the recommendation seeks is provided by the
attribution labels, the calibration/benchmark layering, and — after
this round — formal statements that actually express their prose
claims, which was the legitimate core of the criticism.

## Net effect

The mechanism family's five drift conjectures now identify their
coefficients (they previously did not — the review's scorecard
"soundness 2" for C3/C7/C8/C21 was earned); two displayed formulas
are corrected (C12, C24) with one downstream inference reversed
(C24); one probability law is corrected for the second time, now at
the classical ASCLT weighting (C23(iii)); and seven statements
acquired the hypotheses or definitions they were missing.  25 slots,
no bibliography change, both PDFs compile clean (25 conjectures
each, blind copy free of provenance markers).
