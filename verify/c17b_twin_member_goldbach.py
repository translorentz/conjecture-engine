"""C17' -- quantitative twin-member Goldbach: the orientation-decomposed
Hardy-Littlewood law.

R_T(n) = # ordered (a,b), a+b = n, both a and b members of twin-prime
pairs.  Each unordered orientation (a lower/upper member, b
lower/upper) is a 4-form linear system in t = a:
  (L,L): {t, t+2, n-t, n-t+2}    root set {0,-2,n,n+2} mod p
  (L,U): {t, t+2, n-t-2, n-t}    roots {0,-2,n-2,n}
  (U,L): {t, t-2, n-t, n-t+2}    roots {0,2,n,n+2}
  (U,U): {t, t-2, n-t-2, n-t}    roots {0,2,n-2,n}
Main-term law:
  R_T(n) ~ [ sum_orient S4^{(o)}(n) ] * J(n),
  S4^{(o)}(n) = prod_p (1 - omega_o(p)/p)/(1-1/p)^4,
  J(n) = int dt / (log^2 t log^2(n-t)),
with omega_o(p) = #distinct roots mod p (computed exactly per n).
Members counted with multiplicity of the roles they can play (a member
of two orientations contributes to both), which is what the ordered
count with orientation labels measures.  Derived profile over n vs
exact counts; Dubner's qualitative basis conjecture is the attributed
antecedent, the quantitative orientation law is the new content.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
NSAMP = int(sys.argv[2]) if len(sys.argv) > 2 else 200
PMAX = int(float(sys.argv[3])) if len(sys.argv) > 3 else 30_000

with Timer("sieve + twin members"):
    P = sieve_bool(X)
    tw = P[:-2] & P[2:]
    lower = np.nonzero(tw)[0]
    member = np.zeros(X + 1, dtype=bool)
    member[lower] = True
    member[lower + 2] = True
    lowset = np.zeros(X + 1, dtype=bool)
    lowset[lower] = True
    upset = np.zeros(X + 1, dtype=bool)
    upset[lower + 2] = True

low_arr = lower.astype(np.int64)
up_arr = (lower + 2).astype(np.int64)
ps = [int(p) for p in primes_up_to(PMAX)]
# root sets: {r1, r2, n+s3, n+s4} with (r1, r2) fixed and shifts for n

def S4(n, o):
    r1, r2, s3, s4 = {"LL": (0, -2, 0, 2), "LU": (0, -2, -2, 0),
                      "UL": (0, 2, 0, 2), "UU": (0, 2, -2, 0)}[o]
    logv = 0.0
    for p in ps:
        roots = {r1 % p, r2 % p, (n + s3) % p, (n + s4) % p}
        om = len(roots)
        if om >= p:
            return 0.0
        logv += math.log1p(-om / p) - 4 * math.log1p(-1.0 / p)
    return math.exp(logv)

def J(n):
    t = np.exp(np.linspace(math.log(5.0), math.log(n - 5.0), 3001))
    f = 1.0 / (np.log(t) ** 2 * np.log(n - t) ** 2)
    return float(np.trapezoid(f, t))

rng = np.random.default_rng(20260728)
samples = np.unique((np.exp(rng.uniform(math.log(10**6), math.log(X - 10), NSAMP))
                     .astype(np.int64) // 2) * 2)

rows = []
with Timer("profile over %d samples" % len(samples)):
    for n in samples:
        n = int(n)
        obs = 0
        for arr, bset in ((low_arr, lowset), (low_arr, upset),
                          (up_arr, lowset), (up_arr, upset)):
            i = np.searchsorted(arr, n - 4)
            aa = arr[:i]
            aa = aa[aa >= 5]
            obs += int(np.count_nonzero(bset[n - aa]))
        pred = J(n) * sum(S4(n, o) for o in ("LL", "LU", "UL", "UU"))
        if pred > 0:
            rows.append((n, obs, pred))

ns = np.array([r[0] for r in rows], dtype=float)
obs = np.array([r[1] for r in rows], dtype=float)
pred = np.array([r[2] for r in rows])
ratio = obs.sum() / pred.sum()
corr = float(np.corrcoef(np.log(obs + 1), np.log(pred + 1))[0, 1])
z = (obs - pred) / np.sqrt(np.maximum(pred, 1))
print("samples: %d  aggregate obs/pred = %.4f  log-log correlation = %.4f"
      % (len(rows), ratio, corr))
print("z-profile: mean %+.2f  sd %.2f  max|z| %.2f" % (z.mean(), z.std(), np.abs(z).max()))
blocks = []
for a, b in ((1e6, 1e7), (1e7, 1e8)):
    sel = (ns >= a) & (ns < b)
    if sel.sum() > 5:
        rr = float(obs[sel].sum() / pred[sel].sum())
        # implied second-order constant: ratio = 1 - c/log n
        c = float((1 - rr) * np.log(ns[sel]).mean())
        blocks.append({"range": "[%.0e,%.0e)" % (a, b), "ratio": rr, "c_implied": c})
        print("block %s: ratio = %.4f  implied deficit constant c = %.2f"
              % (blocks[-1]["range"], rr, c))
save_result("c17b", {"conjecture": "quantitative twin-member Goldbach: R_T(n) ~ "
                                   "[sum of 4 orientation S4(n)] J(n)",
                     "X": X, "n_samples": len(rows), "agg_ratio": float(ratio),
                     "loglog_corr": corr, "z_mean": float(z.mean()),
                     "z_sd": float(z.std()), "z_max": float(np.abs(z).max()),
                     "blocks": blocks})
