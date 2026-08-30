# Part XXVIII admission audit: graph-state cut-rank laws

Date: 30 August 2026  
Decision: admit 15 conjectures as Conjectures 396–410 after three independent-review iterations.

## Standard and scope

The audit required each admitted statement to satisfy five tests:

1. **Novelty:** no theorem or materially equivalent conjecture was found in the project or the nearest literature.
2. **Mathematical interest:** the claim concerns a canonical invariant or ensemble and is not merely an isolated numerical pattern.
3. **Sound mechanism:** the proposed scale, constant, or extremizer follows from explicit established inputs, with the genuinely missing implication identified.
4. **Sanity checking:** every accessible finite consequence was checked exactly or by seeded computation, and stronger nearby statements were deliberately tested for failure.
5. **Consequence:** a proof would change the understanding of graph-state entanglement, stabilizer codes, matching theory, reconstruction, percolation, or random width parameters.

The common invariant is

\[
\rho_G(S)=\operatorname{rank}_{\mathbb F_2}A_G[S,V\setminus S],
\qquad
Z_G(x,y)=\sum_{S\subseteq V}x^{|S|}y^{\rho_G(S)}.
\]

The graph-state Schmidt-rank identity, local-complementation invariance of the labelled cut-rank function, rank-width theory, and existing order-of-magnitude results for random graphs were treated as baselines rather than discoveries.

## Iteration ledger

| Iteration | Reviewer disposition | Material objections | Resolution |
|---|---|---|---|
| 1 | 6 accept, 6 revise, 3 reject | A coarse $Z_G$ completeness law had no sound generic mechanism; the weakly-supercritical kernel constant must use branch-width rather than rank-width; an asserted vertex-minor constant lacked a matching upper bound; forest ultra-log-concavity was false. | Removed the coarse invariant claim; corrected the kernel parameter and transfer target; removed the unsupported constant; weakened forest shape to ordinary log-concavity. |
| 1, independent cross-check | Additional boundary objections | A forest Hurwitz law needed a forest-specific mechanism rather than analogy with Part VII; a separate LU–LC item was logically redundant; the claimed ultra-log-concavity failed on a 13-vertex tree. | Added the rooted-tree matching recursion and star root-margin control; folded LU–LC into the consequence of labelled cut-rank rigidity; recorded the exact ULC counterexample. |
| 2 | 7 accept, 6 revise, 2 reject | Universal tree reconstruction was false at order 15; the replacement vertex-minor threshold law was already Conjecture 5.3 of Ascoli–Frederickson–Frederickson–McFarland–Post (2026); transfer and phase-boundary wording required precision. | Replaced universal reconstruction by a typical-tree law and recorded the first collision; removed the literature duplicate entirely; added an LC-orbit entropy law; formalized the transfer and excluded grid criticality. |
| 3 | 15 accept, 3 minor formal edits | Make the repaired multigraph deterministic, state $p\in[0,1]\setminus\{1/2\}$, and specify that “generic stabilizer triviality” concerns extra non-Pauli LC automorphisms. | All three edits were made. The reviewer found no remaining substantive objection. |

## Rejected or materially weakened claims

### Coarse entanglement enumerator as a generic LC invariant

Rejected. At order seven, exact enumeration already merges three distinct labelled local-complementation classes with the same coarse $Z_G(x,y)$ signature. A generic theorem might still exist, but the candidate supplied neither a mechanism that suppresses these fibres nor evidence at a scale capable of distinguishing polynomially rare from exponentially rare collisions.

### Forest ultra-log-concavity

Rejected as false. The 13-vertex graph6 tree

`LqD?I?@O??g??@`

has percolated-matching profile

`(1, 75, 432, 1060, 1360, 912, 256)`,

which violates ultra-log-concavity. Ordinary log-concavity survives and is Conjecture 401. Real-rootedness is also false: a seven-vertex tree has profile `(1, 13, 30, 20)` with nonreal zeros.

### Universal reconstruction of trees from $Z_T$

Rejected as false. The first collision is the nonisomorphic order-15 pair

`NpCa?C@?a??@?@O???G`  
`NpCc?D??G?_@O???g??`

An independent exhaustive scan of all 7,741 unlabelled 15-vertex trees found exactly one collision class, the displayed pair, and none through order 14. This evidence supports the admitted *typical* reconstruction law (Conjecture 405), not universal reconstruction.

### Vertex-minor threshold-density law

Rejected for lack of novelty. The proposed revision was materially Conjecture 5.3 in Ascoli, Frederickson, Frederickson, McFarland, and Post, *Vertex-minors and Erdős–Hajnal* (2026). It is not included or renumbered.

### Separate generic LU–LC law

Removed as logically redundant. Local-unitary equivalence preserves all bipartite Schmidt ranks. Therefore typical completeness of the labelled cut-rank function up to local complementation (Conjecture 399) would already imply generic LU–LC.

## Admitted conjectures

| No. | Conjecture | Novel content | Consequence if proved |
|---:|---|---|---|
| 396 | Quenched balanced-cut nullity universality | Self-averaging of one graph state’s overlapping cuts to the rectangular finite-field nullity law | A quenched entanglement-spectrum law for random qudit graph states |
| 397 | Dependence-sensitive extreme balanced-cut defect | Exact leading constant for the largest nullity across exponentially many dependent cuts | Extreme multipartite entanglement and worst-cut tensor-network complexity |
| 398 | Poisson law for random graph-state distance | Poisson/Gumbel-scale distance law for the symmetric graph-code generator | Sharp finite-blocklength random stabilizer-code performance |
| 399 | Typical rigidity of labelled cut rank | Generic completeness of all bipartite entropies up to labelled LC | Generic LU–LC and entanglement-based graph-state identification |
| 400 | Positive-rank-tail log-concavity | A shape law for cut-rank multiplicities with the exact necessary boundary exclusion | New negative-dependence/injection structure for graph cuts |
| 401 | Full log-concavity for percolated forests | Log-concavity of edge subsets counted by induced maximum matching | A bridge between matching theory and forest graph-state entanglement |
| 402 | Hurwitz stability of the percolated-matching polynomial | Left-half-plane stability for a new maximum-matching enumerator | A stable-polynomial structure generated by rooted-tree recursion |
| 403 | Path–star stochastic extremality | Full stochastic, not only mean, extremality under bond noise | Sharp noisy-entanglement extremizers among trees |
| 404 | Fixed-leaf broom minimum | Leaf-constrained stochastic matching extremality | A new constrained extremal theorem for percolated trees |
| 405 | Typical tree reconstruction from $Z_T$ | Typical completeness despite explicit universal collisions | Efficient average-case reconstruction from bipartite entanglement data |
| 406 | Random-regular rank-width density | Existence of an extensive width constant for each fixed degree | A tensor-network complexity density for regular graph states |
| 407 | Cubic branch-width density and kernel transfer | A robust deterministic transfer plus the weakly-supercritical constant | Exact leading rank-width at the sparse phase boundary |
| 408 | Off-critical grid rank-width surface tension | Existence of a deterministic linear coefficient away from $p_c$ | A percolation surface tension for graph-state simulation complexity |
| 409 | LC-orbit entropy saturation | Typical saturation of the universal $3^n$ orbit upper bound | Exponential classification and compilation complexity of random graph states |
| 410 | Sparse Erdős–Rényi rank-width density curve | A deterministic extensive curve at every fixed mean degree | A sparse graph-state complexity free energy and its phase transition |

## Exact and seeded sanity checks

- **Finite-field calibration:** the exact rectangular matrix rank count was normalized and checked against exhaustive small matrices.
- **Labelled cut-rank rigidity:** all labelled graphs through six vertices were partitioned both by the full cut-rank function and by local-complementation orbit; the partitions agree, with 760 fibres at order six.
- **Positive-tail log-concavity:** passed all 1,252 graph-atlas graphs on at most seven vertices and 8,500 seeded random graphs of orders 8–15. The full-profile and fixed-$|S|$ strengthenings fail.
- **Forest log-concavity:** passed every unlabelled tree through 13 vertices (2,287 trees); an independent implementation extended this through 18.
- **Forest Hurwitz stability:** passed every tree through 18 vertices. The star identity $H_{S_n}(z)=1+(2^{n-1}-1)z$ rules out a uniform root-modulus margin.
- **Tree extremality:** coefficientwise polynomial comparison passed all trees through 15 vertices for both the path–star law and every fixed-leaf broom class, checking all $p\in(0,1)$ simultaneously.
- **Tree reconstruction:** exhaustive through 15 vertices, including exact verification of the unique collision class above.
- **Small cubic rank-width:** exact decomposition dynamic programming gave sample means $2.45,2.60,2.90,3.00$ at orders $8,10,12,14$; this is scale calibration only.
- **LC-orbit entropy:** seeded exact orbit enumeration gave mean $n^{-1}\log_2|\mathcal O_{LC}|=1.285,1.320,1.376,1.383$ at orders $7,8,9,10$, with sample maxima up to $1.471$, below the limiting target $\log_2 3=1.585\ldots$.

## Novelty boundary

The closest established results determine the graph-state cut entropy for a fixed bipartition, invariance under local complementation, rank-width order of magnitude in dense and sparse random graphs, average cut rank, small local-complementation orbit maps, and linear treewidth of supercritical percolated grids. None of those results supplies a quenched cut distribution, an extreme-cut constant, the forest maximum-matching shape laws, the typical reconstruction theorem, a width density constant, or a typical LC-orbit entropy. The project-wide search also found no previous conjecture materially equivalent to the fifteen admitted statements.

The verifier is [`verify/as_graph_state_cutrank.py`](../verify/as_graph_state_cutrank.py). It is a falsification suite, not a proof of any asymptotic statement.
