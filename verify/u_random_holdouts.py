#!/usr/bin/env python3
"""Phase 3: randomized adversarial holdouts.
- C3/C7/C8/C10 on random graphs (8-10 vertices)
- C18/C19/C20 binary rigidity collision searches (bipartite / connected pseudoforest / chordal)
- C5/C6 two-field & hybrid rigidity on random 8-vertex graphs
- C2/C16/C17 on random-collision corpora
"""
import random, itertools
import u_core_atlas as V
import networkx as nx

random.seed(424242)

def strip_both(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    i = 0
    while i < len(a) and a[i] == 0: i += 1
    return a[i:]

def strict_ok(a):
    a = strip_both(a)
    return all(a[i]*a[i] - a[i-1]*a[i+1] > 0 for i in range(1, len(a)-1))

def lc_ok(a):
    a = strip_both(a)
    return all(a[i]*a[i] - a[i-1]*a[i+1] >= 0 for i in range(1, len(a)-1))

def Nkey(N):
    return tuple(sorted(N.items()))

# ---------- random graph families ----------
def rand_graph(n):
    p = random.uniform(0.15, 0.8)
    return [(a, b) for a in range(n) for b in range(a+1, n) if random.random() < p]

def rand_connected(n):
    while True:
        e = rand_graph(n)
        G = nx.Graph(e); G.add_nodes_from(range(n))
        if nx.is_connected(G):
            return e

def rand_tree_edges(n):
    # random Pruefer
    seq = [random.randrange(n) for _ in range(n-2)] if n > 2 else []
    T = nx.from_prufer_sequence(seq) if n > 2 else nx.path_graph(n)
    return list(T.edges())

def rand_unicyclic(n):
    e = rand_tree_edges(n)
    present = set(map(tuple, map(sorted, e)))
    while True:
        a, b = random.sample(range(n), 2)
        if tuple(sorted((a, b))) not in present:
            return e + [(min(a,b), max(a,b))]

def rand_bipartite(n):
    k = random.randint(1, n-1)
    p = random.uniform(0.2, 0.9)
    return [(a, b) for a in range(k) for b in range(k, n) if random.random() < p]

def rand_chordal(n):
    # incremental: new vertex adjacent to a clique inside neighbourhood-closed prior set
    G = nx.Graph(); G.add_node(0)
    for v in range(1, n):
        # pick random existing vertex u, attach v to a random clique in u's closed neighbourhood
        u = random.randrange(v)
        nb = list(G.neighbors(u))
        clq = {u}
        random.shuffle(nb)
        for w in nb:
            if all(G.has_edge(w, x) for x in clq if x != w):
                if random.random() < 0.6:
                    clq.add(w)
        G.add_node(v)
        for w in clq:
            G.add_edge(v, w)
    assert nx.is_chordal(G)
    return list(G.edges())

# ---------- C3/C7/C8/C10 random ----------
def test_lc_random(trials=2500):
    bad3 = bad7 = bad8 = bad10 = 0
    for t in range(trials):
        n = random.randint(8, 10)
        e = rand_graph(n)
        G = nx.Graph(e); G.add_nodes_from(range(n))
        N = V.count_matrix(n, e)
        nE = len(e)
        a = strip_both(V.f_shift_coeffs(N, nE))
        La = V.lc_transform(list(a))
        if not (lc_ok(a) and lc_ok(La)):
            bad3 += 1; print("  C3 violated:", n, e)
        if nx.is_connected(G) and nE >= 1:
            if not strict_ok(a): bad7 += 1; print("  C7 violated:", n, e)
            if not strict_ok(La): bad8 += 1; print("  C8 violated:", n, e)
        for r0 in sorted({r for (k, r) in N}):
            ks = sorted(k for (k, r) in N if r == r0)
            if ks != list(range(ks[0], ks[-1]+1)):
                bad10 += 1; print("  C10 violated:", n, e, r0, ks)
    print(f"[random n=8-10 x{trials}] C3bad={bad3} C7bad={bad7} C8bad={bad8} C10bad={bad10}")

# ---------- binary rigidity within a family ----------
def binary_rigidity(name, gen, n_range, trials, check_c2_c16_c17=False):
    buckets = {}
    for t in range(trials):
        n = random.choice(n_range)
        e = gen(n)
        N = V.count_matrix(n, e)
        key = (n, V.Cq_vec(N, 2))
        buckets.setdefault(key, {})[Nkey(N)] = e
    viol = 0
    multi = 0
    for key, d in buckets.items():
        if len(d) > 1:
            viol += 1
            if viol <= 3:
                print(f"  {name}: C(2,Y) collision with different C(X,Y):", key[0], list(d.values())[:2])
        elif len(d) == 1:
            pass
    nontrivial = sum(1 for key, d in buckets.items() if len(d) >= 1)
    print(f"[{name} x{trials}] C(2,Y)-buckets={len(buckets)}, violations={viol}")
    return buckets

# ---------- C5/C6 random 8v + C2/C16/C17 via full-C collisions ----------
def test_rigidity_random(trials=6000):
    b25 = {}
    fullC = {}
    for t in range(trials):
        n = 8
        e = rand_graph(n)
        N = V.count_matrix(n, e)
        b25.setdefault((n, V.Cq_vec(N, 2), V.Cq_vec(N, 3)), {})[Nkey(N)] = e
        fullC.setdefault((n, Nkey(N)), []).append(e)
    v5 = sum(1 for d in b25.values() if len(d) > 1)
    print(f"[C5 random 8v x{trials}] two-field buckets={len(b25)}, violations={v5}")
    # C-collision corpora -> C2/C16/C17
    coll = {k: v for k, v in fullC.items() if len(v) > 1}
    bad2 = bad16 = bad17 = 0
    checked = 0
    for (n, _), es in coll.items():
        qs, gs, is_ = set(), set(), set()
        for e in es[:6]:
            adj = V.adj_masks(n, e)
            qs.add(V.Qpoly(n, e))
            gs.add(V.dominationgamma(n, adj))
            is_.add(V.idomination(n, adj))
        checked += 1
        if len(qs) > 1: bad2 += 1; print("  C2 violated:", es[:2])
        if len(gs) > 1: bad16 += 1; print("  C16 violated:", es[:2], gs)
        if len(is_) > 1: bad17 += 1; print("  C17 violated:", es[:2], is_)
    print(f"[C-collision corpora n=8] classes={checked} C2bad={bad2} C16bad={bad16} C17bad={bad17}")

if __name__ == "__main__":
    test_lc_random(2500)
    binary_rigidity("C18 bipartite", rand_bipartite, [9, 10, 11, 12], 6000)
    def pf(n):
        return rand_tree_edges(n) if random.random() < 0.5 else rand_unicyclic(n)
    binary_rigidity("C19 pseudoforest", pf, [10, 11, 12, 13], 6000)
    binary_rigidity("C20 chordal", rand_chordal, [9, 10, 11, 12], 6000)
    test_rigidity_random(6000)
