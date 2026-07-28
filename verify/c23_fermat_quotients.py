"""C23 -- Fermat quotients: equidistribution and Wieferich accounting.

q_p(2) = (2^{p-1}-1)/p mod p.  Conjecture:
  (a) q_p(2)/p is equidistributed on [0,1) with square-root discrepancy
      (KS statistic of size ~ 1/sqrt(pi(x)), no drift);
  (b) #{Wieferich p <= x} = #{q_p(2)=0} ~ sum_{p<=x} 1/p ~ log log x + M
      (M = 0.2615), so only {1093, 3511} below 10^8;
  (c) small-quotient counts #{p<=x : q_p(2) < K} ~ K * sum 1/p (uniform tail).
Verification: (a),(c) to 10^7, (b) to 10^8.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

XA = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7
XB = int(float(sys.argv[2])) if len(sys.argv) > 2 else 10**8
MERTENS = 0.2614972128476428

with Timer("quotients to XA"):
    us = []
    small = []          # (p, q_p) with q_p < 100
    for p in primes_up_to(XA):
        p = int(p)
        if p == 2:
            continue
        fq = (pow(2, p - 1, p * p) - 1) // p
        us.append(fq / p)
        if fq < 100:
            small.append((p, fq))
us = np.sort(np.array(us))
n = len(us)
ks = float(np.max(np.abs(np.arange(1, n + 1) / n - us)))
half = n // 2
print("(a) primes used: %d   KS = %.6f   sqrt(n)*KS = %.3f" % (n, ks, ks * math.sqrt(n)))
print("    mean u = %.5f (want 0.5)" % us.mean())

s1p = sum(1.0 / p for p in primes_up_to(XA) if p > 2)
model_c = sum(min(1.0, 100.0 / p) for p in primes_up_to(XA) if p > 2)
print("(c) #{q_p < 100} = %d,  model sum min(1,100/p) = %.1f" % (len(small), model_c))

with Timer("Wieferich sweep to XB"):
    wief = []
    for lo, hi, seg in seg_sieve(XB, seg_size=1 << 24):
        for p in np.nonzero(seg)[0]:
            p = int(p + lo)
            if p > 2 and pow(2, p - 1, p * p) == 1:
                wief.append(p)
                print("    Wieferich:", p)
exp_w = math.log(math.log(XB)) + MERTENS - 0.5  # subtract 1/2 for p=2
print("(b) Wieferich <= %.0e: %s   expected ~ %.2f" % (XB, wief, exp_w))

save_result("c23", {"conjecture": "Fermat quotients equidistribute; Wieferich count ~ loglog x",
                    "XA": XA, "XB": XB, "KS": ks, "sqrt_n_KS": ks * math.sqrt(n),
                    "mean_u": float(us.mean()),
                    "small_quotient_obs": len(small), "small_quotient_pred": model_c,
                    "wieferich": wief, "wieferich_expected": exp_w})
