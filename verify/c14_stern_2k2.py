"""C14 -- Stern-type representation: odd n = p + 2k^2, k >= 1.

Expected representations ~ sqrt(n/2)/log n, divergent => finitely many
exceptions.  Conjecture: the exception list found below (classically
1, 3, 17, 137, 227, 977, 1187, 5777, 5993) is complete; 5993 is the
largest odd number not of the form p + 2k^2.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8

with Timer("sieve"):
    P = sieve_bool(N)
# odd-indexed views: Podd[j] <-> 2j+1
Podd = P[1::2].copy()
del P
M = len(Podd)
rep = np.zeros(M, dtype=bool)
with Timer("shift union"):
    k = 1
    while 2 * k * k < N:
        s = k * k  # shift in odd-index space
        rep[s:] |= Podd[: M - s]
        k += 1

exc = [int(2 * j + 1) for j in np.nonzero(~rep)[0]]
print("exceptions (%d):" % len(exc), exc)

save_result("c14", {"conjecture": "5993 is the largest odd n not of form p+2k^2 (k>=1)",
                    "N": N, "exceptions": exc,
                    "largest_exception": exc[-1] if exc else None})
