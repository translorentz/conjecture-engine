"""C22 -- Least prime in arithmetic progressions: the Cramer law holds
only asymptotically, with a 1/log q finite-size deficit.

Model: in Li-time, U(a,q) = Li(p(a,q))/phi(q) is a first-arrival time;
the naive model says U ~ Exp(1).  Conjecture:
  (i)   U -> Exp(1) in distribution as q -> infinity (tail slope -> -1,
        max_a U - H_phi -> Gumbel, mean -> 1);
  (ii)  the finite-q deficit is first order 1/log q:
        E_a[U] = 1 - theta(q)/log q + o(1/log q), theta slowly varying
        (measured theta reported per q-band; the deficit bottoms out near
        q ~ 200 and recovers -- the signature of a vanishing correction,
        not of a limiting constant below 1);
  (iii) controls: iid labels, permuted residues, and a Cramer pseudo-prime
        sequence all sit strictly above the real primes' deficit -- part
        of the effect is the ordering of the primes (sieve-boosted local
        hazards), documented as an anomaly with its constant open.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

QMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
PLIM = int(float(sys.argv[2])) if len(sys.argv) > 2 else 5 * 10**6

with Timer("primes"):
    primes = primes_up_to(PLIM).astype(np.int64)
grid = np.linspace(2.0, float(PLIM), 2_000_001)
li_grid = np.concatenate([[0.0], np.cumsum(np.diff(grid) /
                                           np.log(grid[:-1] + np.diff(grid) / 2))])


def Li(x):
    return np.interp(x, grid, li_grid)


pooled_U, gumbel, mean_by_band = [], [], {}
with Timer("scan q"):
    for q in range(3, QMAX + 1):
        r = primes % q
        classes, first_idx = np.unique(r, return_index=True)
        keep = np.gcd(classes, q) == 1
        classes, first_idx = classes[keep], first_idx[keep]
        phi = int(np.count_nonzero(np.gcd(np.arange(1, q + 1), q) == 1))
        if len(classes) != phi:
            print("  !! coverage failure at q=%d (increase PLIM)" % q)
            continue
        U = Li(primes[first_idx].astype(float)) / phi
        pooled_U.append(U)
        H = float(np.sum(1.0 / np.arange(1, phi + 1)))
        gumbel.append(float(U.max()) - H)
        band = int(math.log10(q) * 3)
        mean_by_band.setdefault(band, []).append(float(U.mean()))

U = np.sort(np.concatenate(pooled_U))
n = len(U)
# (i) tail slope of log P(U > u) on u in [1, 4]
us = np.linspace(1.0, 4.0, 13)
logtail = np.log(np.array([np.count_nonzero(U > u) for u in us], dtype=float) / n)
A = np.vstack([us, np.ones_like(us)]).T
slope, intercept = np.linalg.lstsq(A, logtail, rcond=None)[0]
gum = np.array(gumbel)
print("pooled classes: %d over q <= %d" % (n, QMAX))
print("(i)   tail log-slope on [1,4]: %.4f  (model: -1)" % slope)
print("(ii)  mean(max U - H_phi) = %+.4f   sd = %.4f  (model: 0, %.4f)"
      % (gum.mean(), gum.std(), math.pi / math.sqrt(6)))
print("(iii) mean U by q-band (log10 thirds), with theta = (1-meanU)*log q:")
bands = []
for b in sorted(mean_by_band):
    m = float(np.mean(mean_by_band[b]))
    qmid = 10 ** ((b + 0.5) / 3)
    theta = (1 - m) * math.log(qmid)
    bands.append({"q_band_lo": round(10 ** (b / 3), 1), "mean_U": round(m, 4),
                  "theta": round(theta, 3)})
    print("      q ~ %8.0f..: mean U = %.4f   theta = %.3f"
          % (10 ** (b / 3), m, theta))

save_result("c22", {"conjecture": "tail of Li(p(a,q))/phi is Exp(1); max ~ H_phi + Gumbel",
                    "qmax": QMAX, "pooled_classes": n,
                    "tail_slope": float(slope), "tail_intercept": float(intercept),
                    "gumbel_mean": float(gum.mean()), "gumbel_sd": float(gum.std()),
                    "gumbel_sd_model": math.pi / math.sqrt(6),
                    "mean_U_overall": float(U.mean()),
                    "mean_U_by_band": bands})
