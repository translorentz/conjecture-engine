"""C24 upgrade -- the derived covariance kernel of the Conjecture-F family.

Two members Q_A, Q_A' share the index set n <= N, so their counts are
correlated exactly when n^2+n+A and n^2+n+A' are simultaneously prime,
an event governed by the PAIR singular series
C(A,A') = C(x^2+x+A, x^2+x+A').  In the local model,

  Cov(Q_A, Q_A') ~ [C(A,A') - C(A) C(A')] * I_{A,A'}(N),
  Var(Q_A)       ~ C(A) I_A(N)              (Poisson level),

so the correlation kernel is

  rho(A,A') ~ [C(A,A') - C(A)C(A')] I_{A,A'}(N)
              / sqrt(C(A) I_A(N) * C(A') I_A'(N)),

with rho < 0 for inadmissible pairs (C(A,A') = 0: the members exclude
each other locally).  The common-mode average of rho then sets the
depression of the observed z-profile variance below 1, exactly as the
triple-constant kernel does for Conjecture 16.  This script evaluates
the kernel over odd A <= AMAX and compares the predicted profile
variance with the observed z-profile from the c24 run.
"""
import os, sys, math, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**6
AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 99
PMAX_PAIR = 20_000

AS = list(range(1, AMAX + 1, 2))
with Timer("single constants"):
    C1, I1 = {}, {}
    for A in AS:
        C1[A], _ = bateman_horn_constant([[A, 1, 1]], pmax=200_000)
        I1[A] = bh_integral([[A, 1, 1]], N)

rho = np.zeros((len(AS), len(AS)))
n_inadm = 0
with Timer("pair kernel"):
    for i, A in enumerate(AS):
        for j in range(i + 1, len(AS)):
            Ap = AS[j]
            polys = [[A, 1, 1], [Ap, 1, 1]]
            try:
                Cp, _ = bateman_horn_constant(polys, pmax=PMAX_PAIR)
            except ValueError:
                Cp = 0.0
                n_inadm += 1
            I2 = bh_integral(polys, N)
            r = (Cp - C1[A] * C1[Ap]) * I2 / math.sqrt(C1[A] * I1[A] * C1[Ap] * I1[Ap])
            rho[i, j] = rho[j, i] = r

off = rho[np.triu_indices(len(AS), 1)]
rbar = float(off.mean())
var_common = float(rho.sum() / len(AS) ** 2)
print("family size %d (odd A <= %d), inadmissible pairs: %d" % (len(AS), AMAX, n_inadm))
print("mean off-diag rho = %+.4f   min %.4f  max %.4f" % (rbar, off.min(), off.max()))
print("predicted common-mode Var(zbar) = %.4f" % var_common)
print("predicted profile variance (excl. diagonal deficit) <= %.4f" % (1 - var_common))

obs_sd = None
try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                           "results", "c24.json")) as f:
        rows = json.load(f)["rows"]
    zs = np.array([r["z"] for r in rows if r["A"] <= AMAX])
    obs_sd = float(zs.std())
    print("observed z-profile sd over same A range (c24 run): %.3f  => var %.3f"
          % (obs_sd, obs_sd ** 2))
except Exception as e:
    print("no c24 observed profile available:", e)

save_result("c24b", {"conjecture": "Conjecture-F family covariance kernel from pair singular series",
                     "N": N, "AMAX": AMAX, "mean_offdiag_rho": rbar,
                     "var_common_mode": var_common,
                     "sigma2_pred_upper": 1 - var_common,
                     "n_inadmissible_pairs": n_inadm,
                     "observed_profile_sd": obs_sd})
