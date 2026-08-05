#!/usr/bin/env python3
"""Phase 4: boundary confirmation.
- Exhaustive C-collision search over all trees n=13,14 (fast tree-specific rho DP)
- Tree conjectures C11-C15 at n=13,14 (C12/C13 at q=2,3)
- Exhaustive unicyclic n=10 collision search; C2/C16/C17 on all found collisions
"""
import itertools, random
import u_core_atlas as V
import networkx as nx

def tree_N(n, edges):
    """count matrix via rho(S) = |N[S]| - |S| + edges_in(S) (valid for forests)."""
    adjm = [1 << v for v in range(n)]
    for a, b in edges:
        adjm[a] |= 1 << b
        adjm[b] |= 1 << a
    total = 1 << n
    closed = [0] * total
    ein = [0] * total
    pc = [0] * total
    adj_open = [adjm[v] & ~(1 << v) for v in range(n)]
    for S in range(1, total):
        low = S & (-S)
        v = low.bit_length() - 1
        R = S ^ low
        closed[S] = closed[R] | adjm[v]
        ein[S] = ein[R] + bin(adj_open[v] & R).count("1")
        pc[S] = pc[R] + 1
    N = {(0, 0): 1}
    for S in range(1, total):
        k = pc[S]
        r = bin(closed[S]).count("1") - k + ein[S]
        N[(k, r)] = N.get((k, r), 0) + 1
    return N

def strip_both(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    i = 0
    while i < len(a) and a[i] == 0: i += 1
    return a[i:]

def Nkey(N):
    return tuple(sorted(N.items()))

def rank_dist_int(N, n, q):
    tot = {}
    for (k, r), c in N.items():
        tot[r] = tot.get(r, 0) + c * (q - 1) ** k
    return tot  # denominators q^n common

def majorizes_int(p, r):
    a = sorted(p.values(), reverse=True)
    b = sorted(r.values(), reverse=True)
    L = max(len(a), len(b))
    a += [0] * (L - len(a)); b += [0] * (L - len(b))
    sa = sb = 0
    for x, y in zip(a, b):
        sa += x; sb += y
        if sa < sb:
            return False
    return True

def var_pair(dist, qn):
    # returns (E r^2 * qn^2, (E r)^2 stuff) as exact comparison key: qn^2*Var = qn*sum r^2 c - (sum r c)^2
    s1 = sum(r * c for r, c in dist.items())
    s2 = sum(r * r * c for r, c in dist.items())
    return qn * s2 - s1 * s1

def trees_pass(n, qs=(2, 3)):
    trees = list(nx.nonisomorphic_trees(n))
    print(f"n={n}: {len(trees)} trees")
    info = []
    buckets = {}
    for idx, T in enumerate(trees):
        mapping = {v: i for i, v in enumerate(T.nodes())}
        edges = [(mapping[a], mapping[b]) for a, b in T.edges()]
        N = tree_N(n, edges)
        leaves = sum(1 for v in T.nodes() if T.degree(v) == 1)
        diam = nx.diameter(T)
        svals = len({r for (k, r) in N})
        ispath = max(dict(T.degree()).values()) <= 2
        isstar = leaves == n - 1
        info.append((idx, edges, N, leaves, diam, svals, ispath, isstar))
        buckets.setdefault(Nkey(N), []).append(idx)
    # collision classes
    coll = {k: v for k, v in buckets.items() if len(v) > 1}
    print(f"  C-collision classes among trees n={n}: {len(coll)}")
    for k, v in coll.items():
        print("   collision:", [info[i][1] for i in v])
        # C2/C16/C17 on the collision
        qsx, gsx, isx = set(), set(), set()
        for i in v:
            e = info[i][1]
            adj = V.adj_masks(n, e)
            qsx.add(V.Qpoly(n, e))
            gsx.add(V.dominationgamma(n, adj))
            isx.add(V.idomination(n, adj))
        print("   Q equal:", len(qsx) == 1, " gamma equal:", len(gsx) == 1, " i equal:", len(isx) == 1)
    # C11, C14, C15
    path = next(x for x in info if x[6])
    star = next(x for x in info if x[7])
    ap = strip_both(V.f_shift_coeffs(path[2], n - 1))
    ast = strip_both(V.f_shift_coeffs(star[2], n - 1))
    bad11 = bad14 = bad15 = 0
    for x in info:
        at = strip_both(V.f_shift_coeffs(x[2], n - 1))
        L = max(len(ap), len(at), len(ast))
        a1 = ap + [0]*(L-len(ap)); a2 = at + [0]*(L-len(at)); a3 = ast + [0]*(L-len(ast))
        if not (all(p <= t for p, t in zip(a1, a2)) and all(t <= s for t, s in zip(a2, a3))):
            bad11 += 1; print("  C11 violated:", x[1])
        if (not x[6]) and a2 == a1: bad11 += 1; print("  C11 path-equality violated:", x[1])
        if (not x[7]) and a2 == a3: bad11 += 1; print("  C11 star-equality violated:", x[1])
        s, l, d = x[5], x[3], x[4]
        if s < n - l + 2 or ((s == n - l + 2) != (x[6] or x[7])):
            bad14 += 1; print("  C14 violated:", x[1], s, l)
        if s < d + 1 or ((s == d + 1) != (x[6] or x[7])):
            bad15 += 1; print("  C15 violated:", x[1], s, d)
    # C12/C13 at q in qs
    bad12 = bad13 = 0
    for q in qs:
        qn = q ** n
        dstar = rank_dist_int(star[2], n, q)
        vs = []
        for x in info:
            d = rank_dist_int(x[2], n, q)
            if not majorizes_int(dstar, d):
                bad12 += 1; print("  C12 violated:", q, x[1])
            vs.append((var_pair(d, qn), x[6], x[7], x[0]))
        vmin = min(v[0] for v in vs); vmax = max(v[0] for v in vs)
        mins = [v for v in vs if v[0] == vmin]; maxs = [v for v in vs if v[0] == vmax]
        if not (len(mins) == 1 and mins[0][1]): bad13 += 1; print("  C13 min violated:", q, mins)
        if not (len(maxs) == 1 and maxs[0][2]): bad13 += 1; print("  C13 max violated:", q, maxs)
    print(f"  n={n}: C11bad={bad11} C12bad={bad12} C13bad={bad13} C14bad={bad14} C15bad={bad15}")

def unicyclic10():
    n = 10
    seen = []
    buckets = {}
    trees = list(nx.nonisomorphic_trees(n))
    graphs = []
    sigs = set()
    for T in trees:
        mapping = {v: i for i, v in enumerate(T.nodes())}
        edges = [tuple(sorted((mapping[a], mapping[b]))) for a, b in T.edges()]
        es = set(edges)
        for a in range(n):
            for b in range(a + 1, n):
                if (a, b) in es:
                    continue
                e2 = sorted(es | {(a, b)})
                graphs.append(e2)
    print(f"unicyclic n=10 candidates (with iso duplicates): {len(graphs)}")
    for e in graphs:
        N = V.count_matrix(n, e)
        buckets.setdefault(Nkey(N), []).append(e)
    coll = 0
    bad2 = bad16 = bad17 = bad19 = 0
    # also C19: bucket by C(2,Y)
    b2 = {}
    for key, es in buckets.items():
        Nd = dict(key)
        b2.setdefault(V.Cq_vec(Nd, 2), set()).add(key)
    v19 = sum(1 for s in b2.values() if len(s) > 1)
    print(f"C19 within unicyclic n=10: C(2,Y) classes={len(b2)}, violations={v19}")
    for key, es in buckets.items():
        if len(es) < 2:
            continue
        # check for genuinely nonisomorphic pair
        Gs = []
        for e in es[:40]:
            G = nx.Graph(e); G.add_nodes_from(range(n))
            if not any(nx.is_isomorphic(G, H) for H in Gs):
                Gs.append(G)
        if len(Gs) > 1:
            coll += 1
            qsx, gsx, isx = set(), set(), set()
            for G in Gs:
                e = list(G.edges())
                adj = V.adj_masks(n, e)
                qsx.add(V.Qpoly(n, e))
                gsx.add(V.dominationgamma(n, adj))
                isx.add(V.idomination(n, adj))
            if len(qsx) > 1: bad2 += 1; print("  C2 violated on unicyclic collision")
            if len(gsx) > 1: bad16 += 1; print("  C16 violated")
            if len(isx) > 1: bad17 += 1; print("  C17 violated")
    print(f"unicyclic n=10: nonisomorphic C-collision classes={coll}, C2bad={bad2} C16bad={bad16} C17bad={bad17}")

if __name__ == "__main__":
    unicyclic10()
    trees_pass(13, qs=(2, 3))
    trees_pass(14, qs=(2,))
