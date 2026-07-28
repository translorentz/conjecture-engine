"""C03 -- Arithmetic-progression prime chain: p, 2p-1, 3p-2 all prime.

These three numbers form a 3-term AP with common difference p-1
(first instance 3, 5, 7).  Bateman-Horn for {x, 2x-1, 3x-2}:
#{p <= x} ~ C3 * int dt/(log t * log(2t-1) * log(3t-2)).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

POLYS = [[0, 1], [-1, 2], [-2, 3]]
N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 3 * 10**8

with Timer("singular series"):
    C, C_early = bateman_horn_constant(POLYS, pmax=2_000_000)
print("C3 = %.6f  (truncation wobble %.2e)" % (C, abs(C - C_early)))

with Timer("sieve to 3N"):
    P = sieve_bool(3 * N)
with Timer("chain count"):
    p = np.nonzero(P[: N + 1])[0].astype(np.int64)
    good = p[P[2 * p - 1] & P[3 * p - 2]]

cps = [10**k for k in range(2, len(str(N)))]
if cps[-1] != N:
    cps.append(N)
rows = []
for x in cps:
    obs = int(np.searchsorted(good, x, side="right"))
    pred = C * bh_integral(POLYS, x)
    rows.append({"N": x, "obs": obs, "pred": round(pred, 1),
                 "ratio": round(obs / pred, 4), "z": round(zscore(obs, pred), 2)})
    print("N=%.0e  obs=%d  pred=%.1f  ratio=%.4f  z=%+.2f" %
          (x, obs, pred, obs / pred, zscore(obs, pred)))

save_result("c03", {"conjecture": "p, 2p-1, 3p-2 all prime (AP chain)",
                    "constant_C": C, "constant_wobble": abs(C - C_early),
                    "first_solutions": [int(v) for v in good[:10]], "table": rows})
