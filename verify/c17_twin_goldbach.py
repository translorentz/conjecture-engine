"""C17 -- Goldbach with twin-prime members.

T = {p : p or p+-2 is also prime, p prime} (members of twin pairs).
Expected representations of even n as t1 + t2 ~ c(n) * n / log^4 n, strongly
divergent => finite exceptions.  Conjecture: the classical list (A007534,
largest element 4208) is complete; every even n >= 4210 is a sum of two
members of twin-prime pairs.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8

with Timer("sieve"):
    P = sieve_bool(N + 2)
T = np.zeros(N + 1, dtype=bool)
T[: N + 1] = P[: N + 1]
mask = np.zeros(N + 1, dtype=bool)
mask[: N - 1] = P[2: N + 1]          # p+2 prime
mask[2: N + 1] |= P[: N - 1]         # p-2 prime
T &= mask
t_list = np.nonzero(T)[0].astype(np.int64)
print("twin-pair members up to N:", len(t_list))

with Timer("existence sweep"):
    todo = np.arange(4, N + 1, 2, dtype=np.int64)
    exceptions = []
    i = 0
    while len(todo) and i < len(t_list):
        t = int(t_list[i])
        rem = todo - t
        dead = rem < 3
        ok = ~dead & T[np.clip(rem, 0, N)]
        exceptions.extend(int(v) for v in todo[dead])
        todo = todo[~ok & ~dead]
        i += 1
    exceptions.extend(int(v) for v in todo)
exceptions.sort()
print("exceptions (%d): %s" % (len(exceptions), exceptions))

save_result("c17", {"conjecture": "every even n>=4210 is a sum of two twin-pair members",
                    "N": N, "exceptions": exceptions,
                    "largest_exception": exceptions[-1] if exceptions else None})
