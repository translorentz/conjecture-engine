"""C03' -- contamination calculus for prime TRIPLETS (n, n+2, n+6).

Extension of the calculus (C21(v)) to k-tuples.  For the triplet
pattern, the prime-square configurations with one entry a square are:
  (q^2, q^2+2, q^2+6):  dead, 3 | q^2+2 for q > 3;
  (q^2-6, q^2-4, q^2):  dead, q^2-4 = (q-2)(q+2) composite;
  (q^2-2, q^2, q^2+4):  SURVIVES -- needs q^2-2 AND q^2+4 both prime
                        (doubly-thinned), automatic q = +-2 (mod 5)
                        since q = +-1 forces 5 | q^2+4.
Triplet starts lie in classes n = 1, 2 (mod 5); the surviving
configuration has start q^2-2 = 2 (mod 5), so class 2 is contaminated
and class 1 leads:
   D(x) = pi_3(x;5,1) - pi_3(x;5,2) = T3(x) + noise,
   T3(x) = (1/log^3 x) sum_{q<=sqrt x, q^2-2 & q^2+4 prime}
             log(q^2-2) log q log(q^2+4).
Drift/noise ~ 1/log^{3/2} x -- weaker than pair races; the testable
statistics are the leadership log-density against the OU null and the
symmetric-class structure.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9

c = {1: 0, 2: 0}
traj = []
carry = np.zeros(6, dtype=bool)
carry_lo = 0
with Timer("sweep"):
    for lo, hi, seg in seg_sieve(X + 7, seg_size=1 << 22):
        comb = np.concatenate([carry, seg]) if lo else seg
        base = carry_lo if lo else 0
        starts = np.nonzero(comb[:-6] & comb[2:-4] & comb[6:])[0] + base
        starts = starts[starts > 7]
        r = starts % 5
        d1 = np.cumsum(r == 1)
        d2 = np.cumsum(r == 2)
        if len(starts):
            traj.append((starts.astype(np.int64), (d1 - d2) + (c[1] - c[2])))
            c[1] += int(d1[-1]); c[2] += int(d2[-1])
        carry, carry_lo = seg[-6:].copy(), hi - 6

D_end = c[1] - c[2]
tot = c[1] + c[2]
# leadership log-density and running max over the full trajectory
num = den = 0.0
runmax = 0.0
count_so_far = 0
prev_log = math.log(7)
for starts, D in traj:
    w = np.diff(np.log(starts.astype(float)), prepend=prev_log)
    prev_log = math.log(float(starts[-1]))
    num += float(np.sum(w * (D > 0)))
    den += float(np.sum(w))
    cnt = count_so_far + np.arange(1, len(starts) + 1)
    runmax = max(runmax, float(np.max(np.abs(D) / np.sqrt(cnt))))
    count_so_far += len(starts)
lead = num / den

def T3(x):
    s = 0.0
    for q in primes_up_to(int(math.isqrt(int(x)))):
        q = int(q)
        if q > 3 and is_prime(q * q - 2) and is_prime(q * q + 4):
            s += math.log(q * q - 2) * math.log(q) * math.log(q * q + 4)
    return s / math.log(x) ** 3

T = T3(X)
noise = math.sqrt(tot)
sd_null = 2 * math.sqrt(math.log(2) / math.log(X))
print("classes at %.0e: c1=%d c2=%d  D=%+d  (T3 pred %+.1f, noise %.0f)"
      % (X, c[1], c[2], D_end, T, noise))
print("leadership log-density {D>0}: %.3f  (null 1/2 +- %.3f)" % (lead, sd_null))
print("running max |D|/sqrt(count) = %.2f  (Darling-Erdos scale sqrt(2 loglog x) = %.2f)"
      % (runmax, math.sqrt(2 * math.log(math.log(X)))))
save_result("c03b", {"conjecture": "triplet (0,2,6) race mod 5: class 1 leads via the "
                                   "(q^2-2, q^2, q^2+4) doubly-thinned configuration",
                     "X": X, "c1": c[1], "c2": c[2], "D": D_end,
                     "T3_pred": T, "noise": noise, "lead_logdensity": lead,
                     "null_sd": sd_null, "runmax_normalized": runmax})
