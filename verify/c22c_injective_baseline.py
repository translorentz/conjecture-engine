"""C22 -- the injective no-collision baseline (eighth review).

For prime modulus q, the primes p < q occupy DISTINCT classes mod q:
a deterministic injective initial phase no exchangeable allocation
reproduces.  Its contribution to the ordering deficit has a closed
form in index time (Li(p_i) ~ i, so U = first-hit index / phi):
forcing the first k0 = pi(q) arrivals to be collision-free and the
rest exchangeable gives

  E[U] = 1 - k0^2/(2 phi^2) + O(k0/phi^2),
  Theta_inj(q) = (1 - E[U]) log q = (1 + o(1)) / (2 log q).

This script verifies the closed form by Monte Carlo and evaluates it
across the measured modulus range [1500, 6000]: Theta_inj ~ 0.07-0.09,
an order of magnitude below the measured theta_corr = 0.824 +- 0.009,
and decaying in q where theta_corr is flat.  The injective phase is
the y < q head of the pair-correlation expansion (collisions require
q | p2 - p1), so subtracting it is the first term of the registered
occupancy programme, not a rival explanation.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

REPS = int(sys.argv[1]) if len(sys.argv) > 1 else 400
rng = np.random.default_rng(20260728)

MODULI = [1499, 2003, 3001, 4001, 4999, 5987]


def pi_below(x):
    # primes strictly below x (x itself, when prime, is 0 mod x and
    # occupies no reduced class)
    return int(np.count_nonzero(primes_up_to(x) < x))


out = {}
for q in MODULI:
    phi = q - 1
    k0 = pi_below(q)
    tot = 0.0
    for _ in range(REPS):
        first = np.empty(phi, dtype=np.int64)
        cls1 = rng.choice(phi, size=k0, replace=False)
        mask = np.ones(phi, dtype=bool)
        mask[cls1] = False
        first[cls1] = np.arange(1, k0 + 1)
        first[mask] = k0 + rng.geometric(1.0 / phi, size=phi - k0)
        tot += first.mean() / phi
    Eu = tot / REPS
    closed = 1 - k0 ** 2 / (2 * phi ** 2) + k0 / (2 * phi ** 2)
    th_mc = (1 - Eu) * math.log(q)
    th_cf = (1 - closed) * math.log(q)
    print("q=%d: pi(q)=%d  E[U]_inj=%.5f (closed %.5f)  Theta_inj=%.4f (closed %.4f)"
          % (q, k0, Eu, closed, th_mc, th_cf))
    out[str(q)] = {"pi_q": k0, "EU_mc": float(Eu), "EU_closed": float(closed),
                   "Theta_inj_mc": float(th_mc), "Theta_inj_closed": float(th_cf)}

save_result("c22c", {"conjecture": "injective no-collision baseline for C22: "
                                   "Theta_inj = (1+o(1))/(2 log q), an order of magnitude "
                                   "below measured theta_corr = 0.824",
                     "reps": REPS, "moduli": out})
