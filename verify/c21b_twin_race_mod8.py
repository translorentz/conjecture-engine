"""C21(iv) -- the mod-8 companion of the twin race.

q^2 = 1 (mod 8) for every odd q, so every contaminating pair
(q^2-2, q^2) has its start in class 7 (mod 8): the ENTIRE deterministic
term lands on one class.  Prediction: class 7 trails, with
   D7(x) = (1/3)(pi_t(x;8,1)+pi_t(x;8,3)+pi_t(x;8,5)) - pi_t(x;8,7)
         = T(x) + noise,  T(x) = (1/log^2 x) sum_{q<=sqrt x, q^2-2 prime}
                                  log q log(q^2-2)
(twice the mod-5 systematic term, since nothing is split), while
classes 1, 3, 5 are mutually symmetric.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9

counts = {1: 0, 3: 0, 5: 0, 7: 0}
snap = []
carry = np.zeros(2, dtype=bool)
carry_lo = 0
with Timer("sweep"):
    for lo, hi, seg in seg_sieve(X + 3, seg_size=1 << 22):
        comb = np.concatenate([carry, seg]) if lo else seg
        base = carry_lo if lo else 0
        starts = np.nonzero(comb[:-2] & comb[2:])[0] + base
        starts = starts[starts > 5]
        r = starts % 8
        for cls in (1, 3, 5, 7):
            counts[cls] += int(np.count_nonzero(r == cls))
        snap.append((hi, counts[1], counts[3], counts[5], counts[7]))
        carry, carry_lo = seg[-2:].copy(), hi - 2


def predicted_T(x):
    s = 0.0
    for q in primes_up_to(int(math.isqrt(int(x)))):
        q = int(q)
        if q > 3 and is_prime(q * q - 2):
            s += math.log(q) * math.log(q * q - 2)
    return s / math.log(x) ** 2


snap = np.array(snap, dtype=float)
x, c1, c3, c5, c7 = snap.T
D7 = (c1 + c3 + c5) / 3 - c7
w = np.diff(np.log(x), prepend=math.log(max(x[0] / 2, 2)))
print("final: c1=%d c3=%d c5=%d c7=%d" % (c1[-1], c3[-1], c5[-1], c7[-1]))
rows = []
for i in sorted({min(len(x) - 1, int(len(x) * f)) for f in (0.01, 0.1, 0.4, 1.0)}):
    T = predicted_T(x[i])
    rows.append({"x": float(x[i]), "D7": float(D7[i]), "T_predicted": round(T, 1),
                 "noise_scale": round(math.sqrt(c7[i] * 4 / 3), 0)})
    print("x=%.2e  D7=%+.0f  T=%+.1f  noise~%.0f" %
          (x[i], D7[i], T, math.sqrt(c7[i] * 4 / 3)))
ld = float(np.sum(w * (D7 > 0)) / np.sum(w))
print("log-density of {D7 > 0}: %.4f  (conjecture: 1/2 limit, finite-x excess)" % ld)
ctrl = {"13": float(c1[-1] - c3[-1]), "15": float(c1[-1] - c5[-1]),
        "35": float(c3[-1] - c5[-1])}
print("controls (pairwise 1,3,5 differences):", ctrl)

save_result("c21b", {"conjecture": "mod-8 twin race: entire square-contamination on class 7; "
                                   "1,3,5 symmetric",
                     "X": X, "final_counts": {k: int(v) for k, v in counts.items()},
                     "lead_density_D7_positive": ld, "controls": ctrl,
                     "table": rows})
