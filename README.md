# Two hundred fifty-five conjectures in mathematics

This repository contains:

- **`paper/conjectures.pdf`** (`conjectures.tex`) — the full paper: two
  hundred fifty-five conjectures in thirteen parts, each with its mechanism,
  nearest literature boundary, first decisive theorem, failure mode, and
  computational verification. Part I (Conjectures 1–25) derives from the
  calibrated local–global random model of the primes; Part II (26–50)
  states five structural programmes, from connected prime-pattern fields
  to adelic factorization processes; Part III (51–56) crosses into
  discrepancy theory, graph limits, and entropy; Part IV (57–76) studies
  Rossmann's class-counting polynomial of graphical Lie algebras;
  Part V (77–96) the rank enumerators of pattern Lie algebras of finite
  posets; Part VI (97–116) the local structure of primes and arithmetic
  functions; Part VII (117–136) the topology of four canonical geometric
  families: Calabi–Yau complete intersections, Brieskorn–Pham links,
  moment-angle complexes, and torus mapping tori; Part VIII (137–156)
  shape laws for five enumerative arrays: Euler indices of hypersurfaces
  in products of projective spaces, Hilbert-scheme Betti profiles,
  cyclic-quotient age histograms, exterior torsion entropy, and
  matroidal Hochster tables; Part IX (157–176) spectra and filtrations
  of combinatorial geometries: graph-associahedron h-polynomials,
  age-filtered McKay complexes, lens-space sine-torsion sectors, and
  boundary-determinant entropy of simplicial spheres; Part X (177–196)
  flux cohomology and protected index laws: torus flux complexes with a
  prime torsion staircase, and chi_y-profile and signature laws for
  Calabi–Yau complete intersections; Part XI (197–216) spectral
  entropies and multibase carry fields: all-order Rényi entropy laws for
  the Laplacian and distance signless Laplacian density matrices of
  graphs, and cross-prime decoupling laws for the carry fields of
  central binomial coefficients; Part XII (217–236) subdivision
  spectra, spanning-tree correlation, and information dimension:
  factorial moment thresholds for barycentric refinement tails, the
  extremal theory of a spanning-tree total-correlation invariant, the
  inverse theory of the prime-field entropy-doubling floor, and
  dimension identities for random-free graphon entropy; Part XIII
  (237–255) flux torsion shape laws, quantum merge monotonicity for
  mirror maps and Gopakumar–Vafa invariants, Bridgeland wall and
  sharp-constant laws, and effective convergence certificates for
  Calabi–Yau metrics, connections, spectra, and Yukawa couplings. Thirteen conjectures
  (63, 71, 87, 90, 107, 135, 153, 154, 155, 156, 183, 205, 229) have since been refuted and are recorded in
  place as resolved false, with their counterexamples or the refuting
  theorem. Twelve conjectures (110, 111, 112, 115, 117, 118, 125,
  151, 152, 182, 195, and 240) have since been proved
  and are recorded in place as resolved true, with their proofs.
- **`paper/conjectures_blind.pdf`** (`conjectures_blind.tex`) — the
  anonymous version of the paper.
- **`paper/conjectures_skeleton.pdf`** (`conjectures_skeleton.tex`) — the
  bare statements, without significance discussions or verification
  reports.
- **[Web version](https://translorentz.github.io/conjecture-engine/)** — the
  paper as a browsable page (`docs/`), with plain-language explanations
  of every conjecture.
- **`engine/`, `verify/`, `adversarial/`, `run_all.py`** — the verification
  programs. `python run_all.py` regenerates every number in Part I;
  machine-readable outputs are in `results/`. The later parts have their
  own reproduction scripts in `verify/`: `u_*.py` (Part IV), `v_*.py`
  (Part V), `w_local_structure.py` (Part VI), `x_topology.py` (Part VII), `wx_shock_landau.py` and `ehrhart_cov_gamma.py` (the shock forcing, Landau-floor, Ehrhart-scaling, covariance, and coverage resolutions of Parts VI--VII and IX--X), `y_shape_laws.py` (Part VIII),
  `z_spectra_filtrations.py` (Part IX), `aa_flux_indices.py` (Part X), `ab_entropy_carry.py` (Part XI), `ac_subdivision_ust_cyclic.py` (Part XII), `ad_flux_torsion.py` and `ad_mirror_merge.py` (Part XIII), and `t5_*.py` (Part III),
  each implemented independently of the primary scans.

Primality below 3.3×10²⁴ is decided deterministically (fixed-base
Miller–Rabin); larger integers are classified by Baillie–PSW and the
corresponding counts are labelled probable-prime counts in the paper.
