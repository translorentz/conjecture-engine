"""C01 (family lift) -- uniform quadratic de Polignac.

For every admissible even shift d, the pair (n^2+1, n^2+1+d) is
simultaneously prime infinitely often with Bateman-Horn count
C(d)*I_d(N), UNIFORMLY over admissible d <= (log N)^B: the whole
profile of constants must be matched at once.  d = 2 is the classical
quadratic twin pair (formerly the whole conjecture in this slot).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**6
DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300

rows = []
with Timer("family scan"):
    for d in range(2, DMAX + 1, 2):
        polys = [[1, 0, 1], [1 + d, 0, 1]]
        try:
            C, _ = bateman_horn_constant(polys, pmax=100_000)
        except ValueError:
            continue  # inadmissible shift
        res = count_poly_primes(polys, N, presieve_to=30_000, checkpoints=(N,))
        obs = res["at"][N]
        pred = C * bh_integral(polys, N)
        rows.append({"d": d, "C": round(C, 4), "obs": obs,
                     "pred": round(pred, 1), "z": round(zscore(obs, pred), 2)})

zs = np.array([r["z"] for r in rows])
obs_v = np.array([r["obs"] for r in rows], dtype=float)
pred_v = np.array([r["pred"] for r in rows])
corr = float(np.corrcoef(obs_v, pred_v)[0, 1])
slope = float(np.sum(obs_v * pred_v) / np.sum(pred_v * pred_v))
print("admissible shifts d <= %d: %d" % (DMAX, len(rows)))
print("correlation obs~pred %.5f  slope %.4f  mean z %+.3f  sd z %.3f  max|z| %.2f"
      % (corr, slope, zs.mean(), zs.std(), np.abs(zs).max()))
save_result("c01", {"conjecture": "uniform quadratic de Polignac: (n^2+1, n^2+1+d) ~ C(d) I(N) "
                                  "uniformly over admissible even d",
                    "N": N, "dmax": DMAX, "n_admissible": len(rows),
                    "correlation": corr, "slope": slope,
                    "z_mean": float(zs.mean()), "z_sd": float(zs.std()),
                    "z_max_abs": float(np.abs(zs).max()),
                    "sample": rows[::10], "d2_row": rows[0]})
