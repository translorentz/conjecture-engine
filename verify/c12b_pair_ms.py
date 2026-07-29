"""C12' -- the pair-level Montgomery-Soundararajan reduction: the
DIAGONAL variance deficit for twin-pair counts in short windows.

For the window field of C16(ii), the variance of pi_2(t;H) below its
Poisson value is governed by the averaged 4-tuple singular series.
With R(h) = C4(0,2,h,h+2)/S(2)^2 (normalized pair-pair correlation;
the overlap term C3(0,2,4) vanishes identically -- {0,2,4} is
inadmissible mod 3, so consecutive twin pairs cannot overlap beyond
(3,5,7)) and

  G(H) := sum_{1<=h<=H} (1 - h/H) (R(h) - 1),

the identity behind the clause is

  Var/E[pi_2(t;H)] = 1 + S(2)(2 G(H) - 1)/log^2 x + o(1/log^2 x),

the -S(2)/log^2 x piece being the explicit Bernoulli diagonal term.

The growth of -G(H) is OPEN.  What is conjectured is only that
-G(H)/log H diverges, i.e. that the pinned pair average grows
strictly faster than the single-prime Montgomery-Soundararajan
secondary term (1/2)(log H + gamma + log 2pi - 1).  The computable
range does not determine the form: a pure log with a large constant,
c log H log log H, and (log H)^alpha all remain compatible with it.
The script therefore only FITS the quadratic-in-log model

  G(H) = -c2 log^2 H - c1 log H + O(1)

(the least-squares coefficients printed below are those of the
equivalent form G = c0 + c1 log H + c2 log^2 H, hence carry the
opposite signs), reporting the log-squared coefficient and its
stability across subranges.  Its sign is NOT assumed and no
log-squared law is asserted; the fit is descriptive of the computable
range, matching the caveat carried with the conjecture in the paper.

The script computes R(h) for h <= HMAX from Euler products, performs
that fit, and compares the extrapolated window deficit with the
measured Var/mean of the c16c window experiment.
"""
import os, sys, math, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

HMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
PMAX = int(float(sys.argv[2])) if len(sys.argv) > 2 else 20_000

S2 = twin_S(2)
# ALL shifts h >= 1: odd h and h = 2 give inadmissible 4-sets (R = 0);
# the second-order log lives in the odd-even alternation, exactly as in
# the Montgomery-Soundararajan single-prime average.
hs = np.arange(1, HMAX + 1)
R = np.empty(len(hs))
with Timer("C4 evaluations (%d values)" % len(hs)):
    for i, h in enumerate(hs):
        h = int(h)
        offs = sorted({0, 2, h, h + 2})
        if len(offs) < 4:
            R[i] = 0.0
            continue
        try:
            R[i] = hl_tuple_constant(tuple(offs), pmax=PMAX) / S2 ** 2
        except ValueError:
            R[i] = 0.0

Hs = np.arange(100, HMAX + 1, 50)
G = np.empty(len(Hs))
for j, H in enumerate(Hs):
    sel = hs <= H
    G[j] = float(np.sum((1 - hs[sel] / H) * (R[sel] - 1)))


# the single-prime MS average has a pure log secondary term; the
# growth of the PINNED-pair average is open -- fit the full
# quadratic-in-log model, without assuming the sign of the log^2
# coefficient, and check stability on subranges.
def fitq(mask):
    L = np.log(Hs[mask].astype(float))
    A = np.column_stack([np.ones(mask.sum()), L, L * L])
    c, *_ = np.linalg.lstsq(A, G[mask], rcond=None)
    return c  # (c0, c1, c2): G = c0 + c1 log H + c2 log^2 H


c_all = fitq(np.ones(len(Hs), dtype=bool))
c_lo = fitq(Hs <= HMAX // 2)
c_hi = fitq(Hs > HMAX // 2)
beta2 = -2 * c_all[2]
print("fit G(H) = c0 + c1 log H + c2 log^2 H:")
print("  all:   c0=%+.3f  c1=%+.4f  c2=%+.5f   (beta2 = -2 c2 = %.4f)"
      % (*c_all, beta2))
print("  lower: c2=%+.5f | upper: c2=%+.5f  (stability)" % (c_lo[2], c_hi[2]))
print("MS single-prime secondary is pure log (constant gamma+log 2pi - 1 = %.4f); "
      "the growth of -G(H) is open -- c2 is a fitted coefficient, its sign "
      "not assumed" % (EULER_GAMMA + math.log(2 * math.pi) - 1))

# predicted window deficit vs the c16c measurement (x = 1e8..2e8, H = 1e5):
# Var/E - 1 = S2 (2 G(H) - 1) / log^2 x, extrapolating the fitted G
# (the -S2/log^2 x Bernoulli diagonal term is retained; the
# extrapolation is descriptive, since the growth of -G is open).
xbar = 1.5e8
Hwin = 1e5
LH = math.log(Hwin)
Gext = c_all[0] + c_all[1] * LH + c_all[2] * LH * LH
pred = 1 + S2 * (2 * Gext - 1) / math.log(xbar) ** 2
obs = None
try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                           "results", "c16c.json")) as f:
        vm = json.load(f)["var_over_mean"]
    obs = float(vm[0])          # d = 2 entry
    obs_mean = float(np.mean(vm))
    print("extrapolated G(1e5) = %.1f -> predicted Var/E: %.3f   observed (d=2): %.3f  "
          "(mean over d: %.3f)" % (Gext, pred, obs, obs_mean))
except Exception as e:
    print("c16c comparison unavailable:", e)

save_result("c12b", {"conjecture": "pair-level MS reduction: "
                                   "Var/E = 1 + S(2)(2 G(H) - 1)/log^2 x; "
                                   "growth of -G(H) open, fitted "
                                   "G(H) = -c2 log^2 H - c1 log H + O(1), "
                                   "sign of c2 not assumed",
                     "HMAX": HMAX, "fit_c0c1c2": [float(v) for v in c_all],
                     "beta2": float(beta2),
                     "c2_lower": float(c_lo[2]), "c2_upper": float(c_hi[2]),
                     "G_ext_1e5": float(Gext),
                     "pred_var_over_mean": float(pred), "obs_var_over_mean_d2": obs,
                     "R_first": [float(r) for r in R[:10]]})
