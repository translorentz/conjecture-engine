"""C16 -- Uniform quantitative de Polignac.

For every even d, pi_d(x) = #{p <= x-d : p, p+d both prime} should equal
S(d) * Li_2(x) with random-model (square-root) errors, *uniformly* in d.
Verification: all even d <= 2000 at x = 10^8; the normalized residuals
z_d = (obs - pred)/sqrt(pred) should look like N(0,1) noise with no trend.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 2000

with Timer("sieve"):
    P = sieve_bool(X)
LI2 = li_k(X, 2)

ds, obs, pred, zs = [], [], [], []
with Timer("pair counts"):
    for d in range(2, DMAX + 1, 2):
        c = int(np.count_nonzero(P[: X + 1 - d] & P[d:]))
        pr = twin_S(d) * LI2
        ds.append(d)
        obs.append(c)
        pred.append(pr)
        zs.append(zscore(c, pr))

zs = np.array(zs)
obs_a, pred_a = np.array(obs, dtype=float), np.array(pred)
corr = float(np.corrcoef(obs_a, pred_a)[0, 1])
slope = float(np.sum(obs_a * pred_a) / np.sum(pred_a * pred_a))
half = len(zs) // 2
print("d <= %d at x = %.0e" % (DMAX, X))
print("correlation(obs, pred)      = %.6f" % corr)
print("regression slope obs~pred   = %.6f" % slope)
print("mean z = %+.3f   sd z = %.3f   max|z| = %.2f (d=%d)"
      % (zs.mean(), zs.std(), np.abs(zs).max(), ds[int(np.abs(zs).argmax())]))
print("mean z first half %+.3f  second half %+.3f (drift check)"
      % (zs[:half].mean(), zs[half:].mean()))

worst = sorted(range(len(ds)), key=lambda i: -abs(zs[i]))[:5]
save_result("c16", {"conjecture": "pi_d(x) ~ S(d) Li2(x) uniformly in d",
                    "x": X, "dmax": DMAX, "correlation": corr, "slope": slope,
                    "z_mean": float(zs.mean()), "z_sd": float(zs.std()),
                    "z_max_abs": float(np.abs(zs).max()),
                    "drift": [float(zs[:half].mean()), float(zs[half:].mean())],
                    "worst": [{"d": ds[i], "obs": obs[i], "pred": round(pred[i], 1),
                               "z": round(float(zs[i]), 2)} for i in worst],
                    "sample": [{"d": ds[i], "obs": obs[i], "pred": round(pred[i], 1),
                                "z": round(float(zs[i]), 2)}
                               for i in range(0, len(ds), 100)]})
