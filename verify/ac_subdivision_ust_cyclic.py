#!/usr/bin/env python3
"""Part XII certification driver (Conjectures 217-236).

Runs the four independent Part XII verifiers, which share no code with the
deposited bundle:

  ac_ust_correlation.py      spanning-tree total correlation (217+5 .. 226):
                             closed formulas vs direct computation, exhaustive
                             atlas through n=7, multipartite partitions through
                             n=45, theta-graph and structured bridgeless sweeps,
                             split/bipartite adversaries, family asymptotics.
  ac_subdivision_spectra.py  barycentric subdivision (217-221): degree and
                             spectral moments from three starting complexes,
                             2D and 3D Hodge maxima, shallow tail counts.
  ac_cyclic_entropy.py       prime-cyclic entropy (227-231): doubling floor,
                             two-bump control, fixed-m floors with adversarial
                             search, heat-kernel wrap crossover, uniform
                             pre-wrap monotonicity at p = 2,000,003.
  ac_threshold_graphon.py    exact threshold-graphon entropies through n=7,
                             the negative control of the second-order
                             programme (Proposition, Conjecture 234).

Usage: python3 ac_subdivision_ust_cyclic.py [quick|all]
  quick: formulas+atlas, degree moments, doubling+m-copy+wrap, graphon (~2 min)
  all:   everything, including partitions to n=45 and p=2e6 monotonicity (~6 min)
"""
import os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
QUICK = [("ac_ust_correlation.py", ["a"]),
         ("ac_subdivision_spectra.py", ["deg"]),
         ("ac_cyclic_entropy.py", ["a"]), ("ac_cyclic_entropy.py", ["b"]),
         ("ac_cyclic_entropy.py", ["c"]),
         ("ac_threshold_graphon.py", [])]
FULL = [("ac_ust_correlation.py", [m]) for m in "abcd"] + \
       [("ac_subdivision_spectra.py", [m]) for m in ("deg", "spec", "hodge")] + \
       [("ac_cyclic_entropy.py", [m]) for m in "abcd"] + \
       [("ac_threshold_graphon.py", [])]

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "quick"
    t0 = time.time()
    for script, args in (FULL if which == "all" else QUICK):
        print(f"=== {script} {' '.join(args)}", flush=True)
        r = subprocess.run([sys.executable, os.path.join(HERE, script)] + args)
        if r.returncode != 0:
            sys.exit(f"FAILED: {script} {args}")
    print(f"Part XII certification complete in {time.time()-t0:.0f}s")
