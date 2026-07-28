"""C14' -- the Stern lane race: k-parity lanes in n = p + 2k^2.

Contamination for the representation count comes from n = q^2 + 2k^2
(the norm form x^2 + 2y^2 of Q(sqrt(-2)) with prime x).  Since
q^2 = 1 (mod 8) for odd q and 2k^2 = 0 or 2 (mod 8) by k parity:
  n = 1 (mod 8):  contamination sits in the k-EVEN lane;
  n = 3 (mod 8):  contamination sits in the k-ODD lane;
  n = 5, 7 (mod 8):  NO square contamination exists (null classes).
Predicted drift (clean lane minus contaminated lane):
  D(n) = R_clean(n) - R_contam(n) = D_sys(n) + noise,
  D_sys(n) = [ sum_{(q,k): q^2+2k^2=n, q prime, k>=1} 2 log q ] / lam(n),
lam(n) the mean of log p over the representations (empirical
estimator of the analytic lane mean); for n = 5,7 (mod 8) the lane
difference is pure noise.  Four-way stratified test.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
NSAMP = int(sys.argv[2]) if len(sys.argv) > 2 else 600

with Timer("sieve"):
    P = sieve_bool(X)

rng = np.random.default_rng(20260728)
lo, hi = 10**6, X - 10
samples = np.unique((np.exp(rng.uniform(math.log(lo), math.log(hi), NSAMP))
                     .astype(np.int64) // 2) * 2 + 1)

strata = {1: [], 3: [], 5: [], 7: []}
with Timer("lane race over %d samples" % len(samples)):
    for n in samples:
        n = int(n)
        kmax = int(math.isqrt((n - 3) // 2))
        k = np.arange(1, kmax + 1, dtype=np.int64)
        v = n - 2 * k * k
        pr = P[v]
        if not pr.any():
            continue
        kp = k[pr]
        vp = v[pr]
        Re = int(np.count_nonzero(kp % 2 == 0))
        Ro = len(kp) - Re
        lam = float(np.mean(np.log(vp.astype(float))))
        # contamination: v = q^2 with q prime
        q = np.sqrt(v.astype(float)).astype(np.int64)
        sq = (q * q == v) & (v > 1)
        dsys = 0.0
        for i in np.nonzero(sq)[0]:
            qq = int(q[i])
            if is_prime(qq):
                dsys += 2 * math.log(qq)
        dsys /= lam
        cls = n % 8
        if cls == 1:
            D = Ro - Re      # clean minus contaminated (even contaminated)
        elif cls == 3:
            D = Re - Ro
        else:
            D = Re - Ro      # sign irrelevant; should be pure noise
        strata[cls].append((D, dsys, Re + Ro))

out = {}
for cls in (1, 3, 5, 7):
    arr = strata[cls]
    if not arr:
        continue
    D = np.array([a[0] for a in arr], dtype=float)
    S = np.array([a[1] for a in arr])
    R = np.array([a[2] for a in arr], dtype=float)
    se = D.std() / math.sqrt(len(D))
    tag = "contaminated" if cls in (1, 3) else "NULL"
    print("n=%d (8) [%s]: samples=%d  mean D=%+.2f +- %.2f  mean D_sys=%.2f  "
          "mean reps=%.0f" % (cls, tag, len(D), D.mean(), se, S.mean(), R.mean()))
    out[str(cls)] = {"n": len(D), "mean_D": float(D.mean()), "se": float(se),
                     "mean_Dsys": float(S.mean()), "mean_reps": float(R.mean())}
save_result("c14b", {"conjecture": "Stern lane race: k-parity drift = norm-form contamination, "
                                   "classes 1,3 (mod 8) contaminated (opposite lanes), 5,7 null",
                     "X": X, "strata": out})
