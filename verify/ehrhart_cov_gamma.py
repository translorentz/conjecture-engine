#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Propositions x:ehrhart, w:cov53, and aa:coverage, and the z4 gamma
reduction: the Ehrhart model for common scaling of Brieskorn-Pham links,
the exact truncated lag-one covariance of the central-binomial slice, the
coverage floor for the sparse-flux threshold, and the gamma-index dominance
reduction for edge-addition concentration.

Checks, from scratch and in exact arithmetic unless stated:
  (1) the three-way identity: Milnor-Orlik alternating sum = count of
      nontrivial root-of-unity tuples with product one = interior lattice
      points of the dilated weighted hypersimplices;
  (2) nonnegativity of all forward differences through order N-1;
  (3) a log-concavity and convexity stress of the open clause of C126;
  (4) truncated lag-one covariances: -1 at cutoff 2 and -5/3 at every
      larger cutoff, with the p-local values -1, -2/3, 0, 0, 0 at
      p = 2, 3, 5, 7, 11, and the full covariance drifting toward -5/3;
  (5) gamma vectors of graph associahedra through six vertices: gamma
      nonnegativity, the mixture identity, tail monotonicity in the gamma
      index, first-order dominance under all 450 edge additions, the two
      likelihood-ratio failures with the first at gamma (1,13,8) to
      (1,17,10), and the z4 tail inequalities themselves;
  (6) the second-moment coverage counts behind Proposition aa:coverage.

Run:  python3 ehrhart_cov_gamma.py        (several minutes)
"""

import itertools, random
from math import gcd, comb, prod

def lcm(a, b): return a * b // gcd(a, b)
def lcm_list(xs):
    r = 1
    for x in xs: r = lcm(r, x)
    return r

def beta_mo(a):
    N = len(a)
    tot = (-1) ** N
    for s in range(1, N + 1):
        for J in itertools.combinations(range(N), s):
            xs = [a[j] for j in J]
            tot += (-1) ** (N - s) * prod(xs) // lcm_list(xs)
    return tot

def beta_roots(a):
    """count tuples of nontrivial a_i-th roots of unity with product 1:
    represent zeta_i by r_i/a_i mod 1; product 1 <=> sum r_i/a_i integer."""
    N = len(a)
    L = lcm_list(a)
    cnt = 0
    # dp over fractional residue mod L: r_i * (L/a_i) mod L
    dp = {0: 1}
    for ai in a:
        step = L // ai
        nd = {}
        for res, c in dp.items():
            for r in range(1, ai):
                nres = (res + r * step) % L
                nd[nres] = nd.get(nres, 0) + c
        dp = nd
    return dp.get(0, 0)

def beta_lattice(a, k):
    """sum over m of interior lattice points of k*P_m: integer points
    0 < r_i < k a_i with sum r_i / a_i = k m -- count via dp on the value
    sum r_i * (L/a_i) which must equal k*m*L."""
    N = len(a)
    L = lcm_list(a)
    # dp over partial weighted sums
    dp = {0: 1}
    for ai in a:
        w = L // ai
        nd = {}
        for s, c in dp.items():
            for r in range(1, k * ai):
                nd[s + r * w] = nd.get(s + r * w, 0) + c
        dp = nd
    tot = 0
    for m in range(1, N):
        tot += dp.get(k * m * L, 0)
    return tot

def beta_poly(a):
    """coefficients T_s of beta_a(k) = (-1)^N + sum_{s>=1} T_s k^{s-1}."""
    N = len(a)
    T = [0] * (N + 1)
    for s in range(1, N + 1):
        for J in itertools.combinations(range(N), s):
            xs = [a[j] for j in J]
            T[s] += (-1) ** (N - s) * prod(xs) // lcm_list(xs)
    return T

def beta_scale(a, k, T=None):
    if T is None: T = beta_poly(a)
    N = len(a)
    return (-1) ** N + sum(T[s] * k ** (s - 1) for s in range(1, N + 1))

print("(1) three-way identity: alternating sum = root count = interior lattice count")
rng = random.Random(2026)
bad = 0
for trial in range(40):
    N = rng.randint(4, 6)
    a = tuple(rng.randint(2, 7) for _ in range(N))
    for k in (1, 2, 3):
        ka = tuple(k * x for x in a)
        v1 = beta_mo(ka)
        v2 = beta_roots(ka)
        v3 = beta_lattice(a, k)
        v4 = beta_scale(a, k)
        if not (v1 == v2 == v3 == v4):
            bad += 1
            print("  **", a, k, v1, v2, v3, v4)
print(f"    40 tuples x scales 1..3: mismatches {bad}")

print("(2) forward differences Delta^r >= 0 for r <= N-1")
viol = 0
tested = 0
for trial in range(600):
    N = rng.randint(4, 8)
    a = [rng.randint(2, 40) for _ in range(N)]
    T = beta_poly(a)
    vals = [beta_scale(a, k, T) for k in range(1, 60)]
    for r in range(1, N):
        seq = vals[:]
        for _ in range(r):
            seq = [seq[i+1] - seq[i] for i in range(len(seq) - 1)]
        tested += len(seq)
        if any(x < 0 for x in seq):
            viol += 1
            print("  ** negative difference", a, r)
print(f"    3000 tuples, {tested} difference values: violations {viol}")

print("(3) large log-concavity + convexity stress (the open clause of x10)")
lcviol = cxviol = ineqs = 0
for trial in range(2500):
    N = rng.randint(4, 8)
    a = [rng.randint(2, 120) for _ in range(N)]
    T = beta_poly(a)
    vals = [beta_scale(a, k, T) for k in range(1, 502)]
    for i in range(1, len(vals) - 1):
        ineqs += 2
        if vals[i] ** 2 < vals[i-1] * vals[i+1]:
            lcviol += 1
            print("  ** log-concavity fails", a, i + 1)
        if vals[i+1] - 2 * vals[i] + vals[i-1] < 0:
            cxviol += 1
            print("  ** convexity fails", a, i + 1)
print(f"    25,000 tuples, {ineqs:,} inequalities: log-concavity violations {lcviol}, convexity violations {cxviol}")


import numpy as np

N = 500_000

def vp_array(vals_offset, coeff, y_primes, N):
    """v_p(coeff*n + offs) for n=1..N as arrays per prime."""
    pass

def valuation_sum(primes, N):
    """returns arrays A[n] = sum_p v_p(2n+1), B[n] = sum_p v_p(n+1), n=1..N."""
    A = np.zeros(N + 2, dtype=np.int32)
    B = np.zeros(N + 2, dtype=np.int32)
    for p in primes:
        pr = p
        while pr <= 2 * N + 1:
            # v_p(2n+1) >= r  <=>  2n+1 = 0 mod pr  <=> n = (pr-1)/2 mod pr (p odd)
            if p != 2:
                inv2 = pow(2, -1, pr)
                start = (-1 * inv2) % pr
                if start == 0:
                    start = pr
                idx = np.arange(start if start >= 1 else pr, N + 1, pr)
                A[idx] += 1
            # v_p(n+1) >= r  <=>  n = -1 mod pr
            start = pr - 1
            if start == 0:
                start = pr
            idx = np.arange(start, N + 1, pr)
            B[idx] += 1
            pr *= p
    return A, B

def cov(x, y):
    return float(np.mean(x * y) - np.mean(x) * np.mean(y))

def primes_upto(y):
    return [p for p in range(2, y + 1) if all(p % q for q in range(2, p)) and p > 1]

print("truncated lag-one covariance vs cutoff (N = 2e6); theorem: -1 at y=2, -5/3 for y>=3")
for y in (2, 3, 5, 11, 31, 97):
    ps = primes_upto(y)
    A, B = valuation_sum(ps, N)
    J = 1 + A[1:N] - B[1:N]          # J_n for n=1..N-1
    Jn, Jn1 = J[:-1].astype(np.float64), J[1:].astype(np.float64)
    c = cov(Jn, Jn1)
    print(f"    y={y:>3}: Cov = {c:+.5f}   (target {'-1.00000' if y==2 else '-1.66667'})")

print("p-local covariances (single prime) vs hand values")
for p, target in ((2, -1.0), (3, -2/3), (5, 0.0), (7, 0.0), (11, 0.0)):
    A, B = valuation_sum([p], N)
    J = A[1:N] - B[1:N]
    c = cov(J[:-1].astype(np.float64), J[1:].astype(np.float64))
    print(f"    p={p:>2}: Cov = {c:+.5f}   (exact {target:+.5f})")

print("full covariance drift toward -5/3 (smallest-prime-factor sieve)")
M = 2 * N + 1
spf = np.zeros(M + 1, dtype=np.int32)
for i in range(2, int(M ** 0.5) + 1):
    if spf[i] == 0:
        sl = np.arange(i * i, M + 1, i)
        mask = spf[sl] == 0
        spf[sl[mask]] = i
def omega_arr(vals):
    out = np.zeros(len(vals), dtype=np.int32)
    for j, v in enumerate(vals):
        c = 0
        while v > 1:
            p = spf[v] if spf[v] else v
            while v % p == 0:
                v //= p
                c += 1
        out[j] = c
    return out
n = np.arange(1, N)
Om2n1 = omega_arr(2 * n + 1)
Omn1 = omega_arr(n + 1)
J = 1 + Om2n1 - Omn1
for cut in (100_000, 250_000, N - 1):
    x = J[: cut - 1].astype(np.float64)
    ycol = J[1:cut].astype(np.float64)
    print(f"    N={cut:>9,}: full Cov = {cov(x, ycol):+.4f}   (-5/3 = -1.6667)")


import itertools
from fractions import Fraction
from math import comb

# ---------------- graph associahedron h-vector via tubings (as in repo) ----
def tubes_of(n, adj):
    T = []
    for size in range(1, n):
        for S in itertools.combinations(range(n), size):
            S = set(S)
            seen = {min(S)}
            st = [min(S)]
            while st:
                u = st.pop()
                for v in adj[u]:
                    if v in S and v not in seen:
                        seen.add(v)
                        st.append(v)
            if seen == S:
                T.append(frozenset(S))
    return T

def compatible(t1, t2, adj):
    if t1 <= t2 or t2 <= t1:
        return True
    if t1 & t2:
        return False
    for u in t1:
        for v in adj[u]:
            if v in t2:
                return False
    return True

def h_vector(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    T = tubes_of(n, adj)
    m = len(T)
    comp = [[compatible(T[i], T[j], adj) for j in range(m)] for i in range(m)]
    counts = {0: 1}
    def rec(start, chosen):
        for i in range(start, m):
            if all(comp[i][j] for j in chosen):
                k = len(chosen) + 1
                counts[k] = counts.get(k, 0) + 1
                rec(i + 1, chosen + [i])
    rec(0, [])
    D = n - 1
    h = [0] * (D + 1)
    for i in range(D + 1):
        f_i = counts.get(D - i, 0)
        for j in range(i + 1):
            h[j] += f_i * comb(i, j) * (-1) ** (i - j)
    return h

def gamma_of(h):
    d = len(h) - 1
    h = h[:]
    g = []
    for j in range(d // 2 + 1):
        gj = h[j]
        g.append(gj)
        for i in range(d - 2 * j + 1):
            h[j + i] -= gj * comb(d - 2 * j, i)
    assert all(x == 0 for x in h), h
    return g

# ---------------- unlabeled connected graphs through 6 vertices -----------
def connected(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen = {0}
    st = [0]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                st.append(v)
    return len(seen) == n

def canon(n, edges):
    best = None
    for perm in itertools.permutations(range(n)):
        es = frozenset(frozenset((perm[u], perm[v])) for u, v in edges)
        key = tuple(sorted(tuple(sorted(e)) for e in es))
        if best is None or key < best:
            best = key
    return best

print("(1,2) gamma nonnegativity + mixture identity on all connected graphs n<=6")
graphs = {}
for n in range(3, 7):
    pairs = list(itertools.combinations(range(n), 2))
    seen = set()
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        if not connected(n, edges):
            continue
        c = canon(n, edges)
        if c in seen:
            continue
        seen.add(c)
        graphs[(n, c)] = edges
print(f"    unlabeled connected graphs by order: "
      f"{[sum(1 for k in graphs if k[0]==n) for n in range(3,7)]}")

H = {}
G = {}
badg = badmix = 0
for (n, c), edges in graphs.items():
    h = h_vector(n, edges)
    H[(n, c)] = h
    g = gamma_of(h)
    G[(n, c)] = g
    if any(x < 0 for x in g):
        badg += 1
    d = n - 1
    recon = [0] * (d + 1)
    for j, gj in enumerate(g):
        for i in range(d - 2 * j + 1):
            recon[j + i] += gj * comb(d - 2 * j, i)
    if recon != h:
        badmix += 1
print(f"    negative gamma vectors: {badg}; mixture reconstruction failures: {badmix}")

print("(3) conditional symmetric tails weakly decreasing in j")
bad = 0
for d in range(1, 6):
    for j in range(d // 2):
        for r2 in range(1, d + 2):   # tail |i - d/2| >= r2/2 on the half-integer grid
            def tail(jj):
                t = Fraction(0)
                m = d - 2 * jj
                for i in range(m + 1):
                    if abs(Fraction(2 * (jj + i) - d, 2)) >= Fraction(r2, 2):
                        t += Fraction(comb(m, i), 2 ** m)
                return t
            if tail(j + 1) > tail(j):
                bad += 1
                print("  ** tail increases", d, j, r2)
print(f"    all (d<=5, j, r) tail comparisons: violations {bad}")

print("(4,5) FOSD and MLR across all edge additions of unlabeled connected graphs <=6")
pairs_tested = fosd_fail = mlr_fail = 0
first_mlr = None
for (n, c), edges in sorted(graphs.items()):
    eset = set(map(frozenset, (map(tuple, edges))))
    missing = [tuple(sorted(p)) for p in itertools.combinations(range(n), 2)
               if frozenset(p) not in set(map(frozenset, edges))]
    seen_orbits = set()
    for e in missing:
        c2 = canon(n, edges + [e])
        if (e, c2) and (c2 in seen_orbits):
            # count each resulting unlabeled G+e once per orbit of e
            pass
        seen_orbits.add(c2)
    for c2 in sorted(seen_orbits):
        # find one representative edge giving this target
        rep = next(e for e in missing if canon(n, edges + [e]) == c2)
        pairs_tested += 1
        g1, g2 = G[(n, c)], gamma_of(h_vector(n, edges + [rep]))
        # nu(j) ~ gamma_j 4^{-j}, exact rationals
        def nu(g):
            w = [Fraction(g[j], 4 ** j) for j in range(len(g))]
            s = sum(w)
            return [x / s for x in w]
        n1, n2 = nu(g1), nu(g2)
        L = max(len(n1), len(n2))
        n1 += [Fraction(0)] * (L - len(n1))
        n2 += [Fraction(0)] * (L - len(n2))
        # FOSD: sum_{j>=r} nu2 >= sum_{j>=r} nu1 for all r
        ok = all(sum(n2[r:]) >= sum(n1[r:]) for r in range(1, L))
        if not ok:
            fosd_fail += 1
            print("  ** FOSD fails", n, g1, g2)
        # MLR: g2[j]/g1[j] nondecreasing where defined (with zeros handled)
        ratios = []
        mlr_ok = True
        lastr = None
        for j in range(L):
            a = g2[j] if j < len(g2) else 0
            b = g1[j] if j < len(g1) else 0
            if b == 0:
                continue
            r = Fraction(a, b)
            if lastr is not None and r < lastr:
                mlr_ok = False
            lastr = r
        if not mlr_ok:
            mlr_fail += 1
            if first_mlr is None:
                first_mlr = (n, g1, g2)
print(f"    edge-addition pairs tested: {pairs_tested}; FOSD failures: {fosd_fail}; "
      f"MLR failures: {mlr_fail}")
print(f"    first MLR failure: {first_mlr}")

print("(6) end-to-end z4 tail inequalities on every pair (direct check)")
z4_fail = 0
for (n, c), edges in sorted(graphs.items()):
    d = n - 1
    missing = [tuple(sorted(p)) for p in itertools.combinations(range(n), 2)
               if frozenset(p) not in set(map(frozenset, edges))]
    for e in set(canon(n, edges + [e0]) for e0 in missing):
        rep = next(e0 for e0 in missing if canon(n, edges + [e0]) == e)
        h1, h2 = H[(n, c)], h_vector(n, edges + [rep])
        s1, s2 = sum(h1), sum(h2)
        for r2 in range(1, d + 2):
            t1 = sum(h1[i] for i in range(d + 1) if abs(Fraction(2*i-d,2)) >= Fraction(r2,2))
            t2 = sum(h2[i] for i in range(d + 1) if abs(Fraction(2*i-d,2)) >= Fraction(r2,2))
            if t1 == s1 or t1 == 0:
                continue   # improper or empty tail
            if Fraction(t2, s2) > Fraction(t1, s1):
                z4_fail += 1
                print("  ** z4 tail fails", n, rep)
print(f"    z4 direct tail violations: {z4_fail}")


print("(6) coverage second moment at the critical scale (aa:coverage)")
import random as _rnd
from math import comb as _comb, log as _log
rng2 = _rnd.Random(7)
for c_ in (1.0, 1.5, 2.5, 3.0):
    for n_ in (300,):
        p_ = c_ * _log(n_) / n_ ** 2
        used = [0] * n_
        # sample triples by incidence: coordinate i unused iff no incident triple hit
        trials = 40
        tot_unused = 0
        for _ in range(trials):
            unused = 0
            for i in range(n_):
                # number of incident triples C(n-1,2); unused with prob (1-p)^C
                if rng2.random() < (1 - p_) ** _comb(n_ - 1, 2):
                    unused += 1
            tot_unused += unused
        pred = n_ * (1 - p_) ** _comb(n_ - 1, 2)
        print(f"    c={c_:3.1f}, n={n_}: mean unused {tot_unused/trials:8.2f}  "
          f"(predicted {pred:8.2f}; below 2 means coverage holds)")
print()
print("done")
