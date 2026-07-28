"""C10 (replacement) -- Primorial twins: p# - 1 and p# + 1 both prime.

Individually each event has probability ~ e^gamma log p / p
(Caldwell-Gallot); under independence the JOINT event has probability
~ (e^gamma log p / p)^2, whose sum over primes CONVERGES.  Borel-Cantelli
therefore predicts only finitely many primorial twins -- the suite's
exemplar of the convergent side of the accounting dichotomy.

Conjecture: the set of primes p with p#-1 and p#+1 both prime is finite,
and the list found below (p <= 4000) is complete; the model-expected
number of further examples is the (tiny) tail sum reported.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 4000
EG = math.exp(EULER_GAMMA)

twins, plus, minus = [], [], []
primo = 1
with Timer("PRP scan"):
    for p in primes_up_to(X):
        p = int(p)
        primo *= p
        up = is_prime(primo + 1)
        dn = is_prime(primo - 1)
        if up:
            plus.append(p)
        if dn:
            minus.append(p)
        if up and dn:
            twins.append(p)
            print("  primorial twin at p =", p)
print("p#+1 primes (p<=%d): %s" % (X, plus))
print("p#-1 primes (p<=%d): %s" % (X, minus))
print("primorial twins:", twins)

# Borel-Cantelli tail: sum over p > X of (e^gamma log p / p)^2
tail = 0.0
for p in primes_up_to(10**7):
    p = int(p)
    if p > X:
        tail += (EG * math.log(p) / p) ** 2
# integral tail beyond 1e7: int (e^g log t/t)^2 dpi(t) ~ int e^{2g} log t/t^2 dt
t = 10**7
tail += (EG ** 2) * (math.log(t) + 1) / t
print("model-expected further twins beyond p=%d: %.2e" % (X, tail))

save_result("c10_primorial", {"conjecture": "finitely many primorial twins (p#-1, p#+1 both prime); "
                                  "list complete",
                    "X": X, "twins": twins, "plus": plus, "minus": minus,
                    "expected_further": tail})
