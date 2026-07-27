"""C13 -- Prime plus a positive cube.

Expected representations of n as p + k^3 (k >= 1) number ~ n^(1/3)/log n,
divergent, so exceptions should be finite (Borel-Cantelli).
Conjecture: the exception set found below is complete.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8

with Timer("sieve"):
    P = sieve_bool(N)
rep = np.zeros(N + 1, dtype=bool)
with Timer("shift union"):
    k = 1
    while k ** 3 < N:
        c = k ** 3
        rep[c:] |= P[: N + 1 - c]
        k += 1

exc = np.nonzero(~rep[2:])[0] + 2
exc = [int(e) for e in exc]
print("exceptions (%d):" % len(exc), exc[:60], "..." if len(exc) > 60 else "")
per_decade = {}
for e in exc:
    per_decade[len(str(e))] = per_decade.get(len(str(e)), 0) + 1
print("exceptions by number of digits:", per_decade)

# Borel-Cantelli with local (mod 2, 3, 7, 9) corrections:
# P(n unrepresented) = exp(-s(n)),  s(n) = sum_k m(n-k^3)/log(n-k^3),
# m(v) = prod_{p in {2,3,7}} [p/(p-1) if p !| v else 0] * (small-p singular factor)
def log_p_unrep(n):
    """log P(n unrepresentable) = sum_k log(1 - m(v)/log v), v = n-k^3."""
    s = 0.0
    k = 1
    while k ** 3 < n - 2:
        v = n - k ** 3
        if v % 2 and v % 3 and v % 7:
            q = min((2.0 * 1.5 * 7.0 / 6.0) / math.log(v), 0.95)
            s += math.log1p(-q)
        k += 1
    return s


def expected_exceptions(lo, hi, nsamp=4000):
    """Model-expected number of unrepresentable n in [lo, hi] by sampling."""
    rng = np.random.default_rng(20260727)
    xs = rng.integers(lo, hi, nsamp)
    return float(np.mean([math.exp(log_p_unrep(int(x))) for x in xs])) * (hi - lo)


with Timer("model"):
    decade_model = {}
    lo = 10
    while lo < N:
        hi = min(10 * lo, N)
        decade_model["%.0e..%.0e" % (lo, hi)] = round(expected_exceptions(lo, hi), 1)
        lo = hi
    te = expected_exceptions(N, 10 * N)
print("model-expected exceptions per decade:", decade_model)
print("model-expected further exceptions in [N, 10N]: %.3g" % te)

save_result("c13", {"conjecture": "finite exception set for n = p + k^3, k>=1",
                    "N": N, "exceptions": exc, "n_exceptions": len(exc),
                    "largest_exception": exc[-1] if exc else None,
                    "by_digits": per_decade,
                    "expected_more_in_next_decade": te})
