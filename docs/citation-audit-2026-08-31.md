# Citation audit for the Part XXVII--XXVIII additions

Date: 31 August 2026

## Final status

**ALL CLEAR from two independent reviewers on the same frozen source
hashes.** The final shared bibliography contains 28 added records. Every one
is cited in both the full and blind manuscripts; the skeleton intentionally
omits the corresponding body citations while importing the same bibliography.

The frozen source hashes reviewed by both reviewers were:

- `paper/additional_bibliography.tex`:
  `665344808b9db2d726359fb5e5cbdb47acc72a534aa13cd05f9f0d9fccd4c476`;
- `paper/part_xxviii.tex`:
  `e79928f6014096b81bc17bfa10f2ce0d4bf3e7ecd4b3a0f25cfd94fc64b2906b`;
- `docs/index.md`:
  `ff011b4445ff59cdadb6a886b2b7ea5cbdd8d52045da6fc2166003ea2317eccb`.

The final review checked titles, author order and diacritics, years, venues,
volumes, issues, pages or article numbers, arXiv identifiers, DOI strings and
resolver targets, and the scope of every nearby claim. Twenty-five of the 28
records have a printed DOI; both reviewers confirmed all 25 resolver targets.

## Review protocol

Two reviewers received clean citation-audit assignments and worked
independently. Neither was asked to edit the files. Each pass required the
reviewer to end with exactly `ALL CLEAR` or `NOT CLEAR` and to identify every
material defect rather than merely sample records.

The audit took four effective passes:

1. **Initial adversarial pass.** Both reviewers withheld clearance and found
   incorrect or incomplete publication metadata, source-to-claim mismatches,
   and unused records.
2. **Corrected-tree pass.** The bibliography was centralized and the reported
   defects were repaired. A source-scope question about finite-field graph
   operations led to an explicit separation between arbitrary prime-power
   graph operations and the odd-prime local-Clifford correspondence.
3. **First frozen pass.** One reviewer found the remaining author-name defect
   `K. E. Tikhomirov`; the authoritative IEEE and arXiv records give
   `K. Tikhomirov`.
4. **Repaired frozen-final pass.** After correction and recompilation, both
   reviewers independently rechecked the new hashes and returned
   `ALL CLEAR`.

An objection was adopted only when the cited primary or publisher record
supported it. Early conflations of the Çineli--Ginzburg--Gürel Math. Z. paper,
the Claudet--Perdrix WG chapter, and the Li--Müller paper with unrelated works
were rejected after checking the corresponding publisher pages. A provisional
objection that `math/0702267` was binary-only was likewise retracted after the
primary text was inspected: its abstract and definitions explicitly work over
`F_q` for prime-power `q`.

## Material repairs

| Area | Repair |
|---|---|
| Shared variants | Replaced three drifting bibliography copies by `paper/additional_bibliography.tex`, imported by full, blind, and skeleton variants. |
| Çineli--Ginzburg--Gürel | Replaced preprint-only dating with the 2024 Math. Z. and J. Mod. Dyn. publication data and DOIs. |
| Nguyen--Oum | Corrected to European J. Combin. 90 (2020), article 103183, DOI 10.1016/j.ejc.2020.103183. |
| Li--Müller | Corrected authors and pagination to A. Li and T. Müller, Adv. Appl. Probab. 49(1) (2017), 49--60, DOI 10.1017/apr.2016.78. |
| Minimum degree up to LC | Recorded the 2012 Javelle--Mhalla--Perdrix and 2015 Cattanéo--Perdrix proceedings publications and their distinct DOIs. |
| Random linear codes | Recorded the 2022 IEEE publication of Hao--Huang--Livshyts--Tikhomirov and corrected the last author to K. Tikhomirov. |
| Claudet--Perdrix | Corrected to *Covering a graph with minimal local sets*, LNCS 14760 (2025), 136--150, DOI 10.1007/978-3-031-75409-8_10. |
| Hosoya extremality | Replaced a source that did not support the stated theorem by Huang--Shi--Xu (2018), whose theorem records the path/star extremals. |
| Finite-field graph states | Added an explicit additive-character definition and a self-contained Schmidt-rank proof for every prime power, including even characteristic. |
| Finite-field graph operations | Cited `math/0702267` for the two operations over arbitrary prime-power fields and `quant-ph/0610267` only for the odd-prime local-Clifford correspondence; cut-rank invariance is proved directly by row/column operations. |
| Unused records | Removed the three orphan keys `BerestyckiWong23`, `Cai26`, and `BahramgiriBeigi07`. |

## Final added-reference ledger

The authoritative locator in the last column is the DOI used in the paper,
or the arXiv record where no publication DOI is printed.

| Key | Final work | Authoritative locator |
|---|---|---|
| `CGGEntropy24` | Çineli--Ginzburg--Gürel, *Topological entropy of Hamiltonian diffeomorphisms* | [10.1007/s00209-024-03627-0](https://doi.org/10.1007/s00209-024-03627-0) |
| `CGGBarcode24` | Çineli--Ginzburg--Gürel, *On the growth of the Floer barcode* | [10.3934/jmd.2024007](https://doi.org/10.3934/jmd.2024007) |
| `Gong26` | Gong, *Persistent entropy of Floer persistence barcodes* | [10.48550/arXiv.2606.19071](https://doi.org/10.48550/arXiv.2606.19071) |
| `Bogenschutz93` | Bogenschütz, *Entropy, pressure, and a variational principle for random dynamical systems* | no DOI printed |
| `HeinEisertBriegel04` | Hein--Eisert--Briegel, *Multiparty entanglement in graph states* | [10.1103/PhysRevA.69.062311](https://doi.org/10.1103/PhysRevA.69.062311) |
| `Oum05` | Oum, *Rank-width and vertex-minors* | [10.1016/j.jctb.2005.03.003](https://doi.org/10.1016/j.jctb.2005.03.003) |
| `OumSeymour06` | Oum--Seymour, *Approximating clique-width and branch-width* | [10.1016/j.jctb.2005.10.006](https://doi.org/10.1016/j.jctb.2005.10.006) |
| `NguyenOum20` | Nguyen--Oum, *The average cut-rank of graphs* | [10.1016/j.ejc.2020.103183](https://doi.org/10.1016/j.ejc.2020.103183) |
| `LeeLeeOum12` | Lee--Lee--Oum, *Rank-width of random graphs* | [10.1002/jgt.20620](https://doi.org/10.1002/jgt.20620) |
| `DoErdeKang24` | Do--Erde--Kang, *A note on the width of sparse random graphs* | [10.1002/jgt.23081](https://doi.org/10.1002/jgt.23081) |
| `LiMuller17` | Li--Müller, *On the treewidth of random geometric graphs and percolated grids* | [10.1017/apr.2016.78](https://doi.org/10.1017/apr.2016.78) |
| `CGGSurvey26` | Çineli--Ginzburg--Gürel--Mazzucchelli, *Topics in symplectic dynamics: barcode entropy* | [10.48550/arXiv.2605.25965](https://doi.org/10.48550/arXiv.2605.25965) |
| `JavelleMhallaPerdrix12` | Javelle--Mhalla--Perdrix, *On the minimum degree up to local complementation* | [10.1007/978-3-642-34611-8_16](https://doi.org/10.1007/978-3-642-34611-8_16) |
| `CattaneoPerdrix15` | Cattanéo--Perdrix, *Minimum degree up to local complementation* | [10.1007/978-3-662-48971-0_23](https://doi.org/10.1007/978-3-662-48971-0_23) |
| `HaoEtAl22` | Hao--Huang--Livshyts--Tikhomirov, *Distribution of the minimum distance of random linear codes* | [10.1109/TIT.2022.3170341](https://doi.org/10.1109/TIT.2022.3170341) |
| `BurchardtDeJongVandre24` | Burchardt--de Jong--Vandré, *Algorithm to verify local equivalence of stabilizer states* | [10.48550/arXiv.2410.03961](https://doi.org/10.48550/arXiv.2410.03961) |
| `ClaudetPerdrix25` | Claudet--Perdrix, *Covering a graph with minimal local sets* | [10.1007/978-3-031-75409-8_10](https://doi.org/10.1007/978-3-031-75409-8_10) |
| `HuangShiXu18` | Huang--Shi--Xu, *The Hosoya index and the Merrifield--Simmons index* | [10.1007/s10910-018-0937-y](https://doi.org/10.1007/s10910-018-0937-y) |
| `PanXuYangZhou07` | Pan--Xu--Yang--Zhou, *Some graphs with minimum Hosoya index and maximum Merrifield--Simmons index* | no DOI printed |
| `YuLv07` | Yu--Lv, *The Merrifield--Simmons indices and Hosoya indices of trees with k pendant vertices* | [10.1007/s10910-006-9088-7](https://doi.org/10.1007/s10910-006-9088-7) |
| `Schwenk73` | Schwenk, *Almost all trees are cospectral* | no DOI printed |
| `Janson16` | Janson, *Asymptotic normality of fringe subtrees and additive functionals* | [10.1002/rsa.20568](https://doi.org/10.1002/rsa.20568) |
| `GhoshHangleiterHelsen25` | Ghosh--Hangleiter--Helsen, *Random regular graph states are complex at almost any depth* | [10.1103/52xz-3hpc](https://doi.org/10.1103/52xz-3hpc) |
| `Oum08` | Oum, *Rank-width is less than or equal to branch-width* | [10.1002/jgt.20280](https://doi.org/10.1002/jgt.20280) |
| `Jelinek10` | Jelínek, *The rank-width of the square grid* | [10.1016/j.dam.2009.02.007](https://doi.org/10.1016/j.dam.2009.02.007) |
| `BahramgiriBeigiEnumerating07` | Bahramgiri--Beigi, *Enumerating the classes of local equivalency in graphs* | [10.48550/arXiv.math/0702267](https://doi.org/10.48550/arXiv.math/0702267) |
| `BahramgiriBeigiNonbinary06` | Bahramgiri--Beigi, *Graph states under the action of local Clifford group in non-binary case* | [10.48550/arXiv.quant-ph/0610267](https://doi.org/10.48550/arXiv.quant-ph/0610267) |
| `AdcockEtAl20` | Adcock--Morley-Short--Dahlberg--Silverstone, *Mapping graph state orbits under local complementation* | [10.22331/q-2020-08-07-305](https://doi.org/10.22331/q-2020-08-07-305) |

## Mechanical and visual verification

The final include-aware citation scan reported:

| Variant | Distinct cited keys | Bibliography records | Undefined | Duplicate keys | Added keys used |
|---|---:|---:|---:|---:|---:|
| full | 419 | 421 | 0 | 0 | 28/28 |
| blind | 419 | 421 | 0 | 0 | 28/28 |
| skeleton | 189 | 311 | 0 | 0 | 0/28 (intentional body omission) |

Tectonic compiled all three PDFs successfully. The final logs contain no
undefined citations, undefined references, duplicate-key warnings, LaTeX
errors, or fatal errors. The resulting PDFs have 344, 344, and 141 pages.
The remaining overfull/underfull box warnings are typographic rather than
citation failures. Most predate this audit; the shared bibliography also
introduces one harmless underfull-box warning at its final entries.

Rendered-page inspection covered the revised finite-field definition and
proof, the full and blind reference pages, the corrected Tikhomirov record,
and the skeleton bibliography terminus. No clipping, overlap, missing glyph,
broken DOI underscore, or unreadable reference was found.

Finally, the scoped mathematical falsifiers were rerun after the source
changes:

- `verify/aq_hybrid_laws.py`: 7/7 checks passed;
- `verify/ar_random_barcode.py`: all 131,071 binary words through length 16
  passed, together with the seeded rate calibration;
- `verify/as_graph_state_cutrank.py`: all finite-field, distance, labelled-LC,
  tree-shape/extremal, reconstruction, small-width, and orbit calibrations
  passed.

These computations are sanity checks of the stated anchors, not proofs of the
conjectures. The admission and novelty limitations remain those recorded in
`docs/conjectures-392-409-admission-audit-2026-08-30.md` and
`docs/graph-state-cut-rank-audit-2026-08-30.md`.
