"""C15' -- the least Goldbach summand: exponential law and canonical
ordering deficit.

Let s(n) be the least prime p (p not dividing n) with n - p prime, and
time-change by the expected-arrivals clock

    U(n) = S(n) * sum_{p <= s(n), p !| n} 1/log(n - p),

S(n) the Goldbach singular series 2C2 prod_{r|n, r>2}(r-1)/(r-2).
Candidate laws (the Goldbach sibling of C22):
 (i)  U => Exp(1) for n log-sampled from the even numbers;
 (ii) canonical deficit: Theta_G(n) = (1 - E[U]) log n tends, in
      dyadic average, to a positive constant -- same occupancy/ordering
      family as Conjecture 22(ii).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
NSAMP = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
TWO_C2 = 1.3203236316

with Timer("sieve"):
    P = sieve_bool(X)
small_primes = [int(p) for p in primes_up_to(100_000)]

def SG(n):
    s = TWO_C2
    m = n // 2
    while m % 2 == 0:
        m //= 2
    d = 3
    while d * d <= m:
        if m % d == 0:
            s *= (d - 1) / (d - 2)
            while m % d == 0:
                m //= d
        d += 2
    if m > 2:
        s *= (m - 1) / (m - 2)
    return s

rng = np.random.default_rng(20260728)
samples = np.unique((np.exp(rng.uniform(math.log(10**6), math.log(X - 10), NSAMP))
                     .astype(np.int64) // 2) * 2)

Us, ns = [], []
with Timer("least summands over %d samples" % len(samples)):
    for n in samples:
        n = int(n)
        acc = 0.0
        U = None
        for p in small_primes:
            if n % p == 0:
                continue
            acc += 1.0 / math.log(n - p)
            if P[n - p]:
                U = SG(n) * acc
                break
        if U is not None:
            Us.append(U)
            ns.append(n)
Us = np.array(Us)
ns = np.array(ns, dtype=float)
meanU = float(Us.mean())
# KS against Exp(1)
srt = np.sort(Us)
F = 1 - np.exp(-srt)
ks = float(np.max(np.abs(F - (np.arange(1, len(srt) + 1) - 0.5) / len(srt))))
print("samples: %d   E[U] = %.4f  (Exp(1) mean 1)   KS vs Exp(1) = %.4f "
      "(sqrt(n)*KS = %.2f)" % (len(Us), meanU, ks, ks * math.sqrt(len(Us))))
rows = []
for a, b in ((1e6, 1e7), (1e7, X)):
    sel = (ns >= a) & (ns < b)
    if sel.sum() < 30:
        continue
    th = float((1 - Us[sel].mean()) * np.log(ns[sel]).mean())
    se = float(Us[sel].std() / math.sqrt(sel.sum()) * np.log(ns[sel]).mean())
    rows.append({"range": "[%.0e,%.0e)" % (a, b), "n": int(sel.sum()),
                 "Theta_G": th, "se": se})
    print("dyadic block %s: Theta_G = %.3f +- %.3f  (n=%d)"
          % (rows[-1]["range"], th, se, sel.sum()))
save_result("c15b", {"conjecture": "least Goldbach summand: U => Exp(1); canonical ordering "
                                   "deficit Theta_G > 0 (sibling of C22(ii))",
                     "X": X, "n_samples": int(len(Us)), "mean_U": meanU,
                     "KS": ks, "blocks": rows})
