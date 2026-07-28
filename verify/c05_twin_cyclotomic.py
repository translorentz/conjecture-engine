"""C05 (replacement) -- Twin cyclotomic bases: Phi_3(n) and Phi_3(n+1)
both prime, i.e. consecutive integers whose length-3 repunits are both
prime.  f1 = n^2+n+1, f2 = (n+1)^2+(n+1)+1 = n^2+3n+3.

Conjecture: #{n <= N} ~ C * int dt/(log f1 log f2), C = BH(f1, f2).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

POLYS = [[1, 1, 1], [3, 3, 1]]
N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7

with Timer("singular series"):
    C, C_early = bateman_horn_constant(POLYS, pmax=2_000_000)
print("C = %.6f  (truncation wobble %.2e)" % (C, abs(C - C_early)))

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

save_result("c05_pair", {"conjecture": "Phi_3(n), Phi_3(n+1) both prime (twin repunit bases)",
                    "constant_C": C, "constant_wobble": abs(C - C_early),
                    "first_solutions": res["first"], "table": rows})
