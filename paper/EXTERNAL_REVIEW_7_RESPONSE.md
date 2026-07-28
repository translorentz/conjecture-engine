# Response to the seventh external review (paper v9 -> v10)

The seventh review was a referee-style assessment: a 1-5 scorecard plus
a list of specific mathematical error claims.  Protocol as always:
every error claim was re-derived or recomputed before being conceded;
everything that survived checking was fixed in full.  No bibliography
entries were added or changed (all new attributions are inline names
already cited), so twin-citation gate round 6 (32/32 unanimous)
remains in force for v10.

## Error claims: verified and conceded

1. **C08(ii), occupation-fraction constant — the review's best catch.**
   The stationary OU occupation covariance is
   Cov(I_s, I_{s+u}) = (1/2pi) arcsin(e^{-u/2}), whose integral over u
   is (ln 2)/2, so the null sd of the leadership log-density is
   sqrt(ln2 / log x).  Our 2*sqrt(ln2/log x) had imported the factor
   belonging to the *sign average* 2I-1.  Verified by quadrature,
   fixed in the paper and in `c03b`/`c07b` (rerun).  Every leadership
   significance in the paper doubles as a result; notably the cousin
   races of C21(v) move to +2.7 and +2.3 null sd and are now
   described as moderately strong directional evidence (with an
   explicit correlated-races caveat), while the C08 null control sits
   at -1.4, inside its band.  A correction that strengthens the
   paper's central evidence is the audit protocol working exactly as
   intended.

2. **C09, p = 3.**  gcd(F_3, L_3) = gcd(2, 4) = 2 with z(2) = 3: the
   divisor-disjointness claim is false as stated for the prime 2.
   Restated for odd prime divisors, with gcd(F_p, L_p) = 2 iff 3 | p
   recorded.  Also softened (iii): a naive-constant tail estimate is
   *contradicted at the 3e-3 level* by A080327's index 148091, not
   "refuted" — one event cannot refute a probability statement.

3. **C14, weight factor.**  Lambda(q^2) = log q, not 2 log q.  Script
   and paper fixed; the predicted contaminated-lane drift halves to
   +0.15 (observed +0.27 +- 0.33 — consistent before and after).  The
   ordered-representation factor 2 survives only in C25, where it
   belongs.

4. **C13, degenerate cases.**  deg F >= 2 and m > j >= 1 added; for
   linear F the cofactor is identically 1 and the principle is empty.

5. **C02, local law.**  The prose now states the full three-state
   law (omega = 3 w.p. (p-1)/3p; omega = 1 w.p. 1/p when p | a;
   omega = 0 otherwise); the computations always used it.

## Formalization demands: implemented

* **Probability spaces.** C15 now carries the explicit dyadic-log
  ensemble E_X U over (X, 2X]; C23(iii) is split into a deterministic
  limsup clause and a randomized CLT clause with the sampling law
  stated (x log-uniform on [X, X^A]).
* **Off-index covariance terms.** C16(ii) gains the pinned 4-point
  (K4) off-index term with its dominance range; C24(ii)'s same-index
  contribution is relabeled and its off-index component flagged open.
* **C19.** Clause (ii) is now *conditional on the realization
  hypothesis* — infinitely many g first occurring at the
  Cramér–Granville envelope scale.  The review is right that
  inverting the limsup is not automatic; without the hypothesis only
  the lower bound liminf >= sqrt(e^gamma/2) follows.  Clause (iii)
  is upgraded from "O_P(1), Gumbel-type" to an explicit min-type
  (reversed) Gumbel distributional limit for the first-passage error.
* **C22.** theta_disc^infty is removed from the formal display — a
  control-model constant has no place in a statement advertised as
  model-free; the formal claim is existence and positivity of the
  dyadic-average limit, and the excess-over-discreteness reading is
  explicitly the diagnostic layer.  The sd(Theta(q)) -> 0 clause is
  withdrawn: the limiting distribution over dyadic blocks is left
  open, since fluctuations from the arithmetic of q and q-1 may
  persist at bounded size.
* **C11.** Convergence is stated along the canonical exhaustion
  S_z = {5 <= p <= z}, and the working constant kappa* = 4.2734... is
  explicitly labeled a hybrid (CRT-exact core through 19 times
  independent per-prime factors to 300), equal to kappa_{S_300} iff
  the observed exact factorization persists.
* **C17.** Display weakened to (1+o(1)): our own measured 13-19%
  level deficit means the 1/log n coefficient is not pinned down.
* **C18.** Clause (i) is now the decaying-repulsion law
  rho_k(x) = -(c_k loglog x + d_k)/log x (1+o(1)); the measured
  rho_1, rho_2 are labeled one-height observations, not asymptotic
  constants; clause (ii) notes sigma^2(x) -> 1 under the decay law.
* **C12.** Clause (i) marked a conditional proposition; the
  divergence clause (ii) carries the caveat that H <= 3000 cannot
  distinguish divergence from a large pure log; "establishing"
  replaced by "consistent with".
* **C20.** The finite-x variance display is tagged conditional on
  the quantitative hypothesis inside the statement, not only in the
  following prose.
* **C21(v).** The contamination operator C_{d,m}(a; x) is given a
  formal display, separating the provable census layer from the
  conjectural transfer layer.
* **C10(iii).** The cross-index dependence question now has a
  registered concrete programme: the deterministic residue linkage
  n! = m! (m+1)...n at primes p > n reduces the covariance to
  explicit character-sum averages, finite at each height.

## Declined

* **Splitting into three papers.**  The operating brief for this
  project is a single suite of 25 substantive, novel, verified
  conjectures; the section structure (Bateman–Horn instances / sparse
  sequences / representation problems / statistical laws) already
  gives the review's proposed partition as internal organization.
  This is a scope decision reserved to the operator, not a
  mathematical defect.

## Net effect

Three numerical constants changed (C08 null sd, C14 predicted drift,
and the leadership significances downstream of C08's constant); no
conjecture was weakened into vacuity; two statements became
conditional where their unconditional forms were unjustified; and the
paper's flagship evidence (cousin-race contamination) became stronger
under the corrected null.  v10 compiles clean in both the full and
blind versions, 25 conjectures each, zero provenance markers in the
blind copy.
