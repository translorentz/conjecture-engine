"""C25 (replacement) -- The Goldbach lane race: a Chebyshev-type bias
between the (1,1) and (3,3) lanes.

For n = 2 (mod 4), ordered Goldbach representations split into lanes
p = q = 1 (4) and p = q = 3 (4) (see C15).  In the Lambda-weighted count
the two lanes are symmetric to main order, but prime-SQUARE terms
n = q^2 + p (q odd prime) land exclusively in the (1,1) lane: q^2 = 1
(mod 4) and n - q^2 = 1 (mod 4) automatically.  Passing to unweighted
counts therefore depresses R1 relative to R3 by exactly the square
contamination:

  D(n) := R3(n) - R1(n)
        = D_sys(n) + noise,
  D_sys(n) = [ 2 * sum_{q odd prime <= sqrt n, n-q^2 prime}
                   log q * log(n-q^2) ] / lbar(n),

where lbar(n) is the mean of log p log(n-p) over the (3,3)-lane
representations (the psi-to-count normalization, computed empirically
per n).  Conjecture: E[D - D_sys] = o(E[D_sys]) on average over
n = 2 (mod 4), n <= x; in particular the (3,3) lane leads on average.
Same mechanism family as C21, driven here by q^2 + p patterns.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
NSAMP = int(sys.argv[2]) if len(sys.argv) > 2 else 400

with Timer("sieve"):
    P = sieve_bool(X)
P1 = np.zeros_like(P)
P1[5::4] = P[5::4]
P3 = np.zeros_like(P)
P3[3::4] = P[3::4]
p1_list = np.nonzero(P1)[0].astype(np.int64)
p3_list = np.nonzero(P3)[0].astype(np.int64)
log_p1 = np.log(p1_list.astype(float))
log_p3 = np.log(p3_list.astype(float))
qs = [int(q) for q in primes_up_to(int(math.isqrt(X)) + 1) if q > 2]

rng = np.random.default_rng(20260727)
lo, hi = 10**6, X
samples = np.unique((np.exp(rng.uniform(math.log(lo), math.log(hi), NSAMP)) // 4).astype(np.int64) * 4 + 2)

rows = []
sumD = sumDsys = 0.0
pos = 0
with Timer("lane race over %d samples" % len(samples)):
    for n in samples:
        n = int(n)
        i3 = np.searchsorted(p3_list, n - 2)
        r3 = n - p3_list[:i3]
        m3 = P3[r3]
        R3 = int(np.count_nonzero(m3))
        w3 = float(np.sum(log_p3[:i3][m3] * np.log(r3[m3].astype(float))))
        i1 = np.searchsorted(p1_list, n - 2)
        r1 = n - p1_list[:i1]
        R1 = int(np.count_nonzero(P1[r1]))
        if R3 == 0:
            continue
        lbar = w3 / R3
        sq = 0.0
        for q in qs:
            v = n - q * q
            if v < 3:
                break
            if P[v]:
                sq += math.log(q) * math.log(v)
        D = R3 - R1
        Dsys = 2.0 * sq / lbar
        sumD += D
        sumDsys += Dsys
        pos += D > 0
        rows.append((n, D, Dsys))

rows.sort()
n_arr = np.array([r[0] for r in rows], dtype=float)
D_arr = np.array([r[1] for r in rows], dtype=float)
S_arr = np.array([r[2] for r in rows], dtype=float)
ratio = sumD / sumDsys
# noise scale of the mean: sd(D)/sqrt(N)
noise = float(np.std(D_arr) / math.sqrt(len(rows)))
print("samples: %d  mean D = %.1f  mean D_sys = %.1f  ratio = %.3f"
      % (len(rows), D_arr.mean(), S_arr.mean(), ratio))
print("mean-D noise scale %.1f -> signal/noise = %.1f"
      % (noise, D_arr.mean() / noise))
print("sign: D>0 in %.3f of samples (fair coin would give ~0.5)"
      % (pos / len(rows)))
half = len(rows) // 2
print("ratio lower-half n: %.3f  upper-half n: %.3f"
      % (float(D_arr[:half].sum() / S_arr[:half].sum()),
         float(D_arr[half:].sum() / S_arr[half:].sum())))

save_result("c25", {"conjecture": "Goldbach lane race: R3-R1 ~ square contamination D_sys "
                                  "on average; (3,3) lane leads",
                    "X": X, "n_samples": len(rows),
                    "mean_D": float(D_arr.mean()), "mean_Dsys": float(S_arr.mean()),
                    "ratio_D_over_Dsys": float(ratio),
                    "mean_noise": noise,
                    "signal_over_noise": float(D_arr.mean() / noise),
                    "frac_D_positive": float(pos / len(rows)),
                    "ratio_halves": [float(D_arr[:half].sum() / S_arr[:half].sum()),
                                     float(D_arr[half:].sum() / S_arr[half:].sum())]})
