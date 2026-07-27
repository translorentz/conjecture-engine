"""C25 -- Consecutive primes mod 3 (Lemke Oliver-Soundararajan instance).

Among consecutive primes p, p' > 3, let s(x) be the fraction with
p = p' (mod 3).  Random model says 1/2; the HL prime-pair correlations
predict a slowly-vanishing deficit.  Conjecture:
    1/2 - s(x) = (c + o(1)) * log log x / log x   with c in (0, infty),
and the deficit splits evenly between (1,1) and (2,2) patterns.
Verification to 10^9: measure c-hat(x) at checkpoints; check stability.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9

pair_counts = np.zeros(4, dtype=np.int64)  # index 2*(r-1)+(r'-1) for r,r' in {1,2}
snap = []
last_r = None
with Timer("sweep"):
    for lo, hi, seg in seg_sieve(X, seg_size=1 << 24):
        pos = np.nonzero(seg)[0] + lo
        pos = pos[pos > 3]
        if len(pos) == 0:
            continue
        r = (pos % 3).astype(np.int64)
        if last_r is not None:
            r = np.concatenate([[last_r], r])
        idx = 2 * (r[:-1] - 1) + (r[1:] - 1)
        pair_counts += np.bincount(idx, minlength=4)
        last_r = int(r[-1])
        snap.append((hi, *pair_counts))

rows = []
for hi, n11, n12, n21, n22 in [snap[i] for i in
                               sorted({min(len(snap) - 1, int(len(snap) * f))
                                       for f in (0.001, 0.01, 0.1, 0.3, 1.0)})]:
    tot = n11 + n12 + n21 + n22
    s = (n11 + n22) / tot
    chat = (0.5 - s) * math.log(hi) / math.log(math.log(hi))
    rows.append({"x": int(hi), "same_fraction": round(s, 5),
                 "c_hat": round(chat, 4),
                 "n11_over_n22": round(n11 / n22, 4)})
    print("x=%.1e  same=%.5f  c_hat=%.4f  n11/n22=%.4f"
          % (hi, s, chat, n11 / n22))

n11, n12, n21, n22 = (int(v) for v in pair_counts)
save_result("c25", {"conjecture": "1/2 - s(x) ~ c log log x/log x, c>0; "
                                  "deficit symmetric in (1,1) vs (2,2)",
                    "X": X, "counts": {"11": n11, "12": n12, "21": n21, "22": n22},
                    "table": rows})
