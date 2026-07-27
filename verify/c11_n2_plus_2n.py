"""C11 -- Primes of the form n^2 + 2^n.

Local analysis: n must be odd (parity) and divisible by 3 (else 3 | n^2+2^n),
so n = 3 (mod 6).  With local correction kappa = prod_p (1-delta_p)/(1-1/p),
where delta_p = density of n = 3 (mod 6) with p | n^2 + 2^n (period
lcm(6, p*ord_p(2))), the model predicts
    E(N) = sum_{n=3 (mod 6), n<=N} kappa / log(n^2 + 2^n)  ~  (kappa/(6 log 2)) log N.
Conjecture: infinitely many, with counting function tracking E(N).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 4200
PMAX_LOCAL = 300


def local_kappa(pmax):
    log_kappa = 0.0
    for p in primes_up_to(pmax):
        p = int(p)
        if p == 2 or p == 3:
            delta = 0.0  # proved impossible for n = 3 (mod 6)
        else:
            # ord_p(2)
            d = 1
            t = 2 % p
            while t != 1:
                t = t * 2 % p
                d += 1
            period = int(np.lcm(6, p * d))
            n = np.arange(period, dtype=np.int64)
            sel = n % 6 == 3
            cycle = np.empty(d, dtype=np.int64)
            t = 1
            for i in range(d):
                cycle[i] = t
                t = t * 2 % p
            val = (n * n + cycle[n % d]) % p
            hit = sel & (val == 0)
            delta = hit.sum() / sel.sum()
        log_kappa += math.log1p(-delta) - math.log1p(-1.0 / p)
    return math.exp(log_kappa)


with Timer("local constant"):
    kappa = local_kappa(PMAX_LOCAL)
print("kappa (p <= %d) = %.4f" % (PMAX_LOCAL, kappa))

hits = []
with Timer("PRP scan"):
    for n in range(3, N + 1, 6):
        if is_prime(n * n + (1 << n)):
            hits.append(n)
            print("  n = %d" % n)


def expected(upto):
    e = 0.0
    for n in range(3, upto + 1, 6):
        e += kappa / (n * math.log(2) + math.log1p(n * n / 2.0 ** n))
    return e


rows = []
for x in [c for c in (10**2, 10**3) if c < N] + [N]:
    obs = sum(1 for h in hits if h <= x)
    pred = expected(x)
    rows.append({"N": x, "obs": obs, "pred": round(pred, 2),
                 "z": round(zscore(obs, pred), 2)})
    print("N=%d  obs=%d  pred=%.2f  z=%+.2f" % (x, obs, pred, zscore(obs, pred)))

save_result("c11", {"conjecture": "infinitely many primes n^2+2^n; count ~ E(N)",
                    "kappa": kappa, "hits": hits, "table": rows})
