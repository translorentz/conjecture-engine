# Admission audit of the ten submitted hybrid conjectures

Date: 30 August 2026

## Final accounting

The source file \`novel_hybrid_conjectures_report.docx\` contained ten
candidates. Two survive the admission standard, both after material repair:

- candidate 3 is admitted as the new **Conjecture 394**, the quenched random
  Floer-barcode entropy law;
- candidate 10 is not double-counted: it strengthens the existing
  **Conjecture 392** from the first Jacobian minimum to every fixed initial
  segment of successive minima.

The other eight candidates are not admitted. Candidate 4, the LQG spectral
tangent, was provisionally retained in an early pass and then removed by an
independent re-audit: after the exact field-shift normalization is made, its
local statement appears to follow from quantum-cone coupling plus locality,
so its claim to novelty is too weak for this collection.

“Novel” here means that no theorem or materially equivalent conjecture was
located in the existing 393-item collection or in the nearest literature
searched as of the audit date. It is an evidence-backed admission judgment,
not a logically absolute claim about every unpublished source.

## Admission standard

A candidate had to pass all of the following tests.

1. **Formal determinacy.** The ensemble, invariant, topology or mode of
   convergence, normalization, and order of limits had to be explicit.
2. **Novelty.** A new conjunction of old project claims, an expected local
   corollary, or a restatement of an existing conjecture was not enough.
3. **Sound mechanism.** Established inputs had to force the proposed scale
   and leave a clearly identified missing implication.
4. **Falsification pressure.** Exact reductions, normalization checks, model
   obstructions, or finite tests had to be recorded without treating them as
   proofs of an asymptotic law.
5. **Consequence.** A proof had to add a reusable theorem or invariant, not
   only settle an isolated numerical pattern.

## Decision ledger

| Source candidate | Decision | Audit finding |
|---|---|---|
| 1. Adelic random-matrix independence | Defer | A joint Archimedean/\(p\)-adic theorem could be new, but the source does not select a real bulk or edge statistic, a \(p\)-adic spectral state space, a topology, or singular-characteristic-polynomial conditioning. Different choices give inequivalent claims. It also sits directly between Conjectures 384 and 388, so the submitted form does not isolate a new mechanism. |
| 2. Random-free graphon rate-distortion | Reject | The leading \(s n\log n\) law and Ahlfors-type latent-row mechanism are already Conjecture 53. The proposed rate-distortion functional and reconstruction class are not defined tightly enough to state a distinct lower-order theorem. |
| 3. Random Floer-barcode entropy | **Accept after repair as 394** | The deterministic surface equality is known, but no iid Hamiltonian-cocycle equality between endpoint barcode growth and quenched prefix entropy was located. The repaired statement fixes coefficients, includes all free homotopy classes and finite bars, handles degenerate endpoints, and keeps the essential outer-\(\varepsilon\)/inner-limsup order. |
| 4. LQG local spectral tangent | Reject on final re-audit | Quantum-area rooting gives the quantum-cone local field. Under \(h\mapsto h+c\), area and Liouville-Brownian eigenvalues scale inversely, so \(\mu_h(B_r)\lambda_j(B_r)\) is already shift-invariant. Once a rescaled metric ball is coupled inside a common field window, locality identifies its killed Dirichlet form and spectrum. The proposed one-scale finite-dimensional limit therefore appears to be an expected local-coupling corollary, not a sufficiently new conjecture. A multiscale spectral-scenery mixing theorem could be new, but it was not the submitted statement. |
| 5. Categorical mass/stability equality | Reject | The shift functor destroys the unquotiented formula. After quotienting by the natural stability-space action, the deterministic core substantially overlaps existing categorical mass-growth and translation-length theory. The random-cocycle data and integrability assumptions needed for a genuinely new law are absent. |
| 6. Quantitative stationary Freiman stability | Defer | A quantitative \(\bar d\)-stability theorem would be stronger than Conjecture 56, but the proposed information-rate deficit need not control long-memory or bilaterally deterministic processes in \(\bar d\). The extremal class and stability modulus also depend on an unresolved equality classification. |
| 7. Transport curvature equals reconstruction threshold | Reject as structurally unsound | A worst-case one-step contraction threshold and a typical long-distance reconstruction threshold are not the same object. On the Ising tree the natural contraction and reconstruction boundaries are governed by \(b\tanh\beta\) and \(b\tanh^2\beta\), respectively; metric rescaling adds another normalization defect. |
| 8. Linial–Meshulam torsion free energy | Reject | The torsion burst, its quadratic logarithmic scale, and its relation to the homology transition already have a substantial experimental and conjectural literature. The source gives no distinct critical window, normalization, spatial observable, or limiting object. |
| 9. Lorentzian-Hodge spectral percolation | Reject | The operator and normalization are not specified. Natural trace and rank quantities reduce first to effective-resistance, cycle-surplus, or ordinary Hodge data, so no new Lorentzian mechanism is isolated at the \(c=1\) transition. |
| 10. Higher Hodge minima versus short geodesics | **Accept after repair by strengthening 392** | The higher-minimum extension is genuinely new once the comparison length is defined by homological rank, not merely by the \(j\)-th shortest geodesic. The collar-capacity asymptotic supports one direction; excluding short integral Hodge combinations without \(k\) independent thin handles is the new converse. Only a sequential shrinking-window law is justified. |

## Conjecture 394: repaired statement and reasoning

Let \(X_1,X_2,\ldots\) be iid Hamiltonian diffeomorphisms of a closed
symplectic surface and \(\Phi_n=X_n\circ\cdots\circ X_1\). The quenched entropy
uses the prefix Bowen metric

\[
d_n^\omega(x,y)=\max_{0\le j<n}d(\Phi_jx,\Phi_jy).
\]

The barcode side uses the unpinned absolute fixed-point Floer barcode over
\(\mathbb F_2\), summed over every free homotopy class. It counts only finite
bars longer than \(\varepsilon\), and defines degenerate endpoints by the
lower-semicontinuous perturbation extension. The admitted equality is

\[
\lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}
 \frac1n\log^+ b_\varepsilon^{\rm fin}(\Phi_n)
 =h_{\rm top}^{\rm q}(\mu)
\qquad\text{almost surely}.
\]

The principal reason the statement is nontrivial is also its main failure
mode: the right side sees every prefix \(\Phi_0,\ldots,\Phi_{n-1}\), while the
left side sees only Floer data of the endpoint \(\Phi_n\). No known
composition inequality prevents exponential creation and cancellation of
long bars.

Two exact boundary reductions survive scrutiny.

- A point-mass law is precisely the deterministic surface theorem of
  Çineli–Ginzburg–Gürel.
- For the in-model lazy law
  \(\mu=(1-p)\delta_{\rm id}+p\delta_\phi\), every deterministic iterate from
  \(0\) through the current endpoint occurs among the prefixes and
  \(S_n/n\to p\). Both sides therefore equal \(p\,h_{\rm top}(\phi)\).

The checked-in verifier exhausts all \(131{,}071\) zero-one words through
length 16 for the no-skipped-iterate identity and performs a separate seeded
Bernoulli-rate check. It computes no Floer barcode and is not presented as
evidence for the unresolved noncommuting cancellation mechanism.

Nearest boundary:

- [Çineli–Ginzburg–Gürel, deterministic entropy equality](https://arxiv.org/abs/2111.03983)
- [Çineli–Ginzburg–Gürel, barcode growth](https://arxiv.org/abs/2207.03613)
- [Çineli–Ginzburg–Gürel–Mazzucchelli, barcode-entropy survey](https://arxiv.org/abs/2605.25965)
- [Gong, deterministic persistent-entropy refinement](https://arxiv.org/abs/2606.19071)

## Conjecture 392: accepted all-fixed-\(k\) strengthening

For a Weil–Petersson random closed genus-\(g\) surface, define

\[
\ell_j^{\rm hom}(X_g)=\inf\left\{L:
 \operatorname{rank}_{\mathbb Z}
 \langle[\gamma]:\gamma\text{ primitive nonseparating simple geodesic},
 \ \ell(\gamma)\le L\rangle\ge j\right\}.
\]

This excludes separating curves and bounding pairs, either of which would
make “the \(j\)-th shortest curve” the wrong coordinate for a lattice
successive minimum. For every fixed \(k\), the admitted two-sided statement
conditions on the union of the Hodge-thin and geodesically thin events and
asserts

\[
\max_{j\le k}\left|
 \frac{\pi m_j(J(X_g))^2}{\ell_j^{\rm hom}(X_g)}-1
\right|\longrightarrow0
\]

in probability as \(g\to\infty\) and then the thinness parameter tends to
zero. It predicts the transferred tail

\[
\Pr\{\pi m_k^2\le\varepsilon\}
 \sim \frac{\varepsilon^{2k}}{4^k k!}.
\]

The normalization is supported by the exact expansions

\[
\Lambda(\varepsilon)=\frac{\varepsilon^2}{4}
 +\frac{\varepsilon^4}{96}+\cdots,
\qquad
\frac{\pi\,\operatorname{cap}(\ell)}{\ell}\to1.
\]

The verifier recomputes the Poisson-tail constants for \(k=1,2,3\) and the
collar-capacity limit. These checks establish the scale and constants only.
The hard conjectural step is the reverse implication: ruling out \(k\) very
short integral harmonic directions in the absence of \(k\) corresponding
homologically independent thin collars.

Nearest boundary: Mirzakhani–Petri's short-geodesic process, deterministic
period-matrix degeneration, and Muetzel's upper bounds for successive
Jacobians minima.

## Reproducibility

- \`python verify/ar_random_barcode.py\`
- \`python verify/aq_hybrid_laws.py\`

Both scripts label exactly what they do not test.
