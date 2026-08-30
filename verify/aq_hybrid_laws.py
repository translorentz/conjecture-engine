#!/usr/bin/env python3
"""Independent verification for Part XXVI (Conjectures 389-393, aq1-aq5):
entropy and rare-event laws for random algebraic and topological structures.

The conjectures are asymptotic laws for invariants whose exact computation is
infeasible at scale; what this script checks, from scratch and sharing no code
with the source diagnostics, is the proved anchor layer and the finite
calibrations each law rests on.

  aq1  tropical double scaling: at profile (-2,0,-1,0) with active faces r=1,
       s=3 (m=2, delta=1), the sqrt(N)-scaled optimal matching displacement
       between the zeros of the full Ginibre matrix polynomial and the
       two-face pencil falls with N at beta=2 log N and stalls at
       beta=0.75 log N, locating the double-scaling threshold.
  aq2  Kazhdan-Lusztig cycle calibration: a from-scratch implementation of the
       defining Elias-Proudfoot-Wakefield recursion reproduces the closed
       formula P_{U_{k-1,k}}(1) = sum_i C(k,i) C(k-i-2,i)/(i+1) exactly, and
       the entropy rate k^{-1} log P rises toward log 3.
  aq3  Khovanov proxy: the reduced-Burau determinant exponent at t=-1 on
       three-strand walks conditioned on cyclic closures is stably positive
       (~0.08).  A decategorified scale check only: it cannot witness the
       homological cancellation.
  aq4  Weil-Petersson constants: the Mirzakhani-Petri intensity integrates to
       Lambda(eps) = eps^2/4 + eps^4/96 + ..., giving the all-k Poisson tail
       constants 1/(4^k k!), and the collar normalization pi*cap(l)/l -> 1.
  aq5  homology shadow: exact integral symplectic transvection walks give a
       positive homological exponent (~0.19).  Abelian shadow only: it cannot
       witness Floer cancellation.

Exact where feasible (aq2 recursion, aq5 integer arithmetic); seeded Monte
Carlo otherwise.  Runs in a few minutes.
"""
import math
import random
from fractions import Fraction
from math import comb
import functools

import numpy as np
from scipy.optimize import linear_sum_assignment

PASS = []
def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))


# ---------------------------------------------------------------------------
print("== aq2 (390): Kazhdan-Lusztig cycle calibration ==")
def pmul(a, b):
    r = {}
    for i, ca in a.items():
        for j, cb in b.items():
            r[i + j] = r.get(i + j, Fraction(0)) + ca * cb
    return r
def padd(a, b):
    r = dict(a)
    for j, cb in b.items():
        r[j] = r.get(j, Fraction(0)) + cb
    return {k: v for k, v in r.items() if v != 0}

def chi_uniform(r, n):
    # characteristic polynomial of U_{r,n} from the Whitney rank sum
    p = {}
    for j in range(n + 1):
        d = r - min(j, r)
        p[d] = p.get(d, Fraction(0)) + Fraction((-1) ** j * comb(n, j))
    return {k: v for k, v in p.items() if v != 0}

@functools.lru_cache(maxsize=None)
def kl_corank1(n):
    """KL polynomial of U_{n-1,n} (cycle matroid of the n-cycle) by the
    defining recursion: t^r P(1/t) = sum over flats F of chi_{M|F}(t) P(M/F)(t),
    with deg P < r/2.  Flats of U_{n-1,n}: subsets of size <= n-2, plus E."""
    r = n - 1
    if r <= 0:
        return ((0, Fraction(1)),)
    rhs = {}
    tm1 = {1: Fraction(1), 0: Fraction(-1)}
    tm1k = {0: Fraction(1)}
    for k in range(1, r):
        tm1k = pmul(tm1k, tm1)          # (t-1)^k = chi of Boolean B_k
        term = pmul({0: Fraction(comb(n, k))},
                    pmul(tm1k, dict(kl_corank1(n - k))))
        rhs = padd(rhs, term)
    rhs = padd(rhs, chi_uniform(r, n))
    P = {0: Fraction(1)}
    for i in range(1, (r + 1) // 2):
        c = -rhs.get(i, Fraction(0))
        if c != 0:
            P[i] = c
    # high-degree consistency: coefficients of t^{r-i} must agree
    for i, ci in P.items():
        want = rhs.get(r - i, Fraction(0)) + P.get(r - i, Fraction(0))
        assert ci == want, (n, i, ci, want)
    return tuple(sorted(P.items()))

def P1_rec(n): return sum(c for _, c in kl_corank1(n))
def P1_formula(n):
    return sum(Fraction(comb(n, i) * comb(n - i - 2, i), i + 1)
               for i in range((n - 2) // 2 + 1))

match = all(P1_rec(n) == P1_formula(n) for n in range(3, 26))
check("aq2 EPW recursion reproduces the closed cycle formula (k=3..25)", match)
h10 = math.log(P1_rec(10)) / 10
h25 = math.log(P1_rec(25)) / 25
print(f"    entropy rate: k=10: {h10:.7f}, k=25: {h25:.7f}  ->  log 3 = {math.log(3):.7f}")
check("aq2 cycle entropy rate rises toward log 3",
      abs(h10 - 0.6401917) < 1e-6 and h25 > h10 and h25 < math.log(3))


# ---------------------------------------------------------------------------
print("== aq4 (392): Weil-Petersson constants ==")
# Lambda(eps) = int_0^eps (e^t+e^-t-2)/(2t) dt
#             = sum_k eps^{2k}/(2k (2k)!).
def Lambda(eps, K=12):
    return sum(eps ** (2 * k) / (2 * k * math.factorial(2 * k))
               for k in range(1, K + 1))

def poisson_upper_tail(mean, k):
    return 1.0 - math.exp(-mean) * sum(mean ** j / math.factorial(j)
                                        for j in range(k))

epsilons = (0.12, 0.08, 0.05)
tail_checks = []
for k in (1, 2, 3):
    target = 1.0 / (4 ** k * math.factorial(k))
    ratios = [poisson_upper_tail(Lambda(e), k) / e ** (2 * k)
              for e in epsilons]
    print(f"    k={k}: P(Poisson(Lambda)>=k)/eps^(2k) =",
          [round(r, 8) for r in ratios], f"-> {target:.8f}")
    tail_checks.append(abs(ratios[-1] / target - 1.0) < 2e-3)
check("aq4 all-k short-geodesic tail constants through k=3",
      all(tail_checks))
def collar_capacity(ell):
    w = math.asinh(1.0 / math.sinh(ell / 2.0))
    return ell / (math.pi - 2.0 * math.asin(1.0 / math.cosh(w)))
caps = [math.pi * collar_capacity(l) / l for l in (0.1, 0.02, 0.005)]
print("    pi*cap(l)/l:", [round(c, 5) for c in caps])
check("aq4 collar normalization pi*cap(l)/l -> 1",
      all(c > 1 for c in caps) and caps[-1] - 1 < 2e-3)


# ---------------------------------------------------------------------------
print("== aq1 (389): tropical double-scaling matching ==")
rng = np.random.default_rng(9157)
def ginibre(N):
    return (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) \
        / math.sqrt(2 * N)
def full_roots(coeffs):
    d = len(coeffs) - 1
    N = coeffs[0].shape[0]
    Ad_inv = np.linalg.inv(coeffs[-1])
    C = np.zeros((d * N, d * N), dtype=complex)
    C[:(d - 1) * N, N:] = np.eye((d - 1) * N)
    C[(d - 1) * N:, :] = np.hstack([-(Ad_inv @ A) for A in coeffs[:-1]])
    return np.linalg.eigvals(C)
a = [-2, 0, -1, 0]  # breakpoint x*=0, active r=1,s=3, m=2, delta=1
def mean_disp(N, c, samples=20):
    beta = c * math.log(N)
    out = []
    for _ in range(samples):
        G = [ginibre(N) for _ in range(4)]
        coeffs = [math.exp(beta * a[k]) * G[k] for k in range(4)]
        fz = full_roots(coeffs)
        lam = np.linalg.eigvals(-np.linalg.solve(G[3], G[1]))
        pz = np.concatenate([np.sqrt(lam), -np.sqrt(lam)])
        cost = np.abs(pz[:, None] - fz[None, :])
        r, ci = linear_sum_assignment(cost)
        out.append(math.sqrt(N) * cost[r, ci].mean())
    return float(np.mean(out))
d_fast = [mean_disp(N, 2.0) for N in (4, 12, 20)]
d_slow = [mean_disp(N, 0.75) for N in (4, 12, 20)]
print(f"    beta=2logN: N=4,12,20 -> {[round(x,4) for x in d_fast]} (decaying)")
print(f"    beta=0.75logN:        -> {[round(x,4) for x in d_slow]} (stalling)")
check("aq1 matching decays at beta=2logN and stalls at beta=0.75logN",
      d_fast[-1] < 0.05 and d_fast[0] > 3 * d_fast[-1] and d_slow[-1] > 0.2)


# ---------------------------------------------------------------------------
print("== aq3 (391): decategorified Burau proxy (scale check only) ==")
S1 = np.array([[1, 1], [0, 1]], dtype=object)
S1i = np.array([[1, -1], [0, 1]], dtype=object)
S2 = np.array([[1, 0], [-1, 1]], dtype=object)
S2i = np.array([[1, 0], [1, 1]], dtype=object)
I2 = np.eye(2, dtype=object)
gens = [S1, S1i, S2, S2i, I2]
perms = [(1, 0, 2), (1, 0, 2), (0, 2, 1), (0, 2, 1), (0, 1, 2)]
def compose(p, q): return tuple(p[q[i]] for i in range(3))
def burau_proxy(n, samples, seed):
    r = random.Random(seed)
    vals = []
    for _ in range(samples):
        M = np.eye(2, dtype=object)
        p = (0, 1, 2)
        for _ in range(n):
            j = r.randrange(5)
            M = gens[j] @ M
            p = compose(perms[j], p)
        if p in [(1, 2, 0), (2, 0, 1)]:      # 3-cycle closures: knots
            A = np.eye(2, dtype=object) - M
            det = int(A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])
            if det:
                vals.append(math.log(abs(det)) / n)
    return float(np.mean(vals))
b100 = burau_proxy(100, 800, 71)
b200 = burau_proxy(200, 500, 72)
print(f"    n=100,200: {b100:.4f}, {b200:.4f}  (calibration scale ~0.08)")
check("aq3 Burau determinant exponent stable and positive (~0.08)",
      0.05 < b100 < 0.12 and 0.05 < b200 < 0.12)


# ---------------------------------------------------------------------------
print("== aq5 (393): integral symplectic homology shadow (scale check only) ==")
def Jmat(g=2):
    I = np.eye(g, dtype=object); Z = np.zeros((g, g), dtype=object)
    return np.block([[Z, I], [-I, Z]])
J = Jmat(2)
def transvection(v, sign):
    v = np.asarray(v, dtype=object).reshape(-1, 1)
    return np.eye(4, dtype=object) + sign * v @ (v.T @ J)
vecs = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
        [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
plus = [transvection(v, 1) for v in vecs]
minus = [transvection(v, -1) for v in vecs]
def sympl_check():
    for T in plus + minus:
        assert np.array_equal(T.T @ J @ T, J), "not symplectic"
sympl_check()
def shadow(n, samples, seed):
    r = random.Random(seed)
    vals = []
    for _ in range(samples):
        M = np.eye(4, dtype=object)
        for _ in range(n):
            j = r.randrange(len(vecs))
            M = (plus[j] if r.random() < 0.5 else minus[j]) @ M
        C = M[2:, :2]
        det = int(C[0, 0] * C[1, 1] - C[0, 1] * C[1, 0])
        if det:
            vals.append(math.log(abs(det)) / n)
    return float(np.mean(vals))
s50 = shadow(50, 120, 5)
s100 = shadow(100, 100, 6)
print(f"    n=50,100: {s50:.4f}, {s100:.4f}  (calibration scale ~0.18-0.19; "
      "transvections verified symplectic exactly)")
check("aq5 homological exponent positive and stable (~0.18-0.19)",
      0.1 < s50 < 0.3 and 0.1 < s100 < 0.3)


n_ok = sum(PASS)
print(f"\n{n_ok}/{len(PASS)} checks passed.  These verify the proved anchors and "
      "finite calibrations of Part XXVI; the Burau and symplectic checks are "
      "decategorified and abelian shadows that cannot witness the homological "
      "cancellations of Conjectures 391 and 393, and no finite computation "
      "reaches the asymptotic laws themselves.")
import sys
sys.exit(0 if all(PASS) else 1)
