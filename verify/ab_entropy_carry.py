#!/usr/bin/env python3
"""Part XI certification: spectral entropies and multibase carry fields.

Independent verification, sharing no code with the deposited scans, of the
Part XI programmes (Conjectures 197-216, labels ab1-ab20).  The graph half
rebuilds both entropy functionals from scratch (numpy eigensolver on the
trace-normalized Laplacian and distance signless Laplacian) and re-runs the
monotonicity and extremality scans on exhaustive corpora, reproducing the four
retained boundary controls and the exact four-vertex min-entropy tie of
Conjecture 201; it also certifies Proposition ab:deg (the order-two degree
identity and the complete-graph majorization law, numerically).  The carry
half is exact integer arithmetic: valuations from Legendre digit sums, the
exact block-mean formula of Proposition ab:carry verified exhaustively, and
the cross-prime correlation, modular-discrepancy, cumulant, multiplier, and
factorial-ratio diagnostics of Conjectures 208-215.

Dependencies: numpy, networkx.  Default ranges certify the asserted claims on
reduced corpora in a few minutes; pass "full" for the ranges quoted in the
stress-test section (slower).
"""
import math
import sys
import itertools

import numpy as np
import networkx as nx

INF = math.inf
A_ALL = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, INF]


def renyi(p, a):
    p = np.array([x for x in p if x > 1e-13])
    if a == INF:
        return -math.log(p.max())
    if abs(a - 1) < 1e-12:
        return float(-(p * np.log(p)).sum())
    return math.log(float((p ** a).sum())) / (1 - a)


def HL(G, a):
    L = nx.laplacian_matrix(G).toarray().astype(float)
    ev = np.linalg.eigvalsh(L)
    return renyi(ev / ev.sum(), a)


def HQ(G, a):
    D = dict(nx.all_pairs_shortest_path_length(G))
    nodes = list(G.nodes())
    M = np.array([[D[u][v] for v in nodes] for u in nodes], float)
    Q = np.diag(M.sum(1)) + M
    ev = np.linalg.eigvalsh(Q)
    return renyi(ev / ev.sum(), a)


def trees(n):
    return nx.nonisomorphic_trees(n)


def check_prop_deg():
    rng = np.random.default_rng(7)
    for _ in range(40):
        n = int(rng.integers(4, 12))
        G = nx.gnp_random_graph(n, float(rng.uniform(0.3, 0.9)), seed=int(rng.integers(10 ** 6)))
        if not nx.is_connected(G) or G.number_of_edges() == 0:
            continue
        m = G.number_of_edges()
        d2 = sum(d * d for _, d in G.degree())
        assert abs(HL(G, 2.0) + math.log((2 * m + d2) / (2 * m) ** 2)) < 1e-10
        K = nx.complete_graph(n)
        for a in A_ALL:
            assert HQ(G, a) <= HQ(K, a) + 1e-11, (n, a)
    print("Prop ab:deg: order-two degree identity and K_n majorization law: OK")


def check_tie_201():
    C4 = nx.cycle_graph(4)
    paw = nx.star_graph(3)
    paw.add_edge(1, 2)
    evc = sorted(np.linalg.eigvalsh(nx.laplacian_matrix(C4).toarray().astype(float)))
    evp = sorted(np.linalg.eigvalsh(nx.laplacian_matrix(paw).toarray().astype(float)))
    assert np.allclose(evc, [0, 2, 2, 4]) and np.allclose(evp, [0, 1, 3, 4])
    assert abs(HL(C4, INF) - HL(paw, INF)) < 1e-12
    print("ab5 boundary: exact C_4 / S_4^+ min-entropy tie (spectra {0,2,2,4}, {0,1,3,4}): OK")


def scan_trees_extremal(maxn):
    v = t = 0
    for n in range(4, maxn + 1):
        P, S = nx.path_graph(n), nx.star_graph(n - 1)
        hp = {a: HL(P, a) for a in A_ALL}
        hs = {a: HQ(S, a) for a in A_ALL}
        for T in trees(n):
            ispath = nx.is_isomorphic(T, P)
            isstar = nx.is_isomorphic(T, S)
            for a in A_ALL:
                t += 1
                if not ispath:
                    assert HL(T, a) < hp[a] - 1e-11, ("ab1", n, a)
                if not isstar:
                    assert HQ(T, a) < hs[a] - 1e-11, ("ab8", n, a)
    print(f"ab1 path-max and ab8 star-max, trees through {maxn} vertices, {t} comparisons each: OK")


def scan_tree_moves(maxn):
    t2 = t3 = t6 = 0
    for n in range(3, maxn + 1):
        for T in trees(n):
            base = {a: HL(T, a) for a in A_ALL}
            baseq = {a: HQ(T, a) for a in A_ALL}
            leaves = [v for v in T if T.degree(v) == 1]
            for u, v in itertools.combinations(leaves, 2):
                G = T.copy()
                G.add_edge(u, v)
                for a in A_ALL:
                    t2 += 1
                    assert HL(G, a) > base[a] + 1e-11, ("ab2", n, a)
            for e in list(T.edges()):
                G = T.copy()
                w = max(T) + 1
                G.remove_edge(*e)
                G.add_edge(e[0], w)
                G.add_edge(w, e[1])
                for a in A_ALL:
                    t3 += 1
                    assert HL(G, a) > base[a] + 1e-11, ("ab3", n, a)
                    t6 += 1
                    assert HQ(G, a) > baseq[a] + 1e-11, ("ab6s", n, a)
            for u in T.nodes():
                G = T.copy()
                w = max(T) + 1
                G.add_edge(u, w)
                for a in A_ALL:
                    assert HQ(G, a) > baseq[a] + 1e-11, ("ab6p", n, a)
    print(f"ab2 leaf-pair ({t2}), ab3 subdivision ({t3}), ab6 extensions ({t6}+): OK")


def scan_leaf_compression(maxn):
    t = 0
    window = [0.5, 0.75, 1.0, 1.5, 2.0]
    for n in range(4, maxn + 1):
        for T in trees(n):
            for x in [v for v in T if T.degree(v) == 1]:
                u = next(iter(T[x]))
                for v in T[u]:
                    if v == x or T.degree(v) < T.degree(u):
                        continue
                    G = T.copy()
                    G.remove_edge(x, u)
                    G.add_edge(x, v)
                    if nx.is_isomorphic(G, T):
                        continue
                    for a in window:
                        t += 1
                        assert HL(G, a) < HL(T, a) - 1e-11, ("ab4", n, a)
    # retained boundary control: the deposited order-12 tree violates at alpha=0.1
    T = nx.from_graph6_bytes(b"KsaCC@??G@G?")
    worst = None
    for x in [v for v in T if T.degree(v) == 1]:
        u = next(iter(T[x]))
        for v in T[u]:
            if v == x or T.degree(v) < T.degree(u):
                continue
            G = T.copy()
            G.remove_edge(x, u)
            G.add_edge(x, v)
            if nx.is_isomorphic(G, T):
                continue
            d = HL(G, 0.1) - HL(T, 0.1)
            worst = d if worst is None else max(worst, d)
    assert worst > 0, "ab4 boundary control should violate at order 0.1"
    print(f"ab4 window ({t} comparisons): OK; order-0.1 control excess {worst:.3e} (deposited 7.65e-07)")


def unicyclic(n):
    seen = []
    for T in trees(n):
        for u, v in itertools.combinations(list(T.nodes()), 2):
            if T.has_edge(u, v):
                continue
            G = T.copy()
            G.add_edge(u, v)
            if not any(nx.is_isomorphic(G, H) for H in seen):
                seen.append(G)
    return seen


def scan_unicyclic(maxn):
    finite = [a for a in A_ALL if a != INF]
    for n in range(4, maxn + 1):
        C = nx.cycle_graph(n)
        Sp = nx.star_graph(n - 1)
        Sp.add_edge(1, 2)
        hc = {a: HL(C, a) for a in finite}
        hs = {a: HL(Sp, a) for a in finite}
        hcq = {a: HQ(C, a) for a in [1.0, 2.0, 10.0, INF]}
        for G in unicyclic(n):
            iscyc = nx.is_isomorphic(G, C)
            issp = nx.is_isomorphic(G, Sp)
            for a in finite:
                if not iscyc:
                    assert HL(G, a) < hc[a] - 1e-11, ("ab5 cycle", n, a)
                if not issp:
                    assert HL(G, a) > hs[a] + 1e-11, ("ab5 S_n^+", n, a)
            for a in [1.0, 2.0, 10.0, INF]:
                if not iscyc:
                    assert HQ(G, a) < hcq[a] - 1e-11, ("ab11", n, a)
    # retained boundary control for ab11 at alpha=0.1, n=4
    C = nx.cycle_graph(4)
    best = max(HQ(G, 0.1) - HQ(C, 0.1) for G in unicyclic(4) if not nx.is_isomorphic(G, C))
    assert best > 0, "ab11 boundary control should violate at order 0.1"
    print(f"ab5 endpoints and ab11 cycle-max, unicyclic through {maxn} vertices: OK; "
          f"order-0.1 control excess {best:.3e} (deposited 6.62e-04)")


def scan_general_and_bipartite():
    from networkx.generators.atlas import graph_atlas_g
    atlas = [G for G in graph_atlas_g()[1:]
             if G.number_of_nodes() >= 3 and nx.is_connected(G)]
    window = [0.1, 0.5, 1.0, 2.0]
    t7 = 0
    for G in atlas:
        if G.number_of_nodes() > 6:
            continue
        base = {a: HQ(G, a) for a in window}
        for e in list(G.edges()):
            H = G.copy()
            w = max(G) + 1
            H.remove_edge(*e)
            H.add_edge(e[0], w)
            H.add_edge(w, e[1])
            for a in window:
                t7 += 1
                assert HQ(H, a) > base[a] + 1e-11, ("ab7s", a)
        for u in list(G.nodes()):
            H = G.copy()
            w = max(G) + 1
            H.add_edge(u, w)
            for a in window:
                t7 += 1
                assert HQ(H, a) > base[a] + 1e-11, ("ab7p", a)
    # retained high-order controls: subdivisions at order 5 (30 vertices) and
    # order 10 (20 vertices), and a pendant attachment at order 10 (15 vertices),
    # all of which DECREASE H^Q beyond the asserted window
    subdiv_controls = [
        (b"]_A??_G?_???@a?A?@FGE?aO??e@R???O_A@w@O???_HC???A????C?@B_?_@a???O?G@?B@C?",
         5.0, (3, 7), -1.000e-2),
        (b"Sem^vBk]~~RvyWN~~r^uRx|\\nu~nj~}m{", 10.0, (5, 11), -2.019e-3),
    ]
    for g6, alpha, edge, deposited in subdiv_controls:
        G = nx.from_graph6_bytes(g6)
        H = G.copy()
        w = max(G) + 1
        H.remove_edge(*edge)
        H.add_edge(edge[0], w)
        H.add_edge(w, edge[1])
        delta = HQ(H, alpha) - HQ(G, alpha)
        assert abs(delta - deposited) < 5e-4 and delta < 0, ("ab7 subdiv control", alpha, delta)
    G = nx.from_graph6_bytes(b"N{~i^ZHxB~xvyplm[~o")
    base = HQ(G, 10.0)
    best = min(HQ(nx.compose(G, nx.Graph([(u, max(G) + 1)])), 10.0) - base for u in G.nodes())
    assert abs(best - (-2.324e-2)) < 5e-4, ("ab7 pendant control", best)
    print(f"ab7 window, atlas through 6 vertices ({t7} comparisons): OK; "
          f"all three high-order controls negative (pendant {best:.3e})")
    t9 = t10 = 0
    for n in range(4, 8):
        P = nx.path_graph(n)
        hb = HQ(P, 1.0)
        K = nx.complete_bipartite_graph(n // 2, n - n // 2)
        hk = {a: HQ(K, a) for a in [1.0, 1.5, 2.0]}
        for G in (H for H in graph_atlas_g()[1:]
                  if H.number_of_nodes() == n and nx.is_connected(H) and nx.is_bipartite(H)):
            if not nx.is_isomorphic(G, P):
                t9 += 1
                assert HQ(G, 1.0) > hb + 1e-11, ("ab9", n)
            if not nx.is_isomorphic(G, K):
                for a in [1.0, 1.5, 2.0]:
                    t10 += 1
                    assert HQ(G, a) < hk[a] - 1e-11, ("ab10", n, a)
    print(f"ab9 path-min ({t9}) and ab10 biclique-max ({t10}), bipartite through 7 vertices: OK")


# ---------------------------------------------------------------- carry half

def digitsum(n, p):
    s = 0
    while n:
        s += n % p
        n //= p
    return s


def Vp(n, p):
    """v_p(binom(2n,n)) = (2 s_p(n) - s_p(2n)) / (p-1), Legendre/Kummer."""
    return (2 * digitsum(n, p) - digitsum(2 * n, p)) // (p - 1)


def check_block_mean():
    for p, kmax in ((3, 8), (5, 6), (7, 5)):
        for k in (kmax - 1, kmax):
            emp = sum(Vp(n, p) for n in range(p ** k)) / p ** k
            pred = k / 2 - (1 - p ** -k) / (2 * (p - 1))
            assert abs(emp - pred) < 1e-12, (p, k, emp, pred)
    print("Prop ab:carry: exact block mean E V_p = k/2 - (1-p^-k)/(2(p-1)), exhaustive: OK")


def digitsum_vec(m, p):
    s = np.zeros(len(m), dtype=np.int64)
    m = m.copy()
    while m.any():
        s += m % p
        m //= p
    return s


def carry_bulk(N):
    primes = [3, 5, 7, 11]
    n = np.arange(N, dtype=np.int64)
    V = {}
    for p in primes:
        V[p] = ((2 * digitsum_vec(n, p) - digitsum_vec(2 * n, p)) // (p - 1)).astype(float)
    for p in primes:
        slope = V[p].var() / (math.log(N) / math.log(p))
        pred = (p + 1) / (4 * (p - 1))
        assert 0.75 * pred < slope < 1.1 * pred, (p, slope, pred)
    worstc = max(abs(np.corrcoef(V[p], V[q])[0, 1])
                 for i, p in enumerate(primes) for q in primes[i + 1:])
    assert worstc < 0.08, worstc
    worstd = 0.0
    for m1 in (2, 3):
        for i, p in enumerate(primes):
            for q in primes[i + 1:]:
                a = (V[p] % m1).astype(int)
                b = (V[q] % m1).astype(int)
                for x in range(m1):
                    for y in range(m1):
                        worstd = max(worstd, abs(np.mean((a == x) & (b == y)) - 1 / m1 ** 2))
    assert worstd < 0.02, worstd
    zp = V[3] - V[3].mean()
    zq = V[5] - V[5].mean()
    k21 = np.mean(zp * zp * zq)
    assert abs(k21) < 1.0, k21
    print(f"ab12/ab13/ab15/ab17 at N={N}: variance slopes track (p+1)/(4(p-1)), "
          f"max |corr| {worstc:.4f}, max mod-2/3 discrepancy {worstd:.2e}, "
          f"mixed cumulant k(2,1)(3,5) {k21:+.4f}: OK")


def carry_multiplier(N, a=3):
    primes = [3, 5, 7]
    n = np.arange(N, dtype=np.int64)
    V = {}
    for p in primes:
        s = digitsum_vec(n, p)
        sa = digitsum_vec((a - 1) * n, p)
        sb = digitsum_vec(a * n, p)
        V[p] = ((s + sa - sb) // (p - 1)).astype(float)
    worst = max(abs(np.corrcoef(V[p], V[q])[0, 1])
                for i, p in enumerate(primes) for q in primes[i + 1:])
    assert worst < 0.08, worst
    print(f"ab18 multiplier a={a} at N={N}: max |corr| {worst:.4f}: OK")


def carry_landau(N):
    coeffs = [(30, 1), (1, 1), (15, -1), (10, -1), (6, -1)]
    primes = [7, 11]
    n = np.arange(N, dtype=np.int64)
    V = {}
    for p in primes:
        tot = np.zeros(N, dtype=np.int64)
        for c, sgn in coeffs:
            tot += sgn * digitsum_vec(c * n, p)
        val = (-tot) // (p - 1)
        assert (val[1:] >= 0).all()
        V[p] = val.astype(float)
    slopes = {p: V[p].var() / (math.log(N) / math.log(p)) for p in primes}
    corr = np.corrcoef(V[7], V[11])[0, 1]
    assert all(s > 0.1 for s in slopes.values()) and abs(corr) < 0.08
    print(f"ab19 Landau ratio at N={N}: variance slopes {slopes[7]:.3f}, {slopes[11]:.3f}, "
          f"corr {corr:+.4f}: OK")


if __name__ == "__main__":
    import time
    t0 = time.time()
    full = len(sys.argv) > 1 and sys.argv[1] == "full"
    check_prop_deg()
    check_tie_201()
    check_block_mean()
    scan_trees_extremal(11 if full else 10)
    scan_tree_moves(10 if full else 9)
    scan_leaf_compression(10 if full else 9)
    scan_unicyclic(7)
    scan_general_and_bipartite()
    carry_bulk(10 ** 6 if full else 4 * 10 ** 5)
    carry_multiplier(3 * 10 ** 5 if full else 10 ** 5)
    carry_landau(10 ** 5 if full else 4 * 10 ** 4)
    print(f"done in {time.time() - t0:.1f}s")
