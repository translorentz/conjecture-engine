"""C12 -- Factorial primes n! + 1.

n! + 1 is coprime to every prime <= n (Mertens boost e^gamma log n against
size log n! ~ n log n), giving P(n!+1 prime) ~ e^gamma / n.
Conjecture: #{n <= N : n! + 1 prime} ~ e^gamma * log N.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 700
EG = math.exp(EULER_GAMMA)

hits = []
f = 1
with Timer("PRP scan"):
    for n in range(1, N + 1):
        f *= n
        if is_prime(f + 1):
            hits.append(n)
            print("  %d! + 1 is prime" % n)

rows = []
for x in [c for c in (10**2,) if c < N] + [N]:
    obs = sum(1 for h in hits if h <= x)
    pred = EG * math.log(x)
    rows.append({"N": x, "obs": obs, "pred": round(pred, 1),
                 "ratio": round(obs / pred, 3), "z": round(zscore(obs, pred), 2)})
    print("N=%d  obs=%d  pred=%.1f  z=%+.2f" % (x, obs, pred, zscore(obs, pred)))

save_result("c12", {"conjecture": "#{n<=N: n!+1 prime} ~ e^gamma log N",
                    "slope_predicted": EG, "hits": hits, "table": rows})
