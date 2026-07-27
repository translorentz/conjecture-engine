"""C16(ii) canonical randomization -- the moving-window pair-count field.

The fifth external review observed that Cov(pi_d(x), pi_d'(x)) of the
deterministic cumulative counts is undefined without a randomization.
Canonical fix: sample t uniformly from [X, 2X] and count pairs in the
moving window (t, t+H]:

    pi_d(t; H) = #{t < n <= t+H : n, n+d prime}.

Then Cov_t and Var_t are honest probabilistic quantities, and the
triple-overlap calculus predicts (per unit length, at scale X):

    Cov(pi_d, pi_d') ~ K(d,d') H / log^3 X,   Var(pi_d) ~ S(d) H / log^2 X,
    rho(d,d') ~ K(d,d') / (sqrt(S(d) S(d')) log X),

with K(d,d') the four-configuration sum of Hardy-Littlewood triple
constants (as in the paper).  This script measures the empirical
window-field correlation matrix over W windows and compares it with
the predicted kernel -- entrywise and in the mean.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
H = int(float(sys.argv[2])) if len(sys.argv) > 2 else 10**5
W = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
DS = int(sys.argv[4]) if len(sys.argv) > 4 else 40

ds = list(range(2, DS + 1, 2))
logX = math.log(1.5 * X)

with Timer("sieve [X, 2X+H]"):
    P = sieve_bool(2 * X + DS + H + 1)
    P = P[X:]  # index i  <->  integer X + i

rng = np.random.default_rng(20260727)
t0 = np.sort(rng.integers(0, X - H - DS - 1, W))

emp = np.empty((W, len(ds)))
with Timer("window counts"):
    for j, d in enumerate(ds):
        pd = (P[:-d] & P[d:]).astype(np.int32)
        cnt = np.cumsum(pd, dtype=np.int64)
        emp[:, j] = cnt[t0 + H] - cnt[t0]
        del pd, cnt
del P

C = np.corrcoef(emp, rowvar=False)
emp_mean = float(C[np.triu_indices(len(ds), 1)].mean())

with Timer("predicted kernel"):
    S = {d: twin_S(d) for d in ds}
    def C3(a, b, c):
        offs = sorted({a, b, c})
        if len(offs) < 3:
            return 0.0
        try:
            return hl_tuple_constant(tuple(offs), pmax=20_000)
        except ValueError:
            return 0.0
    pred = np.zeros((len(ds), len(ds)))
    for i, d in enumerate(ds):
        for j, dp in enumerate(ds):
            if i == j:
                pred[i, j] = 1.0
                continue
            tot = C3(0, d, dp) + C3(0, dp, dp + d) + C3(0, d, d + dp)
            tot += C3(0, abs(d - dp), max(d, dp))
            pred[i, j] = tot / (math.sqrt(S[d] * S[dp]) * logX)

iu = np.triu_indices(len(ds), 1)
pred_mean = float(pred[iu].mean())
match = float(np.corrcoef(C[iu], pred[iu])[0, 1])
resid = C[iu] - pred[iu]
print("windows: %d  H=%.0e  d <= %d  (%d pairs)" % (W, H, DS, len(iu[0])))
print("empirical mean off-diag corr = %.4f   predicted = %.4f" % (emp_mean, pred_mean))
print("entrywise correlation(empirical kernel, predicted kernel) = %.3f" % match)
print("mean residual (emp - pred) = %+.4f  sd %.4f" % (float(resid.mean()), float(resid.std())))
# also check Poisson-level variance ratio per d (diagonal deficit visible?)
var_ratio = emp.var(axis=0) / emp.mean(axis=0)
print("Var/mean across d: min %.3f  mean %.3f  max %.3f (sub-Poisson expected)"
      % (var_ratio.min(), var_ratio.mean(), var_ratio.max()))
save_result("c16c", {"conjecture": "moving-window pair-count field: empirical correlation matrix "
                                   "matches HL triple-constant kernel",
                     "X": X, "H": H, "W": W, "DS": DS,
                     "emp_mean_offdiag": emp_mean, "pred_mean_offdiag": pred_mean,
                     "kernel_entry_correlation": match,
                     "mean_residual": float(resid.mean()),
                     "resid_sd": float(resid.std()),
                     "var_over_mean": [float(v) for v in var_ratio]})
