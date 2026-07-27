"""C08 (replacement) -- the null-mechanism control race.

For the quadratic twin pairs (n^2+1, n^2+3), square contamination is
ALGEBRAICALLY IMPOSSIBLE: n^2+1 = q^2 has no solutions with n >= 1, and
n^2+3 = q^2 only at (n,q) = (1,2).  So, in contrast to C21/C25, every
residue-class race over these pairs is conjectured DRIFTLESS at the
contamination scale sqrt(x)/log^2 x: the normalized difference between
the symmetric classes n = 1 and n = 4 (mod 5) has zero logarithmic
mean, wandering as a fair random walk (arcsine-law leadership).
This is the negative control completing the mechanism family.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

POLYS = [[1, 0, 1], [3, 0, 1]]
N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7

with Timer("solutions"):
    PB = 30_000
    alive = np.ones(N + 1, dtype=bool)
    alive[:2] = False
    for p in primes_up_to(PB):
        p = int(p)
        for c in POLYS:
            for r in poly_roots_mod(c, p):
                start = int(r)
                while poly_eval_int(c, start) <= p and start <= N:
                    start += p
                alive[start:: p] = False
    sols = np.array([n for n in np.nonzero(alive)[0]
                     if is_prime(poly_eval_int(POLYS[0], int(n)))
                     and is_prime(poly_eval_int(POLYS[1], int(n)))],
                    dtype=np.int64)
print("pairs found:", len(sols))

r = sols % 5
c1 = np.cumsum(r == 1)
c4 = np.cumsum(r == 4)
D = (c1 - c4).astype(float)
idx = np.arange(1, len(sols) + 1)
w = 1.0 / idx  # logarithmic-in-count weights
logmean = float(np.sum(w * D / np.sqrt(np.maximum(c1 + c4, 1)))) / float(np.sum(w))
lead = float(np.sum(w * (D > 0)) / np.sum(w))
print("final classes: n=1(5): %d, n=4(5): %d, D=%+d" % (c1[-1], c4[-1], D[-1]))
print("log-mean of normalized drift D/sqrt(count): %+.4f (conjecture: -> 0)" % logmean)
print("weighted lead fraction {D>0}: %.4f (arcsine wandering, no limit claimed)" % lead)
save_result("c08", {"conjecture": "null-mechanism race: quadratic twin pairs have no square "
                                  "contamination; class race n=1 vs n=4 (mod 5) is driftless",
                    "N": N, "n_pairs": int(len(sols)),
                    "final_c1": int(c1[-1]), "final_c4": int(c4[-1]),
                    "normalized_drift_logmean": logmean,
                    "lead_fraction": lead})
