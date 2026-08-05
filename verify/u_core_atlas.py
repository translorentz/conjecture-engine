#!/usr/bin/env python3
"""Part IV (Conjectures 57-76) verification, phase 1: rank formula + atlas tests.

Everything reimplemented from scratch; nothing imported from the bundle.
"""
import itertools, random, sys
from fractions import Fraction
from math import comb

random.seed(20250805)

# ---------- core objects ----------
def adj_masks(n, edges):
    adj = [0] * n
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return adj

def rho(n, adj, S):
    """rho_G(S) = |N[S]| - c(G[S]) for S a bitmask."""
    if S == 0:
        return 0
    NS = S
    c = 0
    rem = S
    while rem:
        v = (rem & -rem).bit_length() - 1
        comp = 1 << v
        frontier = comp
        while frontier:
            newf = 0
            f = frontier
            while f:
                u = (f & -f).bit_length() - 1
                f &= f - 1
                newf |= adj[u] & S & ~comp & ~newf
            comp |= newf
            frontier = newf
        rem &= ~comp
        c += 1
    t = S
    while t:
        v = (t & -t).bit_length() - 1
        t &= t - 1
        NS |= adj[v]
    return bin(NS).count("1") - c

def count_matrix(n, edges):
    """N[k][r] = #{S subset V : |S|=k, rho(S)=r};  returns dict (k,r)->count, and |E|."""
    adj = adj_masks(n, edges)
    N = {}
    for S in range(1 << n):
        k = bin(S).count("1")
        r = rho(n, adj, S)
        N[(k, r)] = N.get((k, r), 0) + 1
    return N

# ---------- 0. rank formula vs direct linear algebra ----------
def matrank_modp(rows, p):
    rows = [r[:] for r in rows]
    rank = 0
    cols = len(rows[0]) if rows else 0
    rr = 0
    for c in range(cols):
        piv = None
        for i in range(rr, len(rows)):
            if rows[i][c] % p:
                piv = i
                break
        if piv is None:
            continue
        rows[rr], rows[piv] = rows[piv], rows[rr]
        inv = pow(rows[rr][c], p - 2, p) if p > 2 else 1
        rows[rr] = [(x * inv) % p for x in rows[rr]]
        for i in range(len(rows)):
            if i != rr and rows[i][c] % p:
                f = rows[i][c] % p
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rr])]
        rr += 1
        rank += 1
    return rank

def adx_rank(n, edges, xvec, p):
    """rank of ad_x on L_G(F_p): matrix rows=edges, cols=vertices; entry for edge {a,b}:
       col b gets +x_a, col a gets -x_b  (from [x, v_j])."""
    rows = []
    for (a, b) in edges:
        row = [0] * n
        row[b] = xvec[a] % p
        row[a] = (-xvec[b]) % p
        rows.append(row)
    if not rows:
        return 0
    return matrank_modp(rows, p)

def test_rank_formula():
    bad = 0
    trials = 0
    for _ in range(300):
        n = random.randint(2, 7)
        pe = random.random()
        edges = [(a, b) for a in range(n) for b in range(a + 1, n) if random.random() < pe]
        adj = adj_masks(n, edges)
        for p in (2, 3, 5):
            for _ in range(20):
                S = random.randint(1, (1 << n) - 1)
                xvec = [0] * n
                t = S
                while t:
                    v = (t & -t).bit_length() - 1
                    t &= t - 1
                    xvec[v] = random.randint(1, p - 1)
                trials += 1
                if adx_rank(n, edges, xvec, p) != rho(n, adj, S):
                    bad += 1
                    if bad <= 3:
                        print("RANK MISMATCH", n, edges, xvec, p)
    print(f"[0] rank formula: {trials} random (graph, x, p) checks, {bad} mismatches")

# ---------- atlas ----------
import networkx as nx
from networkx.generators.atlas import graph_atlas_g

def atlas_graphs():
    out = []
    for G in graph_atlas_g()[1:]:
        n = G.number_of_nodes()
        if n == 0:
            continue
        mapping = {v: i for i, v in enumerate(G.nodes())}
        edges = [(mapping[a], mapping[b]) for a, b in G.edges()]
        out.append((n, tuple(sorted(edges)), G))
    return out

# polynomial helpers: dense int coefficient lists
def padd(a, b):
    if len(a) < len(b):
        a, b = b, a
    out = list(a)
    for i, x in enumerate(b):
        out[i] += x
    return out

def pmul_binom(k, m):
    """Z^k * (1+Z)^m as coeff list."""
    return [0] * k + [comb(m, j) for j in range(m + 1)]

def f_shift_coeffs(N, nE):
    """coefficients of f_G(1+Z) = sum_S Z^{|S|} (1+Z)^{|E|-rho(S)}."""
    out = [0]
    for (k, r), c in N.items():
        term = pmul_binom(k, nE - r)
        out = padd(out, [c * x for x in term])
    return out

def slice_coeffs(N, nE, r0):
    """A_{G,r0}(Z) = sum_{k} N[k][r0] Z^k (1+Z)^{|E|-r0}."""
    out = [0]
    for (k, r), c in N.items():
        if r == r0:
            out = padd(out, [c * x for x in pmul_binom(k, nE - r0)])
    return out

def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a

def logconcave(a, strict=False, interior_only=True):
    a = trim(list(a))
    for i in range(1, len(a) - 1):
        d = a[i] * a[i] - a[i - 1] * a[i + 1]
        if strict:
            if d <= 0:
                return False
        else:
            if d < 0:
                return False
    return True

def lc_transform(a):
    a = trim(list(a))
    return [a[i] * a[i] - (a[i - 1] * a[i + 1] if 0 < i < len(a) - 1 else 0) for i in range(len(a))]

def strict_lc_positions(a):
    """check a_i^2 > a_{i-1} a_{i+1} at every interior i with a_i != 0 -- 'nontrivial' positions."""
    a = trim(list(a))
    for i in range(1, len(a) - 1):
        d = a[i] * a[i] - a[i - 1] * a[i + 1]
        if d <= 0:
            return False, i, a
    return True, None, a

def Cq_vec(N, X):
    """C_G(X,Y) coefficient vector in Y at integer X: v[r] = sum_k N[k][r] (X-1)^k."""
    out = {}
    for (k, r), c in N.items():
        out[r] = out.get(r, 0) + c * (X - 1) ** k
    m = max(out)
    return tuple(out.get(r, 0) for r in range(m + 1))

def Qpoly(n, edges):
    """subgraph-component polynomial data: M[k][c] counts."""
    adj = adj_masks(n, edges)
    M = {}
    for S in range(1 << n):
        k = bin(S).count("1")
        if S == 0:
            c = 0
        else:
            c = 0
            rem = S
            while rem:
                v = (rem & -rem).bit_length() - 1
                comp = 1 << v
                frontier = comp
                while frontier:
                    newf = 0
                    f = frontier
                    while f:
                        u = (f & -f).bit_length() - 1
                        f &= f - 1
                        newf |= adj[u] & S & ~comp & ~newf
                    comp |= newf
                    frontier = newf
                rem &= ~comp
                c += 1
        M[(k, c)] = M.get((k, c), 0) + 1
    return tuple(sorted(M.items()))

def dominationgamma(n, adj):
    full = (1 << n) - 1
    for size in range(0, n + 1):
        for S in itertools.combinations(range(n), size):
            m = 0
            for v in S:
                m |= (1 << v) | adj[v]
            if m == full:
                return size
    return n

def idomination(n, adj):
    full = (1 << n) - 1
    best = n + 1
    for size in range(1, n + 1):
        if size >= best:
            break
        for S in itertools.combinations(range(n), size):
            ok_ind = True
            m = 0
            for v in S:
                if adj[v] & sum(1 << u for u in S):
                    ok_ind = False
                    break
            if not ok_ind:
                continue
            for v in S:
                m |= (1 << v) | adj[v]
            if m == full:
                best = min(best, size)
                break
    return best if best <= n else 0

def main():
    test_rank_formula()

    print("loading atlas...")
    graphs = atlas_graphs()
    data = []
    for n, edges, G in graphs:
        N = count_matrix(n, edges)
        data.append((n, edges, G, N, len(edges)))
    print(f"atlas graphs: {len(data)}")

    # ---- C_G collision classes across atlas (same n) ----
    def Nkey(N):
        return tuple(sorted(N.items()))
    groups = {}
    for i, (n, edges, G, N, nE) in enumerate(data):
        groups.setdefault((n, Nkey(N)), []).append(i)
    collisions = [v for v in groups.values() if len(v) > 1]
    print(f"[collisions] C_G collision classes within atlas (<=7v): {len(collisions)}")

    # C2: does C_G determine Q_G? check collisions
    bad2 = 0
    for cls in collisions:
        qs = {Qpoly(data[i][0], data[i][1]) for i in cls}
        if len(qs) > 1:
            bad2 += 1
            print("  C2 violated on class", [data[i][2].name for i in cls])
    print(f"[C2] Q_G differs within a C_G-collision class: {bad2} violations")

    # C16/C17: domination recovery on collisions
    bad16 = bad17 = 0
    for cls in collisions:
        gs = set()
        is_ = set()
        for i in cls:
            n, edges = data[i][0], data[i][1]
            adj = adj_masks(n, edges)
            gs.add(dominationgamma(n, adj))
            is_.add(idomination(n, adj))
        if len(gs) > 1:
            bad16 += 1
            print("  C16 violated:", [data[i][1] for i in cls], gs)
        if len(is_) > 1:
            bad17 += 1
            print("  C17 violated:", [data[i][1] for i in cls], is_)
    print(f"[C16] gamma differs in C-collision class: {bad16};  [C17] i differs: {bad17}")

    # C5 / C6: two-field & hybrid rigidity (within same n)
    g25, g2Q = {}, {}
    for i, (n, edges, G, N, nE) in enumerate(data):
        g25.setdefault((n, Cq_vec(N, 2), Cq_vec(N, 3)), set()).add(Nkey(N))
        g2Q.setdefault((n, Cq_vec(N, 2), Qpoly(n, edges)), set()).add(Nkey(N))
    v5 = sum(1 for v in g25.values() if len(v) > 1)
    v6 = sum(1 for v in g2Q.values() if len(v) > 1)
    print(f"[C5] (C(2,Y),C(3,Y)) fails to pin C_G: {v5} cases;  [C6] hybrid fails: {v6} cases")

    # C3: global 2-fold log-concavity of f_G(1+Z); C7/C8 strict versions for connected
    bad3 = bad7 = bad8 = 0
    for n, edges, G, N, nE in data:
        a = trim(f_shift_coeffs(N, nE))
        if not (logconcave(a) and logconcave(lc_transform(a))):
            bad3 += 1
            print("  C3 violated:", n, edges)
        if nx.is_connected(G) and nE >= 1:
            ok, i, aa = strict_lc_positions(a)
            if not ok:
                bad7 += 1
                print("  C7 violated:", n, edges, i, aa)
            La = lc_transform(a)
            ok2, i2, _ = strict_lc_positions(La)
            if not ok2:
                bad8 += 1
                print("  C8 violated:", n, edges, i2, trim(La))
    print(f"[C3] {bad3} violations;  [C7] {bad7};  [C8] {bad8} (atlas)")

    # C9: rank-slice strict LC (connected, nonmonomial slices); C10: interval support
    bad9 = bad10 = 0
    for n, edges, G, N, nE in data:
        ranks = sorted({r for (k, r) in N})
        for r0 in ranks:
            ks = sorted(k for (k, r) in N if r == r0)
            if ks != list(range(ks[0], ks[-1] + 1)):
                bad10 += 1
                print("  C10 violated:", n, edges, r0, ks)
            if nx.is_connected(G):
                a = trim(slice_coeffs(N, nE, r0))
                nz = sum(1 for x in a if x)
                if nz > 1:
                    ok, i, aa = strict_lc_positions(a)
                    if not ok:
                        bad9 += 1
                        print("  C9 violated:", n, edges, r0, aa)
    print(f"[C9] {bad9} violations;  [C10] {bad10} violations (atlas)")

    # C4: binary edge-deck reconstruction, graphs with >=4 edges, <=7 vertices
    decks = {}
    for n, edges, G, N, nE in data:
        if nE < 4:
            continue
        deck = []
        for e in edges:
            rest = tuple(x for x in edges if x != e)
            Nd = count_matrix(n, rest)
            deck.append(Cq_vec(Nd, 2))
        key = (n, nE, tuple(sorted(deck)))
        decks.setdefault(key, []).append((n, edges, G))
    bad4 = 0
    for key, lst in decks.items():
        if len(lst) > 1:
            for (n1, e1, G1), (n2, e2, G2) in itertools.combinations(lst, 2):
                if not nx.is_isomorphic(G1, G2):
                    bad4 += 1
                    print("  C4 violated:", e1, "vs", e2)
    print(f"[C4] edge-deck collisions between nonisomorphic graphs (<=7v, >=4 edges): {bad4}")

    print("phase 1 done")

if __name__ == "__main__":
    main()
