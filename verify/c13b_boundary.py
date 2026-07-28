"""C13' -- the boundary-factorization principle.

THEOREM (elementary): for any F in Z[x], (m-j) | F(m)-F(j).  Hence if
F(m)-F(j) is prime then |m-j| = 1, or |m-j| itself is that prime and
the cofactor is +-1 -- for deg F >= 2 an equation defining a curve
with finitely many integer points.  So every representation problem
F(m) = p + F(j) collapses, up to a finite exceptional set, to the
boundary polynomial D_F(m) = F(m) - F(m-1), and the ladder is then
governed by the trichotomy:
  (dead-parity)  D_F always even (e.g. F = x^3 + cx, c odd);
  (dead-3adic)   3 | D_F always (e.g. F = x^3 + cx, c = 2 mod 3, c even);
  (BH lane)      D_F admissible: Bateman-Horn applies (c = 0, 4 mod 6).
This script (1) verifies the collapse for sample F on m <= 1500 and
finds the exceptional pairs; (2) verifies the trichotomy for
F = x^3 + cx, c <= 12; (3) counts the BH lanes c = 4, 6... wait c=6:
D = 3m^2-3m+7, 7 mod 3 = 1, admissible -- counts c = 4 and 6 lanes at
M = 1e6 against their Bateman-Horn constants.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

M = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**6

def F_of(c):
    return lambda x: x ** 3 + c * x

with Timer("collapse check"):
    # algebraic emptiness: F(m)-F(j) prime with m-j >= 2 forces the
    # cofactor m^2+mj+j^2+c = 1, impossible for m > j >= 1, c >= 0 --
    # so the exceptional set is EMPTY for this family; brute-confirm:
    exc = {}
    for c in (0, 4, 6):
        F = F_of(c)
        bad = [(m, j, F(m) - F(j)) for m in range(2, 301)
               for j in range(1, m - 1) if is_prime(F(m) - F(j))]
        exc[c] = bad
        print("F = x^3 + %dx: non-boundary prime differences m<=300: %s"
              % (c, bad or "none (algebraically empty)"))

with Timer("trichotomy for x^3 + cx"):
    tri = {}
    for c in range(0, 13):
        D = [1 + c, -3, 3]           # D_F(m) = 3m^2 - 3m + 1 + c
        if (1 + c) % 2 == 0:
            tri[c] = "dead-parity"
        elif (1 + c) % 3 == 0:
            tri[c] = "dead-3adic"
        else:
            tri[c] = "BH-lane"
    print("trichotomy:", tri)
    # confirm dead branches numerically
    for c, kind in tri.items():
        if kind != "BH-lane":
            hits = [m for m in range(2, 5000)
                    if is_prime(3 * m * m - 3 * m + 1 + c)]
            assert not hits, (c, hits[:3])

out = {}
with Timer("BH lanes c = 4, 6"):
    for c in (4, 6):
        D = [1 + c, -3, 3]
        C, Ce = bateman_horn_constant([D], pmax=500_000)
        res = count_poly_primes([D], M, presieve_to=50_000, checkpoints=(M,))
        obs = res["at"][M]
        pred = C * bh_integral([D], M)
        print("c=%d: C=%.5f  obs=%d  pred=%.1f  ratio=%.4f  z=%+.2f"
              % (c, C, obs, pred, obs / pred, zscore(obs, pred)))
        out["c%d" % c] = {"C": C, "obs": obs, "pred": pred,
                          "z": zscore(obs, pred)}
save_result("c13b", {"conjecture": "boundary-factorization principle: collapse to the boundary "
                                   "lane + dead-parity/dead-3adic/BH trichotomy for x^3+cx",
                     "M": M, "exceptional_pairs": {str(k): v[:20] for k, v in exc.items()},
                     "trichotomy": tri, **out})
