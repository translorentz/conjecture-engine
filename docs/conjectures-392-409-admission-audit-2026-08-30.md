# Combined admission record: source survivors and fifteen new conjectures

Date: 30 August 2026

## Accepted collection change

The completed change contains exactly:

1. **one new numbered survivor from the ten submitted candidates:**
   Conjecture 394 (quenched random Floer-barcode entropy);
2. **one accepted source candidate incorporated as a strengthening rather than
   a duplicate:** Conjecture 392 now treats every fixed initial segment of
   Jacobian successive minima;
3. **fifteen new, independently iterated conjectures:** Conjectures 395–409.

Thus the main collection contains 409 numbered conjectures. The proposed LQG
spectral tangent is not included.

Detailed ledgers:

- [ten submitted candidates](hybrid-candidate-audit-2026-08-30.md)
- [fifteen new cut-rank conjectures](graph-state-cut-rank-audit-2026-08-30.md)

## Admission matrix

| No. | Short title | Novelty boundary | Soundness anchor | Consequence if proved |
|---:|---|---|---|---|
| 392 | Thin-handle Hodge successive minima | Extends the deposited first-minimum law and deterministic upper bounds to a two-sided all-fixed-\(k\) random equivalence | Homological-rank length, Mirzakhani–Petri tails, collar capacity | Transfers rare-event laws between hyperbolic thin handles and Jacobian lattice geometry |
| 394 | Quenched random Floer barcode entropy | Deterministic barcode entropy is known; iid endpoint-versus-prefix equality was not located | Point-mass and lazy Hamiltonian walks reduce exactly | Gives a symplectic formula for quenched random orbit complexity |
| 395 | Quenched balanced-cut nullity | Fixed-cut finite-field law is known; one-realization empirical law is new | Exact rectangular rank count | Quenched entanglement spectrum of random qudit graph states |
| 396 | Extreme balanced-cut defect | Known marginal tail does not settle dependent extrema | First-moment scale and union-bound upper estimate | Worst-cut entanglement and tensor-network bottlenecks |
| 397 | Poisson graph-state distance | Random linear-code law does not cover symmetric graph generators | Two exact formulas for the mean | Sharp finite-blocklength random stabilizer-code distance |
| 398 | Labelled cut-rank rigidity | Universal completeness is false; typical labelled completeness remains open | Exact LC-fibre agreement through six vertices | Generic graph-state identification and generic LU–LC |
| 399 | Positive-rank-tail log-concavity | Rank-one version is explicitly false | 13-vertex negative control and atlas search | New shape/negative-dependence principle for cut entanglement |
| 400 | Forest log-concavity | Classical matching polynomials count different objects | Rooted recurrence and exact tree search | Shape theorem for noisy forest entanglement |
| 401 | Forest Hurwitz stability | Not the classical matching polynomial | Exact Routh and root tests; star boundary | Stable-polynomial structure for maximum-matching enumerators |
| 402 | Path–star stochastic extremality | Ordinary Hosoya extremality is known; stochastic all-threshold order is not | Bernstein-coefficient search | Sharp noise extremizers among tree graph states |
| 403 | Fixed-leaf broom minimum | Ordinary fixed-leaf Hosoya minimum is known | Coefficientwise fixed-leaf search | Constrained stochastic extremal theorem for percolated trees |
| 404 | Typical tree reconstruction | Universal reconstruction fails at order 15 | Collision census and rooted-limb obstruction | Typical identifiability from bipartite entanglement data |
| 405 | Random-regular rank-width density | Linear order is known; normalized limit is not | Expansion scale and exact small cubic DP | Complexity density for random regular graph states |
| 406 | Cubic kernel transfer | Incidence relation is known; robust sparse-repair transfer is not | Oum incidence theorem and cubic-kernel scale | Exact leading rank-width in the barely supercritical regime |
| 407 | Grid rank-width surface tension | Treewidth phase and full-grid endpoint are known | Subcritical clusters and Jelínek endpoint | Percolation surface tension for graph-state simulation width |
| 408 | LC-orbit entropy saturation | Small orbit maps and the \(3^n\) bound are known | Exact orbit data and Eulerian-vector/index factorization | Maximal labelled-representative entropy |
| 409 | Sparse Erdős–Rényi rank-width curve | Zero/positive phases are known; density limit is not | Two-core/kernel mechanism and concentration scale | Sparse graph-state complexity free energy |

## Falsification and verification record

The checked-in scripts pass:

- \`verify/aq_hybrid_laws.py\`: all 7 checks, including the
  \(1/(4^k k!)\) tails for \(k=1,2,3\) and collar normalization;
- \`verify/ar_random_barcode.py\`: all 131,071 zero-one words through length
  16 and the seeded Bernoulli-rate calibration;
- \`verify/as_graph_state_cutrank.py\`: finite-field counts, distance mean,
  labelled LC fibres, shape and extremal tree tests, explicit negative
  controls, the reconstruction collision, small cubic widths, and LC orbit
  data.

The scripts state their limits. In particular, they do not prove the
asymptotic laws, compute noncommuting Floer barcodes, sample
Weil–Petersson surfaces, or directly test the kernel-transfer, grid, and
sparse-\(G(n,c/n)\) density limits.

## Rejected strengthenings retained as controls

- LQG one-scale spectral tangent: excluded as likely local-coupling
  corollary, not counted as novel.
- Full cut-rank log-concavity: false at rank one.
- Forest ultra-log-concavity and real-rootedness: false.
- Universal tree reconstruction from \(Z_T\): false.
- Coarse \(Z_G\) completeness: unsupported and already false in small
  labelled fibres.
- A vertex-minor threshold replacement: removed as a published duplicate.
- A separate generic LU–LC conjecture: logically redundant with 398.

## Final-review status

The frozen text received one final independent, statement-by-statement
admission audit after compilation. The reviewer returned **ACCEPT** for the
Conjecture 392 strengthening, Conjecture 394, and every one of Conjectures
395–409, ending **SATISFIED** with no material repair requested. The review
specifically rechecked the random models, sequential limits, endpoint cases,
anchor propositions, prior-art boundaries, and whether each finite test
reached the claim it was said to test.

The only retained cautions are already explicit in this record: evidence for
398, 404, and 408 is modest and is not a likelihood estimate; the checked-in
suite has no direct finite test for 406, 407, or 409; and the extended forest
computations exceed the default reproducible ranges. None was judged a defect
in the statements or their admission reasoning.
