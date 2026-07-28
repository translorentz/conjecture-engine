"""C1 family statistics -- derived moments of the constants C(d).

The sixth external review asked for a genuinely family-level statistic
rather than an appended error exponent.  The constants
C(d) = C(x^2+1, x^2+1+d) admit DERIVED moments: each local factor
f_p(d) depends only on d mod p, and d mod p equidistributes as d
ranges over an interval of even numbers, so

    mean:      Cbar   = f_2 * prod_{p>=3} E_d[f_p(d)],
    2nd moment: C2bar = f_2^2 * prod_{p>=3} E_d[f_p(d)^2],

each an explicit Euler product (the factors for distinct p are exactly
independent as d varies, by CRT).  Conjecture-level content: the
empirical distribution of C(d) over even d <= D converges, with these
moments, to the law of the random product prod_p f_p(U_p) with
independent uniform U_p mod p.  This script computes Cbar and the
standard deviation from the Euler products and compares them with the
empirical mean/sd of the 150 constants for even d <= 300.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

PMAX = int(float(sys.argv[1])) if len(sys.argv) > 1 else 100_000
DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300

with Timer("derived moments (Euler products over p <= %d)" % PMAX):
    log_mean = 0.0
    log_m2 = 0.0
    f2 = 2.0  # p=2: n even forced; omega(2)=1 for every even d: (1-1/2)/(1-1/2)^2 = 2
    for p in primes_up_to(PMAX):
        p = int(p)
        if p == 2:
            continue
        # roots of x^2+1 mod p: 1+chi(-1); roots of x^2+1+d: 1+chi(-1-d)
        # (single root 0 if p | 1+d); root sets coincide iff p | d.
        n = np.arange(p, dtype=np.int64)
        issq = np.zeros(p, dtype=bool)
        issq[(n * n) % p] = True
        r1 = 2 if issq[p - 1] else 0
        a = (p - 1 - n) % p                       # a = -(1+d) mod p for d = n
        r2 = np.where(a == 0, 1, np.where(issq[a], 2, 0))
        om = (r1 + r2).astype(float)
        om[0] = r1                                # d = 0: same polynomial
        fs = (1 - om / p) / (1 - 1.0 / p) ** 2
        log_mean += math.log(fs.mean())
        log_m2 += math.log((fs ** 2).mean())
    Cbar = f2 * math.exp(log_mean)
    C2bar = f2 ** 2 * math.exp(log_m2)
    sd = math.sqrt(max(C2bar - Cbar ** 2, 0.0))
print("derived: mean C(d) = %.4f   sd = %.4f" % (Cbar, sd))

with Timer("empirical constants d <= %d" % DMAX):
    Cs = []
    for d in range(2, DMAX + 1, 2):
        C, _ = bateman_horn_constant([[1, 0, 1], [1 + d, 0, 1]], pmax=50_000)
        Cs.append(C)
    Cs = np.array(Cs)
print("empirical (%d shifts): mean = %.4f   sd = %.4f" % (len(Cs), Cs.mean(), Cs.std()))
print("mean ratio emp/derived = %.4f   sd ratio = %.4f"
      % (Cs.mean() / Cbar, Cs.std() / sd))
save_result("c01b", {"conjecture": "distribution of C(d): derived Euler-product moments "
                                   "match the empirical family",
                     "PMAX": PMAX, "DMAX": DMAX,
                     "derived_mean": Cbar, "derived_sd": sd,
                     "empirical_mean": float(Cs.mean()), "empirical_sd": float(Cs.std()),
                     "n_shifts": len(Cs)})
