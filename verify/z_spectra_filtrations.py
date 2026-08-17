#!/usr/bin/env python3
"""Part IX (Conjectures 157-176) independent reproduction, from scratch.

Reimplements the four exact calibrations -- tubing enumeration with f-to-h
conversion for graph associahedra, F_2 flag-complex homology of age-filtered
McKay Cayley graphs, deterministic sector convolution for lens-space sine
torsion, and integer boundary matrices with SVD pseudodeterminants for
simplicial spheres -- with no code shared with the deposited scans, and
re-tests a representative finite sample of the twenty conjectures together
with the four retained controls and both log-sine moment identities.
Runs in about ten seconds; the deposited evidence reaches much further."""
import numpy as np
from itertools import combinations
from fractions import Fraction
from math import comb, log, sin, pi, isclose
import random

# ============ Programme I: graph associahedra via tubings ============
def tubes_of(n, adj):
    """proper connected induced subgraphs (as frozensets) of graph on [n]."""
    out = []
    for size in range(1, n):
        for c in combinations(range(n), size):
            cs = set(c)
            seen = {c[0]}; st = [c[0]]
            while st:
                u = st.pop()
                for v in adj[u]:
                    if v in cs and v not in seen:
                        seen.add(v); st.append(v)
            if len(seen) == size:
                out.append(frozenset(c))
    return out

def compatible(t1, t2, adj):
    if t1 <= t2 or t2 <= t1:
        return True
    if t1 & t2:
        return False
    # disjoint: compatible iff no edge between (union not connected-adjacent)
    for u in t1:
        for v in adj[u]:
            if v in t2:
                return False
    return True

def h_vector(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    T = tubes_of(n, adj)
    m = len(T)
    comp = [[compatible(T[i], T[j], adj) for j in range(m)] for i in range(m)]
    counts = {0: 1}   # tubings by size
    def rec(start, chosen):
        for i in range(start, m):
            if all(comp[i][j] for j in chosen):
                k = len(chosen) + 1
                counts[k] = counts.get(k, 0) + 1
                rec(i + 1, chosen + [i])
    rec(0, [])
    D = n - 1
    # h(t) = sum_i f_i (t-1)^i, f_i = #tubings with D-i tubes
    h = [0] * (D + 1)
    for i in range(D + 1):
        f_i = counts.get(D - i, 0)
        for j in range(i + 1):
            h[j] += f_i * comb(i, j) * (-1) ** (i - j)
    return h  # ascending in t

def poly_roots(h):
    return np.roots(h[::-1])

def mahler(h):
    return sum(log(max(1.0, abs(r))) for r in poly_roots(h))

# calibrations: P3 -> pentagon (1,3,1); K3 -> hexagon (1,4,1); P4 -> associahedron (1,6,6,1)? Narayana(4)=1,6,6,1
assert h_vector(3, [(0,1),(1,2)]) == [1,3,1]
assert h_vector(3, [(0,1),(1,2),(0,2)]) == [1,4,1]
assert h_vector(4, [(0,1),(1,2),(2,3)]) == [1,6,6,1]          # Narayana
assert h_vector(4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]) == [1,11,11,1]  # Eulerian K4
print("I-calibration: pentagon (1,3,1), hexagon (1,4,1), Narayana (1,6,6,1), Eulerian (1,11,11,1)")

def connected_graphs(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        adj = [set() for _ in range(n)]
        for u, v in edges: adj[u].add(v); adj[v].add(u)
        seen = {0}; st = [0]
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in seen: seen.add(v); st.append(v)
        if len(seen) == n:
            yield edges

c1bad = c2bad = c3bad = c4bad = 0; n1 = n2 = n3 = 0
H = {}
for n in range(2, 6):
    for edges in connected_graphs(n):
        H[(n, frozenset(edges))] = h_vector(n, edges)
for (n, eset), h in H.items():
    roots = poly_roots(h)
    n1 += 1
    if any(abs(r.imag) > 1e-7 or r.real >= -1e-12 for r in roots): c1bad += 1
    edges = list(eset)
    adj = [set() for _ in range(n)]
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    # C02: connected deletions
    for v0 in range(n):
        rest = [w for w in range(n) if w != v0]
        seen = {rest[0]}; st = [rest[0]]
        while st:
            u = st.pop()
            for w in adj[u]:
                if w != v0 and w in rest and w not in seen: seen.add(w); st.append(w)
        if len(seen) != n - 1 or n - 1 < 2: continue
        relab = {w: i for i, w in enumerate(rest)}
        sub = [(relab[u], relab[w]) for (u, w) in edges if u != v0 and w != v0]
        h2 = H.get((n - 1, frozenset(sub)))
        if h2 is None: h2 = h_vector(n - 1, sub)
        r1 = sorted(r.real for r in poly_roots(h))
        r2 = sorted(r.real for r in poly_roots(h2))
        n2 += 1
        for i in range(len(r2)):
            if not (r1[i] - 1e-7 <= r2[i] <= r1[i + 1] + 1e-7): c2bad += 1; break
    # C03/C04: edge additions
    for e in combinations(range(n), 2):
        if e in eset or (e[1], e[0]) in eset or frozenset() and False: pass
    present = {frozenset(x) for x in eset}
    for e in combinations(range(n), 2):
        if frozenset(e) in present: continue
        h2 = H.get((n, frozenset(list(eset) + [e])))
        if h2 is None: continue
        n3 += 1
        if not mahler(h2) > mahler(h) + 1e-9: c3bad += 1
        # C04 tails (exact integers)
        s1, s2 = sum(h), sum(h2)
        D = n - 1
        for rr in range(1, D + 1):
            t_new = sum(h2[i] for i in range(D + 1) if abs(2 * i - D) >= 2 * rr - (D % 2 == 1))
        # symmetric tails at half-integer radii: use 2|i-c|>=2r style over integer grid
        for twor in range(1, 2 * D + 1):
            tail1 = [i for i in range(D + 1) if abs(2 * i - D) >= twor]
            if not tail1 or len(tail1) == D + 1: continue
            lhs = sum(h2[i] for i in tail1) * s1
            rhs = sum(h[i] for i in tail1) * s2
            if lhs > rhs: c4bad += 1; break
print(f"C01 fails: {c1bad}/{n1} graphs; C02 fails: {c2bad}/{n2} deletions; "
      f"C03 fails: {c3bad}/{n3}; C04 fails: {c4bad} (labelled n<=5)")
# C05 trees through 6
import itertools
def trees(n):
    # all labelled trees via Prufer
    for seq in itertools.product(range(n), repeat=n - 2):
        deg = [1] * n
        for x in seq: deg[x] += 1
        seq2 = list(seq); edges = []
        avail = sorted(i for i in range(n) if deg[i] == 1)
        degc = deg[:]
        import heapq
        heap = [i for i in range(n) if degc[i] == 1]
        heapq.heapify(heap)
        for x in seq2:
            leaf = heapq.heappop(heap)
            edges.append((leaf, x))
            degc[x] -= 1
            if degc[x] == 1: heapq.heappush(heap, x)
        u = heapq.heappop(heap); v = heapq.heappop(heap)
        edges.append((u, v))
        yield edges
c5bad = 0; seen_h = {}
for n in (4, 5, 6):
    path = [(i, i + 1) for i in range(n - 1)]
    star = [(0, i) for i in range(1, n)]
    mp, ms = mahler(h_vector(n, path)), mahler(h_vector(n, star))
    for edges in trees(n):
        key = tuple(sorted(tuple(sorted(e)) for e in edges))
        if key in seen_h: continue
        seen_h[key] = 1
        m = mahler(h_vector(n, list(edges)))
        deg = [0] * n
        for u, v in edges: deg[u] += 1; deg[v] += 1
        is_path = sorted(deg) == [1, 1] + [2] * (n - 2)
        is_star = sorted(deg) == [1] * (n - 1) + [n - 1]
        if m < mp - 1e-9 or m > ms + 1e-9: c5bad += 1
        if not is_path and m <= mp + 1e-9: c5bad += 1
        if not is_star and m >= ms - 1e-9: c5bad += 1
print(f"C05 fails: {c5bad} (all labelled trees n<=6)")

# ============ Programme II: age-filtered McKay flag complexes ============
def f2rank(rows):
    rk = 0; rows = list(rows)
    while rows:
        p = rows.pop()
        if not p: continue
        rk += 1
        low = p & -p
        rows = [r ^ p if r & low else r for r in rows]
    return rk

def flag_betti012(vs, adjset):
    """beta_0, beta_1, beta_2 over F2 of flag complex on vertex list vs."""
    idx = {v: i for i, v in enumerate(vs)}
    edges = [frozenset((u, v)) for u, v in combinations(vs, 2) if v in adjset[u]]
    tris = [frozenset(t) for t in combinations(vs, 3)
            if all(b in adjset[a] for a, b in combinations(t, 2))]
    tets = [frozenset(t) for t in combinations(vs, 4)
            if all(b in adjset[a] for a, b in combinations(t, 2))]
    ei = {e: i for i, e in enumerate(edges)}
    ti = {t: i for i, t in enumerate(tris)}
    d1 = []
    for e in edges:
        m = 0
        for v in e: m |= 1 << idx[v]
        d1.append(m)
    d2 = []
    for t in tris:
        m = 0
        for pair in combinations(sorted(t), 2):
            m |= 1 << ei[frozenset(pair)]
        d2.append(m)
    d3 = []
    for q in tets:
        m = 0
        for tri in combinations(sorted(q), 3):
            m |= 1 << ti[frozenset(tri)]
        d3.append(m)
    r1, r2, r3 = f2rank(d1), f2rank(d2), f2rank(d3)
    b0 = len(vs) - r1
    b1 = len(edges) - r1 - r2
    b2 = len(tris) - r2 - r3
    return b0, b1, b2

def unimodal(seq):
    i = 0
    while i + 1 < len(seq) and seq[i] <= seq[i + 1]: i += 1
    while i + 1 < len(seq) and seq[i] >= seq[i + 1]: i += 1
    return i == len(seq) - 1

def mckay_profiles(p, a):
    d = len(a)
    gens = set()
    for x in a: gens |= {x % p, (-x) % p}
    adjset = {v: set((v + g) % p for g in gens) - {v} for v in range(p)}
    age = {j: sum((j * x) % p for x in a) // p for j in range(1, p)}
    age[0] = 0
    C, B1, B2 = [], [], []
    for k in range(0, d):
        vs = [j for j in range(p) if age[j] <= k]
        if not vs:
            C.append(0); B1.append(0); B2.append(0); continue
        b0, b1, b2 = flag_betti012(vs, adjset)
        C.append(b0); B1.append(b1); B2.append(b2)
    return C, B1, B2

c6b = c7b = c8b = c9b = c10b = 0; nprof = 0
for p in (7, 11, 13):
    units = list(range(1, p))
    for d in range(3, min(p - 1, 8) + 1):
        for a in combinations(units, d):
            if sum(a) % p: continue
            nprof += 1
            C, B1, B2 = mckay_profiles(p, a)
            if not unimodal(C): c6b += 1
            mx = max(C)
            if C.index(mx) > d // 2: c7b += 1
            if d >= 5:
                k = (d + 1) // 2
                vs = [0] + [j for j in range(1, p) if sum((j * x) % p for x in a) // p <= k]
                # recompute b0 at ceil(d/2)
                gens = set()
                for x in a: gens |= {x % p, (-x) % p}
                adjset = {v: set((v + g) % p for g in gens) - {v} for v in range(p)}
                b0, _, _ = flag_betti012(vs, adjset)
                if b0 != 1: c8b += 1
            if not unimodal(B1): c9b += 1
            if not unimodal(B2): c10b += 1
print(f"II: {nprof} exhaustive distinct zero-sum profiles p in {{7,11,13}}, d<=8; "
      f"fails C06={c6b} C07={c7b} C08={c8b} C09={c9b} C10={c10b}")
# retained controls
C, _, _ = mckay_profiles(17, (2, 3, 3, 3, 10, 10, 10, 10))
print("control C06 (17;2,3,3,3,10^4):", C, "non-unimodal:", not unimodal(C))
Cc, _, _ = mckay_profiles(11, (1, 1, 5, 5, 5, 5))
print("control C08 (11;1,1,5^4):", Cc)

# ============ Programme III: sine-torsion sectors ============
def sector_nonempty(p, d, m):
    return d <= m * p <= d * (p - 1)


def sector_data(p, d, s_list):
    w = [2 * sin(pi * j / p) for j in range(1, p)]
    out = {}
    for s in s_list:
        ws = [x ** s for x in w]
        # DP over sum: poly coefficients in q^total, values weight-sums
        tot = [0.0] * (d * (p - 1) + 1)
        cnt = [0.0] * (d * (p - 1) + 1)
        cur = {0: 1.0}
        curc = {0: 1.0}
        # weighted and unweighted counts via convolution
        Wpoly = [0.0] * p
        for j in range(1, p): Wpoly[j] = ws[j - 1]
        Cpoly = [0.0] * p
        for j in range(1, p): Cpoly[j] = 1.0
        def convpow(base, d):
            res = [1.0]
            for _ in range(d):
                new = [0.0] * (len(res) + len(base) - 1)
                for i, a in enumerate(res):
                    if a:
                        for j2, b in enumerate(base):
                            if b: new[i + j2] += a * b
                res = new
            return res
        Wd = convpow(Wpoly, d)
        Cd = convpow(Cpoly, d)
        out[s] = ([Wd[m * p] if m * p < len(Wd) else 0.0 for m in range(d)],
                  [Cd[m * p] if m * p < len(Cd) else 0.0 for m in range(d)])
    return out

c11b = c12b = c15b = 0; n11 = n12 = n15 = 0
for (p, d) in [(7, 4), (11, 4), (11, 5), (13, 5), (13, 6)]:
    data = sector_data(p, d, [1.0, 0.5, -0.5, -1.0])
    # Z(s)_m = Wd[mp]/Cd[mp]
    for s in (1.0, 0.5):
        W, Cn = data[s]
        for m in range(d):
            assert (Cn[m] > 0) == sector_nonempty(p, d, m)
        Z = [W[m] / Cn[m] if Cn[m] else 0 for m in range(d)]
        for m in range(2, d - 1):
            if not all(sector_nonempty(p, d, q) for q in (m - 1, m, m + 1)):
                continue
            n11 += 1
            if not Z[m] ** 2 > Z[m - 1] * Z[m + 1]: c11b += 1
    for s in (-0.5, -1.0):
        W, Cn = data[s]
        Z = [W[m] / Cn[m] if Cn[m] else 0 for m in range(d)]
        for m in range(2, d - 1):
            if not all(sector_nonempty(p, d, q) for q in (m - 1, m, m + 1)):
                continue
            n15 += 1
            if not Z[m] ** 2 < Z[m - 1] * Z[m + 1]: c15b += 1
    # C12: Phi via derivative = E[H] -> use log-weighted convolution
    wlog = [log(2 * sin(pi * j / p)) for j in range(1, p)]
    # E[H] over sector: dp with (count, sum) pairs
    Csum = [0.0] * (d * (p - 1) + 1)
    Ccnt = [0.0] * (d * (p - 1) + 1)
    Ccnt[0] = 1.0
    for _ in range(d):
        ns = [0.0] * len(Csum); nc = [0.0] * len(Ccnt)
        for tot in range(len(Ccnt)):
            if Ccnt[tot] or Csum[tot]:
                for j in range(1, p):
                    ns[tot + j] += Csum[tot] + Ccnt[tot] * wlog[j - 1]
                    nc[tot + j] += Ccnt[tot]
        Csum, Ccnt = ns, nc
    Phi = [Csum[m * p] / Ccnt[m * p] if m * p < len(Ccnt) and Ccnt[m * p] else 0 for m in range(d)]
    for m in range(2, d - 1):
        if not all(sector_nonempty(p, d, q) for q in (m - 1, m, m + 1)):
            continue
        n12 += 1
        if not 2 * Phi[m] > Phi[m - 1] + Phi[m + 1]: c12b += 1
assert not sector_nonempty(5, 11, 2)
print(f"III: C11 fails {c11b}/{n11}; C12 fails {c12b}/{n12}; C15 fails {c15b}/{n15}")
# negative control at (11,4,-2): central curvature positive (log-convexity fails)
data = sector_data(11, 4, [-2.0])
W, Cn = data[-2.0]
Z = [None] + [W[m] / Cn[m] for m in range(1, 4)]
curv = log(Z[2] ** 2 / (Z[1] * Z[3]))
print(f"III control (11,4,s=-2): central log curvature {curv:+.6f} (bundle: +0.4980)")
# centering identity and zeta(3) integral
p = 101
assert isclose(sum(log(2 * sin(pi * j / p)) for j in range(1, p)), log(p), rel_tol=1e-9)
from math import cos
zeta3 = sum(1 / k ** 3 for k in range(1, 200000))

N = 2000000
s_int = 0.0
for i in range(1, N, 2):   # midpoint-ish coarse; use simple midpoint rule
    pass
# midpoint rule with 200k points
M = 200000
s_int = sum(((k + 0.5) / M - 0.5) ** 2 * log(2 * sin(pi * (k + 0.5) / M)) for k in range(M)) / M
print(f"III: centering exact; integral = {s_int:.8f} vs -zeta(3)/(2 pi^2) = {-zeta3/(2*pi**2):.8f}")

# ============ Programme IV: simplicial boundary pseudodeterminants ============
def boundary_matrices(facets):
    """facets: list of sorted tuples (top simplices of a pure complex). Returns dict k->matrix."""
    faces = {}
    dtop = len(facets[0]) - 1
    for k in range(dtop + 1):
        S = set()
        for f in facets:
            for c in combinations(f, k + 1):
                S.add(c)
        faces[k] = sorted(S)
    mats = {}
    for k in range(1, dtop + 1):
        idx = {f: i for i, f in enumerate(faces[k - 1])}
        Mt = np.zeros((len(faces[k - 1]), len(faces[k])))
        for j, f in enumerate(faces[k]):
            for t, drop in enumerate(f):
                sub = tuple(x for x in f if x != drop)
                Mt[idx[sub], j] = (-1) ** t
        mats[k] = Mt
    return mats, faces

def pdet_profile(facets):
    mats, faces = boundary_matrices(facets)
    E = {}; R = {}
    for k, Mt in mats.items():
        ev = np.linalg.eigvalsh(Mt @ Mt.T)
        nz = [x for x in ev if x > 1e-9]
        E[k] = sum(log(x) for x in nz)
        R[k] = len(nz)
    return E, R

def simplex_boundary(d):
    return [tuple(x for x in range(d + 2) if x != i) for i in range(d + 2)]

def cross_polytope(d):
    # vertices 0..2d+1 with pairs (2i,2i+1) antipodal
    facets = []
    for choice in itertools.product(range(2), repeat=d + 1):
        facets.append(tuple(sorted(2 * i + choice[i] for i in range(d + 1))))
    return facets

def stellar(facets, fi, newv):
    f = facets[fi]
    out = [x for i, x in enumerate(facets) if i != fi]
    for drop in f:
        out.append(tuple(sorted([x for x in f if x != drop] + [newv])))
    return out

# calibration: K_n 1-skeleton Laplacian pdet = n^{n-1}
mats, _ = boundary_matrices([tuple(e) for e in combinations(range(5), 2)])
ev = np.linalg.eigvalsh(mats[1] @ mats[1].T)
pd = np.prod([x for x in ev if x > 1e-9])
assert isclose(pd, 5 ** 4, rel_tol=1e-6), pd
print("IV-calibration: pdet(L(K5)) = 5^4 (matrix-tree)")

c16b = c17b = c18b = c19b = c20b = 0
corpus = []
for d in (2, 3, 4):
    corpus.append(("simplex", simplex_boundary(d)))
    corpus.append(("cross", cross_polytope(d)))
rng = random.Random(3)
for d in (2, 3):
    K = simplex_boundary(d)
    nv = d + 2
    for step in range(3):
        K = stellar(K, rng.randrange(len(K)), nv); nv += 1
        corpus.append((f"stacked{d}-{step}", K))
for name, K in corpus:
    E, R = pdet_profile(K)
    dtop = max(E)
    A = {k: E[k] / R[k] for k in E}
    ks = sorted(E)
    for k in ks[1:-1]:
        if E[k] ** 2 < E[k - 1] * E[k + 1] - 1e-6: c16b += 1
    for i in range(len(ks) - 1):
        if A[ks[i]] < A[ks[i + 1]] - 1e-7: c17b += 1
    eq = any(abs(A[ks[i]] - A[ks[i + 1]]) < 1e-7 for i in range(len(ks) - 1))
    if eq != name.startswith("simplex"): c18b += 1
# C19/C20 on subdivision pairs
for d in (2, 3, 4):
    for trial in range(6):
        base = simplex_boundary(d) if trial % 2 == 0 else cross_polytope(d)
        nv = max(max(f) for f in base) + 1
        K = base
        for _ in range(trial % 3):
            K = stellar(K, rng.randrange(len(K)), nv); nv += 1
        K2 = stellar(K, rng.randrange(len(K)), nv)
        E1, _ = pdet_profile(K)
        E2, _ = pdet_profile(K2)
        delta = {k: E2[k] - E1[k] for k in E1}
        ks = sorted(delta)
        for k in ks:
            if delta[k] <= 0: c19b += 1
        for k in ks[1:-1]:
            if delta[k] ** 2 < delta[k - 1] * delta[k + 1] - 1e-6: c20b += 1
print(f"IV: fails C16={c16b} C17={c17b} C18={c18b} C19={c19b} C20={c20b} "
      f"({len(corpus)} spheres + 18 subdivision pairs, d<=4)")
print("done")
