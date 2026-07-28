"""C06 (replacement) -- The alternating cyclotomic chain.

The naive iterated chain {p, Phi_3(p), Phi_3(Phi_3(p))} is INADMISSIBLE:
if p = 2 (mod 3) then u = Phi_3(p) = 1 (mod 3), so 3 | Phi_3(u) always
(our own admissibility engine caught this at design time; the failure is
recorded as part of the statement's provenance).  The viable length-3
chain alternates the sixth cyclotomic:

    p,  u = Phi_3(p) = p^2+p+1,  Phi_6(u) = u^2-u+1,

i.e. the Bateman-Horn system {x, x^2+x+1, x^4+2x^3+2x^2+x+1} (the
quartic is irreducible).  First chains: (2,7,43), (3,13,157).

Conjecture: infinitely many such chains, with count ~ C * I(x),
C the singular series of the system.  This is the repunit analogue of a
Cunningham chain: base p, its length-3 repunit, then (u^3+1)/(u+1).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

POLYS = [[0, 1], [1, 1, 1], [1, 1, 2, 2, 1]]
N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7

with Timer("singular series (brute force)"):
    C, C_early = bateman_horn_constant(POLYS, pmax=100_000, brute_below=100_001)
print("C = %.5f (wobble %.1e)" % (C, abs(C - C_early)))

cps = [10**k for k in range(3, len(str(N)))]
if cps[-1] != N:
    cps.append(N)
with Timer("count"):
    res = count_poly_primes(POLYS, N, presieve_to=30_000, checkpoints=cps)
rows = []
for x in cps:
    pred = C * bh_integral(POLYS, x)
    obs = res["at"][x]
    rows.append({"N": x, "obs": obs, "pred": round(pred, 1),
                 "ratio": round(obs / pred, 4), "z": round(zscore(obs, pred), 2)})
    print("N=%.0e obs=%d pred=%.1f ratio=%.4f z=%+.2f"
          % (x, obs, pred, obs / pred, zscore(obs, pred)))
save_result("c06", {"conjecture": "alternating cyclotomic chain p, Phi3(p), Phi6(Phi3(p)) all prime",
                    "constant_C": C, "constant_wobble": abs(C - C_early),
                    "first_solutions": res["first"], "table": rows})
