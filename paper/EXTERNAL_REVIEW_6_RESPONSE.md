# Response to the sixth external review (paper v7 → v8)

The sixth review is the most technically exacting of the series. We
verified each of its correction claims independently before acting;
every one we could check held up, and all are now implemented. Its
restructuring recommendation (a 5–6 conjecture paper) is declined, as
with earlier reviews — the brief is 25 substantive conjectures with an
explicit benchmark/research layering, which the paper states — but its
mathematical content is accepted nearly in full.

## Corrections verified and implemented

* **C8 occupation clock (conceded, and the review's argument is
  correct).** Under logarithmic averaging the Lamperti reduction of
  the race walk is a stationary ergodic Ornstein–Uhlenbeck process, so
  the log-occupation of leadership converges a.s. to ½ — not to an
  arcsine-distributed limit, which survives only in the natural event
  clock. Clause (ii) rewritten with the ergodic limit and its Gaussian
  fluctuation scale 2√(log 2 / log x) (from the OU sign-covariance
  integral 4 log 2). This makes the clause *more* falsifiable, and the
  correction propagates: the cousin-race leaderships of C21(v) are now
  quantified against the corrected null (+1.3σ and +1.1σ on the
  predicted sides).
* **C21(iii) sign-excess scale (conceded).** The log-average of the
  pointwise drift-to-noise c/log t is ~ log log x / log x, not
  1/log x. Fixed, with the review credited.
* **C21(v) scope (conceded).** The calculus is now stated for
  *balanced* races (equal prime–prime singular series across the
  compared classes; no other mechanism at the √x scale under the
  zero-oscillation hypothesis), with unbalanced/multi-orientation
  races explicitly outside it.
* **C16(ii)/C24(ii) Gaussian range and kernel status (conceded).**
  Gaussian behavior requires the mean count per window to diverge
  (H/log²x → ∞, resp. H/log N → ∞); the critical regimes get
  correlated-Poisson laws; and since ρ ≍ 1/log x → 0, the kernel is
  presented as the first-order correction to independence — a
  quantitative finite-x law (which is what the window experiment
  tests) rather than a nondegenerate limiting kernel.
* **C10 window rigidity (conceded).** 2!−2 = 0 and 3!−3 = 3 are
  genuine counterexamples to the unrestricted statement; clause (i)
  now reads n ≥ 4 with the two anomalies recorded.
* **C10 priority (conceded, second correction on this slot).** The
  review's assertion led us to OEIS A088054, whose comment states
  exactly that 3 is conjecturally the unique common index of A002981
  and A002982. Clause (ii) is now attributed there; Finding f:c10
  records the compounded lesson (search the *neighbourhood* of a
  statement — derived sequences and comments — not only its defining
  sequences). The joint at-a-common-index factor is now derived
  (twin coupling and reciprocal sieve factors cancel), and the
  cross-index dependence is flagged open in clause (iii).
* **C25 null lane (conceded).** The exceptional family n − q² = 3
  (n − 3 a prime square) survives alongside the q = 3 term; the
  "single term" phrasing is corrected. (The numerical model was
  already exact here — its presieve handled v = p cases with
  probability 1 — only the prose overclaimed.)
* **C23(iii) (conceded).** O_ε(V^{1/2+ε}) was weaker than the model's
  exact prediction; replaced by the CLT plus the LIL envelope
  √(2 log log x · log log log log x) — the calibration principle cuts
  both ways.
* **C11 (all three points conceded).** κ_S now defined over primes
  p ≥ 5 (2 and 3 exact in the lane; ord₂2 undefined); "machine
  precision" replaced by an exact-arithmetic result — the joint
  survivor fraction equals the product of per-prime fractions as an
  exact rational identity at every computed level (re-verified with
  exact fractions); and the review's reported OEIS candidate indices
  (29355, 34653, 57285, 99069, 1933695 — which we could not
  independently re-verify and label as reported) are incorporated as
  a two-decade consistency extension: the κ-model predicts 2.9 hits
  in (6·10³, 10⁵] vs 4 reported, 5.9 vs 5 to 1.94·10⁶.
* **C19 (partly conceded).** Clause (ii) is now labeled explicitly as
  the dual of the maximal-gap limsup (registered, not claimed as
  independent); clause (iii)'s sampling measure is specified (uniform
  over realized gaps in dyadic ranges) and O(1) corrected to O_P(1)
  with a conjectured first-passage law.
* **C22 (adopted).** The pointwise limit is weakened to the
  dyadic-average form with a spread clause, and the review's occupancy
  expansion (V_q inclusion–exclusion; first correction from prime
  pairs with gap divisible by q, weighted by Σ_k 𝔖(kq)) is adopted as
  the slot's stated derivation programme.

## Additions prompted by the review

* **C1(iii), a derived family statistic.** The moments of C(d) over
  even d are exact Euler products (the local factors are independent
  in d by CRT). Computed and tested: derived mean 2.7447 and sd
  1.6835 against empirical 2.7434 and 1.6726 over the 150 constants
  d ≤ 300 (`verify/c01b_family_moments.py`). The registered rate
  clause (ii) is separated from the (1+o(1)) core, per the review's
  objection to unspecified exponents.

## Declined

* Restructuring to 5–6 core conjectures with appendices: the layering
  the review wants is present (benchmarks labeled, research group
  identified, core named); the 25-statement format is the brief.
* Removing C12/C14/C17 etc.: retained as attributed benchmarks.

## Gate status

No bibliography entries added (OEIS references are inline A-numbers);
the round-5 unanimous 30/30 pass remains in force.
