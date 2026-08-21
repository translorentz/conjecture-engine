---
title: Twelve promise-class conjectures for many-electron approximation
---

<p style="color:#999;font-size:0.8em;margin:0 0 1em 0;">Trial Project by Bryan Cheong</p>

# Twelve promise-class conjectures for certified polynomial-time many-electron approximation

*A companion collection to [Three hundred nineteen conjectures in mathematics](index.html), held to a deliberately weaker and clearly separated standard of evidence.*

*Added to the companion deposit: 21 August 2026.*

This is a **companion** collection, of a different genre from the main suite. The main collection states exact, unconditional mathematical laws, each reproduced numerically to the stated precision. The twelve conjectures here are **conditional, promise-class** statements: each asserts that, on an explicitly defined structural promise class, a certified bounded-error classical algorithm for a finite-basis many-electron ground-state problem runs in polynomial time. None claims an unconditional polynomial-time solver for arbitrary electronic Hamiltonians, which would conflict with the fermionic-sign, QMA-hardness, and $$N$$-representability barriers [1, 2, 3].

## Standard of evidence

Three separations from the main collection hold throughout.

- **Conditional, not exact.** Every polynomial-time statement is conditioned on an explicit promise class. Where a step is not yet derived — polynomial conditioning, tractable separators, a certified polynomial-time structure for a nonconvex optimization, low approximation rank — it is stated as part of the promise, not silently assumed. A promise class that quietly encodes its own conclusion would make the conjecture vacuous; the falsifiers are written to expose exactly that.
- **Sub-lemma verification only.** The companion script `verify/promise_lemmas.py` re-derives the shared lemmas and three auxiliary bounds and runs small exact-diagonalization proxies. A passing check certifies an *ingredient* of the reasoning or a mechanism on a small instance; it is never evidence that one of the twelve structural laws holds asymptotically.
- **Known barriers respected.** The fermionic sign problem [1], $$N$$-representability being QMA-complete [2], and worst-case intractability of interacting electrons [3] are respected: each conjecture is a structural escape hatch for a restricted class, not a challenge to these results.

## Shared lemmas

Standard ingredients used repeatedly, each re-derived numerically in the companion script (ingredients, not conclusions): Rayleigh continuity; energy-to-fidelity under a gap; Krylov row leverage; natural-orbital freezing ($$q\le T$$, energy error $$\le 2\sqrt2\,\lVert H\rVert\sqrt T$$); Feshbach fixed-point perturbation (error $$\le\delta/(1-L)$$); CMI recovery ($$I(A:C\mid B)\ge-2\log F$$, so single-stitch trace error $$O(\sqrt I)$$) [13]; and treewidth-to-polynomial ($$\operatorname{poly}(n)\exp(O(t))$$ is polynomial when $$t=O(\log(n/\varepsilon))$$) [11].

## The twelve conjectures

**Conjecture 1 — Certified Influence-Graph Coupled Cluster.** On localized, gapped, charge-neutral Hamiltonians with an invertible single-reference Full-CC Jacobian ($$\lVert Df(t^*)^{-1}\rVert\le\operatorname{poly}(n)$$), polynomially many seeds, bounded effective branching, exponentially decaying weighted excitation-influence paths, and a polynomial-time computable omitted-tail envelope, a logarithmic-radius influence graph yields a Full-CC energy within $$\varepsilon$$ with a computable certificate, in polynomial time. *Mechanism:* Hassan–Maday–Wang [5] give $$\lVert t_R-t^*\rVert\le2\kappa_R\rho_R$$; Rayleigh continuity converts to energy error. *Falsifier:* a bounded-geometry gapped family whose outgoing influence does not decay faster than inverse-polynomial, or with super-polynomial Jacobian conditioning.

**Conjecture 2 — Krylov-Leverage Closure Selected CI.** With a reference of polynomial overlap, gap $$\ge1/\operatorname{poly}(n)$$, the ground state within tolerance of a polylogarithmic-order Krylov space, and polynomial effective leverage support after Hamiltonian-neighbor closure, determinant selection by Krylov row-leverage plus $$O(\operatorname{polylog})$$ closure rounds captures the ground state to $$\varepsilon$$ in polynomial time. *Falsifier:* a family whose Krylov leverage has no polynomial effective support, or where closure fails to converge in polylogarithmically many rounds.

**Conjecture 3 — Multiscale Entanglement-Curvature Active Spaces.** If statically correlated orbitals occur in $$O(\operatorname{polylog}(n/\varepsilon))$$ persistent entropy-curvature events across variational resolutions while dynamic correlation has bounded total curvature, selecting by curvature-persistence plus a logarithmic halo yields a polylogarithmic active space with a polynomial solver and a computable complementary-space bound completing the error to $$\varepsilon$$. *Falsifier:* a gapped family with an extensive set of small-but-persistent-curvature orbitals whose omission gives $$O(1)$$ error.

**Conjecture 4 — Cumulant-Treewidth Reconstruction.** If a two-body cumulant interaction graph can be thresholded (from certified interval-error RDMs) to treewidth $$O(\log(n/\varepsilon))$$ while keeping the discarded-cumulant energy below budget, a tree-decomposition solver returns energy and RDMs within $$\varepsilon$$ in polynomial time. *Falsifier:* a family where every edge-deletion set of cumulative dual-weight $$\le\varepsilon$$ leaves treewidth $$\Omega(n^a)$$.

**Conjecture 5 — Feshbach Rational External-Space Compression.** With a self-energy branch isolated and contractive ($$L<1-1/\operatorname{poly}(n)$$), polynomial coupling rank, and rational/Krylov approximability of the $$Q$$-resolvent using $$\operatorname{polylog}(n/\varepsilon)$$ applications of $$D$$, compressing $$\Sigma(E)=B(D-E)^{-1}B^*$$ by a low-degree rational approximant and solving the fixed point gives energy within $$\varepsilon$$ in polynomial time. *Mechanism:* Feshbach fixed-point perturbation converts resolvent error $$\delta$$ into $$\delta/(1-L)$$. *Falsifier:* a family where $$\operatorname{dist}(E_0,\sigma(D))$$ stays inverse-polynomial but the rational rank of $$\Sigma$$ is exponential.

**Conjecture 6 — Fermionic Conditional-Mutual-Information Stitching.** On a bounded-degree separator structure with $$I(A:C\mid B)\le C\exp(-\alpha b)$$ per buffer $$b$$ and tractable ($$O(b)$$-width) parity-preserving patch/recovery representations, recovery-map stitching of local solutions returns the ground state within $$\varepsilon$$ in polynomial time. *Novelty:* not CMI decay itself — established by 2026 work [22] — but the constructive parity-preserving stitching algorithm and its complexity theorem. *Falsifier:* a gapped bounded-degree family with constant CMI across every logarithmic separator, or small CMI with no constructible compatible recovery.

**Conjecture 7 — Natural-Occupation Tail Certified Pruning.** If retaining $$O(\operatorname{polylog}(n/\varepsilon))$$ correlation orbitals per bounded local domain drives the occupation-defect tail $$T=\sum_{F_0}n_p+\sum_{F_1}(1-n_p)$$ below $$(\varepsilon/\lVert H\rVert)^2$$, the frozen core/virtual is certified to energy error $$\varepsilon$$ in polynomial time via $$q\le T$$. *Falsifier:* a bounded-density gapped family where every polynomial local-domain retention leaves $$T=\Omega(1)$$.

**Conjecture 8 — Integral-Frustration Local-Orbital Sign-Gap.** On a localized gapped class, the determinant sign gap obeys $$\Delta_s(U)\le Cn^cF_k(U)+Cn^c\exp(-\alpha k)$$ for an integral-level frustrated-loop functional $$F_k$$, and — given a *certified* polynomial-time structure for the block-rotation optimization — a polynomial algorithm finds a basis with $$F_k\le\varepsilon/\operatorname{poly}(n)$$ at $$k=O(\log(n/\varepsilon))$$ in which projector QMC has at worst polynomial sign penalty. (Highest collision risk in the collection.) *Falsifier:* rotations with $$F_k(U_n)\to0$$ for all $$k=O(\log n)$$ but $$\Delta_s(U_n)\ge c>0$$, or average sign still $$\exp(-\Omega(n))$$.

**Conjecture 9 — Möbius Connected-Fragment Exponential Decay.** On a neutral, gapped, bounded-degree fragment graph, the Möbius connected increment $$\Delta(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}E_{\mathrm{corr}}(T)$$ decays exponentially in fragment diameter after subtracting classical electrostatics and mean-field polarization, giving a computable tail and a polynomial bounded-degree connected-cluster summation to energy $$\varepsilon$$. *Falsifier:* a family with only algebraic non-summable increment tails after the stated subtraction.

**Conjecture 10 — Globally Budgeted Hierarchical Pair Natural Orbitals.** With $$O(n)$$ strong pairs, polylogarithmic per-pair ranks, polynomially bounded certified sensitivities, and a separable discrete-convex rank-cost structure, casting all PNO ranks as one global resource allocation yields a polynomial-time truncation meeting a total discarded-weight budget with energy error $$\varepsilon$$, with strict savings over uniform thresholds on heterogeneous instances. *Falsifier:* a family where every computable polynomial sensitivity is exponentially loose, or cross-pair interference invalidates any summable tail bound.

**Conjecture 11 — Multipole-Separated Cumulant-Order Bound.** On neutral, gapped, bounded-density cell structures with bounded response moments and exponential clustering of connected quantum correlations after separating classical electrostatics, a single additive remainder inequality couples far-field multipole order $$p$$ and connected-cumulant order $$k$$, giving energy error $$\varepsilon$$ in polynomial time. *Falsifier:* a family where connected quantum correlations do not cluster exponentially after electrostatic separation, or the joint remainder is not additively controllable.

**Conjecture 12 — Chordal Local $$N$$-Representability Dual Certificate.** Using a chordal cover with bags of treewidth $$b=O(\log(n/\varepsilon))$$, principal-block $$D/Q/G$$ positivity, globally valid linear identities, no fixed local particle number, and every objective term constrained or residual-bounded, the SDP optimum $$L_b$$ is a rigorous lower bound [21] and any variational $$U_b$$ an upper bound; if $$U_b-L_b\le Cn^c\exp(-\alpha b)$$ on the promise class, increasing bag width gives a polynomial-time algorithm with a rigorous certificate $$E_0\in[L_b,U_b]$$, $$U_b-L_b\le\varepsilon$$. The bracket is unconditionally rigorous; the single conjectural ingredient is the exponentially closing gap. *Falsifier:* a low-treewidth gapped family with $$U_b-L_b\ge c>0$$ for all $$b=O(\log n)$$.

## Relation to the main collection

This companion is deliberately separated from the main suite so that the collection's "every claim verified" standard is never diluted, and so that these conditional conjectures are judged on their own terms: a crisp promise class and a single falsifiable structural quantity apiece. The full statements, mechanisms, and nearest-literature boundaries are in the companion paper `paper/conjectures_promise.tex`.

## References

1. M. Troyer and U.-J. Wiese, *Computational complexity and fundamental limitations to fermionic quantum Monte Carlo simulations*, Phys. Rev. Lett. 94 (2005) 170201.
2. Y.-K. Liu, M. Christandl, and F. Verstraete, *N-representability is QMA-complete*, Phys. Rev. Lett. 98 (2007) 110503.
3. N. Schuch and F. Verstraete, *Computational complexity of interacting electrons and fundamental limitations of density functional theory*, Nat. Phys. 5 (2009) 732–735.
4. M. Griebel and J. Hamaekers, *Sparse configuration interaction for the electronic Schrödinger equation revisited*, arXiv:2606.20385 (2026).
5. M. Hassan, Y. Maday, and Y. Wang, *Analysis of the single reference coupled cluster method: the full-coupled cluster equations*, Numer. Math. 155 (2023) 121–173.
6. S. Basumallick, E. Xu, and S. L. Ten-No, *Improvement on the screening of nonlinear commutator operations in selective coupled-cluster using Lagrangian*, J. Chem. Phys. 161 (2024) 184117.
7. A. A. Holmes, N. M. Tubman, and C. J. Umrigar, *Heat-bath configuration interaction*, J. Chem. Theory Comput. 12 (2016) 3674–3680.
8. S. Greene, R. J. Webber, J. Weare, and T. C. Berkelbach, *Beyond walkers in stochastic quantum chemistry: reducing error using fast randomized iteration*, J. Chem. Theory Comput. 15 (2019) 4834–4850.
9. T. Weaving, A. Mingare, A. Ralli, and P. V. Coveney, *Selected configuration interaction using time-evolved population statistics*, J. Chem. Theory Comput. 22 (2026) 4315–4328.
10. C. J. Stein and M. Reiher, *Automated selection of active orbital spaces*, J. Chem. Theory Comput. 12 (2016) 1760–1771.
11. I. L. Markov and Y. Shi, *Simulating quantum computation by contracting tensor networks*, SIAM J. Comput. 38 (2008) 963–981.
12. B. Peng, R. Van Beeumen, D. B. Williams-Young, K. Kowalski, and C. Yang, *Approximate Green's function coupled cluster method employing effective dimension reduction*, J. Chem. Theory Comput. 15 (2019) 3185–3196.
13. O. Fawzi and R. Renner, *Quantum conditional mutual information and approximate Markov chains*, Comm. Math. Phys. 340 (2015) 575–611.
14. B. Swingle and Y. Wang, *Recovery map for fermionic Gaussian channels*, J. Math. Phys. 60 (2019) 072202.
15. K. J. H. Giesbertz and R. van Leeuwen, *Natural occupation numbers: when do they vanish?*, J. Chem. Phys. 139 (2013) 104109.
16. R. Levy and B. K. Clark, *Mitigating the sign problem through basis rotations*, Phys. Rev. Lett. 126 (2021) 216401.
17. K. Murota and S. Todo, *Local basis transformation to mitigate negative sign problems*, arXiv:2501.18069 (2025).
18. J. S. Herz, R. Schäfer, M. G. Gonzalez, and D. J. Luitz, *Sign-optimized quantum Monte Carlo*, arXiv:2607.24679 (2026).
19. B. Paulus, *The method of increments — a wavefunction-based ab-initio correlation method for solids*, Phys. Rep. 428 (2006) 1–52.
20. A. Altun, F. Neese, and G. Bistoni, *Extrapolation to the limit of a complete pair natural orbital space in local coupled-cluster calculations*, J. Chem. Theory Comput. 16 (2020) 6142–6149.
21. N. C. Rubin and D. A. Mazziotti, *Comparison of one-dimensional and quasi-one-dimensional Hubbard models from the variational two-electron reduced-density-matrix method*, Phys. Rev. B 89 (2014) 245127.
22. J. Yi, K. Li, C. Liu, Z. Li, and L. Zou, *Universal decay of mutual information and conditional mutual information in gapped pure- and mixed-state quantum matter*, Phys. Rev. Lett. 136 (2026) 116604.
23. G. E. Massaccesi et al., *Is the matrix completion of reduced density matrices unique?*, J. Phys. Chem. Lett. 17 (2026) 3430–3434.
24. L. Peng, X. Zhang, and G. K.-L. Chan, *Fermionic reduced density low-rank matrix completion, noise filtering, and measurement reduction in quantum simulations*, J. Chem. Theory Comput. (2023); arXiv:2306.05640.
