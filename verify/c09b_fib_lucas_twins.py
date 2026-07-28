"""C09' -- Fibonacci-Lucas twins: F_p and L_p simultaneously prime.

Prime divisors of F_p (p prime) have rank of apparition exactly p;
prime divisors of L_p have rank exactly 2p.  The two screening pools
are therefore DISJOINT -- the structural reason the two primality
events carry no shared local correlation (the analogue of C10(iii)'s
deterministic-screening argument).  Each event has probability
~ c log p / p (c = e^gamma/log phi screening scale), so the joint sum
converges: finitely many Fibonacci-Lucas twins.  Note F_p L_p = F_{2p}.
NO completeness claim is made: the novelty audit found OEIS A080327
already catalogues the object INCLUDING the index 148091 (F PRP, L
proven), which refutes the naive tail accounting (mass ~1.6e-3 beyond
1e4) by three orders of magnitude in index -- the calibration lesson
is now part of the conjecture (clause iii in the paper).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

PMAX = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10_000
EG = math.exp(EULER_GAMMA)
LPHI = math.log((1 + math.sqrt(5)) / 2)


def fib_lucas(n):
    """(F_n, L_n) by fast doubling."""
    def fd(k):
        if k == 0:
            return (0, 1)
        a, b = fd(k >> 1)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k & 1:
            return (d, c + d)
        return (c, d)
    F, F1 = fd(n)
    return F, 2 * F1 - F


fp, lp, joint = [], [], []
with Timer("scan p <= %d" % PMAX):
    for p in primes_up_to(PMAX):
        p = int(p)
        F, L = fib_lucas(p)
        fprime = is_prime(F)
        lprime = is_prime(L)
        if fprime:
            fp.append(p)
        if lprime:
            lp.append(p)
        if fprime and lprime:
            joint.append(p)
            print("  Fibonacci-Lucas twin at p =", p)

# model tail beyond PMAX: sum over primes of (c log p / p)^2, c = e^g/log phi
tail = 0.0
for q in primes_up_to(10**6):
    q = int(q)
    if q > PMAX:
        tail += (EG * math.log(q) / (q * LPHI)) ** 2 / math.log(q)  # dp measure
# crude continuum tail beyond 1e6
tail += (EG / LPHI) ** 2 * (math.log(10**6) + 1) / 10**6
print("F_p prime for p in:", fp)
print("L_p prime for p in:", lp)
print("joint (Fibonacci-Lucas twins):", joint)
print("expected further twins beyond %d: %.3e" % (PMAX, tail))
save_result("c09b", {"conjecture": "finitely many p with F_p and L_p both prime; "
                                   "disjoint rank pools (p vs 2p) justify joint independence",
                     "PMAX": PMAX, "fp_primes": fp, "lp_primes": lp,
                     "joint": joint, "expected_further": tail})
