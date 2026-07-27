"""C04 (replacement) -- The power-obstruction ladder for n = p + j^k.

Grown from the C13 refutation.  For m >= 2, m^k - j^k factors, so the
only candidate representation of the k-th power m^k as p + j^k is
j = m-1, value D_k(m) = m^k - (m-1)^k.  Hence:

THEOREM (even k >= 4): D_k(m) factors further (via m^{k/2} +- j^{k/2}),
so NO k-th power m^k (m >= 2) is p + j^k.
ELEMENTARY (k = 2): m^2 representable iff 2m-1 prime.
ELEMENTARY (odd k >= 3): m^k representable iff D_k(m) prime.

CONJECTURE: for each odd k >= 3 (and k = 2), Bateman-Horn for D_k:
    #{m <= M : m^k = p + j^k solvable} ~ C_k * int_2^M dt/log D_k(t).
Verified here for k = 2, 3, 5; theorem checked numerically for k = 4.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N4 = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8   # k=4 theorem check range
M3 = int(float(sys.argv[2])) if len(sys.argv) > 2 else 10**6   # k=3 count range
M5 = int(float(sys.argv[3])) if len(sys.argv) > 3 else 8 * 10**5  # k=5 count range

out = {}

# ---- k = 4: theorem check (no fourth power is p + j^4)
with Timer("k=4 theorem check"):
    P = sieve_bool(N4)
    rep = np.zeros(N4 + 1, dtype=bool)
    j = 1
    while j ** 4 < N4:
        c = j ** 4
        rep[c:] |= P[: N4 + 1 - c]
        j += 1
    bad4 = [m for m in range(2, int(N4 ** 0.25) + 1) if m ** 4 <= N4 and rep[m ** 4]]
    del P, rep
print("k=4: fourth powers representable as p+j^4 up to %.0e: %s" % (N4, bad4 or "none (theorem holds)"))
out["k4_counterexamples"] = bad4

# ---- k = 2: m^2 representable iff 2m-1 prime; count vs BH (C = 2 exactly)
with Timer("k=2 count"):
    M2 = 10**7
    P2 = sieve_bool(2 * M2)
    obs2 = int(np.count_nonzero(P2[3: 2 * M2: 2]))  # primes 2m-1, m in [2, M2]
    pred2 = 2 * bh_integral([[-1, 2]], M2)
    del P2
print("k=2: obs=%d pred=%.1f ratio=%.4f z=%+.2f" % (obs2, pred2, obs2 / pred2, zscore(obs2, pred2)))
out["k2"] = {"M": M2, "obs": obs2, "pred": pred2}

# ---- k = 3: D_3 = 3m^2-3m+1
with Timer("k=3 constant+count"):
    C3, C3e = bateman_horn_constant([[1, -3, 3]], pmax=1_000_000)
    r3 = count_poly_primes([[1, -3, 3]], M3, presieve_to=100_000, checkpoints=(M3,))
    pred3 = C3 * bh_integral([[1, -3, 3]], M3)
    obs3 = r3["at"][M3]
print("k=3: C=%.5f obs=%d pred=%.1f ratio=%.4f z=%+.2f"
      % (C3, obs3, pred3, obs3 / pred3, zscore(obs3, pred3)))
out["k3"] = {"M": M3, "C": C3, "C_wobble": abs(C3 - C3e), "obs": obs3, "pred": pred3}

# ---- k = 5: D_5 = 5m^4-10m^3+10m^2-5m+1 (irreducible quartic)
D5 = [1, -5, 10, -10, 5]
with Timer("k=5 constant (brute-force omega)"):
    C5, C5e = bateman_horn_constant([D5], pmax=100_000, brute_below=100_001)
with Timer("k=5 presieve+MR"):
    PB = 20_000
    alive = np.ones(M5 + 1, dtype=bool)
    n0 = 2
    while poly_eval_int(D5, n0) <= PB:
        n0 += 1
    alive[:n0] = False
    for p in primes_up_to(PB):
        p = int(p)
        n = np.arange(p, dtype=np.int64)
        roots = n[poly_eval_mod(D5, n, p) == 0]
        for r in roots:
            r = int(r)
            start = r if r >= n0 else r + ((n0 - r + p - 1) // p) * p
            alive[start:: p] = False
    small = [m for m in range(2, n0) if is_prime(poly_eval_int(D5, m))]
    obs5 = len(small) + sum(1 for m in np.nonzero(alive)[0]
                            if is_prime(poly_eval_int(D5, int(m))))
    pred5 = C5 * bh_integral([D5], M5)
print("k=5: C=%.5f (wobble %.1e) obs=%d pred=%.1f ratio=%.4f z=%+.2f"
      % (C5, abs(C5 - C5e), obs5, pred5, obs5 / pred5, zscore(obs5, pred5)))
out["k5"] = {"M": M5, "C": C5, "C_wobble": abs(C5 - C5e), "obs": obs5, "pred": pred5}

save_result("c04", {"conjecture": "power-obstruction ladder: even k>=4 impossible (thm); "
                                  "odd k / k=2 lanes follow Bateman-Horn for D_k",
                    **out})
