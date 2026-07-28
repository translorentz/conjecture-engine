"""C16 upgrade -- the derived covariance kernel of the de Polignac profile.

The residuals z_d of pair counts share primes: two pairs (n, n+d) and
(m, m+d') overlapping in one prime give triple configurations whose
Hardy-Littlewood constants determine the covariance

  Cov(pi_d, pi_d') ~ [ C3(0,d,d') + C3(0,d',d+d') + C3(0,d,d+d')
                       + C3(0,d-d',d) (d>d') ] * Li_3(x)   (d != d'),

so the correlation kernel is

  rho(d,d') ~ [sum of C3's] * Li_3(x) / ( sqrt(S(d) S(d')) * Li_2(x) ).

The common-mode term Var(zbar) = avg_{d,d'} rho then depresses the
observed profile variance below 1.  This script evaluates the kernel
numerically (all pairs d,d' <= DS) and compares the predicted
common-mode with the observed profile sd (~0.52 at x = 10^8).
Diagonal (4-tuple) deficits are NOT included -- stated as the open
residual in the paper.
"""
import os, sys, math, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
DS = int(sys.argv[2]) if len(sys.argv) > 2 else 60

LI2, LI3 = li_k(X, 2), li_k(X, 3)
ds = list(range(2, DS + 1, 2))
S = {d: twin_S(d) for d in ds}

def C3(a, b, c):
    offs = sorted({a, b, c})
    if len(offs) < 3:
        return 0.0
    try:
        return hl_tuple_constant(tuple(offs), pmax=50_000)
    except ValueError:
        return 0.0

rho = np.zeros((len(ds), len(ds)))
with Timer("kernel"):
    for i, d in enumerate(ds):
        for j, dp in enumerate(ds):
            if i == j:
                continue
            tot = C3(0, d, dp) + C3(0, dp, dp + d) + C3(0, d, d + dp)
            if d > dp:
                tot += C3(0, d - dp, d)
            elif dp > d:
                tot += C3(0, dp - d, dp)
            rho[i, j] = tot * LI3 / (math.sqrt(S[d] * S[dp]) * LI2)
rbar = float(rho[np.triu_indices(len(ds), 1)].mean())
var_common = float(rho.sum() / len(ds) ** 2)  # Var(zbar) approx avg rho
sigma2_pred_upper = 1.0 - var_common
print("pairs evaluated: %d  mean off-diag rho = %.4f" % (len(ds)*(len(ds)-1), rbar))
print("predicted common-mode Var(zbar) = %.4f" % var_common)
print("predicted profile variance (excl. diagonal 4-tuple deficit) <= %.4f" % sigma2_pred_upper)
print("observed profile sd at x=1e8 (from c16 run): ~0.52  => observed var ~0.27")
save_result("c16b", {"conjecture": "covariance kernel of z_d profile from HL triple constants",
                     "X": X, "DS": DS, "mean_offdiag_rho": rbar,
                     "var_common_mode": var_common,
                     "sigma2_pred_upper": sigma2_pred_upper,
                     "observed_sigma2": 0.268})
