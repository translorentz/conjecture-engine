"""C24 -- Hardy-Littlewood 'Conjecture F' family coherence.

For odd A, let Q_A(N) = #{n <= N : n^2+n+A prime} and C(A) its
Bateman-Horn constant.  Conjecture: Q_A(N) = C(A)*I_A(N)*(1 + o(1))
*uniformly* over the family, so the computed constants predict the
entire ordering (Euler's A=41 included) and the residuals are noise.
Verification: all odd A in [1, 199], N = 10^6; report per-A ratios,
correlation, and the ranking agreement.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**6
AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 199

rows = []
with Timer("family scan"):
    for A in range(1, AMAX + 1, 2):
        polys = [[A, 1, 1]]
        C, _ = bateman_horn_constant(polys, pmax=1_000_000)  # truncation drifts ~1e-3; cf. Cohen high-precision values
        res = count_poly_primes(polys, N, presieve_to=50_000, checkpoints=(N,))
        obs = res["at"][N]
        pred = C * bh_integral(polys, N)
        rows.append({"A": A, "C": round(C, 5), "obs": obs,
                     "pred": round(pred, 1), "ratio": round(obs / pred, 4),
                     "z": round(zscore(obs, pred), 2)})

ratios = np.array([r["ratio"] for r in rows])
zs = np.array([r["z"] for r in rows])
obs_v = np.array([r["obs"] for r in rows], dtype=float)
pred_v = np.array([r["pred"] for r in rows])
corr = float(np.corrcoef(obs_v, pred_v)[0, 1])
rank_corr = float(np.corrcoef(np.argsort(np.argsort(obs_v)),
                              np.argsort(np.argsort(pred_v)))[0, 1])
print("family n^2+n+A, odd A <= %d at N=%.0e" % (AMAX, N))
print("mean ratio %.4f  sd %.4f  max|z| %.2f" %
      (ratios.mean(), ratios.std(), np.abs(zs).max()))
print("correlation obs~pred: %.5f   rank correlation: %.5f" % (corr, rank_corr))
top = sorted(rows, key=lambda r: -r["C"])[:5]
print("largest constants:", [(r["A"], r["C"]) for r in top])
print("A=41:", [r for r in rows if r["A"] == 41])

save_result("c24", {"conjecture": "Q_A(N) ~ C(A) I_A(N) uniformly over odd A",
                    "N": N, "amax": AMAX,
                    "mean_ratio": float(ratios.mean()), "sd_ratio": float(ratios.std()),
                    "max_abs_z": float(np.abs(zs).max()),
                    "correlation": corr, "rank_correlation": rank_corr,
                    "rows": rows})
