---
title: Fifty conjectures in number theory
---

<p style="color:#999;font-size:0.8em;margin:0 0 1em 0;">Trial Project by Bryan Cheong</p>

# Fifty conjectures in number theory

*July 27, 2026*

## Summary of the conjectures

**Part I — conjectures from the local–global random model, in importance–novelty order.**

1. **Prime-power contamination calculus (Conjecture 1).** For a balanced pair race $$(n,n+d)$$ mod $$m$$, the surviving prime-square orientations $$(q^2-d,q^2)$$, $$(q^2,q^2+d)$$ occupy provably computable residue classes, and the operator $$\mathcal C_{d,m}(a;x)=\sum_{o}\sum_{q}\Lambda(q^2)\Lambda(\text{prime member})$$ determines the drift vector: for twins, $$\mathcal{M}_x\bigl(D_1(t)\log^2t/\sqrt t\bigr)\to c_T=\tfrac12C(x,x^2-2)$$ (mod $$5$$) and $$\to2c_T$$ on class $$7$$ (mod $$8$$), symmetric differences $$\to0$$; in general each class deficit satisfies $$\mathcal{M}_x(\mathrm{deficit}\cdot\log^2t/\sqrt t)\to\lim\mathcal C_{d,m}(a;x)/\sqrt x$$. Convergence of these logarithmic means at drift scale is part of the conjecture (Rubinstein–Sarnak-type structure for pattern races).

2. **Pinned singular-series variance (Conjecture 2).** With $$R(h)=C_4(0,2,h,h+2)/\mathfrak{S}(2)^2$$ and $$G(H)=\sum_{h\le H}(1-h/H)(R(h)-1)$$: (i) [conditional proposition] the moving-window twin-pair count obeys $$\operatorname{Var}/\mathbb E=1+\mathfrak{S}(2)(2G(H)-1)/\log^2x +o(\log^{-2}x)$$; (ii) $$-G(H)/\log H\to\infty$$: pair counts are more sub-Poisson than prime counts.

3. **Least-prime ordering deficit (Conjecture 3).** With $$U(a,q)=\mathrm{Li}(p(a,q))/\varphi(q)$$: (i) $$U\Rightarrow\mathrm{Exp}(1)$$ marginally (attributed), Gumbel maximum under joint independence; (ii) the dyadic averages of $$\Theta(q)=(1-\mathbb E_a[U])\log q$$ over prime $$q\in[Q,2Q]$$ converge to a limit $$\Theta>0$$: the ordered primes fill residue classes faster than any exchangeable model, in excess of the derived discreteness and injectivity baselines.

4. **Goldbach lane race (Conjecture 4).** For $$n\equiv2\pmod4$$, prime squares enter ordered Goldbach representations only through the $$(1,1)$$ lane mod $$4$$, so with $$D=R_3-R_1$$ and the explicit weighted census $$D_{\mathrm{sys}}$$: $$\mathbb E_x[D-D_{\mathrm{sys}}]=o(\mathbb E_x[D_{\mathrm{sys}}])$$ under logarithmic sampling; the drift vanishes on the internal null subprogression $$n\equiv10\pmod{12}$$; the sign density of $$D$$ tends to $$\tfrac12$$.

5. **Least Goldbach summand (Conjecture 5).** With $$s(n)$$ the least prime $$p\nmid n$$ with $$n-p$$ prime, $$U(n)=\mathfrak{S}(n)\sum_{p\le s(n),\,p\nmid n}1/\log(n-p)$$, and the dyadic-log ensemble $$\mathbb E_X$$: (i) $$U\Rightarrow\mathrm{Exp}(1)$$; (ii) $$\Theta_G(X)=(1-\mathbb E_XU)\log X\to\Theta_G>0$$, the Goldbach sibling of the ordering deficit.

6. **Polynomial–exponential entanglement (Conjecture 6).** Primes $$n^2+2^n$$ force $$n\equiv3\pmod6$$; with $$\kappa_S=3\,D_S/\prod_{p\in S}(1-1/p)$$ built from the CRT-exact survivor density $$D_S$$ over the joint period of $$S$$ and the lane bonus $$3$$ at the primes $$2$$ and $$3$$: $$\kappa_{S_z}$$ converges along the canonical exhaustion $$S_z=\{5\le p\le z\}$$ to $$\kappa$$, the counting function is $$\sim\sum_{n\equiv3(6),\,n\le N}\kappa/\log(n^2+2^n)\asymp\log N$$; whether the limit factors exactly (as observed through $$p\le19$$) is an open question.

7. **Multibase Fermat quotients (Conjecture 7).** For $$p\nmid a$$: the Eisenstein–Lerch homomorphism confines multiplicatively dependent bases to a rational subtorus, and (iv) for multiplicatively independent bases $$(q_p(a_1),\dots,q_p(a_r))/p$$ equidistributes on the full torus as $$p$$ varies; (v) at most finitely many simultaneous Wieferich primes; plus single-base clauses: KS-discrepancy LIL at constant $$1/\sqrt2$$, shrinking-target law $$\#\{p\le x:q_p<K\}\sim\sum\min(1,K/p)$$, Wieferich-count LIL and an almost-sure CLT at the $$du/u$$ weighting.

8. **Uniform de Polignac covariance field (Conjecture 8).** $$\pi_d(x)=\mathfrak{S}(d)\mathrm{Li}_2(x)(1+o(1))$$ uniformly for even $$d\le(\log x)^A$$; the moving-window residual field has covariance $$K_3(d,d')H/\log^3x+(1/\log^4x)\sum_{\vert h\vert \le H}(H-\vert h\vert )K_4(d,d';h)$$, triple term dominant on the polylogarithmic window class, with Poisson/Gaussian regimes as finite-$$x$$ corrections to independence.

9. **Race sub-diffusivity (Conjecture 9).** Balanced-race steps at event index have negative autocorrelations obeying $$\rho_k(x)=-(c_k\log\log x+d_k)/\log x\,(1+o(1))$$; under uniformity in $$k$$, tail summability, and $$\sum c_k,\sum\vert d_k\vert <\infty$$, the diffusivity is $$\sigma^2(x)=1-2(\sum c_k\log\log x+\sum d_k)/\log x\,(1+o(1))$$, those hypotheses being model-layer, not asserted asymptotically; the asymptotic diffusive-vs-rigid dichotomy is registered open, with the rigid branch selected only at Conjecture 1(i-b) for its contaminated races.

10. **Uniform quadratic de Polignac and its constants (Conjecture 10).** $$\#\{n\le N:n^2+1,\,n^2+1+d \text{ prime}\}=C(d)I_d(N)(1+o(1))$$ uniformly for even $$d\le(\log N)^B$$; a separate power-saving rate clause; and the family law: moments of $$C(d)$$ converge to derived Euler products (mean $$2.7456\ldots$$, sd $$1.6840\ldots$$), the empirical law converging to the random product with CRT-independent local factors.

11. **First occurrences of prime gaps (Conjecture 11).** On realized gaps: $$\log p(g)/\sqrt g$$ bounded between positive constants; $$\liminf=\sqrt{\mathrm{e}^{\gamma}/2}$$ conditional on the realization hypothesis; and $$\log p(g)=\sqrt g+\tfrac12\log g-\tfrac12\log\mathfrak{S}^*(g)+E_g$$ with $$\Pr[E_g\le t]\to1-\exp(-\mathrm{e}^{2(t-\mu)})$$, the min-type Gumbel at scale $$\tfrac12$$ forced by the slope-$$2$$ hazard expansion.

12. **Stern lane race (Conjecture 12).** In $$n=p+2k^2$$, square contamination $$n=q^2+2k^2$$ sits in the $$k$$-even lane iff $$n\equiv1\pmod8$$, $$k$$-odd iff $$n\equiv3$$, and is impossible for $$n\equiv5,7$$ (provable null classes); on contaminated classes the clean-minus-contaminated difference obeys $$\mathbb E_X[D-D_{\mathrm{sys}}]=o(\mathbb E_X[D_{\mathrm{sys}}])$$ with the $$\Lambda(q^2)$$-weighted census $$D_{\mathrm{sys}}$$.

13. **Microscopic variance law (Conjecture 13).** [Conditional on quantitative Hardy–Littlewood] For windows of length $$H=\lambda(\log x)^{\alpha}$$, $$\operatorname{Var}X/\mathbb EX=1-(\log H+\gamma+\log2\pi-1)/\log x +o(1/\log x)$$ uniformly in $$1\le\alpha\le A$$, with Gallagher’s Poisson law at the boundary $$\alpha=1$$.

14. **Null-mechanism race (Conjecture 14).** For $$(n^2+1,n^2+3)$$, square contamination is algebraically impossible (single bounded exception $$(n,q)=(1,2)$$); the race mod $$5$$ is driftless at the contamination scale, $$\mathcal{M}_x(D(t)\log^2t/\sqrt t)\to0$$—the negative control for item 1—and the logarithmic occupation of leadership tends to $$\tfrac12$$ with Gaussian fluctuations $$\sqrt{\log2/\log x}$$, conjectured directly (the event-index invariance principle is a separately falsifiable local hypothesis, which does not imply it).

15. **Cubic-shift constants (Conjecture 15).** For non-cube $$a$$, the three-state local law gives $$\mathbb E_a[\omega(p)]=1$$ exactly, so the limit law of $$C(a)$$ has mean exactly $$1$$ (an $$L^2$$-martingale argument), derived sd $$0.2762\ldots$$; counts are uniform over non-cube $$a\le(\log N)^B$$.

16. **Conjecture F as a family (Conjecture 16).** $$Q_A(N)=C(A)I_A(N)(1+o(1))$$ uniformly over odd $$A\le(\log N)^B$$; same-index window covariance $$[C(A,A')-C(A)C(A')]H/4\log^2N$$ (negative for locally exclusive pairs), with the off-index pinned sum at the same $$1/4\log^2N$$ order left open.

17. **Twin-member Goldbach, orientation-resolved (Conjecture 17).** Under $$n$$-uniform Hardy–Littlewood for the four role systems, $$R_T(n)=[\sum_o\mathfrak{S}_4^{(o)}(n)]\int_5^{n-5}dt/(\log^2t\log^2(n-t)) \,(1+o(1))$$, with the exact identities $$\mathfrak{S}_4^{(\mathrm{lu})}=\mathfrak{S}_4^{(\mathrm{ul})}$$ and $$\mathfrak{S}_4^{(\mathrm{uu})}(n)=\mathfrak{S}_4^{(\mathrm{ll})}(n-4)$$.

18. **Triplet contamination (Conjecture 18).** For $$(n,n+2,n+6)$$ mod $$5$$, the unique surviving square configuration is the doubly-thinned $$(q^2-2,q^2,q^2+4)$$ ($$q>3$$), contaminating class $$2$$: $$\mathcal{M}_x\bigl((\pi_3(t;5,1)-\pi_3(t;5,2))\log^3t/\sqrt t\bigr)\to c_3$$, the Bateman–Horn constant of $$(q,q^2-2,q^2+4)$$.

19. **Sexy-pair contamination matrix (Conjecture 19).** For $$(n,n+6)$$ both orientations survive on complementary $$q$$-classes, feeding start classes $$3$$ and $$1$$ (mod $$5$$ and mod $$8$$) with independent constants $$c_A,c_B$$ (the $$(q,q^2\mp6)$$ Bateman–Horn constants) in the drift-scale sense; class $$2$$ (mod $$5$$) and classes $$5,7$$ (mod $$8$$) are provably clean.

20. **Fibonacci–Lucas twins (Conjecture 20).** The odd prime-divisor pools of $$F_p$$ and $$L_p$$ are disjoint (ranks $$p$$ vs $$2p$$; $$\gcd=2$$ iff $$3\mid p$$); only finitely many $$p$$ have both prime; the naive joint accounting assigns the catalogued index $$148091$$ prior mass about $$3\times10^{-3}$$ beyond $$10^4$$, recorded descriptively and conditionally on the probable-prime status of both $$F_{148091}$$ and $$L_{148091}$$, and fatal to any completeness list.

21. **Factorial twins (Conjecture 21).** Window rigidity: $$n!+a$$ is composite for $$2\le\vert a\vert \le n$$ (theorem), so $$\pm1$$ are the only bounded offsets; $$n=3$$ uniqueness is attributed; the joint-fluctuation clause is a declared-model CLT for $$F_+-F_-$$ under explicit covariance and higher-cumulant hypotheses.

22. **Boundary trichotomy (Conjecture 22).** For $$\deg F\ge2$$ with positive leading coefficient, $$F(m)-F(j)$$ prime forces $$m-j=1$$ outside a bounded region; for $$x^3+cx$$ the boundary lane $$3m^2-3m+1+c$$ is dead-parity for odd $$c$$, dead-$$3$$-adic for even $$c\equiv2\pmod3$$, admissible exactly for $$c\equiv0,4\pmod6$$, with uniform Bateman–Horn counts over admissible $$c\le(\log M)^B$$.

23. **Power-obstruction ladder (Conjecture 23).** $$m^k=p+j^k$$ is impossible for composite $$k$$ (theorem); for prime $$k$$ it forces $$j=m-1$$ and reduces to primality of the irreducible $$D_k(m)=m^k-(m-1)^k$$, which follows Bateman–Horn uniformly over the prime-$$k$$ lanes.

24. **Alternating cyclotomic chain (Conjecture 24).** Infinitely many primes $$p$$ with $$\Phi_3(p)$$ and $$\Phi_6(\Phi_3(p))$$ prime, at the derived Bateman–Horn rate; alternation is the unique admissible continuation in the anchored construction space.

25. **Twin cyclotomic bases (Conjecture 25).** Of the $$\varphi(k)=2$$ family, only $$k=3$$ survives ($$k=4$$ parity-dead, $$k=6$$ a translate), and $$\Phi_3(n)$$, $$\Phi_3(n+1)$$ are simultaneously prime infinitely often with the computed Bateman–Horn constant.


**Part II — structural conjectures, in programme order.**


26. **Connected motif generating functional (Conjecture 26).** A full connected diagram calculus for all joint cumulants of prime motifs.

27. **Complete overlap-renormalization filtration (Conjecture 27).** A classification of every possible covariance scale and rigid eigenspace in a finite motif family.

28. **Regularized mesoscopic local–spectral trace formula (Conjecture 28).** Independently mollified Euler-product and multiple-zero functionals agree after named counterterms, and the limit is regularization independent.

29. **Anchored arithmetic polymer expansion (Conjecture 29).** Palm cluster activities are graded by the number of new prime constraints beyond one anchored motif.

30. **Topological expansion of non-Gaussianity (Conjecture 30).** The first non-Gaussian terms are graded by the homology of overlap-incidence complexes.

31. **Connected first-arrival functional (Conjecture 31).** The entire least-prime point process has connected kernels obtained from same-class prime correlations.

32. **Tested Gauss-polyspectral reciprocity (Conjecture 32).** Scalar tensor observables have exact Gauss-transport identities under the random-modulus law and dual arithmetic limits.

33. **Rubinstein–Sarnak terminal chaos dichotomy (Conjecture 33).** Terminal extremes are directed by the limiting low-zero chaos measure, with an explicit self-averaging versus Cox criterion.

34. **Nonlinear spectral response calculus (Conjecture 34).** Low-zero and exceptional-zero perturbations pass through first-arrival statistics by universal Volterra response operators.

35. **Local-information capacity of odd class groups (Conjecture 35).** Cohen–Lenstra independence has a sharp two-resource boundary governed by cell entropy and conductor complexity.

36. **Kummer–Haar law on relation tori (Conjecture 36).** Saturated multiplicative relations give the exact horizontal support and Haar law of Fermat-quotient vectors.

37. **Rank-dimensional finite-logarithm large sieve (Conjecture 37).** A positive power range of frequencies obeys a large sieve whose dual dimension is saturated rank.

38. **Mesoscopic-to-lattice shrinking-target transition (Conjecture 38).** Haar universality persists for growing targets, while bounded lattice targets acquire a separate arithmetic regulator intensity.

39. **Global-lattice $$p$$-adic regulator-matrix law (Conjecture 39).** A fixed integral Galois-relation lattice controls horizontal regulator matrices and their determinantal rare events.

40. **Functorial horizontal logarithms on tori (Conjecture 40).** A finitely generated global subgroup of a torus has a functorial matrix-valued finite-logarithm Haar law.

41. **Entropy–conductor profile of arboreal resolution (Conjecture 41).** Exact class-measure entropy and Artin-conductor profiles determine observable depth and finite-index shifts.

42. **Arboreal family large sieve and cumulant independence (Conjecture 42).** Growing preimage quotients satisfy square-root trace bounds and higher connected Frobenius factorization over parameters.

43. **Coloured dynatomic Galois-factor process (Conjecture 43).** Exact-period components generate independent coloured, Frobenius-marked factor processes, with growing-degree support restrictions.

44. **Complexity-uniform primitive valuation process (Conjecture 44).** The complete primitive valuation vector has an adelic product law under an explicit height–discriminant complexity regime and uniform squarefull tails.

45. **Divisor-sensitive dynamical gcd classification (Conjecture 45).** Positive normalized gcd height is exactly eventual entry into a periodic curve carrying a shared effective component of the two coordinate divisors.

46. **Frobenius-marked Poisson–Dirichlet process (Conjecture 46).** Macroscopic polynomial-value factors carry fixed-point-size-biased Galois marks.

47. **Three-scale polynomial factorization (Conjecture 47).** Small valuations, mesoscopic scale-invariant factors, and macroscopic marked factors form one conservation-corrected product structure.

48. **Adelic Gibbs gluing for reducible values (Conjecture 48).** Reducible polynomial factor processes are an archimedean–$$p$$-adic Gibbs mixture of independent component processes.

49. **Full multivariate adelic saddle law (Conjecture 49).** Joint smoothness is governed by a complete joint Perron action, saddle displacement, and Hessian, not a scalar Euler correction.

50. **Buchstab–Bateman–Horn component flow (Conjecture 50).** Rough prime, semiprime, and higher-almost-prime polynomial values follow universal Buchstab components with Galois marks.


## Abstract

We state fifty conjectures in elementary and analytic number theory in two parts. The twenty-five conjectures of Part I are each derived from the local–global random model of the primes: Cramér’s model corrected by Hardy–Littlewood singular series, with Bateman–Horn as the organizing framework and Borel–Cantelli accounting for sparse events. Each statement is calibrated to the strongest form the heuristic supports. Every computable constant is computed from its definition, with local admissibility checked for every constant computed; every statement was tested against exact counts (probable-prime counts, so labelled, where the integers involved exceed the deterministic certification range), with success measured by the *shape* of agreement (predicted constant, square-root residuals, no drift) rather than by the size of the range searched. The contributions include: a prime-power contamination calculus for pattern races—twin races modulo $$5$$ and $$8$$ driven by the pairs $$(q^2-2,q^2)$$, cousin, sexy-pair, and triplet predictions derived from the calculus before testing, a Goldbach lane race with a verified internal null lane, a Stern-representation lane race whose null classes are provable by direct congruence, and an algebraic null control; the measured sub-diffusivity of balanced races (universal negative step correlations tied to the Lemke Oliver–Soundararajan repulsion); canonical ordering deficits for least primes in progressions and for least Goldbach summands; derived covariance kernels for moving-window residual fields, with the diagonal deficit reduced to a pinned singular-series average whose growth already exceeds the single-prime Montgomery–Soundararajan term; distribution laws for the constants of the quadratic-pair and cubic-shift families, with exact mean-value lemmas; an entanglement-aware local-global law for $$n^2+2^n$$ with an exact-rational CRT factorization; a boundary trichotomy for polynomial ladders; a multibase subtorus law for Fermat quotients; and singular-series waiting-time refinements for first prime gaps. Every statement was checked against the literature by an independent search, with novelty labelled conservatively: statements already known in essence are attributed and kept *inside* the conjecture whose content they calibrate, since those benchmarks are what make the derived constants credible. Every falsifiable-by-instance statement was then stress-tested computationally well beyond its original range, and every constant was recomputed independently from its definition. Part II adds twenty-five structural conjectures in five programmes—connected prime-pattern fields, arithmetic first-arrival fields and class groups, finite logarithms and algebraic tori, arboreal arithmetic dynamics, and adelic factorization processes—each introducing a canonical operator, process, invariant, classification, or phase boundary, with its mechanism, nearest literature boundary, first decisive theorem, and failure mode.

## 1. Introduction

A good conjecture in the theory of numbers is not merely a statement that has resisted counterexample. It is the *prediction of a model*: the assertion that the primes, beyond their local structure, behave like a random set of density $$1/\log n$$. The discipline this imposes is exacting. A conjecture worth stating should (i) survive every congruence and size obstruction; (ii) come with a quantitative asymptotic whose constant is derived, not fitted; (iii) demand exactly the fluctuations the model earns—square-root noise with logarithmic corrections—and no fewer (the Mertens conjecture died of demanding fewer); (iv) sit inside the standard hierarchy of conjectures (Hardy–Littlewood $$k$$-tuples $$\subset$$ Schinzel’s Hypothesis H $$\subset$$ Bateman–Horn), so that its failure would propagate; and (v) be falsifiable instance-by-instance by computation. Numerical range is the least important column in the ledger: most deep phenomena drift at the rate $$\log\log x$$, and $$\log\log 10^{18}\approx 3.7$$, so verification “to $$10^{18}$$” is weak evidence by itself. What persuades is the *shape* of the agreement—a count that tracks a derived constant through several decades with residuals that look like noise.

The twenty-five statements of Part I are built to those specifications and are presented in three sections: the principal conjectures (numbers 1–9), family laws and second-order refinements (numbers 10–17), and instances and structural companions (numbers 18–25). Part II adds twenty-five structural conjectures organized by mechanism into five programmes, numbered 26 to 50. The material they draw on—Bateman–Horn systems, barely-divergent sparse sequences, representation problems with Borel–Cantelli accounting, and statistical laws of the prime sequence—runs through all three. Section 6 reports the stress tests and the independent recomputation of every constant.

One structural lesson organizes several of the statements below. A probability model integrates over density, and is therefore blind to algebraic families of density zero; the admissibility clause, checked at every prime for every system, is what repairs that blindness. The cubes inside the representation problem $$n=p+k^3$$ (Theorem 1) are the sharpest instance: they obstruct the problem outright while contributing nothing to any Borel–Cantelli sum taken over all $$n$$. This is the classical lesson of admissibility, and it is why the statements below separate what is provable by congruence or factorization from what the probabilistic accounting supplies.

Three checks stand behind every statement, and §6 reports their outcomes. First, an independent literature search at neighbourhood depth—defining objects, derived sequences, OEIS comments, and the abstracts and bodies of near-neighbour papers, read rather than skimmed from search summaries—establishes what is already known. Where a statement exists in essence it is attributed and labelled: some verbatim (Dubner’s twin-sum conjecture, the Stern list for $$p+2k^2$$, Caldwell–Gallot’s $$\mathrm{e}^{\gamma}\log N$$ laws), one with an exact constant catalogued as an OEIS entry (A188596), and the rest attributed accordingly. No such statement stands as a conjecture on its own; each is retained *inside* the conjecture whose content it calibrates, restated in our uniform framework and re-verified at our bounds. Second, every falsifiable-by-instance statement was verified against exact counts and then re-tested well past its original bound, the computation being designed as an attempt at refutation rather than at confirmation. Third, constants and counts were recomputed from the definitions alone by independent implementations developed separately from the primary computation. Our novelty policy throughout is conservative: where priority is uncertain we attribute rather than claim.

### Taxonomy: our contribution and its calibration layer

One criterion governs the taxonomy. An unrecorded specialization of Bateman–Horn is analogous to evaluating a classical special function at a new argument—worthwhile as data, but not a new conjecture in the conceptual sense; no conjecture’s contribution is a bare specialization, and the taxonomy is two-layered *within* each one. The *calibration layer*—the previously-known statements this paper begins from (Dubner’s conjectures, the Stern list, the Caldwell–Gallot laws, Martin’s refined Goldbach, Kourbatov’s record framework, the classical single instances of each family)—appears as attributed remarks inside the conjectures, each with its derived constant re-verified at our bounds; membership in the standard hierarchy of conjectures is itself a virtue, and the calibration layer is what makes the new constants credible. Our own contribution is graded as follows: mechanism-level content (the contamination calculus 1(v) with its instances 18, 19, 14, 12, 1, 4; the ordering deficits 5, 3; race sub-diffusivity 9; the entanglement law 6); derived second-order and distributional laws (10, 15, 2, 8(ii), 11(iii), 13, 7(iv), 16(ii)); and structural classifications (23, 25, 24, 20(i), 21(i), 22)—with framework attributions stated where an instance lives inside someone else’s theory (Kowalski’s for 15(ii), Montgomery–Soundararajan’s for 2 and 13). Every statement was novelty-searched at neighbourhood depth and verified at production scale. We regard the prime-power contamination calculus (Conjecture 1(v)) and its mechanism family—1 and 4, the fresh cousin-race predictions it generated, and the negative control 14—together with Conjecture 3(ii) and the derived covariance kernels of 8(ii) and 16(ii) as the paper’s core, joined by 13 and 23; Conjectures 20, 6 and 11 carry open modelling questions flagged in place.

One tagging convention runs through every statement below: clauses marked [theorem] or “elementary” are proved; clauses marked “conditional proposition” follow from the hypotheses stated with them; the remaining clauses are conjectures; and open questions are labelled as such and are not counted among the fifty conjectures.

### Computational-check standards

All counts below are exact (sieves; deterministic Miller–Rabin for $$n<3.3\times10^{24}$$; Baillie–PSW beyond, flagged as such). Every comparison reports the Poisson-normalized residual $$z=(\mathrm{obs}-\mathrm{pred})/\sqrt{\mathrm{pred}}$$. Every quoted $$z$$-score is such a residual and is used *descriptively*: where the counts compared are correlated, overlapping, or examined after selection, these residuals are not calibrated tail probabilities, and no significance claim in this paper rests on them. For sparse counts the cumulative comparison is contaminated at small $$x$$ by the phantom mass of the main-term integral near its lower limit; in those cases we also report per-decade increments, which are clean. Constants are computed by truncated Euler products with the truncation wobble (difference between cutoffs) reported as an error bar; for conditionally convergent quadratic and cubic products this wobble, not the last digit, is the effective precision.

Primality certification is stratified, and every count inherits the stratum of the integers it involves. Primality of every integer below $$3.3\times10^{24}$$ is decided *deterministically*, by fixed-base Miller–Rabin over a witness set verified for that range. For larger integers the classification is made by the Baillie–PSW test, and is a *probable-prime* classification, not a proof: no Baillie–PSW pseudoprime is known—and none exists below $$2^{64}$$, where the test is therefore deterministic—but their nonexistence is unproved. Consequently every count involving such integers is a probable-prime count, and is labelled as one wherever it appears. The computations affected are the factorial scans of Conjectures 21 and 2 ($$n!\pm1$$ for $$n$$ beyond about $$26$$), the $$n^2+2^n$$ scan of Conjecture 6 beyond $$n\approx80$$, the quartic values of the cyclotomic chain of Conjecture 24 beyond $$p\approx2\times10^6$$, and the Fibonacci–Lucas values of Conjecture 20 at all but the smallest indices. Every other count below—sieve censuses, race counts, window fields, and the inputs to every constant—lies entirely inside the deterministic range.

## 2. Notation

$$p,q$$ denote primes; $$\gamma$$ is Euler’s constant, $$\mathrm{e}^{\gamma}=1.781072\ldots$$; $$\varphi$$ is Euler’s totient; $$\phi=(1+\sqrt5)/2$$; $$F_n$$ the Fibonacci numbers; $$p\#$$ the primorial. For irreducible $$f_1,\dots,f_k\in\mathbb Z[x]$$ with positive leading coefficients, the Bateman–Horn singular series is

$$
C(f_1,\dots,f_k)\;=\;\prod_{p}\frac{1-\omega(p)/p}{(1-1/p)^{k}},
\qquad
\omega(p)=\#\{n \bmod p:\ p\mid f_1(n)\cdots f_k(n)\},
$$

and the corresponding main term is

$$
I(N)\;=\;\int_{2}^{N}\frac{dt}{\prod_{i}\log f_i(t)},
$$

which absorbs the usual $$1/\prod_i \deg f_i$$. The Bateman–Horn conjecture [2] asserts $$\#\{n\le N: \text{all } f_i(n) \text{ prime}\}\sim C\cdot I(N)$$ whenever $$C\neq0$$; each Bateman–Horn conjecture below is an instance with its constant evaluated. For nonlinear systems the product converges only conditionally; throughout, it is taken in the canonical ordering of increasing primes, in which convergence follows from the equidistribution of $$\omega(p)$$ about its Chebotarev mean. Our numerical truncation wobble is an error bar for this canonically ordered product. We write $$\mathrm{Li}_k(x)=\int_2^x(\log t)^{-k}\,dt$$. The twin singular series is $$\mathfrak{S}(d)=2C_2\prod_{p\mid d,\,p>2}\frac{p-1}{p-2}$$ for even $$d$$, with $$2C_2=1.3203236\ldots$$; the Goldbach series $$\mathfrak{S}(n)$$ is the same product over odd $$p\mid n$$.

Eight of the conjectures below are built over the Bateman–Horn move—choose an admissible system, compute its singular series, state the count—but none is a bare instance of it: 10 and 15 are family laws with derived constant distributions, 23 and 25 carry structural classifications, 24 is a searched chain, and 18, 19, 14 are contamination-calculus predictions (two fresh races and the negative control) whose mechanism is the contamination calculus of Conjecture 1(v). Each carries its classical calibration instance as an attributed remark. The heuristic is uniform, so we give it once. Model the primality of the values $$f_i(n)$$ as independent events of probability $$1/\log f_i(n)$$, corrected by the factor $$(1-\omega(p)/p)/(1-1/p)^k$$ at each prime $$p$$ to account for the joint local behaviour; multiplying the corrections and integrating gives $$C\cdot I(N)$$.

For locally integrable $$F$$ we write $$\mathcal{M}_x(F)=\frac1{\log x}\int_2^x F(t)\,\frac{dt}t$$ for the logarithmic mean; all race conjectures below state their drift and null clauses through $$\mathcal{M}_x$$, so that “no persistent leader” and “systematic surplus” are claims about a defined functional rather than about pointwise behaviour. Drift clauses are stated at the *drift scale*—for a pair race, $$\mathcal{M}_x(D(t)\log^2t/\sqrt t)$$ converging to an explicit constant—never as $$\mathcal{M}_x((D-T)/\sqrt\pi)\to0$$, which is vacuous for the drift coefficient (both $$T/\sqrt\pi$$ and its multiples have logarithmic mean $$\to0$$). Convergence of $$\mathcal{M}_x$$ at drift scale is itself part of each such conjecture: a pure random-walk fluctuation model would make these means divergent in variance, so their convergence encodes the Rubinstein–Sarnak-type almost-periodicity that the zero-oscillation hypothesis names.

Admissibility ($$\omega(p)<p$$ for all $$p$$) is checked for every constant computed. The natural-looking pair $$\{n^2+n+1,\ n^2+n+3\}$$ has $$\omega(3)=3$$ and is rejected; the $$k=4$$ branch of Conjecture 25 and the naive iterated chain behind Conjecture 24 are inadmissible for the same reason, and both exclusions are part of the statements.

## 3. Principal conjectures

The twin-race statement is split into its provable algebraic core and its conjectural clauses, stated through the logarithmic-mean functional $$\mathcal{M}_x$$ of the notation section.

**Lemma 1** *(Orientation elimination and class assignment).*

In $$\psi_2(x)=\sum_{n\le x}\Lambda(n)\Lambda(n+2)$$, the total contribution of terms in which $$n$$ or $$n+2$$ is a proper prime power is, apart from $$O(x^{1/3}\log^2 x)$$ from cubes and higher powers, carried entirely by the patterns $$(q^2-2,\,q^2)$$ with $$q$$ prime and $$q^2-2$$ prime: the mirror pattern $$(q^2,\,q^2+2)$$ is annihilated by $$3\mid q^2+2$$ for every prime $$q>3$$. Moreover, for every prime $$q\neq5$$, $$q^2-2\equiv2$$ or $$4\pmod 5$$ (never $$1$$), and for every odd $$q$$, $$q^2-2\equiv7\pmod8$$. (Two bounded exceptions: at $$q=5$$ the term $$(23,25)$$ lands outside the twin-start classes altogether, and at $$q=3$$ the mirror term $$(9,11)$$ survives, the annihilation beginning only at $$q>3$$; each is a single term, absorbed in the bounded error.)

The proof is elementary (squares mod $$3$$, $$5$$, $$8$$; the prime-power count). The lemma orients the race: prime-square contamination can enter only specific residue classes, and the model converts that into a drift prediction for the *unweighted* twin counts.

**Conjecture 1** *(Twin races modulo 5 and 8, and the prime-power contamination calculus; apparently new).*

Twin starts $$p>5$$ lie in classes $$p\equiv1,2,4\pmod5$$. Let $$D_1(x)=\pi_t(x;5,1)-\tfrac12\bigl(\pi_t(x;5,2)+\pi_t(x;5,4)\bigr)$$ and

$$
T(x)\;=\;\frac1{2\log^2x}
\sum_{\substack{q\le\sqrt x\\ q^2-2\ \mathrm{prime}}}
\log q\,\log(q^2-2),
$$

Then: *(i)* [drift law, at drift-scale normalization] the clause asserts two sub-claims, labelled separately because they can fail independently. *(i-a)* [mechanism] class $$1$$ carries the systematic surplus $$T$$: one has the decomposition $$D_1(t)=T(t)+R(t)$$ in which the remainder $$R$$ carries no deterministic component at the drift scale, so that the entire drift-scale deterministic content of $$D_1$$ is the contamination term and its coefficient is thereby identified. *(i-b)* [averaging] at the drift-scale normalization the remainder averages away:

$$
\mathcal{M}_x\!\left(\frac{R(t)\,\log^2t}{\sqrt t}\right)\longrightarrow0,
\qquad\text{equivalently}\qquad
\mathcal{M}_x\!\left(\frac{D_1(t)\,\log^2t}{\sqrt t}\right)
\;\longrightarrow\;c_T,
$$

where

$$
c_T\;:=\;\lim_{x\to\infty}\frac{T(x)\log^2x}{\sqrt x}
\;=\;\tfrac12\,C(x,\,x^2-2)
$$

is the half of the Bateman–Horn constant of the pair $$(q,\,q^2-2)$$ (the weighted census sum is $$\sim C\sqrt x$$, so the limit exists and is explicit). A normalization at the noise scale, $$\mathcal{M}_x((D_1-T)/\sqrt{\pi_t})\to0$$, would be *vacuous* for the coefficient of (i-a): since $$T/\sqrt{\pi_t}\asymp1/\log t$$, one has $$\mathcal{M}_x(T/\sqrt{\pi_t})\asymp\log\log x/\log x\to0$$, so the condition holds with $$T$$ replaced by $$0$$, $$2T$$, or any fixed multiple, and does not express “exactly the removed mass.” The statement therefore normalizes at the *drift* scale, where the claimed limit is a nonzero constant. Convergence at this normalization is a Rubinstein–Sarnak-type regularity assertion: under a pure random-walk model the logarithmic mean would not converge (its variance grows like $$\log x$$), so (i-b) asserts almost-periodic structure for the twin race and is the precise content of the zero-oscillation hypothesis, while (i-a) is what fixes the limit at $$c_T$$ rather than $$0$$ or $$2c_T$$, and is the calculus. The convergence asserted in (i-b) selects the rigid branch of the dichotomy registered at Conjecture 9(iii); the two statements stand or fall together at drift scale; *(ii)* [zero deterministic drift in the symmetric differences] the symmetric classes carry no deterministic term *at the same normalization*: $$\mathcal{M}_x\bigl((\pi_t(\cdot;5,2)-\pi_t(\cdot;5,4))\log^2t/\sqrt t\bigr)\to0$$, and likewise for each of the three pairwise differences among classes $$\{1,3,5\}$$ mod $$8$$ in clause (iv)—now a statement distinct from (i), since at drift scale “zero” and “$$c_T$$” are different limits; *(iii)* [sign density, conditional] conditional on the Gaussian fluctuation model for the normalized remainder in (i)–(ii), the logarithmic density of $$\{D_1>0\}$$ exists and equals $$\tfrac12$$, approached from above with a finite-$$x$$ excess of order $$\log\log x/\log x$$: the pointwise drift-to-noise ratio is $$T/\sqrt{\pi_t}\asymp1/\log t$$, and its *logarithmic average* $$\mathcal{M}_x(1/\log t)\sim\log\log x/\log x$$ carries an extra $$\log\log$$ (the scale is not $$1/\log x$$). In contrast to Chebyshev’s races, the twin race has no persistent leader; *(iv)* [mod-8 companion] since $$q^2-2\equiv7\pmod8$$ always (Lemma 1), the *entire* deterministic term falls on the single class $$7\pmod 8$$: with $$D_7(x)=\tfrac13\sum_{a\in\{1,3,5\}}\pi_t(x;8,a)-\pi_t(x;8,7)$$,

$$
\mathcal{M}_x\!\left(\frac{D_7(t)\,\log^2t}{\sqrt t}\right)
\longrightarrow2c_T
$$

(twice the mod-5 constant, undiluted—at this normalization the factor $$2$$ is a falsifiable prediction, the mechanism and averaging claims separating here exactly as in (i-a)–(i-b)), while classes $$1,3,5$$ are mutually symmetric. The mod-5 and mod-8 races are two projections of one mechanism, so their joint behaviour is a family test in the sense of the shape-of-agreement criterion; *(v)* [contamination calculus for balanced races] for a pattern $$(n,n+d)$$ and modulus $$m$$, call the race *balanced* if the prime-prime singular series is identical across the competing residue classes (as CRT gives for the classes compared in (i)–(iv)) and no mechanism other than prime powers contributes at the $$\sqrt x$$ scale under the zero-oscillation hypothesis. For balanced races the deterministic drift vector is computed by one operator. Define the *contamination operator*

$$
\mathcal C_{d,m}(a;x)\;=\;
\sum_{\text{orientations }o\in\{(q^2-d,q^2),\,(q^2,q^2+d)\}}
\ \sum_{\substack{q\le\sqrt x,\ o\ \text{prime-compatible}\\
\mathrm{start}(o)\equiv a\ (m)}}
\Lambda(q^2)\,\Lambda(\text{prime member of }o),
$$

where prime-compatible means the non-square member is prime and no fixed prime annihilates the orientation. The provable layer is the orientation census and class assignment (which $$o$$ survive, and where their starts land—Lemma 1 and its analogues); the conjectural layer is the transfer: the unweighted class counts are depressed by $$\mathcal C_{d,m}(a;x)/\log^2x$$ relative to the clean classes, in the drift-scale limiting-log-mean sense of (i), with the mechanism and averaging claims separated as in (i-a)–(i-b)—for each class $$a$$, the deficit obeys $$\mathcal{M}_x\bigl(\mathrm{deficit}_a(t)\log^2t/\sqrt t\bigr)\to c(a):=\lim\mathcal C_{d,m}(a;x)/\sqrt x$$, an explicit Bateman–Horn constant per class, so every coefficient in the vector is identified—i.e. “exactly the removed mass,” which requires the weighted identity, partial summation uniform in classes, higher-power bounds (exponents $$r\ge3$$ contribute $$O(x^{1/3+\varepsilon})$$ against the operator’s $$\asymp\sqrt x$$ and are negligible—the one easy layer of the transfer), and the zero-oscillation hypothesis, and is the calculus’s single analytic conjecture rather than a rule. The drift is $$\asymp\sqrt x/\log^2x$$ against a count fluctuation $$\asymp\sqrt x/\log x$$, i.e. smaller by $$1/\log x$$ in standard-deviation units at every height—so the calculus predicts occupation biases under long logarithmic aggregation, never a fixed nonzero standardized mean, and every verification in this family is designed around that fact. (Races with unequal primary constants, or with interfering orientations beyond those enumerated, are outside the calculus until those terms are separated.) In particular, for the cousin pattern $$d=4$$ the calculus makes two predictions with no free choices: the orientation $$(q^2-4,q^2)$$ is dead apart from a single term ($$q^2-4=(q-2)(q+2)$$ is composite for $$q>3$$, while at $$q=3$$ the value $$5$$ is prime: one bounded term, whose start $$5$$ lies outside the mod-$$5$$ cousin classes and contributes one bounded term to class $$5$$ mod $$8$$), the orientation $$(q^2,q^2+4)$$ survives (no prime annihilates it), $$q^2+4$$ prime forces $$q\equiv\pm2\pmod5$$ for $$q\neq5$$ (at $$q=5$$ the value $$29$$ is prime, but the start $$25\equiv0\pmod5$$ lies outside the cousin start classes $$\{2,3,4\}$$), so the contaminated cousin-start class is $$4\pmod 5$$ (of $$\{2,3,4\}$$) and—since $$q^2\equiv1\pmod8$$—the class $$1\pmod 8$$ (of $$\{1,3,5,7\}$$): both deficits converge, in the drift-scale limiting-log-mean sense of (i)–(ii), to $$c^{\mathrm c}=\lim_{x\to\infty}T^{\mathrm c}(x)\log^2x/\sqrt x$$, the Bateman–Horn constant of the pair $$(q,\,q^2+4)$$, where $$T^{\mathrm c}(x)=\frac1{\log^2x}\sum_{q\le\sqrt x,\ q\neq5,\ q^2+4\ \mathrm{prime}}\log q\,\log(q^2+4)$$.

Clause (v) answers the structural question of what general principle the mod-5 and mod-8 races instantiate, and the cousin predictions it yields were derived first and tested second. At $$x=10^9$$ the predicted drift is far inside the noise ($$T^{\mathrm c}/\sqrt{\pi_{\mathrm c}}\approx0.09$$, as the $$1/\log x$$ law requires), so the sharp statistic is leadership under logarithmic averaging, calibrated against the null of Conjecture 14(ii) (log-occupation $$\tfrac12$$ with Gaussian spread $$\sqrt{\log2/\log x}\approx0.18$$ at $$10^9$$, at the occupation-fraction constant): the class-4 deficit race led on the predicted side with log-density $$0.99$$ ($$+2.7$$ null standard deviations), the class-1 mod-8 race with $$0.92$$ ($$+2.3$$), both signs agreeing with the prediction, while the control differences among uncontaminated classes stayed within one noise unit of zero in log-mean. This is moderately strong directional evidence—two independent projections each between two and three null standard deviations on the predicted side—though the races share underlying primes and the two statistics are positively correlated, so we do not call it sharp confirmation; the family now has five projections of one mechanism (twin mod 5, twin mod 8, cousin mod 5, cousin mod 8, and the Goldbach lanes of Conjecture 4) plus two algebraic nulls (Conjecture 14 and the dead cousin orientation), which is the shape-of-agreement standard applied to the calculus itself.

A limiting sign density strictly between $$\tfrac12$$ and $$1$$ would be inconsistent with the scale analysis: when drift/noise $$\to0$$, a Gaussian model forces the sign density to $$\tfrac12$$, and a nontrivial limiting density would require a persistent normalized bias that no mechanism here produces. The fluctuation in (iv) is not written as $$O^{*}(\sqrt{\pi_t})$$, since $$O$$-notation asserts a provable bound where only a conjectural fluctuation statement is meant. Two model assumptions remain open and are stated as such: the passage from the $$\Lambda$$-weighted count to unweighted twin counts is a partial-summation argument whose error terms need writing out (higher prime powers are disposed of by Lemma 1); and the *zero-oscillation caveat*—the drift law treats the oscillatory explicit-formula contributions to class differences as having vanishing logarithmic mean, the exact analogue of the Rubinstein–Sarnak GRH-plus-linear-independence framework [6], and a conspiracy among hypothetical zeros could in principle mimic or cancel part of the drift; clause (i) is conjectured on the standard side of that hypothesis.

The mechanism is the twin analogue of the classical explanation of Chebyshev’s bias: prime-square terms contaminate the classes that can contain them. (Biases of twin primes in residue classes have been studied before—Sahoo [27] for the mod-$$4$$ race, and [28] for prime pairs versus isolated primes—but we could find no prior statement of the mod-$$5$$ race, the $$(q^2-2,q^2)$$ mechanism, or the quantified surplus below.) Mod $$3$$ kills the pattern $$(q^2,q^2+2)$$ outright, an amusing local accident that halves the mechanism and concentrates the surplus entirely on class $$1$$, as a mod-$$3$$ computation confirms. Data to $$4\cdot10^9$$: class counts $$(3980017,\ 3982505,\ 3981922)$$, $$D_1$$ within one noise unit of $$T$$ throughout, no persistent leader, and the control race $$\pi_{t,2}-\pi_{t,4}$$ wandering like a fair coin. Mod-8 data to $$10^9$$: class counts $$(856684,\ 855807,\ 856046,\ 855967)$$ for $$a=1,3,5,7$$; $$D_7=+212$$ at $$10^9$$ against predicted $$T=+254$$ with noise $${\sim}1068$$, positive through most of the range (log-density $$0.775$$), and the three pairwise $$\{1,3,5\}$$ controls all within one noise unit of zero—the two projections of the mechanism behave coherently, none of it provable at present.

**Conjecture 2** *(The pair-level Montgomery–Soundararajan reduction; apparently new).*

For the window field of Conjecture 8(ii), the diagonal variance of the twin-pair count reduces to a *pinned* singular-series average. With $$R(h)=C_4(0,2,h,h+2)/\mathfrak{S}(2)^2$$ for $$h\ge1$$ (zero when the offset set is degenerate or inadmissible—all odd $$h$$, and $$h=2$$ since $$\{0,2,4\}$$ dies at $$3$$; consecutive twin pairs cannot overlap beyond $$(3,5,7)$$, so no overlap term exists) and

$$
G(H)\;=\;\sum_{1\le h\le H}\Bigl(1-\frac hH\Bigr)\bigl(R(h)-1\bigr),
$$

the derived identity is

$$
\frac{\operatorname{Var}_t\,\pi_2(t;H)}{\mathbb E_t\,\pi_2(t;H)}
\;=\;1+\frac{\mathfrak{S}(2)\,\bigl(2G(H)-1\bigr)}{\log^2x}
+o\!\Bigl(\frac1{\log^2 x}\Bigr):
$$

with $$p=\mathfrak{S}(2)/\log^2x$$ the per-site intensity, the variance is $$Hp(1-p)+2p^2HG(H)$$, so $$\operatorname{Var}/\mathbb E=1-p+2pG(H)$$ —the Bernoulli diagonal term $$-p=-\mathfrak{S}(2)/\log^2x$$ is of exactly the order of the claimed error and cannot be dropped (it is the same diagonal that, in the single-prime case, merges into Montgomery–Soundararajan’s constant $$\gamma+\log2\pi-1$$). With that term retained, the entire deficit left open at Conjecture 8(ii) is the single computable function $$G$$ plus the explicit Bernoulli correction—the pair analogue of Montgomery–Soundararajan’s reduction of the prime-count variance to $$\sum_{h\le H}\mathfrak{S}(h)(H-h)$$ [19]. Clause (i) is a *conditional proposition*, not an independent conjecture: given quantitative Hardy–Littlewood for $$4$$-tuples, the reduction follows. The conjectural clause is (ii): $$-G(H)/\log H$$ diverges —the pinned average grows strictly faster than the single-prime secondary term $$\tfrac12(\log H+\gamma+\log2\pi-1)$$, so pair counts in windows are more sub-Poisson than prime counts—with the caveat that data to $$H=3000$$ cannot distinguish divergence from a pure $$\log$$ with a large constant (nor $$c\log H\log\log H$$ from $$(\log H)^\alpha$$): what the computation *establishes* is only that the local slope exceeds the single-prime value sevenfold across the computable range; the divergence and its exact form are registered, not evidenced beyond that.

The pinning leaves the local densities in exact balance. At every odd prime $$p$$ the relative local factor of $$R(h)$$ takes the value $$p/(p-2)$$ for $$h\equiv0$$, the value $$p(p-3)/(p-2)^2$$ for $$h\equiv\pm2$$, and the value $$p(p-4)/(p-2)^2$$ otherwise, and their exact average over $$h$$ mod $$p$$ equals $$1$$, since $$(p-2)+2(p-3)+(p-3)(p-4)=(p-2)^2$$. Any persistent negativity of $$G(H)$$ is therefore not a first-order local-density effect but a global correlation effect across primes, which is what makes its growth rate delicate.

$$G$$ was computed exactly to $$H=3000$$ ($$4$$-tuple constants by Euler products to $$2\times10^4$$): $$G(3000)=-20.9$$, with local logarithmic slope increasing from $$3.4$$ to $$3.7$$ across the range—seven times the single-prime slope $$\tfrac12$$, consistent with (ii) over the computable range while leaving the limiting form undetermined (a quadratic-in-$$\log$$ fit is unstable on subranges). The window measurement brackets the extrapolation: at $$H=10^5$$, $$x\in[10^8,2\times10^8]$$ the pure-log form predicts $$\operatorname{Var}/\mathbb E=0.97$$, the $$\log^2$$ form $$0.72$$, and the observed value is $$0.815$$—intermediate growth, exactly where the computable range points. (Caldwell–Gallot’s factorial-prime law $$\#\{n\le N: n!+1 \text{ prime}\}\sim\mathrm{e}^{\gamma}\log N$$ [4], the divergent single-sided companion of Conjecture 21, is included as an attributed calibration benchmark: $$15$$ primes to $$n=700$$ against $$11.7$$, $$z=+0.98$$—a probable-prime count, $$n!+1$$ leaving the deterministic range at $$n\approx26$$.)

*Computational checks.* The pinned singular-series computation and window comparison are reported at the statement; its factorial benchmark stands at $$15$$ primes with $$n\le700$$ against $$11.7$$ ($$z=+0.98$$; a probable-prime count for $$n$$ beyond about $$26$$), the divergent single-sided companion of Conjecture 21’s convergent side.

**Conjecture 3** *(Least primes in progressions; part (i) previously stated [20, 21, 30, 29], part (ii) apparently new).*

Let $$p(a,q)$$ be the least prime $$\equiv a\pmod q$$ and $$U(a,q)=\mathrm{Li}(p(a,q))/\varphi(q)$$. Then: *(i)* $$U\Rightarrow\mathrm{Exp}(1)$$ marginally as $$q\to\infty$$; and, under the additional hypothesis that the class processes are asymptotically jointly independent in the extreme-value sense (which marginal convergence alone does not supply), $$\max_a U-H_{\varphi(q)}$$ converges to a Gumbel law ($$H_n=\sum_{k\le n}1/k$$), the order-statistics form of Wagstaff’s $$\max_a p(a,q)\sim\varphi(q)\log^2q$$; *(ii)* [canonical deficit, dyadic-average form] define, with no reference to any control model, $$\Theta(q)=\bigl(1-\mathbb E_a[U(a,q)]\bigr)\log q$$. The conjecture is stated for dyadic averages over prime moduli—pointwise convergence along every prime $$q$$ may be too strong, since arithmetic fluctuations in $$q$$ could persist:

$$
\frac1{\#\{q\in[Q,2Q]\ \text{prime}\}}
\sum_{\substack{Q\le q\le2Q\\ q\ \mathrm{prime}}}\Theta(q)
\;\longrightarrow\;\Theta\;>\;0
\qquad(Q\to\infty).
$$

(The formal claim is model-free: existence and strict positivity of the dyadic-average limit. The stronger reading—that $$\Theta$$ exceeds the discreteness level any parity-aware control produces—is the diagnostic layer below, not part of the display, since a control constant has no place in a model-free statement.) The limiting *distribution* of $$\Theta(q)$$ over the dyadic block is left open, and in particular we do *not* assert $$\operatorname{sd}(\Theta(q))\to0$$: fluctuations driven by the arithmetic of $$q$$ and of $$q-1$$ (through the singular-series pair terms $$\mathfrak{S}(kq)$$ and the class structure mod $$q$$) may well persist at bounded size, so $$\Theta(q)$$ need not concentrate around its dyadic mean.

The decomposition $$\Theta(q)=\theta_{\mathrm{disc}}(q)+\theta_{\mathrm{corr}}(q)$$ is a *diagnostic*, not a canonical invariant: its two parts move if the benchmark moves, and clause (ii) is therefore stated through the model-free $$\Theta(q)$$ alone. The named benchmark (the parity-aware Cramér–Bernoulli control: candidates $$a,\,a+q,\,a+2q,\dots$$ independently “prime” with hazard $$h_i=(q/\varphi(q))\cdot s_i/\log(a+iq)$$, $$s_i=2$$ for odd candidates and $$0$$ for even, matching density and parity) defines $$\theta_{\mathrm{disc}}(q)=(1-\mathbb E_a[U^{\mathrm{model}}])\log q$$ exactly for each $$q$$, and $$\theta_{\mathrm{corr}}:=\Theta-\theta_{\mathrm{disc}}$$ is the part of the measured deficit that the control cannot produce; it is this diagnostic that localizes the anomaly in the *ordering* of the primes (Remark 1). Measured on prime moduli $$q\in[1500,6000]$$: $$\Theta=1.671\pm0.009$$, of which the control accounts for $$0.847$$.

One further deterministic baseline must be subtracted before any of the residue is called an anomaly: for prime $$q$$, the primes $$p<q$$ occupy *distinct* classes mod $$q$$—an injective initial phase that no exchangeable allocation reproduces. Its size has a closed form in index time (where $$\mathrm{Li}(p_i)\approx i$$, so $$U$$ is the first-hit index over $$\varphi$$): forcing the first $$\pi(q)$$ arrivals to be collision-free and leaving the rest exchangeable gives $$\mathbb E[U]=1-\pi(q)^2/2\varphi^2+O(\pi(q)/\varphi^2)$$, hence

$$
\Theta_{\mathrm{inj}}(q)
\;=\;\frac{\pi(q)^2}{2\varphi(q)^2}\,\log q\;(1+o(1))
\;=\;\frac{1+o(1)}{2\log q},
$$

closed form $$0.092,\ 0.082,\ 0.074$$ at $$q=1499,\ 3001,\ 5987$$, with Monte Carlo agreeing within sampling error and the exchangeable control at $$1.000$$. The injective phase is therefore real but an order of magnitude too small to be the explanation: it accounts for $${\approx}0.08$$ of the measured $$\theta_{\mathrm{corr}}=0.824\pm0.009$$, and carries a $$1/\log q$$ decay that the flat measured values do not show. (One might expect the effect to sit at the full deficit scale, since the *affected-class fraction* is $$\pi(q)/\varphi\asymp1/\log q$$; but the deficit is the affected fraction times the collision probability an exchangeable model would have suffered in that phase, $$\asymp\pi(q)/2\varphi$$, giving $$1/2\log^2q$$ in $$\mathbb E[U]$$, not $$1/\log q$$.) The injective phase is in any case the $$y<q$$ head of the pair-correlation expansion already registered below—collisions require $$q\mid p_2-p_1$$, impossible before $$y=q$$—so subtracting it is the first term of the stated programme, not a rival explanation. The residue $$\theta_{\mathrm{corr}}-\Theta_{\mathrm{inj}} \approx0.74$$ remains the unexplained ordering anomaly.

A derivation route for the deficit, which we adopt as the programme stated here, runs as follows. Let $$V_q(y)$$ be the number of reduced classes mod $$q$$ not yet visited by a prime $$\le y$$; then $$\mathbb E_a[U]=\int_0^\infty \overline{V_q(y_\tau)}/\varphi(q)\, d\tau$$ with the $$\mathrm{Li}$$-time change $$y_\tau$$ defined by $$\mathrm{Li}(y_\tau)=\tau\varphi(q)$$, and inclusion–exclusion expands $$V_q(y)$$ in prime-tuple correlations *within* a class:

$$
\mathbb E\binom{N_a}{2}\ \text{summed over }a
\;=\;\#\{p_1<p_2\le y:\ q\mid p_2-p_1\}
\;\approx\;\sum_{1\le k\le y/q}\mathfrak{S}(kq)\int_2^{y-kq}\frac{dt}{\log t\,\log(t+kq)},
$$

so the first correction to the exchangeable occupancy model is carried by the Hardy–Littlewood singular series of gaps divisible by $$q$$. The truncation is structural, not a convenience: a gap $$kq$$ requires $$p_1\le y-kq$$, so the $$k$$-sum stops at $$y/q$$ and the endpoint-shortened integrals supply the triangular weights, while the untruncated sum $$\sum_{k\ge1}\mathfrak{S}(kq)$$ diverges (the singular series has mean one on average over its argument) and the formally factorized expression $$\mathrm{Li}_2(y)\sum_k\mathfrak{S}(kq)$$ is meaningless. Evaluating this expansion to second order, and comparing it with the measured $$\Theta$$, is the concrete open computation that would either derive the ordering anomaly from pair correlations or prove it lies deeper; either outcome would reduce the mystery of Question 1 by one level.

The stratified experiment behind these numbers separates moduli by factorization type in the matched range $$q\in[1500,6000]$$: over $$40$$ *prime* moduli, $$\theta_{\mathrm{disc}}=0.847$$ (essentially constant across $$q$$) and $$\theta_{\mathrm{corr}}=0.824\pm0.009$$; over $$40$$ *$$7$$-smooth* moduli in the same range, $$\theta_{\mathrm{disc}}=4.32\pm0.22$$ (the large $$q/\varphi(q)$$ hazards make discreteness dominant) while $$\theta_{\mathrm{corr}}=-2.32\pm0.22$$ reverses sign. The comparison with Leung [29] is thereby given its answer-shaped experiment: Leung derives the exponential law under a uniform Hardy–Littlewood hypothesis and reports discrepancies for *smooth* moduli, and our smooth stratum indeed behaves anomalously—but the positive ordering term survives, with small error bars, exactly where smooth-modulus effects cannot reach. Whether $$\theta_{\mathrm{corr}}$$ tends to a constant, and the exact functional form in $$1/\log q$$, remain open: data at $$q\le6000$$ cannot distinguish $$1/\log q$$ from $$(\log\log q)/\log q$$-type refinements—the aggregate $$\theta\approx1.5$$–$$1.9$$ over $$q\in[10^2,6\times10^3]$$, with $$\mathbb E_a[U]$$ bottoming near $$0.737$$ around $$q\approx200$$ and recovering through $$0.776$$ by $$q\approx6000$$, is calibration, not a determination of the form. The averaging family is fixed as: all moduli of the stated type in dyadic ranges of $$q$$, per stratum.

**Remark 1.**

The deficit is reproducible and is *not* an artefact of the time-change: a Cramér pseudo-prime control (independent Bernoulli “primes” with the correct densities and parity) shows roughly half of it—the discreteness of large per-candidate hazards—while the other half vanishes under any reshuffling of the actual prime residues (iid labels, or a random permutation of the true residue sequence, both restore $$\mathbb E[U]=1.00$$). The ordered sequence of primes fills residue classes measurably faster than any exchangeable model, and the stratified experiment above shows the effect is not a smooth-modulus artefact: it is largest and cleanest on prime moduli. We measure $$\theta_{\mathrm{corr}}$$; we cannot yet derive it.

**Conjecture 4** *(The Goldbach lane race; apparently new).*

For $$n\equiv2\pmod4$$ let $$R_1(n)$$, $$R_3(n)$$ be the ordered Goldbach representation counts in the lanes $$p\equiv q\equiv1$$ and $$p\equiv q\equiv3\pmod4$$ (Conjecture 5), and $$D(n)=R_3(n)-R_1(n)$$. Prime-square terms $$n=q^2+p$$ ($$q$$ odd prime) land *exclusively* in the $$(1,1)$$ lane, since $$q^2\equiv1\pmod4$$ and then $$n-q^2\equiv1\pmod4$$ automatically. Consequently the $$(3,3)$$ lane leads on average: with

$$
D_{\mathrm{sys}}(n)\;=\;\frac{2}{\bar\ell(n)}
\sum_{\substack{q \text{ odd prime},\ q\le\sqrt n\\ n-q^2 \text{ prime}}}
\log q\,\log(n-q^2),
\qquad
\bar\ell(n)\;=\;\frac{n-6}{\displaystyle\int_3^{n-3}
\frac{dt}{\log t\,\log(n-t)}},
$$

(the analytic mean of $$\log p\log(n-p)$$ under the lane profile; the empirical lane mean is its estimator). Write $$\mathbb E_x$$ for the average over $$n$$ drawn from $$\{n\equiv2\ (4),\ n\le x\}$$ with weight proportional to $$1/n$$ (the logarithmic sampling measure, now explicit). Then: *(i)* [drift law] $$\mathbb E_x[D-D_{\mathrm{sys}}]=o(\mathbb E_x[D_{\mathrm{sys}}])$$ as $$x\to\infty$$: the $$(3,3)$$ lane leads on average by exactly the square contamination; *(ii)* [weighted mean and internal null lane] $$\mathbb E_x[D_{\mathrm{sys}}]$$ is given by the Hardy–Littlewood (Conjecture H) local model for $$n-q^2$$, whose local factors vary strongly with $$n$$—most drastically at $$p=3$$: for $$n\equiv1\pmod3$$, $$3\mid n-q^2$$ for *every* prime $$q>3$$, so the contamination collapses to a single boundary family, the $$q=3$$ term (when $$n-9$$ is prime): the complementary possibility $$n-q^2=3$$ is empty on this ensemble, since $$n\equiv2\pmod4$$ forces $$n-3\equiv3\pmod4$$, never a square. The family is negligible in logarithmic mean, so the race carries no drift at the systematic scale on the subprogression $$n\equiv10\pmod{12}$$: with the positive comparison scale $$A_G(x):=\mathbb E_x^{(\not\equiv1\,(3))}[D_{\mathrm{sys}}]$$, the logarithmic-ensemble mean of the systematic term over the contaminated lane $$n\not\equiv1\pmod3$$ (a comparison against this subprogression’s own systematic term, which vanishes, would be empty), the claim is $$\mathbb E_x[D]=o\bigl(A_G(x)\bigr)$$ on $$n\equiv10\pmod{12}$$, while the drift concentrates on $$n\not\equiv1\pmod3$$: an internal null lane, predicted by the same mechanism that predicts the lead; *(iii)* [sign density] the per-$$n$$ drift-to-noise ratio $$\kappa(n)=D_{\mathrm{sys}}(n)\big/\sqrt{\mathfrak{S}(n)J(n)}$$ (where $$J(n)=\int_3^{n-3}dt/(\log t\log(n-t))$$, so that $$\mathfrak{S}(n)J(n)$$ is the total ordered representation count) satisfies $$\kappa(n)\asymp c(n)/\log n\to0$$; under the Gaussian fluctuation model the logarithmic density of $$\{D>0\}$$ is therefore $$\tfrac12$$ in the limit, with the finite-$$x$$ sign fraction predicted to be $$\mathbb E_x[\Phi(\kappa)]$$ ($$\Phi$$ the standard normal distribution function)—decaying, but far from $$\tfrac12$$ at any accessible height.

Derivation status: the identity behind $$D_{\mathrm{sys}}$$ is the $$\Lambda$$-weighted lane symmetry minus its prime-power part; the transfer to unweighted counts is a partial-summation argument whose error terms (higher prime powers, which enter only at the $$n^{1/3}$$ scale, and the variation of the weight across the lane) remain to be written out—the same open transfer flagged at Conjecture 1—and clause (iii) inherits the zero-oscillation caveat stated there.

This is the Goldbach-partition analogue of Chebyshev’s bias, produced by the same explicit-formula mechanism as Conjecture 1 but through $$q^2+p$$ patterns rather than twin patterns; the single-sign prediction (every square contamination falls into one lane) makes it cleaner than the classical race. We could find no prior statement. The neighbouring phenomenon for consecutive primes is the Lemke Oliver–Soundararajan mod-3 law, whose verification here— $$\hat c$$ drifting $$0.400\to0.370$$ over $$10^7\!\to\!4\cdot10^9$$ with $$(1,1)/(2,2)$$ symmetry $$0.99989$$—serves as calibration for the present race.

Computational checks. Over $$500$$ log-spaced samples $$n\le10^8$$: mean $$D=76.5$$ against mean empirical $$D_{\mathrm{sys}}=64.5$$, the $$(3,3)$$-lane lead significant at $$5.2$$ standard errors of the mean. Clause (ii)’s weighted model, computed in presieve-exact form (trial division of each $$n-q^2$$ to $$10^3$$ with the exact Mertens normalization), reproduces the empirical contamination with no fitted parameter: model mean $$66.3$$ against empirical $$67.8$$ (ratio $$0.98$$) on a $$400$$-sample run. The internal null lane behaves as predicted: on $$n\equiv1\ (3)$$ ($$123$$ samples) the model and empirical $$D_{\mathrm{sys}}$$ both vanish and the measured lead drops to $$31\pm23$$ (consistent with zero), while on $$n\not\equiv1\ (3)$$ ($$277$$ samples) the lead is $$88\pm21$$ against predicted contamination $$96$$—the drift lives exactly where the mechanism puts it. Clause (iii): computed $$\mathbb E_x[\Phi(\kappa)]=0.572$$ ($$\kappa$$ ranging $$0$$–$$0.64$$ with mean $$0.18$$) against observed sign fraction $$0.588$$; weak, and quantitatively the weakness the model requires.

**Conjecture 5** *(The least Goldbach summand: exponential law and ordering deficit; the time-changed law and deficit constant apparently unstated).*

Let $$s(n)$$ be the least prime $$p\nmid n$$ with $$n-p$$ prime (the exclusion $$p\nmid n$$ removes a trivial obstruction: $$p\mid n$$ forces $$p\mid n-p$$, so $$n-p$$ is composite except in the diagonal case $$n=2p$$, which would otherwise distort the hazard at one atypical point), and time-change by the expected-arrivals clock $$U(n)=\mathfrak{S}(n)\sum_{p\le s(n),\,p\nmid n}1/\log(n-p)$$. Then: The ensemble is fixed first, since $$U(n)$$ is deterministic at each $$n$$ and an expectation therefore needs a declared measure: for a scale $$X$$,

$$
\mathbb E_XU=
\frac{\sum_{X<n\le2X,\ 2\mid n}U(n)/n}
{\sum_{X<n\le2X,\ 2\mid n}1/n},
\qquad
\Theta_G(X)=\bigl(1-\mathbb E_XU\bigr)\log X.
$$

*(i)* [limit law] under $$\mathbb E_X$$-sampling, $$U\Rightarrow\mathrm{Exp}(1)$$ as $$X\to\infty$$; *(ii)* [canonical ordering deficit] $$\Theta_G(X)\to\Theta_G>0$$—the Goldbach sibling of the least-prime deficit of Conjecture 3(ii), produced by the same occupancy mechanism: the ordered primes fill the available representations faster than an exchangeable model, so the first arrival comes *early* and $$\mathbb E_X[U]<1$$.

The extremal theory of $$s(n)$$ is well developed—Granville, van de Lune and te Riele conjectured $$s(n)=O(\log^2n\log\log n)$$, and Oliveira e Silva–Herzog–Pardi [12] tabulate first occurrences of minimal Goldbach summands to $$4\times10^{18}$$ against prime $$k$$-tuple predictions—but the time-changed distributional law (i) and the deficit constant (ii) appear unstated (we could not rule out that the untransformed version of (i) is implicit in the comparisons of [12]). Measured on $$2{,}000$$ log-sampled $$n\le10^8$$: $$\mathbb E[U]=0.796$$, with $$\Theta_G=3.12\pm0.35$$ on $$[10^6,10^7)$$ and $$3.42\pm0.45$$ on $$[10^7,10^8)$$—positive, stable, and roughly *twice* the least-prime-in-progressions deficit $$\Theta=1.67$$ of Conjecture 3, a comparison the occupancy expansion there should eventually explain; the Kolmogorov–Smirnov distance to $$\mathrm{Exp}(1)$$ ($$0.088$$ at this size) is dominated by the deficit displacement itself, as (ii) requires. The derivation route for $$\Theta_G$$, parallel to the occupancy expansion at Conjecture 3: expand the survival probability $$\Pr(s(n)>y)=1-\sum_{p\le y}h_p+\sum_{p_1<p_2\le y}h_{p_1,p_2} -\cdots$$, where the pair term requires $$n-p_1$$ and $$n-p_2$$ simultaneously prime and so carries the Hardy–Littlewood singular series of the shift $$p_2-p_1$$; inserting the $$k$$-tuple predictions and integrating against the time change isolates the $$1/\log X$$ coefficient—deriving $$\Theta_G$$ rather than measuring it is the programme registered here. $$\mathfrak{S}(n)$$ alone does not encode the between-candidate dependence that the pair term carries. (The $$(3,3)$$-lane refined Goldbach statement—every $$n\equiv2\ (4)$$, $$n\ge6$$, is $$p+q$$ with $$p\equiv q\equiv3\ (4)$$, with the halved singular-series count law, formulated by K. Martin [13]—is included as an attributed calibration benchmark: exhaustively verified to $$10^9$$, count formula matching to $$0.2$$–$$1.3\%$$; its comparative lane statement is Conjecture 4.)

For sequences whose $$n$$th term has size $$\mathrm{e}^{cn}$$ the expected number of primes is $$\sum_n \kappa_n/(c\,n)$$: convergence or divergence of this sum is the entire question, and when it diverges it diverges logarithmically, so the right conjecture has counting function $$\alpha\log x$$ with a derived $$\alpha$$.

**Conjecture 6** *($$n^2+2^n$$; sequence is OEIS A064539).*

Every prime of the form $$n^2+2^n$$ with $$n>1$$ has $$n\equiv3\pmod6$$ (elementary), and: *(i)* infinitely many such primes exist, with counting function $$\asymp\log N$$; *(ii)* [candidate law, entanglement-aware form] for a finite set $$S$$ of primes $$p\ge5$$ (the primes $$2$$ and $$3$$ are exact in the lane reduction, $$\delta_2=\delta_3=0$$, and $$\operatorname{ord}_2 2$$ is undefined) let $$D_S$$ be the *exact* joint density, within the lane $$n\equiv3\ (6)$$, of $$n$$ with $$p\nmid n^2+2^n$$ for all $$p\in S$$, computed over the full joint period $$\mathrm{lcm}_{p\in S}\,\mathrm{lcm}(6,\,p\cdot\operatorname{ord}_p2)$$, and set $$\kappa_S=3\,D_S/\prod_{p\in S}(1-1/p)$$: the factor $$3=2\cdot\tfrac32$$ is the exact lane bonus at the primes $$2$$ and $$3$$ (within the lane $$\delta_2=\delta_3=0$$, so each contributes its full $$(1-1/p)^{-1}$$), included in the definition so that $$\kappa_S$$ is the complete local constant of the count in (ii-c). The conjecture is stated along the *canonical exhaustion* $$S_z=\{p\ \text{prime}:5\le p\le z\}$$, and its three layers are logically separate and are asserted separately: *(ii-a)* the sequence $$\kappa_{S_z}$$ converges as $$z\to\infty$$ (a general net over arbitrary finite $$S$$ carries an order-of-exhaustion ambiguity we do not need), with limit $$\kappa$$; *(ii-b)* whether the limit *factors*—i.e. whether the exact finite-level factorization observed below persists, so that entanglement is asymptotically absent—is an *open question*, expressly not counted among this paper’s conjectural assertions, on which (ii-a) takes no position; and *(ii-c)* the count is $$\sim\sum_{n\le N,\,n\equiv3\,(6)}\kappa/\log(n^2+2^n)$$—a genuine further step, since a convergent local density does not automatically govern the global count. The working value $$\kappa^{*}=4.2734\ldots$$ is a *hybrid*, not a computation of any single $$\kappa_{S_z}$$: the lane factor $$3$$ times the CRT-exact core $$S_{19}$$ times independent per-prime factors for $$19<p\le300$$—so $$\kappa^{*}=\kappa_{S_{300}}$$ exactly if and only if the observed exact factorization persists to $$300$$.

This is not a Bateman–Horn problem: the local conditions at different primes are tied through the orders $$\operatorname{ord}_p2$$, so the per-prime product $$\prod_p(1-\delta_p)/(1-1/p)$$ would tacitly assume their independence. The law is therefore stated through the CRT-exact quantities $$\kappa_S$$, which make no independence assumption. The computation then returned a small surprise in the other direction: through $$p\le19$$ (joint period $$116{,}396{,}280$$) the joint survivor fraction equals the product of the per-prime fractions as an *exact rational identity*, verified in exact arithmetic at every level $$S=\{5\le p\le P\}$$, $$P\in\{5,7,11,13,17,19\}$$. Entanglement is thus absent at all computed levels; whether exact factorization persists for all $$p$$—equivalently, whether the survival events are exactly independent over every joint period, which would itself be a striking equidistribution statement about the orbits of $$2$$—is part of what clause (ii) asks. We separate the robust claim (i) from the candidate law (ii), and note that the eight hits below $$6000$$ are far too few to validate a four-digit constant—the verification below checks consistency, not the constant. The OEIS records further candidate indices beyond our completed range: $$29355$$, $$34653$$, $$57285$$, $$99069$$, and the probable-prime candidate $$1933695$$. We could not independently re-verify these, but all five satisfy the lane constraint $$n\equiv3\ (6)$$, and taking them at face value the $$\kappa^{*}$$-model predicts $$2.9$$ hits in $$(6\times10^3,10^5]$$ against $$4$$ reported and $$5.9$$ in $$(6\times10^3,1.94\times10^6]$$ against $$5$$ ($$z=+0.65$$ and $$-0.38$$): the records extend the consistency check by two decades.

The congruence claim is elementary: $$n$$ odd is forced by parity, and for odd $$n$$ with $$3\nmid n$$ we have $$n^2+2^n\equiv1+2\equiv0\pmod3$$. What appears to be a harsh obstruction is, inside the surviving lane, a local bonus: $$\delta_2=\delta_3=0$$ contribute the factors $$2\cdot\tfrac32=3$$ carried explicitly in the definition of $$\kappa_S$$.

*Computational checks* (probable-prime count beyond $$n\approx80$$). Hits $$\{3,9,15,21,33,2007,2127,3759\}$$ up to $$6000$$: observed $$8$$, model $$8.55$$, $$z=-0.19$$ (over the shorter range $$n\le4200$$: $$8$$ vs $$8.19$$, $$z=-0.07$$); the lane constraint was verified exhaustively (no prime off $$n\equiv3\ (6)$$ to $$n=3000$$, independently reconfirmed), and the CRT-exact factorization of clause (ii) was verified through $$p\le19$$ as described at the statement.

**Conjecture 7** *(Fermat quotients: the multibase subtorus law and the Wieferich ledger; single-base heuristic previously stated [22], the vertical multibase law apparently new).*

With $$q_p(a)=(a^{p-1}-1)/p\bmod p$$ (defined for primes $$p\nmid a$$; all clauses below range over such $$p$$ only) and $$q_p=q_p(2)$$, five clauses: *(0)* [structure, classical] $$q_p(ab)\equiv q_p(a)+q_p(b) \pmod p$$ (the Eisenstein–Lerch homomorphism; verified exactly on every tested prime), so for multiplicatively *dependent* bases the vector $$(q_p(a_1),\dots,q_p(a_r))/p$$ is confined to the rational subtorus cut out by the relations; *(iv)* [multibase equidistribution, the claimed law] for multiplicatively *independent* bases the vector equidistributes on the full torus as $$p$$ varies—the *vertical* joint law, complementing the fixed-$$p$$, varying-base statistics of Ostafe–Shparlinski and Cobeli–Zaharescu—with correlations vanishing and the same LIL calibration as (i); *(v)* [simultaneous Wieferich] the expected count of $$p\le x$$ with $$q_p(2)=q_p(3)=0$$ has convergent sum $$\sum1/p^2$$: at most finitely many simultaneous Wieferich primes exist (the single-base folklore of this accounting is Conrad’s), and the empirical list is empty to $$10^7$$. Three further clauses on the base-2 quotient alone: *(i)* [global equidistribution] $$q_p/p$$ equidistributes on $$[0,1)$$ with discrepancy at exactly the calibrated random-model scale: in its sharp form,

$$
\limsup_{x\to\infty}
\frac{\sqrt{\pi(x)}\,D_{\mathrm{KS}}(x)}
{\sqrt{\log\log\pi(x)}}
\;=\;\frac1{\sqrt2},
$$

the Chung–Smirnov law-of-the-iterated-logarithm constant for an i.i.d. uniform sequence—demanding both no more (a bound $$O(\pi(x)^{-1/2})$$ would be *stronger than the random model supports*, the same over-demand that killed the Mertens conjecture) and no less than the model earns: the upper bound alone would be consistent with hidden rigidity, and the matching lower bound asserts the quotients fluctuate like genuine noise; *(ii)* [shrinking targets] for every fixed $$K\ge1$$, and uniformly for $$K=K(x)\le\log x$$, $$\#\{p\le x:\ q_p<K\}\sim\sum_{p\le x}\min(1,K/p)$$—the fixed-$$K$$ case down to $$K=1$$ is what governs the zero event and does NOT follow from (i), since $$\{q_p=0\}$$ is a target of shrinking measure $$1/p$$; *(iii)* [Wieferich count, fluctuation-calibrated, with the probability space declared] $$W(x)=\#\{\text{Wieferich } p\le x\}$$ is a deterministic function, so its fluctuation clauses are stated in the two legitimate forms, an unqualified CLT for a fixed sequence having no meaning: the *deterministic envelope conjecture*

$$
\limsup_{x\to\infty}
\frac{W(x)-\log\log x}
{\sqrt{2\log\log x\,\log\log\log\log x}}\;=\;1
$$

(the iterated-logarithm scale at variance $$V(x)\sim\log\log x$$; a bound $$O_\varepsilon(V^{1/2+\varepsilon})$$ would be weaker than the model’s exact prediction), and the *almost-sure central limit law, at the correct logarithmic weighting*: with $$u=\log\log x$$ the variance-time of the count, sample $$u$$ with density $$du/u$$ on $$[\mathrm{e},\,L]$$, $$L=\log\log X$$ (equivalently: $$\log u =\log\log\log x$$ uniform); then the sampled distribution of $$(W(x)-u)/\sqrt u$$ converges to $$N(0,1)$$ as $$X\to\infty$$. The weighting is what makes the clause true, and the two natural alternatives both fail. A block-sampled version on $$[X,X^A]$$ fails because only $$\log A=O(1)$$ new events enter the block. A *uniform*-in-$$u$$ version on $$[1,L]$$ fails too, by Brownian scaling: with $$W(\mathrm{e}^{\mathrm{e}^u})-u\approx B(u)$$ and $$u=Ls$$, the self-similarity $$B(Ls)/\sqrt{Ls}\overset{d}=\widetilde B(s)/\sqrt s$$ means the uniform-$$u$$ empirical distribution converges not to $$\Phi$$ but to the *random* occupation functional $$\int_0^1\mathbf 1\{\widetilde B(s)/\sqrt s\le z\}\,ds$$—values at proportional times stay correlated, so uniform sampling never averages over enough independent scales. The $$du/u$$ weighting is the classical almost-sure-CLT weighting (the continuous analogue of the $$1/k$$ weights), for which the model does predict almost-sure convergence of the sampled law to $$\Phi$$. Both clauses are conjectured on the Crandall–Dilcher–Pomerance side of the model choice that clause (iv)’s discussion records.

Two things do not follow. Clause (iii) is not a consequence of (i): a square-root-size error in the aggregate distribution is astronomically larger than $$\log\log x$$, and only the shrinking-target clause (ii) at bounded $$K$$ speaks to the zero event. And an $$O(1)$$ fluctuation claim would violate this paper’s calibration principle of demanding exactly the fluctuations the model earns: with event probabilities $$1/p$$ the count has standard deviation $$\sim\sqrt{\log\log x}$$. Nor is any location predicted for a third Wieferich prime: the expected count reaching $$3$$ “at doubly exponential heights” is an expected-count statement whose additive constant is uncalibrated, not a forecast. Consistency data: $$\{1093,3511\}$$ below $$10^8$$ against expected $$\approx2.7$$; $$\sqrt n\,\mathrm{KS}=0.82,\ 0.82,\ 0.52,\ 0.63$$ at $$x=10^5,\dots,10^8$$ (bounded, no drift); census at $$K=100$$: observed $$169$$ against model $$161.2$$.

The multibase clauses were verified at $$10^7$$ ($$664{,}577$$ primes): the homomorphism (0) held *exactly* on every spot-checked prime; for the independent pair $$(2,3)$$, correlation $$+0.0023\pm0.0012$$, a $$20\times20$$ joint occupancy $$\chi^2$$ of $$441$$ on $$399$$ degrees of freedom ($$+1.5\sigma$$), joint small-quotient census $$46$$ against model $$41.2$$ ($$z=+0.75$$), and no simultaneous Wieferich prime. Two positions are taken here: the vertical multibase law (iv) sides with the Crandall–Dilcher–Pomerance accounting against Gras’s competing probabilistic model (which predicts $$q_p(a)=0$$ *rarer* than $$1/p$$, hence possibly finitely many Wieferich primes even for a single base)—the disagreement is what gives clauses (iii)–(iv) content; and the horizontal literature (fixed $$p$$, base varying: Ostafe–Shparlinski’s joint distributions and the Fermat-quotient-matrix statistics of Cobeli–Zaharescu and coauthors) is the attributed neighbour whose vertical counterpart is what we claim here.

**Conjecture 8** *(Uniform quantitative de Polignac; the core is previously stated).*

*(i)* $$\pi_d(x)=\#\{p\le x-d:\ p,\ p+d \text{ prime}\} =\mathfrak{S}(d)\,\mathrm{Li}_2(x)\,(1+o(1))$$ uniformly for even $$d\le(\log x)^{A}$$. *(ii)* [residual field, with derived covariance kernel] The same primes participate in many pair counts, and the covariance of two of them is carried by triple configurations sharing one prime. For even $$d\neq d'$$ define the overlap constant

$$
K(d,d')=C_3(0,d,d')+C_3(0,d',d+d')+C_3(0,d,d+d')
+C_3\bigl(0,\,\vert d-d'\vert ,\,\max(d,d')\bigr),
$$

where $$C_3$$ denotes the Hardy–Littlewood triple constant of the offset set (degenerate or inadmissible triples contributing $$0$$). The field is randomized canonically—covariances of the deterministic cumulative counts are otherwise undefined: for $$t$$ uniform on $$[x,2x]$$ and a window length $$H$$, let $$\pi_d(t;H)=\#\{t<n\le t+H:\ n,\,n+d \text{ prime}\}$$ and let $$Z_d(t;H)$$ be its studentization. The mean count per window is $$\asymp H/\log^2x$$, and the regime is set by that ratio (a phase condition: a bare $$H\to\infty$$ does not fix the regime):

$$
\operatorname{Cov}_t\bigl(\pi_d,\pi_{d'}\bigr)
\sim\frac{K(d,d')\,H}{\log^3x},
\qquad
\rho(d,d')\sim\frac{K(d,d')}{\sqrt{\mathfrak{S}(d)\mathfrak{S}(d')}\,\log x},
$$

valid for $$\max(d,d')=o(H)$$, which is the standing restriction of this clause and holds throughout the window class fixed below. In general each overlap orientation $$o$$—the in-window displacements $$h_o\in\{0,\,d,\,-d',\,d-d'\}$$ and their reflections—enters with multiplicity $$(H-\vert h_o\vert )_+$$ rather than $$H$$, so that the shared-prime term reads

$$
\frac1{\log^3x}\sum_{o}\bigl(H-\vert h_o\vert \bigr)_+\,K_3^{(o)}(d,d'),
\qquad \sum_o K_3^{(o)}(d,d')=K(d,d'),
$$

and an orientation with $$\vert h_o\vert >H$$ is absent from the window altogether; under $$\max(d,d')=o(H)$$ one has $$(H-\vert h_o\vert )_+=H(1+o(1))$$ for every orientation and the displayed form is recovered, so the uniform-in-$$d$$ statement carries that restriction throughout. Here the shared-prime (triple) term is the *first* covariance contribution but not the whole of it: the full expansion is

$$
\operatorname{Cov}_t(\pi_d,\pi_{d'})
=\frac{K(d,d')\,H}{\log^3x}
+\frac1{\log^4x}\sum_{\vert h\vert \le H}(H-\vert h\vert )\,K_4(d,d';h)
+\text{error},
$$

with $$K_4$$ the centred singular series of the off-index four-point sets $$\{0,d,h,h+d'\}$$—the cross analogue of the pinned diagonal average of Conjecture 2—where degenerate offset relations are handled inside the kernels: whenever the four-point set collapses (repeated entries, as at $$h=0,\ h=d,\ h=-d'$$, or $$d'-d=\pm h$$) the configuration is a triple or pair and its contribution belongs to the $$K$$-term (or to the mean), so $$K_4$$ is defined as the centred singular series of *genuinely four-element* sets, with special pairs such as $$d'=2d$$ acquiring their extra overlap orientations in $$K(d,d')$$’s census rather than double-counted across kernels. The triple term dominates only where the pinned sum satisfies $$\sum(1-\vert h\vert /H)K_4=o(\log x)$$; the dominance range is stated as an explicit function class: for $$H=\lambda(\log x)^{\alpha}$$, any fixed $$\lambda>0$$ and any $$\alpha\ge1$$ with $$\alpha>A$$—the inequality on the exponents that makes $$\max(d,d')=o(H)$$ hold uniformly for all $$d,d'\le(\log x)^{A}$$—the per-shift centred average grows only polylogarithmically in $$H$$ (the Conjecture-2 scale), so $$\sum(1-\vert h\vert /H)K_4/H=O((\log\log x)^{2+\varepsilon}) =o(\log x)$$ and the triple term dominates throughout the polylogarithmic window class; the conjecture asserts the two-term form on exactly that class and takes no position outside it. When $$H/\log^2x\to\lambda$$ the window counts converge jointly to Poisson laws with these vanishing covariances, and when $$H/\log^2x\to\infty$$ every fixed finite collection $$\{Z_{d_1},\dots,Z_{d_r}\}$$ is asymptotically jointly normal with *independent* limiting coordinates: both kernels are finite-$$x$$ corrections to independence (test below), not nondegenerate limiting kernels. Both distributional conclusions are asserted under an explicit hypothesis beyond the displayed covariances, namely uniform Hardy–Littlewood tuple estimates on the window class fixed above, strong enough to control all higher joint cumulants of the window counts: every joint cumulant of order at least three vanishes in the respective normalizations. The diagonal correction to $$\operatorname{Var}_t(\pi_d)$$ is Conjecture 2’s pinned average, stated there.

The kernel is verified twice over. Direct window-field measurement ($$x=10^8$$, $$H=10^5$$, $$2000$$ windows, all even $$d\le40$$, $$190$$ pairs): the empirical correlation matrix matches the predicted kernel entrywise with correlation $$0.86$$, mean off-diagonal $$0.33$$ observed against $$0.37$$ predicted, the small deficit having the sign of the omitted diagonal corrections, which are also directly visible as $$\operatorname{Var}/\text{mean}=0.94$$ on average across $$d$$. Second, the deterministic cumulative profile $$z_d(x)=(\pi_d(x)-\mathfrak{S}(d)\mathrm{Li}_2(x))/\sqrt{\mathfrak{S}(d)\mathrm{Li}_2(x)}$$—the estimator the uniformity verification in (i) uses—shows the same structure at cumulative scale (there $$\rho\sim K\mathrm{Li}_3/\sqrt{\mathfrak{S}\mathfrak{S}'}\mathrm{Li}_2$$): mean off-diagonal $$\rho=0.43$$ over all even $$d,d'\le60$$ at $$x=10^8$$, hence predicted profile spread $$\sigma^2\le1-0.41=0.59$$ before the diagonal correction, against observed $${\approx}0.27$$, implying a diagonal factor $${\approx}0.5$$ of Montgomery–Soundararajan sign and order.

The force of the statement is its uniformity: the singular series takes a thousand different values over $$d\le2000$$, spanning a factor of about three between $$d=2$$ and the primorial-rich $$d$$, and the counts must reproduce the entire profile simultaneously with square-root errors. A conspiracy would need to bend a thousand-dimensional vector, not one number. At $$x=10^8$$: correlation $$0.999999$$, slope $$0.99966$$, $$\max_d\vert z_d\vert =1.80$$; stressed to $$d\le6000$$, $$\max\vert z_d\vert =2.01$$ over three thousand values.

(A further Hardy–Littlewood calibration, on a prime quintuplet constellation, gives observed $$15{,}236$$ against predicted $$15{,}230.3$$ at $$4\cdot10^9$$, ratio $$1.0004$$, $$z=+0.05$$.)

**Conjecture 9** *(The sub-diffusivity of balanced prime races; apparently new).*

Model a balanced race (Conjecture 1(ii)’s symmetric class differences) as the walk of its class-assignment steps, the process defined at event index: enumerate the pattern occurrences $$n_1<n_2<\cdots$$ in the two competing classes, set $$\xi_i=\pm1$$ by class membership of $$n_i$$, and let $$\rho_k(x)$$ denote the lag-$$k$$ sample autocorrelation of $$(\xi_i)$$ over the events with $$n_i\le x$$. Then the walk is measurably *sub-diffusive*: *(i)* [decaying-repulsion law] the step autocorrelations are negative at small lags—the race analogue of the Lemke Oliver–Soundararajan consecutive-pattern repulsion [24], which supplies the mechanism—and, since that repulsion is scale-dependent rather than fixed, the conjectured form is a decay law

$$
\rho_k(x)\;=\;-\,\frac{c_k\log\log x+d_k}{\log x}\,(1+o(1)),
$$

with constants $$c_k,d_k$$ in principle derivable from the LOS correlation series (underived here; and the measured values $$\rho_1\approx-0.037$$, $$\rho_2\approx-0.009$$ at $$10^9$$—universal across twin and cousin races mod $$5$$ and $$8$$ to within $$0.004$$, each $${\sim}50$$ standard errors from zero—are observations at one height, consistent with $$c_1\approx0.25$$ there, not asymptotic constants); *(ii)* [long memory, measured] short lags do not exhaust the deficit: the running maxima $$M(x)=\max_{t\le x}\vert D(t)\vert /\sqrt{\text{count}}$$ of the four races land at quantiles $$0.02$$–$$0.17$$ of the simulated independent-step null (median $$2.34$$ at this span), and still only $$0.03$$–$$0.23$$ after correcting for $$\rho_{1,2}$$: the negative correlation persists across lags, so the cumulative diffusivity $$\sigma^2(x)=1+2\sum_k\rho_k(x)$$ sits well below $$1$$ at this height. The model layer is declared: $$(\xi_i)$$ is a deterministic, nonstationary family and the $$\rho_k(x)$$ are empirical statistics of it, so the Green–Kubo identity $$\sigma^2=1+2\sum_k\rho_k$$ is invoked under an explicit *local-stationarity model hypothesis*—the step process restricted to a window $$[x,2x]$$ is modelled as a stationary sequence whose autocorrelations are the measured $$\rho_k(x)$$—and the variance statement can equivalently be taken as a direct *definition* of $$\sigma^2(x)$$ through block averages of $$(S_{n+m}-S_n)^2/m$$ over the events up to $$x$$, a form in which no stationarity is assumed at all. The Green–Kubo sum requires more than the fixed-lag law of (i): the per-lag decay controls each $$\rho_k(x)$$ but not the sum unless the decay is *uniform in $$k$$ with summable tail*, since the number of relevant lags may grow with $$x$$. We therefore state the needed hypothesis as part of the clause: $$\rho_k(x)$$ obeys the law of (i) uniformly for $$k\le K(x)$$ with $$\sum_{k>K(x)}\vert \rho_k(x)\vert =o(\log\log x/\log x)$$ for some $$K(x)\to\infty$$, *and*—since the tail bound alone leaves the growing head sum uncontrolled—the repulsion constants are summable, $$\sum_k c_k<\infty$$ and $$\sum_k\vert d_k\vert <\infty$$, so that $$\sigma^2(x)=1-2\bigl(\textstyle\sum_kc_k\,\log\log x+\sum_kd_k\bigr)/\log x\,(1+o(1))$$ is a genuine consequence rather than an unjustified interchange of limits. The measured correlation length at $$10^9$$ (a few tens of lags, with $$\vert \rho_k\vert$$ decreasing geometrically in the observable range) is consistent with both hypotheses. Under them, $$\sigma^2(x)$$ returns to $$1$$ asymptotically, making sub-diffusivity a finite-height phenomenon of $$\log\log x/\log x$$ size, like every other second-order law in this paper; *(iii)* [registered dichotomy, open] asymptotically the two possibilities are *mutually exclusive*, and which of them holds is the open question. Either the fixed-lag expansion of (i) extends uniformly in $$k$$ with summable constants—in which case the hypotheses of (ii) hold, (ii) applies, and the race is asymptotically diffusive with $$\sigma^2(x)\to1$$ (running maxima $$\sim\sqrt{2\log\log x}$$, Darling–Erdős class)—or that expansion fails at long lags, and only in that case can the race inherit the almost-periodic rigidity that Rubinstein–Sarnak-type structure [6] forces on classical races (maxima $$\asymp(\log\log\log x)^{A}$$, the Montgomery–Ng class). Rigidity therefore requires a failure of the hypotheses of (ii) at long lags, and cannot coexist with them. No explicit formula is known for twin patterns, the two branches differ only beyond any computable height, and we register the dichotomy without choosing *in this conjecture*. What is conjectured here is therefore the fixed-lag law (i) outright, and the variance law of (ii) *conditionally on* its stated uniformity and summability hypotheses, which belong to the finite-height model layer and are not asserted asymptotically: asserting them would silently select the diffusive branch of (iii). The pattern-specific selection is made elsewhere—Conjecture 1 asserts the rigid branch for its races, through (i-b) for the contaminated combinations and through the drift-scale nulls of its clause (ii) for the symmetric differences—and consistency between the two conjectures then requires exactly that the hypotheses of (ii) fail at long lags for those races.

The repulsion constants $$\rho_1,\rho_2$$ are pattern-independent across our four races—a universality the LOS correlation series should predict quantitatively, and the derivation programme stated here—and the suppressed maxima are the first (to our knowledge) direct measurement of race sub-diffusivity, an effect invisible to endpoint statistics. (The twin-gap record benchmark—$$G_t(x)\asymp\log^3x$$ with working constant $$1/(2C_2)$$, inside Kourbatov’s extreme-value framework [15]—is included as an attributed calibration benchmark: records to $$4\cdot10^9$$ wander in $$[0.41,0.56]\log^3x$$, approaching from below on a $$\log\log$$ clock, largest observed twin-to-twin gap $$5292$$ after the twin at $$2{,}466{,}641{,}069$$; the Cramér–Granville fragility of such constants [17] is why the constant was always flagged as first-order.)

## 4. Family laws and second-order refinements

**Conjecture 10** *(Uniform quadratic de Polignac; family law apparently unstated, the $$d=2$$ instance previously stated, cf. OEIS A080149, [32]).*

For even $$d\ge2$$ let $$\pi^{\mathrm q}_d(N)=\#\{n\le N:\ n^2+1,\ n^2+1+d \text{ both prime}\}$$ and $$C(d)=C(x^2+1,\,x^2+1+d)$$. Then: *(i)* [uniform family law] for every fixed $$B>0$$, $$\pi^{\mathrm q}_d(N)=C(d)\,I_d(N)(1+o(1))$$ uniformly over even $$d\le(\log N)^{B}$$; *(ii)* [registered rate, strictly stronger] there is $$\eta_B>0$$ with

$$
\sup_{\substack{2\le d\le(\log N)^{B}\\ 2\mid d}}
\Bigl\vert \frac{\pi^{\mathrm q}_d(N)}{C(d)\,I_d(N)}-1\Bigr\vert
\;\ll_B\;(\log N)^{-\eta_B}
$$

—an error clause that no version of Bateman–Horn supplies, registered separately from (i) since its analytic content is independent; *(iii)* [family statistic: the law of the constants] each local factor of $$C(d)$$ depends only on $$d\bmod p$$, and the factors at any *finite* set of primes are exactly independent as $$d$$ varies (CRT), with the passage to the infinite product controlled by the convergent tail-variance sum—which supplies the uniform integrability (via $$L^2$$-boundedness of the normalized partial products) that the moment identities require, since almost-sure convergence alone would not carry means through the limit; so the moments of $$C(d)$$ over even $$d\le D$$ converge, as $$D\to\infty$$, to *derived* Euler products; in particular

$$
\frac1{\#}\sum_{2\mid d\le D}C(d)\to\bar C=2.7456\ldots,
\qquad
\operatorname{sd}\bigl(C(d)\bigr)\to1.6840\ldots,
$$

and the empirical distribution of $$C(d)$$ converges to the law of the random product $$\prod_p f_p(U_p)$$ with independent uniform residues $$U_p$$. In particular ($$d=2$$, the classical instance): $$\#\{n\le N:\ n^2+1,\ n^2+3 \text{ both prime}\}\sim C(2)\,I(N)$$, $$C(2)=2.954014\ldots$$

This is the quadratic analogue of the uniform de Polignac law of Conjecture 8: not one count but the whole profile of constants must be matched at once, and the family, unlike its linear parent, has no known prior statement. Every even shift is admissible (for $$p\ge5$$, $$\omega(p)\le4<p$$; the classes mod $$3$$ and $$5$$ vary with $$d$$, which is what makes the $$C(d)$$-profile nonconstant, spanning a factor of about twenty over $$d\le300$$, from $$0.47$$ at $$d=298$$ to $$9.06$$ at $$d=162$$). At $$d=2$$ the local analysis reads: $$n$$ even, $$n\not\equiv0\pmod3$$, $$\omega(p)=2+\bigl(\frac{-1}{p}\bigr)+\bigl(\frac{-3}{p}\bigr)$$ for $$p\ge5$$, and the conjecture implies infinitely many twin pairs $$(m+1,m+3)$$ with $$m$$ a perfect square. Profile verification at $$N=10^6$$ over all $$150$$ even shifts $$d\le300$$: correlation $$0.99976$$ between observed and predicted counts, regression slope $$1.0022$$, residual mean $$z=+0.24$$ with spread $$0.84$$ and $$\max_d\vert z\vert =2.28$$—the shape-of-agreement standard applied across the family. Clause (iii) was verified by computing both sides independently: the derived Euler-product moments give mean $$2.7456$$ and standard deviation $$1.6840$$, against $$2.7434$$ and $$1.6726$$ measured over the $$150$$ constants with $$d\le300$$ (ratios $$0.9992$$ and $$0.9932$$)—a family-level statistic whose constants are derived, not fitted. One question the family raises is recorded as open rather than conjectured: the maximal range $$D(N)$$ for which the uniform law can hold (the analogue of the Elliott–Halberstam question for this family—whether there is a sharp transition at some power scale $$N^{\delta}$$ rather than a logarithmic one).

*Computational checks (the classical single instance).* At $$d=2$$ and bound $$10^{7}$$: observed $$32{,}898$$ against predicted $$32{,}862.7$$, ratio $$1.0011$$, $$z=+0.19$$; the family-profile verification across the $$150$$ shifts $$d\le300$$ is reported above.

**Conjecture 11** *(First occurrences of prime gaps, liminf form; the family is classical, the quantified form apparently unstated).*

Let $$\mathcal G$$ be the set of even $$g$$ that occur as gaps between consecutive primes (all even $$g$$, under Polignac’s conjecture), and for $$g\in\mathcal G$$ let $$p(g)$$ be the prime starting the first such gap. Then: *(i)* $$\log p(g)/\sqrt g$$ is bounded between positive constants on $$\mathcal G$$; *(ii)* [liminf law, stated as the dual of the maximal-gap limsup, *conditional on the realization hypothesis below*]

$$
\liminf_{\substack{g\to\infty\\ g\in\mathcal G}}
\ \frac{\log p(g)}{\sqrt g}
\;=\;\sqrt{\mathrm{e}^{\gamma}/2}\;=\;0.943682\ldots
$$

The inversion of Granville’s $$\limsup G(X)/\log^2X=2\mathrm{e}^{-\gamma}$$ into first-occurrence coordinates is *not* automatic: the limsup controls how large maximal gaps get, not which gap *sizes* are realized as first occurrences near the envelope. Clause (ii) is therefore conditional on the *realization hypothesis*: infinitely many $$g\in\mathcal G$$ first occur inside a maximal-gap event at the Cramér–Granville envelope scale, i.e. with $$g=(2\mathrm{e}^{-\gamma}+o(1))\log^2 p(g)$$. Under that hypothesis the displayed value is forced by algebra; without it only the lower bound $$\liminf\log p(g)/\sqrt g\ge\sqrt{\mathrm{e}^{\gamma}/2}$$ follows from the envelope. The value is registered *as* that dual (against the slope-1 laws), not claimed as an independent phenomenon; *(iii)* [second-order, singular-series dependence] sampling $$g$$ uniformly from the realized gaps $$\mathcal G\cap[G,2G]$$ and letting $$G\to\infty$$,

$$
\log p(g)\;=\;\sqrt g+\tfrac12\log g-\tfrac12\log\mathfrak{S}^{*}(g)+E_g,
\qquad
\mathfrak{S}^{*}(g)=\prod_{\substack{p\mid g\\ p>2}}\frac{p-1}{p-2},
$$

where the error $$E_g$$ converges in distribution: for the sampled $$g$$,

$$
\Pr\bigl[E_g\le t\bigr]\;\longrightarrow\;
1-\exp\bigl(-\mathrm{e}^{\,2(t-\mu)}\bigr)
\qquad(G\to\infty)
$$

for some centring constant $$\mu$$—the min-type (reversed) Gumbel law *at scale* $$\tfrac12$$, i.e. the law of $$\tfrac12\log W$$ for $$W$$ a unit exponential. The scale is forced by the hazard computation: the cumulative intensity of gap-$$g$$ events is $$\Lambda_g(y)\asymp(\mathfrak{S}(g)/y^2)\exp(y-g/y)$$ in $$y=\log x$$ (the factor $$\mathrm{e}^{-g/y}$$ *is* the no-intervening-prime probability), so $$\frac{d}{dy}\log\Lambda_g=1+g/y^2-2/y=2+o(1)$$ at the centring point $$y_0\approx\sqrt g$$, and the first-passage identity $$\Lambda_g(y)=W$$ gives $$E_g=y-y_0=\tfrac12\log W+o(1)$$. The scale is $$\tfrac12$$ and not $$1$$ precisely because the slope of the log-intensity at $$y_0$$ is $$2$$ (both the $$y$$-term and the $$g/y$$-term contribute), and the same slope-$$2$$ expansion is what produces the $$\tfrac12$$ coefficients of the centring. (Gumbel-type modelling of gap extremes and first occurrences is Kourbatov–Wolf territory [15, 25]; the claim of this clause is only the $$\mathfrak{S}^{*}$$-centring and the scale-$$\tfrac12$$ first-passage form, not the extreme-value framework. Sampling uniformly over the *realized* gaps in $$[G,2G]$$ conditions on realization, which the independent first-passage model does not represent; the clause conjectures that this selection does not shift the limiting law, and that assumption is part of what a refutation would refute.) Smooth gaps, whose tuple constant is large, appear *earlier* by exactly half a logarithm of that constant—the waiting-time first-passage computation makes the coefficient $$-\tfrac12$$, not a free parameter, while $$\mu$$ is left as the one unresolved constant of the clause. (The restriction to $$\mathcal G$$ is needed: $$p(g)$$ is not known to be defined for every even $$g$$, and quantifying over all $$g$$ would smuggle Polignac’s conjecture into the statement. The $$\mathfrak{S}^{*}$$-clause records that the Hardy–Littlewood factor of $$g$$ materially shifts waiting times; it does not move the liminf constant, since $$\log\mathfrak{S}^{*}(g)=O(\log\log g)$$.)

Clause (iii) was tested on the full first-occurrence table to $$10^9$$: over the $$100$$ even gaps realized in $$[60,500]$$, regressing $$\log p(g)-\sqrt g-\tfrac12\log g$$ on $$\log\mathfrak{S}^{*}(g)$$ (with a $$\sqrt g$$ trend term absorbing the liminf-versus-typical drift) gives coefficient $$-0.466$$ against the predicted $$-\tfrac12$$, partial correlation $$-0.24$$: the singular series of the gap is visible in when the gap first appears, at the predicted strength.

The full limit does not follow by inverting Granville’s $$\limsup G(x)/\log^2x=2\mathrm{e}^{-\gamma}$$: that inversion is invalid, since a limsup envelope for maximal gaps controls only where gaps *can first appear at the earliest*, i.e. a lower envelope for $$p(g)$$—hence a liminf claim, not a limit. Whether $$\log p(g)/\sqrt g$$ converges at all, and if so whether the limit is Shanks’s classical $$1$$ [16] (as Wolf’s refinement $$p(g)\sim\sqrt g\,\mathrm{e}^{\sqrt g}$$ and the Kourbatov–Wolf residue-class laws [25] also assert) or the envelope value, involves at least three distinct phenomena—whether a given $$g$$ occurs near the extreme scale at all, the distribution of exact gap lengths near records, and the difference between record gaps and non-record first occurrences—and is left open here. The two candidate constants differ by $$6\%$$, beneath the resolution of any feasible computation: our regression slope over $$g\ge100$$ falls from $$1.307$$ at $$10^9$$ to $$1.297$$ at $$4\cdot10^9$$, far above both and decreasing, as it must be for either.

**Conjecture 12** *(The Stern lane race; apparently new).*

In Stern’s representation problem $$n=p+2k^2$$ ($$n$$ odd), race the $$k$$-even and $$k$$-odd lanes. Prime-square contamination of the $$\Lambda$$-weighted lane counts comes from $$n=q^2+2k^2$$—the norm form $$x^2+2y^2$$ of $$\mathbb Q(\sqrt{-2})$$ with prime $$x$$—and since $$q^2\equiv1\pmod8$$ while $$2k^2\equiv0$$ or $$2\pmod 8$$ by the parity of $$k$$: *(i)* [class assignment, direct congruence] contamination sits in the $$k$$-*even* lane iff $$n\equiv1\pmod8$$, in the $$k$$-*odd* lane iff $$n\equiv3\pmod8$$, and for $$n\equiv5,7\pmod8$$ *no* square contamination exists at all: $$q^2+2k^2\equiv1$$ or $$3\pmod 8$$ always, a two-line congruence (genus theory enters only for the converse question of which $$n$$ *are* represented), so the null classes are provable, not conjectured; *(ii)* [drift law, in the ensemble form of Conjecture 4] Fix the ensemble: for a scale $$X$$, let $$\mathbb E_X$$ average over odd $$n\in(X,2X]$$ of the given residue class mod $$8$$ with weight proportional to $$1/n$$ (the logarithmic sampling measure, as at Conjectures 5 and 4). Define, per class, the *clean-minus-contaminated* difference with explicit sign: $$D(n)=R_{\mathrm o}-R_{\mathrm e}$$ for $$n\equiv1\pmod 8$$ (even lane contaminated), $$D(n)=R_{\mathrm e}-R_{\mathrm o}$$ for $$n\equiv3\pmod 8$$, and $$D(n)=R_{\mathrm e}-R_{\mathrm o}$$ (sign immaterial) on the null classes $$n\equiv5,7\pmod8$$. Set $$D_{\mathrm{sys}}(n)=\bigl[\sum_{(q,k):\,q^2+2k^2=n,\ q\ \mathrm{prime},\,k\ge1}\log q\bigr]/\lambda_{\mathrm{an}}(n)$$—the weight is $$\Lambda(q^2)=\log q$$, each representation counted once in the $$k\ge1$$ convention (the ordered-representation factor $$2$$ of Conjecture 4 has no counterpart here, and doubling would be a normalization error)—where $$\lambda_{\mathrm{an}}(n)$$ is the *analytic* lane mean of $$\log p$$ over the candidate profile, defined with no reference to which candidates are prime: $$\lambda_{\mathrm{an}}(n)=\bigl(\int_0^{\sqrt{(n-2)/2}}du\bigr)\big/\bigl(\int_0^{\sqrt{(n-2)/2}}du/\log(n-2u^2)\bigr)$$, the mean of $$\log(n-2u^2)$$ under the density proportional to $$1/\log(n-2u^2)$$ on the candidate interval (the upper limit keeps $$n-2u^2\ge2$$, the convention of $$I(N)$$, avoiding the nonintegrable point $$n-2u^2=1$$), which is the profile a Bateman–Horn heuristic assigns to the prime representations. The definition is out-of-sample: the verification’s empirical lane mean over the observed prime representations is an estimator of $$\lambda_{\mathrm{an}}$$, used as a consistency check, not part of the definition. The law, coefficient-identifying as at Conjecture 4(i): on the contaminated classes

$$
\mathbb E_X\bigl[D-D_{\mathrm{sys}}\bigr]
=o\bigl(\mathbb E_X[D_{\mathrm{sys}}]\bigr)
\qquad(X\to\infty),
$$

and on the null classes—where $$D_{\mathrm{sys}}$$ vanishes identically, so that a comparison against it would be empty—the statement is made against the positive comparison scale

$$
A(X)\;:=\;\mathbb E_X^{(1)}\bigl[D_{\mathrm{sys}}\bigr],
$$

the logarithmic-ensemble mean of the systematic census taken over the *contaminated* class $$n\equiv1\pmod 8$$: writing $$D_{\mathrm{null}}$$ for the difference $$D$$ on a null class $$n\equiv5$$ or $$7\pmod 8$$, the claim is $$\mathbb E_X[D_{\mathrm{null}}]=o\bigl(A(X)\bigr)$$.

This is the calculus applied to a *representation* problem with norm-form contamination—the drift weight is carried by the arithmetic of $$\mathbb Q(\sqrt{-2})$$ rather than by a polynomial lane—and it comes with two provable null classes. On depth: an *asymptotic* for the contaminating count $$\#\{(q,k):q^2+2k^2=n,\ q\ \text{prime}\}$$, averaged over $$n$$, is a norm-form-with-prime-argument problem of genuine analytic difficulty (the same species as primes represented with restricted variables); $$D_{\mathrm{sys}}(n)$$ is *computed exactly per sample*, so the verification tests the transfer conjecture against the true census, not against an unproved averaged asymptotic. Verified on $$2{,}500$$ log-sampled odd $$n\le10^8$$ (mean $${\sim}330$$ representations each): contaminated strata pooled $$D=+0.27\pm0.33$$ against predicted $$D_{\mathrm{sys}}=+0.15$$ (at the $$\Lambda(q^2)$$ weight); null strata pooled $$-0.22\pm0.33$$, consistent with zero (one of the four strata sits at $$-2\sigma$$ individually, within a four-test family). (Stern’s exceptional list —the ten known odd integers that are not $$p+2k^2$$, the largest $$5993$$, with the seven prime members the Stern primes; completeness of the list is conjectural, OEIS A060003—is included as the attributed calibration benchmark anchoring this conjecture: no further exception occurs below $$10^9$$ in our computation.)

**Conjecture 13** *(Microscopic variance law; classical family, the constant is Montgomery–Soundararajan’s [19]).*

Fix $$\lambda>0$$ and $$c\in(0,1]$$, and let $$X$$ count primes in $$[t,\,t+\lambda\log x)$$ for $$t$$ uniform on $$[x,(1+c)x]$$. Then, under the Hardy–Littlewood $$k$$-tuple conjectures, $$X\Rightarrow\mathrm{Poisson}(\lambda)$$ (Gallagher’s argument [18], which is conditional on exactly those conjectures), and—*conditional on the quantitative hypothesis* spelled out after the statement (uniform Hardy–Littlewood with $$o(h)$$ control of the averaged singular series), without which the display below is a registered extrapolation rather than a consequence—at finite $$x$$

$$
\frac{\operatorname{Var}X}{\mathbb E\,X}
\;=\;1-\frac{\log(\lambda\log x)+\gamma+\log2\pi-1}{\log x}
+o\!\Bigl(\frac1{\log x}\Bigr),
$$

with $$\gamma+\log2\pi-1=1.41509\ldots$$, the leading correction being independent of the sampling constant $$c$$. [Interpolation clause] More generally, for windows of length $$H=\lambda(\log x)^{\alpha}$$ the *same* formula with $$\log H$$ in place of $$\log(\lambda\log x)$$,

$$
\frac{\operatorname{Var}X}{\mathbb E\,X}
\;=\;1-\frac{\log H+\gamma+\log2\pi-1}{\log x}
+o\!\Bigl(\frac1{\log x}\Bigr),
$$

holds uniformly for $$1\le\alpha\le A$$ (any fixed $$A$$ with $$H\le x^{o(1)}$$): one expression interpolates from Gallagher’s Poisson boundary ($$\alpha=1$$, deficit $$\asymp\log\log x/\log x$$) through the mesoscopic Montgomery–Soundararajan regime (deficit $$\asymp\alpha\log\log x/\log x$$), with no transition other than the slow growth of $$\log H$$.

The deficit arises by inserting Montgomery’s singular-series average $$\sum_{d\le h}\mathfrak{S}(d)(h-d)=\tfrac{h^2}2-\tfrac h2(\log h+\gamma+\log2\pi -1)+o(h)$$ into the second factorial moment at the microscopic window $$h=\lambda\log x$$. The constant $$\gamma+\log2\pi-1$$ is Montgomery–Soundararajan’s, was identified in their framework long before this paper, and the statement is a *microscopic extrapolation and numerical test* of their second-moment formula at Gallagher’s boundary—not a newly discovered second-order law. The hypothesis must also be quantitative: what is required is not the qualitative $$k$$-tuple conjectures but uniform Hardy–Littlewood estimates for all shifts up to $$O(\log x)$$, control of the average singular series at the $$o(h)$$ level, and bounds for prime powers, endpoint weights, and the variation of $$\log t$$ across the sampling range. Three further qualifications are built into the statement: Gallagher’s Poisson law is conditional, not a theorem about primes; the sampling measure for $$t$$ is specified, since different weightings shift lower-order terms; and the error is claimed only as $$o(1/\log x)$$. The naive claim $$\operatorname{Var}/\mathbb E=1$$ fails at every accessible scale by $$18$$–$$28\%$$; the corrected law matches with no fitted parameter, and the observed residual $$\approx+0.003$$ is consistent with (but not evidence for) a genuine $$1/\log^2x$$ term. (Numerical precedent: Sanchis-Lozano [26] fitted the Montgomery–Soundararajan variance shape at $$x\sim10^8$$ in the mesoscopic regime $$h\gg\log N$$; the microscopic statement and test appear to be new.)

| $$\lambda$$ | observed, $$x=10^9$$ | predicted, $$x=10^9$$ | observed, $$x=4\cdot10^9$$ | predicted, $$x=4\cdot10^9$$ |
|---|---|---|---|---|
| $$1/2$$ | $$0.8241$$ | $$0.8189$$ | — | — |
| $$1$$ | $$0.7910$$ | $$0.7854$$ | $$0.7998$$ | $$0.7960$$ |
| $$2$$ | $$0.7527$$ | $$0.7520$$ | $$0.7670$$ | $$0.7646$$ |
| $$4$$ | $$0.7201$$ | $$0.7185$$ | — | — |

The residual $$\approx+0.003$$ is the anticipated $$O(1/\log^2x)$$ term.

**Conjecture 14** *(The null-mechanism race; apparently new).*

For the quadratic twin pairs of Conjecture 10 at $$d=2$$, square contamination is *algebraically impossible*: $$n^2+1=q^2$$ has no solution with $$n\ge1$$, and $$n^2+3=q^2$$ only at $$(n,q)=(1,2)$$. The surviving classes of $$n$$ mod $$5$$ are $$\{0,1,4\}$$ (the single escape $$n=2$$, the pair $$(5,7)$$ in the killed class $$2$$, is one bounded term), and the classes $$1$$ and $$4$$ have identical singular series (elementary, via CRT). Let $$\pi^{\mathrm q}_a(x)$$ count solutions with $$n\equiv a\pmod5$$, $$D(x)=\pi^{\mathrm q}_1(x)-\pi^{\mathrm q}_4(x)$$, and define the normalized race process $$Y(x)=D(x)\big/\sqrt{\pi^{\mathrm q}_1(x)+\pi^{\mathrm q}_4(x)}$$. Then, in contrast to the twin race of Conjecture 1, this race is *driftless*: *(i)* $$\mathcal{M}_x\bigl(D(t)\log^2t/\sqrt t\bigr)\to0$$ at the *drift-scale* normalization of Conjecture 1(i)—the scale at which the contaminated races converge to nonzero constants—so this is the genuine negation of Conjecture 1(i) for this pair (the weaker normalization $$\mathcal{M}_x(Y)\to0$$ with $$Y=D/\sqrt{\pi^{\mathrm q}}$$ would not exclude a drift at the contamination scale, hence would not make this race a control; the form stated excludes exactly that); *(ii)* [occupation law, conjectured directly, with a separately falsifiable local hypothesis] the process is defined precisely at event index: let $$n_1<n_2<\cdots$$ enumerate the $$n$$ with $$n^2+1$$ and $$n^2+3$$ both prime and $$n\equiv1$$ or $$4\pmod5$$, set $$\xi_i=+1$$ if $$n_i\equiv1$$ and $$-1$$ if $$n_i\equiv4$$, and let $$S_N=\xi_1+\cdots+\xi_N$$ (so $$D(x)=S_{N(x)}$$ with $$N(x)$$ the number of such events to $$x$$). The sequence $$(\xi_i)$$ is deterministic, so the hypothesis is stated for a randomly sited window rather than for $$S_N$$ itself. Fix a growth scale $$N_0$$ and a window length $$N=N(N_0)$$ with $$N=o(N_0)$$, and choose the starting index $$M$$ of the window according to the logarithmic measure on $$[1,N_0]$$:

$$
\Pr[M=m]\;=\;\Bigl(\sum_{1\le m'\le N_0}\tfrac1{m'}\Bigr)^{-1}
\frac1m,\qquad 1\le m\le N_0 .
$$

The hypothesis is an *almost-sure invariance principle* (ASIP) for the induced random path $$(S_{M+j}-S_M)_{0\le j\le N}$$ under that sampling law: on a probability space carrying $$M$$ and a standard Brownian motion $$B$$,

$$
S_{M+j}-S_M\;=\;B(j)+O\bigl(N^{1/2-\delta}\bigr)
\qquad\text{uniformly for }0\le j\le N,
$$

almost surely in $$M$$ as $$N_0\to\infty$$, for some $$\delta>0$$. The logarithmic sampling law is the same clock in which the occupation statement below is read, and randomizing the window start is what supplies the deterministic step sequence with a probability space. The weak functional limit theorem—$$S_{\lfloor N\tau\rfloor}/\sqrt N$$ converging weakly to standard Brownian motion on $$\tau\in[0,1]$$—is retained as the weaker, separately falsifiable consequence of the windowed ASIP. The occupation law itself, however, is *not* a consequence of the windowed hypothesis, and is conjectured directly. The windowed path $$S_{M+j}-S_M$$ is recentred at the window start, and recentring erases exactly the absolute level that occupation measures: a deterministic bias $$b(n)=\sqrt n/\log n$$ added to $$S_n$$ shifts the level by $$\sqrt n/\log n$$ while contributing window increments of size $${\sim}j/(2\sqrt n\,\log n)\ll\sqrt j$$, invisible to the windowed ASIP at every window scale, yet it would drive the occupation fraction to $$1$$. A global coupling $$D(t)=B(N(t))+o(\sqrt{N(t)})$$ with $$N(t)\asymp t/\log^2t$$ would suffice, but for the deterministic sequence $$(\xi_i)$$ no randomization is available that makes such a coupling well posed, so we do not hypothesize it. The Brownian computation is instead the motivation that identifies the limit and the constant: for a coupled walk, in *logarithmic* time $$u=\log t$$ the Lamperti reduction $$Z(s)=\mathrm{e}^{-s/2}B(\mathrm{e}^s)$$ is a stationary, ergodic Ornstein–Uhlenbeck process, and the logarithmic occupation measure of leadership converges almost surely to $$\tfrac12$$. The conjectured law is that conclusion itself:

$$
\frac1{\log x}\int_2^x\mathbf 1_{\{D(t)>0\}}\,\frac{dt}t
\;\longrightarrow\;\frac12,
$$

with fluctuations of the Gaussian scale $$\sqrt{\log2/\log x}$$ (the occupation-indicator covariance $$\frac1{2\pi}\arcsin\mathrm{e}^{-u/2}$$ integrates to $$\tfrac12\log2$$; note that the integrated covariance for the *sign* average $$2\mathbf 1-1$$ is four times this, its standard deviation twice, the occupation fraction itself carrying $$\sqrt{\log2/\log x}$$); the classical arcsine spread survives only in the *natural* event clock, i.e. for occupation fractions of $$\{B(m)>0,\ m\le N(x)\}$$. A persistent systematic leader—a log-occupation stuck near $$0$$ or $$1$$ beyond the stated Gaussian scale—is the refutation.

The clock matters here. An arcsine-distributed limit for the logarithmic occupation itself is incompatible with the change of clock: the arcsine law lives in the natural time of the walk, whereas under $$dt/t$$ averaging the Lamperti transform is ergodic and forces the limit $$\tfrac12$$. The distinction is what makes the statistic informative: the observed log-occupation $$0.21$$ at $$10^7$$ sits $$1.4$$ null standard deviations below $$\tfrac12$$ (scale $$\sqrt{\log2/\log x}\approx0.21$$ there)—still consistent with the driftless null—whereas read as an arcsine draw the same number would carry no information at all.

This is the negative control that completes the mechanism family of Conjectures 1 and 4: those races carry a predicted drift *because* prime squares can infiltrate specific residue classes of specific patterns; here the quadratic form blocks squares identically, so the same model predicts *nothing*—a falsifiable contrast. If a persistent drift were found in this race, the mechanism story behind the family would be wrong no matter how well the positive cases fit. The absence of *this* drift source does not by itself prove the race driftless—oscillatory zero terms, higher prime powers, and endpoint corrections are other conceivable sources—so clause (i) is a conjecture under the same zero-oscillation hypothesis as Conjecture 1, not a consequence of the square-blocking algebra alone. What the algebra supplies is the *contrast*: whatever residual model one adopts, it must produce drift in Conjectures 1 and 4 and none here. Computational checks at $$10^7$$: $$32{,}898$$ pairs, class counts $$10{,}917$$ against $$10{,}981$$ ($$D=-64$$, i.e. $$-0.43$$ noise units), log-mean normalized drift $$-0.46$$ (consistent with $$0$$ at one noise unit), log-occupation of leadership $$0.21$$—$$1.4$$ null standard deviations below $$\tfrac12$$ on the clock and constant of clause (ii), within the fair race’s $$95\%$$ band. (The quadratic triple $$n^2+\{1,3,7\}$$, $$C=10.64599\pm0.006$$, is included as a calibration benchmark—observed $$3{,}963$$ against predicted $$3{,}998.6$$ at $$10^7$$, $$z=-0.56$$, independently recomputed to $$3\times10^7$$; the longer pattern $$n^2+\{1,3,7,9,13\}$$ has been recorded in the OEIS since 2000, so the tuple family has prior presence and only its singular-series evaluation is plausibly new.)

*Computational checks.* The race data are reported at the statement above; independent recomputation of this conjecture’s calibration member, the quadratic triple, gave $$10.647706$$, with primes to $$10^9$$—inside our stated wobble—and an independent count to $$3\times10^7$$ with final ratio $$1.0059$$.

**Conjecture 15** *(The cubic shift family: the distribution of its constants; instance-level law apparently unstated).*

For non-cube $$a\ge1$$ let $$C(a)=C(x^3+a)$$. Only $$p\equiv1\pmod3$$ moves the product, and the local root count there takes *three* values as $$a$$ varies mod $$p$$: $$\omega=3$$ with probability $$(p-1)/3p$$ ($$-a$$ a nonzero cube), $$\omega=1$$ with probability $$1/p$$ (the case $$p\mid a$$, easy to overlook and essential to the mean-value identity below), and $$\omega=0$$ with probability $$2(p-1)/3p$$; for $$p\equiv2\pmod 3$$ the cube map is a bijection and $$\omega=1$$ identically. Then: *(i)* [mean-value one, elementary lemma] $$\mathbb E_a[\omega(p)]=3\cdot\frac{p-1}{3p}+\frac1p=1$$ exactly at every $$p$$, so the derived mean of $$C(a)$$ is exactly $$1$$—the cubic analogue of the Korevaar–te Riele mean-value-one theorem for linear prime-pair constants (arXiv:0806.1667), here a one-line computation at each finite level; passing the mean through the infinite product needs more than almost-sure convergence, and the needed ingredient is on hand: the convergent variance sum makes the partial products an $$L^2$$-bounded martingale (each factor has mean $$1$$ and is independent of the earlier ones), so they are uniformly integrable and the limit law has mean exactly $$1$$, not merely limit-of-means $$1$$; *(ii)* [limit law] the empirical law of $$\{C(a):a\le A,\ a\ \text{a non-cube}\}$$ converges, as $$A\to\infty$$, to the law of the random Euler product $$\prod_{p\equiv1(3)}f_p(\xi_p)$$ with the three-state local variables $$\xi_p$$ above—independent at any finite set of primes exactly, by CRT, with the infinite product’s tail controlled by the convergent variance sum (unlike the quadratic family of Conjecture 10(iii), no normalization is needed)—with derived standard deviation $$0.2762\ldots$$ computed from the full three-state law; *(iii)* [uniformity] $$\#\{n\le N: n^3+a \text{ prime}\} =C(a)I_a(N)(1+o(1))$$ uniformly over non-cube $$a\le(\log N)^B$$.

The framework here is Kowalski’s theory of averages of Euler products and singular-series distributions [11], which proves such limit laws for $$k$$-tuple singular series; the one-parameter cubic shift family, its exact mean-one lemma, and the short-range uniformity appear unstated, and we present (ii) as an instance-level law inside that framework rather than a new mechanism. Computational checks: derived moments (mean exactly $$1$$, sd $$0.2762$$) against the $$294$$ non-cube shifts $$a\le300$$: empirical mean $$1.0215$$ ($$+1.5$$ profile standard errors), sd $$0.2481$$ (finite-family tail correlations account for the sd gap: for $$p>a_{\max}$$ the residues of $$a$$ are not yet equidistributed); uniformity profile over $$57$$ shifts at $$N=2\times10^5$$: mean $$z=+0.09$$, spread $$0.72$$, $$\max\vert z\vert =2.31$$. (The single instance $$a=2$$, $$C=1.298435\pm0.0003$$, verified at $$10^7$$ with $$z=+0.32$$, is included as the calibration member; no statement of Bunyakovsky type is proven for any cubic, the nearest theorem being Heath-Brown’s $$x^3+2y^3$$ [3], which is what keeps the whole family conjectural.)

*Computational checks (the classical single instance).* At $$a=2$$ and bound $$10^{7}$$: observed $$287{,}956$$ against predicted $$287{,}784.8$$, ratio $$1.0006$$, $$z=+0.32$$; the family-profile verification across the $$57$$ shifts is reported above.

**Conjecture 16** *(Conjecture F as a family; the core is previously stated, [1], cf. [23]).*

For odd $$A$$ let $$Q_A(N)=\#\{n\le N:\ n^2+n+A \text{ prime}\}$$ and $$C(A)=C(x^2+x+A)$$. Then, for every fixed $$B>0$$, $$Q_A(N)=C(A)\,I_A(N)\,(1+o(1))$$ uniformly over odd $$1\le A\le(\log N)^B$$, with the residual field obeying the analogue of Conjecture 8(ii), kernel derived and probability space specified: for $$t$$ uniform on $$[N,2N]$$ and window length $$H\le N^{o(1)}$$, let $$Q_A(t;H)=\#\{t<n\le t+H:\ n^2+n+A \text{ prime}\}$$ (mean $${\asymp}H/2\log N$$, which sets the regime). Two members share the index window, so with $$C(A,A')=C(x^2+x+A,\ x^2+x+A')$$,

$$
\operatorname{Cov}_t\bigl(Q_A,Q_{A'}\bigr)\;\sim\;
\bigl[C(A,A')-C(A)\,C(A')\bigr]\,\frac{H}{4\log^2N},
$$

with $$C(A,A')=0$$ (hence *negative* correlation) for the locally exclusive pairs. This is the *same-index* contribution only: the full covariance adds the off-index pinned sum

$$
\frac1{4\log^2N}\sum_{0<\vert h\vert \le H}(H-\vert h\vert )\,
\bigl[C(f_A(x),f_{A'}(x+h))-C(A)C(A')\bigr],
$$

the two-parameter analogue of Conjecture 2’s $$G(H)$$, whose evaluation is this family’s open component. (The order of this sum matters: the joint event here is *two single prime values* at distinct indices, of probability $$\asymp1/4\log^2N$$, unlike Conjecture 8’s pair-of-pairs events at $$1/\log^4x$$. At that order the off-index sum, which grows like a pinned $$G$$-average over $$\asymp H$$ shifts against the same-index term’s single $$H$$, is generically the *larger* component, so the numerical cancellation of the same-index kernel establishes nothing about the full cross-member covariance, and the localization of the observed profile deficit to the diagonal is an open question rather than an inference.) For $$H/\log N\to\lambda$$ the counts are jointly Poisson with local exclusions, and for $$H/\log N\to\infty$$ each fixed finite collection of studentized counts is asymptotically jointly normal with independent limiting coordinates, all correlations of size $$\asymp1/\log N$$ making both kernels finite-$$N$$ corrections to independence. As at Conjecture 8(ii), both distributional conclusions are asserted under an explicit hypothesis beyond the displayed covariances—uniform Hardy–Littlewood tuple estimates over the family, strong enough that every joint cumulant of order at least three of the studentized counts vanishes in the respective normalizations—since the covariance kernels alone do not determine the limit laws. (Uniformity over a range growing with $$N$$ is the substantive claim; uniformity over any *fixed* finite set of $$A$$ is logically automatic from the individual asymptotics.) Among odd $$A\le199$$, Euler’s $$A=41$$ has the largest constant, $$C(41)=6.6395463\ldots$$ (Cohen’s high-precision value [31]).

Numerical evaluation of the kernel (all odd $$A,A'\le99$$ at $$N=10^6$$: $$1{,}225$$ pairs, of which $$289$$ locally exclusive) returned a structurally clean answer: the positive correlations of admissible pairs and the negative correlations of exclusive pairs *cancel*, mean off-diagonal $$\rho=-0.003$$, so the derived *same-index* cross-member kernel is null. With the off-index sum at its correct order (larger, not smaller, than the same-index term), this cancellation does not license the conclusion that the members are asymptotically independent or that the observed profile variance $${\approx}0.37$$ must be diagonal; the natural reading remains that each $$\operatorname{Var}(Q_A)$$ is sub-Poisson through within-sequence pair correlations, the quadratic-family analogue of the Montgomery–Soundararajan deficit (Conjecture 13), but the off-index cross terms are an unevaluated competitor—and part of the spread is truncation noise in the constants themselves (the $$\pm10^{-3}$$ wobble moves each $$z_A$$ by $${\sim}0.3$$). Deriving the diagonal law and the off-index pinned sums is the family’s remaining open component, and the more important one; the numerical cancellation of the *same-index* cross-member kernel is a finite computation over $$A\le99$$, which localizes the deficit off the same-index diagonal without proving that the averaged kernel or the off-index contributions vanish—an analytic classification of the sign of $$C(A,A')-C(A)C(A')$$, and the evaluation of the two-parameter pinned sums, remain open. At $$N=10^6$$: mean ratio $$1.0006$$, standard deviation $$0.0027$$, $$\max\vert z\vert =1.92$$, rank correlation $$0.99988$$; for $$A=41$$, observed $$261{,}080$$ against predicted $$261{,}017.6$$ ($$z=+0.12$$, using Cohen’s constant). On precision: a truncated Euler product for $$C(41)$$ at cutoff $$2\cdot10^5$$ reads $$6.64092$$—wrong in the fourth significant decimal—because these conditionally convergent products drift at the $$10^{-3}$$ scale over practical cutoffs. Quoted digits for all quadratic-family constants in this paper are limited by the stated truncation wobble, not by the last printed digit. The entire $$10^8$$-bit primality dataset compresses to one product formula per $$A$$.

**Conjecture 17** *(Twin-member Goldbach, orientation-resolved; the basis conjecture and the integral kernel are Dubner’s [9]; the orientation decomposition apparently new).*

For even $$n$$ let $$R_T(n)$$ count ordered $$(a,b)$$, $$a+b=n$$, with $$a$$ and $$b$$ both members of twin pairs, each ordered role (lower/upper) counted. Each of the four role assignments is a $$4$$-form linear system in $$t=a$$ with root set $$\{0,\pm2\}\cup\{n,n\pm2\}$$-type mod each $$p$$, hence its own $$n$$-dependent singular series $$\mathfrak{S}_4^{(o)}(n)$$, and

$$
R_T(n)\;=\;\Bigl[\sum_{o}\mathfrak{S}_4^{(o)}(n)\Bigr]
\int_5^{n-5}\frac{dt}{\log^2t\,\log^2(n-t)}\;\bigl(1+o(1)\bigr),
$$

the four constants computed exactly per $$n$$ from the coincidence pattern of the root sets (which of $$n,n\pm2,n\pm4$$ each small prime divides). The error term is stated as $$(1+o(1))$$, not $$(1+O(1/\log n))$$: our own measurements show a second-order deficit whose $$1/\log n$$ coefficient is not yet pinned down (below). Two precision notes: the asymptotic runs over *varying* $$n$$, so what is assumed is a Hardy–Littlewood estimate for $$4$$-form systems *uniform in the $$n$$-dependent coefficients*—strictly stronger than the fixed-system conjecture—and the number $$5$$, the unique prime that is simultaneously a lower twin member (of $$(5,7)$$) and an upper one (of $$(3,5)$$), is double-counted consistently by the ordered-role convention, affecting finitely many representations per $$n$$ and no asymptotic.

Dubner’s paper already contains the integral kernel (his quotient $$\mu_4$$) and the qualitative basis conjecture; the content claimed here is the orientation-resolved singular series and its $$n$$-profile. Two exact identities compress the four orientations: the substitution $$t\mapsto n-t$$ exchanges the two summand roles, forcing $$\mathfrak{S}_4^{(\mathrm{lu})}(n)=\mathfrak{S}_4^{(\mathrm{ul})}(n)$$ identically (each of the $$(\mathrm{ll})$$ and $$(\mathrm{uu})$$ systems being self-dual under it), and the affine substitution $$t\mapsto t+2$$ gives $$\mathfrak{S}_4^{(\mathrm{uu})}(n)=\mathfrak{S}_4^{(\mathrm{ll})}(n-4)$$. So only one function of $$n$$ per symmetry class is free, and the profile is really two-dimensional; determining the average of $$\sum_o\mathfrak{S}_4^{(o)}(n)$$ over $$n$$ in closed form is a registered identity-hunting programme. Verified on $$150$$ log-sampled $$n\le10^8$$: the profile *shape* is confirmed at log-log correlation $$0.9993$$ across two decades, while the *level* runs at $$0.87$$ of prediction on $$[10^6,10^7)$$ and $$0.81$$ on $$[10^7,10^8)$$—a systematic deficit of second-order size ($${\approx}3.4/\log n$$ at the top range, the same order as the $$18$$–$$28\%$$ finite-height Poisson deficit of Conjecture 13), which we flag as the open component here rather than absorb into a fitted constant: either the $$4$$-tuple second-order correction accounts for it, or the orientation model needs repair, and the two are distinguishable at $$10^{10}$$. The *direction* of the trend is itself the anomaly: a genuine $$1-c/\log n$$ correction shrinks as $$n$$ grows, so a ratio moving *away* from $$1$$ across the decades indicates either a different error shape or a normalization problem, and settling which is part of what the open component must resolve. (The attributed benchmark stands inside the statement: every even $$n\ge4210$$ is a sum of two twin members, with the conjectured complete list of $$35$$ exceptions (OEIS A007534)—verified to $$10^8$$, re-swept to $$10^9$$, independently re-verified by a different algorithm, the same $$35$$ exceptions each time.)

## 5. Instances and structural companions

**Conjecture 18** *(Contamination in prime triplets; apparently new).*

The contamination calculus of Conjecture 1(v) extends to $$k$$-tuples, and the triplet pattern $$(n,\,n+2,\,n+6)$$ is its first instance beyond pairs. Of the three configurations placing a prime square inside the pattern, two die algebraically for $$q>3$$—$$(q^2,q^2+2,q^2+6)$$ by $$3\mid q^2+2$$, and $$(q^2-6,q^2-4,q^2)$$ because $$q^2-4=(q-2)(q+2)$$ is composite (at $$q=3$$ the factorization is trivial, $$q^2-4=5$$ is prime, and the single bounded exceptional configuration $$(3,5,9)$$ occurs—one term, harmless to every asymptotic)—leaving the single *doubly-thinned* survivor $$(q^2-2,\ q^2,\ q^2+4)$$, which requires $$q^2-2$$ *and* $$q^2+4$$ simultaneously prime and forces $$q\equiv\pm2\pmod5$$ for $$q\neq5$$ (else $$5\mid q^2+4$$; at $$q=5$$ all three conditions do hold, the configuration being $$(23,25,29)$$, but its start $$23\equiv3\pmod5$$ lies outside the triplet start classes $$\{1,2\}$$, so the single term is harmless). Triplet starts lie in classes $$n\equiv1,2\pmod 5$$, and the surviving configuration has start $$q^2-2\equiv2$$: class $$2$$ is contaminated and class $$1$$ leads, in the drift-scale form of Conjecture 1(i) (a normalization at the noise scale, $$\mathcal{M}_x((D-T_3)/\sqrt{\pi_3})$$, would be vacuous for the coefficient, exactly as at the pair races):

$$
\mathcal{M}_x\!\left(
\frac{\bigl(\pi_3(t;5,1)-\pi_3(t;5,2)\bigr)\log^3t}{\sqrt t}\right)
\to c_3:=\lim_{x\to\infty}\frac{T_3(x)\log^3x}{\sqrt x},
\quad
T_3(x)=\frac1{\log^3x}\!\!
\sum_{\substack{q\le\sqrt x,\ q\neq5\\ q^2-2,\ q^2+4\ \mathrm{prime}}}
\!\!\log(q^2-2)\log q\,\log(q^2+4)
$$

($$c_3$$ exists and is the Bateman–Horn constant of the triple $$(q,\,q^2-2,\,q^2+4)$$, since the census sum is $$\sim c_3\sqrt x$$; convergence of the logarithmic mean at this normalization is the same Rubinstein–Sarnak-type structure hypothesis as at Conjecture 1(i)), with drift-to-noise $$\asymp\log^{-3/2}x$$—one logarithm weaker than the pair races, a scale the calculus itself predicts and the verification must respect. The mechanism clause and the averaging clause are asserted separately, as at Conjecture 1(i).

This is the calculus applied at tuple level: the configuration census, the double thinning, and the mod-5 class assignment are all forced, and the prediction was derived before the data were taken. At $$10^9$$: classes $$189{,}837$$ against $$189{,}670$$ ($$D=+167$$ on the predicted side; $$T_3=+25$$ against noise $$616$$, so the endpoint is uninformative exactly as the $$\log^{-3/2}$$ law requires), leadership log-density $$0.65$$ ($$+0.8$$ null standard deviations at the occupation constant of Conjecture 14(ii)—directionally consistent, sharpness unavailable at this height by the calculus’s own accounting). (The Chernick chain $$\{p,2p-1,3p-2\}$$—the population behind the universal-form Carmichael numbers, quantified by Dubner [10]—is included as an attributed calibration benchmark: $$C=2.858249$$, observed $$125{,}379$$ against predicted $$125{,}429.4$$ at $$3\times10^8$$, $$z=-0.14$$.)

*Computational checks.* The triplet-race data and the Chernick-chain calibration count are reported at the statement above.

**Conjecture 19** *(The contamination matrix: sexy pairs with two surviving orientations; apparently new).*

For the pattern $$(n,n+6)$$, *both* prime-square orientations survive, on complementary classes of $$q$$ mod $$5$$—the first matrix instance of the calculus (every pair race so far had exactly one): orientation $$A=(q^2-6,\,q^2)$$ requires $$q^2-6$$ prime, forcing $$q\equiv\pm2\pmod5$$ for $$q\neq5$$ (at $$q=5$$ the value $$19$$ is prime, but its start $$19\equiv4\pmod5$$ lies outside the sexy start classes $$\{1,2,3\}$$), and lands in start class $$3$$ (mod $$5$$), class $$3$$ (mod $$8$$); orientation $$B=(q^2,\,q^2+6)$$ requires $$q^2+6$$ prime, forcing $$q\equiv\pm1\pmod5$$ (the term $$q=5$$ falls outside the start classes), and lands in class $$1$$ (mod $$5$$), class $$1$$ (mod $$8$$). Sexy starts occupy classes $$\{1,2,3\}$$ mod $$5$$ and $$\{1,3,5,7\}$$ mod $$8$$; with $$T_{A}(x)=\frac1{\log^2x}\sum_{q^2-6\ \mathrm{prime},\,q\neq5}\log q\log(q^2-6)$$, $$T_{B}(x)=\frac1{\log^2x}\sum_{q^2+6\ \mathrm{prime},\,q\neq5}\log q\log(q^2+6)$$, and $$c_A,c_B$$ their drift-scale limits ($$c_A=\lim T_A\log^2x/\sqrt x$$, the Bateman–Horn constant of $$(q,q^2-6)$$, likewise $$c_B$$ for $$(q,q^2+6)$$), the predicted drift vector, in the drift-scale limiting-log-mean sense of Conjecture 1(i) (an $$\mathcal{M}_x$$-over-$$\sqrt\pi$$ normalization would be coefficient-blind), is: mod 5: $$\mathcal{M}_x\bigl((\pi(2)-\pi(3))\log^2t/\sqrt t\bigr)\to c_A$$, $$\mathcal{M}_x\bigl((\pi(2)-\pi(1))\log^2t/\sqrt t\bigr)\to c_B$$ (class $$2$$ *clean*); mod 8: $$\mathcal{M}_x\bigl((\tfrac12(\pi(5)+\pi(7))-\pi(3))\log^2t/\sqrt t\bigr)\to c_A$$, $$\mathcal{M}_x\bigl((\tfrac12(\pi(5)+\pi(7))-\pi(1))\log^2t/\sqrt t\bigr)\to c_B$$ (classes $$5,7$$ clean, mutually symmetric, with $$\mathcal{M}_x\bigl((\pi(5)-\pi(7))\log^2t/\sqrt t\bigr)\to0$$). Two independently computable drift constants, one certified null class per modulus. The mechanism clause and the averaging clause are asserted separately, as at Conjecture 1(i).

The matrix structure—two orientations feeding disjoint classes on complementary $$q$$-classes, with an interior null—is what distinguishes this from every single-orientation race, and it tests the calculus beyond its balanced one-mechanism cases; the class assignments were verified independently before the data were taken. At $$10^9$$ the predicted components ($$T_A=191$$, $$T_B=110$$) sit far inside the noise ($$\approx2{,}100$$), as the $$1/\log x$$ law forces; all four measured components and the $$5$$–$$7$$ control lie within one noise unit of their predictions (trivially, at this height), and the four leadership log-densities $$(0.48,0.56,0.53,0.73)$$ sit at $$(-0.1,+0.3,+0.1,+1.2)$$ null standard deviations (occupation constant $$0.18$$): three at the null, the mod-8 $$B$$-component mildly positive on the predicted side. The matrix is *registered and consistent*, with sharpness unavailable below $${\sim}10^{14}$$ by the calculus’s own accounting. (The pair $$\{p,\ p^2-2\}$$, OEIS A062326, $$C=3.383216$$, the input that sets Conjecture 1’s drift scale, is included as an attributed calibration benchmark: verified at $$10^7$$, $$z=-1.31$$, independently recomputed to $$10^9$$; a refutation of its infinitude would remove the twin race’s predicted mechanism.)

*Computational checks.* The sexy-pair race data are reported at the statement above; independent recomputation of this conjecture’s calibration member, the pair $$\{p,p^2-2\}$$, gave $$3.383227$$, with primes to $$10^9$$—inside our stated wobble—and an independent count to $$3\times10^7$$ with final ratio $$0.9965$$.

**Conjecture 20** *(Fibonacci–Lucas twins: the convergent side stress-tested; the object is OEIS A080327).*

*(i)* [rank-disjointness, elementary, with its exception stated] every *odd* prime factor $$r$$ of $$L_p$$ has rank of apparition exactly $$2p$$ (from $$z(r)\mid2p$$, $$z(r)\nmid p$$, and $$z(r)=2$$ being impossible), and every prime factor of $$F_p$$ ($$p\neq5$$ prime) has rank exactly $$p$$: the odd divisor pools of the two numbers are disjoint. The prime $$2$$ is the unique exception: $$2$$ divides both $$F_p$$ and $$L_p$$ precisely when $$p=3$$ ($$F_3=2$$, $$L_3=4$$; $$\gcd(F_p,L_p)=2$$ iff $$3\mid p$$)—the restriction to odd divisors is essential, the clause being false at $$p=3$$ without it. Disjoint pools remove shared-*prime* correlation but not all correlation: dependence can still enter through the order structure of the recurrence, which is why (iii) matters; *(ii)* [finiteness] only finitely many primes $$p$$ have $$F_p$$ and $$L_p$$ simultaneously prime; *(iii)* [calibration clause, quantitative] the naive joint accounting—probability $$(\mathrm{e}^{\gamma}\log p/(p\log\phi))^2$$ per index—assigns the catalogued index $$p=148091$$ (OEIS A080327; *both* $$F_p$$ and $$L_p$$ are *probable* primes—numbers of roughly $$30{,}950$$ digits, with Lucas numbers proved prime only up to index $$56003$$—so everything recorded here is conditional on both probable-prime classifications, for which no Baillie–PSW pseudoprime is known: no unconditional refutation is claimed from uncertified numbers) prior mass about $$3\times10^{-3}$$ beyond $$10^4$$. That rare-event datum is recorded descriptively, with no significance claim attached to it: the model was examined after the event was known, and no test protocol was fixed in advance. A single surprising event is not a strict refutation, and it does not by itself estimate the *size* of the correction: an underestimated constant, genuine cross-dependence, and a mis-calibrated finite-range tail are competing explanations that one event cannot separate. What the datum does bear on (conditionally as above) is not the model but the list: it is fatal to any Goldilocks completeness list; the conjectural content of (ii) is that even the corrected accounting has convergent sum.

This conjecture is our stress test of the convergent Borel–Cantelli template that Conjecture 21 exemplifies. The joint scan to $$p\le10^4$$ found exactly the indices $$\{5,7,11,13,17,47\}$$, with expected further mass $$1.6\times10^{-3}$$, while the catalogued index $$148091$$, at which $$F_p$$ and $$L_p$$ are both probable primes, lies beyond that range. We therefore conjecture finiteness *without* a completeness clause. The lesson, in the language of Grantham–Granville [7], is that recurrence-sequence constants need their local corrections *before* tail masses are trusted. The single-sided calibration (probable-prime counts: $$F_p$$ and $$L_p$$ leave the deterministic range at very small $$p$$): $$25$$ Fibonacci prime indices $$\le10^4$$ against the naive screening prediction $$34.1$$ ($$z=-1.6$$, a deficit confirmed by independent recomputation); $$29$$ Lucas prime indices $$\le10^4$$; the corrected $$c_F$$ needs a Granville-type patch, and clause (iii) quantifies the same need at the joint level.

*Computational checks.* Joint scan and single-sided calibration reported at the statement (Fibonacci prime indices $$\{3,5,7,\dots,9311,9677\}$$, $$25$$ of predicted $$34.1$$, $$z=-1.56$$; Lucas indices $$29$$; joint $$\{5,7,11,13,17,47\}$$ to $$10^4$$)—probable-prime counts at all but the smallest indices, the Fibonacci and Lucas values leaving the deterministic range almost at once.

**Conjecture 21** *(Factorial twins; the uniqueness core is previously stated, OEIS A088054; clauses (i) and (iii) are ours).*

*(i)* [window rigidity, elementary] for $$n\ge4$$ and $$2\le\vert a\vert \le n$$ the number $$n!+a$$ is composite (any prime factor $$p$$ of $$a$$ satisfies $$p\le n$$, so $$p\mid n!+a$$, and $$n!+a>n\ge p$$); the two small anomalies $$2!-2=0$$ and $$3!-3=3$$ are the only exceptions, which is why the clause is restricted to $$n\ge4$$. Hence among all offsets of bounded size the only candidates for primality near $$n!$$ are $$a=\pm1$$: the twin question below is the *unique* bounded-offset constellation question at $$n!$$, and every admissible offset set is a subset of $$\{-1,+1\}$$. *(ii)* [uniqueness; previously stated] Only finitely many $$n$$ have $$n!-1$$ and $$n!+1$$ simultaneously prime, and the complete list is $$n=3$$: i.e. $$6=3!=3\#$$ is the unique factorial lying between twin primes. *(iii)* [joint fluctuation model] the two single-sided counts $$F_{\pm}(N)=\#\{n\le N:\ n!\pm1 \text{ prime}\}$$ are each $$\sim\mathrm{e}^{\gamma}\log N$$ and, *under the independent-indices model stated below*, asymptotically independent, with $$F_{+}-F_{-}$$ normalized by $$\sqrt{2\mathrm{e}^{\gamma}\log N}$$ asymptotically standard normal. The probability space is declared: the clause is about a random model in which the events $$E_n^{\pm}=\{n!\pm1\ \text{prime}\}$$ carry the Caldwell–Gallot marginal hazards $$\mathrm{e}^{\gamma}/n$$ with an *unspecified* dependence structure, and the Gaussian limit is asserted under three explicit hypotheses on that structure: the same-index bound $$\sum_{n\le N}\bigl\vert \operatorname{Cov}(\mathbf 1_{E_n^+},\mathbf 1_{E_n^-})\bigr\vert =o(\log N)$$, which pins the variance at $$2\mathrm{e}^{\gamma}\log N\,(1+o(1))$$ and which the joint law $$\sim(\mathrm{e}^{\gamma}/n)^2$$ derived below supplies with a convergent sum — without it the remaining hypotheses leave the second cumulant free, and a model with $$\Pr(E_n^+\cap E_n^-)=\mathrm{e}^{\gamma}/2n$$ halves the limiting variance; the cross-index covariance bound $$\sum_{m<n\le N}\bigl\vert \operatorname{Cov}(\mathbf 1_{E_m}, \mathbf 1_{E_n})\bigr\vert =o(\log N)$$ over the four sign pairs (the variance itself is $$\asymp\log N$$), *and*—since pairwise control alone cannot preclude higher-order dependence—the higher-cumulant condition $$\kappa_r(F_+-F_-)=o\bigl((\log N)^{r/2}\bigr)$$ for each fixed $$r\ge3$$, the method-of-moments sufficient condition. Neither is imported from an independence model; whether they hold for the arithmetic dependence across factorial indices is the open component of this clause.

Each event separately has Caldwell–Gallot probability $$\sim\mathrm{e}^{\gamma}/n$$ [4] and divergent sum (the $$n!+1$$ side is the classical law retained as calibration at Conjecture 2); the *joint* event has probability $$\sim(\mathrm{e}^{\gamma}/n)^2$$, whose sum converges. This is our exemplar of the convergent side of the Borel–Cantelli dichotomy—the accounting that predicts finitude rather than infinitude. The at-a-common-index independence in (iii) has a derivation: a generic twin pair near $$n!$$ would carry the Hardy–Littlewood twin factor $$2C_2\prod_{2<p\le n}\frac{p-2}{p-1}\big/ \prod_{2<p\le n}\bigl(\tfrac{p-1}p\bigr)^{\!2}$$-type couplings, but here the screening (coprimality to all $$p\le n$$) is *deterministic*—both neighbors always pass it—and the twin coupling factor and the reciprocal sieve factors cancel to first order, leaving the joint probability $$\sim(\mathrm{e}^{\gamma}/n)^2$$ with no singular-series correlation; what remains open, and is flagged in (iii), is dependence *across* distinct indices $$n$$, whose divisibility structures are nested. That open component has a concrete first computation, which we register as a programme: for $$m<n$$ and a prime $$p>n$$, the residues $$m!\bmod p$$ and $$n!\bmod p$$ are deterministically linked by $$n!=m!\cdot(m{+}1)\cdots n$$, so the covariance of the events $$p\mid m!\pm1$$ and $$p\mid n!\pm1$$ is an explicit character-sum average over the multiplier $$(m{+}1)\cdots n$$; summing it over $$p$$ either bounds the cross-index dependence at $$o(1/n)$$—vindicating the independent-indices model—or exhibits genuine coupling, and the computation is finite at each height. Verified for $$n\le700$$ ($$F_+=14$$, $$F_-=16$$: difference $$-2$$ against noise scale $$\approx4.8$$); the model-expected number of further twin examples beyond $$700$$ is $$\mathrm{e}^{2\gamma}/700\approx4.5\times10^{-3}$$ (computed tail). The defensible core is finiteness; the exact one-element list is the Goldilocks-maximal form—strictly stronger than the tail estimate can guarantee. On priority: the exact uniqueness conjecture is on the public record, OEIS A088054 stating that $$3$$ is conjecturally the intersection of A002981 and A002982, so clause (ii) is attributed there and our contribution here is clauses (i) and (iii).

The primorial analogue—$$p\#\pm1$$ both prime only for $$p\in\{3,5,11\}$$—is due to Lillie [5], whose abstract gives both the $$O(n^{-2})$$ joint probability and the prediction that there are three instances in total; it is included here as an attributed calibration benchmark, independently verified to $$p\le4000$$.

*Computational checks* (probable-prime count for $$n$$ beyond about $$26$$). Exhaustive to $$n\le700$$: the only factorial twin is $$n=3$$; individually, $$n!+1$$ is prime for $$n\in\{2,3,11,27,37,41,73,77,116,154,320,340,399,427\}$$ and $$n!-1$$ for $$n\in\{3,4,6,7,12,14,30,32,33,38,94,166,324,379,469,546\}$$—two divergent single-sided laws straddling their shared constant while the joint count stops at one, the convergent accounting in action. (The primorial companion, attributed to Lillie [5]: exhaustive to $$p\le4000$$, twins exactly $$\{3,5,11\}$$, with $$p\#+1$$ prime for eleven $$p$$ against the Caldwell–Gallot prediction $$14.8$$, $$z=-0.98$$; again a probable-prime count above the deterministic range.)

**Theorem 1** *(Cube obstruction).*

For $$k\ge2$$, the cube $$k^3$$ is representable as $$p+j^3$$ with $$p$$ prime, $$j\ge1$$, if and only if $$3k^2-3k+1$$ is prime. Consequently the set of integers not representable as $$p+k^3$$ is infinite: the non-representable *cubes* alone have counting function $$\sim x^{1/3}$$. (That the full exceptional set is $$\sim x^{1/3}$$ follows only when combined with Conjecture 22(i), and is conjectural.)

*Proof.* $$k^3-j^3=(k-j)(k^2+kj+j^2)$$; for $$1\le j\le k-2$$ both factors exceed $$1$$, so the difference is composite. The only candidate is $$j=k-1$$, giving $$3k^2-3k+1$$. Since $$3k^2-3k+1$$ is composite for a density-one set of $$k$$ (all but $$O(K/\log K)$$ of $$k\le K$$, by an upper-bound sieve of Brun or Selberg type applied to the quadratic’s prime values), all but a vanishing proportion of cubes are unrepresentable. $$\square$$

The restriction to non-cubes in the next conjecture is therefore essential: the exception set of $$n=p+k^3$$ over *all* $$n$$ is infinite, and the cubes are exactly what makes it so. The effect is visible immediately in the data—all $$412$$ exceptions found in $$(10^8,10^9]$$ are perfect cubes—and it is invisible to a Borel–Cantelli sum taken over all $$n$$, since the cubes have density zero. The cube lane is not lost, only relocated: by Theorem 1 it is governed by the primality of $$3k^2-3k+1$$, which is a Bateman–Horn family in its own right and appears as such in Conjecture 22.

**Conjecture 22** *(The boundary trichotomy for polynomial ladders; the divisibility principle is classical and its cubic case is Cunningham’s cuban observation (OEIS A002407); the family classification is apparently new).*

For $$F\in\mathbb Z[x]$$ with $$\deg F\ge2$$ and *positive leading coefficient*, and $$m>j\ge1$$, $$(m-j)\mid F(m)-F(j)$$ (textbook), and the divided difference $$(F(m)-F(j))/(m-j)$$—whose leading form is then positive on the cone $$m>j\ge1$$—exceeds $$1$$ outside an effectively bounded region; so $$F(m)-F(j)$$ prime forces $$m-j=1$$ apart from finitely many exceptional pairs (for the family below the exceptional set is provably *empty*). Both hypotheses are necessary: for $$\deg F=1$$ the cofactor can be identically $$1$$ and the collapse fails, and for negative leading coefficient the divided difference tends to $$-\infty$$ on the cone, so the “exceeds $$1$$” clause would be false as stated (one may equivalently keep general sign and read the claim through $$\vert F(m)-F(j)\vert$$). Every representation problem $$F(m)=p+F(j)$$ in this range thus collapses to the boundary polynomial $$D_F(m)=F(m)-F(m-1)$$. The content is the classification of the boundary lanes. For $$F=x^3+cx$$, $$c\ge0$$: *(i)* [trichotomy, elementary] $$D_F=3m^2-3m+1+c$$ and the lane is *dead-parity* for $$c$$ odd ($$D_F$$ always even), *dead-3-adic* for even $$c\equiv2\pmod3$$ ($$3\mid D_F$$ always), and admissible exactly for $$c\equiv0,4\pmod6$$; *(ii)* [uniform boundary law] over the admissible lanes, $$\#\{m\le M: D_F(m) \text{ prime}\}\sim C(D_F)\,I(M)$$ uniformly for $$c\le(\log M)^B$$—a Bateman–Horn family whose members are indexed by the ladder classification; *(iii)* [attributed core] the case $$c=0$$ is the cuban ladder: Cunningham’s classical observation that a prime difference of cubes forces consecutive arguments, with the non-cube exceptional set of $$n=p+k^3$$ finite (Hardy–Littlewood’s $$E_3(X)=O(1)$$ [1]).

The reducible-boundary phenomenon is part of the same classification: $$F=x^4$$ has $$D_F=(2m-1)(2m^2-2m+1)$$—the boundary lane itself factors, which is precisely the composite-$$k$$ obstruction of Conjecture 23 seen from the ladder side, and $$F=x^3+x^2$$ gives $$D_F=m(3m-1)$$, dead by reducibility. Verified: the collapse is algebraically empty for $$x^3+cx$$ ($$c\ge0$$), the trichotomy checked to $$m=5000$$ on all $$c\le12$$, and the two smallest admissible new lanes counted at $$M=10^6$$: $$c=4$$ ($$C=2.12956$$, $$z=+0.27$$) and $$c=6$$ ($$C=2.68954$$, $$z=-0.92$$). (Empirically the non-cube exception census of (iii) by decade is $$4,\,27,\,168,\,763,\,2011,\,2808,\,1181,\,88$$ up to $$10^8$$, peaking at the sixth decade and collapsing thereafter, largest found $$78{,}526{,}384$$.)

**Conjecture 23** *(The power-obstruction ladder: an elementary structural proposition with a Bateman–Horn corollary; apparently new as a family).*

For $$k\ge2$$ and $$m\ge2$$, write $$D_k(m)=m^k-(m-1)^k$$, and call $$m^k$$ representable if $$m^k=p+j^k$$ for some prime $$p$$ and $$j\ge1$$. Then: *(i)* [theorem] for *composite* $$k$$, no $$k$$-th power is representable: if $$r$$ is a proper divisor of $$k$$ with $$r>1$$ (such $$r$$ exists precisely because $$k$$ is composite; the excluded value $$r=1$$ would allow only the useless factor $$m-j=1$$ at $$j=m-1$$), then for every $$1\le j<m$$ the difference $$m^k-j^k$$ has the proper factor $$m^r-j^r>1$$ with cofactor $$>1$$; *(ii)* [elementary] for *prime* $$k$$ (including $$k=2$$), $$m^k$$ is representable if and only if $$D_k(m)$$ is prime; and $$D_k$$ is irreducible for prime $$k$$ (a root $$\alpha$$ has $$(\alpha/(\alpha-1))^k=1$$ with $$\alpha/(\alpha-1)\neq1$$, so $$\zeta=\alpha/(\alpha-1)$$ is a primitive $$k$$-th root of unity and $$\mathbb Q(\alpha)=\mathbb Q(\zeta)$$ has degree $$k-1=\deg D_k$$, forcing irreducibility; explicitly $$D_k(x)=(x-1)^{k-1}\,\Phi_k(x/(x-1))$$. The forcing $$j=m-1$$ needs only $$k\ge2$$); *(iii)* [conjecture] for each prime $$k\ge3$$ the representable lane follows Bateman–Horn ($$k=2$$ is a theorem, the prime number theorem on the lane $$2m-1$$): $$\#\{m\le M:\ D_k(m) \text{ prime}\}\sim C_k\int_2^M dt/\log D_k(t)$$.

The dividing line is prime versus composite $$k$$, not odd versus even: for *odd* composite $$k=rs$$ the factorization of clause (i) applies verbatim, so that $$D_9(m)$$, for instance, is *never* prime. This was checked directly for $$k=9,15,21,25,27,33$$—no prime value of $$D_k$$ occurs up to $$m=2000$$, and the predicted divisor $$D_r(m)\mid D_k(m)$$ is present identically—and it is the same algebraic mechanism, seen from the ladder side, that Theorem 1 exhibits for cubes. The family generalizes the cubic case $$k=3$$ of Conjecture 22.

*Computational checks.* The even-rung theorem was checked numerically to $$10^8$$ (no fourth power is $$p+j^4$$); the three verifiable Bateman–Horn lanes $$k=2,3,5$$ (constants $$2$$ exactly, $$3.36181$$, and $$3.67770\pm0.007$$, the quartic product computed by brute-force root counts to $$10^5$$) all sit within $$\vert z\vert <0.6$$: at bound $$10^{7}$$ the lane $$k=2$$ gives observed $$1{,}270{,}606$$ against predicted $$1{,}270{,}902.8$$ (ratio $$0.9998$$, $$z=-0.26$$); at $$10^{6}$$ the lane $$k=3$$ gives $$126{,}826$$ against $$126{,}641.6$$ (ratio $$1.0015$$, $$z=+0.52$$); and at $$8\cdot10^{5}$$ the lane $$k=5$$ gives $$56{,}925$$ against $$57{,}021.3$$ (ratio $$0.9983$$, $$z=-0.40$$).

**Conjecture 24** *(The alternating cyclotomic chain; apparently new).*

There are infinitely many primes $$p$$ such that, writing $$u=\Phi_3(p)=p^2+p+1$$, the three integers

$$
p,\qquad u=p^2+p+1,\qquad
\Phi_6(u)=u^2-u+1=p^4+2p^3+2p^2+p+1
$$

are all prime, with $$\#\{p\le x\}\sim C_6^{\mathrm{ch}}\,I(x)$$ for the Bateman–Horn system $$\{x,\ x^2+x+1,\ x^4+2x^3+2x^2+x+1\}$$, $$C_6^{\mathrm{ch}}=3.6143\pm0.011$$. The first chains are $$(2,7,43)$$ and $$(3,13,157)$$.

This is the repunit analogue of a Cunningham chain: a prime base $$p$$, its length-3 repunit $$u=(p^3-1)/(p-1)$$, then $$(u^3+1)/(u+1)$$. The chain must *alternate* between $$\Phi_3$$ and $$\Phi_6$$: the naive iterate $$\{p,\ \Phi_3(p),\ \Phi_3(\Phi_3(p))\}$$ is *inadmissible*—if $$p\equiv2\pmod3$$ then $$u\equiv1\pmod3$$, so $$3\mid\Phi_3(u)$$ always, while $$p\equiv1\pmod 3$$ forces $$3\mid u$$, so the admissibility check rejects the naive chain outright. The uniqueness claim is made over a specified construction space: among length-3 chains $$\{x,\ \Phi_j(x),\ \Phi_k(\Phi_j(x))\}$$ with $$j,k\in\{3,6\}$$ *extending the repunit sub-chain* (i.e. $$j=3$$), the mod-3 arithmetic above forces $$k=6$$: alternation is the unique admissible continuation. (Dropping the repunit anchor admits one sibling, the pure-$$\Phi_6$$ chain $$\{x,\Phi_6(x),\Phi_6(\Phi_6(x))\}$$ on the complementary lane $$x\equiv1\pmod3$$; since $$\Phi_6(x)=\Phi_3(x-1)$$, its second element is again a repunit value, and we regard the classification of all admissible words in the two-letter alphabet $$\{\Phi_3,\Phi_6\}$$—which words are obstruction-free at every prime, and whether they form a regular language—as a natural open programme.) The length-2 sub-chain $$\{p,\ p^2+p+1\}$$ is the classical cyclotomic Sophie Germain statement, included here as an attributed calibration benchmark ($$C=1.521661\pm0.0005$$, catalogue value $$1.5217315\ldots$$, OEIS A188596; verified at $$z=-1.06$$ at $$10^7$$): infinitely many prime bases have prime repunits of length $$3$$, the base-independent home of the phenomenon whose base-2 shadow is the Mersenne sequence. The length-3 chain stated here is, as far as we can find, unstated, and its quartic layer makes it the highest-degree system in this paper.

*Computational checks.* At bound $$10^{7}$$: observed $$1{,}362$$ against predicted $$1{,}357.2$$, ratio $$1.0035$$, $$z=+0.13$$. The chain census by decade is $$4,\ 11,\ 41,\ 224,\ 1362$$ at $$N=10^3,\dots,10^7$$ (a probable-prime count for the quartic layer beyond $$p\approx2\times10^6$$; $$z$$ from $$+0.40$$ to $$+0.13$$, no drift), the quartic layer’s singular series computed by brute-force root counts to $$10^5$$; the retained sub-chain benchmark $$\{p,\,p^2+p+1\}$$ stands at $$33{,}661$$ against $$33{,}855.5$$ at $$10^7$$ ($$z=-1.06$$). Independent recomputation of that calibration member, the Sophie Germain sub-chain, gave $$1.521730$$, with primes to $$10^9$$—inside our stated wobble—and an independent count to $$3\times10^7$$ with final ratio $$0.9962$$.

**Conjecture 25** *(Twin cyclotomic bases: the complete quadratic family; no prior trace found).*

For the three cyclotomic polynomials of degree $$2$$ (indices $$k$$ with $$\varphi(k)=2$$, i.e. $$k\in\{3,4,6\}$$), consider $$\Phi_k(n)$$ and $$\Phi_k(n+1)$$ simultaneously prime. Then: *(i)* [parity obstruction, elementary] for $$k=4$$ one member of the pair $$(n^2+1,\,n^2+2n+2)$$ is even for *every* $$n$$, so the only prime pair is $$n=1$$, giving $$(2,5)$$—the same obstruction that forbids consecutive $$n^2+1$$ primes; *(ii)* [collapse, elementary] $$\Phi_6(x)=\Phi_3(x-1)$$ identically, so the $$k=6$$ pair at index $$n$$ *is* the $$k=3$$ pair at index $$n-1$$: the family contains exactly one nontrivial statement; *(iii)* [conjecture, the live instance] there are infinitely many $$n$$ for which the length-3 repunits in bases $$n$$ and $$n+1$$ are simultaneously prime: $$\#\{n\le N:\ \Phi_3(n)=n^2+n+1 \text{ and } \Phi_3(n+1)=n^2+3n+3 \text{ both prime}\}\sim C_5\,I(N)$$, with $$C_5=C(x^2+x+1,\,x^2+3x+3)$$.

Both forms in (iii) are odd for every $$n$$ (each is $$\Phi_3$$ of an integer), and mod $$3$$ each vanishes on exactly one class ($$n\equiv1$$ and $$n\equiv0$$ respectively), so the pair is admissible with $$\omega(3)=2$$. Unlike an arbitrary shifted pair, the companion here is structurally forced: it is the same cyclotomic value at the consecutive base, making this the natural “twin” statement inside the cyclotomic-chain family of Conjecture 24. The family analysis (i)–(ii) is what a family *lift* of the statement uncovers, and both clauses were found by the admissibility computation itself: the $$k=4$$ branch was rejected as inadmissible at $$p=2$$ at singular-series time (both-odd count to $$10^6$$: zero, prime pairs: $$n=1$$ only), and the $$k=6$$ run returned counts *identical* to $$k=3$$, which is the numerical shadow of the polynomial identity in (ii).

*Computational checks.* $$C_5=2.964239\pm0.002$$; at bound $$10^{7}$$, observed $$33{,}274$$ against predicted $$32{,}976.7$$, ratio $$1.0090$$, $$z=+1.64$$.

## Part II: structural conjectures in five programmes

The twenty-five conjectures below are organized by mechanism rather than by the contamination calculus of Part I. Each names a canonical object and averaging law, identifies an arithmetic, geometric, spectral, or adelic source, and states a first decisive theorem and a failure mode.

### Programme I: connected prime-pattern fields

Let $$H\subset\mathbb Z$$ be finite and admissible, and write

$$
\Lambda_H(n)=\prod_{h\in H}\Lambda(n+h),\qquad
 Y_H(x,L)=\sum_n w\!\left(\frac{n-x}{L}\right)
 \bigl(\Lambda_H(n)-\mathfrak S(H)\bigr),
$$

where $$w$$ is a fixed smooth compactly supported function and $$\mathfrak S(H)$$ is the Hardy–Littlewood singular series $$\prod_p(1-\nu_H(p)/p)(1-1/p)^{-\vert H\vert }$$, with $$\nu_H(p)$$ the number of residue classes occupied by $$H$$ modulo $$p$$. The window position $$x$$ is sampled from $$[X,2X]$$ with density $$dx/(x\log2)$$ and $$X^\varepsilon\le L\le X^{1-\varepsilon}$$. For translated motifs $$H_i+t_i$$, their *exact overlap type* records every equality among shifted prime constraints. The connected singular series $$\mathfrak S^{\mathrm c}(K_1,\ldots,K_r)$$ is obtained by Möbius inversion over set partitions of the indexed tuple $$(K_1,\ldots,K_r)$$.

**Connected motif generating functional (Conjecture 26).** Fix admissible motifs $$H_1,\ldots,H_m$$ and put

$$
\mathcal Z_{X,L}(\mathbf z)=
 \mathbb E_x\exp\!\left(\sum_{i=1}^m z_iY_{H_i}(x,L)\right).
$$

For every fixed total degree $$R$$, the degree-$$\le R$$ Taylor polynomial of $$\log\mathcal Z_{X,L}$$ has a uniform asymptotic expansion indexed by connected exact- overlap diagrams of at most $$R$$ translated motifs. A diagram whose coincidence hypergraph connects the $$r$$ translated sets $$H_{i_1}+t_1,\ldots,H_{i_r}+t_r$$ contributes, at the leading order of its stratum,

$$
W_\tau(L;\mathbf t)\,
 \mathfrak S\Bigl(\bigcup_{j=1}^r(H_{i_j}+t_j)\Bigr)
 \prod_v(\log X)^{m_v-1},
$$

where $$W_\tau(L;\mathbf t)=L\int_{\mathbb R}\prod_{j=1}^rw(u+t_j/L)\,du$$ is the archimedean window-overlap weight of the diagram and $$m_v$$ is the multiplicity of the prime constraint at $$v$$: any set partition that separates a coincidence loses at least one factor of $$\log X$$, so the Möbius alternation leaves the single-block moment as the leading term of a connected diagram. The same alternation cancels the leading terms of disconnected diagrams, whose contribution is carried by the connected singular series of their disjoint blocks at strictly smaller logarithmic order, reducing for the fully disjoint type to $$\mathfrak S^{\mathrm c}(H_{i_1}+t_1,\ldots,H_{i_r}+t_r)$$ with no logarithmic enhancement. The log powers are therefore partition dependent and are never factored across the alternation, and every prime-power counterterm is included in the local weight attached to its multiplicity. Ordering terms lexicographically by powers of $$L$$ and $$\log X$$, the remainder after any fixed truncation is smaller than the last retained scale, uniformly in the mesoscopic range.

*Significance.* This is a multitype connected field theory for prime constellations. It simultaneously organizes covariance, odd moments, mixed motifs, overlap singularities, and lower-order prime-power effects. Montgomery–Soundararajan and Kuperberg provide the closest one-field moment frameworks, while constrained singular-series sums provide the nearest local input [19, 34, 35]. The new content is the complete connected multitype functional. The first decisive theorem is the full third-cumulant formula for two distinct pair motifs.

**Complete overlap-renormalization filtration (Conjecture 27).** Fix a finite motif family $$H_1,\ldots,H_m$$. Apply the degree-two specialization of Conjecture 26 and order all of its connected covariance strata by their asymptotic scales $$s_1\succ s_2\succ\cdots$$ (lexicographically in powers of $$L$$, $$\log X$$, and the renormalized disjoint scales). In the mesoscopic range scales sharing the same total power of $$L$$ and of logarithms differ only by powers of $$\theta=\log L/\log X$$ and merge into a single stratum whose limiting form is polynomial in $$\theta$$. The filtration, the graded convergence, and the eigenvalue asymptotics below are asserted for every fixed $$\theta\in(\varepsilon,1-\varepsilon)$$, with each $$A_\nu=A_\nu(\theta)$$ nondegenerate for every such $$\theta$$. Recursively subtract the earlier strata and let $$A_\nu$$ be the limiting covariance form at scale $$s_\nu$$, and put

$$
\mathcal W_\nu=\bigcap_{\mu<\nu}\ker A_\mu.
$$

For every fixed truncation of this ordered diagram expansion, the spectral projections of the covariance matrix converge to the associated graded spaces $$\mathcal W_\nu/\mathcal W_{\nu+1}$$, and every eigenvalue whose first nonzero term occurs within the truncation is asymptotic to $$s_\nu$$ times a positive eigenvalue of the induced form $$A_\nu$$. Vectors annihilating all retained forms pass canonically to the next connected diagram scales of Conjecture 26.

Consequently every asymptotic variance scale of a finite motif statistic is generated by a connected overlap or renormalized disjoint diagram from Conjecture 26, and no scale external to that diagrammatic expansion occurs. The filtration is invariant under replacing the motif family by one with isomorphic exact-overlap incidence algebra and identical local Euler weights.

*Significance.* The claim classifies all mechanisms by which a finite linear combination of prime motifs can become rigid. It predicts a canonical renormalization filtration, not merely one variance formula, and gives an algorithm for constructing observables that expose deeper arithmetic strata. A counterexample would identify a genuinely new source of rigidity outside overlap and disjoint correlation. The first theorem is a three-motif example in which one overlap form has a rational kernel and the next form is nondegenerate on it.

**Regularized mesoscopic local–spectral trace formula (Conjecture 28).** Fix motifs $$H_i,H_j$$, a Schwartz function $$\phi$$ with $$\phi(0)=0$$, an even cutoff $$\eta\in C_c^\infty(\mathbb R)$$ with $$\eta=1$$ near the origin, and an even mollifier $$\kappa\in C_c^\infty(\mathbb R)$$ of integral one. Let $$Q^{\mathrm{loc}}_{ij}(\phi;L)$$ be the exact-overlap-renormalized singular-series form

$$
\sum_{t\in\mathbb Z}
 \left[L\int_{\mathbb R}w(u)w(u+t/L)\,du\right]
 \phi(t/L)\,\mathfrak S^{\mathrm c}(H_i,H_j+t).
$$

Let $$\Lambda_{T,\eta}^{\sharp}$$ be the Weil explicit-formula distribution in the logarithmic variable, with each nontrivial zero of ordinate $$\gamma$$ multiplied by $$\eta(\gamma/T)$$ and with the pole, trivial-zero, archimedean, and prime-power terms kept as separately named summands. For $$\delta>0$$, put

$$
\Lambda_{T,\eta,\delta}^{\sharp}
   =\Lambda_{T,\eta}^{\sharp}*_{\log}\kappa_\delta,
 \qquad \kappa_\delta(u)=\delta^{-1}\kappa(u/\delta).
$$

This is a smooth function, so products of its shifted copies are unambiguous. Define

$$
Q^{\mathrm{spec}}_{ij}[\eta,\kappa]
 =Q^{\mathrm{spec}}_{ij}(\phi;X,L;T,\delta,\eta,\kappa)
$$

by inserting these mollified copies into the smoothed motif covariance, applying the same exact-overlap Möbius projection as on the local side, and subtracting the explicitly specified pole, diagonal, trivial-zero, archimedean, and prime-power counterterms before the mollifier is removed.

For every sufficiently large fixed $$A,B$$, take

$$
T=(X/L)(\log X)^A,
 \qquad
 \delta=(L/X)(\log X)^{-B}.
$$

Then

$$
Q^{\mathrm{spec}}_{ij}(\phi;X,L;T,\delta,\eta,\kappa)
 -Q^{\mathrm{loc}}_{ij}(\phi;L)
 =o\bigl(V_{ij}(X,L)\bigr)
$$

uniformly for $$X^\varepsilon\le L\le X^{1-\varepsilon}$$ and for $$\phi$$ in bounded Schwartz sets, where $$V_{ij}$$ is the first nonzero disjoint covariance scale. The same limit holds jointly for every fixed matrix of motifs and tests. Changing $$A,B,\eta$$, or $$\kappa$$ within the stated admissible class changes the renormalized spectral form by $$o(V_{ij})$$, so the limiting trace functional is canonical.

*Significance.* The spectral side is a finite smooth expression before any products are taken, and regularization independence is part of the conjecture rather than an implicit convention. The statement extends the Goldston–Montgomery and Chan prime/zero equivalence from one prime-counting field to products of shifted von Mangoldt functions [54, 33]. Failure can occur in two mathematically different ways: a missing mesoscopic covariance functional, or a genuine regularization anomaly. The first decisive theorem is the pair-motif covariance with one factor unshifted and two independent admissible mollifiers.

**Anchored arithmetic polymer expansion for prime motifs (Conjecture 29).** Fix an admissible motif $$H$$ of size $$k$$. A finite set $$A\subset\mathbb Z$$ of occurrence starts is a polymer when $$0\in A$$, the overlap graph on $$A$$ is connected, and $$U_A=\bigcup_{t\in A}(H+t)$$ is admissible. Define its *anchored codimension*

$$
d_H(A)=\vert U_A\vert -\vert H\vert ;
$$

this is the number of new prime constraints beyond the occurrence anchored at $$0$$. In the regularized spectral model of Conjecture 28, let $$Z$$ be the limiting low-mode vector (the joint limit, asserted as part of this conjecture, of the mode integrals of the Conjecture 28 functional against frequencies below a fixed cutoff $$K$$ on the $$L$$-scale, the Conjecture 28 limits taken first and $$K\to\infty$$ last), let $$\lambda(t\mid Z)$$ be the conditional one-point occurrence intensity, and set

$$
\lambda_H^0=\frac{\mathfrak S(H)}{(\log X)^k},
 \qquad
 \widetilde\lambda(t\mid Z)=\lambda(t\mid Z)/\lambda_H^0.
$$

For every fixed polymer $$A$$, uniformly for bounded diameter,

$$
\frac{(\log X)^{d_H(A)}\rho^{(\vert A\vert )}(A\mid Z)}
      {\lambda(0\mid Z)\prod_{t\in A\setminus\{0\}}
       \widetilde\lambda(t\mid Z)}
 \longrightarrow
 \frac{\mathfrak S(U_A)}{\mathfrak S(H)}
$$

in probability in the successive limits defining $$Z$$. Thus the conditional environment supplies only the one-point intensity, while every connected Palm activity is graded by $$(\log X)^{-d_H(A)}$$ and weighted by the complete-union singular series.

If admissible overlapping translates exist, put

$$
\delta(H)=\min_{\substack{t\ne0\\H\cup(H+t)\ \mathrm{admissible}}}
 \bigl(\vert H\cup(H+t)\vert -\vert H\vert \bigr),
 \qquad
 \mathcal T_H=\{t\ne0:\ H\cup(H+t)\ \mathrm{admissible},\ \vert H\cup(H+t)\vert -\vert H\vert =\delta(H)\}.
$$

Then the cluster-start fraction has the first nontrivial expansion

$$
\theta_X(H)=1-\frac{c_H}{(\log X)^{\delta(H)}}
   +o\bigl((\log X)^{-\delta(H)}\bigr),
 \qquad
 c_H=\sum_{\substack{t\in\mathcal T_H\\ t<0}}
 \frac{\mathfrak S(H\cup(H+t))}{\mathfrak S(H)}.
$$

The set $$\mathcal T_H$$ is symmetric under $$t\mapsto-t$$, and the cluster-start fraction counts, for each occurrence, only whether it has an overlapping predecessor, so the sum is restricted to $$t<0$$ and equals half the symmetric sum over $$\mathcal T_H$$. If no admissible overlap exists, $$\theta_X(H)=1+o((\log X)^{-M})$$ for every fixed $$M$$. Higher corrections are the connected Ursell sums of anchored polymers ordered by $$d_H(A)$$. These finite-$$X$$ Gibbs expansions are projectively consistent and subcritical, and after division by the low-zero intensity the cluster-start process is Poisson to each fixed order of this triangular expansion.

*Significance.* The relevant rarity is the number of new constraints after one occurrence is given, not the enhancement relative to a product of all one-point intensities. For two translates sharing $$s$$ of the $$k$$ prime positions, the Palm scale is $$(\log X)^{-(k-s)}$$. A universal $$1/\log X$$ correction therefore holds only for special motifs, such as pair motifs that admit an overlapping translate. The law keeps polymers of every size, supplies a canonical extremal-index exponent $$\delta(H)$$, and links Hardy–Littlewood constants, low-zero environments, Palm theory, and extreme motif gaps. For $$H=\{0,6\}$$ one has $$\delta(H)=1$$ and the pair-motif coefficient is recovered.

**Topological expansion of non-Gaussian prime cumulants (Conjecture 30).** For every connected exact-overlap diagram in Conjecture 26, expand its connected singular series over the linking primes and form the linkage graph of each term, whose vertices are the motif occurrences and whose edges join two occurrences sharing a linking prime in that term. Let $$g$$ be the first Betti number of the linkage graph. Once all larger coincidence strata have been subtracted, the total contribution of the terms of Betti number $$g$$ is smaller than that of the spanning-tree terms with the same external motifs by at least $$(\log L)^{-g}$$. The complete leading coefficient at each logarithmic order is the sum of the linked-term weights with the corresponding Betti number. In particular, the first nonzero odd cumulant of a balanced motif statistic, a combination $$Y_c$$ whose coefficient vector annihilates every coincidence-stratum form of Conjecture 27, is carried by incidence trees. For the single-prime field the fully spread connected part $$\kappa^{\mathrm{sp}}_{2m+1}$$, defined by subtracting every coincidence stratum as in Conjecture 27, obeys

$$
\kappa^{\mathrm{sp}}_{2m+1}=(c_m+o(1))L^m(\log L)^{m+1},
$$

where $$c_m$$ is the total connected tree weight. The raw cumulant adds the explicit coincidence diagrams of Conjecture 26, which carry powers of $$\log X$$ and are computable term by term, so the tree law is a statement about the spread diagrams, exactly the regime of Kuperberg’s singular-series sums.

*Significance.* This predicts a topological genus expansion for prime statistics: every independent cycle costs a logarithmic order. Kuperberg’s odd-moment conjecture is the one-field calibration, and the incidence-homology filtration with its motif-dependent coefficients is the new mechanism [34]. A failure would show that logarithmic suppression is controlled by an arithmetic invariant not visible in diagram topology.

### Programme II: arithmetic first-arrival fields and class groups

For a prime modulus $$q$$ and $$a\in\mathbb F_q^\times$$, let $$p(q,a)$$ be the least prime in the class $$a$$ and put

$$
T_q(a)=\frac{\operatorname{Li}(p(q,a))}{q-1},\qquad
 \mathcal N_{q,a}=\sum_{p\equiv a\, (q)}
 \delta_{\operatorname{Li}(p)/(q-1)}.
$$

The probability space chooses $$q$$ uniformly among primes in $$[Q,2Q]$$ and then chooses $$a$$ uniformly from $$\mathbb F_q^\times$$. Write $$e(x)=\mathrm e^{2\pi ix}$$.

**Connected first-arrival functional (Conjecture 31).** Let $$w^{\mathrm c}_{r,Q}$$ be the connected factorial-cumulant measure of the random point process $$\mathcal N_{q,a}$$. For every fixed $$r\ge2$$ there is a signed measure $$K_r$$, locally finite on the off-diagonal region $$\{u\in\mathbb R_+^r:u_i\ \text{distinct}\}$$, such that, on that region (the diagonal strata carry strictly smaller normalizations, as in the stratification of Conjecture 26, and are excluded here),

$$
(\log Q)^{r-1}w^{\mathrm c}_{r,Q}\Longrightarrow K_r
$$

vaguely, and $$K_1$$ denotes the limiting intensity measure, which in this clock is Lebesgue measure on $$\mathbb R_+$$. The measure $$K_r$$ is obtained by averaging, over the modulus aspect, the connected Hardy–Littlewood densities of $$r$$ primes constrained to one residue class. For every nonnegative compactly supported $$f$$ in a fixed uniform ball on which the Laplace functional is analytic,

$$
\log\mathbb E\exp(-\langle f,\mathcal N_{q,a}\rangle)
 =\sum_{r\ge1}\frac{(-1)^r}{r!}
 \int\prod_{j=1}^r(1-e^{-f(u_j)})\,dw^{\mathrm c}_{r,Q}(\mathbf u),
$$

and the asymptotic expansion obtained by inserting the limits $$K_r$$ is uniform to every fixed connected order. In particular the entire survival function, not merely its first correction, is determined by the hierarchy $$(K_r)_{r\ge2}$$.

*Significance.* This is an arithmetic point-process theory of least primes. The coupon-collector model of Li–Pratt–Shakan supplies the nearest extremal analogy, but not a connected Laplace functional [36]. Truth would determine waiting times, occupancy covariance, cover times, and terminal clustering from one hierarchy. The first theorem is the existence and explicit evaluation of $$K_2$$ on compact off-diagonal sets.

**Tested Gauss-polyspectral reciprocity for the least-prime field (Conjecture 32).** Set $$T_q(0)=\operatorname{Li}(q)/(q-1)$$ and centre the resulting field $$f_q$$ on all of $$\mathbb F_q$$. Let $$\mathbf A_q$$ and $$\mathbf M_q$$ be its complete additive and multiplicative Fourier coefficient vectors, including the explicit rank-one coordinate needed to record the value at $$0$$. There is then an explicit invertible Gauss matrix $$U_q$$ with

$$
\mathbf M_q=U_q\mathbf A_q.
$$

Choose $$q$$ uniformly among primes in $$[Q,2Q]$$. For every finite family of degrees $$r_1,\ldots,r_m$$ and uniformly bounded fibrewise test tensors $$\Phi_{j,q}$$, define the scalar additive observables

$$
X_{j,Q}(q)=\langle\Phi_{j,q},\mathbf A_q^{\otimes r_j}\rangle
$$

and the transported multiplicative observables

$$
Y_{j,Q}(q)=
 \left\langle (U_q^{-1})^{*\otimes r_j}\Phi_{j,q},
               \mathbf M_q^{\otimes r_j}\right\rangle.
$$

For every modulus, $$X_{j,Q}(q)=Y_{j,Q}(q)$$, so all joint cumulants under the random-modulus law satisfy the exact finite identity

$$
\operatorname{Cum}_Q(X_{1,Q},\ldots,X_{m,Q})
 =\operatorname{Cum}_Q(Y_{1,Q},\ldots,Y_{m,Q}).
$$

This is the probability-space-correct form of Gauss transport. It makes no reference to a cumulant of a deterministic coefficient vector.

The conjectural content is that, after normalization by the first nonzero connected scale, tests supported on additive zero-sum tensors converge to contractions of the Fourier transforms of the arrival kernels $$K_r$$ from Conjecture 31. Transporting those tests fibrewise by the exact Gauss matrices and only then taking the modulus average gives the same limits as the corresponding multiple explicit-formula correlations of Dirichlet $$L$$-function zeros. The two descriptions determine the same continuous multilinear functional on the completion of the tested tensor class.

*Significance.* The elementary input is the finite Gauss matrix. The new claim is a complete higher-order tomography principle for the random-modulus least-prime field. Every scalar statistic is compared on a genuine probability space, while the varying finite fields are handled fibrewise before averaging. Failure would isolate a tensor class on which local same-class prime correlations and character-zero correlations disagree even though the underlying finite transforms are exact. The first theorem is the quadratic identity for tests localized to one additive lag and its transported character kernel.

**Rubinstein–Sarnak terminal chaos dichotomy (Conjecture 33).** Assume GRH and a $$q$$-aspect linear-independence/random-phase hypothesis for the low zeros of primitive Dirichlet $$L$$-functions. Let $$x_q$$ satisfy $$\operatorname{Li}(x_q)/(q-1)=\log(q-1)$$ and let $$G_{q,A}(a)$$ be the centred, variance-normalized low-zero field obtained from characters $$\chi\ne\chi_0$$ and zeros $$\vert \gamma\vert \le(\log q)^A$$, with the standard compensator $$-\tfrac12\operatorname{Var} G_{q,A}(a)$$. Define the random empirical chaos measure

$$
\mathcal M_{q,A}(dg)=\frac1{q-1}\sum_{a\in\mathbb F_q^\times}
  \exp\!\left(G_{q,A}(a)-\tfrac12\operatorname{Var} G_{q,A}(a)\right)
  \delta_{G_{q,A}(a)}(dg).
$$

Let $$b_Q$$ be the smallest level with $$\mathbb E_q\#\{a:T_q(a)>b_Q\}\le1$$. In the successive limits $$Q\to\infty$$ and then $$A\to\infty$$, the pair consisting of $$\mathcal M_{q,A}$$ and

$$
\sum_a\delta_{(G_{q,A}(a),\,T_q(a)-b_Q)}
$$

converges jointly. Conditionally on the limiting chaos measure $$\mathcal M$$, the terminal cluster-start process is Poisson with directing measure

$$
e^{-x}\,\mathcal M(dg)\,dx.
$$

At finite modulus the cluster-start thinning enters through the terminal extremal index $$\theta_{\mathrm{occ}}(q)$$, the analogue for the last classes of the cluster-start fraction $$\theta_X(H)$$ of Conjecture 29, together with the terminal connected-polymer decorations of Conjecture 31. Both corrections enter at the first nonzero connected scale and vanish in the successive limit, so $$\theta_{\mathrm{occ}}(q)\to1$$ and the limiting directing measure carries no cluster factor.

The nature of the directing measure is governed by the covariance-energy statistic

$$
\mathfrak E_{q,A}=\frac1{(q-1)^2}
 \sum_{a,b\in\mathbb F_q^\times}
 \operatorname{Cov}(G_{q,A}(a),G_{q,A}(b))^2.
$$

If $$\mathfrak E_{q,A}\to0$$ along the successive limit, $$\mathcal M$$ self-averages to the deterministic exponentially tilted Gaussian law and the terminal process is an ordinary decorated Poisson process. If $$\liminf\mathfrak E_{q,A}>0$$ and the Gaussian-chaos second moments are uniformly integrable, $$\mathcal M$$ is nondegenerate and the limit is a genuine Cox process. No nondegeneracy is asserted without this criterion.

*Significance.* Rubinstein–Sarnak theory supplies the fixed-modulus prime-race environment [6]. The new object is its terminal first-arrival chaos measure in the modulus aspect. The statement now treats self-averaging as a serious competing model rather than assuming a Cox limit by terminology. It predicts the complete last class process, its prime-race marks, and an explicit spectral criterion separating a deterministic environment from persistent random mixing.

**Nonlinear spectral response calculus for arithmetic first arrivals (Conjecture 34).** Let a sequence of modulus ensembles have a small explicit-formula perturbation of the arrival intensity

$$
V_Q(a,t)=\sum_{\chi\in\mathcal C_Q}v_{Q,\chi}(t)\chi(a),
 \qquad \|V_Q\|_{T}\to0,
$$

where $$\mathcal C_Q$$ has uniformly bounded cardinality and, on every fixed interval $$[0,T]$$, the canonical norm is $$\|V\|_T=\sup_{a,0\le t\le T}\vert V(a,t)\vert $$. Assume that the connected hierarchy of Conjecture 31 satisfies an exponential cluster bound there, so its Laplace functional is analytic in a fixed $$\|\cdot\|_T$$-ball. If $$S_Q(a,t)$$ and $$S_Q^{(0)}(t)$$ are the perturbed and ordinary survival functions, then for every fixed $$R$$

$$
\log\frac{S_Q(a,t)}{S_Q^{(0)}(t)}
 =\sum_{m=1}^{R}\mathcal R_m[V_Q^{\otimes m}](a,t)
   +o(\|V_Q\|_{T}^{R})
$$

uniformly on compact $$t$$-ranges. The causal Volterra operator $$\mathcal R_m$$ is the universal linked-cluster contraction of the full hierarchy $$(K_r)_{r\ge1}$$ with $$m$$ marked perturbation insertions, and truncating the connected hierarchy at order $$J$$ gives a convergent approximation as $$J\to\infty$$.

If the input character support is $$\mathcal C_Q$$, the $$m$$th response is supported exactly on products of at most $$m$$ input characters (subject only to coincidences and the trivial character). In particular the linear response preserves character rank, while the first new harmonics occur at quadratic order with coefficients determined by connected three-point arrival correlations.

*Significance.* This is a nonlinear transfer calculus from zeros to first-hit statistics. A Siegel zero, a cluster of low zeros, and an ordinary prime-race bias become different inputs to the same response operators. The exceptional-zero rank-one statement is a special case, while the second-order harmonics provide a direct falsification test. The first theorem is the Fréchet derivative $$\mathcal R_1$$ from the two-point occupancy kernel.

**Local-information capacity of odd class groups (Conjecture 35).** Fix an odd prime $$\ell$$. Sample negative fundamental discriminants $$D\in[-2Y,-Y]$$, conditioned on a fixed coarse two-primary invariant. For a set of odd primes $$S_Y$$, put $$M_Y=\prod_{p\in S_Y}p$$, let $$\Sigma_Y(D)=((D/p))_{p\in S_Y}$$ be the attainable sign vector, and let $$H_Y$$ be the logarithm of the number of attainable cells. Let $$\delta_Y(\sigma)$$ be the exact CRT density of the sign cell after imposing quadratic reciprocity and the fixed two-primary data, and let $$\mathcal D_Y$$ be the ambient discriminant family. Write

$$
\Delta_Y(S_Y)=\sup_\sigma
 \left\vert \frac{\#\{D\in\mathcal D_Y:\Sigma_Y(D)=\sigma\}}
 {\vert \mathcal D_Y\vert \,\delta_Y(\sigma)}-1\right\vert 
$$

over attainable cells with $$\vert \mathcal D_Y\vert \delta_Y(\sigma)\ge\log Y$$.

There is a sequence $$\varepsilon_Y\to0$$, independent of $$S_Y$$ in the subcritical range, such that uniformly over those cells

$$
d_{\mathrm{TV}}\!\left(
 \mathcal L(\mathrm{Cl}(D)[\ell^\infty]\mid\Sigma_Y=\sigma,\text{2-data}),
 \mathcal L_{\mathrm{CL},\ell}\right)
 \le \varepsilon_Y+O(\Delta_Y(S_Y)),
$$

and the analogous bound holds for every fixed Cohen–Lenstra moment. In particular, for every $$\varepsilon>0$$, the conclusion is uniform whenever

$$
H_Y\le(1-\varepsilon)\log Y,
 \qquad \log M_Y\le(\tfrac12-\varepsilon)\log Y,
 \qquad \Delta_Y(S_Y)=o(1).
$$

Since every odd prime contributes at most $$\log3\le\log p$$ of cell entropy, $$H_Y\le\log M_Y$$ throughout, so the conductor constraint is the binding one in the displayed range, while the entropy governs the impossibility clause below. At $$H_Y\ge(1+\varepsilon)\log Y$$ no uniform statement is possible. Up to the conductor scale at which $$\Delta_Y$$ becomes macroscopic, every first-order failure of local independence factors through this discriminant-cell discrepancy, and there is no earlier odd-class-group obstruction.

*Significance.* Wood’s framework treats fixed local conditions [37]. The new statement proposes the full information capacity of an odd class group under a growing local sigma-algebra, with the entropy governing impossibility and the conductor governing equidistribution. It would transfer directly to Selmer groups, ray class groups, and unramified extension statistics. The first theorem is uniformity for $$\vert S_Y\vert \to\infty$$ with $$M_Y=Y^{o(1)}$$.

### Programme III: finite logarithms, regulators, and algebraic tori

For $$p\nmid a$$, write

$$
q_p(a)=\frac{a^{p-1}-1}{p}\pmod p.
$$

For a generating tuple $$g=(g_1,\ldots,g_s)$$, let $$R(g)$$ be its multiplicative relation lattice and let $$\mathbb T_g\subset(\mathbb R/\mathbb Z)^s$$ be the identity component of its annihilator. Its dimension is the saturated multiplicative rank.

**Kummer–Haar law on relation tori (Conjecture 36).** Let $$\Gamma\le\mathbb Q^\times$$ be finitely generated and torsion-free, saturated modulo torsion (if $$x^n\in\Gamma\cdot\{\pm1\}$$ for some $$n\ge1$$ then $$x\in\Gamma\cdot\{\pm1\}$$), and let $$g$$ be any ordered generating tuple. As $$p$$ varies in every fixed compatible cyclotomic–Kummer Chebotarev class, the vectors

$$
\frac{(q_p(g_1),\ldots,q_p(g_s))}{p}\in(\mathbb R/\mathbb Z)^s
$$

equidistribute with Haar measure on $$\mathbb T_g$$. More strongly, for every finite collection of compatible Chebotarev restrictions, the conditional empirical measures converge to the Haar disintegration on the corresponding components, and the support is contained in no proper closed coset of $$\mathbb T_g$$. The law is invariant under changing generators and depends on $$\Gamma$$ only through its saturation and the fixed Kummer conditioning data.

*Significance.* Katz formulated horizontal Wieferich equidistribution principles for algebraic groups, and Shparlinski proved estimates in different horizontal and averaged regimes [38, 39]. The new content here is the exact saturated relation torus, full generator invariance, and disintegration under fixed Kummer classes. It turns multiplicative rank into a geometric support theorem rather than a heuristic count of coordinates.

**Rank-dimensional large sieve for finite logarithms (Conjecture 37).** Choose a Smith-normal-form basis of the character lattice $$X^*(\mathbb T_g)=\mathbb Z^s/R(g)^{\mathrm{sat}}$$. There is a constant $$\delta_\Gamma>0$$ such that, for every $$\varepsilon>0$$, every $$M\le X^{\delta_\Gamma}$$, and all complex weights $$a_p$$ supported on $$X<p\le2X$$,

$$
\sum_{\substack{m\in X^*(\mathbb T_g)\\\|m\|_\infty\le M}}
 \left\vert \sum_{X<p\le2X}a_p
 e\!\left(\frac{\langle m,q_p(g)\rangle}{p}\right)\right\vert ^2
 \ll_{\Gamma,\varepsilon}(M^{\operatorname{rank}\Gamma}+\pi(X))X^\varepsilon\sum_p\vert a_p\vert ^2.
$$

The same inequality holds after every fixed compatible cyclotomic–Kummer restriction, and for matrix-valued weights with the Hilbert–Schmidt norm. The exponent $$\delta_\Gamma$$ is invariant under changing the generating tuple.

*Significance.* This is the quantitative mechanism behind Conjecture 36. It predicts that saturated rank is not only the support dimension but the exact dual dimension in a prime-varying large sieve. A proof for any positive power range would control genuine shrinking targets and would be far beyond currently available fixed-frequency tests. Failure would reveal an unrecognized spacing or energy obstruction among finite-logarithm vectors.

**Mesoscopic-to-lattice shrinking-target transition (Conjecture 38).** Let $$\Gamma\le\mathbb Q^\times$$ be torsion-free of rank $$r$$ and saturated modulo torsion, and choose a basis of $$\Gamma$$, identifying its relation torus with $$(\mathbb R/\mathbb Z)^r$$. For integers $$w_p$$ with $$1\le w_p=o(p)$$, let $$E_p(w)$$ be the event that every coordinate of the Fermat-quotient vector has a representative of absolute value at most $$w_p$$.

*Mesoscopic universality.* If $$w_p\to\infty$$, then in every range in which the Haar mass

$$
\lambda(X)=\sum_{p\le X}\left(\frac{2w_p+1}{p}\right)^r
$$

tends to infinity, the count of $$E_p(w)$$ is asymptotic to $$\lambda(X)$$. On prime blocks with bounded Haar mass, the randomly translated event process converges to a Poisson process with that mass.

*Lattice transition.* For every fixed finite target set $$B\subset\mathbb Z^r$$, there is an arithmetic regulator intensity $$\kappa_{\Gamma,B}\ge0$$ such that

$$
\#\{p\le X:q_p\vert _\Gamma\in B\}
 =(\kappa_{\Gamma,B}+o(1))\sum_{p\le X}p^{-r}
$$

whenever the sum diverges, while only finitely many such primes occur when $$r\ge2$$. As a separately falsifiable genericity clause, for Kummer-generic $$\Gamma$$ and $$B=\{0\}$$ one has $$\kappa_{\Gamma,B}=1$$. The transition from Haar universality to the arithmetic intensity occurs only when $$w_p$$ remains bounded.

*Significance.* This separates two universality classes that a single undifferentiated model conflates. Growing targets are controlled by Haar geometry, while exact Wieferich targets can carry a genuinely arithmetic regulator intensity. Gras’s much rarer fixed-base model and the Haar model therefore disagree precisely at the lattice boundary [40, 41]. The first theorem is mesoscopic universality for $$w_p=p^\eta$$ with one rank-one base.

For a $$p$$-adic unit $$a$$, write $$\langle a\rangle_p$$ for the Teichmüller lift of its residue, and for a prime $$\mathfrak p\mid p$$ of a number field write $$\tau_{\mathfrak p}$$ for the Teichmüller lift in the completion at $$\mathfrak p$$. Define $$q_{p,k}(a)=p^{-1}\log(a\langle a\rangle_p^{-1})\pmod{p^k}$$. The matrix entries below are the $$\mathfrak p$$-adic analogues of $$q_{p,k}$$; on $$\mathbb Q$$ with $$k=1$$ one has $$q_{p,1}(a)\equiv-q_p(a)\pmod p$$, the Fermat quotient up to sign.

**Global-lattice horizontal $$p$$-adic regulator-matrix law (Conjecture 39).** Let $$K/\mathbb Q$$ be a fixed Galois number field with group $$G$$, and let $$\Gamma\le\mathcal O_K^\times$$ be torsion-free and saturated modulo $$\mu(K)$$, with ordered basis $$\epsilon_1,\ldots,\epsilon_s$$. Define the fixed global relation lattice

$$
\mathcal R_\Gamma=
 \left\{(c_{\sigma j})\in\mathbb Z^{G\times s}:
   \prod_{\sigma\in G}\prod_{j=1}^s
   \sigma(\epsilon_j)^{c_{\sigma j}}\in\mu(K)\right\}.
$$

Let $$\mathbb T_\Gamma\subset(\mathbb R/\mathbb Z)^{G\times s}$$ be its annihilator. This lattice contains the norm and Galois relations and is independent of the chosen basis up to the natural integral change of coordinates.

For a rational prime $$p$$ splitting completely in $$K$$, label the primes above $$p$$ by $$G$$, use the Teichmüller lift in each completion, and form the depth-$$k$$ matrix

$$
L_{p,k}(\Gamma)=
 \left(p^{-1}\log_{\mathfrak p}
   (\epsilon_j\tau_{\mathfrak p}(\bar\epsilon_j)^{-1})
   \bmod p^k\right)_{\mathfrak p\mid p,\,1\le j\le s}.
$$

It lies in the annihilator of $$\mathcal R_\Gamma\otimes\mathbb Z/p^k\mathbb Z$$. As $$p$$ varies through any fixed compatible Frobenius class, $$L_{p,1}/p$$ equidistributes with Haar measure on $$\mathbb T_\Gamma$$, and the depth-$$k$$ matrices are Haar in the projective system of its reductions modulo $$p^k$$.

Let $$\mathcal D$$ be a basis-invariant determinantal or Smith stratum in this projective module, and let $$\mu_{p,k}(\mathcal D)$$ be its exact local Haar mass. The primes for which $$L_{p,k}\in\mathcal D$$ have counting law governed by $$\sum_{p\le X}\mu_{p,k}(\mathcal D)$$. For a determinantal or Smith stratum of codimension $$c$$, whose point counts are polynomial in $$p$$, $$\mu_{p,1}(\mathcal D)=p^{-c}+O(p^{-c-1})$$, and codimension one has a Poisson point process in $$\log\log p$$ after uniform random translation, while codimension at least two has a summable large-prime tail together with the exact small-prime atoms.

*Significance.* The horizontal state space is one fixed global torus rather than a relation module that changes with $$p$$. The conjecture turns mod-$$p$$ Leopoldt defects into a Galois-equivariant random-matrix problem, with exact Smith strata retaining higher depth. Existing mod-$$p$$ Leopoldt and random-matrix theories provide neighbouring languages [41, 42, 43]. Recent number-field Wieferich results strengthen the arithmetic motivation without supplying this horizontal matrix law [57, 58]. The first theorem is the rank-one split-prime law for a real quadratic field.

**Functorial horizontal finite logarithms on algebraic tori (Conjecture 40).** Let $$T/\mathbb Q$$ be an algebraic torus, let $$\mathcal T$$ be its smooth integral model away from a finite set, and let $$\Gamma\le T(\mathbb Q)$$ be finitely generated. Let $$S$$ be the identity component of the Zariski closure of $$\Gamma$$. At a good unramified prime $$p$$, let $$\tau_p(\bar P)$$ be the canonical prime-to-$$p$$ torsion lift of the reduction of $$P\in\Gamma$$ and define

$$
\ell_p(P)=p^{-1}\log_T\bigl(P\tau_p(\bar P)^{-1}\bigr)\pmod p
 \in\operatorname{Lie}(S)(\mathbb F_p).
$$

For any generators $$P_1,\ldots,P_s$$ of $$\Gamma$$, the normalized matrix $$(\ell_p(P_i)/p)_i$$ equidistributes, in every compatible Frobenius class, with Haar measure on the real relation subtorus cut out jointly by the algebraic subgroup $$S$$ and the integral relations among the $$P_i$$. For every morphism of tori $$\phi:T\to T'$$,

$$
\ell_p(\phi(P))=d\phi(\ell_p(P)),
$$

and the horizontal Haar measures push forward under the induced map. Isogenies preserve the shrinking-target intensities after the explicit finite kernel correction.

*Significance.* Katz already proposed Wieferich equidistribution beyond $$\mathbb G_m$$ [38]. The additional content is a matrix-valued law for a finitely generated global subgroup, relation-subtorus support, fixed-Frobenius disintegration, and exact functoriality under morphisms and isogenies. It turns horizontal finite logarithms into a functor on the category of tori with arithmetic subgroups.

### Programme IV: arboreal arithmetic dynamics

For a degree-$$d$$ map $$f$$ and basepoint $$a$$, write $$K_n=\mathbb Q(f^{-n}(a))$$, $$G_n=\operatorname{Gal}(K_n/\mathbb Q)$$, and let $$\mu_n(C)=\vert C\vert /\vert G_n\vert $$ on conjugacy classes. For primes $$p\le X$$ unramified in $$K_n$$, let $$\widehat\mu_{n,X}$$ be the empirical Frobenius measure.

**Entropy–conductor profile of arboreal resolution (Conjecture 41).** For a degree-$$d$$ map $$f$$ and level $$n$$, let $$G_{n,f}$$ be the arboreal quotient and $$\mu_{n,f}$$ its Haar measure on conjugacy classes. For $$N$$ independent samples from $$\mu_{n,f}$$ define the exact sampling obstruction

$$
\mathcal S_{n,f}(N)=
 \mathbb E\,d_{\mathrm{TV}}\!\left(N^{-1}\sum_{j=1}^N\delta_{Z_j},\mu_{n,f}\right).
$$

For each nontrivial irreducible Artin representation $$\rho$$ of $$G_{n,f}$$, let $$q(\rho)$$ be its Artin conductor and define the GRH conductor energy

$$
\mathcal A_{n,f}(X)=
 \frac{\log X}{\sqrt X}
 \left(\sum_{\rho\ne1}(\dim\rho)^2
  \bigl(\log q(\rho)+\dim(\rho)\log X\bigr)^2\right)^{1/2}.
$$

This is a canonical character-theoretic replacement for a single discriminant proxy. For a parameter family $$\mathcal F(B)$$ put

$$
n^*_{\mathcal F}(B,X;\eta)=
 \max\left\{n:\mathbb E_{f\in\mathcal F(B)}
   \bigl[\mathcal S_{n,f}(\pi(X))+\mathcal A_{n,f}(X)\bigr]\le\eta\right\}.
$$

Assume the generic arboreal image is open, exceptional parameters have density zero, Artin holomorphy and GRH hold at the levels considered, and the family is in the large-sieve range of Conjecture 42. Then the actual empirical resolution depth, defined by the same total-variation threshold with prime Frobenius samples, differs from $$n^*_{\mathcal F}(B,X;\eta)$$ by $$O_{\mathcal F,\eta}(1)$$.

More precisely, suppose, uniformly for a density-one set of parameters, that the class measures have a limiting complete Rényi profile

$$
\psi_{\mathcal F}(\alpha)=
 \lim_{n\to\infty}d^{-n}\log\sum_C\mu_{n,f}(C)^\alpha
$$

uniformly for $$\alpha$$ in a fixed interval containing $$[1/2,2]$$, and the corresponding Artin-conductor energies have finite positive exponential profiles on the same $$d^n$$ scale. Then

$$
n^*_{\mathcal F}(B,X;\eta)=\log_d\log X+O_{\mathcal F,\eta}(1).
$$

Two families of the same degree with boundedly different complete Rényi and conductor profiles have resolution depths differing by $$O(1)$$, and in particular a fixed-index open subgroup changes only the bounded shift.

*Significance.* The observable depth is defined through the exact nonuniform sampling law and a representation-by-representation conductor energy. The $$\log_d\log X$$ scale follows from explicit Rényi and conductor profiles on the natural $$d^n$$ complexity scale. Large arboreal images and effective Chebotarev are inputs [44, 45, 46]. Recent work on fixed-point profiles shows why the full class-measure tail, rather than group order alone, matters [59]. The first theorem is bounded-shift stability for one explicit index-two subgroup of the binary wreath tower.

**Arboreal family large sieve and cumulant independence (Conjecture 42).** Let $$\mathcal F\to\mathbb A^1$$ be a generically finite-index arboreal family. For each level $$n$$ and irreducible representation $$\rho$$ of the generic quotient $$G_n$$, let $$\mathcal V_{n,\rho}$$ be the associated middle-extension sheaf on the good parameter locus. Define the geometric conductor budgets

$$
\mathfrak C_{n,r}=
 \sum_{\rho_1,\ldots,\rho_r}
 \left(\prod_{j=1}^r\dim\rho_j\right)^2
 \operatorname{cond}\!\left(\boxtimes_{j=1}^r\mathcal V_{n,\rho_j}\right)^2,
 \qquad \mathfrak C_n=\mathfrak C_{n,1},
$$

where the external tensor product is taken on the CRT parameter space for distinct primes, and the conductor includes rank, singularities, tame drop, and Swan terms.

*Square-root tier.* For every $$\varepsilon>0$$ and all complex coefficients $$\alpha_{p,\rho}$$,

$$
\sum_{\vert c\vert \le B}
 \left\vert \sum_{p\le X}\sum_{\rho\ne1}
  \alpha_{p,\rho}\operatorname{tr}
  \rho(\operatorname{Frob}_{p,c})\right\vert ^2
 \ll_{\varepsilon,\mathcal F}
 \bigl(B+X^2\mathfrak C_n^{1+\varepsilon}\bigr)
 \sum_{p,\rho}\vert \alpha_{p,\rho}\vert ^2,
$$

uniformly when $$X^2\mathfrak C_n^{1+\varepsilon}\le B^{1-\varepsilon}$$, after deleting the singular fibres.

*Connected tier.* For every fixed $$r\ge3$$, centred trace functions at distinct primes have family-averaged connected cumulants with square-root cancellation in the parameter-family count, uniformly in the range $$X^r\mathfrak C_{n,r}^{1+\varepsilon}\le B^{1-\varepsilon}$$, and equivalently, after normalization, every fixed connected Frobenius cumulant tends to zero. An exponential connected-moment bound makes this convergence uniform in $$r$$ over the range needed for occupancy functionals.

Consequently, whenever the analytic Chebotarev error is $$o(1)$$ but the iid sampling functional of $$\mu_n$$ is nonvanishing, the complete conjugacy-cylinder count vector, averaged over parameters, has the nonuniform multinomial occupancy law of independent samples from $$\mu_n$$, including its missing-mass, collision, and total-variation profile. The multinomial conclusion is derived from the connected tier, not from the $$L^2$$ bound alone.

*Significance.* This separates the two analytic inputs that a single-tier statement compresses into one claim. The square-root tier is a growing-monodromy large sieve in the spirit of Kowalski [47]. The connected tier is the genuinely stronger cross-prime independence principle required for an occupancy limit. The conductor budget is attached to the actual sheaves and their tensor products rather than to an undefined scalar conductor of a cover. A failure identifies either geometric complexity missed by the sheaf conductors or arithmetic entanglement surviving all fixed-order trace tests.

**Coloured dynatomic Galois-factor process (Conjecture 43).** For $$f_c(x)=x^d+c$$, let the critical exact-period polynomial factor as $$\Psi_n(c)=\prod_{j=1}^{s_n}F_{n,j}(c)$$ over $$\mathbb Z$$. Sample $$c$$ from a dyadic height interval away from postcritically finite, discriminant, and fixed-resultant loci.

For every fixed $$n$$, condition on any fixed finite local valuation state and normalize the prime factors of each $$F_{n,j}(c)$$ by that component’s residual logarithmic mass. The component-coloured factor processes converge jointly to independent Frobenius-marked Poisson–Dirichlet $$\operatorname{PD}(1)$$ processes, with the mark in colour $$j$$ given by the fixed-point-size-biased conjugacy law in the splitting field of $$F_{n,j}$$. The total logarithmic mass of ramified factors tends to zero.

Uniformly for $$n=n(H)$$ with $$\deg\Psi_n=o(\log H)$$, every fixed correlation functional whose support lies inside the available level of distribution converges to the corresponding restricted-support correlation of these coloured marked processes. No full-process claim is made at growing degree without level-one distribution.

*Significance.* Exact-period components are genuine geometric colours, and their Galois marks distinguish dynamical families with similar unmarked factor sizes. The statement deliberately separates the full fixed-degree process from the restricted-support growing-degree law, in accordance with the distribution thresholds in Bharadwaj–Rodgers [51]. The first theorem is a two-colour correlation law at one fixed period.

**Complexity-uniform primitive valuation process for dynatomic values (Conjecture 44).** For the critical exact-period polynomial $$\Psi_n(c)$$, remove its canonical greatest common divisor in $$\mathbb Q[c]$$ with the earlier critical-orbit product and denote the result by $$\Psi_n^{\mathrm{new}}$$. Define the logarithmic arithmetic complexity

$$
\mathfrak H_n=
 \deg\Psi_n^{\mathrm{new}}
 +\log^+H_{\mathrm{coeff}}(\Psi_n^{\mathrm{new}})
 +\log^+\vert \operatorname{Disc}(\Psi_n^{\mathrm{new}})\vert 
 +\sum_{m<n}\log^+\vert \operatorname{Res}(\Psi_n^{\mathrm{new}},f_c^m(0))\vert ,
$$

where zero resultants have already been removed by the canonical gcd. For each prime $$p$$, let $$\nu_{n,p}$$ be the exact Haar law on $$\mathbb Z_p$$ of the primitive valuation

$$
V_{n,p}(c)=v_p(\Psi_n^{\mathrm{new}}(c))
 \mathbf 1_{p\nmid f_c^m(0)\ \forall m<n}.
$$

All discriminant, resultant, and collision primes remain inside these local laws.

For every control function $$\omega(H)=o(\log H)$$, uniformly over levels with $$\mathfrak H_n\le\omega(H)$$, the finite-prime valuation vectors for $$c$$ in a dyadic height interval converge to the corresponding marginals of $$\bigotimes_p\nu_{n,p}$$. In addition, for every $$\eta>0$$,

$$
\lim_{z\to\infty}\limsup_{H\to\infty}
 \sup_{n:\,\mathfrak H_n\le\omega(H)}
 \mathbb P\!\left(
   \sum_{p>z}(\log p)(V_{n,p}-1)_+>
   \eta\log\vert \Psi_n^{\mathrm{new}}(c)\vert 
 \right)=0,
$$

and the analogous unnormalized tail $$\sum_{p>z}\mathbb P(V_{n,p}\ge2)$$ tends to zero whenever the local squarefree product is positive. These two clauses give convergence in the topology generated by bounded cylinder functions and the logarithmic squarefull-mass functional.

Consequently

$$
\mathbb P\bigl(\Psi_n^{\mathrm{new}}(c)\ \text{is squarefree}\bigr)
  =\prod_p\tilde\nu_{n,p}(\{0,1\})+o(1)
$$

uniformly in the stated complexity range, where $$\tilde\nu_{n,p}=\nu_{n,p}$$ except at the finitely many collision primes dividing one of the resultants $$\operatorname{Res}(\Psi_n^{\mathrm{new}},f_c^m(0))$$, at which $$\tilde\nu_{n,p}$$ is the law of the raw valuation $$v_p(\Psi_n^{\mathrm{new}}(c))$$, and the logarithmic squarefull mass converges to the law determined by the complete local product.

*Significance.* Degree alone does not control a growing polynomial family. The controlling range includes coefficient height, discriminant, and resultants, while the infinite-product conclusion is supported by an explicit uniform squarefull-tail assertion. The local process still retains every bad-prime and collision state and remains level dependent, as primitive hits at a fixed prime occur by bounded time modulo $$p^k$$. The nearest literature treats primitive divisors and fixed-polynomial squarefree values, not this complexity-uniform adelic process [49, 48].

**Divisor-sensitive classification of dynamical gcd height (Conjecture 45).** Let $$F=(f,g)$$ be a split map on $$(\mathbb P^1)^2$$, with $$f,g$$ disintegrated (in the sense of Medvedev and Scanlon [56], so neither is linearly conjugate to a power map, a Chebyshev map, or a close relative of these) of the same degree, and let $$P=(a,b)$$ have positive canonical heights. Let $$D_1,D_2$$ be the two coordinate-zero divisors and let $$E$$ be the exceptional divisor of the blow-up at $$D_1\cap D_2$$. Then

$$
\limsup_{n\to\infty}
 \frac{h_E(F^n(P))}{\max\{h(f^n(a)),h(g^n(b))\}}>0
$$

if and only if there exist $$m\ge0$$ and an irreducible $$F$$-periodic curve $$Z$$ containing $$F^m(P)$$, with $$Z$$ not contained in $$D_1\cup D_2$$ (automatic when both coordinates have positive canonical height), such that, on the normalization of $$Z$$, the pullbacks of $$D_1$$ and $$D_2$$ have a common nonzero effective component. In the absence of such eventual entry into a divisor-compatible periodic curve, the normalized gcd height tends to zero.

The converse is unconditional in every setting where the required Vojta inequality for the blow-up is known, and otherwise is explicitly conditional on that inequality. The same criterion extends to split maps on $$(\mathbb P^1)^r$$ by replacing a common component with positive codimension-one intersection multiplicity among the pulled-back divisors.

*Significance.* The obstruction is not merely a common dynamical quotient. It is a periodic geometric relation carrying the actual divisors measured by the gcd height. Eventual entry is the right notion, since a preperiodic tail can carry the divisor relation before periodicity begins. Recent work resolves several set-theoretic dynamical-GCD problems, while this height-theoretic divisor classification is the additional boundary [50]. Failure would point to a new source of macroscopic Diophantine proximity outside invariant geometry.

### Programme V: adelic factorization and sieve flow

Throughout this programme $$P^+(m)$$ and $$P^-(m)$$ denote the largest and smallest prime factors of $$m$$, the constant $$\gamma$$ is Euler’s, $$\rho_f(p)$$ counts the roots of $$f$$ modulo $$p$$, and every sample $$n\in[N,2N]$$ is drawn uniformly.

**Frobenius-marked Poisson–Dirichlet process (Conjecture 46).** Let $$f\in\mathbb Z[x]$$ be irreducible with splitting field $$L$$ and transitive Galois group $$G$$. Sample $$n\in[N,2N]$$. Mark each unramified prime factor $$p$$ of $$f(n)$$ by its conjugacy class $$C\subset G$$ and give it mass $$u=\log p/\log\vert f(n)\vert $$. The macroscopic marked process converges to a marked $$\operatorname{PD}(1)$$ process with conditional mark law

$$
\mathbb P(C\mid u)=\frac{\vert C\vert }{\vert G\vert }\operatorname{fix}(C),\qquad\text{$\operatorname{fix}(C)$ the number of fixed roots of an element of $C$,}
$$

independent of $$u$$. Given the masses and every fixed finite local valuation state, the marks of finitely many macroscopic factors are asymptotically independent. Under a normal quotient equipped with the induced permutation representation, the marked process pushes forward functorially.

*Significance.* Chebotarev contributes $$\vert C\vert /\vert G\vert $$, divisibility by a polynomial value size-biases by the number of fixed roots, and Burnside’s lemma normalizes the result. Bharadwaj–Rodgers supply the unmarked factor-process framework [51]. Simultaneous Galois marking, conditional independence, and functorial pushforward are the new content. It connects Galois theory to probabilistic factorization directly.

**Three-scale factorization of polynomial values (Conjecture 47).** Let $$f\in\mathbb Z[x]$$ be irreducible, sample $$n\in[N,2N]$$, choose $$y=y(N)\to\infty$$ with $$\log y=o(\log N)$$, and write $$R_y=f(n)/S_y(f(n))$$, where $$S_y(m)=\prod_{p\le y}p^{v_p(m)}$$ is the $$y$$-smooth part. Jointly with the complete small-prime valuation field $$(v_p(f(n)))_{p\le y}$$, the residual logarithmic factor process

$$
\sum_{p\mid R_y}v_p(R_y)\,
 \delta_{\left(\log p/\log\vert R_y\vert ,\,\mathrm{Frob}_p\right)}
$$

converges to the following conservation-corrected product object: the small valuations have their polynomial Kubilius law (independent exact local limit laws for the small-prime valuations), and conditional on their consumed logarithmic mass the residual process is a scale-invariant Poisson process of intensity $$du/u$$, marked by Conjecture 46, conditioned to have total mass one. The small field and the unconditioned residual Poisson process are asymptotically independent, and all leading dependence after conditioning is the single residual-mass constraint.

For disjoint normalized size bands bounded away from zero, the unconditioned residual process has independent increments. Its mesoscopic restriction and its ranked macroscopic atoms yield respectively the scale-invariant factor process and the Frobenius-marked $$\operatorname{PD}(1)$$ partition. Thus the local Kubilius field is the boundary variable fixing the available mass, while the mesoscopic and macroscopic laws are two projections of one residual process, and no additional cross-scale coupling survives.

*Significance.* Raw small–large independence is false because small factors consume mass. This conjecture identifies the complete conservation-corrected product structure and adds the mesoscopic scale that is absent from a two-scale statement. It would justify, in one limit theorem, the local sieve model, the scale-invariant factor process, and the macroscopic partition.

**Adelic Gibbs gluing for reducible polynomial values (Conjecture 48).** Let $$f=\prod_{i=1}^s g_i$$ be squarefree with irreducible components, sample $$n\in[N,2N]$$, and put $$t=n/N$$. For each prime $$p$$, let $$\nu_p$$ be the exact Haar law on $$\mathbb Z_p$$ of the valuation vector $$(v_p(g_1(x)),\ldots,v_p(g_s(x)))$$. For $$y\to\infty$$ with $$\log y=o(\log N)$$, consider stable convergence jointly with the archimedean coordinate $$t$$ and condition on $$\mathscr L_y=(v_p(g_i(n)))_{p\le y,i\le s}$$. After normalizing each component by its own residual logarithmic mass, the coloured Frobenius-marked factor processes converge to conditionally independent copies of the three-scale law of Conjecture 47, with the marks of Conjecture 46.

Unconditionally, the joint process is the projective Gibbs mixture obtained by integrating those conditional product laws against Lebesgue measure in $$t$$ and the adelic local law $$\bigotimes_p\nu_p$$, in the iterated order $$N\to\infty$$ and then $$y\to\infty$$. Every bounded finite-dimensional Laplace functional is determined by

$$
Z_p(\mathbf z)=\int_{\mathbb Z_p}\prod_i z_i^{v_p(g_i(x))}\,dx
$$

together with the archimedean size profile $$(\log\vert g_i(Nt)\vert )_i$$. No additional colour coupling survives after this adelic–archimedean mixture.

*Significance.* A scalar Euler factor cannot specify a point process. This statement gives the full local-to-global gluing rule and includes the archimedean variable that can couple component sizes. It is functorial under multiplying, splitting, or regrouping components. A persistent medium-prime or archimedean coupling after the stated mixture would identify a new nonadelic invariant.

**Full multivariate adelic saddle law for joint smoothness (Conjecture 49).** Let $$f_1,\ldots,f_s\in\mathbb Z[x]$$ be pairwise coprime and primitive, sample $$n\in[N,2N]$$, and put $$t=n/N$$. For complex variables $$\mathbf s$$ and smoothness bounds $$\mathbf y$$, define

$$
\mathcal Z_{p,\mathbf y}(\mathbf s)=
 \int_{\mathbb Z_p}p^{-\sum_{i:p\le y_i}(s_i-1)v_p(f_i(x))}\,dx,
 \qquad
 \widehat{\mathcal Z}_{p,\mathbf y}(\mathbf s)=
 \frac{\mathcal Z_{p,\mathbf y}(\mathbf s)}
      {\mathcal Z_{p,\mathbf y}(+\boldsymbol\infty)}.
$$

The denominator is the exact Haar probability that $$p$$ divides none of the relevant $$f_i(x)$$. Put

$$
\Phi_t(\mathbf s)=
 \sum_p\log\widehat{\mathcal Z}_{p,\mathbf y}(\mathbf s)
 +\sum_i(s_i-1)\log\vert f_i(Nt)\vert .
$$

For $$f(x)=x$$, this gives the usual truncated zeta factor $$(1-p^{-s})^{-1}$$. Define the joint local probability by the Perron-calibrated multivariate inverse Mellin integral

$$
\mathscr P_t^{\mathrm{joint}}=
 \frac{1}{(2\pi i)^s}
 \int_{\boldsymbol\sigma_t+i\mathbb R^s}
 e^{\Phi_t(\mathbf s)}\prod_{i=1}^s\frac{ds_i}{s_i},
$$

with the standard truncated-contour limit, where $$\boldsymbol\sigma_t$$ is the unique real saddle in the admissible region. The factors $$s_i^{-1}$$ are part of the canonical cumulative smoothness event, and for one variable they recover the Hildebrand–Tenenbaum Perron normalization [55].

Uniformly when every $$u_i(t)=\log\vert f_i(Nt)\vert /\log y_i$$ lies in a fixed compact saddle-point region,

$$
\mathbb P(P^+(f_i(n))\le y_i\ \forall i)
 \sim\int_1^2\mathscr P_t^{\mathrm{joint}}\,dt.
$$

The integral has the full multivariate saddle expansion. Writing $$H_t=\nabla^2\Phi_t(\boldsymbol\sigma_t)$$, its leading term includes the joint action, the amplitude $$\prod_i\sigma_{i,t}^{-1}$$, and $$(\det H_t)^{-1/2}$$, with the usual lattice correction when the valuation span is proper.

If $$\mathscr P_{i,t}^{\mathrm{marg}}$$ are the identically calibrated one-polynomial probabilities, then $$\mathscr P_t^{\mathrm{joint}}/\prod_i\mathscr P_{i,t}^{\mathrm{marg}}$$ is the complete ratio of joint and marginal actions, Perron amplitudes, Hessian determinants, and lattice corrections. Its Euler-product component is the ratio of the exact $$p$$-adic partition functions evaluated at the joint and marginal saddles. None of these factors may be replaced by a scalar Euler correction at the marginal saddle.

*Significance.* The statement is calibrated to the cumulative smoothness probability. It combines exact higher $$p$$-adic valuations, moving archimedean sizes, the joint saddle displacement, Perron amplitudes, mixed curvature, and possible lattice effects. Even one-polynomial smooth-value asymptotics are difficult [52, 53]. A complete multivariate adelic saddle law would be a major new local–global bridge.

**Buchstab–Bateman–Horn component flow (Conjecture 50).** Let $$f\in\mathbb Z[x]$$ be primitive, irreducible, and admissible ($$\rho_f(p)<p$$ for every prime $$p$$), and sample $$n\in[N,2N]$$. For $$y$$ with $$u_n=\log\vert f(n)\vert /\log y$$ in a fixed compact subset of $$(1,\infty)$$, let $$\Omega_y(f(n))$$ be the number of prime factors of $$f(n)$$ exceeding $$y$$, counted with multiplicity, on the event $$P^-(f(n))>y$$. Put

$$
V_f(y)=\prod_{p\le y}\left(1-\frac{\rho_f(p)}p\right).
$$

Define the Buchstab component functions by

$$
\omega_1(u)=\frac1u,
 \qquad
 \omega_j(u)=\frac{1}{u(j-1)!}
 \int_{\substack{t_1,\ldots,t_{j-1}\ge1\\
 t_1+\cdots+t_{j-1}\le u-1}}
 \frac{dt_1\cdots dt_{j-1}}{t_1\cdots t_{j-1}}
 \quad(j\ge2),
$$

so that $$\sum_{j\ge1}\omega_j(u)=\omega(u)$$. Then for every fixed $$j$$,

$$
\mathbb P\bigl(P^-(f(n))>y,\ \Omega_y(f(n))=j\bigr)
 =V_f(y)e^\gamma\mathbb E_{n\in[N,2N]}\omega_j(u_n)+o(V_f(y)),
$$

uniformly on compact $$u$$-ranges. Conditional on the ordered logarithmic sizes of the $$j$$ remaining factors, their unramified Frobenius marks are independent with the fixed-point-size-biased law of Conjecture 46. Summing over $$j$$ gives the rough-value Buchstab law, $$j=1$$ gives the Bateman–Horn prime density, and $$j=2$$ gives the semiprime transition. Whenever $$\max_{N\le n\le2N}\vert f(n)\vert <y^2$$, every rough value has exactly one prime factor above $$y$$, so the $$j=1$$ component exhausts the rough set, while the density formula itself remains conjectural.

*Significance.* The conjecture resolves a rough polynomial value into its complete finite-$$u$$ factor count and Galois mark content. Primes and semiprimes are not inserted as separate heuristics. They are components of one universal flow. Generalized Buchstab equations are the random-integer antecedent [60], and the fixed-polynomial, Galois-marked component law with its local factors is the new statement. It is strongly falsifiable even when total roughness follows Buchstab.

## 6. Stress tests and independent recomputation

Each statement was tested three ways: against the literature, against computation well beyond its original range, and against an independent reimplementation.

*Layer 1: literature.* Five independent searches combed OEIS, arXiv, and the standard references for prior art, producing the novelty labels and the attributions used throughout. Each search was run at neighbourhood depth: defining objects, derived sequences, OEIS comments, and the abstracts and bodies of near-neighbour papers read in full rather than skimmed from search summaries—the depth at which, for instance, OEIS A088054’s intersection comment (Conjecture 21(ii)) and the second half of Lillie’s abstract (the primorial companion) are found, neither being visible in the defining sequences or in a search snippet. This layer also fixes two attributions used above: the $$k\ge1$$ Stern list of Conjecture 12 is OEIS A060003 verbatim, with $$1493$$ the largest known Stern prime, and the primorial-twin statement is Lillie’s [5].

*Layer 2: computational refutation.* Every falsifiable-by-instance statement was pushed at least a decade past its original bound: exception hunts across $$(10^8,10^9]$$ for Conjectures 5, 12, 17, 22; the uniformity of Conjecture 8 stressed on $$d\le6000$$; the statistical laws re-tested at $$4\cdot10^9$$ (Conjectures 1, 4, 9, 11, and 13, and the quintuplet calibration count reported with Conjecture 8); the recovery clause of Conjecture 3 tested on fresh moduli $$q\in(3000,6000]$$. No statement moved.

Each statement was also verified at production scale: the Conjecture 10 profile across $$150$$ shifts and the moment law for its constants $$C(d)$$ (derived mean $$2.7456$$ and sd $$1.6840$$ against measured $$2.7434$$ and $$1.6726$$); the cubic family moments and uniformity of Conjecture 15 ($$294$$ constants, $$57$$ count profiles); the triplet and sexy-pair races of Conjectures 18 and 19 at $$10^9$$ and the Stern lanes of Conjecture 12 on $$2{,}500$$ samples at $$10^8$$; the chain of Conjecture 24 over five decades to $$10^7$$; the null race of Conjecture 14 at $$10^7$$; the Fibonacci–Lucas joint scan to $$p\le10^4$$; factorial twins to $$n=700$$; the CRT-exact factorization of Conjecture 6 through a joint period of $$1.2\times10^8$$, with the scan extended to $$n=6000$$; the pinned average $$G(H)$$ of Conjecture 2 computed exactly to $$H=3000$$; the boundary trichotomy of Conjecture 22 with two new lanes counted at $$10^6$$; the least-summand law of Conjecture 5 on $$2{,}000$$ samples; the covariance kernels of Conjectures 8(ii) and 16(ii) evaluated over $$870$$ and $$1{,}225$$ pairs, with the moving-window randomization of Conjecture 8(ii) over $$2000$$ windows (empirical correlation matrix matching the predicted kernel entrywise at $$0.86$$); the orientation-resolved twin-member profile of Conjecture 17 on $$150$$ samples; the race autocorrelation and running-maximum measurements of Conjecture 9 at $$10^9$$ against simulated nulls; the singular-series waiting-time clause of Conjecture 11(iii) (regression coefficient $$-0.466$$ against the predicted $$-\tfrac12$$); the stratified experiment of Conjecture 3 on $$80$$ moduli; the multibase quotient tests of Conjecture 7 on $$664{,}577$$ primes; and the weighted drift and internal null lane of Conjecture 4 on $$400$$ fresh samples, together with the cousin-race predictions of the contamination calculus, Conjecture 1(v), at $$10^9$$ (leadership log-densities $$0.99$$ and $$0.92$$ on the predicted sides). In each case the prediction was derived before the corresponding data were taken.

*Layer 3: independent replication.* Constants were recomputed from their definitions, and sequences recounted, by implementations developed independently of the primary computation and working from the bare statements alone. All recomputed constants landed inside the stated truncation error, and all recounts agreed. The same layer reproduced the Fibonacci deficit recorded at Conjecture 20 and the ordering anomaly of Remark 1, confirming that both are properties of the primes rather than of a single implementation.

One methodological conclusion is worth recording. The mathematical failure modes in this subject are not statistical but *algebraic*: factorizations and congruence collapses living on density-zero or positive-density-but-structured subsequences—the cubes obstructing $$n=p+k^3$$ (Theorem 1), the composite-$$k$$ factorization of $$D_k$$ (Conjecture 23(i)), the $$k=4$$ parity branch of Conjecture 25, the inadmissible naive chain of Conjecture 24. Probabilistic sanity checks, however extensive, integrate over density and cannot see such families; only structural tests—testing a claimed exception census on special subsequences, for instance—find them. A verification that only re-runs an existing count at a larger bound is blind to every one of them.

## 7. An open question

**Question 1.**

Determine $$\theta(q)$$ of Conjecture 3: derive, from the Hardy–Littlewood correlations or otherwise, the first-order deficit of $$\mathbb E_a\,\mathrm{Li}(p(a,q))/\varphi(q)$$ below its random-model value $$1$$—equivalently, explain quantitatively why the primes in their natural order occupy residue classes faster than any exchangeable resampling of themselves.

## References

1. G. H. Hardy and J. E. Littlewood, *Some problems of ‘Partitio numerorum’; III: On the expression of a number as a sum of primes*, Acta Math. 44 (1923), 1–70. DOI: 10.1007/BF02403921.

2. P. T. Bateman and R. A. Horn, *A heuristic asymptotic formula concerning the distribution of prime numbers*, Math. Comp. 16 (1962), 363–367. DOI: 10.1090/S0025-5718-1962-0148632-7.

3. D. R. Heath-Brown, *Primes represented by $$x^3+2y^3$$*, Acta Math. 186 (2001), 1–84. DOI: 10.1007/BF02392715.

4. C. K. Caldwell and Y. Gallot, *On the primality of $$n!\pm1$$ and $$2\times3\times5\times\cdots\times p\pm1$$*, Math. Comp. 71 (2002), 441–448. DOI: 10.1090/S0025-5718-01-01315-1.

5. G. Lillie, *About the primality of primorials*, arXiv:2110.04302 [math.NT] (2021).

6. M. Rubinstein and P. Sarnak, *Chebyshev’s bias*, Experiment. Math. 3 (1994), no. 3, 173–197. DOI: 10.1080/10586458.1994.10504289.

7. J. Grantham and A. Granville, *Fibonacci primes, primes of the form $$2^n-k$$ and beyond*, J. Number Theory 261 (2024), 190–219; arXiv:2307.07894. DOI: 10.1016/j.jnt.2024.02.002.

8. S. S. Wagstaff, Jr., *Divisors of Mersenne numbers*, Math. Comp. 40 (1983), 385–397. DOI: 10.1090/S0025-5718-1983-0679454-X.

9. H. Dubner, *Twin prime conjectures*, J. Recreational Math. 30, no. 3 (1999–2000) (article reproduced at OEIS A007534).

10. H. Dubner, *Carmichael numbers of the form $$(6m+1)(12m+1)(18m+1)$$*, J. Integer Seq. 5 (2002), Article 02.2.1.

11. E. Kowalski, *Averages of Euler products, distribution of singular series and the ubiquity of Poisson distribution*, Acta Arith. 148 (2011), no. 2, 153–187; arXiv:0805.4682.

12. T. Oliveira e Silva, S. Herzog, and S. Pardi, *Empirical verification of the even Goldbach conjecture and computation of prime gaps up to $$4\cdot10^{18}$$*, Math. Comp. 83 (2014), no. 288, 2033–2060. DOI: 10.1090/S0025-5718-2013-02787-1.

13. K. Martin, *Refined Goldbach conjectures with primes in progressions*, Exp. Math. 31 (2022), 226–232; arXiv:1806.00946. DOI: 10.1080/10586458.2019.1596849.

14. D. A. Goldston and A. H. Ledoan, *Jumping champions and gaps between consecutive primes*, Int. J. Number Theory 7 (2011), 1413–1421; arXiv:0910.2960. DOI: 10.1142/S179304211100471X.

15. A. Kourbatov, *Maximal gaps between prime $$k$$-tuples: a statistical approach*, J. Integer Seq. 16 (2013), Article 13.5.2; arXiv:1301.2242. See also arXiv:1309.4053.

16. D. Shanks, *On maximal gaps between successive primes*, Math. Comp. 18 (1964), 646–651. DOI: 10.1090/S0025-5718-1964-0167472-8.

17. A. Granville, *Harald Cramér and the distribution of prime numbers*, Scand. Actuar. J. 1995:1, 12–28. DOI: 10.1080/03461238.1995.10413946.

18. P. X. Gallagher, *On the distribution of primes in short intervals*, Mathematika 23 (1976), 4–9. DOI: 10.1112/S0025579300016442.

19. H. L. Montgomery and K. Soundararajan, *Primes in short intervals*, Comm. Math. Phys. 252 (2004), 589–617. DOI: 10.1007/s00220-004-1222-4.

20. T. Haddad, S.-K. Leung, and C. Sabuncu, *Visiting early at prime times*, arXiv:2408.11781 (2024). DOI: 10.48550/arXiv.2408.11781.

21. S. S. Wagstaff, Jr., *Greatest of the least primes in arithmetic progressions having a given modulus*, Math. Comp. 33 (1979), 1073–1080. DOI: 10.1090/S0025-5718-1979-0528061-7.

22. R. Crandall, K. Dilcher, and C. Pomerance, *A search for Wieferich and Wilson primes*, Math. Comp. 66 (1997), 433–449. DOI: 10.1090/S0025-5718-97-00791-6.

23. M. J. Jacobson, Jr. and H. C. Williams, *New quadratic polynomials with high densities of prime values*, Math. Comp. 72 (2003), 499–519. DOI: 10.1090/S0025-5718-02-01418-7.

24. R. J. Lemke Oliver and K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, Proc. Natl. Acad. Sci. USA 113 (2016), E4446–E4454; arXiv:1603.03720. DOI: 10.1073/pnas.1605366113.

25. A. Kourbatov and M. Wolf, *On the first occurrences of gaps between primes in a residue class*, J. Integer Seq. 23 (2020), Article 20.9.3; arXiv:2002.02115.

26. M.-A. Sanchis-Lozano, *A heuristic study of the distribution of primes in short and not-so-short intervals*, arXiv:1804.07659 (2018). DOI: 10.48550/arXiv.1804.07659.

27. S. Sahoo, *On twin prime distribution and associated biases*, arXiv:2111.09053 (2021). DOI: 10.48550/arXiv.2111.09053.

28. W. Puszkarz, *Statistical bias in the distribution of prime pairs and isolated primes*, arXiv:1807.00406 (2018). DOI: 10.48550/arXiv.1807.00406.

29. S.-K. Leung, *Moments of primes in progressions to a large modulus*, Forum Mathematicum, published online 26 August 2024; arXiv:2402.07941.

30. A. Fiori, *The least prime in arithmetic an progression* [sic], arXiv:2404.02329 (2024). DOI: 10.48550/arXiv.2404.02329.

31. H. Cohen, *High precision computation of Hardy–Littlewood constants*, unpublished notes (PDF hosted at OEIS A221712).

32. N. A. Carella, *Twin primes in quadratic arithmetic progressions*, arXiv:1710.07827 (unrefereed preprint). DOI: 10.48550/arXiv.1710.07827.

33. T. H. Chan, *More precise pair correlation of zeros and primes in short intervals*, arXiv:math/0206292.

34. V. Kuperberg, *Odd moments in the distribution of primes*, arXiv:2109.03767.

35. V. Kuperberg, B. Rodgers and E. Roditty-Gershon, *Sums of singular series and primes in short intervals in algebraic number fields*, arXiv:2001.09513.

36. J. Li, K. Pratt and G. Shakan, *A lower bound for the least prime in an arithmetic progression*, arXiv:1607.02543.

37. M. M. Wood, *Cohen–Lenstra heuristics and local conditions*, arXiv:1710.01350.

38. N. M. Katz, *Wieferich past and future*, Contemporary Mathematics 632 (2015), 253–270.

39. I. E. Shparlinski, *Fermat quotients: exponential sums, value set and primitive roots*, arXiv:1104.3909.

40. G. Gras, *Etude probabiliste des quotients de Fermat*, Funct. Approx. Comment. Math. 54 (2016), arXiv:1409.2815.

41. G. Boeckle, D.-A. Guiraud, S. Kalyanswamy and C. Khare, *Wieferich primes and a mod $$p$$ Leopoldt conjecture*, arXiv:1805.00131.

42. Y. Wang and R. P. Stanley, *The Smith normal form distribution of a random integer matrix*, arXiv:1506.00160.

43. R. Van Peski, *Limits and fluctuations of $$p$$-adic random matrix products*, arXiv:2011.09356.

44. R. Jones, *Galois representations from pre-image trees: an arboreal survey*, arXiv:1402.6018.

45. B. Kadets, *Large arboreal Galois representations*, arXiv:1802.09074.

46. J. Thorner and A. Zaman, *A unified and improved Chebotarev density theorem*, arXiv:1803.02823.

47. E. Kowalski, *The large sieve, monodromy and zeta functions of curves*, J. reine angew. Math. 601 (2006), 29–69, arXiv:math/0503714.

48. D. Krumm, *Galois groups in a family of dynatomic polynomials*, arXiv:1707.02501.

49. K. Doerksen and A. Haensch, *Primitive prime divisors in zero orbits of polynomials*, arXiv:1009.3971.

50. S. Yang and X. Zhong, *Dynamical GCD problems and a variant of the Dynamical Mordell–Lang conjecture*, arXiv:2602.18302.

51. A. Bharadwaj and B. Rodgers, *Large prime factors of well-distributed sequences*, arXiv:2402.11884.

52. G. Martin, *An asymptotic formula for the number of smooth values of a polynomial*, arXiv:math/9909180.

53. M. Mine, *An upper bound for the number of smooth values of a polynomial and its applications*, arXiv:2410.09558.

54. D. A. Goldston and H. L. Montgomery, *Pair correlation of zeros and primes in short intervals*, in Analytic Number Theory and Diophantine Problems, Progr. Math. 70, Birkhäuser, 1987, 183–203.

55. A. Hildebrand and G. Tenenbaum, *On integers free of large prime factors*, Trans. Amer. Math. Soc. 296 (1986), 265–290.

56. A. Medvedev and T. Scanlon, *Invariant varieties for polynomial dynamical systems*, Ann. of Math. 179 (2014), 81–177, arXiv:0901.2352.

57. N. Fellini and M. R. Murty, *Wieferich primes in number fields and the conjectures of Ankeny–Artin–Chowla and Mordell*, J. Number Theory 285 (2026), 209–229; arXiv:2508.08472.

58. R. Li and J. Zhao, *Non-Wieferich property of prime ideals and a conjecture of Erdős*, arXiv:2601.12753.

59. J. Fariña-Asategui, *Arboreal Galois representations of rational functions: fixed-point proportion and the extension problem*, arXiv:2601.19414.

60. P. Moree, *A generalization of the Buchstab equation*, Manuscripta Math. 94 (1997), 267–270.

## Explanations

### Conjecture 1: Prime-power contamination calculus

The weighted twin count $$\psi_2(x)=\sum_{n\le x}\Lambda(n)\Lambda(n+2)$$ contains terms in which one entry is a prime square rather than a prime. Lemma 1 shows that the only surviving configuration is $$(q^2-2,q^2)$$, and that its first entry is never $$1$$ modulo $$5$$ and always $$7$$ modulo $$8$$. Passing to the unweighted count removes exactly this mass, so the classes that held it are left with fewer twins. The conjecture is that this removed mass is the whole deterministic difference between classes, stated as convergence of a logarithmic mean at the scale of the drift itself, with an explicit Bateman and Horn constant as the limit. This is the same mechanism that produces Chebyshev's bias, where squares of primes displace the count in the class $$1$$ modulo $$4$$. Conjectures 4, 12, 18 and 19 apply the operator to other patterns, and Conjecture 14 supplies the pattern where it provably vanishes.

### Conjecture 2: Pinned singular-series variance

Montgomery and Soundararajan reduced the variance of prime counts in short intervals to an average of singular series. This conjecture performs the same reduction for twin pairs. The variance of the windowed pair count is governed by $$G(H)$$, an average of four-point tuple constants in which two of the four positions are frozen into the twin pattern. Clause (i) is a conditional proposition, following from quantitative tuple estimates. The conjecture proper is clause (ii), that $$-G(H)/\log H$$ diverges, so that pair counts are more strongly sub-Poisson than prime counts. It supplies the diagonal term left open in Conjecture 8 and stands to Conjecture 13 as pairs stand to single primes.

### Conjecture 3: Least-prime ordering deficit

Normalize the least prime in a residue class by its expected arrival time, $$U(a,q)=\mathrm{Li}(p(a,q))/\varphi(q)$$. Leung proved, under uniform tuple hypotheses, that $$U$$ has a unit exponential limit. The new claim is second order: the mean of $$U$$ falls below $$1$$ by an amount whose dyadic average, multiplied by $$\log q$$, converges to a positive constant. The primes in their natural order occupy residue classes faster than any exchangeable rearrangement of themselves. Two deterministic effects, discreteness of the hazards and the injectivity of primes below $$q$$, are computed and subtracted, and neither explains the measured value. Conjecture 5 is the Goldbach analogue, and deriving the constant from pair correlations is posed as Question 1.

### Conjecture 4: Goldbach lane race

For $$n\equiv2\pmod4$$, split the Goldbach representations by whether both summands are $$1$$ or both $$3$$ modulo $$4$$. An odd prime square is $$1$$ modulo $$4$$, so every term $$n=q^2+p$$ falls in the first lane, and removing this non-prime mass leaves the $$(3,3)$$ lane ahead. The conjecture identifies the lead with the computed census exactly, in logarithmic mean. The mechanism also predicts where it must switch off: for $$n\equiv1\pmod3$$ the complements $$n-q^2$$ are divisible by $$3$$, so the drift vanishes on $$n\equiv10\pmod{12}$$. This internal null lane makes the conjecture more falsifiable than a bare bias claim. It is the representation-problem counterpart of Conjecture 1.

### Conjecture 5: Least Goldbach summand

The least prime $$p$$ with $$n-p$$ prime arrives, on the expected-arrival clock, exponentially distributed, and on average slightly early. Clause (i) states the exponential law under an explicit logarithmic sampling measure. Clause (ii) states the earliness: the deficit of the mean below $$1$$, scaled by $$\log X$$, converges to a positive constant. The mechanism is the same occupancy effect as in Conjecture 3, and the measured constant is about twice the least-prime one, a ratio the pair-correlation expansion should explain. The extremal size of the least summand was studied by Granville, van de Lune and te Riele and computed extensively by Oliveira e Silva, Herzog and Pardi. The distributional law and the deficit appear to be new.

### Conjecture 6: Polynomial-exponential entanglement

Primality of $$n^2+2^n$$ imposes local conditions that depend on $$n$$ through two different moduli at once, $$p$$ and the multiplicative order of $$2$$ modulo $$p$$. A product of per-prime densities would assume these conditions independent, which nothing justifies. The conjecture instead uses survivor densities computed exactly over the joint period of all primes up to $$z$$, asserts that these converge along the canonical exhaustion, and asserts that the limit governs the count, which grows like $$\log N$$. The computation found the joint density to factor exactly through $$p\le19$$, and whether that persists is left as an open question about the orbits of $$2$$. The slot is a model for prime counting in sequences outside the polynomial world of Bateman and Horn.

### Conjecture 7: Multibase Fermat quotients

The Fermat quotient $$q_p(a)=(a^{p-1}-1)/p$$ is additive in the base, so quotients of multiplicatively dependent bases are confined to a rational subtorus. The principal claim is the complement: for multiplicatively independent bases the vector of normalized quotients equidistributes on the full torus as $$p$$ varies. This is a vertical law, in contrast to the fixed-$$p$$ statistics of Ostafe and Shparlinski and of Cobeli and Zaharescu. The single-base clauses calibrate fluctuations at exactly the strength an independent uniform model earns, a two-sided law of the iterated logarithm for the discrepancy and an almost-sure central limit law for the Wieferich count (primes $$p$$ with $$q_p(2)\equiv0$$, equivalently $$2^{p-1}\equiv1\bmod p^2$$) at the classical logarithmic weighting. The finiteness of simultaneous Wieferich primes follows the convergent Borel and Cantelli side. The clauses side with the Crandall, Dilcher and Pomerance model against Gras's, and the disagreement is testable.

### Conjecture 8: Uniform de Polignac covariance field

Clause (i) asserts the Hardy and Littlewood pair asymptotic uniformly in the gap $$d$$ up to a power of $$\log x$$, so a thousand singular-series values must be matched at once. Clause (ii) treats the residuals of all gaps as one random field over a moving window and derives its covariance. The leading term comes from configurations in which two pairs share a prime, giving a kernel built from triple constants, valid when $$\max(d,d')$$ is small compared with the window. The next term is an off-index four-point sum of the kind isolated in Conjecture 2. Both kernels vanish in the limit, so the field is asymptotically independent Poisson or Gaussian, and the content is the finite-$$x$$ correction, not a limiting dependence.

### Conjecture 9: Race sub-diffusivity

Recording a balanced race step by step at its event times gives a walk whose increments are measurably anticorrelated. Clause (i) proposes that the lag correlations decay like $$(\log\log x)/\log x$$, with the consecutive-pattern repulsion of Lemke Oliver and Soundararajan as the mechanism. Clause (ii) states, under summability hypotheses that are part of the statement, that the diffusivity returns to $$1$$, making sub-diffusivity a finite-height phenomenon. Clause (iii) records the honest alternative as an exclusive dichotomy: either those hypotheses hold and the race is diffusive, or the expansion fails at long lags and the race may inherit the almost-periodic rigidity that Rubinstein and Sarnak found for classical races. The summability hypotheses are model assumptions rather than assertions, and the dichotomy is left open here. Conjecture 1 takes the rigid side for its contaminated races, so the two conjectures together locate exactly where the hypotheses would have to fail. No explicit formula is known for twin patterns, so the question is genuinely open.

### Conjecture 10: Uniform quadratic de Polignac and its constants

This is the quadratic analogue of Conjecture 8, for pairs $$n^2+1$$ and $$n^2+1+d$$. Beyond the uniform count and a separately registered power-saving error, clause (iii) treats the constants $$C(d)$$ themselves as a statistical family. Local factors at finitely many primes are exactly independent as $$d$$ varies, by the Chinese remainder theorem, and the convergent variance sum carries the mean and moments through the infinite product. The moments converge to derived Euler products with mean $$2.7456\ldots$$ and standard deviation $$1.6840\ldots$$, and the empirical distribution converges to the law of a random Euler product, in the spirit of Kowalski's theory of singular-series distributions.

### Conjecture 11: First occurrences of prime gaps

Write $$p(g)$$ for the prime starting the first occurrence of a realized gap $$g$$. The first-order size of $$\log p(g)$$ is $$\sqrt g$$. Clause (ii) gives the liminf constant $$\sqrt{\mathrm{e}^{\gamma}/2}$$ as the dual of the Cramér and Granville maximal-gap envelope, conditional on a stated realization hypothesis, because inverting a limsup is not automatic. Clause (iii) is the sharpest part: the correction to $$\sqrt g$$ contains $$-\tfrac12\log\mathfrak{S}^{*}(g)$$, so smooth gaps appear earlier by half the logarithm of their tuple constant, and the remaining error follows a min-type Gumbel law at scale $$\tfrac12$$, both features forced by a first-passage computation whose log-intensity has slope $$2$$. Gumbel modelling of gaps is due to Kourbatov and Wolf, and only the singular-series centring and the scale are claimed here.

### Conjecture 12: Stern lane race

In Stern's problem $$n=p+2k^2$$, race the representations with $$k$$ even against those with $$k$$ odd. Contamination comes from $$n=q^2+2k^2$$ with $$q$$ prime, the norm form of $$\mathbb Q(\sqrt{-2})$$, and a two-line congruence shows it sits in the even lane exactly for $$n\equiv1\pmod8$$, the odd lane for $$n\equiv3$$, and cannot exist for $$n\equiv5,7$$. The two null classes are therefore provable, the strongest kind of control. The drift clause matches the clean-minus-contaminated difference to the weighted census in a logarithmic ensemble, in the form of Conjecture 4. The averaged size of the contaminating count is itself a hard norm-form problem, so the census is computed exactly per sample.

### Conjecture 13: Microscopic variance law

Gallagher showed that the tuple conjectures force Poisson statistics for primes in intervals of length $$\lambda\log x$$. At finite $$x$$ the variance falls below the Poisson value, and this conjecture asserts the deficit is $$(\log H+\gamma+\log2\pi-1)/\log x$$, the constant being Montgomery and Soundararajan's, extrapolated from their mesoscopic range down to Gallagher's boundary and tested there. The naive Poisson ratio fails by 18 to 28 per cent at accessible heights, and the corrected law matches without fitted parameters. The statement is conditional on quantitative tuple estimates and interpolates across window exponents with no transition. Conjecture 2 plays the same role one level up, for pairs.

### Conjecture 14: Null-mechanism race

For the pair $$n^2+1$$ and $$n^2+3$$ no entry can be a prime square, by elementary algebra, so the contamination operator of Conjecture 1 is identically zero here. The conjecture asserts that the race between the equal-density classes $$1$$ and $$4$$ modulo $$5$$ is correspondingly driftless at the same normalization at which the contaminated races have nonzero limits. A drift here would refute the mechanism, whatever the positive cases show. The occupation clause is conjectured directly rather than derived. A windowed invariance principle is recorded as a separately falsifiable local hypothesis, but a recentred window cannot see the absolute level of the walk, so it cannot deliver the occupation law on its own. The clause asserts that the logarithmic occupation of leadership tends to one half with Gaussian fluctuations of size $$\sqrt{\log2/\log x}$$, the null against which the leadership statistics of Conjectures 1 and 19 are calibrated.

### Conjecture 15: Cubic-shift constants

For non-cube shifts $$a$$, only primes $$p\equiv1\pmod3$$ move the constant of $$x^3+a$$, and the local root count is $$3$$, $$1$$ or $$0$$ according as $$-a$$ is a nonzero cube, divisible by $$p$$, or neither. These weights give expected root count exactly $$1$$ at every prime, and an $$L^2$$ martingale argument carries the identity through the product, so the limiting distribution of $$C(a)$$ has mean exactly $$1$$, the cubic counterpart of Korevaar and te Riele's mean-value theorem. The derived standard deviation is $$0.2762\ldots$$, and the counts are conjectured uniform over $$a\le(\log N)^B$$. No Bunyakovsky-type theorem exists for any cubic, Heath-Brown's $$x^3+2y^3$$ being the nearest result.

### Conjecture 16: Conjecture F as a family

Hardy and Littlewood's Conjecture F concerns prime values of $$n^2+n+A$$. Here the parameter $$A$$ becomes the family variable: the counts are conjectured uniform over odd $$A$$ up to a power of $$\log N$$, and the windowed residuals of different members are given a same-index covariance $$[C(A,A')-C(A)C(A')]H/4\log^2N$$, negative where the pair is locally exclusive. The off-index part of the covariance, the two-parameter analogue of $$G(H)$$, is generically larger and remains open, so the observed cancellation of the same-index kernel is not read as independence. Euler's $$A=41$$ carries the largest constant in the computed range.

### Conjecture 17: Twin-member Goldbach, orientation-resolved

Dubner conjectured that every even number from some point on is a sum of two members of twin pairs. Each summand can be the lower or upper member of its pair, so the count splits into four linear systems of four forms, each with its own singular series depending on how the small primes divide $$n$$, $$n\pm2$$ and $$n\pm4$$. Two exact identities reduce the four to two. The prediction requires tuple estimates uniform in the coefficients, which vary with $$n$$, and the measured profile confirms the shape while the level sits below prediction by a second-order amount that is left open rather than fitted away.

### Conjecture 18: Triplet contamination

Applying the operator of Conjecture 1 to the triplet $$(n,n+2,n+6)$$, two of the three square configurations die algebraically and the survivor $$(q^2-2,q^2,q^2+4)$$ needs two simultaneous primality conditions. This double thinning costs a logarithm, so the drift is weaker than in pair races by exactly one power, a prediction internal to the calculus. The surviving configuration starts in class $$2$$ modulo $$5$$, so class $$1$$ leads, with the drift-scale limit equal to the Bateman and Horn constant of the triple. The value of the conjecture is that census, class assignment and scale are all forced in advance.

### Conjecture 19: Sexy-pair contamination matrix

For gaps of six, both square orientations survive, on complementary classes of $$q$$ modulo $$5$$, and they feed different residue classes. The drift is therefore a matrix rather than a single number, with two independently computable constants, and the classes $$2$$ modulo $$5$$ and $$5,7$$ modulo $$8$$ provably clean. This is the calculus's test of superposition: two mechanisms acting on one pattern must produce exactly the predicted vector. The scale accounting puts sharp confirmation near $$10^{14}$$, so at present the matrix is registered with consistent signs.

### Conjecture 20: Fibonacci and Lucas twins

Prime divisors of $$F_p$$ have rank of apparition $$p$$ (the least index $$m$$ with $$p\mid F_m$$) and odd prime divisors of $$L_p$$ have rank $$2p$$, so the two numbers share no odd prime factor. This removes one source of dependence but not those entering through the order structure, in the sense of Grantham and Granville. The conjecture is that only finitely many $$p$$ give both prime, the joint hazards having convergent sum. The naive independence accounting prices the catalogued index $$148091$$, at which both values are probable primes, at odds of about three in a thousand. That figure is recorded descriptively as a rare event, with no significance claim attached, because the model was examined only after the index was known. It is enough to leave the finiteness claim without a completeness list.

### Conjecture 21: Factorial twins

Around $$n!$$ every offset $$a$$ with $$2\le\vert a\vert\le n$$ is composite, an immediate theorem, so the only bounded-offset question is the twin one, and OEIS records the conjecture that $$n=3$$ is its only solution. The fluctuation clause concerns a declared random model with the Caldwell and Gallot hazards, and asserts a central limit law for $$F_+-F_-$$, the difference between the counts of prime $$n!+1$$ and prime $$n!-1$$, under three explicit hypotheses, a same-index decorrelation, a cross-index covariance bound, and a higher-cumulant condition. The three are irredundant, and whether the arithmetic of nested factorials satisfies them is the open content. Counts beyond $$n\approx26$$ are probable-prime counts.

### Conjecture 22: Boundary trichotomy

If $$F$$ has degree at least two and positive leading coefficient, then $$F(m)-F(j)$$ prime forces $$j=m-1$$, so every representation problem $$F(m)=p+F(j)$$ collapses to its boundary polynomial $$F(m)-F(m-1)$$. For $$x^3+cx$$ the boundary is $$3m^2-3m+1+c$$ and the parameter space splits three ways, dead by parity, dead $$3$$-adically, or admissible exactly when $$c\equiv0,4\pmod6$$, with Bateman and Horn counts conjectured uniformly over the admissible lanes. The case $$c=0$$ is Cunningham's observation on cuban primes. Theorem 1, on cubes escaping $$n=p+k^3$$, is the cautionary instance: obstructions on density-zero families are invisible to probabilistic accounting.

### Conjecture 23: Power-obstruction ladder

Whether $$m^k=p+j^k$$ is solvable splits cleanly on the arithmetic of $$k$$. For composite $$k$$ it never is, a theorem by factorization. For prime $$k$$ it forces $$j=m-1$$ and reduces to the primality of $$D_k(m)=m^k-(m-1)^k$$, irreducible because a root generates the full cyclotomic field of level $$k$$, via $$D_k(x)=(x-1)^{k-1}\Phi_k(x/(x-1))$$. The conjectural clause is Bateman and Horn on each prime lane, with $$k=2$$ already a theorem. The family generalizes the cubic case in Conjecture 22, and $$D_9$$, odd but composite-exponent, is never prime, showing the dividing line is primality, not parity.

### Conjecture 24: Alternating cyclotomic chain

Starting from a prime $$p$$, the repunit value $$\Phi_3(p)=p^2+p+1$$ can be prime, and then $$\Phi_6$$ of that value can be prime again. Iterating $$\Phi_3$$ instead is impossible, since one residue class of $$p$$ modulo $$3$$ kills the first step and the other kills the second, so within the anchored construction space alternation is the unique admissible continuation. The chain is a repunit analogue of a Cunningham chain, its quartic top layer making it the highest-degree system in the paper. The classification of all admissible words in $$\{\Phi_3,\Phi_6\}$$ is left as an open programme. Quartic values beyond $$p\approx2\times10^6$$ are counted as probable primes.

### Conjecture 25: Twin cyclotomic bases

Among the three cyclotomic polynomials of degree two, only $$\Phi_3$$ admits a twin question. For $$\Phi_4$$ parity kills all but one instance, and $$\Phi_6(x)=\Phi_3(x-1)$$ makes the third case a translate of the first. What remains is that $$n^2+n+1$$ and $$n^2+3n+3$$ are simultaneously prime infinitely often, with computed constant, that is, consecutive bases whose length-three repunits are both prime. The companion polynomial is forced by the structure rather than chosen, which is what distinguishes the pair from an arbitrary shifted pair and ties it to the chain of Conjecture 24.

### Conjecture 26: Connected motif generating functional

A single prime pattern has a Hardy and Littlewood singular series, and the question here is what governs the joint fluctuations of many patterns at once. The answer proposed is a cumulant expansion, the cumulants being the joint-fluctuation coefficients that vanish when the patterns are independent, in which every term is a connected diagram, one that does not factor into independent sub-patterns, indexed by the way translated motifs share prime constraints, and weighted by a connected singular series obtained by Möbius inversion over set partitions. The essential subtlety is the bookkeeping of logarithms. A shared constraint of multiplicity $$m$$ contributes a factor $$(\log X)^{m-1}$$, and separating that coincidence in the partition alternation costs at least one logarithm, so the connected part is the genuine leading term while disconnected diagrams cancel to lower order. This turns the singular series into a generating object for a whole arithmetic field rather than a single constant, and the first decisive test is the third cumulant of two distinct pair motifs. The overlap poset that records which constraints coincide is the structure that Conjectures 27 and 30 refine into a filtration and a topological grading.

### Conjecture 27: Complete overlap-renormalization filtration

Reading a single variance formula tells one which overlap dominates, but it does not classify every scale at which a linear combination of prime motifs can become rigid. The filtration conjectured here does exactly that. It orders the covariance strata of Conjecture 26 by their scales, and asserts that the spectral projections of the covariance matrix converge, stratum by stratum, to forms induced by the successive overlap ranks, with nothing living between two adjacent levels. Because scales that share a power of the window length and of the logarithm differ only by powers of the mesoscopic exponent $$\theta=\log L/\log X$$, the statement is made for each fixed $$\theta$$, with the induced forms nondegenerate there. The value of the claim is constructive. It says one can design balanced statistics that annihilate the coarse coincidence ranks and expose genuinely disjoint arithmetic correlation, and a counterexample would name a source of rigidity outside the overlap and disjoint diagrams altogether.

### Conjecture 28: Regularized mesoscopic local–spectral trace formula

Goldston and Montgomery, and later Chan, tied the variance of primes in short intervals to the pair correlation of zeta zeros. This conjecture lifts that equivalence from one prime-counting field to products of shifted von Mangoldt functions, and states it as a genuine trace formula. The local side is a renormalized singular-series form, and the spectral side is built by replacing every von Mangoldt factor with the symmetrically truncated Weil distribution and expanding, so that pole, trivial-zero, diagonal and prime-power terms are all named rather than hidden in a counterterm. The two sides are defined independently and compared only after common mollification, and the regularization independence of the limit is part of the assertion, which is what makes the resulting functional canonical. Failure would reveal a mesoscopic covariance visible in neither the Hardy and Littlewood language nor the language of zeros, which is why the statement is worth the care it demands.

### Conjecture 29: Anchored arithmetic polymer expansion

Occurrences of a prime pattern cluster, and this conjecture gives the cluster geometry an exact arithmetic law. A polymer is a connected set of occurrence starts whose complete union is admissible, and its rarity is graded by the anchored codimension, the number of new prime constraints beyond one occurrence held fixed. The Palm activity of a polymer, its occurrence rate seen from a typical cluster point, is therefore suppressed by that many powers of the logarithm and weighted by the singular series of its union, which corrects the earlier idea of a single universal cluster scale. Because a non-singleton activity carries at least one such power, the clustering is a finite-height phenomenon, and the extremal index that measures long gaps between occurrences departs from one at the motif-dependent exponent $$\delta(H)$$, the smallest codimension of an admissible overlap, with a constant summed over predecessor shifts alone. The construction joins Hardy and Littlewood constants, the low-zero field of Conjecture 28, Palm theory and extreme gaps in one object, and it couples to the terminal law of Conjecture 33 through the same extremal index.

### Conjecture 30: Topological expansion of non-Gaussianity

A central limit theorem only says that normalized odd cumulants vanish, and this conjecture identifies the invariant that controls the first way they fail to. To each connected diagram of Conjecture 26 one attaches its overlap-incidence complex and reads off the first Betti number, the number of independent cycles after forced coincidences are contracted. The claim is that each independent cycle costs one logarithmic order, so that after the coincidence strata are removed the leading non-Gaussian term is carried by incidence trees. For the single-prime field this reproduces the odd-moment scale of Kuperberg, with the coincidence-subtracted spread part obeying $$\kappa^{\mathrm{sp}}_{2m+1}\asymp L^m(\log L)^{m+1}$$ and the raw cumulant adding the explicit coincidence diagrams. The topological grading is the new mechanism, and a failure would show that logarithmic suppression is governed by an arithmetic invariant that the diagram topology cannot see.

### Conjecture 31: Connected first-arrival functional

The least prime in a residue class is an extreme statistic, and rather than track its tail alone this conjecture proposes a full point-process theory for the arrival times. It posits connected factorial-cumulant measures, the point-process analogue of cumulants that records how the arrivals correlate, whose scaled limits are locally finite signed kernels, obtained by averaging the connected Hardy and Littlewood correlations of primes constrained to one class over the modulus. The Laplace functional of the whole arrival process, the generating functional that encodes all of its finite-dimensional laws, is then determined by this hierarchy, so waiting times, occupancy covariance, cover times and terminal clustering all descend from one object. The coupon-collector picture of Li, Pratt and Shakan supplies the nearest extremal analogy, but it does not supply a connected functional, which is the point of the construction. The kernels here are the same ones that Conjecture 32 transports to the character side and that Conjecture 33 uses to decorate the terminal extremes.

### Conjecture 32: Tested Gauss–polyspectral reciprocity

Additive and multiplicative Fourier analysis of a function on the residues are related exactly by the Gauss transform, and this conjecture makes that elementary fact the base of a higher-order reciprocity for the least-prime field. Applied fibrewise at each modulus, the transform carries the additive coefficient vector to the multiplicative one, so every joint cumulant of the scalar tensor observables, the scalar quantities built from tensor products of the additive and multiplicative Fourier coefficients, is defined and matches under the transform before any limit is taken. The conjectural content is what the two families of limits then compute. The additive cumulants converge to the Fourier transforms of the arrival kernels of Conjecture 31 on the zero-sum frequency sublattice, and the multiplicative energies to the low-zero correlations of the corresponding Dirichlet functions. The statement is careful to assert only that these are two compatible tomographic views of one non-Gaussian field, determining a single continuous multilinear functional between them, and a failure would expose information destroyed by both polyspectra, the additive and multiplicative families of higher-order spectra, despite their exact duality.

### Conjecture 33: Rubinstein–Sarnak terminal chaos dichotomy

Rubinstein and Sarnak described prime races for a fixed modulus through a Gaussian field of low zeros, and this conjecture places the terminal least-prime problem in the modulus aspect and asks whether that environment survives. It builds the centred low-zero field, forms its exceedance point process at the natural terminal centring, and offers a covariance-energy statistic that separates two regimes. If the energy vanishes the environment self-averages and the extremes are an ordinary decorated Poisson process, and if it stays positive the environment is a genuine chaos measure, a random multiplicative-chaos intensity, and the extremes form a Cox process, a Poisson process whose intensity is itself random. The clause is honest in treating self-averaging as a serious competitor rather than assuming a Cox limit by terminology. The cluster decorations come from the arrival hierarchy of Conjecture 31, and the extremal index of the terminal process is the last-class analogue of the cluster-start fraction of Conjecture 29.

### Conjecture 34: Nonlinear spectral response calculus

A Siegel zero, a cluster of low zeros and an ordinary prime-race bias are all small perturbations of the arrival intensity, and this conjecture gives a single calculus for how any of them passes through first-arrival statistics. The log-ratio of perturbed to unperturbed survival is expanded in causal Volterra operators, integral kernels that act only on the past, each the linked-cluster contraction, the connected part of the expansion, of the arrival hierarchy of Conjecture 31 with a fixed number of perturbation insertions. The character support propagates predictably, so the linear response preserves character rank and the first new harmonics appear at quadratic order with coefficients from three-point arrival correlations. The exceptional-zero rank-one statement is then a special case rather than a separate hypothesis, and the second-order harmonics give a direct falsification test. The first theorem is the Fréchet derivative read off the two-point occupancy kernel, which is the smallest nontrivial piece of the whole response.

### Conjecture 35: Local-information capacity of odd class groups

Wood established that Cohen and Lenstra statistics persist under fixed local conditions, and this conjecture asks how much local information a class group can absorb before the statistics break. It measures the imposed data by two genuinely different resources, the entropy of the attainable sign cells and the analytic conductor of the primes carrying them, and asserts that the unconditioned law survives in total variation up to a discriminant-cell discrepancy whenever both resources stay subcritical. The two constraints are not the same bound written twice. The same number of sign bits can be imposed at very different moduli, so the entropy governs the impossibility clause while the conductor governs equidistribution, and the boundary is a two-resource principle rather than a single threshold. A proof in any range with the number of primes growing would be a substantial advance, and the structure transfers directly to Selmer groups and ray class groups.

### Conjecture 36: Kummer–Haar law on relation tori

Fermat quotients are the finite logarithms of the rational numbers, and this conjecture identifies exactly the space they equidistribute in. For a saturated multiplicative group the quotient vector is confined to the relation torus, the annihilator of the multiplicative relation lattice, and the claim is that as the prime varies through a compatible cyclotomic and Kummer class the vector fills that torus with Haar measure and no proper subtorus holds its support. The controlling invariant is the saturated rank, not the number of generators one happens to display, so the law is invariant under changing generators. Katz proposed equidistribution principles of this Wieferich type for algebraic groups, and Shparlinski proved estimates in different averaged regimes, and the content added here is the exact relation torus with its disintegration under fixed Kummer data. It turns multiplicative rank into a geometric support theorem, and it is the qualitative law that Conjecture 37 makes quantitative.

### Conjecture 37: Rank-dimensional large sieve for finite logarithms

The equidistribution of Conjecture 36 needs an engine, and this conjecture supplies one in the form of a large sieve whose dual dimension is the saturated rank. For frequencies drawn from a positive power of the residue modulus, the mean square of the exponential sums over Fermat-quotient vectors is bounded by the rank-dimensional count plus the number of primes, uniformly and with the frequency height well defined on the character lattice of the relation torus. A bound over a genuine power range, rather than at fixed frequencies, is what controls shrinking targets, and it lies well beyond the reach of the fixed-frequency tests presently available. The exponent that measures the admissible range is invariant under changing the generating tuple, matching the generator invariance of the support law. A failure would reveal a spacing or energy obstruction among finite-logarithm vectors that the rank alone does not predict.

### Conjecture 38: Mesoscopic-to-lattice shrinking-target transition

Between the fixed targets of Conjecture 36 and the exact Wieferich condition lies a whole family of shrinking targets, and this conjecture makes the saturated rank the invariant that governs the transition across it. For targets that still grow with the prime, Haar geometry rules and the count matches the Haar mass, with a Poisson limit on prime blocks of bounded mass. For a bounded lattice target the law changes, and the count is governed by an arithmetic regulator intensity that need not equal the Haar prediction, so exact Wieferich events sit at the arithmetic end of the transition rather than being an isolated folklore assertion. The two universality classes meet precisely where the target stops growing, which is the content worth isolating. The much rarer fixed-base heuristics discussed by Gras therefore disagree with the Haar model exactly at the lattice boundary, and that disagreement is where the conjecture can be tested.

### Conjecture 39: Global-lattice $$p$$-adic regulator-matrix law

The mod $$p$$ Leopoldt phenomenon concerns when the $$p$$-adic regulator of a number field degenerates, and this conjecture recasts it as a horizontal random-matrix problem with the correct global relation lattice built in. For a fixed Galois field one forms the matrix of finite logarithms of a unit group across the primes above a split rational prime, and this matrix lies in the exact relation module imposed by the norm, the Galois action and the integral multiplicative relations. The claim is that as the prime varies the normalized matrix is Haar on the associated real relation torus, and that determinantal and Smith strata are hit with their exact local densities, with a Poisson law in double-logarithmic time for codimension one and a summable large-prime tail above it. What controls rare regulator defects is therefore the determinantal codimension, not the number of units displayed, and the higher Smith strata retain their deeper $$p$$-adic structure. It is the horizontal identification of the regulator and random-matrix languages, drawing on the work of Böckle, Guiraud, Kalyanswamy and Khare and of Wang, Stanley and Van Peski.

### Conjecture 40: Functorial horizontal logarithms on tori

The Fermat quotient on the multiplicative group is one instance of a finite logarithm, and this conjecture extends the construction to an arbitrary algebraic torus and makes it a functor. Removing the prime-to-$$p$$ torsion lift of a point and dividing by the prime gives an element of the Lie algebra, and for a finitely generated subgroup the normalized matrix is conjectured Haar on the relation subtorus cut out jointly by the algebraic closure of the subgroup and its integral relations. The construction is functorial in that a morphism of tori carries logarithms to logarithms by its differential, and isogenies preserve the shrinking-target intensities after an explicit kernel correction. For the multiplicative group it recovers the Fermat quotient up to sign, which is the consistency check that pins the normalization. This is the geometric home of the Kummer and Haar law of Conjecture 36, extending Katz's algebraic-group viewpoint to a matrix-valued law with full functoriality.

### Conjecture 41: Entropy–conductor profile of arboreal resolution

An arboreal Galois representation is infinite, and only finitely many of its levels can be reconstructed from primes below a bound, so the natural question is how many. This conjecture answers with the scale $$\log_d\log X$$, coming from the doubly exponential growth of the preimage tree, and pins the bounded correction to two profiles read on that growth scale, the Rényi entropy, a one-parameter measure of how spread out the conjugacy weights are, of the nonuniform conjugacy measures and a representation-by-representation Artin-conductor energy, weighted by how ramified each representation is. The earlier idea of a single discriminant proxy is replaced by these character-theoretic quantities, which stay finite where a raw discriminant rate would diverge doubly exponentially. Two families with comparable profiles then have observable depths differing by a bounded amount, and passing to a fixed-index open subgroup shifts the boundary by only a bounded number of levels. It is a phase invariant of an infinite representation rather than a repackaged effective Chebotarev estimate, with the large-image and effective-Chebotarev inputs of Kadets, Thorner and Zaman supplying the ingredients.

### Conjecture 42: Arboreal family large sieve and cumulant independence

Resolution heuristics for arboreal representations need a quantitative engine, and this conjecture supplies one in two tiers. The first is a square-root Frobenius large sieve over parameters and primes, with a sheaf-theoretic conductor budget, a cap on the total ramification complexity the sieve must control, extending the large-sieve philosophy of Kowalski to growing preimage quotients and controlling parameter and prime dependence together. The second tier controls the higher connected Frobenius cumulants, and it is from this connected tier, not from the second-moment inequality alone, that the nonuniform multinomial occupancy of the boundary is derived. Separating the two is what makes the occupancy conclusion legitimate, since a second moment cannot by itself close a multinomial law. A counterexample would exhibit systematic cross-prime or cross-parameter entanglement invisible in the generic arboreal group, which is precisely the structure the connected tier is designed to exclude.

### Conjecture 43: Coloured dynatomic Galois-factor process

The exact-period polynomials of a unicritical map factor over the integers, and this conjecture treats those factors as genuine colours and asks how the prime factorization of their values behaves. For a fixed period, after conditioning on a finite local state and normalizing each component by its own logarithmic mass, the coloured factor processes converge to independent Poisson–Dirichlet processes, each marked by the fixed-point-size-biased Frobenius class in the splitting field of its component. The colours are geometric, arising from exact-period structure, and their Galois marks distinguish families that have indistinguishable unmarked factor sizes. The statement deliberately separates the full fixed-degree process from the restricted-support law it is willing to assert as the degree grows, in accordance with the distribution thresholds of Bharadwaj and Rodgers. It is the marked, coloured refinement of the factor process, and it feeds the primitive valuation input that Conjecture 44 requires.

### Conjecture 44: Complexity-uniform primitive valuation process

Squarefreeness of dynatomic values cannot be governed by a fixed local density, because for a fixed prime the first primitive hit occurs by a bounded time, so the density must depend on the level. This conjecture states the whole primitive valuation process instead of a single squarefree probability. After removing the canonical common factor with the earlier critical orbit, the primitive valuation vector converges, uniformly under an explicit height, discriminant and resultant complexity regime, to an adelic product of exact local laws, in a topology that includes the squarefull-mass functional. The squarefree probability and the compound law of the squarefull part then both descend from those local measures, with every bad prime and collision state retained rather than hidden in an exceptional set. The uniform squarefull tails are what supply the integrability an infinite adelic product needs, and the multiplicity data feed the coloured factor law of Conjecture 43.

### Conjecture 45: Divisor-sensitive dynamical gcd classification

Recent work has resolved several set-theoretic questions about common factors of orbits, and this conjecture proposes the height-theoretic boundary that decides when the greatest common divisor is genuinely large. The normalized gcd height of the iterates of a split map has positive limit superior exactly when the point eventually enters a periodic curve on which the pullbacks of the two coordinate-zero divisors share a nonzero effective component. A periodic correspondence alone is not enough, since it must actually carry the divisors that the gcd height measures, and allowing eventual rather than immediate entry is what closes the preperiodic tail. The converse direction is stated unconditionally where the relevant Vojta inequality is known and marked conditional otherwise, which keeps the Diophantine input visible. It places dynamical unlikely intersections, blow-up heights and invariant-curve geometry inside one obstruction, in the tradition of the dynamical gcd work of Yang and Zhong.

### Conjecture 46: Frobenius-marked Poisson–Dirichlet process

The large prime factors of a random integer follow the Poisson–Dirichlet law, and this conjecture marks that law with Galois data for values of an irreducible polynomial. Each macroscopic factor is marked by its Frobenius class, and the mark law is the class probability weighted by the number of fixed roots, which is the size-bias that divisibility by a polynomial value imposes, normalized to one by Burnside's lemma. Conditional on the masses and a finite local state the marks are asymptotically independent, and under a normal quotient the marked process pushes forward functorially. Bharadwaj and Rodgers supply the unmarked factor process, and the simultaneous Galois marking with its conditional independence and functorial pushforward is the content added here. It connects Galois theory to probabilistic factorization directly, and it supplies the marks for the three-scale and Buchstab laws of Conjectures 47 and 50.

### Conjecture 47: Three-scale factorization of polynomial values

Small and large prime factors of a polynomial value are not independent, because the small factors consume logarithmic mass, and this conjecture identifies the complete conservation-corrected structure once that mass is accounted for. The small valuations follow their Kubilius law, and conditional on the mass they consume the residual factor process is a scale-invariant Poisson process of intensity $$du/u$$ marked by Conjecture 46 and conditioned to total mass one. The small field and the unconditioned residual are then asymptotically independent, with the single residual-mass constraint carrying all the leading dependence. The mesoscopic and macroscopic laws are two projections of the one residual process, the scale-invariant factor process and the Frobenius-marked partition respectively, so no additional cross-scale coupling survives. The added mesoscopic scale is what a two-scale statement misses, and the whole object would justify the local sieve model, the scale-invariant process and the macroscopic partition in one limit theorem.

### Conjecture 48: Adelic Gibbs gluing for reducible values

A scalar Euler factor can correct a single avoidance probability but cannot specify a point process, and this conjecture gives the full local-to-global rule for the factor processes of a reducible polynomial value. After conditioning on the finite local state and normalizing each component by its residual mass, the coloured Frobenius-marked processes are conditionally independent copies of the three-scale law of Conjecture 47. Unconditionally they form a projective Gibbs mixture, a statistical-mechanics weighting of the conditional laws taken as a projective limit, obtained by integrating those conditional laws against the archimedean size profile and the adelic product of the exact local valuation laws, in a declared order of limits. Every bounded Laplace functional is then determined by the local partition functions, the per-prime normalizing sums of that weighting, together with the archimedean sizes, and no further colour coupling survives the mixture. The archimedean variable is included precisely because it can couple component sizes, and a persistent medium-prime or archimedean correlation after the stated mixture would identify a new nonadelic invariant.

### Conjecture 49: Full multivariate adelic saddle law

Joint smoothness of several polynomial values is an adelic problem, and this conjecture asserts that its governing object is a complete joint saddle rather than a scalar Euler correction. Each local factor is normalized by its own smooth mass, so that in one variable the construction reduces exactly to the Hildebrand and Tenenbaum saddle for the density of smooth numbers, which is the calibration that fixes the normalization. The joint smoothness probability is then a multivariate inverse Mellin integral with the Perron amplitudes appropriate to a cumulative event, and its leading approximation contains the joint action, the saddle displacement, the Hessian determinant and any lattice correction, all of which are indispensable. The ratio of the joint density to the product of marginals is therefore not a single Euler factor but the full entanglement of actions and curvatures. Even the one-variable theory is difficult, in the work of Martin and of Mine, so a complete multivariate saddle law would be a substantial local-to-global bridge.

### Conjecture 50: Buchstab–Bateman–Horn component flow

Primes, semiprimes and higher almost-primes among polynomial values are usually treated by separate heuristics, and this conjecture resolves a rough value into all of them at once through one universal flow. It defines Buchstab component functions whose sum is the Buchstab function, and asserts that the probability of a value being rough with exactly a given number of large factors is the sieve density times the expectation of the corresponding component, with the remaining factors carrying independent Frobenius marks from Conjecture 46. Summing the components recovers the rough-value law, the first component gives the Bateman and Horn prime density, and the second gives the semiprime transition, so the polynomial enters only through the sieve density while the factor-count flow is universal. The pointwise endpoint, where every rough value has a single large factor, is exact. It is strongly falsifiable, because even if total roughness follows Buchstab the distribution among the components can fail, and it is the sieve-to-prime bridge that Moree's generalized Buchstab equation anticipates.
