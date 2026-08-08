---
title: Ninety-six conjectures in mathematics
---

<p style="color:#999;font-size:0.8em;margin:0 0 1em 0;">Trial Project by Bryan Cheong</p>

# Ninety-six conjectures in mathematics

*July 27, 2026*

## Summary of the conjectures

**Part I — conjectures from the local–global random model, in importance–novelty order.**

**1. Prime-power contamination calculus (Conjecture 1).** For a balanced pair race $$(n,n+d)$$ mod $$m$$, the surviving prime-square orientations $$(q^2-d,q^2)$$, $$(q^2,q^2+d)$$ occupy provably computable residue classes, and the operator $$\mathcal C_{d,m}(a;x)=\sum_{o}\sum_{q}\Lambda(q^2)\Lambda(\text{prime member})$$ determines the drift vector: for twins, $$\mathcal{M}_x\bigl(D_1(t)\log^2t/\sqrt t\bigr)\to c_T=\tfrac12C(x,x^2-2)$$ (mod $$5$$) and $$\to2c_T$$ on class $$7$$ (mod $$8$$), symmetric differences $$\to0$$; in general each class deficit satisfies $$\mathcal{M}_x(\mathrm{deficit}\cdot\log^2t/\sqrt t)\to\lim\mathcal C_{d,m}(a;x)/\sqrt x$$. Convergence of these logarithmic means at drift scale is part of the conjecture (Rubinstein–Sarnak-type structure for pattern races).

**2. Pinned singular-series variance (Conjecture 2).** With $$R(h)=C_4(0,2,h,h+2)/\mathfrak{S}(2)^2$$ and $$G(H)=\sum_{h\le H}(1-h/H)(R(h)-1)$$: (i) [conditional proposition] the moving-window twin-pair count obeys $$\operatorname{Var}/\mathbb E=1+\mathfrak{S}(2)(2G(H)-1)/\log^2x +o(\log^{-2}x)$$; (ii) $$-G(H)/\log H\to\infty$$: pair counts are more sub-Poisson than prime counts.

**3. Least-prime ordering deficit (Conjecture 3).** With $$U(a,q)=\mathrm{Li}(p(a,q))/\varphi(q)$$: (i) $$U\Rightarrow\mathrm{Exp}(1)$$ marginally (attributed), Gumbel maximum under joint independence; (ii) the dyadic averages of $$\Theta(q)=(1-\mathbb E_a[U])\log q$$ over prime $$q\in[Q,2Q]$$ converge to a limit $$\Theta>0$$: the ordered primes fill residue classes faster than any exchangeable model, in excess of the derived discreteness and injectivity baselines.

**4. Goldbach lane race (Conjecture 4).** For $$n\equiv2\pmod4$$, prime squares enter ordered Goldbach representations only through the $$(1,1)$$ lane mod $$4$$, so with $$D=R_3-R_1$$ and the explicit weighted census $$D_{\mathrm{sys}}$$: $$\mathbb E_x[D-D_{\mathrm{sys}}]=o(\mathbb E_x[D_{\mathrm{sys}}])$$ under logarithmic sampling; the drift vanishes on the internal null subprogression $$n\equiv10\pmod{12}$$; the sign density of $$D$$ tends to $$\tfrac12$$.

**5. Least Goldbach summand (Conjecture 5).** With $$s(n)$$ the least prime $$p\nmid n$$ with $$n-p$$ prime, $$U(n)=\mathfrak{S}(n)\sum_{p\le s(n),\,p\nmid n}1/\log(n-p)$$, and the dyadic-log ensemble $$\mathbb E_X$$: (i) $$U\Rightarrow\mathrm{Exp}(1)$$; (ii) $$\Theta_G(X)=(1-\mathbb E_XU)\log X\to\Theta_G>0$$, the Goldbach sibling of the ordering deficit.

**6. Polynomial–exponential entanglement (Conjecture 6).** Primes $$n^2+2^n$$ force $$n\equiv3\pmod6$$; with $$\kappa_S=3\,D_S/\prod_{p\in S}(1-1/p)$$ built from the CRT-exact survivor density $$D_S$$ over the joint period of $$S$$ and the lane bonus $$3$$ at the primes $$2$$ and $$3$$: $$\kappa_{S_z}$$ converges along the canonical exhaustion $$S_z=\{5\le p\le z\}$$ to $$\kappa$$, the counting function is $$\sim\sum_{n\equiv3(6),\,n\le N}\kappa/\log(n^2+2^n)\asymp\log N$$; whether the limit factors exactly (as observed through $$p\le19$$) is an open question.

**7. Multibase Fermat quotients (Conjecture 7).** For $$p\nmid a$$: the Eisenstein–Lerch homomorphism confines multiplicatively dependent bases to a rational subtorus, and (iv) for multiplicatively independent bases $$(q_p(a_1),\dots,q_p(a_r))/p$$ equidistributes on the full torus as $$p$$ varies; (v) at most finitely many simultaneous Wieferich primes; plus single-base clauses: KS-discrepancy LIL at constant $$1/\sqrt2$$, shrinking-target law $$\#\{p\le x:q_p<K\}\sim\sum\min(1,K/p)$$, Wieferich-count LIL and an almost-sure CLT at the $$du/u$$ weighting.

**8. Uniform de Polignac covariance field (Conjecture 8).** $$\pi_d(x)=\mathfrak{S}(d)\mathrm{Li}_2(x)(1+o(1))$$ uniformly for even $$d\le(\log x)^A$$; the moving-window residual field has covariance $$K_3(d,d')H/\log^3x+(1/\log^4x)\sum_{\vert h\vert \le H}(H-\vert h\vert )K_4(d,d';h)$$, triple term dominant on the polylogarithmic window class, with Poisson/Gaussian regimes as finite-$$x$$ corrections to independence.

**9. Race sub-diffusivity (Conjecture 9).** Balanced-race steps at event index have negative autocorrelations obeying $$\rho_k(x)=-(c_k\log\log x+d_k)/\log x\,(1+o(1))$$; under uniformity in $$k$$, tail summability, and $$\sum c_k,\sum\vert d_k\vert <\infty$$, the diffusivity is $$\sigma^2(x)=1-2(\sum c_k\log\log x+\sum d_k)/\log x\,(1+o(1))$$, those hypotheses being model-layer, not asserted asymptotically; the asymptotic diffusive-vs-rigid dichotomy is registered open, with the rigid branch selected only at Conjecture 1(i-b) for its contaminated races.

**10. Uniform quadratic de Polignac and its constants (Conjecture 10).** $$\#\{n\le N:n^2+1,\,n^2+1+d \text{ prime}\}=C(d)I_d(N)(1+o(1))$$ uniformly for even $$d\le(\log N)^B$$; a separate power-saving rate clause; and the family law: moments of $$C(d)$$ converge to derived Euler products (mean $$2.7456\ldots$$, sd $$1.6840\ldots$$), the empirical law converging to the random product with CRT-independent local factors.

**11. First occurrences of prime gaps (Conjecture 11).** On realized gaps: $$\log p(g)/\sqrt g$$ bounded between positive constants; $$\liminf=\sqrt{\mathrm{e}^{\gamma}/2}$$ conditional on the realization hypothesis; and $$\log p(g)=\sqrt g+\tfrac12\log g-\tfrac12\log\mathfrak{S}^*(g)+E_g$$ with $$\Pr[E_g\le t]\to1-\exp(-\mathrm{e}^{2(t-\mu)})$$, the min-type Gumbel at scale $$\tfrac12$$ forced by the slope-$$2$$ hazard expansion.

**12. Stern lane race (Conjecture 12).** In $$n=p+2k^2$$, square contamination $$n=q^2+2k^2$$ sits in the $$k$$-even lane iff $$n\equiv1\pmod8$$, $$k$$-odd iff $$n\equiv3$$, and is impossible for $$n\equiv5,7$$ (provable null classes); on contaminated classes the clean-minus-contaminated difference obeys $$\mathbb E_X[D-D_{\mathrm{sys}}]=o(\mathbb E_X[D_{\mathrm{sys}}])$$ with the $$\Lambda(q^2)$$-weighted census $$D_{\mathrm{sys}}$$.

**13. Microscopic variance law (Conjecture 13).** [Conditional on quantitative Hardy–Littlewood] For windows of length $$H=\lambda(\log x)^{\alpha}$$, $$\operatorname{Var}X/\mathbb EX=1-(\log H+\gamma+\log2\pi-1)/\log x +o(1/\log x)$$ uniformly in $$1\le\alpha\le A$$, with Gallagher’s Poisson law at the boundary $$\alpha=1$$.

**14. Null-mechanism race (Conjecture 14).** For $$(n^2+1,n^2+3)$$, square contamination is algebraically impossible (single bounded exception $$(n,q)=(1,2)$$); the race mod $$5$$ is driftless at the contamination scale, $$\mathcal{M}_x(D(t)\log^2t/\sqrt t)\to0$$—the negative control for item 1—and the logarithmic occupation of leadership tends to $$\tfrac12$$ with Gaussian fluctuations $$\sqrt{\log2/\log x}$$, conjectured directly (the event-index invariance principle is a separately falsifiable local hypothesis, which does not imply it).

**15. Cubic-shift constants (Conjecture 15).** For non-cube $$a$$, the three-state local law gives $$\mathbb E_a[\omega(p)]=1$$ exactly, so the limit law of $$C(a)$$ has mean exactly $$1$$ (an $$L^2$$-martingale argument), derived sd $$0.2762\ldots$$; counts are uniform over non-cube $$a\le(\log N)^B$$.

**16. Conjecture F as a family (Conjecture 16).** $$Q_A(N)=C(A)I_A(N)(1+o(1))$$ uniformly over odd $$A\le(\log N)^B$$; same-index window covariance $$[C(A,A')-C(A)C(A')]H/4\log^2N$$ (negative for locally exclusive pairs), with the off-index pinned sum at the same $$1/4\log^2N$$ order left open.

**17. Twin-member Goldbach, orientation-resolved (Conjecture 17).** Under $$n$$-uniform Hardy–Littlewood for the four role systems, $$R_T(n)=[\sum_o\mathfrak{S}_4^{(o)}(n)]\int_5^{n-5}dt/(\log^2t\log^2(n-t)) \,(1+o(1))$$, with the exact identities $$\mathfrak{S}_4^{(\mathrm{lu})}=\mathfrak{S}_4^{(\mathrm{ul})}$$ and $$\mathfrak{S}_4^{(\mathrm{uu})}(n)=\mathfrak{S}_4^{(\mathrm{ll})}(n-4)$$.

**18. Triplet contamination (Conjecture 18).** For $$(n,n+2,n+6)$$ mod $$5$$, the unique surviving square configuration is the doubly-thinned $$(q^2-2,q^2,q^2+4)$$ (the other two configurations dying for every prime $$q>3$$), contaminating class $$2$$: $$\mathcal{M}_x\bigl((\pi_3(t;5,1)-\pi_3(t;5,2))\log^3t/\sqrt t\bigr)\to c_3$$, the Bateman–Horn constant of $$(q,q^2-2,q^2+4)$$.

**19. Sexy-pair contamination matrix (Conjecture 19).** For $$(n,n+6)$$ both orientations survive on complementary $$q$$-classes, feeding start classes $$3$$ and $$1$$ (mod $$5$$ and mod $$8$$) with independent constants $$c_A,c_B$$ (the $$(q,q^2\mp6)$$ Bateman–Horn constants) in the drift-scale sense; class $$2$$ (mod $$5$$) and classes $$5,7$$ (mod $$8$$) are provably clean.

**20. Fibonacci–Lucas twins (Conjecture 20).** The odd prime-divisor pools of $$F_p$$ and $$L_p$$ are disjoint (ranks $$p$$ vs $$2p$$; $$\gcd=2$$ iff $$3\mid p$$); only finitely many $$p$$ have both prime; the naive joint accounting assigns prior mass about $$1.4\times10^{-2}$$ to the index range beyond $$10^4$$, in which the catalogued index $$148091$$ falls, recorded descriptively and conditionally on the probable-prime status of both $$F_{148091}$$ and $$L_{148091}$$, and fatal to any completeness list.

**21. Factorial twins (Conjecture 21).** Window rigidity: $$n!+a$$ is composite for $$2\le\vert a\vert \le n$$ (theorem), so $$\pm1$$ are the only bounded offsets; $$n=3$$ uniqueness is attributed; the joint-fluctuation clause is a declared-model CLT for $$F_+-F_-$$ under explicit covariance and higher-cumulant hypotheses.

**22. Boundary trichotomy (Conjecture 22).** For $$\deg F\ge2$$ with positive leading coefficient, $$F(m)-F(j)$$ prime forces $$m-j=1$$ outside a bounded region; for $$x^3+cx$$ the boundary lane $$3m^2-3m+1+c$$ is dead-parity for odd $$c$$, dead-$$3$$-adic for even $$c\equiv2\pmod3$$, admissible exactly for $$c\equiv0,4\pmod6$$, with uniform Bateman–Horn counts over admissible $$c\le(\log M)^B$$.

**23. Power-obstruction ladder (Conjecture 23).** $$m^k=p+j^k$$ is impossible for composite $$k$$ (theorem); for prime $$k$$ it forces $$j=m-1$$ and reduces to primality of the irreducible $$D_k(m)=m^k-(m-1)^k$$, which follows Bateman–Horn uniformly over the prime-$$k$$ lanes.

**24. Alternating cyclotomic chain (Conjecture 24).** Infinitely many primes $$p$$ with $$\Phi_3(p)$$ and $$\Phi_6(\Phi_3(p))$$ prime, at the derived Bateman–Horn rate; alternation is the unique admissible continuation in the anchored construction space.

**25. Twin cyclotomic bases (Conjecture 25).** Of the $$\varphi(k)=2$$ family, only $$k=3$$ survives ($$k=4$$ parity-dead, $$k=6$$ a translate), and $$\Phi_3(n)$$, $$\Phi_3(n+1)$$ are simultaneously prime infinitely often with the computed Bateman–Horn constant.


**Part II — structural conjectures, in programme order.**


**26. Connected motif generating functional (Conjecture 26).** A full connected diagram calculus for all joint cumulants of prime motifs.

**27. Complete overlap-renormalization filtration (Conjecture 27).** A classification of every possible covariance scale and rigid eigenspace in a finite motif family.

**28. Regularized mesoscopic local–spectral trace formula (Conjecture 28).** Independently mollified Euler-product and multiple-zero functionals agree after named counterterms, and the limit is regularization independent.

**29. Anchored arithmetic polymer expansion (Conjecture 29).** Palm cluster activities are graded by the number of new prime constraints beyond one anchored motif.

**30. Topological expansion of non-Gaussianity (Conjecture 30).** The first non-Gaussian terms are graded by the homology of overlap-incidence complexes.

**31. Connected first-arrival functional (Conjecture 31).** The entire least-prime point process has connected kernels obtained from same-class prime correlations.

**32. Tested Gauss-polyspectral reciprocity (Conjecture 32).** Scalar tensor observables have exact Gauss-transport identities under the random-modulus law and dual arithmetic limits.

**33. Rubinstein–Sarnak terminal chaos dichotomy (Conjecture 33).** Terminal extremes are directed by the limiting low-zero chaos measure, with an explicit self-averaging versus Cox criterion.

**34. Nonlinear spectral response calculus (Conjecture 34).** Low-zero and exceptional-zero perturbations pass through first-arrival statistics by universal Volterra response operators.

**35. Local-information capacity of odd class groups (Conjecture 35).** Cohen–Lenstra independence has a sharp two-resource boundary governed by cell entropy and conductor complexity.

**36. Kummer–Haar law on relation tori (Conjecture 36).** Saturated multiplicative relations give the exact horizontal support and Haar law of Fermat-quotient vectors.

**37. Rank-dimensional finite-logarithm large sieve (Conjecture 37).** A positive power range of frequencies obeys a large sieve whose dual dimension is saturated rank.

**38. Mesoscopic-to-lattice shrinking-target transition (Conjecture 38).** Haar universality persists for growing targets, while bounded lattice targets acquire a separate arithmetic regulator intensity.

**39. Global-lattice $$p$$-adic regulator-matrix law (Conjecture 39).** A fixed integral Galois-relation lattice controls horizontal regulator matrices and their determinantal rare events.

**40. Functorial horizontal logarithms on tori (Conjecture 40).** A finitely generated global subgroup of a torus has a functorial matrix-valued finite-logarithm Haar law.

**41. Entropy–conductor profile of arboreal resolution (Conjecture 41).** Exact class-measure entropy and Artin-conductor profiles determine observable depth and finite-index shifts.

**42. Arboreal family large sieve and cumulant independence (Conjecture 42).** Growing preimage quotients satisfy square-root trace bounds and higher connected Frobenius factorization over parameters.

**43. Coloured dynatomic Galois-factor process (Conjecture 43).** Exact-period components generate independent coloured, Frobenius-marked factor processes, with growing-degree support restrictions.

**44. Complexity-uniform primitive valuation process (Conjecture 44).** The complete primitive valuation vector has an adelic product law under an explicit height–discriminant complexity regime and uniform squarefull tails.

**45. Divisor-sensitive dynamical gcd classification (Conjecture 45).** Positive normalized gcd height is exactly eventual entry into a periodic curve carrying a shared effective component of the two coordinate divisors.

**46. Frobenius-marked Poisson–Dirichlet process (Conjecture 46).** Macroscopic polynomial-value factors carry fixed-point-size-biased Galois marks.

**47. Three-scale polynomial factorization (Conjecture 47).** Small valuations, mesoscopic scale-invariant factors, and macroscopic marked factors form one conservation-corrected product structure.

**48. Adelic Gibbs gluing for reducible values (Conjecture 48).** Reducible polynomial factor processes are an archimedean–$$p$$-adic Gibbs mixture of independent component processes.

**49. Full multivariate adelic saddle law (Conjecture 49).** Joint smoothness is governed by a complete joint Perron action, saddle displacement, and Hessian, not a scalar Euler correction.

**50. Buchstab–Bateman–Horn component flow (Conjecture 50).** Rough prime, semiprime, and higher-almost-prime polynomial values follow universal Buchstab components with Galois marks.



**Part III — six conjectures across fields, in statement order.**

**51. Relative polynomial pretentiousness inverse principle (Conjecture 51).** A persistently nonzero logarithmic correlation of completely multiplicative unimodular functions along multiplicatively independent irreducible polynomials forces one existential block of primitive characters and archimedean parameters with finite relative pretentious distances, the balance identity $$\sum_j t_j \deg P_j = 0$$, and a nonvanishing joint character average at a common modulus.

**52. Monotone threshold purification of vector paths (Conjecture 52).** Every monotone fractional activation schedule of $$m$$ vectors of norm at most one in $$\mathbb R^d$$ admits a rounding to single irreversible activation times whose path error is $$O(\sqrt d)$$ uniformly in $$m$$, containing the open Euclidean Steinitz prefix-sum problem and asserting removal of the logarithm from Banaszczyk's $$O(\sqrt{d+\log m})$$.

**53. Entropy dimension of random-free graphons (Conjecture 53).** If the row space of a $$\{0,1\}$$-valued graphon is Ahlfors $$s$$-regular then $$H(G(n,W))=s\,n\log n+O_W(n)$$, the limit law itself being provable from regularity, and the hypothesis class nonvacuous at every $$s\in(0,2]$$ by Cantor-type threshold constructions.

**54. A Hessian principle for isolated microcanonical graph phases (Conjecture 54).** Under isolated-phase, transversally Lipschitz, and nonemptiness hypotheses, the tangent block averages of a microcanonical coloured graph ensemble fluctuate at scale $$n^{-1}$$ around their mean with centred Gaussian limit of covariance $$A^{-1}$$, the inverse of the contracted entropy Hessian.

**55. Sharp stability of entropy idempotence on finite abelian groups (Conjecture 55).** The squared total variation distance from a probability measure to the nearest uniform coset measure is bounded by a universal constant, conjecturally exactly $$2/\log 2$$ as pinned by discretized Gaussians on $$\mathbb Z/p\mathbb Z$$, times the convolution entropy defect $$H(\mu*\mu)-H(\mu)$$.

**56. Stationary convolution-entropy rigidity (Conjecture 56).** An ergodic stationary process over a finite abelian group preserves entropy under independent self-convolution exactly when its quotient by the translational stabilizer has zero entropy, so in particular every ergodic binary process of intermediate entropy gains entropy under independent XOR.


**Part IV — twenty conjectures on the class-counting polynomial, in statement order.**

**57. Irreducibility and connectivity (Conjecture 57).** The shifted class-counting polynomial $$H_G(U,Y)=C_G(1+U,Y)$$ is irreducible in $$\mathbb Z[U,Y]$$ exactly when $$G$$ is connected. The disconnected direction is immediate from Rossmann's multiplicativity, each factor being nonconstant since $$H_{K_1}=1+U$$, and the connected direction was verified by exact factorization over $$\mathbb Z$$ for all $$996$$ connected graphs on at most seven vertices.

**58. Recovery of the subgraph-component polynomial (Conjecture 58).** Equality of class-counting polynomials forces equality of the subgraph-component polynomials of Tittmann–Averbouch–Makowsky. The polynomial $$C_G$$ records the joint distribution of $$(\vert S\vert ,\vert N[S]\vert -c(G[S]))$$ and $$Q_G$$ that of $$(\vert S\vert ,c(G[S]))$$, and no functional relation between the two arrays is apparent, yet every known $$C$$-collision class has agreeing $$Q$$.

**59. Two-field rigidity (Conjecture 59).** If two graphs have equal $$C_G(2,Y)$$ and equal $$C_G(3,Y)$$ then their class-counting polynomials coincide. Equivalently, the adjoint-rank distributions of the graphical Lie algebras over $$\mathbb F_2$$ and $$\mathbb F_3$$ determine them over every finite field.

**60. Hybrid rigidity (Conjecture 60).** The $$\mathbb F_2$$ rank distribution $$C_G(2,Y)$$ together with the subgraph-component polynomial $$Q_G$$ determines $$C_G$$. The pairing is sharp in one direction, since $$C_G(2,Y)$$ together with the degree sequence does not determine $$C_G$$.

**61. Binary edge-deck reconstruction (Conjecture 61).** For graphs with at least four edges, the multiset of binary specializations $$\{C_{G-e}(2,Y):e\in E(G)\}$$ determines the graph up to isomorphism. This is the high-risk member of the part, in the orbit of the edge reconstruction conjecture, with each card compressed from an isomorphism type to a single rank polynomial.

**62. Bipartite binary rigidity (Conjecture 62).** Within bipartite graphs the single specialization $$C_G(2,Y)$$ determines the whole polynomial $$C_G$$. The statement was tested on a six-thousand-graph random holdout spanning $$2747$$ distinct binary specializations.

**63. Connected-pseudoforest binary rigidity (Conjecture 63, resolved false).** The proposed one-field rigidity for trees and connected unicyclic graphs is refuted by an explicit seven-vertex unicyclic pair sharing the binary specialization with distinct degree multisets, the unique violating class through nine vertices. The tree case survives exhaustively through fourteen vertices.

**64. Chordal binary rigidity (Conjecture 64).** The same one-field rigidity holds within chordal graphs, tested on a six-thousand-graph random holdout spanning $$5598$$ distinct binary specializations.

**65. Recovery of the domination number (Conjecture 65).** Equality of class-counting polynomials forces equality of domination numbers $$\gamma$$. The statement sits strictly between a theorem and a false analogue, since connected domination is readable from the coefficients by Rossmann while total domination is not determined by $$C_G$$.

**66. Recovery of the independent domination number (Conjecture 66).** Equality of class-counting polynomials forces equality of independent domination numbers $$i$$. Every known collision class of $$C$$ has agreeing $$i$$.

**67. Global double log-concavity (Conjecture 67).** For every graph the coefficient sequence $$a$$ of $$f_G(1+Z)$$ is log-concave, and so is its transform $$L(a)_i=a_i^2-a_{i-1}a_{i+1}$$. The calibration is exact, since the third iterate of $$L$$ fails for a thirteen-vertex graph.

**68. Strict log-concavity for connected graphs (Conjecture 68).** For connected graphs with at least one edge, $$a_i^2>a_{i-1}a_{i+1}$$ at every interior position of the support, so equality cases live only on the disconnected stratum.

**69. Strict second-order log-concavity (Conjecture 69).** Under the same hypotheses the transform $$L(a)$$ is strictly log-concave at every interior position of its support, one level below the thirteen-vertex counterexample to the third iterate.

**70. Rank-slice strict log-concavity (Conjecture 70).** For connected graphs and every attainable rank $$r$$, the slice $$A_{G,r}(Z)=[Y^r]F_G(1+Z,Y)$$, when not a monomial, is strictly log-concave at every interior position of its support. The second-order strengthening of the slice statement fails for an eight-vertex graph.

**71. Interval support at fixed rank (Conjecture 71, resolved false).** The proposed gaplessness of $$K_r(G)=\{\vert S\vert :\rho_G(S)=r\}$$ is refuted by a connected eight-vertex graph whose sizes attaining rank five skip size two, the unique violating order. The transposed statement was already false, so neither direction of the array has interval structure.

**72. Coefficientwise tree extremality (Conjecture 72).** For every tree $$T$$ on $$n$$ vertices, $$f_{P_n}(1+Z)\le f_T(1+Z)\le f_{K_{1,n-1}}(1+Z)$$ coefficientwise, with equality only for the path and the star respectively. The verification is exhaustive over all trees through fourteen vertices.

**73. Star rank-majorization (Conjecture 73).** For every $$n\ge5$$ and every prime power $$q$$, the decreasingly ordered adjoint-rank distribution of the star majorizes that of every $$n$$-vertex tree over $$\mathbb F_q$$. The hypothesis is sharp, since at $$n=4$$ and $$q=2$$ the star fails to majorize the path, and the dual assertion that the path is majorization-minimal is false.

**74. Tree rank-variance extremality (Conjecture 74).** For every $$n\ge4$$ and every prime power $$q$$, among $$n$$-vertex trees the variance of $$\operatorname{rank}(\operatorname{ad}_x)$$ over uniformly random $$x\in L_T(\mathbb F_q)$$ is uniquely minimized by the path and uniquely maximized by the star.

**75. Leaf-count rigidity (Conjecture 75).** Equality holds in the lemma's bound $$s(T)\ge n-\ell(T)+2$$ exactly when $$T$$ is a path or a star.

**76. Diameter rigidity (Conjecture 76).** Equality holds in the lemma's bound $$s(T)\ge\operatorname{diam}(T)+1$$ exactly when $$T$$ is a path or a star.

**Part V — twenty conjectures on pattern Lie algebras of posets, in statement order.**

**77. Adjoint–Kirillov determination (Conjecture 77).** Equality of the adjoint enumerators $$A_{P,q}$$ forces equality of the Kirillov enumerators $$K_{P,q}$$. The two enumerators are the two contractions of the same bracket, and the implication was verified across $$64$$ adjoint-collision classes.

**78. Lower-central recovery (Conjecture 78).** The adjoint enumerator determines the vector of lower-central factor dimensions $$(\dim\gamma_i(L_P)/\gamma_{i+1}(L_P))_i$$. This vector was constant on every adjoint-collision class in testing.

**79. Ordinary Poincaré recovery (Conjecture 79).** The adjoint enumerator is conjectured to determine the ordinary cohomological Poincaré polynomial $$\sum_i\dim H^i(L_P,\mathbb F_q)U^i$$. It is tested only for $$\dim H^2$$ and $$\dim H^3$$, resting on the deposited cohomology data rather than an independent recomputation.

**80. Derivation recovery (Conjecture 80).** The adjoint enumerator determines $$\dim\operatorname{Der}(L_P)$$, the dimension of the derivation algebra, which was constant on every adjoint-collision class.

**81. Adjoint Poincaré recovery (Conjecture 81).** The adjoint enumerator is conjectured to determine every adjoint-cohomology dimension $$\dim H^i(L_P,L_P)$$. It is tested only for $$\dim H^1$$, $$\dim H^2$$, and $$\dim H^3$$ from the deposited data.

**82. Centroid-dimension recovery (Conjecture 82).** The adjoint enumerator determines $$\dim\operatorname{Cent}(L_P)$$, the dimension of the centroid, which was constant on every adjoint-collision class.

**83. Adjoint spectrum characteristic independence (Conjecture 83).** The set of attained adjoint ranks $$\{\operatorname{rank}(\operatorname{ad}_x)\}$$ is independent of $$q$$. The attained-rank sets agreed across $$\mathbb F_2$$, $$\mathbb F_3$$, and $$\mathbb F_5$$ in every case.

**84. Kirillov spectrum characteristic independence (Conjecture 84).** The set of attained Kirillov ranks $$\{\operatorname{rank}(B_f)\}$$ is independent of $$q$$, agreeing across $$\mathbb F_2$$, $$\mathbb F_3$$, and $$\mathbb F_5$$ in every case.

**85. Two-field arithmetic rigidity (Conjecture 85).** Equality of adjoint enumerators over $$\mathbb F_2$$ and $$\mathbb F_3$$ is conjectured to force equality over every finite field. Its only tested holdout beyond $$q=2,3$$ is $$q=5$$, on $$16$$ three-field collision classes.

**86. Adjoint stochastic field monotonicity (Conjecture 86).** For $$q<q'$$ the distribution of $$\operatorname{rank}(\operatorname{ad}_x)$$ over $$\mathbb F_{q'}$$ first-order stochastically dominates its distribution over $$\mathbb F_q$$. Dominance held in all $$221$$ field-pair tests, while the monotone-likelihood-ratio strengthening is false.

**87. Kirillov likelihood-ratio field monotonicity (Conjecture 87, resolved false).** The proposed monotone likelihood-ratio domination of the normalized even-rank distributions is refuted by a seven-point poset whose likelihood ratio from $$\mathbb F_2$$ to $$\mathbb F_3$$ already decreases across the even ranks, while the first-order dominance of Conjecture 86 stands.

**88. Centre-one reverse determination (Conjecture 88).** When $$\dim Z(L_P)=1$$ the Kirillov enumerator determines the adjoint enumerator. This was verified on all $$43$$ centre-one records.

**89. Centre-one Laplace positivity (Conjecture 89).** When $$\dim Z(L_P)=1$$ the incidence quotient $$R_{P,q}(T)=(K_{P,q}-A_{P,q})/((1-T)(1-qT))$$ has nonnegative integer coefficients, on all $$43$$ centre-one records.

**90. Centre-one quotient shape (Conjecture 90, resolved false).** The proposed unimodality of $$R_{P,q}$$ under a line centre is refuted by a seven-point poset whose quotient has a strict interior valley, while the positivity and interval support of Conjecture 89 stand.

**91. Hasse-forest reverse determination (Conjecture 91).** When the Hasse cover graph of $$P$$ is a forest the Kirillov enumerator determines the adjoint enumerator, across $$44$$ forest-collision classes.

**92. Hasse-forest coadjoint saturation (Conjecture 92).** On a Hasse forest the support of $$K_{P,q}$$ is the full even range $$\{0,2,4,\ldots,b_K\}$$ up to the maximal Kirillov rank, filled in every case.

**93. Hasse-forest Kirillov unimodality (Conjecture 93).** On a Hasse forest the even-rank sequence $$([T^{2j}]K_{P,q})_j$$ is unimodal. Strict log-concavity is false, so unimodality is the calibrated boundary.

**94. Hasse-forest breadth–orbit bound (Conjecture 94).** On a Hasse forest the maximal Kirillov rank and adjoint breadth satisfy $$b_K(P,q)\le 2\,b_A(P,q)$$. The unrestricted bound failed fourteen times off the forest class.

**95. Unitriangular Kirillov strict log-concavity (Conjecture 95).** For $$L=\mathrm{ut}_n(\mathbb F_q)$$ the even-rank sequence $$([T^{2j}]K_{L,q})_j$$ is strictly log-concave at every nontrivial interior index, confirmed through $$\mathrm{ut}_6$$ over $$\mathbb F_2$$.

**96. Adjoint–coadjoint incidence anticorrelation (Conjecture 96).** Sampling $$(x,f)$$ uniformly on the incidence variety gives $$\operatorname{Cov}(\operatorname{rank}(\operatorname{ad}_x),\operatorname{rank}(B_f))<0$$ for every nonabelian $$L_P$$, with covariance zero exactly in the abelian case.

## Abstract

We state ninety-six conjectures in five parts. The twenty-five conjectures of Part I are each derived from the local–global random model of the primes: Cramér’s model corrected by Hardy–Littlewood singular series, with Bateman–Horn as the organizing framework and Borel–Cantelli accounting for sparse events. Each statement is calibrated to the strongest form the heuristic supports. Every computable constant is computed from its definition, with local admissibility checked for every constant computed; every statement was tested against exact counts (probable-prime counts, so labelled, where the integers involved exceed the deterministic certification range), with success measured by the *shape* of agreement (predicted constant, square-root residuals, no drift) rather than by the size of the range searched. The contributions include: a prime-power contamination calculus for pattern races—twin races modulo $$5$$ and $$8$$ driven by the pairs $$(q^2-2,q^2)$$, cousin, sexy-pair, and triplet predictions derived from the calculus before testing, a Goldbach lane race with a verified internal null lane, a Stern-representation lane race whose null classes are provable by direct congruence, and an algebraic null control; the measured sub-diffusivity of balanced races (universal negative step correlations tied to the Lemke Oliver–Soundararajan repulsion); canonical ordering deficits for least primes in progressions and for least Goldbach summands; derived covariance kernels for moving-window residual fields, with the diagonal deficit reduced to a pinned singular-series average whose growth already exceeds the single-prime Montgomery–Soundararajan term; distribution laws for the constants of the quadratic-pair and cubic-shift families, with exact mean-value lemmas; an entanglement-aware local-global law for $$n^2+2^n$$ with an exact-rational CRT factorization; a boundary trichotomy for polynomial ladders; a multibase subtorus law for Fermat quotients; and singular-series waiting-time refinements for first prime gaps. Every statement was checked against the literature by an independent search, with novelty labelled conservatively: statements already known in essence are attributed and kept *inside* the conjecture whose content they calibrate, since those benchmarks are what make the derived constants credible. Every falsifiable-by-instance statement was then stress-tested computationally well beyond its original range, and every constant was recomputed independently from its definition. Part II adds twenty-five structural conjectures in five programmes—connected prime-pattern fields, arithmetic first-arrival fields and class groups, finite logarithms and algebraic tori, arboreal arithmetic dynamics, and adelic factorization processes—each introducing a canonical operator, process, invariant, classification, or phase boundary, with its mechanism, nearest literature boundary, first decisive theorem, and failure mode. Part III adds six conjectures across fields: a relative pretentious inverse principle for polynomial arguments, a threshold purification law for monotone vector paths, an entropy–dimension law for random-free graphons, a Hessian principle for microcanonical graph phases, a sharp stability law for entropy idempotence on finite abelian groups, and a convolution-entropy rigidity for stationary processes. Part IV (Conjectures 57–76) adds twenty conjectures on a single further object, Rossmann's class-counting polynomial of graphical Lie algebras: rigidity and reconstruction laws for the polynomial and its binary specialization, recovery of the subgraph-component polynomial and of domination invariants, a strict log-concavity ladder with proven failure boundaries, and extremal laws for trees, each tested exhaustively at small order, on adversarial random holdouts, and at every known collision class of the polynomial. Two of the twenty, the pseudoforest one-field rigidity claim and the interval-support claim, have since been refuted, by an explicit seven-vertex pair and a connected eight-vertex graph, and are recorded as resolved false with their counterexamples. Part V (Conjectures 77–96) adds a second algebraic family, the nilpotent pattern Lie algebras of finite posets, and studies two rank-weight enumerators of the bracket tensor, the adjoint and the Kirillov enumerators: determination of structural and coadjoint invariants by the adjoint enumerator, characteristic and field-monotonicity behaviour, a positive unimodal centre-one incidence quotient, and reverse determination, saturation, and a breadth bound for Hasse-forest posets, fifteen of them supported throughout the tested corpus, three stated in greater generality than the computations reach, and two since refuted by explicit seven-point posets and recorded as resolved false, all reverified on an independently generated poset corpus over a proved calibration identity.

## Introduction

This collection states ninety-six conjectures in five parts. Part I (Conjectures 1–25) is a single sustained experiment: the primes, beyond their local structure, are modelled as a random set of density $$1/\log n$$, and the model is pushed to its sharpest consequences. Part II (Conjectures 26–50) leaves the single model for five structural programmes—connected prime-pattern fields, arithmetic first-arrival fields and class groups, finite logarithms and algebraic tori, arboreal dynamics, and adelic factorization—each contributing one canonical object and its laws. Part III (Conjectures 51–56) leaves number theory itself, carrying the same discipline into multiplicative number theory's pretentious frontier, discrepancy theory, graph limits, additive information theory, and ergodic theory. Part IV (Conjectures 57–76) turns to a single object on the algebraic side, the class-counting polynomial of graphical Lie algebras, and states for it a rigidity and reconstruction programme, a log-concavity programme, and a tree extremal programme, with the proved layer, an exact rank formula and two lower bounds for trees, separated from the twenty conjectural laws. Part V (Conjectures 77–96) turns to a second algebraic family, the nilpotent pattern Lie algebras of finite posets, whose adjoint and Kirillov rank enumerators carry a determination programme, a characteristic-and-field programme, a centre-one positivity programme, and a Hasse-forest programme over a proved calibration identity, three of the twenty being stated in greater generality than the computations reach and flagged as such, and two since resolved false with explicit counterexamples.

One standard governs all five parts. A good conjecture is not merely a statement that has resisted counterexample: it is a determinate proposition about a canonical object, with a stated mechanism, and with enough exposed structure to be refuted in pieces. Concretely, every statement here is asked to (i) survive every congruence and size obstruction; (ii) come with a quantitative form whose constants are derived, not fitted; (iii) demand exactly the fluctuations its mechanism earns and no fewer (the Mertens conjecture died of demanding fewer); (iv) sit inside a known hierarchy where one exists (for Part I, Hardy–Littlewood $$k$$-tuples $$\subset$$ Schinzel's Hypothesis H $$\subset$$ Bateman–Horn), so that failure would propagate; and (v) expose instance-falsifiable content—congruences, null lanes, exact identities, derived constants—so that computation can refute the derivation even where the asymptotic itself lies beyond finite refutation. Numerical range is the least important column in the ledger: most deep phenomena drift at the rate $$\log\log x$$, and $$\log\log 10^{18}\approx 3.7$$, so verification “to $$10^{18}$$” is weak evidence by itself. What persuades is the *shape* of the agreement—a count that tracks a derived constant through several decades with residuals that look like noise.

Part I is presented in three sections: the principal conjectures (numbers 1–9), family laws and second-order refinements (numbers 10–17), and instances and structural companions (numbers 18–25). The material they draw on—Bateman–Horn systems, barely-divergent sparse sequences, representation problems with Borel–Cantelli accounting, and statistical laws of the prime sequence—runs through all three. The stress-tests section reports the independent recomputation of every constant.

One structural lesson organizes several of the statements below. A probability model integrates over density, and is therefore blind to algebraic families of density zero; the admissibility clause, checked at every prime for every system, is what repairs that blindness. The cubes inside the representation problem $$n=p+k^3$$ (Theorem 1) are the sharpest instance: they obstruct the problem outright while contributing nothing to any Borel–Cantelli sum taken over all $$n$$. This is the classical lesson of admissibility, and it is why the statements below separate what is provable by congruence or factorization from what a probabilistic accounting supplies. Parts II to V inherit the same separation in a different key: each statement names its canonical object and averaging law, identifies its source, states a first decisive theorem where one exists, and records an honest failure mode.

Three checks stand behind every statement, and the stress-tests section reports their outcomes for Part I. First, an independent literature search at neighbourhood depth—defining objects, derived sequences, OEIS comments where relevant, and the abstracts and bodies of near-neighbour papers, read rather than skimmed from search summaries—establishes what is already known. Where a statement exists in essence it is attributed and labelled: some verbatim (Dubner's twin-sum conjecture, the Stern list for $$p+2k^2$$, Caldwell–Gallot's $$\mathrm{e}^{\gamma}\log N$$ laws), one with an exact constant catalogued as an OEIS entry (A188596), and the rest attributed accordingly. No such statement occupies a conjecture on its own; each is retained *inside* the conjecture whose claimed content it calibrates, restated in our uniform framework and re-verified at our bounds, and where a statement strengthens a named open problem the containment is stated as its headline. Second, every falsifiable-by-instance statement was verified against exact counts and then re-tested well past its original bound, the computation being designed as an attempt at refutation rather than at confirmation. Third, constants and counts were recomputed from the definitions alone by independent implementations sharing no code with the primary computation. Our novelty policy throughout is conservative: where priority is uncertain we attribute rather than claim.

### Taxonomy: our contribution and its calibration layer

Within Part I, one criterion governs the taxonomy. An unrecorded specialization of Bateman–Horn is analogous to evaluating a classical special function at a new argument—worthwhile as data, but not a new conjecture in the conceptual sense; no conjecture’s contribution is a bare specialization, and the taxonomy is two-layered *within* each one. The *calibration layer*—the previously-known statements this paper begins from (Dubner’s conjectures, the Stern list, the Caldwell–Gallot laws, Martin’s refined Goldbach, Kourbatov’s record framework, the classical single instances of each family)—appears as attributed remarks inside the conjectures, each with its derived constant re-verified at our bounds; membership in the standard hierarchy of conjectures is itself a virtue, and the calibration layer is what makes the new constants credible. Our own contribution is graded as follows: mechanism-level content (the contamination calculus 1(v) with its instances 18, 19, 14, 12, 1, 4; the ordering deficits 5, 3; race sub-diffusivity 9; the entanglement law 6); derived second-order and distributional laws (10, 15, 2, 8(ii), 11(iii), 13, 7(iv), 16(ii)); and structural classifications (23, 25, 24, 20(i), 21(i), 22)—with framework attributions stated where an instance lives inside someone else’s theory (Kowalski’s for 15(ii), Montgomery–Soundararajan’s for 2 and 13). Every statement was searched against the literature at neighbourhood depth and verified at the scales reported in the stress-tests section. We regard the prime-power contamination calculus (Conjecture 1(v)) and its mechanism family—1 and 4, the fresh cousin-race predictions it generated, and the negative control 14—together with Conjecture 3(ii) and the derived covariance kernels of 8(ii) and 16(ii) as the paper’s core, joined by 13 and 23; Conjectures 20, 6 and 11 carry open modelling questions flagged in place.

One tagging convention runs through every statement below: clauses marked [theorem] or “elementary” are proved; clauses marked “conditional proposition” follow from the hypotheses stated with them; the remaining clauses are conjectures; and open questions are labelled as such and are not counted among the ninety-six conjectures.

### Computational-check standards

All counts below are exact (sieves; deterministic Miller–Rabin for $$n<3.3\times10^{24}$$; Baillie–PSW beyond, flagged as such). Every comparison reports the Poisson-normalized residual $$z=(\mathrm{obs}-\mathrm{pred})/\sqrt{\mathrm{pred}}$$. Every quoted $$z$$-score is such a residual and is used *descriptively*: where the counts compared are correlated, overlapping, or examined after selection, these residuals are not calibrated tail probabilities, and no significance claim in this paper rests on them. For sparse counts the cumulative comparison is contaminated at small $$x$$ by the phantom mass of the main-term integral near its lower limit; in those cases we also report per-decade increments, which are clean. Constants are computed by truncated Euler products with the truncation wobble (difference between cutoffs) reported as an error bar; for conditionally convergent quadratic and cubic products this wobble, not the last digit, is the effective precision.

Primality certification is stratified, and every count inherits the stratum of the integers it involves. Primality of every integer below $$3.3\times10^{24}$$ is decided *deterministically*, by fixed-base Miller–Rabin over a witness set verified for that range. For larger integers the classification is made by the Baillie–PSW test, and is a *probable-prime* classification, not a proof: no Baillie–PSW pseudoprime is known—and none exists below $$2^{64}$$, where the test is therefore deterministic—but their nonexistence is unproved. Consequently every count involving such integers is a probable-prime count, and is labelled as one wherever it appears. The computations affected are the factorial scans of Conjectures 21 and 2 ($$n!\pm1$$ for $$n$$ beyond about $$26$$), the $$n^2+2^n$$ scan of Conjecture 6 beyond $$n\approx80$$, the quartic values of the cyclotomic chain of Conjecture 24 beyond $$p\approx2\times10^6$$, and the Fibonacci–Lucas values of Conjecture 20 at all but the smallest indices. Every other count below—sieve censuses, race counts, window fields, and the inputs to every constant—lies entirely inside the deterministic range.

## Notation

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

Admissibility ($$\omega(p)<p$$ for all $$p$$) is checked for every constant computed. The natural-looking pair $$\{n^2+n+1,\ n^2+n+3\}$$ has $$\omega(3)=3$$ and is rejected; the $$k=4$$ branch of Conjecture 25 and the naive iterated chain behind Conjecture 24 are rejected by the same machinery, and both exclusions are part of the statements.

**How to read the ninety-six.** The count is a numbering convention, not a claim of ninety-six independent mechanisms. The contamination calculus is one operator, stated with the twin races at Conjecture 1 and projected onto the Goldbach (Conjecture 4), Stern (12), triplet (18) and sexy-pair (19) patterns, together with the provably null pattern of Conjecture 14 as its control, and those six statements stand or fall largely together. Several conjectures pair a proved classification with a Bateman–Horn lane that is standard once stated, and several keep attributed benchmarks inside them as calibration, with the tagging convention above separating the layers and the novelty labels marking what is claimed as new. Part II is five programmes, each contributing one central object and its laws. Part IV is one polynomial invariant carrying three programmes, and its twenty statements stand or fall in blocks rather than singly, with two, Conjectures 63 and 71, already fallen and recorded as resolved false. Part V is two rank enumerators of one bracket tensor, fifteen conjectures supported throughout the tested corpus, three stated in greater generality than the computations reach, and two resolved false with explicit counterexamples, flagged in place. Depth and independence therefore vary by design across the ninety-six, and the summary's ordering, not the raw count, carries the priority claim.

## Part I: conjectures from a local–global random model

*Added to the deposit: 28 July 2026.*

## Principal conjectures

The twin-race statement is split into its provable algebraic core and its conjectural clauses, stated through the logarithmic-mean functional $$\mathcal{M}_x$$ of the notation section.

**Lemma 1** *(Orientation elimination and class assignment).*

In $$\psi_2(x)=\sum_{n\le x}\Lambda(n)\Lambda(n+2)$$, the total contribution of terms in which $$n$$ or $$n+2$$ is a proper prime power is, apart from $$O(x^{1/3}\log^2 x)$$ from cubes and higher powers, carried entirely by the patterns $$(q^2-2,\,q^2)$$ with $$q$$ prime and $$q^2-2$$ prime: the mirror pattern $$(q^2,\,q^2+2)$$ is annihilated by $$3\mid q^2+2$$ for every prime $$q>3$$. Moreover, for every prime $$q\neq5$$, $$q^2-2\equiv2$$ or $$4\pmod 5$$ (never $$1$$), and for every odd $$q$$, $$q^2-2\equiv7\pmod8$$. (Two bounded exceptions: at $$q=5$$ the term $$(23,25)$$ lands outside the twin-start classes altogether, and at $$q=3$$ the mirror term $$(9,11)$$ survives, the annihilation beginning only at $$q>3$$; each is a single term, absorbed in the bounded error.)

The proof is elementary (squares mod $$3$$, $$5$$, $$8$$; the prime-power count). The lemma orients the race: prime-square contamination can enter only specific residue classes, and the model converts that into a drift prediction for the *unweighted* twin counts.

**Conjecture 1** *(Twin races modulo 5 and 8, and the prime-power contamination calculus; apparently new).*

Twin starts $$p>5$$ lie in classes $$p\equiv1,2,4\pmod5$$. Let $$D_1(x)=\pi_t(x;5,1)-\tfrac12\bigl(\pi_t(x;5,2)+\pi_t(x;5,4)\bigr)$$ and

$$
T(x)\;=\;\frac1{2\log^2x}
\sum_{\substack{q\le\sqrt x\\ q^2-2\ \mathrm{prime}}}
\log q\,\log(q^2-2).
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

The mechanism is the twin analogue of the classical explanation of Chebyshev’s bias: prime-square terms contaminate the classes that can contain them. (Biases of twin primes in residue classes have been studied before—Sahoo [27] for the mod-$$4$$ race, and [28] for prime pairs versus isolated primes—but we could find no prior statement of the mod-$$5$$ race, the $$(q^2-2,q^2)$$ mechanism, or the quantified surplus below.) Mod $$3$$ kills the pattern $$(q^2,q^2+2)$$ outright, a local accident that halves the mechanism and concentrates the surplus entirely on class $$1$$, as a mod-$$3$$ computation confirms. Data to $$4\times10^9$$: class counts $$(3980017,\ 3982505,\ 3981922)$$, $$D_1$$ within one noise unit of $$T$$ throughout, no persistent leader, and the control race $$\pi_{t,2}-\pi_{t,4}$$ wandering like a fair coin. Mod-8 data to $$10^9$$: class counts $$(856684,\ 855807,\ 856046,\ 855967)$$ for $$a=1,3,5,7$$; $$D_7=+212$$ at $$10^9$$ against predicted $$T=+254$$ with noise $${\sim}1068$$, positive through most of the range (log-density $$0.775$$), and the three pairwise $$\{1,3,5\}$$ controls all within one noise unit of zero—the two projections of the mechanism behave coherently, none of it provable at present.

**Conjecture 2** *(The pair-level Montgomery–Soundararajan reduction; apparently new).*

For the window field of Conjecture 8(ii), the diagonal variance of the twin-pair count reduces to a *pinned* singular-series average. With $$R(h)=C_4(0,2,h,h+2)/\mathfrak{S}(2)^2$$ for $$h\ge1$$ (zero when the offset set is degenerate or inadmissible—all odd $$h$$, and $$h=2$$ since $$\{0,2,4\}$$ dies at $$3$$; consecutive twin pairs cannot overlap beyond $$(3,5,7)$$, so no overlap term exists) and

$$
G(H)\;=\;\sum_{1\le h\le H}\Bigl(1-\frac hH\Bigr)\bigl(R(h)-1\bigr),
$$

the derived identity (clause *(i)*) is

$$
\frac{\operatorname{Var}_t\,\pi_2(t;H)}{\mathbb E_t\,\pi_2(t;H)}
\;=\;1+\frac{\mathfrak{S}(2)\,\bigl(2G(H)-1\bigr)}{\log^2x}
+o\!\Bigl(\frac1{\log^2 x}\Bigr):
$$

with $$p=\mathfrak{S}(2)/\log^2x$$ the per-site intensity, the variance is $$Hp(1-p)+2p^2HG(H)$$, so $$\operatorname{Var}/\mathbb E=1-p+2pG(H)$$—the Bernoulli diagonal term $$-p=-\mathfrak{S}(2)/\log^2x$$ is of exactly the order of the claimed error and cannot be dropped (it is the same diagonal that, in the single-prime case, merges into Montgomery–Soundararajan’s constant $$\gamma+\log2\pi-1$$). With that term retained, the entire deficit left open at Conjecture 8(ii) is the single computable function $$G$$ plus the explicit Bernoulli correction—the pair analogue of Montgomery–Soundararajan’s reduction of the prime-count variance to $$\sum_{h\le H}\mathfrak{S}(h)(H-h)$$ [19]. Clause (i) is a *conditional proposition*, not an independent conjecture: given quantitative Hardy–Littlewood for $$4$$-tuples, the reduction follows. The conjectural clause is (ii): $$-G(H)/\log H$$ diverges—the pinned average grows strictly faster than the single-prime secondary term $$\tfrac12(\log H+\gamma+\log2\pi-1)$$, so pair counts in windows are more sub-Poisson than prime counts—with the caveat that data to $$H=3000$$ cannot distinguish divergence from a pure $$\log$$ with a large constant (nor $$c\log H\log\log H$$ from $$(\log H)^\alpha$$): what the computation *establishes* is only that the local slope exceeds the single-prime value sevenfold across the computable range; the divergence and its exact form are registered, not evidenced beyond that.

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

The stratified experiment behind these numbers separates moduli by factorization type in the matched range $$q\in[1500,6000]$$: over $$40$$ *prime* moduli, $$\theta_{\mathrm{disc}}=0.847$$ (essentially constant across $$q$$) and $$\theta_{\mathrm{corr}}=0.824\pm0.009$$; over $$40$$ *$$7$$-smooth* moduli in the same range, $$\theta_{\mathrm{disc}}=4.32\pm0.22$$ (the large $$q/\varphi(q)$$ hazards make discreteness dominant) while $$\theta_{\mathrm{corr}}=-2.32\pm0.22$$ reverses sign. The comparison with Leung [29] is thereby given its answer-shaped experiment: Leung derives the exponential law under a uniform Hardy–Littlewood hypothesis and reports discrepancies for *smooth* moduli, and our smooth stratum indeed behaves anomalously—but the positive ordering term survives, with small error bars, exactly where smooth-modulus effects cannot reach. Whether $$\theta_{\mathrm{corr}}$$ tends to a constant, and the exact functional form in $$1/\log q$$, remain open: data at $$q\le6000$$ cannot distinguish $$1/\log q$$ from $$(\log\log q)/\log q$$-type refinements—the aggregate $$\Theta\approx1.5$$–$$1.9$$ over $$q\in[10^2,6\times10^3]$$, with $$\mathbb E_a[U]$$ bottoming near $$0.737$$ around $$q\approx200$$ and recovering through $$0.776$$ by $$q\approx6000$$, is calibration, not a determination of the form. The averaging family is fixed as: all moduli of the stated type in dyadic ranges of $$q$$, per stratum.

**Remark 1.**

The deficit is reproducible and is *not* an artefact of the time-change: a Cramér pseudo-prime control (independent Bernoulli “primes” with the correct densities and parity) shows roughly half of it—the discreteness of large per-candidate hazards—while the other half vanishes under any reshuffling of the actual prime residues (iid labels, or a random permutation of the true residue sequence, both restore $$\mathbb E[U]=1.00$$). The ordered sequence of primes fills residue classes measurably faster than any exchangeable model, and the stratified experiment above shows the effect is not a smooth-modulus artefact: it is largest and cleanest on prime moduli. We measure $$\theta_{\mathrm{corr}}$$; we cannot yet derive it.

**Conjecture 4** *(The Goldbach lane race; apparently new).*

For $$n\equiv2\pmod4$$ let $$R_1(n)$$, $$R_3(n)$$ be the ordered Goldbach representation counts in the lanes $$p\equiv q\equiv1$$ and $$p\equiv q\equiv3\pmod4$$ (the lane convention of the Martin benchmark recorded at Conjecture 5), and $$D(n)=R_3(n)-R_1(n)$$. Prime-square terms $$n=q^2+p$$ ($$q$$ odd prime) land *exclusively* in the $$(1,1)$$ lane, since $$q^2\equiv1\pmod4$$ and then $$n-q^2\equiv1\pmod4$$ automatically. Consequently the $$(3,3)$$ lane leads on average. Define

$$
D_{\mathrm{sys}}(n)\;=\;\frac{2}{\bar\ell(n)}
\sum_{\substack{q \text{ odd prime},\ q\le\sqrt n\\ n-q^2 \text{ prime}}}
\log q\,\log(n-q^2),
\qquad
\bar\ell(n)\;=\;\frac{n-6}{\displaystyle\int_3^{n-3}
\frac{dt}{\log t\,\log(n-t)}},
$$

(the analytic mean of $$\log p\log(n-p)$$ under the lane profile; the empirical lane mean is its estimator). Write $$\mathbb E_x$$ for the average over $$n$$ drawn from $$\{n\equiv2\ (4),\ n\le x\}$$ with weight proportional to $$1/n$$ (the logarithmic sampling measure, now explicit). Then: *(i)* [drift law] $$\mathbb E_x[D-D_{\mathrm{sys}}]=o(\mathbb E_x[D_{\mathrm{sys}}])$$ as $$x\to\infty$$: the $$(3,3)$$ lane leads on average by exactly the square contamination; *(ii)* [weighted mean and internal null lane] $$\mathbb E_x[D_{\mathrm{sys}}]$$ is given by the Hardy–Littlewood (Conjecture H) local model for $$n-q^2$$, whose local factors vary strongly with $$n$$—most drastically at $$p=3$$: for $$n\equiv1\pmod3$$, $$3\mid n-q^2$$ for *every* prime $$q>3$$, so the contamination collapses to a single boundary family, the $$q=3$$ term (when $$n-9$$ is prime): the complementary possibility $$n-q^2=3$$ is empty on this ensemble, since $$n\equiv2\pmod4$$ forces $$n-3\equiv3\pmod4$$, never a square. The family is negligible in logarithmic mean, so the race carries no drift at the systematic scale on the subprogression $$n\equiv10\pmod{12}$$: with the positive comparison scale $$A_G(x):=\mathbb E_x^{(\not\equiv1\,(3))}[D_{\mathrm{sys}}]$$, the logarithmic-ensemble mean of the systematic term over the contaminated lane $$n\not\equiv1\pmod3$$ (a comparison against this subprogression’s own systematic term, which vanishes, would be empty), the claim is $$\mathbb E_x[D]=o\bigl(A_G(x)\bigr)$$ on $$n\equiv10\pmod{12}$$, while the drift concentrates on $$n\not\equiv1\pmod3$$: an internal null lane, predicted by the same mechanism that predicts the lead; *(iii)* [sign density] the per-$$n$$ drift-to-noise ratio $$\kappa(n)=D_{\mathrm{sys}}(n)\big/\sqrt{\mathfrak{S}(n)J(n)}$$ (where $$J(n)=\int_3^{n-3}dt/(\log t\log(n-t))$$, so that $$\mathfrak{S}(n)J(n)$$ is the total ordered representation count) satisfies $$\kappa(n)\asymp c(n)/\log n\to0$$; under the Gaussian fluctuation model the logarithmic density of $$\{D>0\}$$ is therefore $$\tfrac12$$ in the limit, with the finite-$$x$$ sign fraction predicted to be $$\mathbb E_x[\Phi(\kappa)]$$ ($$\Phi$$ the standard normal distribution function)—decaying, but far from $$\tfrac12$$ at any accessible height.

Derivation status: the identity behind $$D_{\mathrm{sys}}$$ is the $$\Lambda$$-weighted lane symmetry minus its prime-power part; the transfer to unweighted counts is a partial-summation argument whose error terms (higher prime powers, which enter only at the $$n^{1/3}$$ scale, and the variation of the weight across the lane) remain to be written out—the same open transfer flagged at Conjecture 1—and clause (iii) inherits the zero-oscillation caveat stated there. One further disclosure: the census $$D_{\mathrm{sys}}$$ is computed from the primes in the same sample it is compared against, so the level agreement is in-sample; the out-of-sample content of the verification is the null lane and the class assignment, which the mechanism fixes in advance.

This is the Goldbach-partition analogue of Chebyshev’s bias, produced by the same explicit-formula mechanism as Conjecture 1 but through $$q^2+p$$ patterns rather than twin patterns; the single-sign prediction (every square contamination falls into one lane) makes it cleaner than the classical race. We could find no prior statement. The neighbouring phenomenon for consecutive primes is the Lemke Oliver–Soundararajan mod-3 law, whose verification here—$$\hat c$$ drifting $$0.400\to0.370$$ over $$10^7\!\to\!4\times10^9$$ with $$(1,1)/(2,2)$$ symmetry $$0.99989$$—serves as calibration for the present race.

Computational checks. Over $$500$$ log-spaced samples $$n\le10^8$$: mean $$D=76.5$$ against mean empirical $$D_{\mathrm{sys}}=64.5$$, the $$(3,3)$$-lane lead significant at $$5.2$$ standard errors of the mean. Clause (ii)’s weighted model, computed in presieve-exact form (trial division of each $$n-q^2$$ to $$10^3$$ with the exact Mertens normalization), reproduces the empirical contamination with no fitted parameter: model mean $$66.3$$ against empirical $$67.8$$ (ratio $$0.98$$) on a $$400$$-sample run. The internal null lane behaves as predicted: on $$n\equiv1\ (3)$$ ($$123$$ samples) the model and empirical $$D_{\mathrm{sys}}$$ both vanish and the measured lead drops to $$31\pm23$$ (consistent with zero), while on $$n\not\equiv1\ (3)$$ ($$277$$ samples) the lead is $$88\pm21$$ against predicted contamination $$96$$—the drift lives exactly where the mechanism puts it. Clause (iii): computed $$\mathbb E_x[\Phi(\kappa)]=0.572$$ ($$\kappa$$ ranging $$0$$–$$0.64$$ with mean $$0.18$$) against observed sign fraction $$0.588$$; weak, and quantitatively the weakness the model requires.

**Conjecture 5** *(The least Goldbach summand: exponential law and ordering deficit; the time-changed law and deficit constant apparently unstated).*

Let $$s(n)$$ be the least prime $$p\nmid n$$ with $$n-p$$ prime (the exclusion $$p\nmid n$$ removes a trivial obstruction: $$p\mid n$$ forces $$p\mid n-p$$, so $$n-p$$ is composite except in the diagonal case $$n=2p$$, which would otherwise distort the hazard at one atypical point), and time-change by the expected-arrivals clock $$U(n)=\mathfrak{S}(n)\sum_{p\le s(n),\,p\nmid n}1/\log(n-p)$$. Here $$s(n)=+\infty$$ when no admissible prime exists, which among even $$n$$ happens only at $$n=4$$ and $$n=6$$ and conjecturally at no larger even $$n$$, so the law below runs over the even $$n$$ with $$s(n)$$ finite. The ensemble is fixed first, since $$U(n)$$ is deterministic at each $$n$$ and an expectation therefore needs a declared measure: for a scale $$X$$,

$$
\mathbb E_XU=
\frac{\sum_{X<n\le2X,\ 2\mid n}U(n)/n}
{\sum_{X<n\le2X,\ 2\mid n}1/n},
\qquad
\Theta_G(X)=\bigl(1-\mathbb E_XU\bigr)\log X.
$$

Then: *(i)* [limit law] under $$\mathbb E_X$$-sampling, $$U\Rightarrow\mathrm{Exp}(1)$$ as $$X\to\infty$$; *(ii)* [canonical ordering deficit] $$\Theta_G(X)\to\Theta_G>0$$—the Goldbach sibling of the least-prime deficit of Conjecture 3(ii), produced by the same occupancy mechanism: the ordered primes fill the available representations faster than an exchangeable model, so the first arrival comes *early* and $$\mathbb E_X[U]<1$$.

The extremal theory of $$s(n)$$ is well developed—Granville, van de Lune and te Riele conjectured $$s(n)=O(\log^2n\log\log n)$$, and Oliveira e Silva–Herzog–Pardi [12] tabulate first occurrences of minimal Goldbach summands to $$4\times10^{18}$$ against prime $$k$$-tuple predictions—but the time-changed distributional law (i) and the deficit constant (ii) appear unstated (we could not rule out that the untransformed version of (i) is implicit in the comparisons of [12]). Measured on $$2{,}000$$ log-sampled $$n\le10^8$$: $$\mathbb E[U]=0.796$$, with $$\Theta_G=3.12\pm0.35$$ on $$[10^6,10^7)$$ and $$3.42\pm0.45$$ on $$[10^7,10^8)$$—positive, stable, and roughly *twice* the least-prime-in-progressions deficit $$\Theta=1.67$$ of Conjecture 3, a comparison the occupancy expansion there should eventually explain; the Kolmogorov–Smirnov distance to $$\mathrm{Exp}(1)$$ ($$0.088$$ at this size) is dominated by the deficit displacement itself, as (ii) requires. The derivation route for $$\Theta_G$$, parallel to the occupancy expansion at Conjecture 3: expand the survival probability $$\Pr(s(n)>y)=1-\sum_{p\le y}h_p+\sum_{p_1<p_2\le y}h_{p_1,p_2} -\cdots$$, where the pair term requires $$n-p_1$$ and $$n-p_2$$ simultaneously prime and so carries the Hardy–Littlewood singular series of the shift $$p_2-p_1$$; inserting the $$k$$-tuple predictions and integrating against the time change isolates the $$1/\log X$$ coefficient—deriving $$\Theta_G$$ rather than measuring it is the programme registered here. $$\mathfrak{S}(n)$$ alone does not encode the between-candidate dependence that the pair term carries. (The $$(3,3)$$-lane refined Goldbach statement—every $$n\equiv2\ (4)$$, $$n\ge6$$, is $$p+q$$ with $$p\equiv q\equiv3\ (4)$$, with the halved singular-series count law, formulated by K. Martin [13]—is included as an attributed calibration benchmark: exhaustively verified to $$10^9$$, count formula matching to $$0.2$$–$$1.3\%$$; its comparative lane statement is Conjecture 4.)

One scale observation prepares the next conjecture: for sequences whose $$n$$th term has size $$\mathrm{e}^{cn}$$ the expected number of primes is $$\sum_n \kappa_n/(c\,n)$$: convergence or divergence of this sum is the entire question, and when it diverges it diverges logarithmically, so the right conjecture has counting function $$\alpha\log x$$ with a derived $$\alpha$$.

**Conjecture 6** *($$n^2+2^n$$; sequence is OEIS A064539).*

Every prime of the form $$n^2+2^n$$ with $$n>1$$ has $$n\equiv3\pmod6$$ (elementary), and: *(i)* infinitely many such primes exist, with counting function $$\asymp\log N$$; *(ii)* [candidate law, entanglement-aware form] for a finite set $$S$$ of primes $$p\ge5$$ (the primes $$2$$ and $$3$$ are exact in the lane reduction, $$\delta_2=\delta_3=0$$, and $$\operatorname{ord}_2 2$$ is undefined) let $$D_S$$ be the *exact* joint density, within the lane $$n\equiv3\ (6)$$, of $$n$$ with $$p\nmid n^2+2^n$$ for all $$p\in S$$, computed over the full joint period $$\mathrm{lcm}_{p\in S}\,\mathrm{lcm}(6,\,p\cdot\operatorname{ord}_p2)$$, and set $$\kappa_S=3\,D_S/\prod_{p\in S}(1-1/p)$$: the factor $$3=2\cdot\tfrac32$$ is the exact lane bonus at the primes $$2$$ and $$3$$ (within the lane $$\delta_2=\delta_3=0$$, so each contributes its full $$(1-1/p)^{-1}$$), included in the definition so that $$\kappa_S$$ is the complete local constant of the count in (ii-c). The conjecture is stated along the *canonical exhaustion* $$S_z=\{p\ \text{prime}:5\le p\le z\}$$, and its three layers are logically separate and are asserted separately: *(ii-a)* the sequence $$\kappa_{S_z}$$ converges as $$z\to\infty$$ (a general net over arbitrary finite $$S$$ carries an order-of-exhaustion ambiguity we do not need), with limit $$\kappa$$; *(ii-b)* whether the limit *factors*—i.e. whether the exact finite-level factorization observed below persists, so that entanglement is asymptotically absent—is an *open question*, expressly not counted among this paper’s conjectural assertions, on which (ii-a) takes no position; and *(ii-c)* the count is $$\sim\sum_{n\le N,\,n\equiv3\,(6)}\kappa/\log(n^2+2^n)$$—a genuine further step, since a convergent local density does not automatically govern the global count. The working value $$\kappa^{*}=4.2734\ldots$$ is a *hybrid*, not a computation of any single $$\kappa_{S_z}$$: the lane factor $$3$$ times the CRT-exact core $$S_{19}$$ times independent per-prime factors for $$19<p\le300$$—so $$\kappa^{*}=\kappa_{S_{300}}$$ exactly if and only if the observed exact factorization persists to $$300$$.

This is not a Bateman–Horn problem: the local conditions at different primes are tied through the orders $$\operatorname{ord}_p2$$, so the per-prime product $$\prod_p(1-\delta_p)/(1-1/p)$$ would tacitly assume their independence. The law is therefore stated through the CRT-exact quantities $$\kappa_S$$, which make no independence assumption. The computation then returned a small surprise in the other direction: through $$p\le19$$ (joint period $$116{,}396{,}280$$) the joint survivor fraction equals the product of the per-prime fractions as an *exact rational identity*, verified in exact arithmetic at every level $$S=\{5\le p\le P\}$$, $$P\in\{5,7,11,13,17,19\}$$. Entanglement is thus absent at all computed levels; whether exact factorization persists for all $$p$$—equivalently, whether the survival events are exactly independent over every joint period, which would itself be a nontrivial equidistribution statement about the orbits of $$2$$—is part of what clause (ii) asks. We separate the robust claim (i) from the candidate law (ii), and note that the eight hits below $$6000$$ are far too few to validate a four-digit constant—the verification below checks consistency, not the constant. The OEIS records further candidate indices beyond our completed range: $$29355$$, $$34653$$, $$57285$$, $$99069$$, and the probable-prime candidate $$1933695$$. We could not independently re-verify these, but all five satisfy the lane constraint $$n\equiv3\ (6)$$, and taking them at face value the $$\kappa^{*}$$-model predicts $$2.9$$ hits in $$(6\times10^3,10^5]$$ against $$4$$ reported and $$5.9$$ in $$(6\times10^3,1.94\times10^6]$$ against $$5$$ ($$z=+0.65$$ and $$-0.38$$): the records extend the consistency check by two decades.

The congruence claim is elementary: $$n$$ odd is forced by parity, and for odd $$n$$ with $$3\nmid n$$ we have $$n^2+2^n\equiv1+2\equiv0\pmod3$$. What appears to be a harsh obstruction is, inside the surviving lane, a local bonus: $$\delta_2=\delta_3=0$$ contribute the factors $$2\cdot\tfrac32=3$$ carried explicitly in the definition of $$\kappa_S$$.

*Computational checks* (probable-prime count beyond $$n\approx80$$). Hits $$\{3,9,15,21,33,2007,2127,3759\}$$ up to $$6000$$: observed $$8$$, model $$8.55$$, $$z=-0.19$$ (over the shorter range $$n\le4200$$: $$8$$ vs $$8.19$$, $$z=-0.07$$); the lane constraint was verified exhaustively (no prime off $$n\equiv3\ (6)$$ to $$n=3000$$, independently reconfirmed), and the CRT-exact factorization of clause (ii) was verified through $$p\le19$$ as described at the statement.

**Conjecture 7** *(Fermat quotients: the multibase subtorus law and the Wieferich ledger; single-base heuristic previously stated [22], the vertical multibase law apparently new).*

With $$q_p(a)=(a^{p-1}-1)/p\bmod p$$ (defined for primes $$p\nmid a$$; all clauses below range over such $$p$$ only) and $$q_p=q_p(2)$$, clauses *(0)*–*(v)*, stated multibase group first: *(0)* [structure, classical] $$q_p(ab)\equiv q_p(a)+q_p(b) \pmod p$$ (the Eisenstein–Lerch homomorphism; verified exactly on every tested prime), so for multiplicatively *dependent* bases the vector $$(q_p(a_1),\dots,q_p(a_r))/p$$ is confined to the rational subtorus cut out by the relations; *(iv)* [multibase equidistribution, the claimed law] for multiplicatively *independent* bases the vector equidistributes on the full torus as $$p$$ varies—the *vertical* joint law, complementing the fixed-$$p$$, varying-base statistics of Ostafe–Shparlinski and Cobeli–Zaharescu—with correlations vanishing and the same LIL calibration as (i) below; *(v)* [simultaneous Wieferich] the expected count of $$p\le x$$ with $$q_p(2)=q_p(3)=0$$ has convergent sum $$\sum1/p^2$$: at most finitely many simultaneous Wieferich primes exist (the single-base folklore of this accounting is Conrad’s), and the empirical list is empty to $$10^7$$. Three further clauses on the base-2 quotient alone: *(i)* [global equidistribution] $$q_p/p$$ equidistributes on $$[0,1)$$ with discrepancy at exactly the calibrated random-model scale: in its sharp form,

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

(A further Hardy–Littlewood calibration, on a prime quintuplet constellation, gives observed $$15{,}236$$ against predicted $$15{,}230.3$$ at $$4\times10^9$$, ratio $$1.0004$$, $$z=+0.05$$.)

**Conjecture 9** *(The sub-diffusivity of balanced prime races; apparently new).*

Model a balanced race (Conjecture 1(ii)’s symmetric class differences) as the walk of its class-assignment steps, the process defined at event index: enumerate the pattern occurrences $$n_1<n_2<\cdots$$ in the two competing classes, set $$\xi_i=\pm1$$ by class membership of $$n_i$$, and let $$\rho_k(x)$$ denote the lag-$$k$$ sample autocorrelation of $$(\xi_i)$$ over the events with $$n_i\le x$$. Then the walk is measurably *sub-diffusive*: *(i)* [decaying-repulsion law] the step autocorrelations are negative at small lags—the race analogue of the Lemke Oliver–Soundararajan consecutive-pattern repulsion [24], which supplies the mechanism—and, since that repulsion is scale-dependent rather than fixed, the conjectured form is a decay law

$$
\rho_k(x)\;=\;-\,\frac{c_k\log\log x+d_k}{\log x}\,(1+o(1)),
$$

with constants $$c_k,d_k$$ in principle derivable from the LOS correlation series (underived here; and the measured values $$\rho_1\approx-0.037$$, $$\rho_2\approx-0.009$$ at $$10^9$$—universal across twin and cousin races mod $$5$$ and $$8$$ to within $$0.004$$, each $${\sim}50$$ standard errors from zero—are observations at one height, consistent with $$c_1\approx0.25$$ there, not asymptotic constants); *(ii)* [long memory, measured] short lags do not exhaust the deficit: the running maxima $$M(x)=\max_{t\le x}\vert D(t)\vert /\sqrt{\text{count}}$$ of the four races land at quantiles $$0.02$$–$$0.17$$ of the simulated independent-step null (median $$2.34$$ at this span), and still only $$0.03$$–$$0.23$$ after correcting for $$\rho_{1,2}$$: the negative correlation persists across lags, so the cumulative diffusivity $$\sigma^2(x)=1+2\sum_k\rho_k(x)$$ sits well below $$1$$ at this height. The model layer is declared: $$(\xi_i)$$ is a deterministic, nonstationary family and the $$\rho_k(x)$$ are empirical statistics of it, so the Green–Kubo identity $$\sigma^2=1+2\sum_k\rho_k$$ is invoked under an explicit *local-stationarity model hypothesis*—the step process restricted to a window $$[x,2x]$$ is modelled as a stationary sequence whose autocorrelations are the measured $$\rho_k(x)$$—and the variance statement can equivalently be taken as a direct *definition* of $$\sigma^2(x)$$ through block averages of $$(S_{n+m}-S_n)^2/m$$ over the events up to $$x$$, a form in which no stationarity is assumed at all. The Green–Kubo sum requires more than the fixed-lag law of (i): the per-lag decay controls each $$\rho_k(x)$$ but not the sum unless the decay is *uniform in $$k$$ with summable tail*, since the number of relevant lags may grow with $$x$$. We therefore state the needed hypothesis as part of the clause: $$\rho_k(x)$$ obeys the law of (i) uniformly for $$k\le K(x)$$ with $$\sum_{k>K(x)}\vert \rho_k(x)\vert =o(\log\log x/\log x)$$ for some $$K(x)\to\infty$$, *and*—since the tail bound alone leaves the growing head sum uncontrolled—the repulsion constants are summable, $$\sum_k c_k<\infty$$ and $$\sum_k\vert d_k\vert <\infty$$, so that $$\sigma^2(x)=1-2\bigl(\textstyle\sum_kc_k\,\log\log x+\sum_kd_k\bigr)/\log x\,(1+o(1))$$ is a genuine consequence rather than an unjustified interchange of limits. The measured correlation length at $$10^9$$ (a few tens of lags, with $$\vert \rho_k\vert$$ decreasing geometrically in the observable range) is consistent with both hypotheses. Under them, $$\sigma^2(x)$$ returns to $$1$$ asymptotically, making sub-diffusivity a finite-height phenomenon of $$\log\log x/\log x$$ size, like every other second-order law in this paper; *(iii)* [registered dichotomy, open] asymptotically the two possibilities are *mutually exclusive*, and which of them holds is the open question. Either the fixed-lag expansion of (i) extends uniformly in $$k$$ with summable constants—in which case the hypotheses of (ii) hold, (ii) applies, and the race is asymptotically diffusive with $$\sigma^2(x)\to1$$ (running maxima $$\sim\sqrt{2\log\log x}$$, Darling–Erdős class)—or that expansion fails at long lags, and only in that case can the race inherit the almost-periodic rigidity that Rubinstein–Sarnak-type structure [6] forces on classical races (maxima $$\asymp(\log\log\log x)^{A}$$, the Montgomery–Ng class). Rigidity therefore requires a failure of the hypotheses of (ii) at long lags, and cannot coexist with them. No explicit formula is known for twin patterns, the two branches differ only beyond any computable height, and we register the dichotomy without choosing *in this conjecture*. What is conjectured here is therefore the fixed-lag law (i) outright, and the variance law of (ii) *conditionally on* its stated uniformity and summability hypotheses, which belong to the finite-height model layer and are not asserted asymptotically: asserting them would silently select the diffusive branch of (iii). The pattern-specific selection is made elsewhere—Conjecture 1 asserts the rigid branch for its races, through (i-b) for the contaminated combinations and through the drift-scale nulls of its clause (ii) for the symmetric differences—and consistency between the two conjectures then requires exactly that the hypotheses of (ii) fail at long lags for those races.

The repulsion constants $$\rho_1,\rho_2$$ are pattern-independent across our four races—a universality the LOS correlation series should predict quantitatively, and the derivation programme stated here—and the suppressed maxima are the first (to our knowledge) direct measurement of race sub-diffusivity, an effect invisible to endpoint statistics. (The twin-gap record benchmark—$$G_t(x)\asymp\log^3x$$ with working constant $$1/(2C_2)$$, inside Kourbatov’s extreme-value framework [15]—is included as an attributed calibration benchmark: records to $$4\times10^9$$ wander in $$[0.41,0.56]\log^3x$$, approaching from below on a $$\log\log$$ clock, largest observed twin-to-twin gap $$5292$$ after the twin at $$2{,}466{,}641{,}069$$; the Cramér–Granville fragility of such constants [17] is why the constant was always flagged as first-order.)

## Family laws and second-order refinements

**Conjecture 10** *(Uniform quadratic de Polignac; family law apparently unstated, the $$d=2$$ instance previously stated, cf. OEIS A080149, [32]).*

For even $$d\ge2$$ let $$\pi^{\mathrm q}_d(N)=\#\{n\le N:\ n^2+1,\ n^2+1+d \text{ both prime}\}$$ and $$C(d)=C(x^2+1,\,x^2+1+d)$$. Then: *(i)* [uniform family law] for every fixed $$B>0$$, $$\pi^{\mathrm q}_d(N)=C(d)\,I_d(N)(1+o(1))$$ uniformly over even $$d\le(\log N)^{B}$$; *(ii)* [registered rate, strictly stronger] there is $$\eta_B>0$$ with

$$
\sup_{\substack{2\le d\le(\log N)^{B}\\ 2\mid d}}
\Bigl\vert \frac{\pi^{\mathrm q}_d(N)}{C(d)\,I_d(N)}-1\Bigr\vert
\;\ll_B\;(\log N)^{-\eta_B}
$$

—an error clause that no version of Bateman–Horn supplies, registered separately from (i) since its analytic content is independent; *(iii)* [family statistic: the law of the constants] each local factor of $$C(d)$$ depends only on $$d\bmod p$$, and the factors at any *finite* set of primes are exactly independent as $$d$$ varies (CRT), with the passage to the infinite product controlled by the convergent tail-variance sum—which supplies the uniform integrability (via $$L^2$$-boundedness of the normalized partial products) that the moment identities require, since almost-sure convergence alone would not carry means through the limit; so the moments of $$C(d)$$ over even $$d\le D$$ converge, as $$D\to\infty$$, to *derived* Euler products; in particular

$$
\frac1{\#\{2\mid d\le D\}}\sum_{2\mid d\le D}C(d)\to\bar C=2.7456\ldots,
\qquad
\operatorname{sd}\bigl(C(d)\bigr)\to1.6840\ldots,
$$

and the empirical distribution of $$C(d)$$ converges to the law of the random product $$\prod_p f_p(U_p)$$ with independent uniform residues $$U_p$$. In particular ($$d=2$$, the classical instance): $$\#\{n\le N:\ n^2+1,\ n^2+3 \text{ both prime}\}\sim C(2)\,I(N)$$, $$C(2)=2.954014\ldots$$

This is the quadratic analogue of the uniform de Polignac law of Conjecture 8: not one count but the whole profile of constants must be matched at once, and the family, unlike its linear parent, has no known prior statement. Every even shift is admissible (for $$p\ge5$$, $$\omega(p)\le4<p$$; the classes mod $$3$$ and $$5$$ vary with $$d$$, which is what makes the $$C(d)$$-profile nonconstant, spanning a factor of about twenty over $$d\le300$$, from $$0.47$$ at $$d=298$$ to $$9.06$$ at $$d=162$$). At $$d=2$$ the local analysis reads: $$n$$ even, $$n\not\equiv0\pmod3$$, $$\omega(p)=2+\bigl(\frac{-1}{p}\bigr)+\bigl(\frac{-3}{p}\bigr)$$ for $$p\ge5$$, and the conjecture implies infinitely many twin pairs $$(m+1,m+3)$$ with $$m$$ a perfect square. Profile verification at $$N=10^6$$ over all $$150$$ even shifts $$d\le300$$: correlation $$0.99976$$ between observed and predicted counts, regression slope $$1.0022$$, residual mean $$z=+0.24$$ with spread $$0.84$$ and $$\max_d\vert z\vert =2.28$$—the shape-of-agreement standard applied across the family. Clause (iii) was verified by computing both sides independently: the derived Euler-product moments give mean $$2.7456$$ and standard deviation $$1.6840$$, against $$2.7434$$ and $$1.6726$$ measured over the $$150$$ constants with $$d\le300$$ (ratios $$0.9992$$ and $$0.9932$$)—a family-level statistic whose constants are derived, not fitted. Clause (iii), unlike (i) and (ii), may prove accessible unconditionally by the exact-CRT and martingale route recorded at Conjecture 15; the hard content here is the uniform law and the rate clause. One question the family raises is recorded as open rather than conjectured: the maximal range $$D(N)$$ for which the uniform law can hold (the analogue of the Elliott–Halberstam question for this family—whether there is a sharp transition at some power scale $$N^{\delta}$$ rather than a logarithmic one).

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

The full limit does not follow by inverting Granville’s $$\limsup G(x)/\log^2x=2\mathrm{e}^{-\gamma}$$: that inversion is invalid, since a limsup envelope for maximal gaps controls only where gaps *can first appear at the earliest*, i.e. a lower envelope for $$p(g)$$—hence a liminf claim, not a limit. Whether $$\log p(g)/\sqrt g$$ converges at all, and if so whether the limit is Shanks’s classical $$1$$ [16] (as Wolf’s refinement $$p(g)\sim\sqrt g\,\mathrm{e}^{\sqrt g}$$ and the Kourbatov–Wolf residue-class laws [25] also assert) or the envelope value, involves at least three distinct phenomena—whether a given $$g$$ occurs near the extreme scale at all, the distribution of exact gap lengths near records, and the difference between record gaps and non-record first occurrences—and is left open here. The two candidate constants differ by $$6\%$$, beneath the resolution of any feasible computation: our regression slope over $$g\ge100$$ falls from $$1.307$$ at $$10^9$$ to $$1.297$$ at $$4\times10^9$$, far above both and decreasing, as it must be for either.

**Conjecture 12** *(The Stern lane race; apparently new).*

In Stern’s representation problem $$n=p+2k^2$$ ($$n$$ odd), race the $$k$$-even and $$k$$-odd lanes. Prime-square contamination of the $$\Lambda$$-weighted lane counts comes from $$n=q^2+2k^2$$—the norm form $$x^2+2y^2$$ of $$\mathbb Q(\sqrt{-2})$$ with prime $$x$$—and since $$q^2\equiv1\pmod8$$ while $$2k^2\equiv0$$ or $$2\pmod 8$$ by the parity of $$k$$: *(i)* [class assignment, direct congruence] contamination sits in the $$k$$-*even* lane iff $$n\equiv1\pmod8$$, in the $$k$$-*odd* lane iff $$n\equiv3\pmod8$$, and for $$n\equiv5,7\pmod8$$ *no* square contamination exists at all: $$q^2+2k^2\equiv1$$ or $$3\pmod 8$$ always, a two-line congruence (genus theory enters only for the converse question of which $$n$$ *are* represented), so the null classes are provable, not conjectured; *(ii)* [drift law, in the ensemble form of Conjecture 4] Fix the ensemble: for a scale $$X$$, let $$\mathbb E_X$$ average over odd $$n\in(X,2X]$$ of the given residue class mod $$8$$ with weight proportional to $$1/n$$ (the logarithmic sampling measure, as at Conjectures 5 and 4). Define, per class, with $$R_{\mathrm o}(n)$$ and $$R_{\mathrm e}(n)$$ the numbers of representations $$n=p+2k^2$$ with $$k$$ odd and $$k$$ even respectively, the *clean-minus-contaminated* difference with explicit sign: $$D(n)=R_{\mathrm o}-R_{\mathrm e}$$ for $$n\equiv1\pmod 8$$ (even lane contaminated), $$D(n)=R_{\mathrm e}-R_{\mathrm o}$$ for $$n\equiv3\pmod 8$$, and $$D(n)=R_{\mathrm e}-R_{\mathrm o}$$ (sign immaterial) on the null classes $$n\equiv5,7\pmod8$$. Set $$D_{\mathrm{sys}}(n)=\bigl[\sum_{(q,k):\,q^2+2k^2=n,\ q\ \mathrm{prime},\,k\ge1}\log q\bigr]/\lambda_{\mathrm{an}}(n)$$—the weight is $$\Lambda(q^2)=\log q$$, each representation counted once in the $$k\ge1$$ convention (the ordered-representation factor $$2$$ of Conjecture 4 has no counterpart here, and doubling would be a normalization error)—where $$\lambda_{\mathrm{an}}(n)$$ is the *analytic* lane mean of $$\log p$$ over the candidate profile, defined with no reference to which candidates are prime: $$\lambda_{\mathrm{an}}(n)=\bigl(\int_0^{\sqrt{(n-2)/2}}du\bigr)\big/\bigl(\int_0^{\sqrt{(n-2)/2}}du/\log(n-2u^2)\bigr)$$, the mean of $$\log(n-2u^2)$$ under the density proportional to $$1/\log(n-2u^2)$$ on the candidate interval (the upper limit keeps $$n-2u^2\ge2$$, the convention of $$I(N)$$, avoiding the nonintegrable point $$n-2u^2=1$$), which is the profile a Bateman–Horn heuristic assigns to the prime representations. The definition is out-of-sample: the verification’s empirical lane mean over the observed prime representations is an estimator of $$\lambda_{\mathrm{an}}$$, used as a consistency check, not part of the definition. The law, coefficient-identifying as at Conjecture 4(i): on the contaminated classes

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

This is the calculus applied to a *representation* problem with norm-form contamination—the drift weight is carried by the arithmetic of $$\mathbb Q(\sqrt{-2})$$ rather than by a polynomial lane—and it comes with two provable null classes. On depth: an *asymptotic* for the contaminating count $$\#\{(q,k):q^2+2k^2=n,\ q\ \text{prime}\}$$, averaged over $$n$$, is a norm-form-with-prime-argument problem of genuine analytic difficulty (the same species as primes represented with restricted variables); $$D_{\mathrm{sys}}(n)$$ is *computed exactly per sample*, so the verification tests the transfer conjecture against the true census, not against an unproved averaged asymptotic. Verified on $$2{,}500$$ log-sampled odd $$n\le10^8$$ (mean $${\sim}330$$ representations each): contaminated strata pooled $$D=+0.27\pm0.33$$ against predicted $$D_{\mathrm{sys}}=+0.15$$ (at the $$\Lambda(q^2)$$ weight); null strata pooled $$-0.22\pm0.33$$, consistent with zero (one of the four strata sits at $$-2\sigma$$ individually, within a four-test family). (Stern’s exceptional list—the ten known odd integers that are not $$p+2k^2$$, the largest $$5993$$, with the seven prime members the Stern primes; completeness of the list is conjectural, OEIS A060003—is included as the attributed calibration benchmark anchoring this conjecture: no further exception occurs below $$10^9$$ in our computation.)

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

| $$\lambda$$ | observed, $$x=10^9$$ | predicted, $$x=10^9$$ | observed, $$x=4\times10^9$$ | predicted, $$x=4\times10^9$$ |
|---|---|---|---|---|
| $$1/2$$ | $$0.8241$$ | $$0.8189$$ | — | — |
| $$1$$ | $$0.7910$$ | $$0.7854$$ | $$0.7998$$ | $$0.7960$$ |
| $$2$$ | $$0.7527$$ | $$0.7520$$ | $$0.7670$$ | $$0.7646$$ |
| $$4$$ | $$0.7201$$ | $$0.7185$$ | — | — |

The residual $$\approx+0.003$$ sits at the scale of a $$1/\log^2x$$ term, consistent with the hedged reading at the statement.

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

For non-cube $$a\ge1$$ let $$C(a)=C(x^3+a)$$. Only $$p\equiv1\pmod3$$ moves the product, and the local root count there takes *three* values as $$a$$ varies mod $$p$$: $$\omega=3$$ with probability $$(p-1)/3p$$ ($$-a$$ a nonzero cube), $$\omega=1$$ with probability $$1/p$$ (the case $$p\mid a$$, easy to overlook and essential to the mean-value identity below), and $$\omega=0$$ with probability $$2(p-1)/3p$$; for $$p\equiv2\pmod 3$$ the cube map is a bijection and $$\omega=1$$ identically. Then: *(i)* [mean-value one, elementary lemma] $$\mathbb E_a[\omega(p)]=3\cdot\frac{p-1}{3p}+\frac1p=1$$ exactly at every $$p$$, so the derived mean of $$C(a)$$ is exactly $$1$$—the cubic analogue of the Korevaar–te Riele mean-value-one theorem for linear prime-pair constants, here a one-line computation at each finite level; passing the mean through the infinite product needs more than almost-sure convergence, and the needed ingredient is on hand: the convergent variance sum makes the partial products an $$L^2$$-bounded martingale (each factor has mean $$1$$ and is independent of the earlier ones), so they are uniformly integrable and the limit law has mean exactly $$1$$, not merely limit-of-means $$1$$; *(ii)* [limit law] the empirical law of $$\{C(a):a\le A,\ a\ \text{a non-cube}\}$$ converges, as $$A\to\infty$$, to the law of the random Euler product $$\prod_{p\equiv1(3)}f_p(\xi_p)$$ with the three-state local variables $$\xi_p$$ above—independent at any finite set of primes exactly, by CRT, with the infinite product’s tail controlled by the convergent variance sum (unlike the quadratic family of Conjecture 10(iii), no normalization is needed)—with derived standard deviation $$0.2762\ldots$$ computed from the full three-state law; *(iii)* [uniformity] $$\#\{n\le N: n^3+a \text{ prime}\} =C(a)I_a(N)(1+o(1))$$ uniformly over non-cube $$a\le(\log N)^B$$.

The framework here is Kowalski’s theory of averages of Euler products and singular-series distributions [11], which proves such limit laws for $$k$$-tuple singular series; the one-parameter cubic shift family, its exact mean-one lemma, and the short-range uniformity appear unstated, and we present (ii) as an instance-level law inside that framework rather than a new mechanism. Computational checks: derived moments (mean exactly $$1$$, sd $$0.2762$$) against the $$294$$ non-cube shifts $$a\le300$$: empirical mean $$1.0215$$ ($$+1.5$$ profile standard errors), sd $$0.2481$$ (finite-family tail correlations account for the sd gap: for $$p>a_{\max}$$ the residues of $$a$$ are not yet equidistributed); uniformity profile over $$57$$ shifts at $$N=2\times10^5$$: mean $$z=+0.09$$, spread $$0.72$$, $$\max\vert z\vert =2.31$$. (The single instance $$a=2$$, $$C=1.298435\pm0.0003$$, verified at $$10^7$$ with $$z=+0.32$$, is included as the calibration member; no statement of Bunyakovsky type is proven for any cubic, the nearest theorem being Heath-Brown’s $$x^3+2y^3$$ [3], which is what keeps the whole family conjectural.)

*Computational checks (the classical single instance).* At $$a=2$$ and bound $$10^{7}$$: observed $$287{,}956$$ against predicted $$287{,}784.8$$, ratio $$1.0006$$, $$z=+0.32$$; the family-profile verification across the $$57$$ shifts is reported above.

**Conjecture 16** *(Conjecture F as a family; the core is previously stated, [1], cf. [23]).*

For odd $$A$$ let $$Q_A(N)=\#\{n\le N:\ n^2+n+A \text{ prime}\}$$ and $$C(A)=C(x^2+x+A)$$. Then: *(i)* for every fixed $$B>0$$, $$Q_A(N)=C(A)\,I_A(N)\,(1+o(1))$$ uniformly over odd $$1\le A\le(\log N)^B$$; *(ii)* [window field] the residual field obeys the analogue of Conjecture 8(ii), kernel derived and probability space specified: for $$t$$ uniform on $$[N,2N]$$ and window length $$H\le N^{o(1)}$$, let $$Q_A(t;H)=\#\{t<n\le t+H:\ n^2+n+A \text{ prime}\}$$ (mean $${\asymp}H/2\log N$$, which sets the regime). Two members share the index window, so with $$C(A,A')=C(x^2+x+A,\ x^2+x+A')$$,

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

Numerical evaluation of the kernel (all odd $$A,A'\le99$$ at $$N=10^6$$: $$1{,}225$$ pairs, of which $$289$$ locally exclusive) returned a structurally clean answer: the positive correlations of admissible pairs and the negative correlations of exclusive pairs *cancel*, mean off-diagonal $$\rho=-0.003$$, so the derived *same-index* cross-member kernel is null. With the off-index sum at its correct order (larger, not smaller, than the same-index term), this cancellation does not license the conclusion that the members are asymptotically independent or that the observed profile variance $${\approx}0.37$$ must be diagonal; the natural reading remains that each $$\operatorname{Var}(Q_A)$$ is sub-Poisson through within-sequence pair correlations, the quadratic-family analogue of the Montgomery–Soundararajan deficit (Conjecture 13), but the off-index cross terms are an unevaluated competitor—and part of the spread is truncation noise in the constants themselves (the $$\pm10^{-3}$$ wobble moves each $$z_A$$ by $${\sim}0.3$$). Deriving the diagonal law and the off-index pinned sums is the family’s remaining open component, and the more important one; the numerical cancellation of the *same-index* cross-member kernel is a finite computation over $$A\le99$$, which localizes the deficit off the same-index diagonal without proving that the averaged kernel or the off-index contributions vanish—an analytic classification of the sign of $$C(A,A')-C(A)C(A')$$, and the evaluation of the two-parameter pinned sums, remain open. At $$N=10^6$$: mean ratio $$1.0006$$, standard deviation $$0.0027$$, $$\max\vert z\vert =1.92$$, rank correlation $$0.99988$$; for $$A=41$$, observed $$261{,}080$$ against predicted $$261{,}017.6$$ ($$z=+0.12$$, using Cohen’s constant). On precision: a truncated Euler product for $$C(41)$$ at cutoff $$2\times10^5$$ reads $$6.64092$$—wrong in the fourth significant decimal—because these conditionally convergent products drift at the $$10^{-3}$$ scale over practical cutoffs. Quoted digits for all quadratic-family constants in this paper are limited by the stated truncation wobble, not by the last printed digit. The entire $$10^8$$-bit primality dataset compresses to one product formula per $$A$$.

**Conjecture 17** *(Twin-member Goldbach, orientation-resolved; the basis conjecture and the integral kernel are Dubner’s [9]; the orientation decomposition apparently new).*

For even $$n$$ let $$R_T(n)$$ count ordered $$(a,b)$$, $$a+b=n$$, with $$a$$ and $$b$$ both members of twin pairs, each ordered role (lower/upper) counted. Each of the four role assignments is a $$4$$-form linear system in $$t=a$$ with root set $$\{0,\pm2\}\cup\{n,n\pm2\}$$-type mod each $$p$$, hence its own $$n$$-dependent singular series $$\mathfrak{S}_4^{(o)}(n)$$, and

$$
R_T(n)\;=\;\Bigl[\sum_{o}\mathfrak{S}_4^{(o)}(n)\Bigr]
\int_5^{n-5}\frac{dt}{\log^2t\,\log^2(n-t)}\;\bigl(1+o(1)\bigr),
$$

the four constants computed exactly per $$n$$ from the coincidence pattern of the root sets (which of $$n,n\pm2,n\pm4$$ each small prime divides). The error term is stated as $$(1+o(1))$$, not $$(1+O(1/\log n))$$: our own measurements show a second-order deficit whose $$1/\log n$$ coefficient is not yet pinned down (below). Two precision notes: the asymptotic runs over *varying* $$n$$, so what is assumed is a Hardy–Littlewood estimate for $$4$$-form systems *uniform in the $$n$$-dependent coefficients*—strictly stronger than the fixed-system conjecture—and the number $$5$$, the unique prime that is simultaneously a lower twin member (of $$(5,7)$$) and an upper one (of $$(3,5)$$), is double-counted consistently by the ordered-role convention, affecting finitely many representations per $$n$$ and no asymptotic.

Dubner’s paper already contains the integral kernel (his quotient $$\mu_4$$) and the qualitative basis conjecture; the content claimed here is the orientation-resolved singular series and its $$n$$-profile. Two exact identities compress the four orientations: the substitution $$t\mapsto n-t$$ exchanges the two summand roles, forcing $$\mathfrak{S}_4^{(\mathrm{lu})}(n)=\mathfrak{S}_4^{(\mathrm{ul})}(n)$$ identically (each of the $$(\mathrm{ll})$$ and $$(\mathrm{uu})$$ systems being self-dual under it), and the affine substitution $$t\mapsto t+2$$ gives $$\mathfrak{S}_4^{(\mathrm{uu})}(n)=\mathfrak{S}_4^{(\mathrm{ll})}(n-4)$$. So only one function of $$n$$ per symmetry class is free, and the profile is really two-dimensional; determining the average of $$\sum_o\mathfrak{S}_4^{(o)}(n)$$ over $$n$$ in closed form is a registered identity-hunting programme. Verified on $$150$$ log-sampled $$n\le10^8$$: the profile *shape* is confirmed at log-log correlation $$0.9993$$ across two decades, while the *level* runs at $$0.87$$ of prediction on $$[10^6,10^7)$$ and $$0.81$$ on $$[10^7,10^8)$$—a systematic deficit of second-order size ($${\approx}3.4/\log n$$ at the top range, the same order as the $$18$$–$$28\%$$ finite-height Poisson deficit of Conjecture 13), which we flag as the open component here rather than absorb into a fitted constant: either the $$4$$-tuple second-order correction accounts for it, or the orientation model needs repair, and the two are distinguishable at $$10^{10}$$. The *direction* of the trend is itself the anomaly: a genuine $$1-c/\log n$$ correction shrinks as $$n$$ grows, so a ratio moving *away* from $$1$$ across the decades indicates either a different error shape or a normalization problem, and settling which is part of what the open component must resolve. (The attributed benchmark stands inside the statement: every even $$n\ge4210$$ is a sum of two twin members, with the conjectured complete list of $$35$$ exceptions (OEIS A007534)—verified to $$10^8$$, re-swept to $$10^9$$, independently re-verified by a different algorithm, the same $$35$$ exceptions each time.)

## Instances and structural companions

**Conjecture 18** *(Contamination in prime triplets; apparently new).*

The contamination calculus of Conjecture 1(v) extends to $$k$$-tuples, and the triplet pattern $$(n,\,n+2,\,n+6)$$ is its first instance beyond pairs. Of the three configurations placing a prime square inside the pattern, two die algebraically for $$q>3$$—$$(q^2,q^2+2,q^2+6)$$ by $$3\mid q^2+2$$, and $$(q^2-6,q^2-4,q^2)$$ because $$q^2-4=(q-2)(q+2)$$ is composite (at $$q=3$$ the factorization is trivial, $$q^2-4=5$$ is prime, and the single bounded exceptional configuration $$(3,5,9)$$ occurs—one term, harmless to every asymptotic)—leaving the single *doubly-thinned* survivor $$(q^2-2,\ q^2,\ q^2+4)$$, which requires $$q^2-2$$ *and* $$q^2+4$$ simultaneously prime and forces $$q\equiv\pm2\pmod5$$ for $$q\neq5$$ (else $$5\mid q^2+4$$; at $$q=5$$ all three conditions do hold, the configuration being $$(23,25,29)$$, but its start $$23\equiv3\pmod5$$ lies outside the triplet start classes $$\{1,2\}$$, so the single term is harmless). Triplet starts lie in classes $$n\equiv1,2\pmod 5$$ (single bounded exception $$(5,7,11)$$, start $$\equiv0$$), and the surviving configuration has start $$q^2-2\equiv2$$: class $$2$$ is contaminated and class $$1$$ leads, in the drift-scale form of Conjecture 1(i):

$$
\mathcal{M}_x\!\left(
\frac{\bigl(\pi_3(t;5,1)-\pi_3(t;5,2)\bigr)\log^3t}{\sqrt t}\right)
\to c_3:=\lim_{x\to\infty}\frac{T_3(x)\log^3x}{\sqrt x},
\quad
T_3(x)=\frac1{\log^3x}\!\!
\sum_{\substack{q\le\sqrt x,\ q\neq5\\ q^2-2,\ q^2+4\ \mathrm{prime}}}
\!\!\log(q^2-2)\log q\,\log(q^2+4)
$$

($$c_3$$ exists and is the Bateman–Horn constant of the triple $$(q,\,q^2-2,\,q^2+4)$$, since the census sum is $$\sim c_3\sqrt x$$; convergence of the logarithmic mean at this normalization is the same Rubinstein–Sarnak-type structure hypothesis as at Conjecture 1(i); a normalization at the noise scale, $$\mathcal{M}_x\bigl((D-T_3)/\sqrt{\pi_3}\bigr)$$ with $$D$$ the class difference displayed above and $$\pi_3$$ the total triplet count to $$t$$, would be vacuous for the coefficient, exactly as at the pair races), with drift $$\asymp\sqrt x/\log^3x$$, one logarithm weaker than the pair races, and drift-to-noise $$\asymp\log^{-3/2}x$$ against their $$\log^{-1}$$, a scale the calculus itself predicts and the verification must respect. The mechanism clause and the averaging clause are asserted separately, as at Conjecture 1(i).

This is the calculus applied at tuple level: the configuration census, the double thinning, and the mod-5 class assignment are all forced, and the prediction was derived before the data were taken. At $$10^9$$: classes $$189{,}837$$ against $$189{,}670$$ ($$D=+167$$ on the predicted side; $$T_3=+25$$ against noise $$616$$, so the endpoint is uninformative exactly as the $$\log^{-3/2}$$ law requires), leadership log-density $$0.65$$ ($$+0.8$$ null standard deviations at the occupation constant of Conjecture 14(ii)—directionally consistent, sharpness unavailable at this height by the calculus’s own accounting). (The Chernick chain $$\{p,2p-1,3p-2\}$$—the population behind the universal-form Carmichael numbers, quantified by Dubner [10]—is included as an attributed calibration benchmark: $$C=2.858249$$, observed $$125{,}379$$ against predicted $$125{,}429.4$$ at $$3\times10^8$$, $$z=-0.14$$.)

*Computational checks.* The triplet-race data and the Chernick-chain calibration count are reported at the statement above.

**Conjecture 19** *(The contamination matrix: sexy pairs with two surviving orientations; apparently new).*

For the pattern $$(n,n+6)$$, *both* prime-square orientations survive, on complementary classes of $$q$$ mod $$5$$—the first matrix instance of the calculus (every pair race so far had exactly one): orientation $$A=(q^2-6,\,q^2)$$ requires $$q^2-6$$ prime, forcing $$q\equiv\pm2\pmod5$$ for $$q\neq5$$ (at $$q=5$$ the value $$19$$ is prime, but its start $$19\equiv4\pmod5$$ lies outside the sexy start classes $$\{1,2,3\}$$), and lands in start class $$3$$ (mod $$5$$), class $$3$$ (mod $$8$$); orientation $$B=(q^2,\,q^2+6)$$ requires $$q^2+6$$ prime, forcing $$q\equiv\pm1\pmod5$$ (the term $$q=5$$ falls outside the start classes), and lands in class $$1$$ (mod $$5$$), class $$1$$ (mod $$8$$). Sexy starts occupy classes $$\{1,2,3\}$$ mod $$5$$ and $$\{1,3,5,7\}$$ mod $$8$$; with $$T_{A}(x)=\frac1{\log^2x}\sum_{q^2-6\ \mathrm{prime},\,q\neq5}\log q\log(q^2-6)$$, $$T_{B}(x)=\frac1{\log^2x}\sum_{q^2+6\ \mathrm{prime},\,q\neq5}\log q\log(q^2+6)$$, and $$c_A,c_B$$ their drift-scale limits ($$c_A=\lim T_A\log^2x/\sqrt x$$, the Bateman–Horn constant of $$(q,q^2-6)$$, likewise $$c_B$$ for $$(q,q^2+6)$$), the predicted drift vector, in the drift-scale limiting-log-mean sense of Conjecture 1(i) (an $$\mathcal{M}_x$$-over-$$\sqrt\pi$$ normalization would be coefficient-blind), is, writing $$\pi(a)$$ for the number of sexy starts up to $$t$$ in class $$a$$ of the modulus in question: mod 5: $$\mathcal{M}_x\bigl((\pi(2)-\pi(3))\log^2t/\sqrt t\bigr)\to c_A$$, $$\mathcal{M}_x\bigl((\pi(2)-\pi(1))\log^2t/\sqrt t\bigr)\to c_B$$ (class $$2$$ *clean*); mod 8: $$\mathcal{M}_x\bigl((\tfrac12(\pi(5)+\pi(7))-\pi(3))\log^2t/\sqrt t\bigr)\to c_A$$, $$\mathcal{M}_x\bigl((\tfrac12(\pi(5)+\pi(7))-\pi(1))\log^2t/\sqrt t\bigr)\to c_B$$ (classes $$5,7$$ clean, mutually symmetric, with $$\mathcal{M}_x\bigl((\pi(5)-\pi(7))\log^2t/\sqrt t\bigr)\to0$$). Two independently computable drift constants, one certified null class per modulus. The mechanism clause and the averaging clause are asserted separately, as at Conjecture 1(i).

The matrix structure—two orientations feeding disjoint classes on complementary $$q$$-classes, with an interior null—is what distinguishes this from every single-orientation race, and it tests the calculus beyond its balanced one-mechanism cases; the class assignments were verified independently before the data were taken. At $$10^9$$ the predicted components ($$T_A=191$$, $$T_B=110$$) sit far inside the noise ($$\approx2{,}100$$), as the $$1/\log x$$ law forces; all four measured components and the $$5$$–$$7$$ control lie within one noise unit of their predictions (trivially, at this height), and the four leadership log-densities $$(0.48,0.56,0.53,0.73)$$ sit at $$(-0.1,+0.3,+0.1,+1.2)$$ null standard deviations (occupation constant $$0.18$$): three at the null, the mod-8 $$B$$-component mildly positive on the predicted side. The matrix is *registered and consistent*, with sharpness unavailable below $${\sim}10^{14}$$ by the calculus’s own accounting. (The pair $$\{p,\ p^2-2\}$$, OEIS A062326, $$C=3.383216$$, the input that sets Conjecture 1’s drift scale, is included as an attributed calibration benchmark: verified at $$10^7$$, $$z=-1.31$$, independently recomputed to $$10^9$$; a refutation of its infinitude would remove the twin race’s predicted mechanism.)

*Computational checks.* The sexy-pair race data are reported at the statement above; independent recomputation of this conjecture’s calibration member, the pair $$\{p,p^2-2\}$$, gave $$3.383227$$, with primes to $$10^9$$—inside our stated wobble—and an independent count to $$3\times10^7$$ with final ratio $$0.9965$$.

**Conjecture 20** *(Fibonacci–Lucas twins: the convergent side stress-tested; the object is OEIS A080327).*

*(i)* [rank-disjointness, elementary, with its exception stated] every *odd* prime factor $$r$$ of $$L_p$$ has rank of apparition exactly $$2p$$ (from $$z(r)\mid2p$$, $$z(r)\nmid p$$, and $$z(r)=2$$ being impossible), and every prime factor of $$F_p$$ ($$p\neq5$$ prime) has rank exactly $$p$$: the odd divisor pools of the two numbers are disjoint. The prime $$2$$ is the unique exception: $$2$$ divides both $$F_p$$ and $$L_p$$ precisely when $$p=3$$ ($$F_3=2$$, $$L_3=4$$; $$\gcd(F_p,L_p)=2$$ iff $$3\mid p$$)—the restriction to odd divisors is essential, the clause being false at $$p=3$$ without it. Disjoint pools remove shared-*prime* correlation but not all correlation: dependence can still enter through the order structure of the recurrence, which is why (iii) matters; *(ii)* [finiteness] only finitely many primes $$p$$ have $$F_p$$ and $$L_p$$ simultaneously prime; *(iii)* [calibration clause, quantitative] the naive joint accounting—probability $$(\mathrm{e}^{\gamma}\log p/(p\log\phi))^2$$ per index—assigns prior mass about $$1.4\times10^{-2}$$ to the whole index range beyond $$10^4$$, in which the catalogued index $$p=148091$$ falls (OEIS A080327; *both* $$F_p$$ and $$L_p$$ are *probable* primes—numbers of roughly $$30{,}950$$ digits, with Lucas numbers proved prime only up to index $$56003$$—so everything recorded here is conditional on both probable-prime classifications, for which no Baillie–PSW pseudoprime is known: no unconditional refutation is claimed from uncertified numbers). That rare-event datum is recorded descriptively, with no significance claim attached to it: the model was examined after the event was known, and no test protocol was fixed in advance. A single surprising event is not a strict refutation, and it does not by itself estimate the *size* of the correction: an underestimated constant, genuine cross-dependence, and a mis-calibrated finite-range tail are competing explanations that one event cannot separate. What the datum does bear on (conditionally as above) is not the model but the list: it is fatal to any Goldilocks completeness list; the conjectural content of (ii) is that even the corrected accounting has convergent sum.

This conjecture is our stress test of the convergent Borel–Cantelli template that Conjecture 21 exemplifies. The joint scan to $$p\le10^4$$ found exactly the indices $$\{5,7,11,13,17,47\}$$, with expected further mass $$1.4\times10^{-2}$$, while the catalogued index $$148091$$, at which $$F_p$$ and $$L_p$$ are both probable primes, lies beyond that range. We therefore conjecture finiteness *without* a completeness clause. The lesson, in the language of Grantham–Granville [7], is that recurrence-sequence constants need their local corrections *before* tail masses are trusted. The single-sided calibration (probable-prime counts: $$F_p$$ and $$L_p$$ leave the deterministic range at very small $$p$$): $$25$$ Fibonacci prime indices $$\le10^4$$ against the naive screening prediction $$29.2$$ (the finite sum of the declared per-index hazard over primes to $$10^4$$) ($$z=-0.8$$, a mild deficit, not significant on its own); $$29$$ Lucas prime indices $$\le10^4$$; the corrected $$c_F$$ needs a Granville-type patch, and clause (iii) quantifies the same need at the joint level.

*Computational checks.* Joint scan and single-sided calibration reported at the statement (Fibonacci prime indices $$\{3,5,7,\dots,9311,9677\}$$, $$25$$ of predicted $$29.2$$, $$z=-0.78$$; Lucas indices $$29$$; joint $$\{5,7,11,13,17,47\}$$ to $$10^4$$)—probable-prime counts at all but the smallest indices, the Fibonacci and Lucas values leaving the deterministic range almost at once.

**Conjecture 21** *(Factorial twins; the uniqueness core is previously stated, OEIS A088054; clauses (i) and (iii) are ours).*

*(i)* [window rigidity, elementary] for $$n\ge4$$ and $$2\le\vert a\vert \le n$$ the number $$n!+a$$ is composite (any prime factor $$p$$ of $$a$$ satisfies $$p\le n$$, so $$p\mid n!+a$$, and $$n!+a>n\ge p$$); the two small anomalies $$2!-2=0$$ and $$3!-3=3$$ are the only exceptions, which is why the clause is restricted to $$n\ge4$$. Hence among all offsets of bounded size the only candidates for primality near $$n!$$ are $$a=\pm1$$: the twin question below is the *unique* bounded-offset constellation question at $$n!$$, and every admissible offset set is a subset of $$\{-1,+1\}$$. *(ii)* [uniqueness; previously stated] Only finitely many $$n$$ have $$n!-1$$ and $$n!+1$$ simultaneously prime, and the complete list is $$n=3$$: i.e. $$6=3!=3\#$$ is the unique factorial lying between twin primes. *(iii)* [joint fluctuation model] the two single-sided counts $$F_{\pm}(N)=\#\{n\le N:\ n!\pm1 \text{ prime}\}$$ are each $$\sim\mathrm{e}^{\gamma}\log N$$ and, *under the independent-indices model stated below*, asymptotically independent, with $$F_{+}-F_{-}$$ normalized by $$\sqrt{2\mathrm{e}^{\gamma}\log N}$$ asymptotically standard normal. The probability space is declared: the clause is about a random model in which the events $$E_n^{\pm}=\{n!\pm1\ \text{prime}\}$$ carry the Caldwell–Gallot marginal hazards $$\mathrm{e}^{\gamma}/n$$ with an *unspecified* dependence structure, and the Gaussian limit is asserted under three explicit hypotheses on that structure: the same-index bound $$\sum_{n\le N}\bigl\vert \operatorname{Cov}(\mathbf 1_{E_n^+},\mathbf 1_{E_n^-})\bigr\vert =o(\log N)$$, which pins the variance at $$2\mathrm{e}^{\gamma}\log N\,(1+o(1))$$ and which the joint law $$\sim(\mathrm{e}^{\gamma}/n)^2$$ derived below supplies with a convergent sum—without it the remaining hypotheses leave the second cumulant free, and a model with $$\Pr(E_n^+\cap E_n^-)=\mathrm{e}^{\gamma}/2n$$ halves the limiting variance; the cross-index covariance bound $$\sum_{m<n\le N}\bigl\vert \operatorname{Cov}(\mathbf 1_{E_m}, \mathbf 1_{E_n})\bigr\vert =o(\log N)$$ over the four sign pairs (the variance itself is $$\asymp\log N$$), *and*—since pairwise control alone cannot preclude higher-order dependence—the higher-cumulant condition $$\kappa_r(F_+-F_-)=o\bigl((\log N)^{r/2}\bigr)$$ for each fixed $$r\ge3$$, the method-of-moments sufficient condition. None of the three is imported from an independence model; whether they hold for the arithmetic dependence across factorial indices is the open component of this clause.

Each event separately has Caldwell–Gallot probability $$\sim\mathrm{e}^{\gamma}/n$$ [4] and divergent sum (the $$n!+1$$ side is the classical law retained as calibration at Conjecture 2); the *joint* event has probability $$\sim(\mathrm{e}^{\gamma}/n)^2$$, whose sum converges. This is our exemplar of the convergent side of the Borel–Cantelli dichotomy—the accounting that predicts finitude rather than infinitude. The at-a-common-index independence in (iii) has a derivation: a generic twin pair near $$n!$$ would carry the Hardy–Littlewood twin factor $$2C_2\prod_{2<p\le n}\frac{p-2}{p-1}\big/ \prod_{2<p\le n}\bigl(\tfrac{p-1}p\bigr)^{\!2}$$-type couplings, but here the screening (coprimality to all $$p\le n$$) is *deterministic*—both neighbours always pass it—and the twin coupling factor and the reciprocal sieve factors cancel to first order, leaving the joint probability $$\sim(\mathrm{e}^{\gamma}/n)^2$$ with no singular-series correlation; what remains open, and is flagged in (iii), is dependence *across* distinct indices $$n$$, whose divisibility structures are nested. That open component has a concrete first computation, which we register as a programme: for $$m<n$$ and a prime $$p>n$$, the residues $$m!\bmod p$$ and $$n!\bmod p$$ are deterministically linked by $$n!=m!\cdot(m{+}1)\cdots n$$, so the covariance of the events $$p\mid m!\pm1$$ and $$p\mid n!\pm1$$ is an explicit character-sum average over the multiplier $$(m{+}1)\cdots n$$; summing it over $$p$$ either bounds the cross-index dependence at $$o(1/n)$$—vindicating the independent-indices model—or exhibits genuine coupling, and the computation is finite at each height. Verified for $$n\le700$$ ($$F_+=15$$, $$F_-=16$$: difference $$-1$$ against noise scale $$\approx4.8$$); the model-expected number of further twin examples beyond $$700$$ is $$\mathrm{e}^{2\gamma}/700\approx4.5\times10^{-3}$$ (computed tail). The defensible core is finiteness; the exact one-element list is the Goldilocks-maximal form—strictly stronger than the tail estimate can guarantee. On priority: the exact uniqueness conjecture is on the public record, OEIS A088054 stating that $$3$$ is conjecturally the intersection of A002981 and A002982, so clause (ii) is attributed there and our contribution here is clauses (i) and (iii).

The primorial analogue—$$p\#\pm1$$ both prime only for $$p\in\{3,5,11\}$$—is due to Lillie [5], whose abstract gives both the $$O(n^{-2})$$ joint probability and the prediction that there are three instances in total; it is included here as an attributed calibration benchmark, independently verified to $$p\le4000$$.

*Computational checks* (probable-prime count for $$n$$ beyond about $$26$$). Exhaustive to $$n\le700$$: the only factorial twin is $$n=3$$; individually, $$n!+1$$ is prime for $$n\in\{2,3,11,27,37,41,73,77,116,154,320,340,399,427\}$$ and $$n!-1$$ for $$n\in\{3,4,6,7,12,14,30,32,33,38,94,166,324,379,469,546\}$$—two divergent single-sided laws straddling their shared constant while the joint count stops at one, the convergent accounting in action. (The primorial companion, attributed to Lillie [5]: exhaustive to $$p\le4000$$, twins exactly $$\{3,5,11\}$$, with $$p\#+1$$ prime for eleven $$p$$ against the Caldwell–Gallot prediction $$12.4$$, $$z=-0.40$$; again a probable-prime count above the deterministic range.)

**Theorem 1** *(Cube obstruction).*

For $$k\ge2$$, the cube $$k^3$$ is representable as $$p+j^3$$ with $$p$$ prime, $$j\ge1$$, if and only if $$3k^2-3k+1$$ is prime. Consequently the set of integers not representable as $$p+k^3$$ is infinite: the non-representable *cubes* alone have counting function $$\sim x^{1/3}$$. (That the full exceptional set is $$\sim x^{1/3}$$ follows only when combined with Conjecture 22(iii), and is conjectural.)

*Proof.* $$k^3-j^3=(k-j)(k^2+kj+j^2)$$; for $$1\le j\le k-2$$ both factors exceed $$1$$, so the difference is composite. The only candidate is $$j=k-1$$, giving $$3k^2-3k+1$$. Since $$3k^2-3k+1$$ is composite for a density-one set of $$k$$ (all but $$O(K/\log K)$$ of $$k\le K$$, by an upper-bound sieve of Brun or Selberg type applied to the quadratic’s prime values), all but a vanishing proportion of cubes are unrepresentable. $$\square$$

The restriction to non-cubes in the next conjecture is therefore essential: the exception set of $$n=p+k^3$$ over *all* $$n$$ is infinite, and the cubes are exactly what makes it so. The effect is visible immediately in the data—all $$412$$ exceptions found in $$(10^8,10^9]$$ are perfect cubes—and it is invisible to a Borel–Cantelli sum taken over all $$n$$, since the cubes have density zero. The cube lane is not lost, only relocated: by Theorem 1 it is governed by the primality of $$3k^2-3k+1$$, which is a Bateman–Horn family in its own right and appears as such in Conjecture 22.

**Conjecture 22** *(The boundary trichotomy for polynomial ladders; the divisibility principle is classical and its cubic case is Cunningham’s cuban observation (OEIS A002407); the family classification is apparently new).*

For $$F\in\mathbb Z[x]$$ with $$\deg F\ge2$$ and *positive leading coefficient*, and $$m>j\ge1$$, $$(m-j)\mid F(m)-F(j)$$ (textbook), and the divided difference $$(F(m)-F(j))/(m-j)$$—whose leading form is then positive on the cone $$m>j\ge1$$—exceeds $$1$$ outside an effectively bounded region; so $$F(m)-F(j)$$ prime forces $$m-j=1$$ apart from finitely many exceptional pairs (for the family below the exceptional set is provably *empty*). Both hypotheses are necessary: for $$\deg F=1$$ the cofactor can be identically $$1$$ and the collapse fails, and for negative leading coefficient the divided difference tends to $$-\infty$$ on the cone, so the “exceeds $$1$$” clause would be false as stated (one may equivalently keep general sign and read the claim through $$\vert F(m)-F(j)\vert$$). Every representation problem $$F(m)=p+F(j)$$ in this range thus collapses to the boundary polynomial $$D_F(m)=F(m)-F(m-1)$$. The content is the classification of the boundary lanes. For $$F=x^3+cx$$, $$c\ge0$$: *(i)* [trichotomy, elementary] $$D_F=3m^2-3m+1+c$$ and the lane is *dead-parity* for $$c$$ odd ($$D_F$$ always even), *dead-3-adic* for even $$c\equiv2\pmod3$$ ($$3\mid D_F$$ always), and admissible exactly for $$c\equiv0,4\pmod6$$; *(ii)* [uniform boundary law] over the admissible lanes, $$\#\{m\le M: D_F(m) \text{ prime}\}\sim C(D_F)\,I(M)$$ uniformly for $$c\le(\log M)^B$$—a Bateman–Horn family whose members are indexed by the ladder classification; *(iii)* [attributed core] the case $$c=0$$ is the cuban ladder: Cunningham’s classical observation that a prime difference of cubes forces consecutive arguments, with the non-cube exceptional set of $$n=p+k^3$$ finite (Hardy–Littlewood’s $$E_3(X)=O(1)$$ [1]).

The reducible-boundary phenomenon is part of the same classification: $$F=x^4$$ has $$D_F=(2m-1)(2m^2-2m+1)$$—the boundary lane itself factors, which is precisely the composite-$$k$$ obstruction of Conjecture 23 seen from the ladder side, and $$F=x^3+x^2$$ gives $$D_F=m(3m-1)$$, dead by reducibility. Verified: the collapse is algebraically empty for $$x^3+cx$$ ($$c\ge0$$), the trichotomy checked to $$m=5000$$ on all $$c\le12$$, and the two smallest admissible new lanes counted at $$M=10^6$$: $$c=4$$ ($$C=2.12956$$, $$z=+0.27$$) and $$c=6$$ ($$C=2.68954$$, $$z=-0.92$$). (Empirically the non-cube exception census of (iii) by decade is $$4,\,27,\,168,\,763,\,2011,\,2808,\,1181,\,88$$ up to $$10^8$$, peaking at the sixth decade and collapsing thereafter, largest found $$78{,}526{,}384$$.)

**Conjecture 23** *(The power-obstruction ladder: an elementary structural proposition with a Bateman–Horn corollary; apparently new as a family).*

For $$k\ge2$$ and $$m\ge2$$, write $$D_k(m)=m^k-(m-1)^k$$, and call $$m^k$$ representable if $$m^k=p+j^k$$ for some prime $$p$$ and $$j\ge1$$. Then: *(i)* [theorem] for *composite* $$k$$, no $$k$$-th power is representable: if $$r$$ is a proper divisor of $$k$$ with $$r>1$$ (such $$r$$ exists precisely because $$k$$ is composite; the excluded value $$r=1$$ would allow only the useless factor $$m-j=1$$ at $$j=m-1$$), then for every $$1\le j<m$$ the difference $$m^k-j^k$$ has the proper factor $$m^r-j^r>1$$ with cofactor $$>1$$; *(ii)* [elementary] for *prime* $$k$$ (including $$k=2$$), $$m^k$$ is representable if and only if $$D_k(m)$$ is prime; and $$D_k$$ is irreducible for prime $$k$$ (a root $$\alpha$$ has $$(\alpha/(\alpha-1))^k=1$$ with $$\alpha/(\alpha-1)\neq1$$, so $$\zeta=\alpha/(\alpha-1)$$ is a primitive $$k$$-th root of unity and $$\mathbb Q(\alpha)=\mathbb Q(\zeta)$$ has degree $$k-1=\deg D_k$$, forcing irreducibility; explicitly $$D_k(x)=(x-1)^{k-1}\,\Phi_k(x/(x-1))$$. The forcing $$j=m-1$$ needs only $$k\ge2$$); *(iii)* [conjecture] for each prime $$k\ge3$$ the representable lane follows Bateman–Horn ($$k=2$$ is a theorem, the prime number theorem on the lane $$2m-1$$): $$\#\{m\le M:\ D_k(m) \text{ prime}\}\sim C_k\int_2^M dt/\log D_k(t)$$.

The dividing line is prime versus composite $$k$$, not odd versus even: for *odd* composite $$k=rs$$ the factorization of clause (i) applies verbatim, so that $$D_9(m)$$, for instance, is *never* prime. This was checked directly for $$k=9,15,21,25,27,33$$—no prime value of $$D_k$$ occurs up to $$m=2000$$, and the predicted divisor $$D_r(m)\mid D_k(m)$$ is present identically—and it is the same algebraic mechanism, seen from the ladder side, that Theorem 1 exhibits for cubes. The family generalizes the cubic case $$k=3$$ of Conjecture 22.

*Computational checks.* The even-rung theorem was checked numerically to $$10^8$$ (no fourth power is $$p+j^4$$); the three verifiable Bateman–Horn lanes $$k=2,3,5$$ (constants $$2$$ exactly, $$3.36181$$, and $$3.67770\pm0.007$$, the quartic product computed by brute-force root counts to $$10^5$$) all sit within $$\vert z\vert <0.6$$: at bound $$10^{7}$$ the lane $$k=2$$ gives observed $$1{,}270{,}606$$ against predicted $$1{,}270{,}902.8$$ (ratio $$0.9998$$, $$z=-0.26$$); at $$10^{6}$$ the lane $$k=3$$ gives $$126{,}826$$ against $$126{,}641.6$$ (ratio $$1.0015$$, $$z=+0.52$$); and at $$8\times10^{5}$$ the lane $$k=5$$ gives $$56{,}925$$ against $$57{,}021.3$$ (ratio $$0.9983$$, $$z=-0.40$$).

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

*Added to the deposit: 3 August 2026.*

The twenty-five conjectures below are organized by mechanism rather than by the contamination calculus of Part I. Each names a canonical object and averaging law, identifies an arithmetic, geometric, spectral, or adelic source, and states a first decisive theorem and a failure mode.

### Programme I: connected prime-pattern fields

Let $$H\subset\mathbb Z$$ be finite and admissible, and write

$$
\Lambda_H(n)=\prod_{h\in H}\Lambda(n+h),\qquad
 Y_H(x,L)=\sum_n w\!\left(\frac{n-x}{L}\right)
 \bigl(\Lambda_H(n)-\mathfrak S(H)\bigr),
$$

where $$w$$ is a fixed smooth compactly supported function and $$\mathfrak S(H)$$ is the Hardy–Littlewood singular series $$\prod_p(1-\nu_H(p)/p)(1-1/p)^{-\vert H\vert }$$, with $$\nu_H(p)$$ the number of residue classes occupied by $$H$$ modulo $$p$$. The window position $$x$$ is sampled from $$[X,2X]$$ with density $$dx/(x\log2)$$ and $$X^\varepsilon\le L\le X^{1-\varepsilon}$$. For translated motifs $$H_i+t_i$$, their *exact overlap type* records every equality among shifted prime constraints. The connected singular series $$\mathfrak S^{\mathrm c}(K_1,\ldots,K_r)$$ is obtained by Möbius inversion over set partitions of the indexed tuple $$(K_1,\ldots,K_r)$$.

**Connected motif generating functional (Conjecture 26).** Fix admissible motifs $$H_1,\ldots,H_m$$ and put

$$
\mathcal Z_{X,L}(\mathbf z)=
 \mathbb E_x\exp\!\left(\sum_{i=1}^m z_iY_{H_i}(x,L)\right).
$$

For every fixed total degree $$R$$, the degree-$$\le R$$ Taylor polynomial of $$\log\mathcal Z_{X,L}$$ has a uniform asymptotic expansion indexed by connected exact-overlap diagrams of at most $$R$$ translated motifs. A diagram whose coincidence hypergraph connects the $$r$$ translated sets $$H_{i_1}+t_1,\ldots,H_{i_r}+t_r$$ contributes, at the leading order of its stratum,

$$
W_\tau(L;\mathbf t)\,
 \mathfrak S\Bigl(\bigcup_{j=1}^r(H_{i_j}+t_j)\Bigr)
 \prod_v(\log X)^{m_v-1},
$$

where $$W_\tau(L;\mathbf t)=L\int_{\mathbb R}\prod_{j=1}^rw(u+t_j/L)\,du$$ is the archimedean window-overlap weight of the diagram and $$m_v$$ is the multiplicity of the prime constraint at $$v$$: any set partition that separates a coincidence loses at least one factor of $$\log X$$, so the Möbius alternation leaves the single-block moment as the leading term of a connected diagram. The same alternation cancels the leading terms of disconnected diagrams, whose contribution is carried by the connected singular series of their disjoint blocks at strictly smaller logarithmic order, reducing for the fully disjoint type to $$\mathfrak S^{\mathrm c}(H_{i_1}+t_1,\ldots,H_{i_r}+t_r)$$ with no logarithmic enhancement. The log powers are therefore partition dependent and are never factored across the alternation, and every prime-power counterterm is included in the local weight attached to its multiplicity. Ordering terms lexicographically by powers of $$L$$ and $$\log X$$, the remainder after any fixed truncation is smaller than the last retained scale, uniformly in the mesoscopic range.

*Significance.* This is a multitype connected field theory for prime constellations. It simultaneously organizes covariance, odd moments, mixed motifs, overlap singularities, and lower-order prime-power effects. Montgomery–Soundararajan and Kuperberg provide the closest one-field moment frameworks, while constrained singular-series sums provide the nearest local input [19, 34, 35]. The new content is the complete connected multitype functional. The first decisive theorem is the full third-cumulant formula for two distinct pair motifs. A failure would reveal a term of $$\log\mathcal Z_{X,L}$$ at a scale indexed by no connected exact-overlap diagram, a correlation source among the motif fields $$Y_{H_i}(x,L)$$ invisible to the Möbius alternation over set partitions.

**Complete overlap-renormalization filtration (Conjecture 27).** Fix a finite motif family $$H_1,\ldots,H_m$$. Apply the degree-two specialization of Conjecture 26 and order all of its connected covariance strata by their asymptotic scales $$s_1\succ s_2\succ\cdots$$ (lexicographically in powers of $$L$$, $$\log X$$, and the renormalized disjoint scales). In the mesoscopic range scales sharing the same total power of $$L$$ and of logarithms differ only by powers of $$\theta=\log L/\log X$$ and merge into a single stratum whose limiting form is polynomial in $$\theta$$. The filtration, the graded convergence, and the eigenvalue asymptotics below are asserted for every fixed $$\theta\in(\varepsilon,1-\varepsilon)$$. Recursively subtract the earlier strata and let $$A_\nu=A_\nu(\theta)$$ be the limiting covariance form at scale $$s_\nu$$, and put

$$
\mathcal W_\nu=\bigcap_{\mu<\nu}\ker A_\mu.
$$

Each $$A_\nu$$ is asserted to induce a nondegenerate form on the graded quotient $$\mathcal W_\nu/\mathcal W_{\nu+1}$$ for every such $$\theta$$, so that $$\mathcal W_{\nu+1}=\mathcal W_\nu\cap\ker A_\nu$$ and the filtration does not collapse.

For every fixed truncation of this ordered diagram expansion, the spectral projections of the covariance matrix converge to the associated graded spaces $$\mathcal W_\nu/\mathcal W_{\nu+1}$$, and every eigenvalue whose first nonzero term occurs within the truncation is asymptotic to $$s_\nu$$ times a positive eigenvalue of the induced form $$A_\nu$$. Vectors annihilating all retained forms pass canonically to the next connected diagram scales of Conjecture 26.

Consequently every asymptotic variance scale of a finite motif statistic is generated by a connected overlap or renormalized disjoint diagram from Conjecture 26, and no scale external to that diagrammatic expansion occurs. The filtration is invariant under replacing the motif family by one with isomorphic exact-overlap incidence algebra and identical local Euler weights.

*Significance.* The claim classifies all mechanisms by which a finite linear combination of prime motifs can become rigid. It predicts a canonical renormalization filtration, not merely one variance formula, and gives an algorithm for constructing observables that expose deeper arithmetic strata. A counterexample would identify a genuinely new source of rigidity outside overlap and disjoint correlation. The first theorem is a three-motif example in which one overlap form has a rational kernel and the next form is nondegenerate on it.

**Regularized mesoscopic local–spectral trace formula (Conjecture 28).** Fix motifs $$H_i,H_j$$, a Schwartz function $$\phi$$ with $$\phi(0)=0$$, an even cutoff $$\eta\in C_c^\infty(\mathbb R)$$ with $$\eta=1$$ near the origin, and an even mollifier $$\kappa\in C_c^\infty(\mathbb R)$$ of integral one. Let $$Q^{\mathrm{loc}}_{ij}(\phi;L)$$ be the exact-overlap-renormalized singular-series form

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

*Significance.* The spectral side is a finite smooth expression before any products are taken, and regularization independence is part of the conjecture rather than an implicit convention. The statement extends the Goldston–Montgomery and Chan prime/zero equivalence from one prime-counting field to products of shifted von Mangoldt functions [54, 33]. Failure can occur in two mathematically different ways: a missing mesoscopic covariance functional, or a genuine regularization anomaly. The first decisive theorem is the pair-motif covariance with one factor unshifted and two independent admissible mollifiers.

**Anchored arithmetic polymer expansion for prime motifs (Conjecture 29).** Fix an admissible motif $$H$$ of size $$k$$. A finite set $$A\subset\mathbb Z$$ of occurrence starts is a polymer when $$0\in A$$, the overlap graph on $$A$$ is connected, and $$U_A=\bigcup_{t\in A}(H+t)$$ is admissible. Define its *anchored codimension*

$$
d_H(A)=\vert U_A\vert -\vert H\vert ;
$$

this is the number of new prime constraints beyond the occurrence anchored at $$0$$. In the regularized spectral model of Conjecture 28, let $$Z$$ be the limiting low-mode vector (the joint limit, asserted as part of this conjecture, of the mode integrals of the Conjecture 28 functional against frequencies below a fixed cutoff $$K$$ on the $$L$$-scale, the Conjecture 28 limits taken first and $$K\to\infty$$ last), let $$\lambda(t\mid Z)$$ be the conditional one-point occurrence intensity, and set

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

The set $$\mathcal T_H$$ is symmetric under $$t\mapsto-t$$, and the cluster-start fraction counts, for each occurrence, only whether it has an overlapping predecessor, so the sum is restricted to $$t<0$$ and equals half the symmetric sum over $$\mathcal T_H$$. If no admissible overlap exists, $$\theta_X(H)=1+o((\log X)^{-M})$$ for every fixed $$M$$. Higher corrections are the connected Ursell sums (the signed connected sums of cluster-expansion theory) of anchored polymers ordered by $$d_H(A)$$. These finite-$$X$$ Gibbs expansions are projectively consistent and subcritical, and after division by the low-zero intensity the cluster-start process is Poisson to each fixed order of this triangular expansion.

*Significance.* The relevant rarity is the number of new constraints after one occurrence is given, not the enhancement relative to a product of all one-point intensities. For two translates sharing $$s$$ of the $$k$$ prime positions, the Palm scale is $$(\log X)^{-(k-s)}$$. A universal $$1/\log X$$ correction therefore holds only for special motifs, such as pair motifs that admit an overlapping translate. The law keeps polymers of every size, supplies a canonical extremal-index exponent $$\delta(H)$$, and links Hardy–Littlewood constants, low-zero environments, Palm theory, and extreme motif gaps. For $$H=\{0,6\}$$ one has $$\delta(H)=1$$ and the pair-motif coefficient is recovered. The first decisive theorem is the two-element polymer law for one pair motif, the Palm limit at $$A=\{0,t\}$$ with $$t\in\mathcal T_H$$ together with the expansion of $$\theta_X(H)$$ at order $$(\log X)^{-\delta(H)}$$. A failure would show that the low-mode environment $$Z$$ supplies more than the one-point intensity, so connected Palm activities would not be graded by $$(\log X)^{-d_H(A)}$$ and weighted by $$\mathfrak S(U_A)$$ alone.

**Topological expansion of non-Gaussian prime cumulants (Conjecture 30).** For every connected exact-overlap diagram in Conjecture 26, expand its connected singular series over the linking primes and form the linkage graph of each term, whose vertices are the motif occurrences and whose edges join two occurrences sharing a linking prime in that term. Let $$g$$ be the first Betti number of the linkage graph. Once all larger coincidence strata have been subtracted, the total contribution of the terms of Betti number $$g$$ is smaller than that of the spanning-tree terms with the same external motifs by at least $$(\log L)^{-g}$$. The complete leading coefficient at each logarithmic order is the sum of the linked-term weights with the corresponding Betti number. In particular, the first nonzero odd cumulant of a balanced motif statistic, a combination $$Y_c$$ whose coefficient vector annihilates every coincidence-stratum form of Conjecture 27, is carried by incidence trees. For the single-prime field the fully spread connected part $$\kappa^{\mathrm{sp}}_{2m+1}$$, defined by subtracting every coincidence stratum as in Conjecture 27, obeys

$$
\kappa^{\mathrm{sp}}_{2m+1}=(c_m+o(1))L^m(\log L)^{m+1},
$$

where $$c_m$$ is the total connected tree weight. The raw cumulant adds the explicit coincidence diagrams of Conjecture 26, which carry powers of $$\log X$$ and are computable term by term, so the tree law is a statement about the spread diagrams, exactly the regime of Kuperberg’s singular-series sums.

*Significance.* This predicts a topological genus expansion for prime statistics: every independent cycle costs a logarithmic order. Kuperberg’s odd-moment conjecture is the one-field calibration, and the incidence-homology filtration with its motif-dependent coefficients is the new mechanism [34]. The first theorem is the case $$m=1$$ for the single-prime field, the spread third-cumulant tree law $$\kappa^{\mathrm{sp}}_{3}=(c_1+o(1))L(\log L)^{2}$$ with its one-cycle terms suppressed by $$(\log L)^{-1}$$. A failure would show that logarithmic suppression is controlled by an arithmetic invariant not visible in diagram topology.

### Programme II: arithmetic first-arrival fields and class groups

For a prime modulus $$q$$ and $$a\in\mathbb F_q^\times$$, let $$p(q,a)$$ be the least prime in the class $$a$$ and put

$$
T_q(a)=\frac{\operatorname{Li}(p(q,a))}{q-1},\qquad
 \mathcal N_{q,a}=\sum_{p\equiv a\, (q)}
 \delta_{\operatorname{Li}(p)/(q-1)}.
$$

The probability space chooses $$q$$ uniformly among primes in $$[Q,2Q]$$ and then chooses $$a$$ uniformly from $$\mathbb F_q^\times$$.

**Connected first-arrival functional (Conjecture 31).** Let $$w^{\mathrm c}_{r,Q}$$ be the connected factorial-cumulant measure of the random point process $$\mathcal N_{q,a}$$. For every fixed $$r\ge2$$ there is a signed measure $$K_r$$, locally finite on the off-diagonal region $$\{u\in\mathbb R_+^r:u_i\ \text{distinct}\}$$, such that, on that region (the diagonal strata carry strictly smaller normalizations, as in the stratification of Conjecture 26, and are excluded here),

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

*Significance.* This is an arithmetic point-process theory of least primes. The coupon-collector model of Li–Pratt–Shakan supplies the nearest extremal analogy, but not a connected Laplace functional [36]. Truth would determine waiting times, occupancy covariance, cover times, and terminal clustering from one hierarchy. The first theorem is the existence and explicit evaluation of $$K_2$$ on compact off-diagonal sets. A failure would show that least primes in residue classes cluster through a mechanism not captured by modulus-averaged connected Hardy–Littlewood densities, a connected correlation of $$\mathcal N_{q,a}$$ living outside the hierarchy $$(K_r)_{r\ge2}$$.

**Tested Gauss-polyspectral reciprocity for the least-prime field (Conjecture 32).** Set $$T_q(0)=\operatorname{Li}(q)/(q-1)$$ and centre the resulting field $$f_q$$ on all of $$\mathbb F_q$$. Let $$\mathbf A_q$$ and $$\mathbf M_q$$ be its complete additive and multiplicative Fourier coefficient vectors, including the explicit rank-one coordinate needed to record the value at $$0$$. There is then an explicit invertible Gauss matrix $$U_q$$ with

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

The conjectural content is that, after normalization by the first nonzero connected scale, tests supported on additive zero-sum tensors converge to contractions of the Fourier transforms of the arrival kernels $$K_r$$ from Conjecture 31. Transporting those tests fibrewise by the exact Gauss matrices and only then taking the modulus average gives the same limits as the corresponding multiple explicit-formula correlations of Dirichlet $$L$$-function zeros. The two descriptions determine the same continuous multilinear functional on the completion of the tested tensor class.

*Significance.* The elementary input is the finite Gauss matrix. The new claim is a complete higher-order tomography principle for the random-modulus least-prime field. Every scalar statistic is compared on a genuine probability space, while the varying finite fields are handled fibrewise before averaging. Failure would isolate a tensor class on which local same-class prime correlations and character-zero correlations disagree even though the underlying finite transforms are exact. The first theorem is the quadratic identity for tests localized to one additive lag and its transported character kernel.

**Rubinstein–Sarnak terminal chaos dichotomy (Conjecture 33).** Assume GRH and a $$q$$-aspect linear-independence/random-phase hypothesis for the low zeros of primitive Dirichlet $$L$$-functions. Let $$x_q$$ satisfy $$\operatorname{Li}(x_q)/(q-1)=\log(q-1)$$ and let $$G_{q,A}(a)$$ be the centred, variance-normalized low-zero field obtained from characters $$\chi\ne\chi_0$$ and zeros $$\vert \gamma\vert \le(\log q)^A$$, with the standard compensator $$-\tfrac12\operatorname{Var} G_{q,A}(a)$$. Define the random empirical chaos measure

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

At finite modulus the cluster-start thinning enters through the terminal extremal index $$\theta_{\mathrm{occ}}(q)$$, the analogue for the last classes of the cluster-start fraction $$\theta_X(H)$$ of Conjecture 29, together with the terminal connected decorations supplied by the hierarchy of Conjecture 31. Both corrections enter at the first nonzero connected scale and vanish in the successive limit, so $$\theta_{\mathrm{occ}}(q)\to1$$ and the limiting directing measure carries no cluster factor.

The nature of the directing measure is governed by the covariance-energy statistic

$$
\mathfrak E_{q,A}=\frac1{(q-1)^2}
 \sum_{a,b\in\mathbb F_q^\times}
 \operatorname{Cov}(G_{q,A}(a),G_{q,A}(b))^2.
$$

If $$\mathfrak E_{q,A}\to0$$ along the successive limit, $$\mathcal M$$ self-averages to the deterministic exponentially tilted Gaussian law and the terminal process is an ordinary decorated Poisson process. If $$\liminf\mathfrak E_{q,A}>0$$ and the Gaussian-chaos second moments are uniformly integrable, $$\mathcal M$$ is nondegenerate and the limit is a genuine Cox process. No nondegeneracy is asserted without this criterion.

*Significance.* Rubinstein–Sarnak theory supplies the fixed-modulus prime-race environment [6]. The new object is its terminal first-arrival chaos measure in the modulus aspect. The statement now treats self-averaging as a serious competing model rather than assuming a Cox limit by terminology. It predicts the complete last class process, its prime-race marks, and an explicit spectral criterion separating a deterministic environment from persistent random mixing. The first theorem is the self-averaging branch at one fixed cutoff $$A$$, where $$\mathfrak E_{q,A}\to0$$ forces the deterministic exponentially tilted Gaussian limit of $$\mathcal M_{q,A}$$ and an ordinary decorated Poisson law for the terminal cluster-start process.

**Nonlinear spectral response calculus for arithmetic first arrivals (Conjecture 34).** Let a sequence of modulus ensembles have a small explicit-formula perturbation of the arrival intensity

$$
V_Q(a,t)=\sum_{\chi\in\mathcal C_Q}v_{Q,\chi}(t)\chi(a),
 \qquad \|V_Q\|_{T}\to0,
$$

where $$\mathcal C_Q$$ has uniformly bounded cardinality and, on every fixed interval $$[0,T]$$, the canonical norm is $$\|V\|_T=\sup_{a,0\le t\le T}\vert V(a,t)\vert $$. Assume that the connected hierarchy of Conjecture 31 satisfies an exponential cluster bound there, so its Laplace functional is analytic in a fixed $$\|\cdot\|_T$$-ball. If $$S_Q(a,t)$$ and $$S_Q^{(0)}(t)$$ are the perturbed and ordinary survival functions, then for every fixed $$R$$

$$
\log\frac{S_Q(a,t)}{S_Q^{(0)}(t)}
 =\sum_{m=1}^{R}\mathcal R_m[V_Q^{\otimes m}](a,t)
   +o(\|V_Q\|_{T}^{R})
$$

uniformly on compact $$t$$-ranges. The causal Volterra operator $$\mathcal R_m$$ is the universal linked-cluster contraction of the full hierarchy $$(K_r)_{r\ge1}$$ with $$m$$ marked perturbation insertions, and truncating the connected hierarchy at order $$J$$ gives a convergent approximation as $$J\to\infty$$.

If the input character support is $$\mathcal C_Q$$, the $$m$$th response has Fourier support contained in the products of at most $$m$$ input characters, with the reverse inclusion possibly failing through cancellation or the trivial character. In particular the linear response preserves character rank, while any new harmonics first appear at quadratic order with coefficients determined by connected three-point arrival correlations.

*Significance.* This is a nonlinear transfer calculus from zeros to first-hit statistics. A Siegel zero, a cluster of low zeros, and an ordinary prime-race bias become different inputs to the same response operators. The exceptional-zero rank-one statement is a special case, while the second-order harmonics provide a direct falsification test. The first theorem is the Fréchet derivative $$\mathcal R_1$$ from the two-point occupancy kernel.

**Local-information capacity of odd class groups (Conjecture 35).** Fix an odd prime $$\ell$$. Sample negative fundamental discriminants $$D\in[-2Y,-Y]$$, conditioned on a fixed coarse two-primary invariant. For a set of odd primes $$S_Y$$, put $$M_Y=\prod_{p\in S_Y}p$$, let $$\Sigma_Y(D)=((D/p))_{p\in S_Y}$$ be the attainable sign vector, and let $$H_Y$$ be the logarithm of the number of attainable cells. Let $$\delta_Y(\sigma)$$ be the exact CRT density of the sign cell after imposing quadratic reciprocity and the fixed two-primary data (for a single odd unramified prime the density of each sign is $$p/(2(p+1))$$, and an unconditioned cell density is the corresponding product), and let $$\mathcal D_Y$$ be the ambient discriminant family. Write

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

*Significance.* Wood’s framework treats fixed local conditions [37]. The new statement proposes the full information capacity of an odd class group under a growing local sigma-algebra, with the entropy governing impossibility and the conductor governing equidistribution. It would transfer directly to Selmer groups, ray class groups, and unramified extension statistics. The first theorem is uniformity for $$\vert S_Y\vert \to\infty$$ with $$M_Y=Y^{o(1)}$$. The discrepancy half is not the obstruction: for cells of macroscopic mass the equidistribution of discriminants is elementary for $$M_Y\le Y^{1/2-\varepsilon}$$, and squarefree-in-progressions technology carries it to $$Y^{2/3-\varepsilon}$$, so the conjectural content lies entirely in the class-group law over the growing cell family.

### Programme III: finite logarithms, regulators, and algebraic tori

For $$p\nmid a$$, write

$$
q_p(a)=\frac{a^{p-1}-1}{p}\pmod p.
$$

For a generating tuple $$g=(g_1,\ldots,g_s)$$, let $$R(g)$$ be its multiplicative relation lattice and let $$\mathbb T_g\subset(\mathbb R/\mathbb Z)^s$$ be the identity component of its annihilator. Its dimension is the saturated multiplicative rank. Write $$e(x)=\mathrm e^{2\pi ix}$$.

**Kummer–Haar law on relation tori (Conjecture 36).** Let $$\Gamma\le\mathbb Q^\times$$ be finitely generated and torsion-free, saturated modulo torsion (if $$x^n\in\Gamma\cdot\{\pm1\}$$ for some $$n\ge1$$ then $$x\in\Gamma\cdot\{\pm1\}$$), and let $$g$$ be any ordered generating tuple. As $$p$$ varies in every fixed compatible cyclotomic–Kummer Chebotarev class, the vectors

$$
\frac{(q_p(g_1),\ldots,q_p(g_s))}{p}\in(\mathbb R/\mathbb Z)^s
$$

equidistribute with Haar measure on $$\mathbb T_g$$. More strongly, for every finite collection of compatible Chebotarev restrictions, the conditional empirical measures converge to the Haar disintegration on the corresponding components, and the support is contained in no proper closed coset of $$\mathbb T_g$$. The law is invariant under changing generators and depends on $$\Gamma$$ only through its saturation and the fixed Kummer conditioning data.

*Significance.* Katz formulated horizontal Wieferich equidistribution principles for algebraic groups, and Shparlinski proved estimates in different horizontal and averaged regimes [38, 39]. The new content here is the exact saturated relation torus, full generator invariance, and disintegration under fixed Kummer classes. It turns multiplicative rank into a geometric support theorem rather than a heuristic count of coordinates. The first decisive theorem is the Haar law on $$\mathbb T_g$$ for one rank-one saturated $$\Gamma$$ presented by two dependent generators, restricted to a single fixed compatible cyclotomic–Kummer Chebotarev class. A failure would show that the vectors $$q_p(g_i)/p$$ remember more of $$\Gamma$$ than its saturation, concentrating on a proper closed coset of $$\mathbb T_g$$ that no relation in $$R(g)$$ predicts.

**Rank-dimensional large sieve for finite logarithms (Conjecture 37).** Choose a Smith-normal-form basis of the character lattice $$X^*(\mathbb T_g)=\mathbb Z^s/R(g)^{\mathrm{sat}}$$. There is a constant $$\delta_\Gamma>0$$ such that, for every $$\varepsilon>0$$, every $$M\le X^{\delta_\Gamma}$$, and all complex weights $$a_p$$ supported on $$X<p\le2X$$,

$$
\sum_{\substack{m\in X^*(\mathbb T_g)\\\|m\|_\infty\le M}}
 \left\vert \sum_{X<p\le2X}a_p
 e\!\left(\frac{\langle m,q_p(g)\rangle}{p}\right)\right\vert ^2
 \ll_{\Gamma,\varepsilon}(M^{\operatorname{rank}\Gamma}+\pi(X))X^\varepsilon\sum_p\vert a_p\vert ^2.
$$

The same inequality holds after every fixed compatible cyclotomic–Kummer restriction, and for matrix-valued weights with the Hilbert–Schmidt norm. The exponent $$\delta_\Gamma$$ is invariant under changing the generating tuple.

*Significance.* This is the quantitative mechanism behind Conjecture 36. It predicts that saturated rank is not only the support dimension but the exact dual dimension in a prime-varying large sieve. A proof for any positive power range would control genuine shrinking targets and would be far beyond currently available fixed-frequency tests. Failure would reveal an unrecognized spacing or energy obstruction among finite-logarithm vectors.

**Mesoscopic-to-lattice shrinking-target transition (Conjecture 38).** Let $$\Gamma\le\mathbb Q^\times$$ be torsion-free of rank $$r$$ and saturated modulo torsion, and choose a basis of $$\Gamma$$, identifying its relation torus with $$(\mathbb R/\mathbb Z)^r$$. For integers $$w_p$$ with $$1\le w_p=o(p)$$, let $$E_p(w)$$ be the event that every coordinate of the Fermat-quotient vector has a representative of absolute value at most $$w_p$$.

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

whenever the sum diverges, while only finitely many such primes occur when $$r\ge2$$. As a separately falsifiable genericity clause, for Kummer-generic $$\Gamma$$ (the Kummer fields $$\mathbb Q(\zeta_m,\Gamma^{1/m})$$ have the maximal degree $$\varphi(m)m^{r}$$ for every $$m$$) and $$B=\{0\}$$ one has $$\kappa_{\Gamma,B}=1$$. The transition from Haar universality to the arithmetic intensity occurs only when $$w_p$$ remains bounded.

*Significance.* This separates two universality classes that a single undifferentiated model conflates. Growing targets are controlled by Haar geometry, while exact Wieferich targets can carry a genuinely arithmetic regulator intensity. Gras’s much rarer fixed-base model and the Haar model therefore disagree precisely at the lattice boundary [40, 41]. The first theorem is mesoscopic universality for $$w_p=p^\eta$$ with one rank-one base.

For a $$p$$-adic unit $$a$$, write $$\langle a\rangle_p$$ for the Teichmüller lift of its residue, and for a prime $$\mathfrak p\mid p$$ of a number field write $$\tau_{\mathfrak p}$$ for the Teichmüller lift in the completion at $$\mathfrak p$$. Define $$q_{p,k}(a)=p^{-1}\log(a\langle a\rangle_p^{-1})\pmod{p^k}$$. The matrix entries below are the $$\mathfrak p$$-adic analogues of $$q_{p,k}$$, and on $$\mathbb Q$$ with $$k=1$$ one has $$q_{p,1}(a)\equiv-q_p(a)\pmod p$$, the Fermat quotient up to sign.

**Global-lattice horizontal $$p$$-adic regulator-matrix law (Conjecture 39).** Let $$K/\mathbb Q$$ be a fixed Galois number field with group $$G$$, and let $$\Gamma\le\mathcal O_K^\times$$ be torsion-free and saturated modulo $$\mu(K)$$, with ordered basis $$\epsilon_1,\ldots,\epsilon_s$$. Define the fixed global relation lattice

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

It lies in the annihilator of $$\mathcal R_\Gamma\otimes\mathbb Z/p^k\mathbb Z$$. As $$p$$ varies through any fixed compatible Frobenius class, $$L_{p,1}/p$$ equidistributes with Haar measure on $$\mathbb T_\Gamma$$, and the depth-$$k$$ matrices are Haar at every fixed depth $$k$$, with the depth-$$(k+1)$$ law pushing forward to the depth-$$k$$ law under reduction (the moduli vary with $$p$$, so this is a per-depth statement with compatible marginals, not Haar on one fixed group).

Let $$\mathcal D$$ be a basis-invariant determinantal or Smith stratum in this projective module, and let $$\mu_{p,k}(\mathcal D)$$ be its exact local Haar mass. The primes for which $$L_{p,k}\in\mathcal D$$ have counting law governed by $$\sum_{p\le X}\mu_{p,k}(\mathcal D)$$. For a determinantal or Smith stratum of codimension $$c$$, whose point counts are polynomial in $$p$$, $$\mu_{p,1}(\mathcal D)=p^{-c}+O(p^{-c-1})$$, and codimension one has a Poisson point process in $$\log\log p$$ after uniform random translation, while codimension at least two has a summable large-prime tail together with the exact small-prime atoms.

*Significance.* The horizontal state space is one fixed global torus rather than a relation module that changes with $$p$$. The conjecture turns mod-$$p$$ Leopoldt defects into a Galois-equivariant random-matrix problem, with exact Smith strata retaining higher depth. Existing mod-$$p$$ Leopoldt and random-matrix theories provide neighbouring languages [41, 42, 43]. Recent number-field Wieferich results strengthen the arithmetic motivation without supplying this horizontal matrix law [57, 58]. The first theorem is the rank-one split-prime law for a real quadratic field. A failure would show that the matrices $$L_{p,k}(\Gamma)$$ favour some Smith stratum beyond its exact local Haar mass, so mod-$$p$$ Leopoldt defects would be governed by an arithmetic invariant outside the fixed global torus $$\mathbb T_\Gamma$$.

**Functorial horizontal finite logarithms on algebraic tori (Conjecture 40).** Let $$T/\mathbb Q$$ be an algebraic torus, let $$\mathcal T$$ be its smooth integral model away from a finite set, and let $$\Gamma\le T(\mathbb Q)$$ be finitely generated. Let $$S$$ be the identity component of the Zariski closure of $$\Gamma$$. At a good unramified prime $$p$$, let $$\tau_p(\bar P)$$ be the canonical prime-to-$$p$$ torsion lift of the reduction of $$P\in\Gamma$$ and define

$$
\ell_p(P)=p^{-1}\log_T\bigl(P\tau_p(\bar P)^{-1}\bigr)\pmod p
 \in\operatorname{Lie}(S)(\mathbb F_p).
$$

Here $$\operatorname{Lie}(S)(\mathbb F_p)$$ is identified with $$(\mathbb Z/p)^{\dim S}$$ through a fixed integral basis of the Lie algebra of $$\mathcal T$$, with representatives in $$[0,p)$$, and a different basis changes the matrix by a fixed element of $$\mathrm{GL}_{\dim S}(\mathbb Z)$$, which preserves the Haar law and the shrinking-target intensities. For any generators $$P_1,\ldots,P_s$$ of $$\Gamma$$, the normalized matrix $$(\ell_p(P_i)/p)_i$$ equidistributes, in every compatible Frobenius class, with Haar measure on the real relation subtorus cut out jointly by the algebraic subgroup $$S$$ and the integral relations among the $$P_i$$. For every morphism of tori $$\phi:T\to T'$$,

$$
\ell_p(\phi(P))=d\phi(\ell_p(P)),
$$

and the horizontal Haar measures push forward under the induced map. Isogenies preserve the shrinking-target intensities after the explicit finite kernel correction.

*Significance.* Katz already proposed Wieferich equidistribution beyond $$\mathbb G_m$$ [38]. The additional content is a matrix-valued law for a finitely generated global subgroup, relation-subtorus support, fixed-Frobenius disintegration, and exact functoriality under morphisms and isogenies. It turns horizontal finite logarithms into a functor on the category of tori with arithmetic subgroups. The first decisive theorem is the Haar law for the group generated by a single point of a one-dimensional nonsplit torus $$T$$, in a single fixed compatible Frobenius class. A failure would show that the matrices $$(\ell_p(P_i)/p)_i$$ concentrate on a proper closed subset of the relation subtorus, an arithmetic constraint beyond the algebraic subgroup $$S$$ and the integral relations among the $$P_i$$.

### Programme IV: arboreal arithmetic dynamics

For a degree-$$d$$ map $$f$$ and basepoint $$a$$, write $$K_n=\mathbb Q(f^{-n}(a))$$, $$G_n=\operatorname{Gal}(K_n/\mathbb Q)$$, and let $$\mu_n(C)=\vert C\vert /\vert G_n\vert $$ on conjugacy classes. For primes $$p\le X$$ unramified in $$K_n$$, let $$\widehat\mu_{n,X}$$ be the empirical Frobenius measure.

**Entropy–conductor profile of arboreal resolution (Conjecture 41).** For a degree-$$d$$ map $$f$$ and level $$n$$, let $$G_{n,f}$$ be the arboreal quotient and $$\mu_{n,f}$$ its Haar measure on conjugacy classes. For $$N$$ independent samples from $$\mu_{n,f}$$ define the exact sampling obstruction

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

Assume the generic arboreal image is open, exceptional parameters have density zero, Artin holomorphy and GRH hold at the levels considered, and the family is in the large-sieve range of Conjecture 42 below. Then the actual empirical resolution depth, defined by the same total-variation threshold with prime Frobenius samples, differs from $$n^*_{\mathcal F}(B,X;\eta)$$ by $$O_{\mathcal F,\eta}(1)$$.

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

*Significance.* The observable depth is defined through the exact nonuniform sampling law and a representation-by-representation conductor energy. The $$\log_d\log X$$ scale follows from explicit Rényi and conductor profiles on the natural $$d^n$$ complexity scale. Large arboreal images and effective Chebotarev are inputs [44, 45, 46]. Recent work on fixed-point profiles shows why the full class-measure tail, rather than group order alone, matters [59]. The first theorem is bounded-shift stability for one explicit index-two subgroup of the binary wreath tower. A failure would show that resolution depth responds to a family invariant beyond the complete Rényi profile $$\psi_{\mathcal F}(\alpha)$$ and the conductor energy $$\mathcal A_{n,f}(X)$$, so two families with matching profiles could separate by an unbounded shift.

**Arboreal family large sieve and cumulant independence (Conjecture 42).** Let $$\mathcal F\to\mathbb A^1$$ be a generically finite-index arboreal family. For each level $$n$$ and irreducible representation $$\rho$$ of the generic quotient $$G_n$$, let $$\mathcal V_{n,\rho}$$ be the associated middle-extension sheaf on the good parameter locus (the canonical extension of the corresponding local system across the bad parameters). Define the geometric conductor budgets

$$
\mathfrak C_{n,r}=
 \sum_{\rho_1,\ldots,\rho_r}
 \left(\prod_{j=1}^r\dim\rho_j\right)^2
 \operatorname{cond}\!\left(\boxtimes_{j=1}^r\mathcal V_{n,\rho_j}\right)^2,
 \qquad \mathfrak C_n=\mathfrak C_{n,1},
$$

where the external tensor product is taken on the CRT parameter space for distinct primes, and the conductor includes rank, the number of singular points, and the tame-drop and Swan terms (the tame and wild ramification invariants at those points).

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

*Significance.* This separates the two analytic inputs that a single-tier statement compresses into one claim. The square-root tier is a growing-monodromy large sieve in the spirit of Kowalski [47]. The connected tier is the genuinely stronger cross-prime independence principle required for an occupancy limit. The conductor budget is attached to the actual sheaves and their tensor products rather than to an undefined scalar conductor of a cover. The first theorem is the connected tier at $$r=3$$ for one fixed level $$n$$, square-root cancellation of the family-averaged third connected cumulant within the range governed by $$\mathfrak C_{n,3}$$. A failure identifies either geometric complexity missed by the sheaf conductors or arithmetic entanglement surviving all fixed-order trace tests.

**Coloured dynatomic Galois-factor process (Conjecture 43).** For $$f_c(x)=x^d+c$$, let the critical exact-period polynomial factor as $$\Psi_n(c)=\prod_{j=1}^{s_n}F_{n,j}(c)$$ over $$\mathbb Z$$. Sample $$c$$ from a dyadic height interval away from postcritically finite, discriminant, and fixed-resultant loci.

For every fixed $$n$$, condition on any fixed finite local valuation state and normalize the prime factors of each $$F_{n,j}(c)$$ by that component’s residual logarithmic mass. The component-coloured factor processes converge jointly to independent Frobenius-marked Poisson–Dirichlet $$\operatorname{PD}(1)$$ processes, with the mark in colour $$j$$ given by the fixed-point-size-biased conjugacy law in the splitting field of $$F_{n,j}$$. The total logarithmic mass of ramified factors tends to zero.

Uniformly for $$n=n(H)$$ with $$\deg\Psi_n=o(\log H)$$, every fixed correlation functional whose support lies inside the available level of distribution converges to the corresponding restricted-support correlation of these coloured marked processes. No full-process claim is made at growing degree without level-one distribution.

*Significance.* Exact-period components are genuine geometric colours, and their Galois marks distinguish dynamical families with similar unmarked factor sizes. The statement deliberately separates the full fixed-degree process from the restricted-support growing-degree law, in accordance with the distribution thresholds in Bharadwaj–Rodgers [51]. The first theorem is a two-colour correlation law at one fixed period. A failure would show that distinct exact-period components are entangled, with the splitting fields of two factors $$F_{n,j}$$ sharing Frobenius information that survives conditioning on the fixed finite local valuation state.

**Complexity-uniform primitive valuation process for dynatomic values (Conjecture 44).** For the critical exact-period polynomial $$\Psi_n(c)$$, remove its canonical greatest common divisor in $$\mathbb Q[c]$$ with the earlier critical-orbit product $$\prod_{m<n}f_c^m(0)$$, in the notation of Conjecture 43, and denote the result by $$\Psi_n^{\mathrm{new}}$$. Define the logarithmic arithmetic complexity

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

*Significance.* Degree alone does not control a growing polynomial family. The controlling range includes coefficient height, discriminant, and resultants, while the infinite-product conclusion is supported by an explicit uniform squarefull-tail assertion. The local process still retains every bad-prime and collision state and remains level dependent, as primitive hits at a fixed prime occur by bounded time modulo $$p^k$$. For the unicritical families $$x^d+c$$ the resultants at the first levels are units, so the stated complexity range is nonempty there. The first decisive theorem is the primitive valuation law with its uniform squarefull tail at one fixed level of the unicritical family $$x^d+c$$, giving the squarefree asymptotic for that single $$\Psi_n^{\mathrm{new}}$$. A failure would show that $$\mathfrak H_n$$ is not the right complexity gauge, with some growing-level family carrying squarefull mass or valuation correlations that degree, coefficient height, discriminant, and resultants together do not see. The nearest literature treats primitive divisors and fixed-polynomial squarefree values, not this complexity-uniform adelic process [49, 48].

**Divisor-sensitive classification of dynamical gcd height (Conjecture 45).** Let $$F=(f,g)$$ be a split map on $$(\mathbb P^1)^2$$, with $$f,g$$ disintegrated (in the sense of Medvedev and Scanlon [56], so neither is linearly conjugate to a power map, a Chebyshev map, or a close relative of these) of the same degree, and let $$P=(a,b)$$ have positive canonical heights. Let $$D_1,D_2$$ be the two coordinate-zero divisors and let $$E$$ be the exceptional divisor of the blow-up at $$D_1\cap D_2$$. Then

$$
\limsup_{n\to\infty}
 \frac{h_E(F^n(P))}{\max\{h(f^n(a)),h(g^n(b))\}}>0
$$

if and only if there exist $$m\ge0$$ and an irreducible $$F$$-periodic curve $$Z$$ containing $$F^m(P)$$, with $$Z$$ not contained in $$D_1\cup D_2$$ (automatic when both coordinates have positive canonical height), such that, on the normalization of $$Z$$, the pullbacks of $$D_1$$ and $$D_2$$ have a common nonzero effective component. In the absence of such eventual entry into a divisor-compatible periodic curve, the normalized gcd height tends to zero.

The converse is unconditional in every setting where the required Vojta inequality for the blow-up is known, and otherwise is explicitly conditional on that inequality. The same criterion extends to split maps on $$(\mathbb P^1)^r$$ by replacing a common component with positive codimension-one intersection multiplicity among the pulled-back divisors.

*Significance.* The obstruction is not merely a common dynamical quotient. It is a periodic geometric relation carrying the actual divisors measured by the gcd height. Eventual entry is the right notion, since a preperiodic tail can carry the divisor relation before periodicity begins. Recent work resolves several set-theoretic dynamical-GCD problems, while this height-theoretic divisor classification is the additional boundary [50]. The first theorem is the positive-limsup direction, that eventual entry of the orbit into a divisor-compatible periodic curve $$Z$$ forces $$\limsup h_E(F^n(P))/\max\{h(f^n(a)),h(g^n(b))\}>0$$. Failure would point to a new source of macroscopic Diophantine proximity outside invariant geometry.

### Programme V: adelic factorization and sieve flow

Throughout this programme $$P^+(m)$$ and $$P^-(m)$$ denote the largest and smallest prime factors of $$m$$, the constant $$\gamma$$ is Euler’s, $$\rho_f(p)$$ counts the roots of $$f$$ modulo $$p$$, and every sample $$n\in[N,2N]$$ is drawn uniformly.

**Frobenius-marked Poisson–Dirichlet process (Conjecture 46).** Let $$f\in\mathbb Z[x]$$ be irreducible with splitting field $$L$$ and transitive Galois group $$G$$. Sample $$n\in[N,2N]$$. Mark each unramified prime factor $$p$$ of $$f(n)$$ by its conjugacy class $$C\subset G$$ and give it mass $$u=\log p/\log\vert f(n)\vert $$. The macroscopic marked process converges to a marked $$\operatorname{PD}(1)$$ process with conditional mark law

$$
\mathbb P(C\mid u)=\frac{\vert C\vert }{\vert G\vert }\operatorname{fix}(C),\qquad\text{$\operatorname{fix}(C)$ the number of fixed roots of an element of $C$,}
$$

independent of $$u$$. Given the masses and every fixed finite local valuation state, the marks of finitely many macroscopic factors are asymptotically independent. Under a normal quotient equipped with the induced permutation representation, the marked process pushes forward functorially.

*Significance.* Chebotarev contributes $$\vert C\vert /\vert G\vert $$, divisibility by a polynomial value size-biases by the number of fixed roots, and Burnside’s lemma normalizes the result. Bharadwaj–Rodgers supply the unmarked factor-process framework [51]. Simultaneous Galois marking, conditional independence, and functorial pushforward are the new content. It connects Galois theory to probabilistic factorization directly. The first theorem is the mark law for the largest prime factor of one irreducible quadratic $$f$$, the two-class case where the size bias $$\operatorname{fix}(C)$$ already separates the marked law from the plain Chebotarev weight $$\vert C\vert /\vert G\vert $$. A failure would show that divisibility size-biases Frobenius by more than the fixed-root count, a coupling between factor masses $$u$$ and Galois marks that survives conditioning on the finite local valuation state.

**Three-scale factorization of polynomial values (Conjecture 47).** Let $$f\in\mathbb Z[x]$$ be irreducible, sample $$n\in[N,2N]$$, choose $$y=y(N)\to\infty$$ with $$\log y=o(\log N)$$, and write $$R_y=f(n)/S_y(f(n))$$, where $$S_y(m)=\prod_{p\le y}p^{v_p(m)}$$ is the $$y$$-smooth part. Jointly with the complete small-prime valuation field $$(v_p(f(n)))_{p\le y}$$, the residual logarithmic factor process

$$
\sum_{p\mid R_y}v_p(R_y)\,
 \delta_{\left(\log p/\log\vert R_y\vert ,\,\mathrm{Frob}_p\right)}
$$

converges to the following conservation-corrected product object: the small valuations have their polynomial Kubilius law (independent exact local limit laws for the small-prime valuations), and conditional on their consumed logarithmic mass the residual process is a scale-invariant Poisson process of intensity $$du/u$$, marked by Conjecture 46, conditioned to have total mass one. The small field and the unconditioned residual Poisson process are asymptotically independent, and all leading dependence after conditioning is the single residual-mass constraint.

For disjoint normalized size bands bounded away from zero, the unconditioned residual process has independent increments. Its mesoscopic restriction and its ranked macroscopic atoms yield respectively the scale-invariant factor process and the Frobenius-marked $$\operatorname{PD}(1)$$ partition. Thus the local Kubilius field is the boundary variable fixing the available mass, while the mesoscopic and macroscopic laws are two projections of one residual process, and no additional cross-scale coupling survives.

*Significance.* Raw small–large independence is false because small factors consume mass. This conjecture identifies the complete conservation-corrected product structure and adds the mesoscopic scale that is absent from a two-scale statement. It would justify, in one limit theorem, the local sieve model, the scale-invariant factor process, and the macroscopic partition. The first decisive theorem is the conservation-corrected joint law at one fixed prime $$p$$ and one normalized size band, where the only surviving dependence is the residual-mass constraint. A failure would show a cross-scale coupling between the small-prime valuation field and the residual process beyond the single residual-mass constraint, so smooth-part consumption would not exhaust the dependence between the sieve scale and the factor process.

**Adelic Gibbs gluing for reducible polynomial values (Conjecture 48).** Let $$f=\prod_{i=1}^s g_i$$ be squarefree with irreducible components, sample $$n\in[N,2N]$$, and put $$t=n/N$$. For each prime $$p$$, let $$\nu_p$$ be the exact Haar law on $$\mathbb Z_p$$ of the valuation vector $$(v_p(g_1(x)),\ldots,v_p(g_s(x)))$$. For $$y\to\infty$$ with $$\log y=o(\log N)$$, consider stable convergence jointly with the archimedean coordinate $$t$$ and condition on $$\mathscr L_y=(v_p(g_i(n)))_{p\le y,i\le s}$$. After normalizing each component by its own residual logarithmic mass, the coloured Frobenius-marked factor processes converge to conditionally independent copies of the three-scale law of Conjecture 47, with the marks of Conjecture 46.

Unconditionally, the joint process is the projective Gibbs mixture obtained by integrating those conditional product laws against Lebesgue measure in $$t$$ and the adelic local law $$\bigotimes_p\nu_p$$, in the iterated order $$N\to\infty$$ and then $$y\to\infty$$. Every bounded finite-dimensional Laplace functional is determined by

$$
Z_p(\mathbf z)=\int_{\mathbb Z_p}\prod_i z_i^{v_p(g_i(x))}\,dx
$$

together with the archimedean size profile $$(\log\vert g_i(Nt)\vert )_i$$. No additional colour coupling survives after this adelic–archimedean mixture.

*Significance.* A scalar Euler factor cannot specify a point process. This statement gives the full local-to-global gluing rule and includes the archimedean variable that can couple component sizes. It is functorial under multiplying, splitting, or regrouping components. The first theorem is the case of two linear components, where $$Z_p(\mathbf z)$$ is computable in closed form and the mixture over $$t$$ and $$\bigotimes_p\nu_p$$ already yields the full two-colour gluing law. A persistent medium-prime or archimedean coupling after the stated mixture would identify a new nonadelic invariant.

**Full multivariate adelic saddle law for joint smoothness (Conjecture 49).** Let $$f_1,\ldots,f_s\in\mathbb Z[x]$$ be pairwise coprime, primitive, and jointly admissible, meaning that for every prime $$p$$ some residue $$x$$ has $$p\nmid\prod_{i}f_i(x)$$, sample $$n\in[N,2N]$$, and put $$t=n/N$$. For complex variables $$\mathbf s$$ and smoothness bounds $$\mathbf y$$, define

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

*Significance.* The statement is calibrated to the cumulative smoothness probability. It combines exact higher $$p$$-adic valuations, moving archimedean sizes, the joint saddle displacement, Perron amplitudes, mixed curvature, and possible lattice effects. Even one-polynomial smooth-value asymptotics are difficult [52, 53]. A complete multivariate adelic saddle law would be a major new local–global bridge. A failure would show a joint smoothness dependence not produced by the exact $$p$$-adic partition functions and the moving archimedean sizes, an arithmetic coupling among the $$f_i$$ outside the saddle displacement, the Hessian $$H_t$$, and the lattice correction.

**Buchstab–Bateman–Horn component flow (Conjecture 50).** Let $$f\in\mathbb Z[x]$$ be primitive, irreducible, and admissible ($$\rho_f(p)<p$$ for every prime $$p$$), and sample $$n\in[N,2N]$$. For $$y$$ with $$u_n=\log\vert f(n)\vert /\log y$$ in a fixed compact subset of $$(1,\infty)$$, let $$\Omega_y(f(n))$$ be the number of prime factors of $$f(n)$$ exceeding $$y$$, counted with multiplicity, on the event $$P^-(f(n))>y$$. Put

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

uniformly on compact $$u$$-ranges. Conditional on the ordered logarithmic sizes of the $$j$$ remaining factors, their unramified Frobenius marks are independent with the fixed-point-size-biased law of Conjecture 46. Summing over $$j$$ gives the rough-value Buchstab law, $$j=1$$ gives the Bateman–Horn prime density, and $$j=2$$ gives the semiprime transition. Whenever $$\max_{N\le n\le2N}\vert f(n)\vert <y^2$$, every rough value has exactly one prime factor above $$y$$, so the $$j=1$$ component exhausts the rough set, while the density formula itself remains conjectural.

*Significance.* The conjecture resolves a rough polynomial value into its complete finite-$$u$$ factor count and Galois mark content. Primes and semiprimes are not inserted as separate heuristics. They are components of one universal flow. Generalized Buchstab equations are the random-integer antecedent [60], and the fixed-polynomial, Galois-marked component law with its local factors is the new statement. It is strongly falsifiable even when total roughness follows Buchstab.

## Part III: six conjectures across fields

*Added to the deposit: 4 August 2026.*

The six conjectures below leave the prime model. They range over multiplicative number theory, discrepancy theory, graph limits, additive information theory, and ergodic theory, and each is held to the same standard as the rest of the collection: a canonical object, a stated mechanism, the nearest literature boundary, a first decisive theorem where one exists, and an honest failure mode.

### Relative polynomial pretentiousness

Let $$P\in\mathbb Z[x]$$ be primitive (the greatest common divisor of its coefficients is $$1$$) and irreducible, with positive leading coefficient. For a prime $$p$$ write

$$
\rho_P(p)=\#\{a\in\mathbb Z/p\mathbb Z:P(a)\equiv0\pmod p\}.
$$

The weight $$\rho_P(p)/p$$ is the first-order frequency with which $$p$$ divides a polynomial value $$P(n)$$. A function $$f$$ on the positive integers is completely multiplicative if $$f(mn)=f(m)f(n)$$ for all $$m,n\ge1$$. For completely multiplicative $$f,g$$ with values in the closed complex unit disc, define the truncated $$P$$-relative pretentious distance

$$
\mathbb D_P(f,g;X)^2
=
\sum_{p\le X}\frac{\rho_P(p)}{p}
\bigl(1-\operatorname{Re}\bigl(f(p)\overline{g(p)}\bigr)\bigr),
\qquad
\mathbb D_P(f,g)^2=\lim_{X\to\infty}\mathbb D_P(f,g;X)^2\in[0,\infty].
$$

Every summand is nonnegative, so the truncated distance is nondecreasing in $$X$$ and the limit exists. Throughout, a primitive Dirichlet character $$\chi$$ of conductor $$c$$ is regarded as the $$c$$-periodic completely multiplicative function on $$\mathbb Z$$ that vanishes on integers not coprime to $$c$$, so that expressions such as $$\chi(P(a))$$ are defined for every residue $$a$$ modulo any multiple of $$c$$. For $$t\in\mathbb R$$, the comparison function $$n\mapsto\chi(n)n^{it}$$ is completely multiplicative with values in the closed unit disc.

Let $$P_1,\ldots,P_m\in\mathbb Z[x]$$ be pairwise distinct primitive irreducible polynomials with positive leading coefficients and no fixed prime divisor, meaning $$\rho_{P_j}(p)<p$$ for every $$j$$ and every prime $$p$$. Assume multiplicative independence modulo constants:

$$
\prod_{j=1}^m P_j(x)^{e_j}\in\mathbb Q^\times,\quad e_j\in\mathbb Z
\quad\Longrightarrow\quad
e_1=\cdots=e_m=0.
$$

Write $$\mathbb S^1$$ for the unit circle in the complex plane.

**Relative polynomial pretentiousness inverse principle (Conjecture 51).** Let $$f_1,\ldots,f_m:\{1,2,3,\ldots\}\to\mathbb S^1$$ be completely multiplicative. If

$$
\limsup_{X\to\infty}
\left\vert 
\frac{1}{\log X}
\sum_{\substack{n\le X\\P_j(n)>0\ \forall j}}
\frac{\prod_{j=1}^m f_j(P_j(n))}{n}
\right\vert >0,
$$

then there exist primitive Dirichlet characters $$\chi_1,\ldots,\chi_m$$ and real numbers $$t_1,\ldots,t_m$$ such that the following three conditions hold simultaneously:

*(i)* $$\mathbb D_{P_j}\bigl(f_j,\chi_j(n)n^{it_j}\bigr)<\infty$$ for every $$1\le j\le m$$,

*(ii)* $$\displaystyle\sum_{j=1}^m t_j\deg P_j=0$$,

*(iii)* for some common multiple $$q$$ of the conductors of $$\chi_1,\ldots,\chi_m$$,

$$
\frac1q\sum_{a\bmod q}\prod_{j=1}^m\chi_j(P_j(a))\ne0,
$$

the characters being extended by $$0$$ on nonunits as above.

*Significance.* The mechanism is that a persistent logarithmic correlation should have exactly two sources: an archimedean resonance carried by the factors $$n^{it_j}$$ and a finite local resonance carried by the characters $$\chi_j$$. The balance condition (ii) is forced by the expansion $$P_j(n)^{it_j}=c_j^{it_j}n^{it_j\deg P_j}(1+o(1))$$, with $$c_j$$ the leading coefficient, because logarithmic averaging annihilates any nonzero total power of $$n$$, and (iii) asserts that the finite-modulus resonances are jointly compatible, so that the model correlation does not vanish identically for local reasons. Packaging the conclusion as one existential block matters: the characters and archimedean parameters cannot be chosen independently for each $$j$$, and it is the joint system (i)–(iii) that reproduces the correlation. The decisive-theorem ledger for the linear case is as follows. For linear polynomials the two-point case is Tao’s logarithmically averaged two-point Elliott theorem [75]. The odd-order cases are the theorems of Tao–Teräväinen, and the shape of the conclusion here, one existential block coupling characters, archimedean parameters, and a nonvanishing local average, is the template of their structure theorem for logarithmically averaged correlations [76]. The general even-order linear case is precisely the logarithmically averaged Elliott conjecture. All of the novelty of the present statement therefore sits at $$\max_j\deg P_j\ge2$$, where even the logarithmic mean value of $$f(n^2+1)$$ for a single nonpretentious completely multiplicative $$f$$ is open, and a logarithmic mean value theorem for $$f(n^2+1)$$ with a conclusion of the stated relative-pretentious type would be the first decisive theorem. The failure mode is a system of functions nonpretentious in every relative metric whose logarithmic correlation has positive limsup, which would reveal a correlation mechanism beyond the archimedean and finite local resonances.

*Remark.* The restriction to completely multiplicative $$f_j$$ is not cosmetic. For $$1$$-bounded multiplicative functions that are not completely multiplicative, the fixed-parameter form of the conclusion is false: Matomäki–Radziwiłł–Tao [71] constructed a $$1$$-bounded multiplicative function that pretends to be $$n^{it_k}$$ for different parameters $$t_k$$ on different scales, refuting the original fixed-parameter Elliott conjecture, and the corrected conjecture must allow the comparison parameter to vary with the scale $$X$$. For the unimodular completely multiplicative $$f_j$$ of the present statement the fixed-parameter form survives, and by a rigidity argument rather than by monotonicity alone. Fix a member $$f_j$$ of the system, a primitive Dirichlet character $$\chi$$, and scales $$X_k\le X_{k+1}$$, the scale index $$k$$ being unrelated to the function index $$j$$. If $$\chi n^{is_k}$$ and $$\chi n^{is_{k+1}}$$ are within bounded truncated distance of $$f_j$$ at the scales $$X_k$$ and $$X_{k+1}$$ respectively, monotonicity of the truncated distance in the scale places both within bounded distance of $$f_j$$ at the common scale $$X_k$$, the triangle inequality places them within bounded distance of each other, and the growth in $$X$$ of $$\sum_{p\le X}(1-\cos(\delta\log p))/p$$ for fixed $$\delta\ne0$$ then forces $$\vert s_{k+1}-s_k\vert =O(1/\log X_k)$$. After passing to a geometrically growing subsequence of the scales, $$\log X_{k+1}\ge2\log X_k$$ say, which monotonicity permits without weakening the conclusion, the increments are summable, the parameters converge, and monotonicity converts boundedness along the scales into finiteness of the full distance at the limit parameter. Unimodularity at the primes is consumed at the triangle-inequality step: the passage through the middle function $$f_j$$ rests on the identity $$\chi n^{is_k}\,\overline{\chi n^{is_{k+1}}}=(\chi n^{is_k}\,\bar f_j)(f_j\,\overline{\chi n^{is_{k+1}}})$$, valid at the primes exactly when $$\vert f_j(p)\vert =1$$, and for values of modulus less than one the two comparisons decouple on the primes where the modulus drops, which is exactly the room the scale-switching construction occupies.

*Remark.* For each $$j$$, the finitely many primes dividing $$\operatorname{disc}(P_j)\operatorname{lc}(P_j)$$, the discriminant times the leading coefficient, may be weighted arbitrarily: replacing the weights $$\rho_{P_j}(p)/p$$ at those primes by any bounded values changes $$\mathbb D_{P_j}(f,g)^2$$ by a bounded amount and leaves the finiteness condition (i) unchanged. The relative metric is therefore canonical up to the bad primes, and the conjecture is insensitive to that choice.

### Monotone threshold purification of vector paths

Let $$d,m\ge1$$. Let $$v_1,\ldots,v_m\in\mathbb R^d$$ satisfy $$\|v_i\|_2\le1$$, where $$\|\cdot\|_2$$ is the Euclidean norm. Let $$a_i:[0,1]\to[0,1]$$ be continuous nondecreasing functions with $$a_i(0)=0$$ and $$a_i(1)=1$$, called a monotone activation schedule, and define the fractional path

$$
F(t)=\sum_{i=1}^m a_i(t)v_i.
$$

A threshold rounding of $$F$$ is a choice of $$\tau_1,\ldots,\tau_m\in(0,1]$$ together with the pure path

$$
G(t)=\sum_{i:\ \tau_i\le t}v_i .
$$

**Monotone threshold purification of vector paths (Conjecture 52).** There exists a universal constant $$C<\infty$$ such that for every $$d,m\ge1$$, every $$(v_i)_{i\le m}$$, and every monotone activation schedule $$(a_i)_{i\le m}$$ as above, some threshold rounding satisfies

$$
\sup_{0\le t\le1}\|G(t)-F(t)\|_2\le C\sqrt d .
$$

*Significance.* The headline attribution comes first. The special case $$a_i(t)=t$$ for all $$i$$ with $$\sum_iv_i=0$$ is exactly the open prefix-sum form of the Euclidean Steinitz problem at the scale $$O(\sqrt d)$$: there $$F\equiv0$$, and ordering the vectors by their thresholds turns the display into the assertion that some permutation $$\pi$$ has all prefix sums bounded, $$\max_{k\le m}\|\sum_{i\le k}v_{\pi(i)}\|_2\le C\sqrt d$$. Grinberg–Sevast'yanov [65] proved the bound $$d$$ in every norm, the best known Euclidean bound is Banaszczyk’s [61, 62] $$O(\sqrt{d+\log m})$$, and so already in this special case the conjecture asserts the removal of the logarithmic term uniformly in $$m$$. For the general threshold form, even the existence of any bound $$C(d)$$ depending on $$d$$ alone and uniform in $$m$$ appears to be open. The mechanism is that $$F$$ is a monotone trajectory in the zonotope generated by the $$v_i$$, the set of sums $$\sum_i\lambda_iv_i$$ with $$\lambda_i\in[0,1]$$, and the conjecture asserts that every monotone zonotope path admits an integral shadow at the optimal Euclidean discrepancy scale. The order $$\sqrt d$$ is verified sharp: take $$m=d$$, $$v_i=e_i$$ the standard basis, and $$a_i(t)=t$$, so that at $$t=1/2$$ every coordinate of $$G(1/2)-F(1/2)$$ equals $$\pm1/2$$ whatever the thresholds, giving $$\|G(1/2)-F(1/2)\|_2=\sqrt d/2$$. No decisive theorem exists: the first would be any $$m$$-uniform bound $$C(d)$$ for the threshold form, even with a $$d$$-dependence far worse than $$\sqrt d$$. A falsification honesty note: since even the existence of a finite bound at each fixed $$d$$ is open, the conjecture can fail in two ways, at fixed dimension, through paths with $$d$$ fixed and $$m\to\infty$$ whose best threshold roundings have unbounded discrepancy, or asymptotically, through an infinite family of monotone paths with $$d\to\infty$$ every threshold rounding of which has discrepancy $$\omega(\sqrt d)$$. Small-$$d$$ computer searches at bounded $$m$$ cannot decide either failure mode.

### Entropy dimension of random-free graphons

A graphon is a symmetric measurable function $$W:[0,1]^2\to[0,1]$$, and $$W$$ is random-free if it takes values in $$\{0,1\}$$ almost everywhere. Define the row pseudometric

$$
d_W(x,y)=\int_0^1\vert W(x,z)-W(y,z)\vert \,\mathrm dz .
$$

Identifying points at zero distance and completing yields a metric-measure space $$(\Omega_W,d_W,\rho_W)$$, the row space, where $$\rho_W$$ is the pushforward of Lebesgue measure. The row space is Ahlfors $$s$$-regular if it is compact and there exist $$c,C,r_0>0$$ such that

$$
cr^s\le\rho_W(B(x,r))\le Cr^s
$$

for every $$x\in\operatorname{supp}\rho_W$$ and every $$0<r<r_0$$. Let $$G(n,W)$$ be the random labelled graph on $$[n]=\{1,\ldots,n\}$$ obtained from independent uniform $$U_1,\ldots,U_n$$ on $$[0,1]$$ by declaring $$ij$$ an edge exactly when $$W(U_i,U_j)=1$$, and let $$H(G(n,W))$$ be its Shannon entropy with natural logarithms.

**Entropy dimension of random-free graphons (Conjecture 53).** 

*(i)* [nonvacuity] For every $$s\in(0,2]$$ there exists a random-free graphon whose row space is Ahlfors $$s$$-regular.

*(ii)* [refined entropy-dimension law] If the row space of a random-free graphon $$W$$ is Ahlfors $$s$$-regular for some $$s>0$$, then $$H(G(n,W))=s\,n\log n+O_W(n)$$.

*Proposition (entropy-dimension limit law).* If the row space of a random-free graphon $$W$$ is Ahlfors $$s$$-regular for some $$s>0$$, then $$H(G(n,W))=s\,n\log n+O_W(n\log\log n)$$, and in particular $$\lim_{n\to\infty}H(G(n,W))/(n\log n)=s$$.

*Proof.* Write $$d=d_W$$ and $$\rho=\rho_W$$, and use natural logarithms. For the lower bound, set $$k=\lfloor n/\log n\rfloor$$, fix the labelling, and designate the last $$k$$ vertices as tests, with latent points $$Z=(Z_1,\ldots,Z_k)$$ and remaining latent points $$X_1,\ldots,X_{n-k}$$. The cross matrix $$M=(W(X_i,Z_j))_{i,j}$$ is a function of the labelled graph, and conditioning cannot increase entropy, so $$H(G(n,W))\ge H(M)\ge H(M\mid Z)$$. Conditionally on $$Z$$ the signature rows $$S_Z(X_i)=(W(X_i,Z_1),\ldots,W(X_i,Z_k))$$ are independent with a common law, whence $$H(M\mid Z)=(n-k)\,\mathbb E_Z H(S_Z(X))$$ with $$X$$ an independent uniform point. Let $$C_Z$$ be the collision probability of the signature law. Shannon entropy dominates the Rényi entropy of order two, so $$H(S_Z(X))\ge-\log C_Z$$, and convexity of $$-\log$$ gives $$\mathbb E_Z H(S_Z(X))\ge-\log\mathbb E_Z C_Z$$. For independent uniform $$X$$ and $$Y$$ the tests are independent uniform points, two rows agree at a test with probability $$1-d(X,Y)$$, and Fubini gives the exact identity $$\mathbb E_Z C_Z=\mathbb E_{X,Y}(1-d(X,Y))^{k}$$. Since $$(1-u)^k\le\mathrm e^{-ku}$$ and the upper mass bound gives $$\rho(B(x,r))\le Cr^s$$, a dyadic shell decomposition yields, uniformly in $$x$$,

$$
\int\mathrm e^{-k\,d(x,y)}\,\mathrm d\rho(y)\le\rho\bigl(B(x,1/k)\bigr)+\sum_{m\ge0}\mathrm e^{-2^{m}}\rho\bigl(B(x,2^{m+1}/k)\bigr)=O_W(k^{-s}).
$$

Hence $$\mathbb E_Z C_Z=O_W(k^{-s})$$, so $$\mathbb E_Z H(S_Z(X))\ge s\log k-O_W(1)$$ and $$H(G(n,W))\ge(n-k)(s\log k-O_W(1))=s\,n\log n-O_W(n\log\log n)$$.

For the upper bound, let $$\delta\in(0,\tfrac12)$$. The lower mass bound makes the balls of radius $$\delta/2$$ around a maximal $$\delta$$-separated set disjoint, each of mass at least $$c(\delta/2)^s$$, so the row space admits a Borel partition into $$N_\delta=O_W(\delta^{-s})$$ cells of diameter at most $$2\delta$$. Let $$Q_i$$ be the cell of the $$i$$th latent row. Subadditivity and conditioning give $$H(G(n,W))\le n\log N_\delta+\binom n2\,\mathbb E_{(a,b)}h(p_{ab})$$, where $$(a,b)$$ is the cell pair of two independent rows, $$p_{ab}$$ is the conditional edge probability, and $$h$$ is the binary entropy. For a $$\{0,1\}$$-valued $$W$$, draw independent latent points $$X,X'$$ with rows in the cell $$a$$ and independent latent points $$Y,Y'$$ with rows in the cell $$b$$, so that $$W(X,Y)$$ and $$W(X',Y')$$ are independent indicators of mean $$p_{ab}$$ and $$p_{ab}(1-p_{ab})=\tfrac12\mathbb P(W(X,Y)\ne W(X',Y'))$$, while the union bound gives $$\mathbb P(W(X,Y)\ne W(X',Y'))\le\mathbb P(W(X,Y)\ne W(X',Y))+\mathbb P(W(X',Y)\ne W(X',Y'))$$. Averaging each term over the opposite cell with its mass removes that cell restriction, so $$\mathbb E_{(a,b)}[p_{ab}(1-p_{ab})]\le\tfrac12\bigl(\mathbb E_a\mathbb E_{X,X'\in a}\,d(X,X')+\mathbb E_b\mathbb E_{Y,Y'\in b}\,d(Y,Y')\bigr)\le2\delta$$. The bound $$h(p)\le\varphi(p(1-p))$$ with the concave increasing $$\varphi(u)=2u(1+\log(1/u))$$ and Jensen give $$\mathbb E_{(a,b)}h(p_{ab})\le\varphi(2\delta)=O(\delta\log(1/\delta))$$. Therefore $$H(G(n,W))\le s\,n\log(1/\delta)+O_W(n)+O(n^2\delta\log(1/\delta))$$, and the choice $$\delta=(n\log^2n)^{-1}$$ gives $$H(G(n,W))\le s\,n\log n+O_W(n\log\log n)$$. ∎

*Remark.* The conjecture is the refinement of the error term of the proposition to $$O_W(n)$$, which lies beyond both bounds of the proof: locating the mispredicted edges of a resolution-$$1/n$$ code costs order $$n\log n$$ if done naively, and the two-scale correction that codes coarse types first stops at $$O(n\log\log n)$$.

*Significance.* The mechanism is metric distinguishability of rows: two row types at $$d_W$$-distance $$\varepsilon$$ disagree on an $$\varepsilon$$-fraction of potential neighbours and become statistically distinguishable against $$n$$ sampled vertices at a scale comparable to $$1/n$$, an Ahlfors $$s$$-regular row space has about $$n^s$$ distinguishable types at that scale, and the latent type of each of the $$n$$ labelled vertices then carries $$s\log n+O(1)$$ nats. Clause (i) certifies that the hypothesis class is nonvacuous at every fractional $$s$$: it is expected to be provable by Cantor-type threshold constructions, in which $$W$$ is the indicator of a threshold event read along a self-similar Cantor set, and it is included so that clause (ii) quantifies over a genuinely rich family. The nearest literature boundary is Hatami–Norine [66]: a graphon is random-free exactly when $$H(G(n,W))=o(n^2)$$, and every subquadratic growth order occurs for suitable random-free graphons, so no hypothesis short of a metric-measure condition on the row space can pin the coefficient of $$n\log n$$, and Ahlfors regularity is exactly the condition that does. The decisive theorem half-exists: the limit law is provable from regularity by the collision-entropy and quantization bounds of the proposition above, so the first theorem for the conjecture proper is the linear error term for one explicit self-similar threshold graphon of noninteger $$s$$, together with a proof of clause (i). The failure mode is a genuinely growing correction: an Ahlfors regular random-free graphon whose entropy exceeds $$s\,n\log n+C\,n$$ for every $$C$$ would show that the resolution-$$1/n$$ coding loss is intrinsic rather than an artefact of the two-scale method.

### A Hessian principle for isolated microcanonical graph phases

Fix a partition

$$
[0,1]=I_1\sqcup\cdots\sqcup I_q,
\qquad\vert I_a\vert =\alpha_a>0 .
$$

A coloured graphon is a symmetric measurable $$U:[0,1]^2\to[0,1]$$ considered together with this fixed colour partition. Let $$p(U)\in[0,1]^D$$ with $$D=q(q+1)/2$$ denote the block-average vector

$$
p_{ab}(U)=\frac1{\vert I_a\vert \vert I_b\vert }\int_{I_a\times I_b}U(x,y)\,\mathrm
dx\,\mathrm dy,
\qquad 1\le a\le b\le q .
$$

A coloured finite graph is a finite simple graph $$F$$ with a colour $$c(v)\in\{1,\ldots,q\}$$ attached to each vertex, and its coloured homomorphism density in $$U$$ is

$$
t(F,U)=\int_{[0,1]^{V(F)}}
\prod_{v\in V(F)}\alpha_{c(v)}^{-1}\mathbf 1_{I_{c(v)}}(x_v)
\prod_{uv\in E(F)}U(x_u,x_v)
\prod_{v\in V(F)}\mathrm dx_v .
$$

Fix coloured finite graphs $$F_1,\ldots,F_k$$ and put $$\mathbf t(U)=(t(F_1,U),\ldots,t(F_k,U))$$. Define the graphon entropy

$$
\mathcal S(U)=\frac12\int_{[0,1]^2}
\bigl[-U\log U-(1-U)\log(1-U)\bigr]\,\mathrm dx\,\mathrm dy,
$$

with $$0\log0=0$$, and for a feasible constraint vector $$\mathbf a$$ the contracted entropy

$$
\Psi_{\mathbf a}(p)=\sup\{\mathcal S(U):
\mathbf t(U)=\mathbf a,\ p(U)=p\}.
$$

The finite graphs are coloured with pinned classes. For each $$n$$ set $$n_a=\lfloor\alpha_an\rfloor$$ and $$N_n=\sum_an_a$$, and fix a partition of the vertex set $$[N_n]$$ into colour classes $$V_1,\ldots,V_q$$ with $$\vert V_a\vert =\lfloor\alpha_an\rfloor$$ exactly, so that $$N_n=n+O(q)$$. For a graph $$G$$ on $$[N_n]$$ with these colour classes, partition each $$I_a$$ into $$n_a$$ consecutive intervals of length $$\vert I_a\vert /n_a$$ assigned to the vertices of $$V_a$$, let $$U_G$$ be the $$\{0,1\}$$-valued coloured graphon equal to $$1$$ on a product of two vertex intervals exactly when the corresponding pair is an edge, and put $$\mathbf t(G)=\mathbf t(U_G)$$ and $$\widehat p(G)=p(U_G)$$.

Fix $$0<\eta<1$$ and assume the following regularity hypotheses.

*(H1)* The supremum of $$\mathcal S(U)$$ over $$\mathbf t(U)=\mathbf a$$ is attained at a unique coloured graphon $$U_*$$, up to measure-preserving maps preserving each colour class.

*(H2)* Writing $$p_*=p(U_*)$$, the feasible block-average set $$\{p(U):\mathbf t(U)=\mathbf a\}$$ is, near $$p_*$$, a $$C^3$$ embedded manifold $$M\subset\mathbb R^D$$.

*(H3)* The restriction $$\Psi_{\mathbf a}\vert _M$$ is $$C^3$$ near $$p_*$$ and has there a unique local maximum.

*(H4)* The quadratic form $$A=-D^2_M\Psi_{\mathbf a}(p_*)$$ is positive definite on the tangent space $$T=T_{p_*}M$$.

*(H5)* [transversally Lipschitz constraint correspondence] There exist $$\delta_0>0$$ and $$L<\infty$$ such that every coloured graphon $$U$$ with $$\|p(U)-p_*\|\le\delta_0$$ and $$\|\mathbf t(U)-\mathbf a\|_\infty=\delta\le\delta_0$$ satisfies $$\operatorname{dist}(p(U),M)\le L\delta$$. In particular the conditioning window below confines $$\widehat p_n$$, on the event $$\|\widehat p_n-p_*\|\le\delta_0$$, to an $$o(n^{-1})$$ thickening of $$M$$.

*(H6)* [nonemptiness] For every sufficiently large $$n$$ the conditioning set $$\{G:\|\mathbf t(G)-\mathbf a\|_\infty\le n^{-1-\eta}\}$$ over graphs $$G$$ on $$[N_n]$$ with the pinned colour classes is nonempty.

Let $$G_n$$ be uniform on the conditioning set of (H6), let $$\widehat p_n=\widehat p(G_n)$$, and let $$\Pi_T$$ be orthogonal projection of $$\mathbb R^D$$ onto $$T$$.

**Hessian principle for an isolated microcanonical phase (Conjecture 54).** Under hypotheses (H1)–(H6),

$$
n\,\Pi_T\bigl(\widehat p_n-\mathbb E\,\widehat p_n\bigr)
\xrightarrow{\ d\ }
N_T(0,A^{-1}),
$$

where $$N_T(0,A^{-1})$$ denotes the centred Gaussian law on $$T$$ whose precision form is $$A$$.

*Significance.* The mechanism is a Laplace expansion at the dense-graph entropy exponent $$n^2$$: on the feasible manifold, $$\Psi_{\mathbf a}(p_*+u)=\Psi_{\mathbf a}(p_*)
-\tfrac12\langle Au,u\rangle+O(\|u\|^3)$$, so the fluctuation scale is $$u\asymp n^{-1}$$ and the predicted covariance on the tangent space is $$A^{-1}$$, while (H5) suppresses the transversal directions below the fluctuation scale, which is exactly why the conclusion is stated only after projection by $$\Pi_T$$ and centring at $$\mathbb E\,\widehat p_n$$. The nearest literature boundary is the Chatterjee–Varadhan [63] large deviation principle, which supplies the $$n^2$$ normalization and the variational description of conditioned dense graphs, together with the multipodal structure theory of Kenyon–Radin–Ren–Sadun [67] and Neeman–Radin–Sadun [72] (constrained entropy maximizers are step-function graphons with finitely many blocks), which makes hypotheses (H1)–(H4) verifiable in concrete constrained ensembles. A scale audit disposes of one suspect: a single edge toggle moves each coordinate of $$\mathbf t(G)$$ by $$O(n^{-2})$$, so the lattice of attainable constraint values has spacing of order $$n^{-2}$$, far below the fluctuation scale $$n^{-1}$$, and the genuine risk is therefore Laplace-ratio control, namely uniform comparison of microcanonical counts with their Laplace approximations across windows of width $$o(n^{-1})$$, not arithmetic oscillation. Nonemptiness (H6) is a genuine hypothesis and may fail along subsequences of $$n$$ for arithmetic reasons, in which case the statement is asserted only along the subsequence where it holds. No decisive theorem exists at this generality: the natural first one is the case $$q=1$$ with the edge-triangle constraint pair in a region where the entropy maximizer is bipodal, a two-block step function, and (H1)–(H5) have been verified. The failure mode is an isolated nondegenerate phase whose tangent fluctuations are non-Gaussian or live at a different scale, which would necessarily come from a failure of Laplace-ratio control. The conjectural content is exactly that (H1)–(H6) already force this local regularity: a subexponential prefactor in the microcanonical counts varying across the conditioning window would leave every hypothesis intact while tilting the limit away from $$N_T(0,A^{-1})$$, and the conjecture asserts that isolated nondegenerate phases exclude it.

### Sharp stability of entropy idempotence on finite abelian groups

Let $$G$$ be a finite abelian group and $$\mu$$ a probability measure on $$G$$. Write $$H(\mu)$$ for Shannon entropy with natural logarithms, $$\mu*\mu$$ for the convolution, the law of $$X+Y$$ with $$X,Y$$ independent of law $$\mu$$, and

$$
\Delta(\mu)=H(\mu*\mu)-H(\mu)
$$

for the convolution entropy defect. If $$H\le G$$ is a subgroup and $$a\in G$$, let $$u_{a+H}$$ be the uniform measure on the coset $$a+H$$. Total variation distance is

$$
\|\mu-\nu\|_{\mathrm{TV}}=\frac12\sum_{x\in G}\vert \mu(x)-\nu(x)\vert  .
$$

**Sharp stability of entropy idempotence (Conjecture 55).** There exists a universal constant $$C<\infty$$ such that for every finite abelian group $$G$$ and every probability measure $$\mu$$ on $$G$$,

$$
\inf_{\substack{H\le G\\a\in G}}
\|\mu-u_{a+H}\|_{\mathrm{TV}}^2
\le
C\bigl(H(\mu*\mu)-H(\mu)\bigr).
$$

*Remark.* The equality case is verified. With $$X,Y$$ independent of law $$\mu$$,

$$
\Delta(\mu)=H(X+Y)-H(X)=H(X+Y)-H(X+Y\mid Y)=I(X+Y;Y)\ge0,
$$

where $$I$$ denotes mutual information. If $$\Delta(\mu)=0$$ then $$X+Y$$ is independent of $$Y$$, which forces the translates of $$\mu$$ by the elements of its support to coincide, and hence forces $$\mu$$ to be uniform on a coset of a subgroup. The right-hand side therefore vanishes exactly on the proposed extremizers.

*Significance.* The mechanism is that the defect is the mutual information created by one self-convolution, so the conjecture is a dimension-free quantitative classification of near-idempotent measures with cosets as the exact equality case. The sharpness discussion identifies the extremal geometry. Coset perturbations $$\mu=(1+\varepsilon f)u_H$$ with $$\sum_{x\in H}f(x)=0$$ give, as $$\varepsilon\to0$$, the ratio

$$
\frac{\|\mu-u_H\|_{\mathrm{TV}}^2}{\Delta(\mu)}
\longrightarrow
\frac{(\mathbb E\vert f\vert )^2}{2\,\mathbb E f^2}\le\frac12
$$

by Cauchy–Schwarz, so perturbative examples certify at most the constant $$1/2$$. The near-extremizers are instead discretized Gaussians at intermediate scale on $$\mathbb Z/p\mathbb Z$$: for $$1\ll\sigma(p)\ll p$$, the discretization $$\mu_p$$ of a centred Gaussian of standard deviation $$\sigma(p)$$ has $$\Delta(\mu_p)\to\tfrac12\log2$$, the entropy-power constant recording the entropy gain of doubling a Gaussian variance, while its total variation distance to every $$u_{a+H}$$ tends to $$1$$, since the only subgroups of $$\mathbb Z/p\mathbb Z$$ are trivial and full and $$\mu_p$$ is asymptotically singular to every point mass and to the uniform measure. Hence $$C\ge2/\log2$$, and we conjecture that the sharp constant is exactly $$2/\log2$$. The positioning against the literature is as follows: the known entropic inverse theorems, Tao’s sumset entropy theory [74] and the entropic polynomial Freiman–Ruzsa theorem of Gowers–Green–Manners–Tao [64], conclude in Ruzsa distance, an entropic closeness of $$X$$ to a subgroup-uniform variable, not in total variation, and the total variation form over all finite abelian groups is neither proven nor refuted by them. On $$\mathbb Z/p\mathbb Z$$ there are no proper nontrivial subgroups, so the conjecture specializes to a discrete entropy-power-type lower bound for spread measures: any $$\mu$$ far in total variation from every point mass and from the uniform measure must create a definite amount of entropy under self-convolution. No decisive theorem exists: the natural first one is precisely that $$\mathbb Z/p\mathbb Z$$ specialization with some constant. The defect also has the exact form $$H(\mu*\mu)-H(\mu)=\mathbb E_Y D_{\mathrm{KL}}(\tau_Y\mu\,\Vert\,\mu*\mu)$$, with $$\tau_y$$ translation by $$y$$, so a small defect makes typical support-translates of $$\mu$$ close to $$\mu*\mu$$ in relative entropy, and Pinsker's inequality converts that closeness to total variation: the route to a universal constant is to upgrade approximate invariance under many translations to proximity to a coset uniform. The failure mode is a sequence $$\mu_n$$ with $$\Delta(\mu_n)\to0$$ whose coset distance is much larger than $$\sqrt{\Delta(\mu_n)}$$, and the natural hunting ground is measures straddling several subgroup scales inside groups with rich subgroup lattices, a family for which computational search through $$\mathbb Z/2^{8}\mathbb Z$$ finds no ratio $$\|\mu-u_{a+H}\|_{\mathrm{TV}}^2/\Delta(\mu)$$ above the discretized-Gaussian value $$2/\log2$$. The assertion has three layers of decreasing confidence: the existence of some universal constant, the sharp value $$2/\log2$$, and the classification of near-extremizers as the discretized Gaussians at intermediate scale.

### Stationary convolution-entropy rigidity

Let $$K$$ be a finite abelian group and $$\Omega=K^{\mathbb Z}$$ with coordinatewise addition and the left shift $$\sigma$$. Let $$\mu$$ be a $$\sigma$$-invariant ergodic Borel probability measure on $$\Omega$$, and write $$h_\sigma(\mu)$$ for its Kolmogorov–Sinai entropy. Define the translational stabilizer

$$
H_\mu=\{h\in K^{\mathbb Z}:(\tau_h)_*\mu=\mu\},
\qquad\tau_h(x)=x+h,
$$

a closed shift-invariant subgroup of $$K^{\mathbb Z}$$, and let $$\pi_\mu:K^{\mathbb Z}\to K^{\mathbb Z}/H_\mu$$ be the quotient homomorphism. Let $$\mu*\mu$$ be the law of $$X+Y$$ for independent $$X,Y\sim\mu$$.

**Stationary convolution-entropy rigidity (Conjecture 56).** For every shift-ergodic $$\mu$$,

$$
h_\sigma(\mu*\mu)=h_\sigma(\mu)
\quad\Longleftrightarrow\quad
h_\sigma\bigl((\pi_\mu)_*\mu\bigr)=0 .
$$

*Remark.* The binary specialization deserves prominence. Take $$K=\mathbb Z/2\mathbb Z$$. By Kitchens’ structure theory of group shifts [68], every closed shift-invariant subgroup of $$(\mathbb Z/2\mathbb Z)^{\mathbb Z}$$ is a group shift of finite type, and every proper one is the solution set of a nontrivial linear recurrence and hence finite. If $$H_\mu$$ is finite the quotient map has finite fibres and $$h_\sigma((\pi_\mu)_*\mu)=h_\sigma(\mu)$$, while if $$H_\mu$$ is everything then $$\mu$$ is the Haar measure, the uniform Bernoulli process, with entropy $$\log2$$. Since $$h_\sigma(\mu*\mu)\ge h_\sigma(\mu)$$ always, by conditioning on one summand, the conjecture therefore asserts: every ergodic binary process with $$0<h_\sigma(\mu)<\log2$$ gains entropy under independent XOR, the coordinatewise sum modulo $$2$$ with an independent copy.

*Proposition (Easy direction, conditional).* Suppose $$h_\sigma((\pi_\mu)_*\mu)=0$$. Assume the following two ingredients.

*(a)* The Abramov–Rokhlin entropy addition formula holds for the Haar-fibred compact group extension $$\pi_\mu:(\Omega,\mu,\sigma)\to(\Omega/H_\mu,(\pi_\mu)_*\mu,\sigma)$$ and for the corresponding extension of $$\mu*\mu$$, so that each total entropy splits as the quotient entropy plus the common Haar fibre entropy, the conditional measures of $$\mu$$ and of $$\mu*\mu$$ over the quotient being Haar measures on cosets of $$H_\mu$$.

*(b)* The entropy of a factor of an independent joining is bounded by the sum of the entropies of the factors, so that $$(\pi_\mu)_*(\mu*\mu)=((\pi_\mu)_*\mu)*((\pi_\mu)_*\mu)$$ has entropy at most $$2h_\sigma((\pi_\mu)_*\mu)=0$$.

Then $$h_\sigma(\mu*\mu)=h_\sigma(\mu)$$.

*Significance.* The mechanism is the stationary analogue of entropy idempotence on a finite group: equality of entropy under independent self-convolution should force all positive entropy to be Haar-type randomness along a translation-invariant subgroup process, modulo a quotient that may retain arbitrarily rich zero-entropy dynamics such as rotations, substitutions, or Toeplitz systems. The easy direction is recorded above as a conditional proposition with its two ingredients named, the Abramov–Rokhlin formula for Haar-fibred compact group extensions and the factor-of-joining entropy bound, and the difficult direction is the rigidity claim that no other equality mechanism exists. The nearest literature boundary consists of Kułaga-Przymus–Lemańczyk [69] on the entropy of products of independent stationary processes and Lindenstrauss–Meiri–Peres [70] on the entropy of convolutions, neither of which decides the binary specialization above. No decisive theorem appears to be on record even for Markov processes, and strict XOR entropy gain for mixing two-state Markov chains would be the first. The failure-mode honesty note is this: the natural counterexample hunting ground is the Ornstein–Weiss [73] bilaterally deterministic processes, positive entropy processes whose distant past and distant future jointly determine the whole trajectory, together with $$T,T^{-1}$$-type constructions (skew products driven by a random walk, in the style of Kalikow), and no search has yet probed either family, so the negation of the conjecture has an unexplored natural habitat. The gap the rigidity must close is quantitative: equality of entropy rates asserts only that the block mutual information $$I(X_{1:n}+Y_{1:n};Y_{1:n})$$ is $$o(n)$$, not that it is bounded, so sublinear information spread through arbitrarily long-range structure is the resource a counterexample would exploit. The natural staircase of evidence runs from independent letters through Markov and mixing processes to completely positive entropy.

## Part IV: the class-counting polynomial of graphical Lie algebras

*Added to the deposit: 5 August 2026.*

The twenty conjectures below concern a single canonical object, the class-counting polynomial of a finite graph, approached through the two-step nilpotent Lie algebras that realize it as a rank generating function. They form three programmes. A rigidity and reconstruction programme (Conjectures 57 to 66) asserts that coarse specializations of the polynomial already determine it and that the polynomial in turn determines classical invariants. A log-concavity programme (Conjectures 67 to 71) locates the exact strength of positivity that the coefficient arrays support, with the boundary calibrated by explicit counterexamples one level higher. A tree extremal programme (Conjectures 72 to 76) places the path and the star at the two ends of every ordering the polynomial induces on trees. The proved layer is separated from the conjectural one: the rank formula and the two lower bounds on the number of rank values in a tree are theorems with full proofs, joined by the equality cases of those bounds and the reduction of the star majorization to a single anti-concentration bound, and every conjecture is stated against that floor. Each statement is held to the standard of the rest of the collection: a canonical object, a stated mechanism, the nearest literature boundary, a first decisive theorem where one exists, and an honest failure mode. Two statements, Conjectures 63 and 71, have since been resolved false by explicit counterexamples recorded with them, a seven-vertex unicyclic pair and a connected eight-vertex graph respectively, and both are retained with their resolutions rather than renumbered.

For a finite simple graph $$G$$ on vertex set $$V(G)$$ with edge set $$E(G)$$ and a field $$F$$, the graphical Lie algebra $$L_G(F)$$ is the two-step nilpotent Lie algebra over $$F$$ with basis $$\{v_i:i\in V(G)\}$$ together with the central basis $$\{z_e:e\in E(G)\}$$, the bracket being $$[v_a,v_b]=z_{ab}$$ for each edge $$\{a,b\}$$ with $$a<b$$, $$[v_b,v_a]=-z_{ab}$$, and all other brackets of basis vectors zero. For $$S\subseteq V(G)$$ write $$N_G[S]$$ for the closed neighbourhood of $$S$$, the set of vertices lying in $$S$$ or adjacent to it, and $$c(G[S])$$ for the number of connected components of the induced subgraph $$G[S]$$, and set

$$
\rho_G(S)=\bigl\vert N_G[S]\bigr\vert -c(G[S]),\qquad\rho_G(\emptyset)=0 .
$$

*Proposition (rank formula).* Let $$G$$ be a graph on $$n$$ vertices, let $$F$$ be a field, and let $$x\in L_G(F)$$ have vertex part supported on $$S$$, all coordinates $$x_i$$ with $$i\in S$$ being nonzero. Then $$\operatorname{rank}(\operatorname{ad}_x)=\rho_G(S)$$, independently of the field and of the nonzero values.

*Proof.* The map $$\operatorname{ad}_x$$ kills the centre and sends $$v_j$$ to $$\sum_{i\in S,\,i\sim j}\pm x_iz_{ij}$$, so $$\operatorname{rank}(\operatorname{ad}_x)$$ is the rank of the linear map $$y\mapsto[x,y]$$ on the vertex space, whose coefficient at $$z_{ab}$$ is $$x_ay_b-x_by_a$$. A vector $$y$$ lies in the kernel if and only if $$x_ay_b=x_by_a$$ for every edge $$\{a,b\}$$. If both endpoints lie in $$S$$ this forces the ratio $$y_i/x_i$$ to be constant along edges of $$G[S]$$, one free parameter per connected component of $$G[S]$$. If exactly one endpoint $$a$$ lies in $$S$$ it forces $$y_b=0$$, for every $$b\in N(S)\setminus S$$. Edges with neither endpoint in $$S$$ impose nothing, so $$y_j$$ is free for every $$j$$ outside $$N[S]$$. Hence $$\dim\ker=(n-\vert N[S]\vert )+c(G[S])$$, and the rank is $$\vert N[S]\vert -c(G[S])$$. ∎

The formula was verified before it was proved: on eighteen thousand random pairs of a graph and an element, the rank of $$\operatorname{ad}_x$$ computed by direct linear algebra over $$\mathbb F_2$$, $$\mathbb F_3$$, and $$\mathbb F_5$$ agreed with $$\rho_G(S)$$ in every case, and the proof above was written only afterwards.

The class-counting polynomial of $$G$$ is

$$
C_G(X,Y)=\sum_{S\subseteq V(G)}(X-1)^{\vert S\vert }\,Y^{\rho_G(S)} .
$$

The polynomial is Rossmann's [77]: he introduced it, proved that its specializations enumerate the conjugacy classes of graphical groups over $$\mathbb F_q$$ by size, proved the multiplicativity $$C_{G\sqcup H}=C_G\,C_H$$ over disjoint unions, and showed that the cardinalities of the connected dominating sets of $$G$$ can be read off from it. Set

$$
H_G(U,Y)=C_G(1+U,Y),\qquad
F_G(X,Y)=X^{\vert E(G)\vert }\,C_G(X,X^{-1}Y),\qquad
f_G(X)=F_G(X,1),
$$

so that the coefficient of $$U^kY^r$$ in $$H_G$$ counts the sets $$S$$ with $$\vert S\vert =k$$ and $$\rho_G(S)=r$$. At $$X=q$$ the polynomial records the distribution of $$\operatorname{rank}(\operatorname{ad}_x)$$ over $$L_G(\mathbb F_q)$$, by the rank formula. The subgraph-component polynomial of Tittmann–Averbouch–Makowsky [78] is

$$
Q_G(U,W)=\sum_{S\subseteq V(G)}U^{\vert S\vert }\,W^{c(G[S])} .
$$

For a tree $$T$$ on $$n$$ vertices let $$s(T)$$ be the number of distinct values taken by $$\rho_T$$, let $$\ell(T)$$ be the number of leaves, and let $$\operatorname{diam}(T)$$ be the diameter.

*Lemma (two lower bounds on the number of rank values).* For every tree $$T$$ on $$n\ge2$$ vertices, $$s(T)\ge n-\ell(T)+2$$ and $$s(T)\ge\operatorname{diam}(T)+1$$.

*Proof.* For the first bound, when $$n=2$$ the values $$0$$ and $$1$$ occur. For $$n\ge3$$ the internal vertices, those that are not leaves, induce a subtree with $$m=n-\ell(T)\ge1$$ vertices. Order them $$v_1,\ldots,v_m$$ by breadth-first search from an internal root, so that every prefix $$S_j=\{v_1,\ldots,v_j\}$$ is connected and $$\rho(S_j)=\vert N[S_j]\vert -1$$. Each $$v_{j+1}$$ has degree at least two in $$T$$ and its parent lies in the prefix, so it has a neighbour $$c$$ on the far side, whose only neighbour inside $$N[S_j]$$ could be $$v_{j+1}$$ itself, which is not in $$S_j$$. Hence $$c$$ lies in $$N[S_{j+1}]$$ but not in $$N[S_j]$$, the sizes strictly increase, and the chain realizes $$m$$ distinct values, all at least $$\deg(v_1)\ge2$$. Together with $$\rho(\emptyset)=0$$ and the value $$1$$ at a single leaf this gives at least $$m+2=n-\ell(T)+2$$ values. For the second bound take a diametral path $$v_0,v_1,\ldots,v_d$$ with $$d=\operatorname{diam}(T)$$, whose endpoint $$v_0$$ is a leaf. For the prefixes $$S_j=\{v_0,\ldots,v_{j-1}\}$$ with $$1\le j\le d$$, the vertex $$v_{j+1}$$ witnesses strict growth of $$\vert N[S_j]\vert $$ as long as it exists, since a tree has no edge from $$v_{j+1}$$ back into $$\{v_0,\ldots,v_{j-1}\}$$. The chain realizes $$d$$ distinct values starting from $$\rho(S_1)=1$$, and $$\rho(\emptyset)=0$$ gives $$d+1$$ in total. ∎

*Proposition (equality cases of the bounds: path and star).* The path $$P_n$$ has $$s(P_n)=n$$ for every $$n\ge2$$, and the star $$K_{1,n-1}$$ has $$s(K_{1,n-1})=3$$ for every $$n\ge3$$. Both trees attain equality in each bound of the lemma.

*Proof.* For a connected graph on $$n$$ vertices and a nonempty subset $$S$$ one has $$1\le\rho(S)\le n-1$$, the lower bound because a single vertex gives $$\rho(\{v\})=\deg(v)\ge1$$ and the upper because $$\vert N[S]\vert \le n$$ and $$c(G[S])\ge1$$. With $$\rho(\emptyset)=0$$ this leaves at most $$n$$ distinct values, so $$s(T)\le n$$ for every tree $$T$$. The path has $$\operatorname{diam}(P_n)=n-1$$, so the lemma gives $$s(P_n)\ge n$$, forcing $$s(P_n)=n$$, and with $$\ell(P_n)=2$$ both $$n-\ell(P_n)+2$$ and $$\operatorname{diam}(P_n)+1$$ equal $$n$$. For the star with $$n\ge3$$, the rank formula gives attained ranks $$\{0,1,n-1\}$$, so $$s(K_{1,n-1})=3$$, and with $$\ell(K_{1,n-1})=n-1$$ and $$\operatorname{diam}(K_{1,n-1})=2$$ both $$n-\ell+2$$ and $$\operatorname{diam}+1$$ equal $$3$$. ∎

### Rigidity and reconstruction

**Conjecture 57** *(Irreducibility and connectivity)*. For every graph $$G$$ with at least one vertex, $$H_G(U,Y)$$ is irreducible in $$\mathbb Z[U,Y]$$ if and only if $$G$$ is connected.

*Significance.* Rossmann's multiplicativity [77] makes the disconnected direction immediate, each factor being nonconstant since $$H_{K_1}=1+U$$, so the content is the connected direction. The mechanism is that a factorization of $$H_G$$ would express the joint array of $$(\vert S\vert ,\rho_G(S))$$ over all vertex subsets as a product of two smaller arrays, which is exactly what a separation of $$G$$ into two vertex-disjoint parts produces, and the conjecture asserts that no other source of such a product structure exists: connectivity of the graph should be readable as algebraic indecomposability of the polynomial. The nearest literature boundary is the multiplicativity theorem itself, which supplies one direction and gives the statement its shape. The verification is exact rather than probabilistic: all $$996$$ connected graphs on at most seven vertices have irreducible $$H_G$$, by exact factorization over $$\mathbb Z$$. A first decisive theorem would be irreducibility of $$H_{P_n}$$ for the paths, a one-parameter family at the bottom of the connectivity hierarchy. The failure mode is a connected graph whose polynomial factors, which would reveal a product structure in the rank array not induced by any decomposition of the graph and would make the polynomial blind to connectivity.

**Conjecture 58** *(Recovery of the subgraph-component polynomial)*. For all graphs $$G$$ and $$H$$, $$C_G=C_H$$ implies $$Q_G=Q_H$$.

*Significance.* The two polynomials record transverse marginals of the induced-subgraph structure: $$C_G$$ records the joint distribution of $$(\vert S\vert ,\,\vert N_G[S]\vert -c(G[S]))$$ over all vertex subsets and $$Q_G$$ the joint distribution of $$(\vert S\vert ,\,c(G[S]))$$, and no functional relation between the two arrays is apparent, so the mechanism must be rigidity of the pairs of arrays that actually arise from graphs. The nearest literature boundary pairs the two sources: the class-counting polynomial and its enumerative theorems are Rossmann's [77], the subgraph-component polynomial is Tittmann–Averbouch–Makowsky's [78], and no bridge between them is on record. The polynomial $$C_G$$ does not determine the graph, and every known collision class was tested: the $$119$$ collision classes among the $$1252$$ graphs on at most seven vertices, a randomized eight-vertex corpus, the unique collision class among all $$3159$$ trees on fourteen vertices (there is none through thirteen, and the class was refound independently by exhaustive search), and the first unicyclic collision at ten vertices. In every class $$Q_G$$ agrees, as do the domination invariants of Conjectures 65 and 66. A first decisive theorem would be a derivation of $$Q_T$$ from $$C_T$$ for trees. The failure mode is a $$C$$-collision pair with distinct $$Q$$, which would show that the closed-neighbourhood array and the component array are genuinely independent invariants and would break the entire recovery programme at its first joint.

**Conjecture 59** *(Two-field rigidity)*. If $$C_G(2,Y)=C_H(2,Y)$$ and $$C_G(3,Y)=C_H(3,Y)$$, then $$C_G=C_H$$. Equivalently, the adjoint-rank distributions of the graphical Lie algebras over $$\mathbb F_2$$ and $$\mathbb F_3$$ determine them over every finite field.

*Significance.* The two hypotheses are the unweighted and the $$2^{\vert S\vert }$$-weighted rank statistics, $$C_G(2,Y)=\sum_SY^{\rho_G(S)}$$ and $$C_G(3,Y)=\sum_S2^{\vert S\vert }Y^{\rho_G(S)}$$, and recovering a nonnegative integer array from these two evaluations is impossible for general arrays, so the mechanism is rigidity of the arrays that graphs realize rather than linear algebra. The equivalence with the finite-field form is the rank formula, and the nearest literature boundary is Rossmann's enumeration theorem [77], through which the conjecture reads: two conjugacy-class censuses, over $$\mathbb F_2$$ and $$\mathbb F_3$$, determine the census over every finite field. The verification is exhaustive on at most seven vertices and covers six thousand random eight-vertex graphs. A first decisive theorem would be two-field rigidity for trees. The failure mode is a pair of graphs agreeing over $$\mathbb F_2$$ and $$\mathbb F_3$$ yet separated over some larger field, which would reveal genuinely field-dependent information in the adjoint-rank distribution and would locate it at a specific weight $$(q-1)^{\vert S\vert }$$.

**Conjecture 60** *(Hybrid rigidity)*. If $$C_G(2,Y)=C_H(2,Y)$$ and $$Q_G=Q_H$$, then $$C_G=C_H$$.

*Significance.* The mechanism is complementarity of marginals: the binary specialization carries the rank distribution and $$Q_G$$ carries the joint size-and-component array, and the conjecture asserts that these two projections of the induced-subgraph data jointly pin the full class-counting polynomial. The pairing is calibrated against a cheaper substitute, since $$C_G(2,Y)$$ together with the degree sequence does not determine $$C_G$$, so the component information in $$Q_G$$ is doing work that no degree data can do. The nearest literature boundary is again the pair Rossmann [77] and Tittmann–Averbouch–Makowsky [78], whose polynomials the hypothesis mixes. The verification is exhaustive on at most seven vertices. A first decisive theorem would be the tree case. The failure mode is a pair agreeing in both hypotheses but not in $$C$$, which would show that the joint array holds correlation information invisible to this pair of its natural projections.

**Conjecture 61** *(Binary edge-deck reconstruction)*. For graphs $$G$$ and $$H$$ with at least four edges each, if the multisets $$\{C_{G-e}(2,Y):e\in E(G)\}$$ and $$\{C_{H-e}(2,Y):e\in E(H)\}$$ coincide, then $$G$$ and $$H$$ are isomorphic.

*Significance.* This is the high-risk member of the part, in the orbit of the edge reconstruction conjecture, for which Bondy–Hemminger [79] is the survey. Each card here retains only the binary rank distribution of an edge-deleted subgraph rather than its isomorphism type, so the deck is a drastic coarsening of the classical edge deck, and the mechanism is that rank distributions vary so tightly under single-edge deletion that the multiset of shadows should already separate graphs. The nearest literature boundary is the reconstruction literature surveyed in [79], against which the present statement trades weaker cards for the same conclusion. The verification is exhaustive on at most seven vertices among graphs with at least four edges. A first decisive theorem would be reconstruction of trees from the binary deck. The failure mode is a nonisomorphic pair with equal binary decks, which would measure exactly how much the rank distribution forgets under edge deletion, and a counterexample here would be the least surprising in the part, which is why the statement is flagged as its stress point.

**Conjecture 62** *(Bipartite binary rigidity)*. For bipartite graphs $$G$$ and $$H$$, $$C_G(2,Y)=C_H(2,Y)$$ implies $$C_G=C_H$$.

*Significance.* A single specialization cannot determine the polynomial in general, since the implication fails already for connected unicyclic graphs on seven vertices (the resolution of Conjecture 63), so the mechanism is that a hereditary class restriction removes the room in which the unweighted rank distribution and the size-weighted array can decouple. The nearest literature boundary is Rossmann's specialization theorem [77], which gives the hypothesis its meaning as the $$\mathbb F_2$$ census. The verification is a six-thousand-graph random holdout of bipartite graphs on nine to twelve vertices, spanning $$2747$$ distinct binary specializations, with no violation. A first decisive theorem would be the tree case, shared with the surviving tree layer of Conjecture 63. The failure mode is a bipartite pair with equal binary specialization and distinct $$C$$, which would locate the boundary of one-field rigidity strictly inside the bipartite world and would redirect the class-restriction programme towards sparser families.

**Conjecture 63** *(Connected-pseudoforest binary rigidity, resolved false)*. For $$G$$ and $$H$$ each a tree or a connected unicyclic graph, $$C_G(2,Y)=C_H(2,Y)$$ implies $$C_G=C_H$$.

*Remark (resolution).* The conjecture is false as stated. The connected unicyclic graphs on vertex set $$\{0,\ldots,6\}$$ with edge sets $$\{\{0,3\},\{0,4\},\{1,2\},\{1,3\},\{1,4\},\{3,6\},\{4,5\}\}$$ and $$\{\{0,1\},\{0,3\},\{0,4\},\{1,2\},\{2,5\},\{2,6\},\{5,6\}\}$$, a four-cycle carrying three leaves against a triangle carrying a three-vertex path with two further leaves, share the binary specialization $$C(2,Y)=1+3Y+7Y^2+29Y^3+32Y^4+40Y^5+16Y^6$$ while their class-counting polynomials differ already in the singleton stratum, whose coefficients record the degree multisets $$\{1,1,1,2,3,3,3\}$$ and $$\{1,1,2,2,2,3,3\}$$. An exhaustive scan shows the pair is the unique violating class among all trees and connected unicyclic graphs through nine vertices. One member is bipartite and not chordal and the other chordal and not bipartite, and the ternary specializations differ, so Conjectures 62, 64, and 59 are untouched. The tree case survives exhaustively through fourteen vertices and remains open. Connectedness was in any case not the failure boundary, since the implication also fails for disconnected pseudoforests.

*Significance.* The statement is retained with its resolution because the failure is itself informative. The refuting pair shows that on unicyclic graphs the binary rank distribution can forget the degree multiset, the coarsest datum beyond the vertex and edge counts, so one cycle already leaves enough freedom to decouple the unweighted rank census from the size-weighted array. The failure calibrates the neighbouring statements rather than undermining them: the pair straddles the classes of Conjectures 62 and 64, one member bipartite and one chordal, so the bipartite and chordal rigidity claims stand on graphs the counterexample cannot reach, and the two-field claim of Conjecture 59 absorbs it, since the ternary specializations differ. The surviving positive content is the tree case, exhaustively unrefuted through fourteen vertices, which is exactly the first decisive theorem the original statement named.

**Conjecture 64** *(Chordal binary rigidity)*. For chordal graphs $$G$$ and $$H$$, $$C_G(2,Y)=C_H(2,Y)$$ implies $$C_G=C_H$$.

*Significance.* Chordal graphs, those in which every cycle of length at least four has a chord, form the natural dense counterpart to the sparse classes of Conjectures 62 and 63, and the mechanism is the same class rigidity tested against a family with unbounded clique structure rather than bounded cycle structure. The nearest literature boundary is once more the specialization theorem [77] that interprets the hypothesis over $$\mathbb F_2$$. The verification is a six-thousand-graph random holdout of chordal graphs on nine to twelve vertices, spanning $$5598$$ distinct binary specializations, with no violation. A first decisive theorem would be the case of trees, which are chordal, followed by block graphs. The failure mode is a chordal pair separating the binary specialization from the polynomial. The resolution of Conjecture 63 sharpens rather than settles the question here, since the refuting pair there has exactly one chordal member, so chordal rigidity survives it and its status is genuinely open.

**Conjecture 65** *(Recovery of the domination number)*. For all graphs $$G$$ and $$H$$, $$C_G=C_H$$ implies $$\gamma(G)=\gamma(H)$$.

*Significance.* A set is dominating exactly when its closed neighbourhood is the whole vertex set, and the array behind $$C_G$$ records $$\vert N_G[S]\vert $$ only through the difference $$\rho_G(S)=\vert N_G[S]\vert -c(G[S])$$, so the dominating sets are entangled with component counts and the mechanism is that the entanglement can be undone at the extreme where $$\gamma$$ lives. The conjecture sits strictly between a theorem and a false analogue, which is the nearest literature boundary: the cardinalities of connected dominating sets are readable from the coefficients, by Rossmann [77], while the total domination number is not determined by $$C_G$$. Every known collision class of $$C$$, the corpus recorded at Conjecture 58, has agreeing domination number. A first decisive theorem would be the tree case, where the unique fourteen-vertex collision class is the only known test. The failure mode is a collision class with distinct domination numbers, which would place $$\gamma$$ on the undetermined side of the boundary alongside total domination and would show that the connected-domination theorem is the exact limit of what the polynomial sees.

**Conjecture 66** *(Recovery of the independent domination number)*. For all graphs $$G$$ and $$H$$, $$C_G=C_H$$ implies $$i(G)=i(H)$$, where $$i$$ is the independent domination number, the least cardinality of a set that is simultaneously independent and dominating.

*Significance.* Independent dominating sets impose the two conditions the array treats most asymmetrically, domination through $$\vert N_G[S]\vert $$ and independence through $$c(G[S])=\vert S\vert $$, and the mechanism is that their interaction leaves a trace in the joint distribution of $$(\vert S\vert ,\rho_G(S))$$ even though neither condition is separately readable. The nearest literature boundary is the same theorem-versus-false-analogue frame as Conjecture 65: connected domination is readable [77], total domination is not determined, and $$i$$ is conjectured to fall on the determined side. Every known collision class of $$C$$, the corpus recorded at Conjecture 58, has agreeing independent domination number. A first decisive theorem would be recovery of $$i$$ for trees. The failure mode is a collision class with distinct $$i$$, which would split the domination invariants into determined and undetermined families along a line that no present structural explanation predicts.

### Log-concavity and support

**Conjecture 67** *(Global double log-concavity)*. For every graph $$G$$ the coefficient sequence $$a$$ of $$f_G(1+Z)$$ is log-concave, and so is its transform $$L(a)$$ defined by $$L(a)_i=a_i^2-a_{i-1}a_{i+1}$$, out-of-range terms being zero.

*Significance.* The expansion point is canonical: at $$X=1+Z$$ the polynomial is expanded about the degenerate point $$X=1$$, where the weights $$(X-1)^{\vert S\vert }$$ vanish for every nonempty set, and $$f_G$$ folds the rank variable into the size variable at the same point, so the sequence $$a$$ is the most compressed image of the whole array. The statement is calibrated to the strongest form the data support: log-concavity is asserted, its once-iterated form is asserted, and the calibration is exact because the third iterate of $$L$$ fails for a thirteen-vertex graph. The nearest literature boundary is Rossmann's paper [77], whose theorems about this polynomial are enumerative, the specialization, multiplicativity, and dominating-set results, so the positivity layer opens a new face of the object. The verification covers the full atlas of graphs on at most seven vertices and twenty-five hundred random graphs on eight to ten vertices. A first decisive theorem would be log-concavity of $$f_T(1+Z)$$ for trees. The failure mode is graded: a failure of the second level would compress the true boundary into the narrow band between one and three iterates, while a failure of bare log-concavity on some large graph would show that the seven-vertex atlas sits below the threshold where the array's geometry turns.

**Conjecture 68** *(Strict log-concavity for connected graphs)*. For connected $$G$$ with at least one edge, $$a_i^2>a_{i-1}a_{i+1}$$ at every interior position of the support of $$a$$, where $$a$$ is the coefficient sequence of $$f_G(1+Z)$$.

*Significance.* The mechanism is that equality cases of log-concavity should be confined to the degenerate stratum, and in this part the degenerate stratum is disconnectedness, exactly as in Conjecture 57: multiplicativity [77] builds the polynomials of disconnected graphs as products, and products are where interior coincidences are manufactured. The nearest literature boundary is that same multiplicativity theorem, which marks the hypothesis as necessary in spirit. The verification is the corpus of Conjecture 67, the full seven-vertex atlas and twenty-five hundred random graphs on eight to ten vertices, with strictness observed throughout the connected stratum. A first decisive theorem would be strictness for paths and stars, the two ends of the tree order of Conjecture 72. The failure mode is a connected graph with an interior equality, an exact coincidence $$a_i^2=a_{i-1}a_{i+1}$$, which would demand an algebraic explanation and would show that connectivity does not exhaust the sources of degeneracy.

**Conjecture 69** *(Strict second-order log-concavity)*. For connected $$G$$ with at least one edge, the transform $$L(a)$$ of Conjecture 67 is strictly log-concave at every interior position of its support.

*Significance.* The statement pushes the strictness mechanism of Conjecture 68 one level up the $$L$$-hierarchy, and its position is the sharpest the evidence permits, since the third iterate of $$L$$ fails already for a thirteen-vertex graph and the second-order slice strengthening fails for an eight-vertex graph (Conjecture 70), so the conjecture threads a boundary with counterexamples visible on two sides. The nearest literature boundary is as in Conjecture 67: the polynomial's literature [77] is enumerative and the positivity hierarchy is uncharted. The verification is the same corpus, the full seven-vertex atlas and twenty-five hundred random graphs on eight to ten vertices. A first decisive theorem would be second-order strictness for paths. The failure mode is a connected graph whose $$L(a)$$ has an interior equality or reversal, which by the two flanking counterexamples would pin the exact rung of the hierarchy at which graphs stop being log-concave.

**Conjecture 70** *(Rank-slice strict log-concavity)*. For connected $$G$$ and every attainable rank $$r$$, the slice $$A_{G,r}(Z)=[Y^r]\,F_G(1+Z,Y)$$, when it is not a monomial, has strictly log-concave coefficients at every interior position of its support.

*Significance.* The mechanism refines Conjecture 68 from the folded sequence to each rank slice separately: the sets of a fixed rank $$r$$ are counted by size, and strict log-concavity asserts that each of these level sets is unimodal in the strong multiplicative sense, so that positivity holds fibrewise and not only in aggregate. The calibration is exact here too, since the second-order strengthening of this slice statement fails for an eight-vertex graph, a counterexample reconfirmed by the independent implementation, so the slice hierarchy stops one level below the global hierarchy of Conjecture 69. The nearest literature boundary is Rossmann's [77] reading of the slices as class data over finite fields. The verification is the full seven-vertex atlas and twenty-five hundred random graphs on eight to ten vertices. A first decisive theorem would be strict log-concavity of every slice for stars. The failure mode is a connected graph with a non-log-concave slice, which would show that aggregate log-concavity, if it survives in Conjecture 67, is an artefact of summation rather than a fibrewise phenomenon.

**Conjecture 71** *(Interval support at fixed rank, resolved false)*. For every graph $$G$$ and every attainable rank $$r$$, the set $$K_r(G)=\{\vert S\vert :\rho_G(S)=r\}$$ is an interval of integers.

*Remark (resolution).* The conjecture is false as stated. The connected graph on vertex set $$\{0,\ldots,7\}$$ with edge set $$\{\{0,3\},\{0,6\},\{0,7\},\{1,4\},\{1,6\},\{1,7\},\{2,5\},\{2,6\},\{3,6\},\{3,7\},\{4,6\},\{4,7\},\{5,7\}\}$$ attains adjoint rank five at support sizes one and three but at no size two: the degree-five vertices $$6$$ and $$7$$ give rank five at size one, the independent set $$\{0,1,2\}$$ has closed neighbourhood all eight vertices and so gives $$8-3=5$$ at size three, while every two-vertex set has rank in $$\{3,4,6\}$$. Hence $$K_5(G)=\{1,3,4,5,6\}$$ has an interior gap at size two. An exhaustive scan of all $$12{,}346$$ graphs on eight vertices finds exactly two violations, both connected, and none on seven or fewer vertices.

*Significance.* The statement is retained with its resolution because the failure is informative and sharply located. A connected eight-vertex graph attains rank five at the support sizes $$\{1,3,4,5,6\}$$, skipping size two, so the size direction of the array is not gapless in general, and since the transposed statement was already false, neither direction carries interval structure. The failure does not reach the slice positivity beneath which the support claim was placed: on the two refuting graphs every rank slice $$[Y^r]F_G(1+Z,Y)$$ of Conjecture 70 stays strictly log-concave, since each slice weights the raw size counts by a full binomial row that closes the gap, so gapless raw support is not after all necessary for the slice statement. The nearest literature boundary is unchanged, Rossmann's [77] reading of one extreme stratum of the array. The surviving positive content is the interval property for all graphs through seven vertices and, conjecturally, for trees, which the eight-vertex counterexample leaves open.

### Tree extremality and rigidity

**Conjecture 72** *(Coefficientwise tree extremality)*. For every tree $$T$$ on $$n$$ vertices, $$f_{P_n}(1+Z)\le f_T(1+Z)\le f_{K_{1,n-1}}(1+Z)$$ coefficientwise, with equality only for the path and the star respectively.

*Significance.* The mechanism is visible in the lemma above: the rank landscape of a tree is driven by its internal vertices and its diameter, and the path and the star are the two trees that extremize both statistics simultaneously, the path with two leaves and maximal diameter, the star with maximal leaf count and diameter two. The conjecture asserts that this extremality is not merely a matter of the range of $$\rho_T$$ but holds coefficient by coefficient in the shifted polynomial, the strongest ordering the object admits. The nearest literature boundary is Rossmann's enumeration [77], which interprets each coefficientwise inequality as a family of inequalities between class censuses over every finite field at once. The verification is exhaustive over all trees through fourteen vertices. A first decisive theorem would be either inequality for one nontrivial family, say the star bound for caterpillars. The failure mode is a tree escaping the sandwich at a single coefficient, which would show that the coefficientwise order on trees is not anchored at the degree extremes and would force the extremal programme to work slice by slice instead.

**Conjecture 73** *(Star rank-majorization)*. For every $$n\ge5$$ and every prime power $$q$$, the decreasingly ordered adjoint-rank distribution of $$L_{K_{1,n-1}}(\mathbb F_q)$$ majorizes that of $$L_T(\mathbb F_q)$$ for every $$n$$-vertex tree $$T$$.

*Remark.* The hypothesis $$n\ge5$$ cannot be dropped: at $$n=4$$ and $$q=2$$ the star fails to majorize the path. The dual assertion, that the path is majorization-minimal among $$n$$-vertex trees, is false. The failure at $$(n,q)=(4,2)$$ was found in the verification reported below.

*Significance.* Majorization compares two probability vectors through all partial sums of their decreasingly ordered entries, so the conjecture asserts that the star's adjoint-rank distribution is the most concentrated among trees uniformly across the whole partial-sum hierarchy and across every finite field at once. The mechanism is concentration: by the rank formula the rank of a random element is a statistic of its vertex support, and the star compresses the possible values harder than any other tree. The remark shows the inequality system is genuinely tight, which is the honest register for a majorization claim: at $$(n,q)=(4,2)$$ one partial sum reverses, and the dual minimality of the path fails outright, so the surviving statement is exactly the one the data leave standing. The nearest literature boundary is Rossmann's [77] reading of these distributions as class data of graphical groups. The verification is exhaustive for $$q\in\{2,3,4,5\}$$ over all trees through twelve vertices, for $$q\in\{2,3\}$$ at thirteen, and for $$q=2$$ at fourteen. The reduction proved above collapses the whole majorization, across every partial sum and every field, to the single anti-concentration bound $$\max_r\pi_{T,q}(r)\le1-1/q$$, whose extremal value is the star's own top atom, so the failure at $$(n,q)=(4,2)$$ is exactly a violation of that bound. A first decisive theorem would be the reduced bound for all $$n\ge5$$ trees, of which the comparison of star against path is the tightest case. The failure mode is a tree and a prime power breaking one partial sum at some $$n\ge5$$, which would show that the small-$$n$$ anomaly is the visible end of a persistent phenomenon rather than a boundary effect.

*Proposition (reduction of the star majorization).* Let $$T$$ be a tree on $$n\ge3$$ vertices and $$q$$ a prime power, and write $$\pi_{T,q}(r)=q^{-n}\sum_{\rho_T(S)=r}(q-1)^{\vert S\vert }$$ for the adjoint-rank distribution of a uniformly random element of $$L_T(\mathbb F_q)$$. The decreasingly ordered distribution of the star $$K_{1,n-1}$$ majorizes that of $$T$$ if and only if $$\max_r\pi_{T,q}(r)\le 1-1/q$$.

*Proof.* By the rank formula the star attains ranks $$0$$, $$1$$, and $$n-1$$, from the empty support, the nonempty sets of leaves, and the supports meeting the centre, with masses $$1-1/q$$, $$1/q-1/q^n$$, and $$1/q^n$$ in decreasing order for every $$q\ge2$$. For any tree $$\rho_T(S)=0$$ holds only at $$S=\emptyset$$, so $$\pi_{T,q}(0)=1/q^n$$, and this is the least atom, every nonempty rank carrying mass a sum of terms $$q^{-n}(q-1)^{\vert S\vert }\ge q^{-n}$$. A tree on $$n\ge3$$ vertices has $$\operatorname{diam}\ge2$$, so the lemma gives at least three attained ranks. Majorization of the three-atom star vector over the padded tree vector is the family of partial-sum inequalities on decreasingly ordered atoms, both sides totalling $$1$$. The first reads $$1-1/q\ge\max_r\pi_{T,q}(r)$$, the displayed bound. The second bounds the two largest tree atoms by $$1-1/q^n$$, and holds automatically, since removing them leaves at least one atom of mass at least $$1/q^n$$. Every later star partial sum equals $$1$$. Hence the whole family holds if and only if its first member does. ∎

**Conjecture 74** *(Tree rank-variance extremality)*. For every $$n\ge4$$ and every prime power $$q$$, among $$n$$-vertex trees the variance of $$\operatorname{rank}(\operatorname{ad}_x)$$ over uniformly random $$x\in L_T(\mathbb F_q)$$ is uniquely minimized by the path and uniquely maximized by the star.

*Significance.* The two tree orderings of this programme are not redundant: majorization compares the ordered probabilities while the variance measures the spread of the rank values themselves, and the star sits at the top of both scales, most concentrated in the sense of Conjecture 73 and most spread in the sense of variance, with the path now appearing as the genuine minimum. The mechanism is again the rank formula, which makes the variance a purely combinatorial functional of the array $$(\vert S\vert ,\rho_T(S))$$ weighted by $$(q-1)^{\vert S\vert }$$. The nearest literature boundary is the enumerative frame of Rossmann [77], in which the variance is a second moment of the class census. The verification matches Conjecture 73: exhaustive for $$q\in\{2,3,4,5\}$$ through twelve vertices, for $$q\in\{2,3\}$$ at thirteen, and for $$q=2$$ at fourteen. A first decisive theorem would be the uniqueness of the star maximum at $$q=2$$. The failure mode is a tree overtaking an extreme at some $$(n,q)$$, and since the statement begins at $$n=4$$ where the majorization statement already fails, a violation would separate the variance order from the majorization order and show that the two concentration scales genuinely diverge on trees.

**Conjecture 75** *(Leaf-count rigidity)*. For a tree $$T$$ on $$n\ge2$$ vertices, equality holds in the bound $$s(T)\ge n-\ell(T)+2$$ of the lemma exactly when $$T$$ is a path or a star.

*Significance.* The lemma's proof realizes $$n-\ell(T)+2$$ rank values along a breadth-first chain of internal vertices, and equality demands that every subset of vertices lands on one of the chain's values, so the mechanism is rigidity of the equality case: only the two extreme trees should leave no room for excess values off the chain. The nearest literature boundary is internal, the lemma itself, whose bound the conjecture upgrades to a characterization, in the same relation as an isoperimetric equality case stands to its inequality. The verification is exhaustive over all trees through fourteen vertices. The forward half, that the path and the star do achieve equality, is proved in the proposition above, leaving uniqueness, that no third tree is equally tight, as the open content. The failure mode is a third tree achieving equality, which would show that the leaf count fails to see some genuinely different extremal shape and would refute the rigidity reading of the lemma while leaving the lemma intact.

**Conjecture 76** *(Diameter rigidity)*. For a tree $$T$$ on $$n\ge2$$ vertices, equality holds in the bound $$s(T)\ge\operatorname{diam}(T)+1$$ of the lemma exactly when $$T$$ is a path or a star.

*Significance.* The diametral chain of the lemma realizes $$\operatorname{diam}(T)+1$$ values, and equality requires the whole subset lattice to produce nothing beyond the chain, so the mechanism parallels Conjecture 75 with the diameter replacing the internal vertex count, and the two rigidity statements pin the same extremal pair from two independent directions, each serving as a cross-check on the other. The nearest literature boundary is again the lemma itself. The verification is exhaustive over all trees through fourteen vertices. The forward half, that the path and the star do achieve equality, is proved in the same proposition, so only uniqueness remains open. The failure mode is a tree of small diameter and few rank values outside the pair, which would show the diameter bound to be loose in a structured way and would decouple the two rigidity statements that the exhaustive search through fourteen vertices keeps locked together.

## Part V: pattern Lie algebras of finite posets

*Added to the deposit: 6 August 2026.*

The twenty conjectures below concern the pattern Lie algebras of finite posets, studied through two rank-weight enumerators that record how the bracket contracts against an element and against a functional. They form four programmes. A determination programme (Conjectures 77 to 82) asserts that the adjoint enumerator alone determines the coadjoint enumerator and a list of classical invariants. A characteristic-and-field programme (Conjectures 83 to 87) identifies what in these distributions is independent of the ground field and how the field affects them when it does. A centre-one programme (Conjectures 88 to 90) studies the incidence quotient that measures the difference between the two enumerators when the centre is a line. A Hasse-forest and unitriangular programme (Conjectures 91 to 96) relates coadjoint structure to the shape of the cover graph and treats the unitriangular chain as a separate extremal case. The proved results are kept separate from the conjectural ones: the incidence identity is a theorem with a full proof, the standard adjoint–coadjoint duality of this family, included for calibration and not claimed as new, and every conjecture is stated relative to it. Fifteen of the twenty are supported throughout the tested corpus. Three more, Conjectures 79, 81, and 85, are stated in greater generality than the computations reach, and each carries a remark giving the restricted case its evidence covers. Two, Conjectures 87 and 90, have since been refuted by explicit seven-point posets and are recorded as resolved false with their counterexamples.

For a finite poset $$P$$ on a set of points and a prime power $$q$$, the pattern Lie algebra over $$\mathbb F_q$$ is

$$
L_P(\mathbb F_q)=\operatorname{span}\{e_{ij}:i<_Pj\}
$$

inside the strictly upper triangular matrices under a fixed linear extension of $$P$$, with the matrix-unit bracket

$$
[e_{ij},e_{kl}]=\delta_{jk}\,e_{il}-\delta_{li}\,e_{kj}.
$$

It is nilpotent, and $$\dim L_P$$ is the number of strict order relations of $$P$$. Write $$\operatorname{ad}_x(y)=[x,y]$$ for the adjoint map of $$x$$, and for a functional $$f\in L_P(\mathbb F_q)^*$$ let $$B_f(u,v)=f([u,v])$$ be the alternating Kirillov form. The two natural contractions of the bracket tensor give two rank-weight enumerators over a single finite field,

$$
A_{P,q}(T)=\sum_{x\in L_P(\mathbb F_q)}T^{\operatorname{rank}(\operatorname{ad}_x)},\qquad
K_{P,q}(T)=\sum_{f\in L_P(\mathbb F_q)^*}T^{\operatorname{rank}(B_f)},
$$

the adjoint enumerator and the Kirillov enumerator, each a distribution over one finite field. Write $$b_A(P,q)=\max_x\operatorname{rank}(\operatorname{ad}_x)$$ for the adjoint breadth and $$b_K(P,q)=\max_f\operatorname{rank}(B_f)$$ for the maximal Kirillov rank, the largest coadjoint-orbit rank. Write $$Z(L_P)$$, $$\operatorname{Cent}(L_P)$$, and $$\operatorname{Der}(L_P)$$ for the centre, the centroid (the linear maps commuting with every $$\operatorname{ad}_x$$), and the derivation algebra, and $$\gamma_i(L_P)$$ for the lower central series. Say $$P$$ is a Hasse forest if the undirected Hasse cover graph of $$P$$ is a forest. The chain on $$n$$ points gives $$L=\mathrm{ut}_n(\mathbb F_q)$$, the strictly upper triangular Lie algebra.

*Proposition (incidence identity and calibration).* Let $$L=L_P(\mathbb F_q)$$ and let $$I_L=\{(x,f)\in L\times L^*:f([x,L])=0\}$$ be the incidence variety. Then $$\vert I_L\vert =q^{\dim L}A_{L,q}(q^{-1})=q^{\dim L}K_{L,q}(q^{-1})$$. Consequently $$A_{L,q}(1)=K_{L,q}(1)=q^{\dim L}$$ and $$A_{L,q}(q^{-1})=K_{L,q}(q^{-1})$$, so $$(1-T)(1-qT)$$ divides $$A_{L,q}(T)-K_{L,q}(T)$$ in $$\mathbb Z[T]$$.

*Proof.* Count $$I_L$$ two ways. For fixed $$x$$ the condition $$f([x,L])=0$$ says $$f$$ vanishes on the image $$[x,L]=\operatorname{im}(\operatorname{ad}_x)$$, a subspace of dimension $$\operatorname{rank}(\operatorname{ad}_x)$$, so the number of admissible $$f$$ is $$q^{\dim L-\operatorname{rank}(\operatorname{ad}_x)}$$, and summing over $$x$$ gives $$\vert I_L\vert =q^{\dim L}\sum_x q^{-\operatorname{rank}(\operatorname{ad}_x)}=q^{\dim L}A_{L,q}(q^{-1})$$. For fixed $$f$$ the condition says $$x$$ lies in the radical of the alternating form $$B_f$$, of dimension $$\dim L-\operatorname{rank}(B_f)$$, giving $$q^{\dim L-\operatorname{rank}(B_f)}$$ admissible $$x$$, so $$\vert I_L\vert =q^{\dim L}K_{L,q}(q^{-1})$$. Equating the two counts gives $$A_{L,q}(q^{-1})=K_{L,q}(q^{-1})$$. Taking every element and every functional, the rank-zero terms included, gives $$A_{L,q}(1)=K_{L,q}(1)=q^{\dim L}$$. The two evaluations exhibit $$T=1$$ and $$T=1/q$$ as common roots of $$A_{L,q}-K_{L,q}$$, and since $$q>1$$ these are distinct, so $$(1-T)(1-qT)$$ divides $$A_{L,q}-K_{L,q}$$. ∎

The identity is the standard adjoint–coadjoint duality of this family, a Knuth-type contraction of one bracket tensor, and is recorded here as calibration rather than as a new result. For the centre-one conjectures define

$$
R_{P,q}(T)=\frac{K_{P,q}(T)-A_{P,q}(T)}{(1-T)(1-qT)},
$$

a polynomial in $$\mathbb Z[T]$$ by the proposition.

### Determination by the adjoint enumerator

**Conjecture 77** *(Adjoint–Kirillov determination)*. For all finite posets $$P$$ and $$Q$$ and every prime power $$q$$, if $$A_{P,q}(T)=A_{Q,q}(T)$$ then $$K_{P,q}(T)=K_{Q,q}(T)$$.

*Significance.* The adjoint and Kirillov enumerators are the two contractions of the same bracket, one in the element variable and one in the functional variable, and the proposition forces them to agree at $$T=1$$ and $$T=1/q$$. The conjecture asserts that the adjoint enumerator determines the Kirillov enumerator at every value of $$T$$, not only at those two points. The nearest related result is Delsarte's [85] analysis of the rank distributions of alternating bilinear forms over a finite field, which describes the Kirillov side alone but does not connect it to the adjoint side. A tractable special case is the chain $$L=\mathrm{ut}_n(\mathbb F_q)$$, where the divisibility of the proposition already relates the two enumerators. In tests on the corpus described in the stress-test section, the adjoint enumerator determined the Kirillov enumerator across $$64$$ adjoint-collision classes with no exception. A counterexample would be an adjoint-collision pair with distinct Kirillov enumerators, which would show that $$K$$ is not determined by $$A$$ beyond the two points where the proposition equates them.

**Conjecture 78** *(Lower-central recovery)*. For every finite poset $$P$$ and every prime power $$q$$, the enumerator $$A_{P,q}(T)$$ determines the vector of lower-central factor dimensions $$(\dim\gamma_i(L_P)/\gamma_{i+1}(L_P))_i$$.

*Significance.* The rank of $$\operatorname{ad}_x$$ is the dimension of the image $$[x,L_P]$$, and the lower central series is built from these images as $$x$$ ranges over the algebra. The conjecture asserts that the distribution of adjoint ranks determines the graded dimensions $$\dim\gamma_i/\gamma_{i+1}$$. The nearest related result is the breadth theory of Cameron–Coll–Mayers–Russoniello [80], in which the maximal adjoint rank $$b_A$$ is one value of the distribution that the full enumerator records. A tractable special case is the chain, where $$\mathrm{ut}_n$$ has a known lower central series matched to its adjoint spectrum. In tests on the corpus described in the stress-test section, the lower-central factor vector was constant on every adjoint-collision class. A counterexample would be an adjoint-collision class with two distinct factor vectors, which would show that the lower-central factors are not determined by $$A$$.

**Conjecture 79** *(Ordinary Poincaré recovery)*. For every finite poset $$P$$ and every prime power $$q$$, the enumerator $$A_{P,q}(T)$$ determines the ordinary cohomological Poincaré polynomial $$\sum_i\dim H^i(L_P,\mathbb F_q)U^i$$.

*Remark.* The evidence tests only the equality of $$\dim H^2(L_P,\mathbb F_q)$$ and $$\dim H^3(L_P,\mathbb F_q)$$ across adjoint-collision classes, and it rests on the deposited cohomology computation rather than on an independent recomputation of Lie-algebra cohomology. The universal statement over all degrees is more tentative than the other conjectures of this part, the remaining cases being untested.

*Significance.* The Chevalley–Eilenberg differential of $$L_P$$ is built from the same structure constants that the adjoint maps record, so the adjoint-rank distribution constrains the cohomological Betti numbers through the ranks of those differentials. The nearest related result is the poset Lie cohomology of Lampret–Vavpetič [82], the closest computation of $$H^i(L_P,\mathbb F_q)$$ for this family. No decisive special case is proposed, and the tested range is the two degrees recorded in the remark. A counterexample would be an adjoint-collision class with distinct ordinary Betti numbers in some degree, which would show that cohomology is not determined by the adjoint enumerator.

**Conjecture 80** *(Derivation recovery)*. For every finite poset $$P$$ and every prime power $$q$$, the enumerator $$A_{P,q}(T)$$ determines $$\dim\operatorname{Der}(L_P)$$.

*Significance.* A derivation is constrained at each point by its interaction with the adjoint action, so the derivation algebra is determined by the adjoint representation, of which the adjoint-rank distribution is a coarse record. The conjecture asserts that this distribution determines the dimension of the space of derivations. The nearest related result is again the breadth theory of Cameron–Coll–Mayers–Russoniello [80], which reads structural invariants of $$L_P$$ off the same adjoint data. A tractable special case is the chain, where $$\dim\operatorname{Der}(\mathrm{ut}_n)$$ is classical. In tests on the corpus described in the stress-test section, $$\dim\operatorname{Der}(L_P)$$ was constant on every adjoint-collision class. A counterexample would be an adjoint-collision class with distinct derivation dimensions, which would show that $$\dim\operatorname{Der}(L_P)$$ is not determined by the adjoint distribution.

**Conjecture 81** *(Adjoint Poincaré recovery)*. For every finite poset $$P$$ and every prime power $$q$$, the enumerator $$A_{P,q}(T)$$ determines the adjoint-cohomology dimensions $$\dim H^i(L_P,L_P)$$ for every $$i$$.

*Remark.* The evidence tests only the equality of $$\dim H^1(L_P,L_P)$$, $$\dim H^2(L_P,L_P)$$, and $$\dim H^3(L_P,L_P)$$ across adjoint-collision classes, and it rests on the deposited cohomology computation rather than on an independent recomputation. The universal statement over all degrees is more tentative than the other conjectures of this part, the remaining cases being untested.

*Significance.* Cohomology with coefficients in the adjoint module governs the deformation theory of $$L_P$$, and its differentials are built from the same brackets whose ranks the adjoint maps record, so the situation parallels Conjecture 79 with the algebra acting on itself. The nearest related result is the poset Lie cohomology of Lampret–Vavpetič [82]. No decisive special case is proposed, and the tested range is the three degrees recorded in the remark. A counterexample would be an adjoint-collision class with distinct adjoint Betti numbers in some degree, which would show that the deformation theory is not determined by the adjoint enumerator.

**Conjecture 82** *(Centroid-dimension recovery)*. For every finite poset $$P$$ and every prime power $$q$$, the enumerator $$A_{P,q}(T)$$ determines $$\dim\operatorname{Cent}(L_P)$$.

*Significance.* The centroid is by definition the space of linear maps commuting with every $$\operatorname{ad}_x$$, so it is an invariant of the adjoint representation, of which the adjoint-rank distribution is a coarse record. The conjecture asserts that this distribution determines its dimension. The nearest related result is again the breadth theory of Cameron–Coll–Mayers–Russoniello [80], whose invariants are defined on the same adjoint data. A tractable special case is the chain, where $$\dim\operatorname{Cent}(\mathrm{ut}_n)=n$$ for $$n\ge3$$. In tests on the corpus described in the stress-test section, $$\dim\operatorname{Cent}(L_P)$$ was constant on every adjoint-collision class. A counterexample would be an adjoint-collision class with distinct centroid dimensions, which would show that the centroid dimension is not determined by the adjoint-rank distribution.

### Characteristic and field behaviour

**Conjecture 83** *(Adjoint spectrum characteristic independence)*. For every finite poset $$P$$, the set $$\{\operatorname{rank}(\operatorname{ad}_x):x\in L_P(\mathbb F_q)\}$$ of attained adjoint ranks is independent of $$q$$.

*Significance.* The attained adjoint ranks are governed by which support patterns of $$x$$ can produce a given image dimension, a combinatorial condition on $$P$$. The conjecture asserts that the set of attained values depends only on the poset, while the multiplicities depend on the field. The nearest related result is Halasi–Pálfy [83], whose theorem that pattern-group class counts are not polynomial in $$q$$ shows that the counts depend on the field. The invariance of the support is a stronger statement about a smaller object. A tractable special case is the chain, where the attained ranks of $$\mathrm{ut}_n$$ form an interval determined by $$n$$. In tests on the corpus described in the stress-test section, the attained-rank sets agreed across $$\mathbb F_2$$, $$\mathbb F_3$$, and $$\mathbb F_5$$ in every case. A counterexample would be a poset with an adjoint rank attained over one field but not another, which would show that the support depends on the characteristic.

**Conjecture 84** *(Kirillov spectrum characteristic independence)*. For every finite poset $$P$$, the set $$\{\operatorname{rank}(B_f):f\in L_P(\mathbb F_q)^*\}$$ of attained Kirillov ranks is independent of $$q$$.

*Significance.* The attained Kirillov ranks are the even numbers realized as ranks of the alternating forms $$B_f$$, and which of these occur is a combinatorial condition on the coadjoint action of $$P$$. The conjecture is the coadjoint analogue of Conjecture 83. The nearest related results are Delsarte [85] for the rank distributions of alternating forms and Halasi–Pálfy [83] for the field dependence of the associated class counts, against which the invariance of the support is the finer statement. A tractable special case is the chain. In tests on the corpus described in the stress-test section, the attained Kirillov-rank sets agreed across $$\mathbb F_2$$, $$\mathbb F_3$$, and $$\mathbb F_5$$ in every case. A counterexample would be a poset with a Kirillov rank attained over one field but not another, which would show field dependence in the coadjoint support.

**Conjecture 85** *(Two-field arithmetic rigidity)*. For all finite posets $$P$$ and $$Q$$, if $$A_{P,2}=A_{Q,2}$$ and $$A_{P,3}=A_{Q,3}$$ then $$A_{P,q}=A_{Q,q}$$ for every prime power $$q$$.

*Remark.* Among the posets computed over all three fields, the only field beyond $$q=2$$ and $$q=3$$ at which equality was actually tested is the single holdout $$q=5$$. The universal statement over every prime power is more tentative than the other conjectures of this part, the remaining cases being untested.

*Significance.* The two adjoint enumerators over the smallest fields are two weighted counts drawn from the poset's rank array. The conjecture asserts that the arrays realized by posets are rigid enough that no third field carries information absent from the first two. The nearest related result is Halasi–Pálfy [83], whose non-polynomiality theorem shows that larger fields can behave differently in general, against which the two-field claim asserts that this family is nonetheless determined. No decisive special case is proposed, and the tested range is the single holdout recorded in the remark. Equality of $$A$$ at $$q=2$$ and $$q=3$$ forced equality at $$q=5$$ across $$16$$ three-field collision classes. A counterexample would be a pair agreeing over $$\mathbb F_2$$ and $$\mathbb F_3$$ but differing over some larger field.

**Conjecture 86** *(Adjoint stochastic field monotonicity)*. For every finite poset $$P$$ and prime powers $$q<q'$$, the distribution of $$\operatorname{rank}(\operatorname{ad}_x)$$ for uniformly random $$x\in L_P(\mathbb F_{q'})$$ first-order stochastically dominates its distribution over $$\mathbb F_q$$.

*Significance.* First-order stochastic dominance compares two distributions across all of their tail probabilities at once, so the conjecture asserts that raising the field can only move the adjoint rank upward in this sense. The reason is that a larger field provides more elements of high rank at each support pattern. The nearest related result is the breadth theory of Cameron–Coll–Mayers–Russoniello [80], in which the top rank $$b_A$$ is stable while the rest of the distribution shifts. The statement is calibrated to the strongest form that holds. The monotone-likelihood-ratio strengthening is false, failing three times already from $$q=2$$ to $$q=3$$, so first-order dominance is the appropriate form. In tests on the corpus described in the stress-test section, first-order dominance held in all $$221$$ field-pair tests, while the likelihood-ratio strengthening failed as recorded. A counterexample would be a poset and a field pair reversing one tail probability, which would show that first-order dominance is too strong.

**Conjecture 87** *(Kirillov likelihood-ratio field monotonicity, resolved false)*. For every finite poset $$P$$ and prime powers $$q<q'$$, the normalized even-rank distribution defined by $$K_{P,q'}$$ dominates that defined by $$K_{P,q}$$ in monotone likelihood-ratio order.

*Remark (resolution).* The conjecture is false as stated. The seven-point poset with cover relations $$1\prec2$$, $$2\prec3$$, $$2\prec4$$, $$1\prec5$$, $$5\prec7$$, $$1\prec6$$, $$6\prec7$$ gives a ten-dimensional pattern algebra whose Kirillov enumerator has even-rank coefficients $$128,384,128,384$$ at ranks $$0,2,4,6$$ over $$\mathbb F_2$$ and $$2187,17496,4374,34992$$ over $$\mathbb F_3$$. The likelihood ratio $$[T^{2j}]K_{P,3}/[T^{2j}]K_{P,2}$$ then takes the values $$17.1$$, $$45.6$$, $$34.2$$, $$91.1$$ across the four even ranks, decreasing from rank $$2$$ to rank $$4$$, so the monotone likelihood-ratio order already fails at the pair $$q=2$$, $$q'=3$$. The first-order dominance of Conjecture 86 is untouched, being the weaker order the data do support.

*Significance.* The statement is retained with its resolution because the failure locates the boundary precisely. Monotone likelihood-ratio order is strictly stronger than first-order dominance and compares the two distributions ratio by ratio across the even ranks, and the refuting poset shows that the coadjoint side does not satisfy this strengthening any more than the adjoint side does in Conjecture 86. The nearest related result is Delsarte [85], whose rank distributions of alternating forms are the model for the even-rank sequence. The surviving positive content is the first-order Kirillov dominance that the same data support, the coadjoint analogue of Conjecture 86, which the counterexample leaves standing.

### Centre-one incidence quotient

**Conjecture 88** *(Centre-one reverse determination)*. For every finite poset $$P$$ with $$\dim Z(L_P)=1$$ and every prime power $$q$$, the enumerator $$K_{P,q}(T)$$ determines $$A_{P,q}(T)$$.

*Significance.* Conjecture 77 states the implication from the adjoint side to the coadjoint side, and this is the reverse implication under the hypothesis that the centre is a line. The reason is that a one-dimensional centre makes the incidence quotient of the proposition rigid enough to invert. The nearest related result is Delsarte [85], whose alternating-form rank distributions are what $$K_{P,q}$$ records. A tractable special case is the chain $$\mathrm{ut}_n$$, whose centre is the single corner entry. In tests on the corpus described in the stress-test section, the Kirillov enumerator determined the adjoint enumerator on all $$43$$ centre-one records. A counterexample would be a centre-one pair with equal $$K$$ and distinct $$A$$, which would show that $$A$$ is not determined by $$K$$ even when the centre is a line.

**Conjecture 89** *(Centre-one Laplace positivity)*. For every finite poset $$P$$ with $$\dim Z(L_P)=1$$ and every prime power $$q$$, the polynomial $$R_{P,q}(T)$$ has nonnegative integer coefficients.

*Significance.* The quotient $$R_{P,q}$$ measures the difference between the coadjoint and adjoint enumerators after the two common roots of the proposition are divided out. The conjecture asserts that under a line centre this difference is a counting polynomial, so its coefficients are nonnegative integers. The nearest related result is Delsarte [85], against whose alternating-form model the positivity of $$R_{P,q}$$ constrains how far $$K$$ can exceed $$A$$. A tractable special case is the chain, where $$R$$ is computable in closed form. In tests on the corpus described in the stress-test section, $$R_{P,q}$$ had nonnegative integer coefficients on all $$43$$ centre-one records. A counterexample would be a centre-one poset with a negative coefficient in $$R_{P,q}$$, which would show that $$R_{P,q}$$ is not a counting polynomial and would remove the basis for the shape statement of Conjecture 90.

**Conjecture 90** *(Centre-one quotient shape, resolved false)*. For every finite poset $$P$$ with $$\dim Z(L_P)=1$$ and every prime power $$q$$, the coefficient sequence of $$R_{P,q}(T)$$ has interval support and is unimodal.

*Remark (resolution).* The conjecture is false as stated. The seven-point poset with cover relations $$1\prec2$$, $$2\prec3$$, $$2\prec4$$, $$3\prec6$$, $$4\prec5$$, $$5\prec6$$, $$6\prec7$$ has a one-dimensional centre and a nineteen-dimensional pattern algebra over $$\mathbb F_2$$, and its incidence quotient $$R_{P,2}$$ has nonnegative integer coefficients with interval support but is not unimodal: the coefficients at degrees $$8$$, $$9$$, and $$10$$ are $$206336$$, $$198656$$, $$225280$$, a strict interior valley between two higher values. The positivity of Conjecture 89 and the interval support both hold on this poset, so the unimodality alone fails.

*Significance.* The statement is retained with its resolution because the failure sharpens the neighbouring positivity result. Given the positivity of Conjecture 89, the natural next question was the shape of the coefficient sequence, and the refuting poset shows that positivity does not force a single peak, since the quotient can carry a strict interior valley while keeping nonnegative coefficients and gapless support. The nearest related results are Delsarte [85] for the alternating-form arithmetic and Coll–Mayers [81] for the coadjoint-orbit reading of $$K$$. The surviving positive content is exactly the positivity and interval support of Conjecture 89, which the counterexample leaves intact, so the regularity of $$R_{P,q}$$ under a line centre stops at nonnegativity and gapless support and does not extend to unimodality.

### Hasse-forest and unitriangular structure

**Conjecture 91** *(Hasse-forest reverse determination)*. For every finite poset $$P$$ whose Hasse cover graph is a forest and every prime power $$q$$, the enumerator $$K_{P,q}(T)$$ determines $$A_{P,q}(T)$$.

*Significance.* This is the reverse determination of Conjecture 77 under a structural hypothesis complementary to the centre-one hypothesis of Conjecture 88. The reason is that a forest cover graph builds the coadjoint form from independent covers, which makes the incidence quotient rigid enough to invert. The nearest related result is Coll–Mayers [81], whose index computations for Lie poset algebras are sharpest on tree-shaped posets. A tractable special case is the chain, a forest on one branch. In tests on the corpus described in the stress-test section, the Kirillov enumerator determined the adjoint enumerator across $$44$$ forest-collision classes. A counterexample would be a forest pair with equal $$K$$ and distinct $$A$$, which would show that the forest hypothesis is not the right setting for reverse determination.

**Conjecture 92** *(Hasse-forest coadjoint saturation)*. For every finite poset $$P$$ whose Hasse cover graph is a forest and every prime power $$q$$, with $$b_K=b_K(P,q)$$ the maximal Kirillov rank, $$\operatorname{supp}K_{P,q}=\{0,2,4,\ldots,b_K\}$$, so every even rank up to $$b_K$$ is attained.

*Significance.* An alternating form has even rank, and the conjecture asserts that on a forest every even rank up to the top is realized by some functional. The reason is that the independent covers of a forest allow the coadjoint rank to be adjusted one pair at a time. The nearest related results are Coll–Mayers [81], whose index is the codimension complementary to $$b_K$$, and Delsarte [85], whose alternating-form model predicts which even ranks can occur. A tractable special case is the chain, where $$K_{\mathrm{ut}_n}$$ fills its even range. In tests on the corpus described in the stress-test section, the forest Kirillov support filled every even rank up to $$b_K$$ in each case. A counterexample would be a forest with a gap in its Kirillov support, which would remove the support hypothesis used in Conjecture 93.

**Conjecture 93** *(Hasse-forest Kirillov unimodality)*. For every finite poset $$P$$ whose Hasse cover graph is a forest and every prime power $$q$$, the even-rank sequence $$([T^{2j}]K_{P,q}(T))_j$$ is unimodal.

*Significance.* On the gapless support of Conjecture 92 the next question is the shape of the even-rank counts. The conjecture asserts that the coadjoint rank distribution of a forest rises to a single peak and falls, with no interior dip. The nearest related results are Delsarte [85] for the alternating-form counts and Coll–Mayers [81] for the coadjoint reading. The statement is calibrated to the strongest form that holds. Strict log-concavity is false, so unimodality is the appropriate form. In tests on the corpus described in the stress-test section, the forest even-rank sequence was unimodal throughout. A counterexample would be a forest whose even-rank sequence has two peaks, which would confine the shape statement to the unitriangular chain of Conjecture 95.

**Conjecture 94** *(Hasse-forest breadth–orbit bound)*. For every finite poset $$P$$ whose Hasse cover graph is a forest and every prime power $$q$$, $$b_K(P,q)\le 2\,b_A(P,q)$$.

*Significance.* The bound relates the maximal coadjoint-orbit rank to the adjoint breadth. The reason is that on a forest the largest alternating form cannot exceed twice the largest adjoint image, since both come from the same covers. The nearest related results are Cameron–Coll–Mayers–Russoniello [80] for the breadth $$b_A$$ and Coll–Mayers [81] for the index that controls $$b_K$$. The forest hypothesis is essential. The unrestricted inequality is false, with many counterexamples off the forest class. In tests on the corpus described in the stress-test section, the forest bound held everywhere, and the unrestricted bound failed fourteen times off the forest class. A counterexample would be a forest violating $$b_K\le 2b_A$$, which would show that a tree-shaped poset can carry a coadjoint orbit large relative to its adjoint breadth.

**Conjecture 95** *(Unitriangular Kirillov strict log-concavity)*. For $$L=\mathrm{ut}_n(\mathbb F_q)$$ and every prime power $$q$$, the even-rank sequence $$([T^{2j}]K_{L,q}(T))_j$$ is strictly log-concave at every nontrivial interior index.

*Significance.* The chain is the extremal forest, and here the unimodality of Conjecture 93 strengthens to strict log-concavity. The conjecture asserts that the coadjoint rank distribution of $$\mathrm{ut}_n$$ is as concentrated as the family allows. The nearest related result is Marberg [84], whose character and orbit enumeration for the unitriangular group is the closest account of the coadjoint data of $$\mathrm{ut}_n$$. A tractable special case would be strict log-concavity for a single infinite family of indices, such as the central ones. In tests on the corpus described in the stress-test section, strict log-concavity was confirmed for $$\mathrm{ut}_4$$, $$\mathrm{ut}_5$$, and $$\mathrm{ut}_6$$ over $$\mathbb F_2$$, for $$\mathrm{ut}_4$$ and $$\mathrm{ut}_5$$ over $$\mathbb F_3$$, and for $$\mathrm{ut}_4$$ over $$\mathbb F_5$$. A counterexample would be an interior index of some $$\mathrm{ut}_n$$ where the strict inequality fails, which would show that even the chain falls short of strict concentration.

**Conjecture 96** *(Adjoint–coadjoint incidence anticorrelation)*. For every nonabelian pattern Lie algebra $$L=L_P$$ and every prime power $$q$$, sampling $$(x,f)$$ uniformly on the incidence variety $$I_L=\{(x,f):f([x,L])=0\}$$ gives $$\operatorname{Cov}(\operatorname{rank}(\operatorname{ad}_x),\operatorname{rank}(B_f))<0$$, with covariance zero exactly when $$L_P$$ is abelian.

*Significance.* The incidence variety of the proposition pairs an element with a functional annihilating its adjoint image. The conjecture asserts that a high adjoint rank leaves little room for the coadjoint form to be large, so the two ranks are negatively correlated on $$I_L$$. The nearest related result is Coll–Mayers [81], whose coadjoint-orbit analysis of Lie poset algebras is the setting in which $$\operatorname{rank}(B_f)$$ is an orbit dimension. A tractable special case is the abelian case, where both ranks are zero and the covariance vanishes, giving the equality clause. In tests on the corpus described in the stress-test section, the covariance was negative on every nonabelian poset tested and exactly zero on all sixteen abelian ones. The statement is calibrated to the strongest form that holds. The stronger conditional stochastic-order and conditional-mean forms are false, so the sign of the covariance is the surviving claim. A counterexample would be a nonabelian poset with nonnegative incidence covariance, which would decouple the two ranks on the variety that defines their duality.

## Stress tests and independent recomputation

Each statement was tested three ways: against the literature, against computation well beyond its original range, and against an independent reimplementation.

*Layer 1: literature.* Five independent searches combed OEIS, arXiv, and the standard references for prior art, producing the novelty labels and the attributions used throughout. Each search was run at neighbourhood depth: defining objects, derived sequences, OEIS comments, and the abstracts and bodies of near-neighbour papers read in full rather than skimmed from search summaries—the depth at which, for instance, OEIS A088054’s intersection comment (Conjecture 21(ii)) and the second half of Lillie’s abstract (the primorial companion) are found, neither being visible in the defining sequences or in a search snippet. This layer also fixes two attributions used above: the $$k\ge1$$ Stern list of Conjecture 12 is OEIS A060003 verbatim, with $$1493$$ the largest known Stern prime, and the primorial-twin statement is Lillie’s [5].

*Layer 2: computational refutation.* Every falsifiable-by-instance statement was pushed at least a decade past its original bound: exception hunts across $$(10^8,10^9]$$ for Conjectures 5, 12, 17, 22; the uniformity of Conjecture 8 stressed on $$d\le6000$$; the statistical laws re-tested at $$4\times10^9$$ (Conjectures 1, 4, 9, 11, and 13, and the quintuplet calibration count reported with Conjecture 8); the recovery clause of Conjecture 3 tested on fresh moduli $$q\in(3000,6000]$$. No statement moved.

Each statement was also verified at large scale: the Conjecture 10 profile across $$150$$ shifts and the moment law for its constants $$C(d)$$ (derived mean $$2.7456$$ and sd $$1.6840$$ against measured $$2.7434$$ and $$1.6726$$); the cubic family moments and uniformity of Conjecture 15 ($$294$$ constants, $$57$$ count profiles); the triplet and sexy-pair races of Conjectures 18 and 19 at $$10^9$$ and the Stern lanes of Conjecture 12 on $$2{,}500$$ samples at $$10^8$$; the chain of Conjecture 24 over five decades to $$10^7$$; the null race of Conjecture 14 at $$10^7$$; the Fibonacci–Lucas joint scan to $$p\le10^4$$; factorial twins to $$n=700$$; the CRT-exact factorization of Conjecture 6 through a joint period of $$1.2\times10^8$$, with the scan extended to $$n=6000$$; the pinned average $$G(H)$$ of Conjecture 2 computed exactly to $$H=3000$$; the boundary trichotomy of Conjecture 22 with two new lanes counted at $$10^6$$; the least-summand law of Conjecture 5 on $$2{,}000$$ samples; the covariance kernels of Conjectures 8(ii) and 16(ii) evaluated over $$870$$ and $$1{,}225$$ pairs, with the moving-window randomization of Conjecture 8(ii) over $$2000$$ windows (empirical correlation matrix matching the predicted kernel entrywise at $$0.86$$); the orientation-resolved twin-member profile of Conjecture 17 on $$150$$ samples; the race autocorrelation and running-maximum measurements of Conjecture 9 at $$10^9$$ against simulated nulls; the singular-series waiting-time clause of Conjecture 11(iii) (regression coefficient $$-0.466$$ against the predicted $$-\tfrac12$$); the stratified experiment of Conjecture 3 on $$80$$ moduli; the multibase quotient tests of Conjecture 7 on $$664{,}577$$ primes; and the weighted drift and internal null lane of Conjecture 4 on $$400$$ fresh samples, together with the cousin-race predictions of the contamination calculus, Conjecture 1(v), at $$10^9$$ (leadership log-densities $$0.99$$ and $$0.92$$ on the predicted sides). In each case the prediction was derived before the corresponding data were taken.

*Layer 3: independent replication.* Constants were recomputed from their definitions, and sequences recounted, by implementations developed independently of the primary computation and working from the bare statements alone. All recomputed constants landed inside the stated truncation error, and all recounts agreed. The same layer reproduced the Fibonacci deficit recorded at Conjecture 20 and the ordering anomaly of Remark 1, confirming that both are properties of the primes rather than of a single implementation.

One methodological conclusion is worth recording. The mathematical failure modes in this subject are not statistical but *algebraic*: factorizations and congruence collapses living on density-zero or positive-density-but-structured subsequences—the cubes obstructing $$n=p+k^3$$ (Theorem 1), the composite-$$k$$ factorization of $$D_k$$ (Conjecture 23(i)), the $$k=4$$ parity branch of Conjecture 25, the inadmissible naive chain of Conjecture 24. Probabilistic sanity checks, however extensive, integrate over density and cannot see such families; only structural tests—testing a claimed exception census on special subsequences, for instance—find them. A verification that only re-runs an existing count at a larger bound is blind to every one of them.

*Part IV.* The Part IV verification programme follows the same standard. The rank formula was checked against direct linear algebra over $$\mathbb F_2$$, $$\mathbb F_3$$, and $$\mathbb F_5$$ on eighteen thousand random pairs of a graph and an element before the proof was written. The irreducibility claim of Conjecture 57 was verified by exact factorization over $$\mathbb Z$$ for all $$996$$ connected graphs on at most seven vertices. The recovery statements of Conjectures 58, 65, and 66 were tested on every known collision class of $$C_G$$: the $$119$$ classes among the $$1252$$ graphs on at most seven vertices, a randomized eight-vertex corpus, the unique class among all $$3159$$ trees on fourteen vertices, refound independently by exhaustive search, and the first unicyclic collision at ten vertices, with $$Q_G$$, $$\gamma$$, and $$i$$ agreeing in every class. The rigidity statements were scanned exhaustively on at most seven vertices, with six thousand random eight-vertex graphs added for Conjecture 59 and the scan for Conjecture 61 restricted to graphs with at least four edges, and the class-restricted statements were tested on six-thousand-graph random holdouts for each of Conjectures 62, 63, and 64, spanning $$2747$$, $$3192$$, and $$5598$$ distinct binary specializations respectively, together with all $$656$$ binary classes of ten-vertex unicyclic graphs for Conjecture 63. The log-concavity and support statements of Conjectures 67 to 71 were verified on the full atlas of graphs on at most seven vertices and twenty-five hundred random graphs on eight to ten vertices, with the eight-vertex counterexample to the second-order slice strengthening reconfirmed by the independent implementation. The tree programme of Conjectures 72 to 76 was verified exhaustively over all trees through fourteen vertices, for Conjectures 73 and 74 with $$q\in\{2,3,4,5\}$$ through twelve vertices, $$q\in\{2,3\}$$ at thirteen, and $$q=2$$ at fourteen, and the sharpness failure at $$(n,q)=(4,2)$$ recorded at Conjecture 73 was found in this verification rather than assumed. A seven-vertex pair refutes Conjecture 63, below the ten-to-thirteen-vertex range of those holdouts. An exhaustive rescan locates it as the unique violating class among trees and connected unicyclic graphs through nine vertices, and the tree case was reverified exhaustively through fourteen vertices.

*Part V.* The Part V verification programme follows the same standard, on an independently generated corpus of all $$87$$ unlabelled posets on at most five points, over $$\mathbb F_2$$ and $$\mathbb F_3$$ fully and $$\mathbb F_5$$ to dimension six, cross-checked against the deposited enumerators. The calibration identity held with no exception. The determination statements were tested on every adjoint-collision class: the adjoint-to-Kirillov determination of Conjecture 77 held across $$64$$ classes, and the lower-central factor vector, $$\dim\operatorname{Der}$$, and $$\dim\operatorname{Cent}$$ of Conjectures 78, 80, and 82 were constant on every class. The characteristic statements of Conjectures 83 and 84 were confirmed by agreement of the attained adjoint-rank and Kirillov-rank sets across $$\mathbb F_2$$, $$\mathbb F_3$$, and $$\mathbb F_5$$ in every case, the two-field rigidity of Conjecture 85 forced equality at $$q=5$$ across $$16$$ three-field collision classes, and the adjoint field monotonicity of Conjecture 86 held as first-order dominance in all $$221$$ field-pair tests while its likelihood-ratio strengthening failed. The centre-one statements were tested on all $$43$$ centre-one records, where the Kirillov enumerator determined the adjoint enumerator, $$R_{P,q}$$ had nonnegative integer coefficients, and $$R_{P,q}$$ had interval support and was unimodal throughout this corpus, with log-concavity failing four times. The unimodality was subsequently refuted by a seven-point poset outside the corpus, and Conjecture 90 is recorded as resolved false. The forest statements were tested on the forest class, where the Kirillov enumerator determined the adjoint enumerator across $$44$$ forest-collision classes, the Kirillov support filled every even rank up to $$b_K$$, the even-rank sequence was unimodal, and the bound $$b_K\le 2b_A$$ held everywhere while the unrestricted bound failed fourteen times off the forest class. The unitriangular strict log-concavity of Conjecture 95 was confirmed for $$\mathrm{ut}_4$$, $$\mathrm{ut}_5$$, and $$\mathrm{ut}_6$$ over $$\mathbb F_2$$, for $$\mathrm{ut}_4$$ and $$\mathrm{ut}_5$$ over $$\mathbb F_3$$, and for $$\mathrm{ut}_4$$ over $$\mathbb F_5$$, and the incidence anticorrelation of Conjecture 96 gave negative covariance on every nonabelian poset and exactly zero on all sixteen abelian ones. Two statements were not independently recomputed: the cohomology recoveries of Conjectures 79 and 81 rest on the deposited computation of $$H^2$$ and $$H^3$$ (ordinary) and $$H^1$$, $$H^2$$, and $$H^3$$ (adjoint), our reverification having not recomputed Lie-algebra cohomology. Three statements, Conjectures 79, 81, and 85, are supported only by the restricted tests recorded with each, and their general forms should not be read as carrying evidence comparable to the other conjectures. Two further statements, Conjectures 87 and 90, are false as stated and are recorded as resolved false with the seven-point counterexamples given in their resolutions.

## An open question

**Question 1.**

Determine $$\Theta(q)$$ of Conjecture 3: derive, from the Hardy–Littlewood correlations or otherwise, the first-order deficit of $$\mathbb E_a\,\mathrm{Li}(p(a,q))/\varphi(q)$$ below its random-model value $$1$$—equivalently, explain quantitatively why the primes in their natural order occupy residue classes faster than any exchangeable resampling of themselves.

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

12. T. Oliveira e Silva, S. Herzog, and S. Pardi, *Empirical verification of the even Goldbach conjecture and computation of prime gaps up to $$4\times10^{18}$$*, Math. Comp. 83 (2014), no. 288, 2033–2060. DOI: 10.1090/S0025-5718-2013-02787-1.

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

61. W. Banaszczyk, *Balancing vectors and Gaussian measures of $$n$$-dimensional convex bodies*, Random Structures Algorithms 12 (1998), no. 4, 351–360.

62. W. Banaszczyk, *On series of signed vectors and their rearrangements*, Random Structures Algorithms 40 (2012), no. 3, 301–316.

63. S. Chatterjee and S. R. S. Varadhan, *The large deviation principle for the Erdős–Rényi random graph*, European J. Combin. 32 (2011), no. 7, 1000–1017.

64. W. T. Gowers, B. Green, F. Manners, and T. Tao, *On a conjecture of Marton*, Ann. of Math. (2) 201 (2025), no. 2, 515–549.

65. V. S. Grinberg and S. V. Sevast'yanov, *Value of the Steinitz constant*, Funct. Anal. Appl. 14 (1980), 125–126.

66. H. Hatami and S. Norine, *The entropy of random-free graphons and properties*, Combin. Probab. Comput. 22 (2013), no. 4, 517–526.

67. R. Kenyon, C. Radin, K. Ren, and L. Sadun, *Multipodal structure and phase transitions in large constrained graphs*, J. Stat. Phys. 168 (2017), no. 2, 233–258.

68. B. Kitchens, *Expansive dynamics on zero-dimensional groups*, Ergodic Theory Dynam. Systems 7 (1987), no. 2, 249–261.

69. J. Kułaga-Przymus and M. D. Lemańczyk, *Entropy rate of product of independent processes*, Monatsh. Math. 200 (2023), 131–162; arXiv:2004.07648.

70. E. Lindenstrauss, D. Meiri, and Y. Peres, *Entropy of convolutions on the circle*, Ann. of Math. (2) 149 (1999), no. 3, 871–904.

71. K. Matomäki, M. Radziwiłł, and T. Tao, *An averaged form of Chowla's conjecture*, Algebra Number Theory 9 (2015), no. 9, 2167–2196.

72. J. Neeman, C. Radin, and L. Sadun, *Typical large graphs with given edge and triangle densities*, Probab. Theory Related Fields 186 (2023), 1167–1223.

73. D. S. Ornstein and B. Weiss, *Every transformation is bilaterally deterministic*, Israel J. Math. 21 (1975), 154–158.

74. T. Tao, *Sumset and inverse sumset theory for Shannon entropy*, Combin. Probab. Comput. 19 (2010), no. 4, 603–639.

75. T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, Forum Math. Pi 4 (2016), e8, 36 pp.

76. T. Tao and J. Teräväinen, *The structure of logarithmically averaged correlations of multiplicative functions, with applications to the Chowla and Elliott conjectures*, Duke Math. J. 168 (2019), no. 11, 1977–2027.

77. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bull. Lond. Math. Soc. 54 (2022), 1923–1943.

78. P. Tittmann, I. Averbouch, and J. A. Makowsky, *The enumeration of vertex induced subgraphs with respect to the number of components*, European J. Combin. 32 (2011), 954–974.

79. J. A. Bondy and R. L. Hemminger, *Graph reconstruction—a survey*, J. Graph Theory 1 (1977), 227–268.

80. A. Cameron, V. E. Coll, Jr., N. Mayers, and N. Russoniello, *The breadth of Lie poset algebras*, Linear Multilinear Algebra 71 (2023), no. 16.

81. V. E. Coll, Jr. and N. Mayers, *The index of Lie poset algebras*, J. Combin. Theory Ser. A 177 (2021), 105324.

82. L. Lampret and A. Vavpetič, *(Co)homology of poset Lie algebras*, arXiv:1504.07743 (2015).

83. Z. Halasi and P. P. Pálfy, *The number of conjugacy classes in pattern groups is not a polynomial function*, J. Group Theory 14 (2011), no. 6, 841–854.

84. E. Marberg, *Combinatorial methods of character enumeration for the unitriangular group*, J. Algebra 345 (2011), 295–323.

85. P. Delsarte, *Bilinear forms over a finite field, with applications to coding theory*, J. Combin. Theory Ser. A 25 (1978), 226–241.

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

### Conjecture 6: Polynomial–exponential entanglement

Primality of $$n^2+2^n$$ imposes local conditions that depend on $$n$$ through two different moduli at once, $$p$$ and the multiplicative order of $$2$$ modulo $$p$$. A product of per-prime densities would assume these conditions independent, which nothing justifies. The conjecture instead uses survivor densities computed exactly over the joint period of all primes up to $$z$$, asserts that these converge along the canonical exhaustion, and asserts that the limit governs the count, which grows like $$\log N$$. The computation found the joint density to factor exactly through $$p\le19$$, and whether that persists is left as an open question about the orbits of $$2$$. The conjecture is a model for prime counting in sequences outside the polynomial world of Bateman and Horn.

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

Prime divisors of $$F_p$$ have rank of apparition $$p$$ (the least index $$m$$ with $$p\mid F_m$$) and odd prime divisors of $$L_p$$ have rank $$2p$$, so the two numbers share no odd prime factor. This removes one source of dependence but not those entering through the order structure, in the sense of Grantham and Granville. The conjecture is that only finitely many $$p$$ give both prime, the joint hazards having convergent sum. The naive independence accounting prices the whole index range beyond $$10^4$$, in which the catalogued index $$148091$$ falls with both values probable primes, at about fourteen in a thousand. That figure is recorded descriptively as a rare event, with no significance claim attached, because the model was examined only after the index was known. It is enough to leave the finiteness claim without a completeness list.

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

### Conjecture 32: Tested Gauss-polyspectral reciprocity

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

### Conjecture 51: Relative polynomial pretentiousness inverse principle

A multiplicative function is one that turns products into products, and the pretentious distance of Granville and Soundararajan measures how closely such a function mimics another one at the primes. This conjecture concerns averages of a product of multiplicative functions evaluated along several polynomials, such as $$f_1(n^2+1)f_2(2n+1)$$, where each prime is weighted by how often it divides values of the relevant polynomial. The statement asserts that if these averages, taken with logarithmic weights, do not tend to zero, then the only possible explanation is the obvious one: each function must mimic a Dirichlet character (a periodic multiplicative function) twisted by a power $$n^{it}$$, the twists must cancel in the exact accounting $$\sum_j t_j\deg P_j=0$$, and the characters must be jointly compatible at a common modulus. For linear polynomials the two-point and odd-order cases are theorems of Tao and of Tao and Teräväinen, and the even-order linear case is the logarithmic Elliott conjecture, so all of the new content lives at degree two and higher, where even the average of a single $$f(n^2+1)$$ is open.

### Conjecture 52: Monotone threshold purification of vector paths

Take $$m$$ vectors in $$d$$-dimensional space, each of length at most one, and let each grow from zero to full length according to its own nondecreasing schedule. The conjecture asserts that the gradual schedule can be replaced by a jump process, in which each arrow appears fully grown at one chosen instant, so that at every moment the running sums of the two films differ by at most a constant times $$\sqrt d$$. The special case in which all schedules are linear and the arrows sum to zero is a famous open problem, the Euclidean Steinitz prefix-sum problem, which asks whether zero-sum vectors can always be ordered so that every partial sum has length $$O(\sqrt d)$$. The best known bound, due to Banaszczyk, carries an extra logarithm in the number of vectors, and for the full threshold form no bound depending on the dimension alone is known at all. A diagonal example with coordinate vectors shows the $$\sqrt d$$ scale cannot be improved, and the statement only has content when the dimension is large, so no small computer search can decide it.

### Conjecture 53: Entropy dimension of random-free graphons

A graphon is a symmetric measurable function on the unit square that serves as a limit object for large dense graphs, and it is called random-free when it takes only the values zero and one, so that sampling a graph from it involves no coin flips beyond the choice of vertex positions. Each vertex position has a row, its profile of connections, and the rows form a metric space in which the distance between two rows is the measure of the set where they disagree. The conjecture asserts that when this row space is Ahlfors regular of dimension $$s$$, meaning that balls of radius $$r$$ carry measure comparable to $$r^s$$, the Shannon entropy of the sampled $$n$$-vertex graph grows like $$s\,n\log n$$, because each of the $$n$$ vertices carries a latent type resolvable at scale $$1/n$$ and there are about $$n^s$$ such types. A theorem of Hatami and Norine says random-free graphons are exactly those with subquadratic entropy and that any subquadratic growth can occur, so the geometric hypothesis is exactly what pins the coefficient. The construction of regular row spaces of every fractional dimension up to two is part of the statement, and the refined error term of order $$n$$ is recorded separately as a strictly stronger open claim. The limit law itself is proved in the proposition accompanying the statement, by a collision-entropy lower bound and a quantization upper bound.

### Conjecture 54: Hessian principle for an isolated microcanonical phase

In statistical physics one studies ensembles of systems conditioned to have prescribed values of a few observables, and the analogous graph ensembles fix the densities of several small subgraphs and colour classes of prescribed proportions. Large deviation theory, following Chatterjee and Varadhan, describes the most likely shape of such a conditioned graph as the maximizer of a suitable entropy functional, and later work showed these maximizers are often multipodal, built from finitely many blocks. This conjecture concerns the fluctuations around an isolated, nondegenerate maximizer: it predicts that the block-average statistics of the conditioned graph, projected onto the manifold of feasible values and centred at their mean, are asymptotically Gaussian at scale $$1/n$$ with covariance given by the inverse Hessian (the matrix of second derivatives) of the constrained entropy. The attainable constraint values are spaced at the far finer scale $$1/n^2$$, so no arithmetic obstruction interferes, and the genuine difficulty is comparing exact microcanonical counts with their Laplace approximations. No fluctuation theorem of this kind is currently known in any nontrivial case.

### Conjecture 55: Sharp stability of entropy idempotence

On a finite abelian group, convolving a probability measure with itself, that is, adding two independent samples, can only increase Shannon entropy, and the increase is zero exactly for uniform measures on cosets of subgroups. The conjecture upgrades this equality case to a sharp stability estimate: the squared total variation distance from any measure to the nearest coset uniform is at most a universal constant times the entropy increase. Known entropic inverse theorems, from Tao's sumset entropy theory to the entropic polynomial Freiman–Ruzsa theorem of Gowers, Green, Manners, and Tao, conclude in Ruzsa distance, a weaker entropic notion of closeness, and neither prove nor refute the total variation form. The extremal analysis is delicate: small perturbations of a coset uniform only achieve half the conjectured ratio, and the true near-extremizers are discretized Gaussians on $$\mathbb Z/p\mathbb Z$$ at scales between one and $$p$$, whose entropy increase approaches the entropy-power constant $$\tfrac12\log2$$ while their distance to every coset approaches one, which forces the constant to be at least $$2/\log2$$, a value conjectured to be exactly sharp. On $$\mathbb Z/p\mathbb Z$$, which has no proper nontrivial subgroups, the statement becomes a discrete entropy-power inequality for spread measures.

### Conjecture 56: Stationary convolution-entropy rigidity

A stationary process over a finite abelian group is a two-sided random sequence of group elements whose law is invariant under time shifts, and its Kolmogorov–Sinai entropy measures the information produced per symbol. Adding two independent copies of the process coordinatewise can only increase this entropy, and the conjecture characterizes exactly when nothing is gained: precisely when, after quotienting by the group of translations that preserve the law, the remaining process has zero entropy, so that all the randomness was already uniform, Haar-type noise along a subgroup of sequences. The soft direction follows from two standard ingredients, the Abramov–Rokhlin entropy formula for group extensions and the entropy bound for factors of independent joinings, and is recorded as a conditional proposition. The binary case is the sharpest test: by Kitchens' structure theory of group shifts, the conjecture asserts that every ergodic binary process with entropy strictly between zero and $$\log2$$ strictly gains entropy when combined by XOR with an independent copy of itself. The most promising place to look for counterexamples, so far unexplored, is the bilaterally deterministic processes of Ornstein and Weiss and the $$T,T^{-1}$$-type constructions.

### Conjecture 57: Irreducibility and connectivity

A graphical Lie algebra is built from a graph by taking one generator per vertex and one central generator per edge, the bracket of two vertex generators being the central generator of their edge when they are adjacent and zero otherwise. Rossmann's class-counting polynomial $$C_G(X,Y)$$ packages, over all vertex subsets $$S$$, the size $$\vert S\vert $$ and the invariant $$\rho_G(S)=\vert N[S]\vert -c(G[S])$$, the size of the closed neighbourhood minus the number of induced components, and its specializations count conjugacy classes of the associated finite groups by size. The conjecture asserts that the shifted form $$H_G(U,Y)=C_G(1+U,Y)$$ factors over the integers exactly when the graph falls into disjoint pieces. One direction is Rossmann's product formula for disjoint unions, so the content is that a connected graph always yields an irreducible polynomial, a claim verified by exact factorization for all $$996$$ connected graphs on at most seven vertices.

### Conjecture 58: Recovery of the subgraph-component polynomial

The subgraph-component polynomial of Tittmann, Averbouch, and Makowsky records, for each vertex subset, its size and the number of connected components it induces, while the class-counting polynomial records the size together with the closed neighbourhood minus that same component count. The two invariants are transverse projections of the induced-subgraph structure, and no formula converting one into the other is known. The conjecture asserts that graphs with equal class-counting polynomials nevertheless have equal subgraph-component polynomials. The evidence comes from collision classes, pairs of nonisomorphic graphs sharing the polynomial $$C$$: all known classes were assembled, including the unique one among the $$3159$$ trees on fourteen vertices, and the subgraph-component polynomial agrees in every one.

### Conjecture 59: Two-field rigidity

Evaluating the class-counting polynomial at $$X=q$$ gives the distribution of the rank of the adjoint map $$\operatorname{ad}_x$$, the linear map bracketing with a random element $$x$$ of the Lie algebra over $$\mathbb F_q$$. The conjecture asserts that the two smallest fields already suffice: if two graphs give the same rank distribution over $$\mathbb F_2$$ and over $$\mathbb F_3$$, then their entire polynomials agree, and with them the distributions over every finite field. Since $$C_G(2,Y)$$ is the unweighted rank census of vertex subsets and $$C_G(3,Y)$$ the census weighted by $$2^{\vert S\vert }$$, the statement says that two weighted shadows of a two-dimensional array determine it whenever the array comes from a graph, a rigidity that fails for arbitrary arrays.

### Conjecture 60: Hybrid rigidity

This conjecture mixes the two polynomials of the part: the binary specialization $$C_G(2,Y)$$, which is the rank distribution over the two-element field, and the full subgraph-component polynomial $$Q_G$$. Together they are conjectured to determine the entire class-counting polynomial. The pairing is calibrated, because replacing $$Q_G$$ by the degree sequence, the list of vertex degrees, is known to be insufficient. The statement therefore isolates exactly what the component information adds beyond any degree data.

### Conjecture 61: Binary edge-deck reconstruction

The edge reconstruction conjecture, surveyed by Bondy and Hemminger, asks whether a graph with enough edges is determined by the multiset of its edge-deleted subgraphs considered up to isomorphism. Here each of those cards is compressed much further, to the single polynomial $$C_{G-e}(2,Y)$$, the rank distribution of the card over $$\mathbb F_2$$. The conjecture asserts that this deck of polynomial shadows still determines the graph once it has at least four edges. It is deliberately the highest-risk statement of the part, verified exhaustively for all graphs on at most seven vertices with at least four edges, and a counterexample would calibrate precisely how much information edge deletion destroys.

### Conjecture 62: Bipartite binary rigidity

A graph is bipartite when its vertices split into two sides with all edges crossing between them. Within this class the conjecture asserts one-field rigidity: the single specialization $$C_G(2,Y)$$ determines the whole class-counting polynomial. No such statement can hold for all graphs, since it already fails for disconnected pseudoforests, so the class restriction is doing genuine work. The evidence is a six-thousand-graph random holdout on nine to twelve vertices spanning $$2747$$ distinct binary specializations.

### Conjecture 63: Connected-pseudoforest binary rigidity (resolved false)

The conjecture proposed that within trees and connected unicyclic graphs the binary specialization $$C_G(2,Y)$$ determines the whole class-counting polynomial. It is false: two seven-vertex unicyclic graphs, a four-cycle carrying three leaves and a triangle carrying a short path and two further leaves, share $$C(2,Y)$$ while their polynomials differ already at the singleton level, which records the degree multiset. An exhaustive scan shows the pair is the only violating class among trees and connected unicyclic graphs through nine vertices. One member is bipartite and the other chordal, so the neighbouring rigidity conjectures are untouched, and the tree case, which survives exhaustively through fourteen vertices, remains open.

### Conjecture 64: Chordal binary rigidity

A graph is chordal when every cycle of length at least four has a chord, an edge joining two nonconsecutive vertices of the cycle, which makes the class the standard dense companion to trees. The conjecture asserts one-field rigidity within chordal graphs, so that the $$\mathbb F_2$$ rank distribution determines the class-counting polynomial. Together with Conjectures 62 and 63 it probes whether rigidity is a sparsity phenomenon or a structural one. The evidence is a six-thousand-graph random holdout on nine to twelve vertices spanning $$5598$$ distinct binary specializations.

### Conjecture 65: Recovery of the domination number

A dominating set is a vertex subset whose closed neighbourhood is the entire graph, and the domination number $$\gamma(G)$$ is the least size of one. The conjecture asserts that graphs with equal class-counting polynomials have equal domination numbers. The statement is placed with unusual precision, since Rossmann proved that connected dominating sets can be counted from the polynomial, while the total domination number is known not to be determined by it, so $$\gamma$$ sits strictly between a theorem and a false analogue. Every known collision class of the polynomial has agreeing domination number.

### Conjecture 66: Recovery of the independent domination number

The independent domination number $$i(G)$$ is the least size of a set that is simultaneously independent, inducing no edges, and dominating. Independence forces the induced component count $$c(G[S])$$ to equal $$\vert S\vert $$, so independent dominating sets couple the two quantities that the invariant $$\rho_G$$ mixes. The conjecture asserts that equality of class-counting polynomials forces equality of $$i$$. As with the domination number, every known collision class agrees, including the unique fourteen-vertex tree class and the first unicyclic collision at ten vertices.

### Conjecture 67: Global double log-concavity

A sequence of nonnegative numbers is log-concave when each internal term satisfies $$a_i^2\ge a_{i-1}a_{i+1}$$, a strong form of unimodality standard in combinatorics. The conjecture concerns the coefficient sequence of $$f_G(1+Z)$$, a one-variable compression of the class-counting polynomial expanded at its singular point, and asserts that this sequence is log-concave and that the derived sequence $$L(a)_i=a_i^2-a_{i-1}a_{i+1}$$ is log-concave again. The double form is exactly calibrated, since the third iterate of the transform fails for a thirteen-vertex graph. The evidence is the full atlas of graphs on at most seven vertices and twenty-five hundred random graphs on eight to ten vertices.

### Conjecture 68: Strict log-concavity for connected graphs

For disconnected graphs the class-counting polynomial factors, and products are where equalities in log-concavity arise, so the natural refinement is that connectivity forces strictness. The conjecture asserts that for a connected graph with at least one edge, every interior position of the coefficient sequence of $$f_G(1+Z)$$ satisfies the strict inequality $$a_i^2>a_{i-1}a_{i+1}$$. A connected graph with an exact interior coincidence would be a structural surprise demanding an algebraic explanation. The corpus of Conjecture 67 shows strictness throughout the connected stratum.

### Conjecture 69: Strict second-order log-concavity

This conjecture asserts strict log-concavity one level up, for the transform $$L(a)$$ of the previous two statements, again for connected graphs with at least one edge. Its position is the sharpest the data permit, threaded between two known counterexamples: the third iterate of $$L$$ fails for a thirteen-vertex graph, and the second-order refinement of the rank-slice statement of Conjecture 70 fails at eight vertices. A violation would pin the exact rung at which the log-concavity hierarchy of graphs stops.

### Conjecture 70: Rank-slice strict log-concavity

Instead of compressing the polynomial to one variable, one can fix a rank value $$r$$ and extract the slice $$A_{G,r}(Z)=[Y^r]F_G(1+Z,Y)$$, which counts the vertex subsets achieving that rank, graded by size. The conjecture asserts that for connected graphs every slice that is not a single monomial is strictly log-concave at the interior of its support, so positivity holds fibre by fibre and not only in aggregate. The second-order strengthening of this statement is false for an eight-vertex graph, a counterexample reconfirmed by an independent implementation, so the slice hierarchy provably stops one level below the global one.

### Conjecture 71: Interval support at fixed rank (resolved false)

Beneath any log-concavity claim lies a support claim, since a sequence with internal gaps cannot be strictly log-concave. The conjecture proposed that for every graph and every attainable rank $$r$$, the set $$K_r(G)$$ of sizes of vertex subsets achieving rank $$r$$ is an interval of integers, but it is false: a connected eight-vertex graph attains rank five at sizes $$\{1,3,4,5,6\}$$, skipping size two, and an exhaustive scan finds exactly two such graphs and none on fewer vertices. The failure does not reach the slice log-concavity of Conjecture 70, whose shifted slices multiply the raw size counts by a binomial that fills the gap, so those slices stay log-concave on the very graphs that break the raw interval. The transposed statement was already false, so neither direction of the array is gapless, and the tree case remains open.

### Conjecture 72: Coefficientwise tree extremality

Among trees on $$n$$ vertices, the path $$P_n$$ and the star $$K_{1,n-1}$$ are the extremes of the two statistics that drive the rank landscape, the number of internal vertices and the diameter. The conjecture asserts that the shifted polynomial of every tree is sandwiched between those of the path and the star coefficient by coefficient, $$f_{P_n}(1+Z)\le f_T(1+Z)\le f_{K_{1,n-1}}(1+Z)$$, with equality only at the extremes themselves. Through Rossmann's dictionary each coefficientwise inequality encodes a family of inequalities between conjugacy-class censuses over every finite field simultaneously. The verification is exhaustive over all $$n$$-vertex trees through $$n=14$$.

### Conjecture 73: Star rank-majorization

One probability vector majorizes another when, after sorting both in decreasing order, every partial sum of the first dominates the corresponding partial sum of the second, so majorization is a uniform statement that one distribution is more concentrated than the other. The conjecture asserts that for $$n\ge5$$ and every prime power $$q$$, the adjoint-rank distribution of the star majorizes that of every $$n$$-vertex tree over $$\mathbb F_q$$. The hypothesis is sharp: at $$n=4$$ and $$q=2$$ the star fails to majorize the path, a failure found during verification, and the dual guess that the path is majorization-minimal is simply false. A short argument reduces the whole comparison to a single anti-concentration bound, that no rank is attained with probability above $$1-1/q$$, whose extremal value is the star's top atom and whose failure at $$(n,q)=(4,2)$$ is exactly the observed one. The surviving statement was tested exhaustively for $$q\in\{2,3,4,5\}$$ through twelve vertices, $$q\in\{2,3\}$$ at thirteen, and $$q=2$$ at fourteen.

### Conjecture 74: Tree rank-variance extremality

The variance of the adjoint rank of a uniformly random element is a different concentration scale from majorization, measuring the spread of the rank values rather than the shape of the ordered probabilities. The conjecture asserts that among $$n$$-vertex trees with $$n\ge4$$, for every prime power $$q$$, this variance is uniquely minimized by the path and uniquely maximized by the star. The star thus tops both scales at once, most concentrated in the majorization sense yet most spread in variance, and the two orders genuinely differ, since the variance statement begins at $$n=4$$ where the majorization statement already fails. The verification schedule matches Conjecture 73.

### Conjecture 75: Leaf-count rigidity

The lemma accompanying the part proves that a tree on $$n$$ vertices realizes at least $$n-\ell(T)+2$$ distinct values of the invariant $$\rho_T$$, where $$\ell(T)$$ is the number of leaves, by walking a breadth-first chain through the internal vertices. The conjecture upgrades the bound to a characterization: equality holds exactly for the path and the star. The forward half, that these two trees do achieve equality, is now proved by a direct computation of $$s$$, and the substantive half that remains open is that no third shape is equally tight. All trees through fourteen vertices confirm the rigidity.

### Conjecture 76: Diameter rigidity

The same lemma proves the companion bound $$s(T)\ge\operatorname{diam}(T)+1$$, realizing one new rank value for each step along a diametral path. The conjecture again asserts that equality holds exactly for the path and the star, so that the two lower bounds of the lemma, one governed by leaves and one by diameter, pin the same extremal pair from independent directions. The forward half is proved together with that of Conjecture 75, the path giving $$s(P_n)=n$$ and the star $$s=3$$, so only uniqueness remains open. A tree of small diameter attaining equality would show the diameter bound loose in a structured way, and the exhaustive search through fourteen vertices finds none.

### Conjecture 77: Adjoint–Kirillov determination

A pattern Lie algebra is built from a finite poset by taking one matrix unit $$e_{ij}$$ for each strict relation $$i<_Pj$$ inside the strictly upper triangular matrices, so its dimension is the number of relations. Two enumerators record the same bracket from opposite sides: the adjoint enumerator $$A_{P,q}$$ tallies the ranks of the adjoint map $$\operatorname{ad}_x=[x,\cdot]$$ over all elements $$x$$, and the Kirillov enumerator $$K_{P,q}$$ tallies the ranks of the alternating Kirillov form $$B_f(u,v)=f([u,v])$$ over all functionals $$f$$. The conjecture asserts that the first determines the second: any two posets with the same adjoint enumerator have the same Kirillov enumerator. The incidence identity already forces the two to agree at two evaluations, and the conjecture asserts that the agreement extends to the whole polynomial, verified across $$64$$ adjoint-collision classes.

### Conjecture 78: Lower-central recovery

The lower central series $$\gamma_1\supseteq\gamma_2\supseteq\cdots$$ of a Lie algebra is the descending chain in which each term is spanned by brackets of the previous term with the whole algebra, and its successive quotient dimensions measure how nilpotency unwinds degree by degree. Since the rank of $$\operatorname{ad}_x$$ is exactly the dimension of the image $$[x,L_P]$$, the adjoint enumerator aggregates the sizes of these images. The conjecture asserts that this aggregate already fixes the entire vector of lower-central factor dimensions, so that the graded shape of the nilpotency filtration is a function of the adjoint-rank distribution alone. In reverification the vector was constant on every adjoint-collision class.

### Conjecture 79: Ordinary Poincaré recovery

The Lie-algebra cohomology $$H^i(L_P,\mathbb F_q)$$ is computed from the Chevalley–Eilenberg complex, whose differentials are assembled from the structure constants of the bracket, and its dimensions are packaged in the Poincaré polynomial $$\sum_i\dim H^i U^i$$. The conjecture asserts that the adjoint enumerator, which sees those same structure constants only through the ranks of the adjoint maps, nonetheless determines the whole Poincaré polynomial. The tested evidence reaches only the second and third cohomology dimensions and rests on the deposited cohomology data rather than an independent recomputation, so the general statement should be read as more tentative than the others. The universal claim over all degrees is retained for provenance and flagged as such.

### Conjecture 80: Derivation recovery

A derivation of a Lie algebra is a linear map $$D$$ satisfying the Leibniz rule $$D[u,v]=[Du,v]+[u,Dv]$$, and the derivations form a Lie algebra $$\operatorname{Der}(L_P)$$ whose dimension is a standard structural invariant. Because the derivation condition is phrased entirely through the bracket, and the bracket is exposed to the enumerator through the adjoint maps, the conjecture asserts that the adjoint enumerator determines $$\dim\operatorname{Der}(L_P)$$. The evidence is that this dimension is constant on every adjoint-collision class, so posets indistinguishable by their adjoint-rank distribution have derivation algebras of equal size.

### Conjecture 81: Adjoint Poincaré recovery

Cohomology with coefficients in the adjoint module, $$H^i(L_P,L_P)$$, is the invariant that controls deformations of the Lie algebra, with $$H^2$$ classifying infinitesimal deformations and $$H^1$$ the outer derivations. The conjecture asserts that the adjoint enumerator determines all of these dimensions. As with Conjecture 79, the tested evidence reaches only the first three adjoint-cohomology dimensions and rests on the deposited data, so the statement over all degrees should be read as more tentative than the others.

### Conjecture 82: Centroid-dimension recovery

The centroid $$\operatorname{Cent}(L_P)$$ is the associative algebra of linear maps that commute with every adjoint map $$\operatorname{ad}_x$$, a measure of how far the algebra is from being central-simple. Since it is defined directly through the adjoint representation, whose coarsest numerical shadow is the adjoint-rank distribution, the conjecture asserts that $$\dim\operatorname{Cent}(L_P)$$ is determined by the adjoint enumerator. The supporting evidence is that this dimension is constant on every adjoint-collision class.

### Conjecture 83: Adjoint spectrum characteristic independence

For a fixed poset the adjoint ranks that actually occur, as $$x$$ ranges over $$L_P(\mathbb F_q)$$, form a set of integers, and one may ask whether that set changes with the field. The conjecture asserts it does not: the attained adjoint ranks depend only on the poset, while only the multiplicities, the coefficients of the enumerator, move with $$q$$. This sits against the background of Halasi and Pálfy's theorem that the associated class counts are genuinely non-polynomial in $$q$$, so the invariance of the bare support is the sharper phenomenon. The attained-rank sets agreed across $$\mathbb F_2$$, $$\mathbb F_3$$, and $$\mathbb F_5$$ throughout.

### Conjecture 84: Kirillov spectrum characteristic independence

A coadjoint orbit of a nilpotent Lie algebra corresponds to a functional $$f$$, and its dimension is the rank of the alternating Kirillov form $$B_f$$, always an even number. The conjecture asserts that the set of even ranks realized by these forms is independent of the field, mirroring the adjoint statement on the coadjoint side. The relevant background is Delsarte's classification of alternating-form rank distributions together with the non-polynomiality of the class counts, against which the invariance of the attained support is the finer claim. The Kirillov-rank sets agreed across $$\mathbb F_2$$, $$\mathbb F_3$$, and $$\mathbb F_5$$ in every tested case.

### Conjecture 85: Two-field arithmetic rigidity

Evaluating over the two smallest fields gives two weighted shadows of a poset's rank array. The conjecture asserts that these already determine the array over every finite field: if two posets have equal adjoint enumerators over $$\mathbb F_2$$ and over $$\mathbb F_3$$, they agree over all $$\mathbb F_q$$. Its only tested holdout beyond $$q=2,3$$ is the single field $$q=5$$, on $$16$$ three-field collision classes, so the general statement should be read as more tentative than the others. Since Halasi and Pálfy show larger fields can behave differently in general, the claim is that this particular family is nonetheless rigid, and it is retained for provenance with that narrow core stated plainly.

### Conjecture 86: Adjoint stochastic field monotonicity

One distribution first-order stochastically dominates another when, for every threshold, it puts at least as much mass at or above that threshold, a comparison of all upper tails at once. The conjecture asserts that raising the field from $$q$$ to $$q'$$ can only push the distribution of $$\operatorname{rank}(\operatorname{ad}_x)$$ upward in this sense. The calibration is exact: the stronger monotone-likelihood-ratio ordering, which compares the two distributions ratio by ratio, is false and fails three times already from $$q=2$$ to $$q=3$$, so first-order dominance is the surviving form. It held in all $$221$$ field-pair tests.

### Conjecture 87: Kirillov likelihood-ratio field monotonicity (resolved false)

Monotone likelihood-ratio order is the strong comparison under which the ratio of the two probability mass functions is monotone across the ranks, and it implies but is not implied by first-order dominance. The conjecture proposed that the coadjoint even-rank distributions are rigid enough to satisfy this strong ordering as the field grows, but it is false: a seven-point poset has Kirillov even-rank counts whose likelihood ratio from $$\mathbb F_2$$ to $$\mathbb F_3$$ rises and then falls across the ranks, so the order fails already at the smallest pair of fields. The weaker first-order Kirillov dominance, the coadjoint analogue of Conjecture 86, is left standing.

### Conjecture 88: Centre-one reverse determination

The centre $$Z(L_P)$$ is the set of elements bracketing to zero with everything, and here attention is restricted to posets whose pattern Lie algebra has a one-dimensional centre. Under that hypothesis the conjecture reverses the determination of Conjecture 77: the Kirillov enumerator determines the adjoint enumerator. The mechanism is that a line centre makes the incidence quotient between the two enumerators rigid enough to invert. The evidence is that the Kirillov enumerator determined the adjoint enumerator on all $$43$$ centre-one records.

### Conjecture 89: Centre-one Laplace positivity

The incidence identity shows that $$K_{P,q}-A_{P,q}$$ is divisible by $$(1-T)(1-qT)$$, and the quotient $$R_{P,q}$$ is the residual gap between the coadjoint and adjoint enumerators once those two forced roots are removed. The conjecture asserts that, when the centre is a line, this quotient is a genuine counting polynomial, with nonnegative integer coefficients rather than a signed difference. Positivity held on all $$43$$ centre-one records and is the foundation for the shape statement that follows.

### Conjecture 90: Centre-one quotient shape (resolved false)

A finite integer sequence is unimodal if it rises to a single peak and then falls, and it has interval support if its nonzero entries occupy a gapless block, while log-concavity, the condition $$a_i^2\ge a_{i-1}a_{i+1}$$, is strictly stronger than unimodality for positive sequences. The conjecture proposed that the coefficient sequence of the incidence quotient $$R_{P,q}$$ is unimodal with interval support whenever the centre is a line, but it is false: a seven-point poset with a line centre has a quotient whose coefficients are nonnegative and gaplessly supported yet dip into a strict interior valley, so unimodality fails while positivity and interval support survive.

### Conjecture 91: Hasse-forest reverse determination

The Hasse cover graph of a poset joins each element to those that cover it, and $$P$$ is a Hasse forest when this graph has no cycles. Under that structural hypothesis, complementary to the centre-one hypothesis of Conjecture 88, the conjecture again reverses the determination of Conjecture 77: the Kirillov enumerator determines the adjoint enumerator. The mechanism is that a forest of covers builds the coadjoint form from independent pieces, leaving the incidence quotient invertible. The Kirillov enumerator determined the adjoint enumerator across $$44$$ forest-collision classes.

### Conjecture 92: Hasse-forest coadjoint saturation

Because an alternating form has even rank, the Kirillov enumerator of any poset is supported on even integers, and its top value is the maximal Kirillov rank $$b_K$$, the dimension of the largest coadjoint orbit. The conjecture asserts that on a Hasse forest no even value below the top is skipped, so the support is the full even interval $$\{0,2,4,\ldots,b_K\}$$. The mechanism is that the independent covers of a forest allow the coadjoint rank to be adjusted one pair at a time. The forest Kirillov support filled every even rank in each tested case.

### Conjecture 93: Hasse-forest Kirillov unimodality

Once the even-rank support of a Hasse forest is known to be gapless, the next question is the shape of the counts along it. The conjecture asserts that the sequence of even-rank coefficients of $$K_{P,q}$$ is unimodal, rising to one peak and falling. As with the centre-one quotient, the strengthening to strict log-concavity is false, so unimodality is the calibrated form. The even-rank sequence was unimodal throughout the tested forests.

### Conjecture 94: Hasse-forest breadth–orbit bound

The adjoint breadth $$b_A$$ is the largest rank of an adjoint map, the maximal dimension of an image $$[x,L_P]$$, and the maximal Kirillov rank $$b_K$$ is the largest coadjoint-orbit dimension. The conjecture bounds the orbit size by twice the breadth, $$b_K\le 2b_A$$, on Hasse forests. The hypothesis is essential: off the forest class the same inequality is false, failing fourteen times in reverification, while on forests it held everywhere. The bound links the element side and the functional side of the same bracket through the tree structure of the covers.

### Conjecture 95: Unitriangular Kirillov strict log-concavity

The chain on $$n$$ points gives the strictly upper triangular Lie algebra $$\mathrm{ut}_n(\mathbb F_q)$$, the extremal Hasse forest. For this algebra the conjecture upgrades the mere unimodality of Conjecture 93 to strict log-concavity, the condition $$a_i^2>a_{i-1}a_{i+1}$$ at every nontrivial interior index of the even-rank sequence. The relevant background is Marberg's character and orbit enumeration for the unitriangular group. Strict log-concavity was confirmed for $$\mathrm{ut}_4$$, $$\mathrm{ut}_5$$, and $$\mathrm{ut}_6$$ over $$\mathbb F_2$$, for $$\mathrm{ut}_4$$ and $$\mathrm{ut}_5$$ over $$\mathbb F_3$$, and for $$\mathrm{ut}_4$$ over $$\mathbb F_5$$.

### Conjecture 96: Adjoint–coadjoint incidence anticorrelation

The incidence variety $$I_L$$ consists of the pairs $$(x,f)$$ for which the functional $$f$$ annihilates the adjoint image $$[x,L]$$, the same variety whose two-way count proves the calibration identity. Sampling a pair uniformly from it gives a joint distribution of the two ranks $$\operatorname{rank}(\operatorname{ad}_x)$$ and $$\operatorname{rank}(B_f)$$, and the conjecture asserts these are negatively correlated for every nonabelian pattern Lie algebra, with zero covariance exactly in the abelian case where both ranks vanish. The mechanism is that a large adjoint image forces $$f$$ into a smaller space, holding the coadjoint rank down. Stronger conditional stochastic-order and conditional-mean versions are false, so the negative sign of the covariance is the surviving statement, confirmed negative on every nonabelian poset and zero on all sixteen abelian ones.
