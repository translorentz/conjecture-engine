#!/usr/bin/env python3
"""Part VII (Conjectures 117-136) independent reproduction, from scratch.

Reimplements the four exact calibrations -- the Chern-class evaluation, the
Milnor-Orlik formula, F_2 Hochster strands, and signed-orbit counting for
exterior actions -- with no code shared with the deposited scans, and re-tests
a representative finite sample of the twenty conjectures.  Ranges are kept
modest so the script runs in a few minutes; the deposited evidence reaches
much further.
"""
from math import gcd, prod, comb
from itertools import combinations
from functools import reduce
from fractions import Fraction
import random


# ---- Program C calibration: chi via c(TX) = (1+H)^{n+r+1} / prod(1+d_i H) ----
def euler_ci(n, degs):
    r = len(degs)
    num = [comb(n + r + 1, k) for k in range(n + 1)]
    for d in degs:
        out = [0] * (n + 1)
        for k in range(n + 1):
            out[k] = num[k] - d * (out[k - 1] if k else 0)
        num = out
    return prod(degs) * num[n]


def partitions(total, mx=None):
    if mx is None:
        mx = total
    if total == 0:
        yield ()
        return
    for p in range(min(total, mx), 0, -1):
        for rest in partitions(total - p, p):
            yield (p,) + rest


def E(n, degs):
    return (-1) ** n * euler_ci(n, degs)


def multiply_truncated(left, right, degree):
    out = [0] * (degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                out[i + j] += a * b
    return out


def normalized_merge_increment(n, shifted, i, j):
    """Coefficient formula for the normalized Euler increment in C118."""
    degree = n - 2
    a, b = shifted[i], shifted[j]
    series = [(-1) ** k * (k + 1) for k in range(degree + 1)]
    ratios = [a, b, a + b]
    ratios.extend(shifted[k] for k in range(len(shifted)) if k not in (i, j))
    for ratio in ratios:
        series = multiply_truncated(series, [ratio ** k for k in range(degree + 1)], degree)
    return a * b * series[degree]


def main():
    assert euler_ci(3, (5,)) == -200 and euler_ci(2, (4,)) == 24
    assert euler_ci(3, (2, 2, 2, 2)) == -128
    # C117 finite clauses through n=40, C118/119/120 merges through n=18, and C121 gcd law
    Q = {n: E(n, tuple([2] * (n + 1))) for n in range(2, 41)}
    for n in range(5, 39):
        assert Q[n + 1] * Q[n + 1] > 0 and Fraction(Q[n + 1], Q[n]) < 8
        assert Fraction(Q[n + 2], Q[n + 1]) > Fraction(Q[n + 1], Q[n])
    for n in range(2, 21):
        configs = [tuple(e + 1 for e in p) for p in partitions(n + 1)]
        g = reduce(gcd, (abs(euler_ci(n, d)) for d in configs))
        assert g == 24 // gcd(24, n) * (2 if n % 8 in (0, 2) else 1), n   # C121
        if n == 2:
            vals = {d: E(n, d) for d in configs}
            for d in configs:
                for i, j in combinations(range(len(d)), 2):
                    m = tuple(sorted([d[k] for k in range(len(d)) if k not in (i, j)]
                                     + [d[i] + d[j] - 1], reverse=True))
                    increment = Fraction(vals[m], prod(m)) - Fraction(vals[d], prod(d))
                    shifted = tuple(x - 1 for x in d)
                    assert increment == normalized_merge_increment(n, shifted, i, j)
                    assert increment > 0
        if n < 3 or n > 18:
            continue
        vals = {d: E(n, d) for d in configs}
        assert min(vals.values()) == vals[tuple([2] * (n + 1))]           # C120
        assert max(vals.values()) == vals[(n + 2,)]
        for d in configs:
            if len(d) < 2:
                continue
            dm = max(d)
            for i, j in combinations(range(len(d)), 2):
                m = tuple(sorted([d[k] for k in range(len(d)) if k not in (i, j)]
                                 + [d[i] + d[j] - 1], reverse=True))
                increment = Fraction(vals[m], prod(m)) - Fraction(vals[d], prod(d))
                shifted = tuple(x - 1 for x in d)
                assert increment == normalized_merge_increment(n, shifted, i, j)
                assert increment > 0                                            # C118, resolved true
                if dm in (d[i], d[j]):
                    assert vals[m] > vals[d]                              # C119
    for c in range(1, 30):
        for degree in range(40):
            paired = Fraction(c ** (degree + 1) + (-1) ** degree, c + 1)
            assert paired.denominator == 1 and paired >= 0
    print("C117-C121: ladder, exact merge identity (n<=18), extremes, gcd law all pass")

    # ---- Program B calibration: Milnor-Orlik ----
    def beta(a):
        N = len(a)
        tot = (-1) ** N
        for k in range(1, N + 1):
            for J in combinations(a, k):
                l = reduce(lambda x, y: x * y // gcd(x, y), J)
                tot += (-1) ** (N - k) * prod(J) // l
        return tot

    assert beta((2, 3, 5)) == 0 and beta((3, 3, 3, 3)) == 6
    # C122 through cap 16; C124 entries <= 25; C125/126 random scales
    for A in range(9, 17):
        best, args = -1, []
        for a1 in range(2, A + 1):
            for a2 in range(a1, A + 1):
                for a3 in range(a2, A + 1):
                    a4 = A
                    if a4 < a3:
                        continue
                    if Fraction(1, a1) + Fraction(1, a2) + Fraction(1, a3) + Fraction(1, a4) <= 1:
                        continue
                    b = beta((a1, a2, a3, a4))
                    if b > best:
                        best, args = b, [(a1, a2, a3, a4)]
                    elif b == best:
                        args.append((a1, a2, a3, a4))
        assert best == A - 1 and args == [(2, 2, A, A)], (A, best, args)  # C122
    for a1 in range(2, 26):
        for a2 in range(a1, 26):
            for a3 in range(a2, 26):
                for a4 in range(a3, 26):
                    t = (a1, a2, a3, a4)
                    adj = [[gcd(t[i], t[j]) > 1 for j in range(4)] for i in range(4)]
                    seen, stack = {0}, [0]
                    while stack:
                        u = stack.pop()
                        for v in range(4):
                            if adj[u][v] and v not in seen:
                                seen.add(v)
                                stack.append(v)
                    if len(seen) == 4:
                        assert beta(t) >= 1, t                            # C124
    rng = random.Random(11)
    for _ in range(1200):
        N = rng.choice([4, 5, 6])
        base = tuple(sorted(rng.randint(2, 12) for _ in range(N)))
        seq = [beta(tuple(k * x for x in base)) for k in range(1, 11)]
        for k in range(1, 9):
            assert seq[k] >= seq[k - 1]                                   # C125
            assert seq[k] * seq[k] >= seq[k - 1] * seq[k + 1]             # C126
            assert seq[k + 1] - 2 * seq[k] + seq[k - 1] >= 0
    print("C122/124/125/126: cap extremum (A<=16), gcd-graph (<=25), scale laws pass")

    # ---- Program M calibration: F_2 Hochster strands ----
    def cliques(adjmask, verts):
        out = [frozenset()]
        def extend(cur, cand):
            for i, v in enumerate(cand):
                if all(adjmask[v] >> u & 1 for u in cur):
                    nxt = cur | {v}
                    out.append(frozenset(nxt))
                    extend(nxt, cand[i + 1:])
        extend(set(), verts)
        return out

    def f2rank(rows):
        rk = 0
        rows = list(rows)
        while rows:
            p = rows.pop()
            if not p:
                continue
            rk += 1
            low = p & -p
            rows = [r ^ p if r & low else r for r in rows]
        return rk

    def reduced_betti(adjmask, verts):
        cl = cliques(adjmask, verts)
        bydim = {}
        for c in cl:
            bydim.setdefault(len(c) - 1, []).append(c)
        idx = {d: {c: i for i, c in enumerate(cs)} for d, cs in bydim.items()}
        maxd = max(bydim)
        ranks = {}
        for d in range(0, maxd + 1):
            rows = []
            for c in bydim.get(d, []):
                m = 0
                for v in c:
                    m |= 1 << idx[d - 1][c - {v}]
                rows.append(m)
            ranks[d] = f2rank(rows)
        return {d: len(bydim.get(d, [])) - ranks.get(d, 0) - ranks.get(d + 1, 0)
                for d in range(0, maxd + 1)}

    def strands(m, edges):
        adjmask = [0] * m
        for u, v in edges:
            adjmask[u] |= 1 << v
            adjmask[v] |= 1 << u
        h = {}
        for smask in range(1, 1 << m):
            verts = [v for v in range(m) if smask >> v & 1]
            for r, b in reduced_betti(adjmask, verts).items():
                if b:
                    h[(r, len(verts))] = h.get((r, len(verts)), 0) + b
        return h

    assert strands(4, []) == {(0, 2): 6, (0, 3): 8, (0, 4): 3}   # 6z^2+8z^3+3z^4

    def hurwitz_stable(coeffs):
        c = [Fraction(x) for x in coeffs[::-1]]
        n = len(c) - 1
        if n == 0:
            return True
        rows = [c[0::2], c[1::2]]
        while len(rows) <= n:
            a, b = rows[-2], rows[-1]
            if not b or b[0] == 0:
                return False
            nxt = []
            for i in range(1, max(len(a), len(b))):
                ai = a[i] if i < len(a) else Fraction(0)
                bi = b[i] if i < len(b) else Fraction(0)
                nxt.append(ai - a[0] / b[0] * bi)
            while nxt and nxt[-1] == 0:
                nxt.pop()
            if not nxt:
                break
            rows.append(nxt)
        return all(r[0] > 0 for r in rows) and len(rows) == n + 1

    assert hurwitz_stable([2, 2, 1]) and not hurwitz_stable([1, -1, 1])

    def check_graph(m, edges):
        h = strands(m, edges)
        conn = False
        if edges:
            adj = {v: set() for v in range(m)}
            for u, v in edges:
                adj[u].add(v)
                adj[v].add(u)
            seen, st = {0}, [0]
            while st:
                u = st.pop()
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        st.append(v)
            conn = len(seen) == m
        complete = len(edges) == m * (m - 1) // 2
        for r in {r for (r, s) in h}:
            supp = sorted(s for (rr, s) in h if rr == r)
            assert supp == list(range(supp[0], supp[-1] + 1))             # C127
            seq = [h.get((r, s), 0) for s in range(m + 1)]
            for s in range(1, m):
                assert seq[s] ** 2 >= seq[s - 1] * seq[s + 1]             # C128
                if r == 0 and conn and not complete and seq[s - 1] > 0 and seq[s] > 0 and seq[s + 1] > 0:
                    assert seq[s] ** 2 > seq[s - 1] * seq[s + 1]          # C131
            nz = [s for s in range(m + 1) if seq[s]]
            if nz and nz[-1] > nz[0]:
                assert hurwitz_stable(seq[nz[0]:nz[-1] + 1]), (m, edges, r)  # C129
        return h

    for m in range(2, 6):
        pairs = list(combinations(range(m), 2))
        for mask in range(1 << len(pairs)):
            check_graph(m, [pairs[i] for i in range(len(pairs)) if mask >> i & 1])
    rng = random.Random(5)
    pairs6 = list(combinations(range(6), 2))
    for _ in range(150):
        check_graph(6, [p for p in pairs6 if rng.random() < rng.choice([0.3, 0.5, 0.7])])
    # C130 on 2-connected graphs through 5 vertices
    for m in (4, 5):
        cyc = strands(m, [(i, (i + 1) % m) for i in range(m)])
        cycseq = [cyc.get((0, s), 0) for s in range(m + 1)]
        pairs = list(combinations(range(m), 2))
        for mask in range(1 << len(pairs)):
            edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
            adj = {v: set() for v in range(m)}
            for u, v in edges:
                adj[u].add(v)
                adj[v].add(u)
            def connected(vs):
                vs = list(vs)
                seen, st = {vs[0]}, [vs[0]]
                while st:
                    u = st.pop()
                    for v in adj[u]:
                        if v in vs and v not in seen:
                            seen.add(v)
                            st.append(v)
                return len(seen) == len(vs)
            if len(edges) < m or not connected(range(m)):
                continue
            if any(not connected([v for v in range(m) if v != c]) for c in range(m)):
                continue
            h = strands(m, edges)
            assert all(h.get((0, s), 0) <= cycseq[s] for s in range(m + 1))   # C130
    print("C127-C131: strand laws pass (exhaustive m<=5, random m=6, cycles m<=5)")

    # ---- Program T calibration: signed-orbit counting ----
    def wedge_orbits(d, cycles):
        perm, sign = [0] * d, [1] * d
        pos = 0
        for L, sg in cycles:
            idx = list(range(pos, pos + L))
            for i in range(L):
                perm[idx[i]] = idx[(i + 1) % L]
            sign[idx[-1]] = sg
            pos += L
        res = {}
        for k in range(0, d + 1):
            subs = list(combinations(range(d), k))
            index = {S: i for i, S in enumerate(subs)}
            seen = [False] * len(subs)
            pk = nk = 0
            for i, S in enumerate(subs):
                if seen[i]:
                    continue
                cur, sgn, first = S, 1, i
                while True:
                    seen[index[cur]] = True
                    img = [(perm[v], sign[v]) for v in cur]
                    sprod = 1
                    for _, sv in img:
                        sprod *= sv
                    arr = sorted(p for p, _ in img)
                    tgt = [p for p, _ in img]
                    swaps = 0
                    for x in range(len(tgt)):
                        for y in range(len(tgt) - 1 - x):
                            if tgt[y] > tgt[y + 1]:
                                tgt[y], tgt[y + 1] = tgt[y + 1], tgt[y]
                                swaps += 1
                    sgn *= sprod * (-1) ** (swaps % 2)
                    cur = tuple(arr)
                    if index[cur] == first:
                        break
                if sgn > 0:
                    pk += 1
                else:
                    nk += 1
            res[k] = (pk, nk)
        return res

    r = wedge_orbits(4, [(1, -1)] * 4)
    assert [r[k][0] for k in range(5)] == [1, 0, 6, 0, 1]        # -I_4 control

    def types(d):
        for p in partitions(d):
            parts = list(p)
            for smask in range(1 << len(parts)):
                cyc = [(parts[i], -1 if smask >> i & 1 else 1) for i in range(len(parts))]
                det = 1
                for L, sg in cyc:
                    det *= (-1) ** (L - 1) * sg
                if det == 1:
                    yield cyc

    def unimodal(seq):
        i = 0
        while i + 1 < len(seq) and seq[i] <= seq[i + 1]:
            i += 1
        while i + 1 < len(seq) and seq[i] >= seq[i + 1]:
            i += 1
        return i == len(seq) - 1

    minima = {}
    for d in range(2, 11):
        best = None
        for cyc in types(d):
            r = wedge_orbits(d, cyc)
            f = [r[k][0] for k in range(d + 1)]
            neg = [r[k][1] for k in range(d + 1)]
            b = [(f[k] if k <= d else 0) + (f[k - 1] if k >= 1 else 0) for k in range(d + 2)]
            assert unimodal(f[0::2]) and unimodal(f[1::2])       # C132
            assert unimodal(b)                                   # C133
            assert sum(neg) <= sum(b)                            # C136
            tot = sum(b)
            if best is None or tot < best[0]:
                best = (tot, cyc)
        minima[d] = best
    # C134 structure at d=8,9,10
    for d in (8, 9, 10):
        tot, cyc = minima[d]
        pos = [L for L, sg in cyc if sg > 0]
        negs = [L for L, sg in cyc if sg < 0]
        assert len(pos) == (0 if d % 2 == 0 else 1) and len(set(negs)) == len(negs), (d, cyc)
    # C132 boundary: log-concavity of the parity strand fails at d=10, type (8,+)(2,+)
    r = wedge_orbits(10, [(8, 1), (2, 1)])
    f = [r[k][0] for k in range(11)]
    ev = f[0::2]
    assert any(ev[i] ** 2 < ev[i - 1] * ev[i + 1] for i in range(1, len(ev) - 1))
    print(f"C132-C136: monodromy laws pass d<=10; minima {[(d, minima[d][0]) for d in (8, 9, 10)]}")

    print("Part VII representative checks passed")


if __name__ == "__main__":
    main()
