"""C10 -- Primorial primes p# + 1.

p# + 1 is coprime to every prime q <= p, so the Mertens boost e^gamma log p
applies against size log(p#) = theta(p) ~ p.
Conjecture: #{p <= x : p# + 1 prime} ~ e^gamma * log x.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 4000
EG = math.exp(EULER_GAMMA)

hits = []
theta = 0.0
primo = 1
with Timer("PRP scan"):
    for p in primes_up_to(X):
        p = int(p)
        primo *= p
        if is_prime(primo + 1):
            hits.append(p)
            print("  %d# + 1 is prime" % p)

rows = []
for x in [c for c in (10**2, 10**3) if c < X] + [X]:
    obs = sum(1 for h in hits if h <= x)
    pred = EG * math.log(x)
    rows.append({"x": x, "obs": obs, "pred": round(pred, 1),
                 "ratio": round(obs / pred, 3), "z": round(zscore(obs, pred), 2)})
    print("x=%.0e  obs=%d  pred=%.1f  z=%+.2f" % (x, obs, pred, zscore(obs, pred)))

save_result("c10", {"conjecture": "#{p<=x: p#+1 prime} ~ e^gamma log x",
                    "slope_predicted": EG, "hits": hits, "table": rows})
