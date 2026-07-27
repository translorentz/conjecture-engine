"""C15 -- Goldbach in the 3 (mod 4) class.

For n = 2 (mod 4), p + q = n with p,q odd forces p = q (mod 4), so the
representations split into a (1,1) and a (3,3) family.  Conjecture:
(a) every n = 2 (mod 4), n >= 6, is p + q with p = q = 3 (mod 4);
(b) ordered representation count R3(n) ~ (1/2) S(n) * int dt/(log t log(n-t)),
    S(n) the Goldbach singular series.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8

with Timer("sieve"):
    P = sieve_bool(N)
P3 = np.zeros_like(P)
P3[3::4] = P[3::4]
p3_list = np.nonzero(P3)[0].astype(np.int64)
print("primes = 3 (mod 4) up to N:", len(p3_list))

with Timer("existence sweep"):
    todo = np.arange(6, N + 1, 4, dtype=np.int64)
    exceptions = []
    i = 0
    while len(todo) and i < len(p3_list):
        t = int(p3_list[i])
        rem = todo - t
        ok = (rem >= 3) & P3[np.clip(rem, 0, N)]
        # numbers whose remaining partner would be < 3 have exhausted all t
        dead = rem < 3
        exceptions.extend(int(v) for v in todo[dead])
        todo = todo[~ok & ~dead]
        i += 1
    exceptions.extend(int(v) for v in todo)
print("exceptions:", exceptions if exceptions else "none")

# representation-count check at sampled n
def goldbach_S(n):
    s = TWIN_2C2
    m = n
    while m % 2 == 0:
        m //= 2
    p = 3
    while p * p <= m:
        if m % p == 0:
            s *= (p - 1) / (p - 2)
            while m % p == 0:
                m //= p
        p += 2
    if m > 1:
        s *= (m - 1) / (m - 2)
    return s


def pred_R3(n, npts=20001):
    t = np.linspace(3.0, n - 3.0, npts)
    return 0.5 * goldbach_S(n) * float(np.trapezoid(1 / (np.log(t) * np.log(n - t)), t))


samples = []
sample_ns = sorted({n for n in
                    (10**6 + 2, 10**6 + 6, 10**7 + 2, 10**7 + 6, N - 2, N - 6)
                    if 100 <= n <= N - 2})
for n in sample_ns:
    while n % 4 != 2:
        n -= 2
    if True:
        rem = n - p3_list[p3_list <= n - 3]
        obs = int(np.count_nonzero(P3[rem]))
        pred = pred_R3(n)
        samples.append({"n": int(n), "obs": obs, "pred": round(pred, 1),
                        "ratio": round(obs / pred, 4)})
        print("n=%d  R3=%d  pred=%.1f  ratio=%.4f" % (n, obs, pred, obs / pred))

save_result("c15", {"conjecture": "every n=2(4)>=6 is a sum of two primes =3(4); "
                                  "R3(n) ~ (1/2)S(n)*I(n)",
                    "N": N, "exceptions": exceptions, "samples": samples})
