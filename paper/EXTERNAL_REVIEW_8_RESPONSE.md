# Response to the eighth external review (paper v10 -> v11)

Protocol unchanged: every mathematical error claim was re-derived or
recomputed before being conceded; everything that survived checking
was implemented.  One of the review's own quantitative claims (the
C22 baseline scale) fails checking, and we document the correct
magnitude below.  No bibliography entries were added or changed —
twin-citation gate round 6 (32/32 unanimous) remains in force.

## The review's "highest-priority revisions" — disposition

1. **C19 fluctuation scale: CONFIRMED and fixed.**  The slope of the
   log-intensity log Lambda_g(y) = log S + y - g/y - 2 log y at the
   centering point y0 ~ sqrt(g) is 1 + g/y0^2 - 2/y0 = 2 + o(1) —
   both the y-term and the g/y-term contribute — so the first-passage
   error is E_g = (1/2) log W, the reversed Gumbel at scale 1/2:
   P[E_g <= t] -> 1 - exp(-e^{2(t - mu)}).  The paper now prints the
   derivation in-statement (including the point that e^{-g/y} *is*
   the no-intervening-prime probability).  The centering (the
   -1/2 log S* coefficient) and the regression test are unaffected.
   Gumbel-framework attribution to Kourbatov–Wolf tightened at the
   same spot.

2. **C23(iii) block-sampled CLT: CONFIRMED vacuous and replaced.**
   On [X, X^A] the expected number of new Wieferich events is
   log A + o(1) = O(1), so the block-sampled statistic freezes at
   the historical value.  Replaced by the almost-sure-CLT weighting:
   u = loglog x uniform on [1, loglog X] — a window on which the
   variance itself sweeps a diverging interval — with
   (W(x) - u)/sqrt(u) => N(0,1).  The vacuity argument is printed in
   the paper as the reason for the form.

3. **C13 positivity hypothesis: CONFIRMED and added** (positive
   leading coefficient; with the |.|-reading noted as the
   sign-free alternative).  Likewise C4's divisor wording now
   requires r > 1.

4. **Quantitative uniformity**: C1(ii) already carries the explicit
   eta_B clause; the remaining parameter dependences (discriminant,
   coefficient height, exceptional loci) are acknowledged as the
   analytic content of the uniform clauses rather than silently
   assumed.

5. **Random-model vs arithmetic separation**: C8(ii) is now stated
   as conditional on an explicit invariance principle — the
   invariance principle IS the arithmetic content; the occupation
   law is labeled its probabilistic consequence.  C10(iii)'s
   Gaussian limit now carries the explicit dependency-graph
   summability hypothesis sum|Cov| = o(log N) instead of importing
   independence.  C18(ii) closes the Green–Kubo gap: the decay law
   is hypothesized uniformly in k <= K(x) with summable tail —
   fixed-lag decay alone does not control the variance sum, as the
   review says.

6. **Derive rather than fit**: the C22 injective baseline is now
   derived (below); the survival-expansion route for Theta_G (C15)
   and the occupancy expansion for Theta (C22) remain the registered
   programmes, explicitly labeled as underived.

7. **Consolidation of the contamination examples**: declined as
   restructuring (see below), but the substance is present — C21(v)
   is the general operator with census/transfer layers, the
   operating-scale sentence demanded by the review (drift smaller
   than the sd by 1/log x; occupation biases under log aggregation,
   never a fixed standardized mean) is now in the statement, and the
   r >= 3 negligibility step (O(x^{1/3+eps}) vs sqrt(x)) is
   separated as the transfer's one easy layer.

## The C22 no-collision baseline: review partially right, its scale wrong

The review demanded subtraction of the deterministic injective phase
(primes p < q occupy distinct classes mod q) and argued it may
explain the deficit "substantially," since the affected-class
fraction pi(q)/phi ~ 1/log q matches the deficit scale.  The demand
is right; the magnitude claim is not.  Closed form (index time,
Li(p_i) ~ i): forcing the first pi(q) arrivals collision-free and
the rest exchangeable gives E[U] = 1 - pi(q)^2/(2 phi^2) + O(pi/phi^2),
hence

    Theta_inj(q) = (1 + o(1)) / (2 log q)  ~  0.07–0.09  on [1500, 6000],

verified by Monte Carlo (new verifier `c22c_injective_baseline.py`;
exchangeable control at 1.000).  The review conflated the
affected-class fraction (1/log q) with the deficit, which is that
fraction times the collision probability the exchangeable model
suffers in the phase (pi/2phi), i.e. 1/(2 log^2 q) in E[U].  The
baseline is real, is now subtracted in the paper
(theta_corr - Theta_inj ~ 0.74 remains the unexplained anomaly), and
is identified as the y < q head of the registered pair-correlation
expansion — the first term of the stated programme, not a rival
explanation.

## Other implemented points

* C1(iii)/C2(i): the mean/moment identities now cite the uniform
  integrability they need (convergent variance sum -> L^2-bounded
  mean-one martingale -> the limit law's mean is exactly 1); the
  review is right that a.s. convergence alone is insufficient, and
  the needed ingredient was on hand but unstated.
* C16: degenerate offset relations (h = 0, d, -d'; d' - d = +-h;
  the review's d' = 2d) are assigned to kernels explicitly — K4 is
  defined over genuinely four-element sets; collapsed configurations
  belong to the triple term's census.  No double counting.
* C11(ii): split into (ii-a) convergence along the canonical
  exhaustion, (ii-b) factorization/entanglement of the limit,
  (ii-c) local density -> global count, asserted separately as the
  review demanded.
* C14: the honest-depth caveat is added — an averaged asymptotic for
  the contaminating count q^2 + 2k^2 = n is a hard
  restricted-variable norm-form problem; D_sys is computed exactly
  per sample, so the verification tests the transfer against the
  true census, never against an unproved asymptotic.
* C17: two exact orientation identities derived and printed
  (t -> n - t forces S4^(lu) = S4^(ul), with (ll) and (uu)
  self-dual; t -> t + 2 forces S4^(uu)(n) = S4^(ll)(n - 4)), so the
  four-orientation profile is really two-dimensional; the averaged
  identity hunt is the slot's registered programme.
* C9's caveat that rank-pool disjointness removes shared-prime
  correlation but not order-structure dependence was already present
  (round 7); the review's point is covered.
* C12's divergence caveat (log H with a large constant cannot be
  excluded at H <= 3000) was already present (round 7); the
  degenerate-separation removals the review asks about are already
  in R(h)'s definition.
* C6's composition-language programme (regular-language question)
  was already registered; the review's elevation of it is noted.

## Declined

* **Reduction to 6–8 principal conjectures, appendixing
  C1/C2/C4–C6/C9/C10/C13/C17, and the four-part restructuring.**
  Same scope decision as rounds 7's split recommendation: the
  operating brief is a single suite of 25 substantive conjectures
  (its hard floor), and the honesty the recommendation seeks is
  carried by the in-statement attribution labels, the
  operator-instance framing of the contamination family, and the
  audit record — not by reducing the count.
* **C23 as a separate paper**: same scope decision.

## Net effect

Two probabilistic scaling errors corrected (C19 scale 1/2, C23(iii)
sampling window), two missing hypotheses added (C13 positivity, C4
r > 1), one deterministic baseline derived, quantified, and
subtracted (C22, with the review's own scale claim corrected), and
nine statements hardened from model-import to explicit-hypothesis
form.  No conjecture count change; no bibliography change; v11
compiles clean in full and blind versions (25 conjectures each, zero
provenance markers).
