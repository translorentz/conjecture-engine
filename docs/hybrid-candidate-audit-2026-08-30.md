# Audit of the hybrid candidate conjectures (30 August 2026)

This note records the admission decision for the ten candidates in
`novel_hybrid_conjectures_report.docx`.  The tests were deliberately stricter
than a plausibility screen: each candidate was compared with the existing
collection and the nearest literature, its state space and order of limits
were checked, and any exact normalization or finite proxy was recomputed.
Only candidates 3 and 4 survive, in sharpened form, as Conjectures 394 and
395.  The attachment's wording is not adopted verbatim.

## Decision ledger

| Candidate | Decision | Novelty and soundness finding |
|---|---|---|
| 1. Adelic spectral factorization for iid integer matrices | Not admitted | This is a non-Hermitian hybrid of the collection's Conjecture 384 (real local spectrum versus Smith data) and Conjecture 388 (real versus fixed-prime root processes).  [Shen's 2026 fixed-prime universality theorem](https://arxiv.org/abs/2608.06576) also makes the local factor law a rapidly moving boundary.  More importantly, the report does not specify the p-adic spectral state space (roots, irreducible factors, eigenvalue valuations, or a projective point process), the conditioning needed for singular characteristic polynomials, or the real bulk/edge scaling.  Those choices produce inequivalent claims. |
| 2. Random-free graphon rate-distortion | Not admitted | Its principal Ahlfors-regular conclusion is already Conjecture 53, including the `s n log n` normalization and the latent-row coding mechanism.  The proposed rate-distortion identity may be a useful proof programme, but `R_W` and the reconstructible class are not defined tightly enough to create a distinct statement. |
| 3. Random Floer barcode entropy | **Admitted as Conjecture 394** | The deterministic one-map equality between barcode and topological entropy on closed surfaces is known, as is a sequential deterministic formalism.  The iid cocycle equality appears to be a genuine extension.  The corrected statement uses the standard quenched Bowen metric, counts finite bars, uses an outer epsilon limit and an inner limsup, and makes no unsupported fixed-epsilon subadditivity claim. |
| 4. LQG local spectral tangent | **Admitted as Conjecture 395** | Weyl asymptotics for Liouville Brownian motion and local metric/volume results do not identify the joint low-eigenvalue law of a shrinking intrinsic metric ball.  The corrected statement is rooted at a quantum-area-typical point and normalizes by `mu_h(B_r)`, the unique multiplicative normalization invariant under adding a constant to the field.  It explicitly requires a spectral, not merely metric-measure, tangent. |
| 5. Categorical mass growth | Not admitted | The unquotiented statement fails under shifts: categorical mass can be displaced without genuine complexity growth.  Quotienting by shifts removes that counterexample but leaves an overlap-sensitive stability problem rather than the asserted law. |
| 6. Stationary quantitative Freiman principle | Not admitted | The exact zero-defect mechanism is already Conjecture 56, formulated through the translational stabilizer of the stationary law.  The report's quantitative version does not fix a topology or distance on stationary processes and does not define the claimed zero-entropy extension, so there is no falsifiable stability modulus. |
| 7. Transport curvature equals reconstruction | Not admitted | The proposed identity conflates a local second variation of transport cost with a global statistical reconstruction threshold.  No common variational object or normalization forces equality; simple rescaling changes one side without preserving the other. |
| 8. Linial-Meshulam torsion free energy | Not admitted | The torsion burst and its coincidence with the homology transition were already the subject of the experiments and Cohen--Lenstra conjectures of [Kahle--Lutz--Newman--Parsons](https://arxiv.org/abs/1710.05683), so the report's broad novelty claim fails.  Any potentially new spatial “burst localization” clause lacks a specified window, torsion statistic, and limiting law, and therefore cannot be tested as written. |
| 9. Lorentzian-Hodge spectral percolation | Not admitted | The proposed Lorentzian-Hodge control is not the first-order obstruction: ordinary cycle surplus and effective resistance already govern the relevant emergence and small-eigenvalue mechanisms.  The report gives no regime in which the new structure changes the threshold rather than re-encoding it. |
| 10. Weil-Petersson/Hodge process transfer | Not admitted | The first-minimum rare-tail statement is already Conjecture 392.  Its linear collar normalization is asymptotic only as the geodesic length tends to zero, so it cannot justify the report's full fixed-window point-process transfer.  A higher-minimum claim would also have to impose homological independence and specify the capacity-corrected coordinate. |

## Accepted statement 394: checks and limitations

Let `X_1,X_2,...` be iid Hamiltonian diffeomorphisms of a closed symplectic
surface and let `Phi_n=X_n...X_1`.  For a sample path, the quenched random
topological entropy is defined from the Bowen metric

`d_n^omega(x,y)=max_{0<=j<n} d(Phi_j x,Phi_j y)`.

The admitted claim equates it with the exponential growth rate of finite
Floer bars longer than epsilon, after taking `epsilon` down to zero.  Three
repairs to the source statement are essential:

1. the finite-bar convention avoids counting the homological infinite bars;
2. `limsup` is retained because no concatenation inequality for barcode
   counts has been proved for random products;
3. the equality is almost sure and uses the quenched, not annealed, entropy.

The one-atom law reduces exactly to the deterministic surface theorem of
Çineli--Ginzburg--Gürel.  As a finite diagnostic only, products of positive
hyperbolic matrices in `SL(2,Z)` satisfy
`n^{-1} log|det(Phi_n-I)| - n^{-1} log rho(Phi_n) -> 0`; the verification
script recomputes this proxy.  It does not compute Floer homology and is not
presented as evidence for the cancellation mechanism.  A decisive first
theorem would be a tempered quasi-multiplicative estimate for long-bar counts
under composition.  Failure could occur through exponentially many short
bars which are repeatedly created and cancelled, so that the outer epsilon
limit disagrees with orbit complexity.

Nearest boundary: [Çineli--Ginzburg--Gürel, *Topological entropy of Hamiltonian diffeomorphisms: a persistence homology and Floer theory perspective*](https://arxiv.org/abs/2111.03983),
[Çineli--Ginzburg--Gürel, *On the growth of the Floer barcode*](https://arxiv.org/abs/2207.03613), [Gong's deterministic persistent-entropy refinement](https://arxiv.org/abs/2606.19071),
and Bogenschütz's random topological entropy formalism.

## Accepted statement 395: checks and limitations

For a unit-area gamma-LQG sphere, root at a point sampled from quantum area,
take the intrinsic metric ball `B_r` and the Dirichlet spectrum of Liouville
Brownian motion killed on leaving that ball.  The admitted finite-dimensional
law says that

`(mu_h(B_r) lambda_1(B_r), ..., mu_h(B_r) lambda_k(B_r))`

converges to the corresponding vector for the unit metric ball in the rooted
gamma-quantum cone.

The normalization survives the exact field shift.  Under `h -> h+c`, quantum
area is multiplied by `exp(gamma c)`, the LQG metric by `exp(xi c)`, and the
Liouville-Brownian generator by `exp(-gamma c)`; hence the product of area and
each Dirichlet eigenvalue is unchanged after the radius is co-scaled.  The
verification script checks the analogous generalized-eigenvalue identity on
random weighted Dirichlet forms to machine precision.

Weyl's law supports area as the high-energy normalization but does not imply
this low-spectrum tangent.  The missing step is joint convergence of the
rooted metric, measure, and Dirichlet form (for example in a Mosco/resolvent
topology).  A decisive first theorem would be tightness and uniqueness of the
killed resolvent on shrinking metric balls.  A concrete failure mode is that
metric-measure tangents converge while the energy forms retain microscopic
information and have multiple subsequential spectral limits.

Nearest boundary: [Berestycki--Wong, *Weyl's law in Liouville quantum gravity*](https://arxiv.org/abs/2307.05407),
[Cai, *A Response Calculus for the Liouville Brownian Motion Spectrum*](https://arxiv.org/abs/2608.02459),
and the established LQG metric and metric-ball volume/exit-time theory.

## Reproducibility

Run `python verify/ar_random_barcode_lqg.py`.  It checks the two exact
calibrations above, reports the proxy gap rather than suppressing it, and
labels both asymptotic conjectures as untested by finite computation.
