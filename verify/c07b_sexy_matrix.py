"""C07' -- the two-orientation contamination MATRIX: sexy pairs (n, n+6).

For d = 6 BOTH prime-square orientations survive, on complementary
classes of q mod 5 -- the first matrix instance of the calculus
(pair races so far had exactly one surviving orientation):

  A = (q^2-6, q^2):  q^2-6 prime forces q = +-2 (5); start class
      q^2-6 = 3 (mod 5) and 3 (mod 8);
  B = (q^2, q^2+6):  q^2+6 prime forces q = +-1 (5) (q=5 gives start
      25 = 0 mod 5, outside the classes); start class q^2 = 1 (mod 5)
      and 1 (mod 8).

Sexy starts lie in classes {1,2,3} mod 5 and {1,3,5,7} mod 8.
Predicted drift vector (M_x sense):
  mod 5: class 2 clean;  pi(2)-pi(3) = T_A,  pi(2)-pi(1) = T_B;
  mod 8: classes 5,7 clean & symmetric;
         (pi(5)+pi(7))/2 - pi(3) = T_A,  (pi(5)+pi(7))/2 - pi(1) = T_B,
with T_A(x) = (1/log^2 x) sum_{q^2-6 prime} log q log(q^2-6),
     T_B(x) = (1/log^2 x) sum_{q^2+6 prime, q!=5} log q log(q^2+6).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9

c5 = {1: 0, 2: 0, 3: 0}
c8 = {1: 0, 3: 0, 5: 0, 7: 0}
# leadership tracking for the four drift components (weights per start)
COMPS = {"DA5": lambda r5, r8: (r5 == 2) * 1.0 - (r5 == 3) * 1.0,
         "DB5": lambda r5, r8: (r5 == 2) * 1.0 - (r5 == 1) * 1.0,
         "DA8": lambda r5, r8: ((r8 == 5) | (r8 == 7)) * 0.5 - (r8 == 3) * 1.0,
         "DB8": lambda r5, r8: ((r8 == 5) | (r8 == 7)) * 0.5 - (r8 == 1) * 1.0}
lead_num = {k: 0.0 for k in COMPS}
lead_den = 0.0
run = {k: 0.0 for k in COMPS}
prev_log = math.log(7.0)
carry = np.zeros(6, dtype=bool)
carry_lo = 0
with Timer("sweep"):
    for lo, hi, seg in seg_sieve(X + 7, seg_size=1 << 22):
        comb = np.concatenate([carry, seg]) if lo else seg
        base = carry_lo if lo else 0
        starts = np.nonzero(comb[:-6] & comb[6:])[0] + base
        starts = starts[starts > 7]
        if len(starts):
            r5 = starts % 5
            r8 = starts % 8
            w = np.diff(np.log(starts.astype(float)), prepend=prev_log)
            prev_log = math.log(float(starts[-1]))
            for k, f in COMPS.items():
                D = np.cumsum(f(r5, r8)) + run[k]
                lead_num[k] += float(np.sum(w * (D > 0)))
                run[k] = float(D[-1])
            lead_den += float(np.sum(w))
            for k in (1, 2, 3):
                c5[k] += int(np.count_nonzero(r5 == k))
            for k in (1, 3, 5, 7):
                c8[k] += int(np.count_nonzero(r8 == k))
        carry, carry_lo = seg[-6:].copy(), hi - 6
leads = {k: lead_num[k] / lead_den for k in COMPS}


def T(x, shift, excl=()):
    s = 0.0
    for q in primes_up_to(int(math.isqrt(int(x)))):
        q = int(q)
        v = q * q + shift
        if q > 3 and q not in excl and v > 1 and is_prime(v):
            s += math.log(q) * math.log(v)
    return s / math.log(x) ** 2


TA, TB = T(X, -6), T(X, 6, excl=(5,))
n5 = math.sqrt(c5[2] + c5[3])
n8 = math.sqrt(c8[1] + c8[5])
print("mod 5 classes (1,2,3): %d %d %d" % (c5[1], c5[2], c5[3]))
print("mod 8 classes (1,3,5,7): %d %d %d %d" % (c8[1], c8[3], c8[5], c8[7]))
DA5 = c5[2] - c5[3]; DB5 = c5[2] - c5[1]
DA8 = (c8[5] + c8[7]) / 2 - c8[3]; DB8 = (c8[5] + c8[7]) / 2 - c8[1]
ctrl8 = c8[5] - c8[7]
print("T_A pred %+.0f  T_B pred %+.0f  noise ~%.0f" % (TA, TB, n5))
print("mod5: pi(2)-pi(3)=%+d (pred %+.0f)  pi(2)-pi(1)=%+d (pred %+.0f)"
      % (DA5, TA, DB5, TB))
print("mod8: avg(5,7)-pi(3)=%+.1f (pred %+.0f)  avg(5,7)-pi(1)=%+.1f (pred %+.0f)  "
      "ctrl 5-7: %+d" % (DA8, TA, DB8, TB, ctrl8))
sd_null = math.sqrt(math.log(2) / math.log(X))  # occupation-fraction constant
print("leadership log-densities (null 1/2 +- %.3f): %s"
      % (sd_null, {k: round(v, 3) for k, v in leads.items()}))
save_result("c07b", {"conjecture": "sexy-pair contamination matrix: two surviving orientations, "
                                   "drift components T_A (class 3 mod 5 / 3 mod 8) and "
                                   "T_B (class 1 mod 5 / 1 mod 8), class 2 mod 5 and 5,7 mod 8 clean",
                     "X": X, "mod5": {str(k): v for k, v in c5.items()},
                     "mod8": {str(k): v for k, v in c8.items()},
                     "T_A": TA, "T_B": TB,
                     "DA5": DA5, "DB5": DB5, "DA8": DA8, "DB8": DB8,
                     "ctrl_57": ctrl8, "noise5": n5, "noise8": n8,
                     "leads": {k: float(v) for k, v in leads.items()},
                     "null_sd": sd_null})
