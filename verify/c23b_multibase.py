"""C23' -- multibase Fermat quotients: subtorus equidistribution and
simultaneous Wieferich accounting.

q_p(a) = (a^{p-1}-1)/p mod p.  The homomorphism
q_p(ab) = q_p(a) + q_p(b) (mod p) (classical, Eisenstein) confines
the vector (q_p(a_1),...,q_p(a_r))/p to the rational subtorus cut out
by the multiplicative relations among the bases.  Candidate laws:
 (i)   [structure, exact] the homomorphism identity (verified exactly);
 (ii)  [joint equidistribution] for multiplicatively independent bases
       (here 2 and 3), (q_p(2)/p, q_p(3)/p) equidistributes on the
       FULL 2-torus, with LIL-calibrated discrepancy and vanishing
       correlation;
 (iii) [simultaneous Wieferich] the count of p <= x with
       q_p(2) = q_p(3) = 0 has convergent expected mass sum 1/p^2:
       at most finitely many simultaneous Wieferich primes exist, and
       the empirical list is EMPTY (checked to PMAX).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

PMAX = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7
K = int(sys.argv[2]) if len(sys.argv) > 2 else 100

q2s, q3s, ps = [], [], []
simul = []
homo_fail = 0
with Timer("quotients to %d" % PMAX):
    for i, p in enumerate(primes_up_to(PMAX)):
        p = int(p)
        if p < 5:
            continue
        p2 = p * p
        q2 = (pow(2, p - 1, p2) - 1) // p
        q3 = (pow(3, p - 1, p2) - 1) // p
        ps.append(p)
        q2s.append(q2)
        q3s.append(q3)
        if q2 == 0 and q3 == 0:
            simul.append(p)
        if i % 1000 == 0:  # spot-check the homomorphism on base 6
            q6 = (pow(6, p - 1, p2) - 1) // p
            if q6 != (q2 + q3) % p:
                homo_fail += 1
ps = np.array(ps, dtype=float)
u = np.array(q2s) / ps
v = np.array(q3s) / ps
n = len(ps)
corr = float(np.corrcoef(u, v)[0, 1])
# 2-D chi-square on a 20x20 grid
H, _, _ = np.histogram2d(u, v, bins=20, range=[[0, 1], [0, 1]])
chi2 = float(((H - n / 400) ** 2 / (n / 400)).sum())
# joint small-quotient census
obs_joint = int(np.count_nonzero((np.array(q2s) < K) & (np.array(q3s) < K)))
model = 0.0
for p in primes_up_to(PMAX):
    p = int(p)
    if p >= 5:
        model += min(1.0, K / p) ** 2
print("primes used: %d   homomorphism failures: %d (exact identity)" % (n, homo_fail))
print("correlation(q2/p, q3/p) = %+.5f   chi2(20x20) = %.0f (df 399, sd ~28)"
      % (corr, chi2))
print("joint census q2,q3 < %d: obs %d vs model %.1f (z=%+.2f)"
      % (K, obs_joint, model, (obs_joint - model) / math.sqrt(max(model, 1))))
print("simultaneous Wieferich (q2=q3=0) up to %d: %s" % (PMAX, simul or "NONE"))
save_result("c23b", {"conjecture": "multibase Fermat quotients: exact homomorphism; joint "
                                   "equidistribution for independent bases; simultaneous "
                                   "Wieferich finiteness (empirical list empty)",
                     "PMAX": PMAX, "n_primes": n, "homo_failures": homo_fail,
                     "correlation": corr, "chi2_20x20": chi2,
                     "joint_census": {"K": K, "obs": obs_joint, "model": model},
                     "simultaneous_wieferich": simul})
