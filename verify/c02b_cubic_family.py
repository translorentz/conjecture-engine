"""C02' -- the cubic family: distribution of the constants C(a) and
uniformity over a.

For f_a(x) = x^3 + a (a not a cube), only primes p = 1 (mod 3) move
the singular series: omega_a(p) = 3 if -a is a nonzero cube mod p,
1 if p | a, else 0.  As a varies, the local factors at distinct p are
exactly independent (CRT), and -- unlike the quadratic pair family of
C1 -- the variance sum converges WITHOUT normalization, so C(a) has a
genuine limiting distribution: the law of the random Euler product
prod_{p=1(3)} f_p(U_p) with independent uniform residues.  Moments are
derived Euler products:
  E[f_p]   = ((p-1)/(3p))(1-3/p)/(1-1/p) + (1/p) + (rest)/(1-1/p)...
computed exactly per p below.  Verified against the empirical family
a <= AMAX, plus a uniformity z-profile of prime counts over a <= AU
at N (the family-level analogue of C1(i) in the cubic world).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

PMAX = int(float(sys.argv[1])) if len(sys.argv) > 1 else 100_000
AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300
AU = int(sys.argv[3]) if len(sys.argv) > 3 else 60
N = int(float(sys.argv[4])) if len(sys.argv) > 4 else 2 * 10**5

cubes = {i ** 3 for i in range(1, 20)}
As = [a for a in range(1, AMAX + 1) if a not in cubes]
p1 = [int(p) for p in primes_up_to(PMAX) if p % 3 == 1]

with Timer("derived moments"):
    lm = l2 = 0.0
    for p in p1:
        f3 = (1 - 3.0 / p) / (1 - 1.0 / p)   # -a a nonzero cube: omega=3
        f1 = 1.0                              # p | a: omega=1
        f0 = 1.0 / (1 - 1.0 / p)              # else: omega=0
        pcube = (p - 1) / (3.0 * p)
        pdiv = 1.0 / p
        prest = 1 - pcube - pdiv
        m1 = pcube * f3 + pdiv * f1 + prest * f0
        m2 = pcube * f3 ** 2 + pdiv * f1 ** 2 + prest * f0 ** 2
        lm += math.log(m1)
        l2 += math.log(m2)
    Cbar, C2bar = math.exp(lm), math.exp(l2)
    sd = math.sqrt(max(C2bar - Cbar ** 2, 0))
print("derived: mean C(a) = %.4f  sd = %.4f" % (Cbar, sd))

with Timer("empirical constants a <= %d" % AMAX):
    Cs = []
    for a in As:
        lv = 0.0
        for p in p1:
            if a % p == 0:
                om = 1
            else:
                om = 3 if pow((-a) % p, (p - 1) // 3, p) == 1 else 0
            lv += math.log1p(-om / p) - math.log1p(-1.0 / p)
        Cs.append(math.exp(lv))
    Cs = np.array(Cs)
print("empirical (%d values): mean = %.4f  sd = %.4f   (ratios %.4f / %.4f)"
      % (len(Cs), Cs.mean(), Cs.std(), Cs.mean() / Cbar, Cs.std() / sd))

with Timer("uniformity profile a <= %d at N = %.0e" % (AU, N)):
    zs = []
    for a in [x for x in range(1, AU + 1) if x not in cubes]:
        res = count_poly_primes([[a, 0, 0, 1]], N, presieve_to=30_000,
                                checkpoints=(N,))
        obs = res["at"][N]
        pred = Cs[As.index(a)] * bh_integral([[a, 0, 0, 1]], N)
        zs.append(zscore(obs, pred))
    zs = np.array(zs)
print("uniformity: mean z %+.2f  sd %.2f  max|z| %.2f over %d shifts"
      % (zs.mean(), zs.std(), np.abs(zs).max(), len(zs)))
save_result("c02b", {"conjecture": "cubic family: C(a) has a limiting distribution with derived "
                                   "Euler-product moments; count uniform over a",
                     "PMAX": PMAX, "AMAX": AMAX,
                     "derived_mean": Cbar, "derived_sd": sd,
                     "empirical_mean": float(Cs.mean()), "empirical_sd": float(Cs.std()),
                     "z_mean": float(zs.mean()), "z_sd": float(zs.std()),
                     "z_max": float(np.abs(zs).max()), "n_uniformity_shifts": len(zs)})
