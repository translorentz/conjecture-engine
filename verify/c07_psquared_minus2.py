"""C07 -- Downward companion: p and p^2-2 both prime.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

POLYS = [[0, 1], [-2, 0, 1]]
N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7

with Timer("singular series"):
    C, C_early = bateman_horn_constant(POLYS, pmax=2_000_000)
print("C07: C = %.6f  (truncation wobble %.2e)" % (C, abs(C - C_early)))

cps = [10**k for k in range(3, len(str(N)))]
if cps[-1] != N:
    cps.append(N)
with Timer("count"):
    res = count_poly_primes(POLYS, N, presieve_to=100_000, checkpoints=cps)

rows = []
for x in cps:
    pred = C * bh_integral(POLYS, x)
    obs = res["at"][x]
    rows.append({"N": x, "obs": obs, "pred": round(pred, 1),
                 "ratio": round(obs / pred, 4), "z": round(zscore(obs, pred), 2)})
    print("N=%.0e  obs=%d  pred=%.1f  ratio=%.4f  z=%+.2f" %
          (x, obs, pred, obs / pred, zscore(obs, pred)))

save_result("c07", {"conjecture": "p and p^2-2 both prime",
                    "constant_C": C, "constant_wobble": abs(C - C_early),
                    "first_solutions": res["first"], "table": rows})
