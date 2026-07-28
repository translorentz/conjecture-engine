"""C21 -- Chebyshev-type race among twin pairs mod 5.

A twin start p (p, p+2 prime, p > 5) has p mod 5 in {1, 2, 4}.  The
square-contamination mechanism of Chebyshev's bias transfers to twins
through pairs (q^2 - 2, q^2): note 3 | q^2 + 2 for every prime q > 3,
so (q^2, q^2+2) never contributes -- only upper-member squares matter.
Since q^2 = 1 or 4 (mod 5), the start q^2-2 lies in class 4 or 2, never 1.
Conjecture: pi_t(x;5,1) systematically LEADS; with
  D1(x) = pi_t(x;5,1) - (pi_t(x;5,2)+pi_t(x;5,4))/2
        = (1/2) * (1/log^2 x) * sum_{q<=sqrt x, q^2-2 prime} log q * log(q^2-2)
          + random-walk noise,
while classes 2 and 4 are symmetric.  The bias-to-noise ratio decays like
1/log x (unlike classical prime races), so leadership density < 1.
Verification to 10^9: D1 vs the mechanism prediction, and the 2-4 control.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9

counts = {1: 0, 2: 0, 4: 0}
snap = []
carry = np.zeros(2, dtype=bool)
carry_lo = 0
with Timer("sweep"):
    for lo, hi, seg in seg_sieve(X + 3, seg_size=1 << 22):
        comb = np.concatenate([carry, seg]) if lo else seg
        base = carry_lo if lo else 0
        starts = np.nonzero(comb[:-2] & comb[2:])[0] + base
        starts = starts[starts > 5]
        r = starts % 5
        for cls in (1, 2, 4):
            counts[cls] += int(np.count_nonzero(r == cls))
        snap.append((hi, counts[1], counts[2], counts[4]))
        carry, carry_lo = seg[-2:].copy(), hi - 2


def predicted_D1(x):
    s = 0.0
    for q in primes_up_to(int(math.isqrt(int(x)))):
        q = int(q)
        if q > 3 and is_prime(q * q - 2):
            s += math.log(q) * math.log(q * q - 2)
    return 0.5 * s / math.log(x) ** 2


snap = np.array(snap, dtype=float)
x, c1, c2, c4 = snap.T
D1 = c1 - (c2 + c4) / 2
D24 = c2 - c4
w = np.diff(np.log(x), prepend=math.log(max(x[0] / 2, 2)))
lead1 = float(np.sum(w * (D1 > 0)) / np.sum(w))
print("final: c1=%d c2=%d c4=%d" % (c1[-1], c2[-1], c4[-1]))
rows = []
for i in sorted({min(len(x) - 1, int(len(x) * f)) for f in (0.01, 0.1, 0.4, 1.0)}):
    pd = predicted_D1(x[i])
    rows.append({"x": float(x[i]), "D1": float(D1[i]), "D1_predicted": round(pd, 1),
                 "D24_control": float(D24[i]),
                 "noise_scale": round(math.sqrt(c1[i] + (c2[i] + c4[i]) / 4), 1)})
    print("x=%.2e  D1=%+.0f  predicted=%+.1f  control D24=%+.0f  noise~%.0f"
          % (x[i], D1[i], pd, D24[i], math.sqrt(c1[i] + (c2[i] + c4[i]) / 4)))
print("log-density of {D1 > 0}: %.4f  (conjecture: > 1/2 but < 1)" % lead1)
print("log-density of {D24 > 0}: %.4f  (control: near 1/2 or wandering)"
      % float(np.sum(w * (D24 > 0)) / np.sum(w)))

save_result("c21", {"conjecture": "class 1 leads twin race mod 5 via q^2-2 mechanism; "
                                  "classes 2,4 symmetric; bias/noise ~ 1/log x",
                    "X": X, "final_counts": {k: int(v) for k, v in counts.items()},
                    "lead_density_D1_positive": lead1,
                    "lead_density_D24_positive": float(np.sum(w * (D24 > 0)) / np.sum(w)),
                    "table": rows})
