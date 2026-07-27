"""C05 (family lift) -- cyclotomic twin bases across the phi(k)=2 family.

For k with phi(k) = 2, i.e. k in {3, 4, 6}, consider Phi_k(n) and
Phi_k(n+1) simultaneously prime.

  k=3: (n^2+n+1, n^2+3n+3)   -- admissible, BH constant C(3)
  k=6: (n^2-n+1, n^2+n+1)    -- IDENTICAL to k=3: Phi_6(x) = Phi_3(x-1)
       as polynomials, so the k=6 pair at index n is the k=3 pair at
       index n-1.  The run below confirms the counts coincide; the k=6
       branch is the same conjecture, not a second instance.
  k=4: (n^2+1,  n^2+2n+2)    -- INADMISSIBLE at p=2: n^2+1 is even for
       odd n and n^2+2n+2 is even for even n, so one member is always
       even; the only prime pair is n=1, giving (2, 5).  This is the
       same parity obstruction that forbids consecutive n^2+1 primes,
       and it is part of the family statement, not a defect of it.

The family analysis is COMPLETE: among the three quadratic cyclotomic
polynomials, twin-base simultaneous primality yields exactly one
nontrivial conjecture (k=3 = k=6), one parity-dead branch (k=4).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from ntlib import *

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7
FAMS = {3: [[1, 1, 1], [3, 3, 1]],
        6: [[1, -1, 1], [1, 1, 1]]}

out = {}

# k = 4: verify the parity obstruction and the uniqueness of n = 1
with Timer("k=4 obstruction"):
    k4_pairs = [n for n in range(1, 10**6)
                if (n * n + 1) % 2 == 1 and (n * n + 2 * n + 2) % 2 == 1]
    assert k4_pairs == [], "parity obstruction violated"
    k4_prime_pairs = [n for n in range(1, 10**6)
                      if is_prime(n * n + 1) and is_prime(n * n + 2 * n + 2)]
print("k=4: both-odd count to 1e6: %d (theorem: 0); prime pairs: %s "
      "(only n=1 -> (2,5) possible)" % (len(k4_pairs), k4_prime_pairs))
out["k4"] = {"both_odd_to_1e6": len(k4_pairs), "prime_pairs": k4_prime_pairs}

for k, polys in FAMS.items():
    with Timer("k=%d" % k):
        C, Ce = bateman_horn_constant(polys, pmax=1_000_000)
        res = count_poly_primes(polys, N, presieve_to=100_000, checkpoints=(N,))
        obs = res["at"][N]
        pred = C * bh_integral(polys, N)
    print("k=%d: C=%.5f (wobble %.1e)  obs=%d pred=%.1f ratio=%.4f z=%+.2f"
          % (k, C, abs(C - Ce), obs, pred, obs / pred, zscore(obs, pred)))
    out["k%d" % k] = {"C": C, "wobble": abs(C - Ce), "obs": obs,
                      "pred": pred, "z": zscore(obs, pred),
                      "first": res["first"]}
save_result("c05", {"conjecture": "cyclotomic twin bases: complete quadratic family analysis; "
                                  "one live instance k=3 (= k=6 via Phi_6(x)=Phi_3(x-1)), "
                                  "k=4 dead by parity (only (2,5))",
                    "N": N, **out})
