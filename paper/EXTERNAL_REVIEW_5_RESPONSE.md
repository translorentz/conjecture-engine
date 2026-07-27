# Response to the fifth external review (paper v6 → v7)

The fifth review is a constructive novelty assessment: rather than
grading, it asks of each statement "what does this add beyond the
surrounding general heuristic?" and proposes concrete strengthenings.
We implemented its highest-value suggestions, declined others for
scope, and record both here.

## Accepted and implemented

**Cluster D — canonical random fields (the review's sharpest formal
point).** Correct: covariances of the deterministic cumulative counts
π_d(x) are undefined. C16(ii) and C24(ii) are now stated on an
explicit probability space (t uniform on [x,2x], moving window of
length H), with the kernel scaled per unit length. The fix was then
*tested*: a 2000-window experiment at x=10⁸, H=10⁵, all even d≤40,
matches the predicted correlation matrix entrywise at 0.86 (mean
off-diagonal 0.33 observed vs 0.37 predicted, the deficit carrying the
sign of the omitted diagonal corrections, which are separately visible
as Var/mean ≈ 0.94). C8's "arcsine fashion" is likewise replaced by a
defined normalized process and an occupation-time law, plus the
review's caution that absence of one drift source does not prove
driftlessness (the null is conjectured under the same zero-oscillation
hypothesis as C21, with the algebra supplying the *contrast*).

**Cluster A — contamination calculus.** The review's structural
question ("what general principle do the mod-5/mod-8 races
instantiate?") is answered by a new clause C21(v): a general rule
computing the drift vector of any (n, n+d) race mod m from the
surviving prime-square orientations. The calculus was then made to
*pay rent*: applied to the cousin pattern d=4 it produces two fresh
predictions with no free choices — orientation (q²−4, q²) dead
algebraically; contamination entirely in class 4 (mod 5) and class 1
(mod 8) — derived first, tested second at 10⁹ (drift/noise ≈ 0.09 as
the 1/log x law forces; leadership log-densities 0.99 and 0.92 on the
predicted sides; controls null; reported as directional support, not
sharp confirmation). The family now has five projections of one
mechanism plus two algebraic nulls.

**C19.** Implemented the review's singular-series observation as a new
verified clause (iii): log p(g) = √g + ½log g − ½log 𝔖*(g) + O(1).
Tested on the full first-occurrence table to 10⁹: regression
coefficient −0.466 against the predicted −½ over 100 gaps.

**C22.** Conceded that θ_disc + θ_corr is benchmark-dependent. Clause
(ii) is now stated through the canonical, model-free invariant
Θ(q) = (1 − E_a[U])·log q with the conjecture Θ(q) → Θ > θ_disc^∞
along prime moduli (measured Θ = 1.671 ± 0.009); the decomposition is
retained explicitly as a diagnostic.

**C1.** Added the explicit uniform error clause
sup_d |π_d/C(d)I_d − 1| ≪ (log N)^{−η_B} and recorded the two open
questions the review suggests (maximal uniformity range / transition
scale; distribution of the constants C(d)).

**C20.** Added the interpolation clause: one formula with log H valid
uniformly for H = λ(log x)^α, connecting Gallagher's boundary to the
mesoscopic Montgomery–Soundararajan regime.

**C23.** Sharpened clause (i) from a big-O to the exact Chung–Smirnov
LIL constant (limsup √π D_KS/√(log log π) = 2^{−1/2}), with the
matching lower bound now part of the claim, per the review.

**C10.** Softened the novelty label to "explicit prior statement not
found" (the review asserts a prior record without citation; the
single-sided lists are classical and the n=3 coincidence is visible in
them). Added content where the review suggested it: a window-rigidity
clause (for 2 ≤ |a| ≤ n, n!+a is composite, so ±1 is the *only*
bounded-offset constellation at n! — every admissible offset set is a
subset of {−1,+1}), and a joint-independence clause with the
deterministic-screening justification (F₊ − F₋ normalized by
√(2e^γ log N) asymptotically normal; data: 14 vs 16 at N=700).

**C6.** The uniqueness claim is now made over a specified construction
space (extensions of the repunit sub-chain by words in {Φ₃, Φ₆}), the
sibling pure-Φ₆ chain is acknowledged, and the classification of
admissible cyclotomic words is recorded as an open programme.

**C15.** Added the pointer that the lane *comparison* the review asks
for is exactly C25, driven by the calculus.

## Declined, with reasons

* Rebuilding C2, C3, C14, C17 into large classification programmes
  (n³+a families, Chernick optimization, Stern explanations,
  Waring–Goldbach for tuple members): recorded as open directions in
  the attribution section, but the brief is 25 verified, honest
  statements — we do not trade attributed benchmarks for unverified
  programme sketches. The benchmarks' role (calibration) is stated.
* C18 Gumbel centering/scaling: Kourbatov's framework already occupies
  much of that ground; flagged in the open-programme note instead of
  claiming it.
* C9 exact entanglement constant for Fibonacci: remains out of scope
  (as stated in the paper); the deficit flag stands.
* C11 full compatibility/convergence theory of the D_S net: the
  CRT-exact computations (machine-precision factorization through
  p ≤ 19) are in; the general dependency-component Euler product is
  noted as the natural continuation, not claimed.

## Gate status

No bibliography entries were added or changed in this revision; the
round-5 unanimous 30/30 pass remains in force.
