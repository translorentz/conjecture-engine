"""C13 -- Prime plus a positive cube (RESTATED after adversarial refutation).

The first version of this conjecture claimed the exception set of
n = p + k^3 (k >= 1) is finite.  The adversarial battery refuted it:
for n = k^3 the difference n - j^3 = (k-j)(k^2+kj+j^2) factors, so a cube
is representable iff 3k^2-3k+1 (the j = k-1 term) is prime -- an
elementary THEOREM producing an infinite, density-one-in-cubes family of
exceptions that the naive Borel-Cantelli accounting missed.

Restated conjecture:
  (i)  [theorem, checked here] for k >= 2: k^3 unrepresentable
       iff 3k^2-3k+1 composite;
  (ii) [conjecture] the set of NON-CUBE integers n >= 2 not of the form
       p + k^3 is finite; per-decade counts decay super-geometrically;
  (iii)[Bateman-Horn corollary for the cube lane]
       #{k <= K : 3k^2-3k+1 prime} ~ C * int dt/log(3t^2-3t+1).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8

with Timer("sieve"):
    P = sieve_bool(N)
rep = np.zeros(N + 1, dtype=bool)
with Timer("shift union"):
    k = 1
    while k ** 3 < N:
        c = k ** 3
        rep[c:] |= P[: N + 1 - c]
        k += 1

exc = [int(e) for e in (np.nonzero(~rep[2:])[0] + 2)]
kc = np.arange(2, int(round(N ** (1 / 3))) + 2)
cube_set = set(int(v) for v in kc ** 3 if v <= N)
cube_exc = [n for n in exc if n in cube_set]
noncube_exc = [n for n in exc if n not in cube_set]

# (i) theorem check: cube k^3 unrepresentable iff 3k^2-3k+1 composite
bad = []
for k in kc:
    k = int(k)
    n = k ** 3
    if n > N:
        break
    if (n in set(cube_exc)) != (not is_prime(3 * k * k - 3 * k + 1)):
        bad.append(k)
print("(i) cube criterion mismatches:", bad or "none (theorem verified in range)")

per_decade = {}
for e in noncube_exc:
    per_decade[len(str(e))] = per_decade.get(len(str(e)), 0) + 1
print("(ii) non-cube exceptions: %d, largest %s" %
      (len(noncube_exc), noncube_exc[-1] if noncube_exc else None))
print("    per decade:", per_decade)
print("    cube exceptions: %d of %d cubes in range" % (len(cube_exc), len(cube_set)))

with Timer("(iii) cube-lane BH"):
    C, _ = bateman_horn_constant([[1, -3, 3]], pmax=1_000_000)
    K = int(round(N ** (1 / 3)))
    obs = sum(1 for k in range(2, K + 1) if is_prime(3 * k * k - 3 * k + 1))
    pred = C * bh_integral([[1, -3, 3]], K)
print("    #{k<=%d: 3k^2-3k+1 prime} = %d  pred %.1f  ratio %.4f  z %+.2f"
      % (K, obs, pred, obs / pred, zscore(obs, pred)))

save_result("c13", {"conjecture": "RESTATED: non-cube exceptions of n=p+k^3 finite; "
                                  "cube k^3 exceptional iff 3k^2-3k+1 composite (thm); "
                                  "cube lane follows BH",
                    "N": N,
                    "noncube_exceptions": len(noncube_exc),
                    "noncube_largest": noncube_exc[-1] if noncube_exc else None,
                    "noncube_by_digits": per_decade,
                    "noncube_tail_sample": noncube_exc[-20:],
                    "cube_exceptions": len(cube_exc),
                    "cube_criterion_mismatches": bad,
                    "cube_lane_C": C, "cube_lane_obs": obs,
                    "cube_lane_pred": pred})
