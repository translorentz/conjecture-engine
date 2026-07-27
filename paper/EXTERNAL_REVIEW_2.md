# External review of conjectures_blind.pdf (second review)

*Received from the operator; committed with key content preserved. The
authors' actions are documented in `RESPONSE_TO_EXTERNAL_REVIEW.md`.*

The paper is unusually self-aware about the difference between conjecture generation, numerical verification, and proof. Its central methodology—local congruence corrections, singular series, Bateman–Horn, and Borel–Cantelli—is mathematically sound as a heuristic framework. The paper also correctly emphasizes that agreement over a large numerical range is much weaker evidence than agreement with a derived constant and the expected fluctuation scale.

Nevertheless, the 25 statements are not remotely equal in mathematical significance:

* About half are standard consequences or special cases of Bateman–Horn, Hardy–Littlewood, or familiar random-prime heuristics.
* Several are useful numerical formulations but have modest conceptual novelty.
* Four or five contain genuinely interesting new phenomena.
* Some of the most ambitious statistical conclusions are stronger than the stated heuristic derivations justify.
* Conjectures 19, 20, 21 and 23 require substantial reformulation before they should be presented as polished mathematical conjectures.

Key per-conjecture assessments:

- C1–C8: competent Bateman–Horn catalogue; low conceptual novelty. C5's "nearest shift" claim needs precise qualification; C8's "natural stopping point" is not mathematically compelling; C7's "stand or fall together" with C21 is too strong. Conditional convergence of singular-series products needs a canonical ordering or regularization, not just a "truncation wobble".
- C9: e^γ/log φ is a first-order screening approximation; the conjecture should use a constant c_F derived from the Grantham–Granville recurrence-sequence model, not the displayed exact constant.
- C10/C12: classical Caldwell–Gallot territory; structured-sequence dependence makes exact constants less secure than Bateman–Horn constants.
- C11: genuinely interesting (not Bateman–Horn); needs a convergence argument for the local product, independence caveats through ord_p(2), and cannot validate a four-digit constant on eight data points.
- C13: the cube-obstruction theorem is valuable; "super-geometric decay" is undefined in the statement; largest-exception numerics do not belong in the formal statement. The x^{1/3} asymptotic for the full exceptional set is conditional on part (i).
- C14/C15/C17: classical; C15 must make the ordered/unordered normalization and the 1/2 factor explicit.
- C16: the uniform clause is significant; the Gaussian-residual clause is underdefined — specify the empirical measure and the covariance structure; Poisson normalization need not give unit variance.
- C18: the log³x exponent is robust; the exact limsup constant is speculative; "to first order" after an exact limsup equality is incoherent.
- C19: inverting Granville's limsup to a first-occurrence limit is logically insufficient and the stated conjecture may well be false; weaken to a liminf or record-subsequence law.
- C20: potentially significant; state Gallagher's law conditionally on Hardy–Littlewood; define the sampling distribution of t; the O(1/log²x) error does not follow from an o(h) singular-series remainder.
- C21: the prime-square mechanism appears genuinely interesting; clause (iii) — sign density strictly between 1/2 and 1 — is inconsistent with the paper's own drift/noise → 0 analysis, which forces density 1/2; the weighted→unweighted passage, exclusion of other prime-power configurations, and class-count covariance all need work.
- C22: part (i) is established territory (HLS); marginal Exp(1) convergence does not imply a Gumbel law for the max without a joint-independence hypothesis; θ(q) is underspecified — decompose into discrete-hazard and ordering-correlation parts; q ≤ 6000 cannot distinguish candidate functional forms.
- C23: global KS equidistribution does not control the shrinking target q_p = 0, so the Wieferich count does not follow from clause (i); the O(1) fluctuation contradicts the Bernoulli model's √(log log x) and the paper's own calibration principle; the third-Wieferich location forecast is uncalibrated.
- C24: uniformity over the fixed set A ≤ 199 is logically automatic; a meaningful uniform conjecture must let A grow with N.
- C25: a weakened restatement of Lemke Oliver–Soundararajan; extract the constant analytically from their formula instead of fitting a numerical range.

Comparative ranking — most important as open problems: C2, C1/C8, C16, C20, C22, C23, C17. Most genuinely novel: C22(ii), C21(i)–(ii), C20, C11, and the cube-obstruction theorem. C19 is novel in its constant but, without a valid derivation, of lower present value.

Final judgment: methodological value high; computational and expository value high; conceptual novelty across all 25 moderate; novelty of the best two or three phenomena potentially high; reliability of the statistical section as formulated uneven, with several substantive logical problems. A more compelling paper would separate a benchmark suite from a small set of focused research conjectures (revised 20, 21, 22 and perhaps 11 or 19) with complete heuristic derivations and clearly stated dependence assumptions. Publication readiness: promising working draft; major revision of Conjectures 19–23 and a more conservative novelty taxonomy required.
