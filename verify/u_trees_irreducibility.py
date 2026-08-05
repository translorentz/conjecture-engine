#!/usr/bin/env python3
"""Phase 2: C1 irreducibility, tree conjectures C11-C15, majorization C12, variance C13."""
import sys, random
from fractions import Fraction
import u_core_atlas as V
import networkx as nx
import sympy
from sympy import symbols, Poly, ZZ

random.seed(7)
U, Y = symbols("U Y")

def Hpoly(N):
    e = 0
    for (k, r), c in N.items():
        e += c * U**k * Y**r
    return Poly(e, U, Y, domain=ZZ)

def test_C1(maxn=7, sample7=None):
    graphs = [g for g in V.atlas_graphs() if g[0] <= maxn]
    conn = [(n, e, G) for (n, e, G) in graphs if nx.is_connected(G)]
    if sample7 is not None:
        seven = [g for g in conn if g[0] == 7]
        small = [g for g in conn if g[0] < 7]
        conn = small + random.sample(seven, min(sample7, len(seven)))
    bad = 0
    checked = 0
    for n, edges, G in conn:
        N = V.count_matrix(n, edges)
        P = Hpoly(N)
        fl = P.factor_list()
        nontriv = [f for f, m in fl[1] if f.total_degree() > 0]
        irr = (len(nontriv) == 1 and fl[1][0][1] == 1) if nontriv else False
        checked += 1
        if not irr:
            bad += 1
            print("  C1 violated (connected but reducible):", n, edges, fl)
    # disconnected direction: reducible (multiplicativity check on a few)
    for _ in range(20):
        n1, n2 = random.randint(1, 4), random.randint(1, 4)
        e1 = [(a, b) for a in range(n1) for b in range(a + 1, n1) if random.random() < .5]
        e2 = [(a, b) for a in range(n2) for b in range(a + 1, n2) if random.random() < .5]
        Nu = V.count_matrix(n1 + n2, tuple(e1) + tuple((a + n1, b + n1) for a, b in e2))
        if Hpoly(Nu) != Hpoly(V.count_matrix(n1, e1)) * Hpoly(V.count_matrix(n2, e2)):
            print("  multiplicativity FAILS", e1, e2)
    print(f"[C1] connected graphs checked: {checked}, reducible: {bad}; multiplicativity spot-checked")

def tree_edges(T):
    mapping = {v: i for i, v in enumerate(T.nodes())}
    return [(mapping[a], mapping[b]) for a, b in T.edges()]

def strip_both(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    i = 0
    while i < len(a) and a[i] == 0: i += 1
    return a[i:]

def rank_dist(N, n, q):
    tot = {}
    for (k, r), c in N.items():
        tot[r] = tot.get(r, Fraction(0)) + Fraction(c * (q - 1) ** k, q ** n)
    return tot

def majorizes(p, r):
    a = sorted(p.values(), reverse=True)
    b = sorted(r.values(), reverse=True)
    while len(a) < len(b): a.append(Fraction(0))
    while len(b) < len(a): b.append(Fraction(0))
    sa = sb = Fraction(0)
    for x, y in zip(a, b):
        sa += x; sb += y
        if sa < sb:
            return False
    return True

def variance(dist):
    m = sum(r * p for r, p in dist.items())
    return sum(p * (r - m) ** 2 for r, p in dist.items())

def test_trees(maxn=12):
    for n in range(4, maxn + 1):
        trees = list(nx.nonisomorphic_trees(n))
        info = []
        for T in trees:
            edges = tree_edges(T)
            N = V.count_matrix(n, edges)
            a = strip_both(V.f_shift_coeffs(N, n - 1))
            leaves = sum(1 for v in T.nodes() if T.degree(v) == 1)
            diam = nx.diameter(T)
            svals = len({r for (k, r) in N})
            ispath = max(dict(T.degree()).values()) <= 2
            isstar = leaves == n - 1
            info.append((T, edges, N, a, leaves, diam, svals, ispath, isstar))
        path = next(x for x in info if x[7])
        star = next(x for x in info if x[8])
        # C11 coefficientwise
        bad11 = 0
        for x in info:
            ap, at, ast = path[3], x[3], star[3]
            L = max(len(ap), len(at), len(ast))
            ap = ap + [0] * (L - len(ap)); at = at + [0] * (L - len(at)); ast = ast + [0] * (L - len(ast))
            le = all(p <= t for p, t in zip(ap, at)) and all(t <= s for t, s in zip(at, ast))
            if not le:
                bad11 += 1; print("  C11 violated at n=", n, x[1])
            if not x[7] and at == ap: bad11 += 1; print("  C11 path-equality violated", x[1])
            if not x[8] and at == ast: bad11 += 1; print("  C11 star-equality violated", x[1])
        # C12 majorization, C13 variance for q in {2,3,4,5}
        bad12 = bad13 = 0
        if n >= 5:
            for q in (2, 3, 4, 5):
                dstar = rank_dist(star[2], n, q)
                dpath = rank_dist(path[2], n, q)
                vs = []
                for x in info:
                    d = rank_dist(x[2], n, q)
                    if not majorizes(dstar, d):
                        bad12 += 1; print("  C12 violated n,q=", n, q, x[1])
                    vs.append((variance(d), x[7], x[8], x[1]))
                vmin = min(v for v, _, _, _ in vs); vmax = max(v for v, _, _, _ in vs)
                mins = [x for x in vs if x[0] == vmin]; maxs = [x for x in vs if x[0] == vmax]
                if not (len(mins) == 1 and mins[0][1]):
                    bad13 += 1; print("  C13 min not unique path:", n, q, [m[3] for m in mins])
                if not (len(maxs) == 1 and maxs[0][2]):
                    bad13 += 1; print("  C13 max not unique star:", n, q, [m[3] for m in maxs])
        # C14 / C15
        bad14 = bad15 = 0
        for x in info:
            s, l, d = x[6], x[4], x[5]
            if s < n - l + 2:
                bad14 += 1; print("  C14 bound violated:", n, x[1], s, l)
            eq = (s == n - l + 2)
            if eq != (x[7] or x[8]):
                bad14 += 1; print("  C14 equality class violated:", n, x[1], s, l, x[7], x[8])
            if s < d + 1:
                bad15 += 1; print("  C15 bound violated:", n, x[1], s, d)
            eq2 = (s == d + 1)
            if eq2 != (x[7] or x[8]):
                bad15 += 1; print("  C15 equality class violated:", n, x[1], s, d, x[7], x[8])
        print(f"n={n}: trees={len(trees)} C11bad={bad11} C12bad={bad12} C13bad={bad13} C14bad={bad14} C15bad={bad15}")

if __name__ == "__main__":
    test_C1(sample7=200)
    test_trees(12)
