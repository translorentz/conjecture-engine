"""C11 (upgrade) -- entanglement-aware local constant for n^2 + 2^n.

The per-prime product kappa = prod_p (1 - delta_p)/(1 - 1/p) tacitly
assumes the survival events at distinct primes are independent over
their joint period.  They need not be: the survival event at p is
periodic in n with period T_p = lcm(6, p * ord_p 2), and distinct T_p
share factors.  Following the fourth external review we define, for
each finite set S of primes, the CRT-exact quantity

    kappa_S = D_S / prod_{p in S} (1 - 1/p),

where D_S is the EXACT density, within the lane n = 3 (mod 6), of n
with p | n^2 + 2^n for no p in S, computed over the full joint period
L_S = lcm of the T_p.  The upgraded conjecture is that the net
{kappa_S} converges as S increases to all primes; the working constant
multiplies kappa_{p<=19}^CRT by the per-prime factors for
23 <= p <= 300 (conjecturally negligible entanglement in the tail).

This script (1) computes kappa_S exactly for nested S = {p <= P},
P in {5,...,19}, against the naive per-prime product on the same S;
(2) extends the PRP scan from 4200 to NMAX (default 6000).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

NMAX = int(float(sys.argv[1])) if len(sys.argv) > 1 else 6000
PMAX_TAIL = 300
PRESIEVE = 100_000

CORE = [5, 7, 11, 13, 17, 19]  # 2, 3 are exact zeros on the lane


def ord2(p):
    d, t = 1, 2 % p
    while t != 1:
        t = t * 2 % p
        d += 1
    return d


def per_prime_delta(p):
    d = ord2(p)
    period = int(np.lcm(6, p * d))
    n = np.arange(period, dtype=np.int64)
    sel = n % 6 == 3
    cyc = np.empty(d, dtype=np.int64)
    t = 1
    for i in range(d):
        cyc[i] = t
        t = t * 2 % p
    hit = sel & ((n * n + cyc[n % d]) % p == 0)
    return hit.sum() / sel.sum()


with Timer("CRT-exact joint densities"):
    rows = []
    for k in range(1, len(CORE) + 1):
        S = CORE[:k]
        L = 6
        data = {}
        for p in S:
            d = ord2(p)
            L = int(np.lcm(L, p * d))
            cyc = np.empty(d, dtype=np.int64)
            t = 1
            for i in range(d):
                cyc[i] = t
                t = t * 2 % p
            data[p] = (d, cyc)
        lane = L // 6
        surv = 0
        CH = 4_000_000
        for lo in range(0, lane, CH):
            hi = min(lane, lo + CH)
            n = 3 + 6 * np.arange(lo, hi, dtype=np.int64)
            alive = np.ones(hi - lo, dtype=bool)
            for p in S:
                d, cyc = data[p]
                alive &= (n % p * (n % p) + cyc[n % d]) % p != 0
            surv += int(np.count_nonzero(alive))
        D = surv / lane
        base = 1.0
        for p in S:
            base *= 1 - 1.0 / p
        kcrt = D / base
        knaive = 1.0
        for p in S:
            knaive *= (1 - per_prime_delta(p)) / (1 - 1.0 / p)
        rows.append({"P": S[-1], "L": L, "kappa_crt": kcrt,
                     "kappa_naive": knaive, "rel_gap": kcrt / knaive - 1})
        print("S = p<=%2d  L=%11d  kappa_crt=%.6f  naive=%.6f  gap=%+.2e"
              % (S[-1], L, kcrt, knaive, kcrt / knaive - 1))

with Timer("tail factors 23..%d" % PMAX_TAIL):
    tail = 1.0
    for p in primes_up_to(PMAX_TAIL):
        p = int(p)
        if p <= 19:
            continue
        tail *= (1 - per_prime_delta(p)) / (1 - 1.0 / p)
    # lane bonuses at 2 and 3 (delta = 0 exactly)
    lane_factor = 2.0 * 1.5
    kappa_star = lane_factor * rows[-1]["kappa_crt"] * tail
print("working constant kappa* = %.4f  (lane 3, core CRT %.6f, tail %.6f)"
      % (kappa_star, rows[-1]["kappa_crt"], tail))

hits = []
with Timer("PRP scan to %d" % NMAX):
    small = primes_up_to(PRESIEVE)
    for n in range(3, NMAX + 1, 6):
        v_ok = True
        for p in small:
            p = int(p)
            if (n * n + pow(2, n, p)) % p == 0 and (n * n + (1 << n)) != p:
                v_ok = False
                break
        if v_ok and is_prime(n * n + (1 << n)):
            hits.append(n)
            print("  n = %d" % n)


def expected(upto, kap):
    e = 0.0
    for n in range(3, upto + 1, 6):
        t = math.log1p(n * n / 2.0 ** n) if n < 900 else 0.0
        e += kap / (n * math.log(2) + t)
    return e


table = []
for x in (10**3, 4200, NMAX):
    obs = sum(1 for h in hits if h <= x)
    pred = expected(x, kappa_star)
    table.append({"N": x, "obs": obs, "pred": round(pred, 2),
                  "z": round(zscore(obs, pred), 2)})
    print("N=%d  obs=%d  pred=%.2f  z=%+.2f" % (x, obs, pred, zscore(obs, pred)))

save_result("c11b", {"conjecture": "n^2+2^n: CRT-exact kappa_S net converges; count ~ E(N)",
                     "crt_rows": rows, "kappa_star": kappa_star,
                     "tail_factor": tail, "hits": hits, "table": table})
