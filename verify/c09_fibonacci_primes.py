"""C09 -- Fibonacci prime counting (Lenstra-Pomerance-Wagstaff analogue).

Every prime factor q of F_p (p prime, p != 5) satisfies q = +-1 (mod p),
exactly the screening structure behind the LPW Mersenne heuristic.
Conjecture: #{p <= x : p prime, F_p prime} ~ (e^gamma / log phi) * log x.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**4
PHI = (1 + 5 ** 0.5) / 2
SLOPE = math.exp(EULER_GAMMA) / math.log(PHI)
print("predicted slope e^gamma/log(phi) = %.4f" % SLOPE)


def fib_pair(n):
    """(F_n, F_{n+1}) by fast doubling."""
    if n == 0:
        return 0, 1
    a, b = fib_pair(n >> 1)
    c = a * ((b << 1) - a)
    d = a * a + b * b
    return (d, c + d) if n & 1 else (c, d)


hits = []
with Timer("PRP scan"):
    for p in primes_up_to(X):
        p = int(p)
        if is_prime(fib_pair(p)[0]):
            hits.append(p)
            print("  F_%d is prime" % p)

rows = []
for x in [c for c in (10**2, 10**3) if c < X] + [X]:
    obs = sum(1 for h in hits if h <= x)
    pred = SLOPE * math.log(x)
    rows.append({"x": x, "obs": obs, "pred": round(pred, 1),
                 "ratio": round(obs / pred, 3), "z": round(zscore(obs, pred), 2)})
    print("x=%.0e  obs=%d  pred=%.1f  z=%+.2f" % (x, obs, pred, zscore(obs, pred)))

save_result("c09", {"conjecture": "#{p<=x: F_p prime} ~ (e^gamma/log phi) log x",
                    "slope_predicted": SLOPE, "hits": hits, "table": rows})
