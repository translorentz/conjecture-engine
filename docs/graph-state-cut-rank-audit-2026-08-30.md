# Admission audit: fifteen graph-state cut-rank conjectures

Date: 30 August 2026
Final numbering: Conjectures 395–409

## Decision

Fifteen conjectures are admitted after repeated independent review and
revision. They form one connected programme around

\[
\rho_G(S)=\operatorname{rank}_{\mathbb F_2}A_G[S,V\setminus S],
\qquad
Z_G(x,y)=\sum_{S\subseteq V}x^{|S|}y^{\rho_G(S)}.
\]

The graph-state Schmidt-rank identity, local-complementation invariance,
Oum–Seymour rank-width theory, and known order-of-magnitude results for
random graphs are treated as calibrations, not discoveries.

No theorem or materially equivalent conjecture was located in the project or
the nearest literature searched as of the audit date. This is a rigorous
novelty search, but—as with any literature search—not a logical guarantee
about every unpublished source.

## Review protocol

Each iteration was frozen and sent to an independent reviewer. A statement
was revised, replaced, or removed when an objection exposed a counterexample,
a duplicate, an ambiguous quantifier, a wrong citation, an unsupported
consequence, or a mechanism that did not reach the claim.

| Iteration | Independent finding | Resolution before the next review |
|---|---|---|
| 1. Broad candidate slate | A coarse \(Z_G\)-completeness claim lacked a generic mechanism; the weakly supercritical constant used the wrong width; a vertex-minor constant had no upper bound; forest ultra-log-concavity was false. | Removed the coarse claim and unsupported constant; changed the kernel parameter to branch-width; weakened the forest shape law to ordinary log-concavity and kept the counterexample. |
| 2. Replacement slate | Universal tree reconstruction was false at order 15; a replacement vertex-minor threshold was already present in Ascoli et al. (2026); a separate LU–LC conjecture was redundant. | Replaced universal reconstruction by a typical-tree law; removed the published duplicate; made generic LU–LC only a consequence of labelled cut-rank rigidity. |
| 3. Formal pass | The cubic-kernel repair law, grid parameter range, and LC-stabilizer wording had ambiguous quantifiers. | Restricted cubic size to even \(N\), made repairs conditional and uniform, used one-vertex sums for tree attachments, excluded grid criticality, and removed the unsupported algorithmic consequence. |
| 4. Forest and width re-audit | The star bound is elementary; ordinary Hosoya extremality for paths, stars, and fixed-leaf brooms is classical; finite uniqueness does not defeat rooted-limb substitution; the Oum, Jelínek, and Bahramgiri–Beigi boundaries were miscited; several verifier claims exceeded its actual scope. | Narrowed novelty to stochastic domination; added the Schwenk/Janson rooted-limb obstruction; corrected all three literature boundaries; separated extended reviewer computations from checked-in defaults; stated explicitly which asymptotic width laws have no direct finite test. |
| 5. Cut-rank and coding re-audit | Full log-concavity fails already at rank one; the \(q\)-ensemble and additive-code distance needed exact conventions; labelled and unlabelled rigidity evidence had been conflated. | Began the shape law at rank two; deposited a 13-vertex exact counterexample; made zero edge labels and the \(\mathbb F_q\) Pauli convention explicit; distinguished labelled verification from unlabelled census data. |
| 6. Source-slate cross-check | The fifteen new statements remained distinct from the ten attached candidates and from Conjectures 1–394. | Preserved the fifteen-item count; source candidate 10 instead strengthens Conjecture 392 and source candidate 3 becomes 394. |
| 7. Frozen-text holistic audit | A fresh reviewer challenged every statement for quantifiers, edge cases, prior-art boundaries, anchor accuracy, evidentiary reach, and consequence. | All fifteen received ACCEPT. The reviewer found no material defect and retained only the already disclosed cautions about modest evidence for 398, 404, and 408 and the absence of direct finite tests for 406, 407, and 409. |

## Admitted statements

| No. | Statement | Novel content | Main sanity pressure |
|---:|---|---|---|
| 395 | Quenched balanced-cut nullity universality | Self-averaging over all balanced cuts of one dense random \(q\)-level graph state to the rectangular finite-field nullity law | Exact rectangular rank count; fixed-cut marginal is known exactly |
| 396 | Dependence-sensitive extreme balanced-cut defect | Leading constant for the maximum nullity among exponentially many overlapping cuts | Exact tail \(q^{-d(d+s)+O_q(1)}\) and first-moment location; dependence is explicitly the unresolved lower bound |
| 397 | Poisson law for random graph-state distance | Poisson finite-length law for the symmetric graph-state additive-code ensemble | Two exact formulas for \(\Lambda_n(\ell)\) agree through \(n=20\); random-linear-code theorem does not cover symmetric generators |
| 398 | Typical rigidity of the labelled cut-rank function | Generic completeness of every labelled cut rank up to labelled local complementation | Exact fibre/orbit agreement for all labelled graphs through six vertices; universal unlabelled completeness is known false |
| 399 | Positive-rank-tail log-concavity | Log-concavity only from rank two onward, the strongest version surviving falsification | All 1,252 nonempty graph-atlas graphs pass; explicit connected 13-vertex rank-one failure |
| 400 | Full log-concavity for percolated forests | Shape law for edge subsets counted by the maximum matching they induce | Exact rooted recurrence; all unlabelled trees through order 20 in extended review; ULC and real-rooted strengthenings refuted |
| 401 | Hurwitz stability of the percolated-matching polynomial | Left-half-plane stability for a nonclassical maximum-matching enumerator | Exact Routh tests through order 20 in extended review; path and structured-family stress tests; star roots approach zero |
| 402 | Path–star stochastic extremality under bond noise | All-threshold stochastic path maximum; the star minimum is retained as an elementary sharp boundary | Exact Bernstein-coefficient comparison through order 17; ordinary Hosoya extremality is cited as known |
| 403 | Fixed-leaf broom minimum | Stochastic, rather than total-Hosoya, minimization under a leaf constraint | Exact coefficientwise comparison through order 17; classical fixed-leaf Hosoya minimization is cited |
| 404 | Typical tree reconstruction from \(Z_T\) | Typical identifiability despite explicit universal collisions | Unique collision at order 15; no unrooted collision through order 18 or rooted transfer collision through order 16 in extended review |
| 405 | Rank-width density of random regular graph states | Existence of a deterministic extensive constant for each fixed degree | Linear lower/upper scale is known; checked-in exact DP samples only small cubic graphs and is labelled accordingly |
| 406 | Cubic branch-width density and kernel transfer | A branch-width density plus a uniform deterministic incidence/subdivision transfer yielding the \(4/3\) weakly-supercritical constant | Oum’s exact incidence boundary; even-\(N\), repair, subdivision, and attachment quantifiers adversarially checked |
| 407 | Rank-width surface tension for off-critical percolated grids | Deterministic linear coefficient away from \(p_c\) | Subcritical component bound, Jelínek endpoint \(\operatorname{rw}(Q_L)=L-1\), and an explicit missing balanced-crossing step above criticality |
| 408 | Saturation of local-complementation orbit entropy | Typical exponent \(\log_2 3\), requiring both many Eulerian vectors and subexponential isotropic index | Exact seeded orbits at orders 7–9; numerator and denominator mechanisms stated separately |
| 409 | Sparse Erdős–Rényi rank-width density curve | A deterministic extensive curve for every fixed mean degree | Known zero/positive phases fix the sign; no direct finite test is claimed for existence of the limit |

## Exact negative controls

### Rank-one log-concavity is false

The connected graph

\`LG??XrL?[A?KCW\`

has vertices \(0,\ldots,12\), edges

\[
\begin{aligned}
&(0,8),(0,10),(1,2),(1,8),(2,7),(3,7),(3,12),(4,6),\\
&(4,7),(4,8),(5,6),(5,8),(7,8),(7,9),(7,10),(7,11),\\
&(7,12),(8,9),(8,11),(8,12),
\end{aligned}
\]

and exact cut-rank profile

\[
(c_0,\ldots,c_6)=(2,28,410,1896,3296,2208,352).
\]

Thus \(c_1^2=784<820=c_0c_2\). Conjecture 399 deliberately starts at
rank two.

### Forest ultra-log-concavity and real-rootedness are false

The graph6 tree

\`LqD?I?@O??g??@\`

has profile

\[
(1,75,432,1060,1360,912,256),
\]

which is not ultra-log-concave. A seven-vertex tree has profile

\[
(1,13,30,20)
\]

with nonreal zeros. Conjectures 400 and 401 assert only the ordinary
log-concavity and Hurwitz properties that survived these stronger tests.

### Universal tree reconstruction is false

The nonisomorphic order-15 graph6 trees are:

- \`NpCa?C@?a??@?@O???G\`
- \`NpCc?D??G?_@O???g??\`

have the same \(Z_T(x,y)\). This is why Conjecture 404 is probabilistic. A
proof must confront a stronger possible obstruction: nonisomorphic rooted
limbs with identical transfer data could be substituted into arbitrary hosts,
and standard fringe-subtree laws would then make collisions typical.

## Literature boundaries that changed the statements

- Javelle–Mhalla–Perdrix and Cattanéo–Perdrix establish the minimum-degree-up-
  to-local-complementation/code-distance boundary, but not Conjecture 397's
  Poisson law.
- Csikvári and the classical Hosoya literature settle ordinary path/star
  extremality; Pan–Xu–Yang–Zhou and Yu–Lv cover the fixed-leaf minimum. The
  new content of 402–403 is stochastic domination after percolation.
- Ghosh–Hangleiter–Helsen prove average-case complexity results for random
  regular graph states, not a normalized rank-width limit.
- Oum relates branch-width to rank-width of incidence graphs up to an
  additive constant; the robustness under sparse unreplaced edges, repairs,
  repeated subdivision, and one-vertex tree sums is the conjectural part of
  406.
- Jelínek gives the exact square-grid endpoint, not the off-critical random
  surface-tension limit of 407.
- Bahramgiri–Beigi express binary LC-orbit size as
  \(\varepsilon(L)/\lambda(L)\). Conjecture 408 therefore requires both
  \(\varepsilon(L)=3^{n-o(n)}\) and \(\lambda(L)=2^{o(n)}\); generic absence
  of automorphisms alone is insufficient.
- Lee–Lee–Oum and Do–Erde–Kang establish the qualitative rank-width phases
  used by 409, not the density limit.

## Reproducible checked-in suite

Run

\`PYTHONPATH=<environment containing networkx> python verify/as_graph_state_cutrank.py\`.

The current default suite reports:

- exact \(3\times4\) binary matrix rank counts;
- the exact Conjecture 397 mean identity through \(n=20\);
- all labelled cut-rank fibres versus LC orbits through \(n=6\), including
  760 fibres at order six;
- all 1,252 nonempty graph-atlas graphs for the positive-rank tail and the
  exact 13-vertex negative control;
- 985 unlabelled trees through order 12 for log-concavity and a numerical
  Hurwitz scan;
- 434 unlabelled trees through order 11 for coefficientwise stochastic
  extremality;
- the exact order-15 \(Z_T\) collision;
- exact rank-width on a small seeded cubic sample;
- exact seeded LC-orbit sizes at orders 7–9.

An independent extended computation—not the checked-in default—reached
order 20 for forest log-concavity and exact Routh conditions, order 17 for
the two stochastic extremal laws, order 18 for unrooted reconstruction
collisions, and order 16 for rooted transfer collisions.

There is no direct finite experiment for Conjectures 406, 407, or 409, and
the cubic experiment for 405 covers only \(d=3\). The suite is a falsifier,
not a proof of any asymptotic statement.
