"""C19 -- First occurrence of prime gaps (Shanks with Granville correction).

Let p(g) be the prime beginning the first gap of exactly g.  Cramer's model
gives log p(g) ~ sqrt(g); Granville's correction (max gap ~ c log^2 x with
c = 2e^{-gamma} = 1.1229) gives log p(g) ~ sqrt(g/c), slope 0.9436.
Conjecture: log p(g)/sqrt(g) -> 2^{-1/2}e^{gamma/2} = 0.9436 (from below).
Verification: all first occurrences to 10^9, regression of log p(g) on sqrt g.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9

first = {}
last = None
with Timer("sweep"):
    for lo, hi, seg in seg_sieve(X, seg_size=1 << 24):
        pos = np.nonzero(seg)[0] + lo
        if len(pos) == 0:
            continue
        if last is not None:
            pos = np.concatenate([[last], pos])
        gaps = np.diff(pos)
        for g in np.unique(gaps):
            g = int(g)
            if g not in first:
                first[g] = int(pos[int(np.argmax(gaps == g))])
        last = int(pos[-1])

gs = sorted(first)
missing = [g for g in range(2, max(gs), 2) if g not in first]
print("gaps with a first occurrence found: %d (largest %d)" % (len(gs), gs[-1]))
print("even gaps below the largest with NO occurrence yet:", missing)

# regression log p(g) = s * sqrt(g) over the top half of observed gaps
fit_g = [g for g in gs if g >= 100 and first[g] > 100]
sq = np.array([math.sqrt(g) for g in fit_g])
lp = np.array([math.log(first[g]) for g in fit_g])
slope = float(np.sum(sq * lp) / np.sum(sq * sq))
print("regression slope log p(g)/sqrt(g) (g>=100): %.4f" % slope)
print("model slopes: Cramer 1.0000, Granville %.4f"
      % (1 / math.sqrt(2 * math.exp(-EULER_GAMMA))))
table = [{"g": g, "p": first[g], "log_p_over_sqrt_g": round(math.log(first[g]) / math.sqrt(g), 4)}
         for g in gs if g % 30 == 0 or g == gs[-1]]
for r in table:
    print("  g=%4d  p(g)=%12d  log p/sqrt g = %.4f" % (r["g"], r["p"], r["log_p_over_sqrt_g"]))

save_result("c19", {"conjecture": "log p(g)/sqrt(g) -> sqrt(e^gamma/2) = 0.9436",
                    "slope_measured_g_ge_100": slope,
                    "slope_cramer": 1.0, "slope_granville": 1 / math.sqrt(2 * math.exp(-EULER_GAMMA)),
                    "missing_even_gaps": missing, "table": table})
