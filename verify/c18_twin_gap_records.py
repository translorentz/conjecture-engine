"""C18 -- Cramer-type record gaps between twin-prime pairs.

Twin starts have density ~ 2C2/log^2 t; a Cramer model for that thinned
process predicts record gaps G_t(x) of size ~ log^3 x / (2C2), i.e.
    limsup G_t(x) / log^3 x = 1/(2C2) = 0.7573...  (first order; a
Granville-type local correction may lift the constant -- see the memo).
Verification: track records to 10^9 and the normalized ratio.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9

records = []   # (gap, at_twin_start)
best = 0
last = None
cps = [10**k for k in range(5, len(str(X)))]
if cps[-1] != X:
    cps.append(X)
cp_stats = {}
carry = np.zeros(2, dtype=bool)
carry_lo = 0
with Timer("sweep"):
    for lo, hi, seg in seg_sieve(X + 3, seg_size=1 << 24):
        comb = np.concatenate([carry, seg]) if lo else seg
        base = carry_lo if lo else 0
        starts = np.nonzero(comb[:-2] & comb[2:])[0] + base
        if len(starts) == 0:
            carry, carry_lo = seg[-2:].copy(), hi - 2
            continue
        if last is not None:
            starts_full = np.concatenate([[last], starts])
        else:
            starts_full = starts
        gaps = np.diff(starts_full)
        big = np.nonzero(gaps > best)[0]
        for i in big:
            if gaps[i] > best:
                best = int(gaps[i])
                records.append((best, int(starts_full[i])))
        last = int(starts[-1])
        carry, carry_lo = seg[-2:].copy(), hi - 2

print("record twin-pair gaps (gap, from twin start):")
for g, p in records[-12:]:
    print("  G=%6d  after twin %10d   G/log^3 = %.4f" % (g, p, g / math.log(p) ** 3))
rows = []
for x in cps:
    b = max((g for g, p in records if p <= x), default=0)
    rows.append({"x": x, "record": b, "ratio_log3": round(b / math.log(x) ** 3, 4)})
    print("x=%.0e  record=%d  record/log^3 x = %.4f  (model 1/(2C2)=%.4f)"
          % (x, b, b / math.log(x) ** 3, 1 / TWIN_2C2))

save_result("c18", {"conjecture": "limsup G_twin(x)/log^3 x = 1/(2C2)",
                    "model_constant": 1 / TWIN_2C2,
                    "records": records, "checkpoints": rows})
