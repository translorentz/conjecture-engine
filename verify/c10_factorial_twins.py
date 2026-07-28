"""C10 (replacement) -- factorial twins: n!-1 and n!+1 both prime.

The former occupant (primorial twins) turned out to be stated by Lillie
(arXiv:2110.04302), which we missed; this slot now carries the factorial
analogue, for which we found no prior statement.  Joint probability
~ (e^gamma/n)^2 by the Caldwell-Gallot single-sided laws; the sum
converges, so Borel-Cantelli predicts finitely many.

Conjecture: n = 3 is the ONLY factorial twin (5, 7 around 3! = 6), i.e.
6 is the unique number that is simultaneously n!, p#, and sandwiched by
twin primes.  Verified n <= 700; expected further examples ~ e^{2gamma}/700.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 700
EG = math.exp(EULER_GAMMA)
twins, plus, minus = [], [], []
f = 1
with Timer("PRP scan"):
    for n in range(2, N + 1):
        f *= n
        up = is_prime(f + 1)
        dn = is_prime(f - 1)
        if up: plus.append(n)
        if dn: minus.append(n)
        if up and dn:
            twins.append(n)
            print("  factorial twin at n =", n)
tail = EG * EG / N  # sum_{n>N} (e^g/n)^2 ~ e^{2g}/N
print("n!+1 primes:", plus)
print("n!-1 primes:", minus)
print("factorial twins:", twins, "| expected further: %.2e" % tail)
save_result("c10", {"conjecture": "n=3 is the only factorial twin (n!-1, n!+1 both prime)",
                    "N": N, "twins": twins, "plus": plus, "minus": minus,
                    "expected_further": tail})
