"""C04 -- Prime quintuplet with pattern (0, 2, 6, 12, 14).

An admissible 5-tuple distinct from the classical (0,2,6,8,12)/(0,4,6,10,12)
patterns.  Hardy-Littlewood: #{n <= x} ~ C4 * int_2^x dt/(log t)^5.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

H = (0, 2, 6, 12, 14)
X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9

with Timer("HL constant"):
    C = hl_tuple_constant(H, pmax=2_000_000)
print("C4 = %.6f" % C)

span = max(H)
cps = [10**k for k in range(4, len(str(X)))]
if cps[-1] != X:
    cps.append(X)
counts_at = {}
total = 0
first = []
carry = np.zeros(0, dtype=bool)
carry_lo = 0
with Timer("segmented sweep"):
    for lo, hi, seg in seg_sieve(X + span + 1, seg_size=1 << 24):
        comb = np.concatenate([carry, seg])
        base = carry_lo
        m = np.ones(len(comb) - span, dtype=bool)
        for h in H:
            m &= comb[h: len(comb) - span + h]
        idx = np.nonzero(m)[0] + base
        idx = idx[idx <= X]
        total += len(idx)
        if len(first) < 10 and len(idx):
            first.extend(int(v) for v in idx[:10 - len(first)])
        for x in cps:
            if base <= x < hi:
                counts_at[x] = counts_at.get(x, 0) + int(np.sum(idx <= x))
            elif x >= hi:
                counts_at[x] = counts_at.get(x, 0) + len(idx)
        carry = seg[-span:].copy()
        carry_lo = hi - span

rows = []
prev_obs, prev_pred = 0, 0.0
for x in cps:
    obs = counts_at[x]
    pred = C * li_k(x, 5)
    d_obs, d_pred = obs - prev_obs, pred - prev_pred
    rows.append({"N": x, "obs": obs, "pred": round(pred, 1),
                 "ratio": round(obs / pred, 4), "z": round(zscore(obs, pred), 2),
                 "increment_obs": d_obs, "increment_pred": round(d_pred, 1),
                 "increment_ratio": round(d_obs / d_pred, 4)})
    print("x=%.0e  obs=%d  pred=%.1f  ratio=%.4f  incr_ratio=%.4f  z=%+.2f" %
          (x, obs, pred, obs / pred, d_obs / d_pred, zscore(obs, pred)))
    prev_obs, prev_pred = obs, pred

save_result("c04", {"conjecture": "quintuplets n+(0,2,6,12,14) all prime",
                    "constant_C": C, "first_solutions": first, "table": rows})
