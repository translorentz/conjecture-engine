"""C19 second-order refinement -- singular-series dependence of first
occurrences of prime gaps.

The waiting-time model for a specific even gap g (rate per prime
~ S*(g) e^{-g/log t} at scale t, with S*(g) = prod_{p|g, p>2}
(p-1)/(p-2) the Hardy-Littlewood factor) predicts, on taking
logarithms of the first-passage condition, the normal-order refinement

    log p(g) = sqrt(g) + (1/2) log g - (1/2) log S*(g) + O(1):

smooth gaps (large S*(g)) should appear EARLIER by exactly half a log
of their tuple constant.  This script computes the full first-
occurrence table p(g) to X, forms the residual

    r(g) = log p(g) - sqrt(g) - (1/2) log g,

and regresses r(g) against log S*(g): the model predicts slope -1/2.
The liminf constant of C19 is unaffected (log S* = O(log log g)).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9
GMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 60
GMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 500

first = {}
prev = None
with Timer("sweep"):
    for lo, hi, seg in seg_sieve(X, seg_size=1 << 23):
        idx = np.nonzero(seg)[0] + lo
        if prev is not None and len(idx):
            g = int(idx[0]) - prev
            if g not in first:
                first[g] = prev
        gaps = np.diff(idx)
        for j in np.nonzero(gaps > 0)[0]:
            g = int(gaps[j])
            if g not in first:
                first[g] = int(idx[j])
        if len(idx):
            prev = int(idx[-1])


def Sstar(g):
    s = 1.0
    m = g
    p = 3
    while p * p <= m:
        if m % p == 0:
            s *= (p - 1) / (p - 2)
            while m % p == 0:
                m //= p
        p += 2
    if m > 2:
        s *= (m - 1) / (m - 2)
    return s


gs = np.array(sorted(g for g in first if GMIN <= g <= GMAX and g % 2 == 0))
r = np.array([math.log(first[int(g)]) - math.sqrt(g) - 0.5 * math.log(g) for g in gs])
lS = np.array([math.log(Sstar(int(g))) for g in gs])
# regress r on lS with an sqrt(g) trend removed via including sqrt(g) as covariate
A = np.column_stack([np.ones_like(r), np.sqrt(gs.astype(float)), lS])
coef, *_ = np.linalg.lstsq(A, r, rcond=None)
pred_slope = -0.5
rho = float(np.corrcoef(r - A[:, :2] @ coef[:2], lS)[0, 1])
print("gaps observed in [%d, %d]: %d" % (GMIN, GMAX, len(gs)))
print("regression r(g) ~ a + b sqrt(g) + c log S*(g):")
print("  a=%.3f  b=%.4f  c=%.3f   (model predicts c = -0.5)" % tuple(coef))
print("partial correlation(residual, log S*) = %.3f" % rho)
save_result("c19b", {"conjecture": "second-order S*(g) dependence of first occurrences: "
                                   "log p(g) = sqrt g + (1/2)log g - (1/2)log S*(g) + O(1)",
                     "X": X, "gmin": GMIN, "gmax": GMAX, "n_gaps": int(len(gs)),
                     "slope_logSstar": float(coef[2]), "pred_slope": pred_slope,
                     "intercept": float(coef[0]), "sqrtg_coef": float(coef[1]),
                     "partial_corr": rho})
