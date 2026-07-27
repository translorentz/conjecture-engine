# Response to the fourth external review (paper v5 → v6)

The assessment of the review and the per-conjecture plan are in
`REVISION_PLAN.md`; this document records what was executed.

## Priority concessions (both verified against primary sources)

* **C10 / Lillie.** Conceded in full. Lillie, *About the Primality of
  Primorials* (arXiv:2110.04302, Oct 2021) states the O(n⁻²) joint
  probability AND the three-instance prediction. Our earlier search
  surfaced this preprint but read it only at snippet depth. The paper
  now records this against ourselves as Finding f:c10, cites Lillie,
  and the slot carries the factorial-twin analogue (searched at
  abstract depth, including Lillie's paper itself; no prior statement
  found; verified to n = 700).
* **C20 / Montgomery–Soundararajan.** Conceded in substance; framing
  demoted to "microscopic extrapolation and numerical test", with the
  quantitative-uniform Hardy–Littlewood hypothesis spelled out.

## Structural response

The reviewer proposed shrinking to a 4-conjecture research core with a
benchmark appendix. Our brief is 25 substantive conjectures, so we
responded by raising the novelty floor of the weakest slots instead:

* **Replaced:** C6 (alternating cyclotomic chain, C = 3.6143, verified
  over five decades), C8 (null-mechanism race — the negative control of
  the C21/C25 mechanism family), C10 (factorial twins).
* **Lifted to family level:** C1 (uniform quadratic de Polignac over
  all even shifts, 150-shift profile verified), C5 (complete φ(k)=2
  twin-base analysis: k=4 parity-dead, k=6 collapses to k=3 via
  Φ₆(x) = Φ₃(x−1) — both facts found by our own machinery during the
  lift).
* **Derivational upgrades:** C16(ii) covariance kernel from HL triple
  constants (evaluated, 870 pairs); C24(ii) family kernel from pair
  singular series (computed: the cross-member kernel is *null* — the
  observed sub-Poisson profile must be diagonal); C22(ii) θ_disc
  defined by a named Bernoulli control + the stratified prime/smooth
  experiment (θ_corr = +0.824 ± 0.009 on prime moduli, differentiating
  the ordering anomaly from Leung's smooth-q effects); C11(ii)
  entanglement-aware CRT-exact κ (factorization verified exact through
  p ≤ 19); C21 split into Lemma + M_x-clauses with the
  Rubinstein–Sarnak zero-oscillation caveat; C25 given the explicit
  log-sampling measure, the HL-weighted drift (model/empirical = 0.98),
  the internal null lane n ≡ 1 (mod 3) (predicted and verified), and
  the sign-density clause (E[Φ(κ)] = 0.572 vs observed 0.588).
* **Kept with fixes:** C13 (sieve wording), C19 (realized-gap domain),
  C23 (LIL scale; quantifier), C4 (reframed per the reviewer's own
  words), C9 (deficit flag retained; the Grantham–Granville
  rank-of-apparition computation judged out of scope and said so),
  attributed benchmarks unchanged at the reviewer's grades.

## Gate maintenance

The bibliography gained Lillie and Rubinstein–Sarnak (30 entries);
per standing protocol this re-triggered the twin-citation gate with a
fresh pair of independent verifiers (round 5). See VERIFICATION.md for
the outcome.
