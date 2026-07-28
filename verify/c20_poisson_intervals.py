"""C20 -- Primes in microscopic intervals: Poisson limit with an explicit
second-order variance deficit.

Windows of length h = lambda*log x near x.  Gallagher: counts -> Poisson(lambda)
as x -> infty.  At finite x the pair-correlation average
sum_{d<=h} S(d)(h-d) = h^2/2 - (h/2)(log h + gamma + log 2pi - 1) + o(h)
(Montgomery) forces a variance deficit.  Conjecture:
    Var/mean = 1 - (log h + gamma + log 2pi - 1)/log x + O(1/log^2 x),
uniformly for fixed lambda.  The naive Poisson model (Var/mean = 1) is
*refuted* by the data; this corrected version is the Goldilocks statement.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X0 = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9
WIDTH = int(float(sys.argv[2])) if len(sys.argv) > 2 else 2 * 10**8
CDEF = EULER_GAMMA + math.log(2 * math.pi) - 1

with Timer("collect primes"):
    pos = []
    for lo, hi, seg in seg_sieve(X0 + WIDTH, seg_size=1 << 24, start=X0):
        pos.append(np.nonzero(seg)[0].astype(np.int64) + lo)
    pos = np.concatenate(pos)
print("primes in [%.1e, %.1e]: %d" % (X0, X0 + WIDTH, len(pos)))

logx = math.log(X0)
out = {}
rows = []
for lam in (0.5, 1.0, 2.0, 4.0):
    h = lam * logx
    edges = np.arange(X0, X0 + WIDTH, h)
    counts, _ = np.histogram(pos, bins=edges)
    mean, var = float(counts.mean()), float(counts.var())
    ratio = var / mean
    pred = 1 - (math.log(h) + CDEF) / logx
    zr = (ratio - pred) / math.sqrt(2.0 / len(counts))  # rough normal scale
    rows.append({"lambda": lam, "windows": len(counts), "mean": round(mean, 4),
                 "var": round(var, 4), "var_over_mean": round(ratio, 4),
                 "predicted": round(pred, 4), "naive_poisson": 1.0,
                 "z_vs_pred": round(zr, 2)})
    print("lambda=%.1f  mean=%.4f  Var/mean=%.4f  predicted=%.4f  naive=1  z=%+.1f"
          % (lam, mean, ratio, pred, zr))
    # distribution snapshot for lambda=1
    if lam == 1.0:
        kmax = int(counts.max())
        obsh = np.bincount(counts, minlength=kmax + 1)
        pk = [math.exp(-lam) * lam ** k / math.factorial(k) for k in range(kmax + 1)]
        out["hist_lambda1"] = {"obs": obsh.tolist(),
                               "poisson_exp": [round(p * len(counts), 1) for p in pk]}

save_result("c20", {"conjecture": "Var/mean = 1 - (log h + gamma + log 2pi - 1)/log x",
                    "x0": X0, "width": WIDTH, "second_order_constant": CDEF,
                    "table": rows, **out})
