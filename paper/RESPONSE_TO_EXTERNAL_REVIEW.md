# Response to the second (external) review

The review (committed verbatim as `paper/EXTERNAL_REVIEW_2.md`) was
accepted in nearly all substantive points. Changes in paper v3:

## Structural
* **Conservative novelty taxonomy (accepted).** New introduction
  subsection classifies the 25 statements into a *benchmark suite*
  (C1–C8, C10, C12–C18, C23–C25) and *research conjectures* (C9, C11,
  C19–C22); the abstract was rewritten to match, and the attribution
  section now distinguishes bibliographic novelty (C2, C4, C5, C7, C8 —
  "new arguments of a classical special function") from conceptual
  novelty (C11, C19, C20, C21, C22(ii)). We kept the original ordering
  and numbering rather than physically splitting the paper, to preserve
  the stable C-numbering used throughout the repository's audit trail;
  the classification carries the reviewer's intent.

## Logical errors (all accepted and fixed)
* **C21 clause (iii)** asserted a limiting sign density strictly in
  (1/2, 1) while also asserting drift/noise → 0 — inconsistent, as the
  reviewer showed. Corrected: if the logarithmic sign density exists it
  equals 1/2, with a positive finite-x excess of order 1/log x. The
  correction is noted in the text. Also added: precise symmetry clause
  for classes 2/4, the weighted→unweighted caveat, the q³-order remark,
  and the open covariance modeling.
* **C23** — the "hence" deriving the Wieferich count from global
  equidistribution was invalid (shrinking-target vs global KS), and the
  O(1) fluctuation violated our own calibration principle. Clauses are
  now logically independent; clause (ii) is stated uniformly down to
  K=1; clause (iii) now reads log log x + O((log log x)^{1/2+ε}); the
  "doubly exponential location" forecast is retracted as uncalibrated.
* **C19** — the envelope inversion does not give a limit; restated as a
  liminf law along envelope-realized gap sizes, with the three
  confounded phenomena listed and the limit question left open.
* **C24** — uniformity over a fixed finite set is vacuous; restated
  uniformly over odd A ≤ (log N)^B, with A ≤ 199 demoted to benchmark
  computation.

## Formulation gaps (accepted)
* **C9**: exact constant withdrawn; conjecture now for c_F from the
  Grantham–Granville recurrence model, with e^γ/log φ labeled the
  first-order screening value and the observed deficit noted.
* **C11**: split into robust clause (count ≍ log N) and candidate law;
  convergence of the κ-product in increasing-prime order is now part of
  the conjecture; independence caveats via ord_p(2) stated; the 8-hit
  sample explicitly disclaimed as evidence for the constant.
* **C16**: residual clause restated as weak convergence of the
  empirical measure of z_d to a centered Gaussian with variance σ² ≤ 1
  governed by overlapping-pair covariance (measured σ ≈ 0.5).
* **C18**: split into robust order claim and candidate limsup constant;
  "to first order" removed from after an exact limsup equality.
* **C20**: Gallagher stated conditionally on Hardy–Littlewood; sampling
  measure defined (t uniform on [x,(1+c)x]); error term weakened to
  o(1/log x) with the obstacles to O(1/log²x) enumerated.
* **C22**: Gumbel now conditional on an explicit joint-independence
  hypothesis; θ decomposed into θ_disc + θ_corr per the reviewer's
  suggestion; averaging convention fixed; functional-form
  indistinguishability at q ≤ 6000 stated.
* **C25**: constant defined as c₃ from the LOS formula at q=3; the
  fitted range removed from conjectural content.
* **C13**: numerical census and largest-exception moved out of the
  formal statement (kept as verification data); "super-geometric"
  wording dropped from the statement.
* **C15**: ordered-count normalization and the origin of the 1/2 factor
  made explicit (verified consistent numerically).
* **C10/C12**: structural-dependence caveat added; labeled classical
  benchmarks.
* **C2 / notation**: canonical increasing-prime ordering of
  conditionally convergent singular series adopted globally, with the
  wobble described as an error bar for that ordering, not a convergence
  proof.
* **C7**: "stand or fall together" softened to the actual
  one-directional partial dependence.
* **C8**: "natural stopping point" claim withdrawn.

## An error the review exposed indirectly
* **C5**: the claim that +7 is "the nearest shift that survives" was
  false — we verified computationally that the pair {n²+n+1, n²+n+5} is
  admissible (C = 3.497). The text now records the correction and
  presents c = 7 as a non-canonical choice.

## Not changed
* The 25 conjecture statements' count and numbering (baseline
  requirement of the project); the physical two-part split is realized
  as a classification rather than a reordering.
* The bibliography — no references added or removed, so the twin-agent
  citation-gate certification (27/27 unanimous) remains valid for v3.
