#!/usr/bin/env python3
"""Independent verification of the UST total-correlation programme (Conjectures 6-10).

All code written from scratch; shares nothing with the bundle's scripts.
C(G) = sum_e h(R_e) - log tau(G), h = binary entropy (nats).
"""
import math, itertools, sys, random
import numpy as np
import networkx as nx

def h(p):
    if p <= 0 or p >= 1: return 0.0
    return -p*math.log(p) - (1-p)*math.log(1-p)

def C_direct(G):
    """Direct: pseudoinverse effective resistances + matrix-tree via eigenvalues."""
    G = nx.convert_node_labels_to_integers(G)
    n = G.number_of_nodes()
    L = nx.laplacian_matrix(G).toarray().astype(float)
    ev = np.linalg.eigvalsh(L)
    logtau = float(np.log(ev[1:]).sum()) - math.log(n)
    P = np.linalg.pinv(L)
    s = 0.0
    for u, v in G.edges():
        R = P[u,u] + P[v,v] - 2*P[u,v]
        s += h(min(1.0, max(0.0, R)))
    return s - logtau

# ---------- formula layer ----------

def C_split(n, r):
    """Complete split S_{n,r} = K_r joined to empty(n-r), via closed formulas."""
    s = n - r
    if r < 1 or s < 1: return None
    if s == 1: return C_complete(n)
    logtau = (r-1)*math.log(n) + (s-1)*math.log(r)
    p_core = 2.0/n
    p_cross = (n + r - 1.0)/(n*r)
    return r*(r-1)/2*h(p_core) + r*s*h(p_cross) - logtau

def C_complete(n):
    logtau = (n-2)*math.log(n)
    return n*(n-1)/2*h(2.0/n) - logtau

def C_bip(n, r):
    s = n - r
    if r < 1 or s < 1: return None
    if r == 1 or s == 1: return 0.0
    logtau = (s-1)*math.log(r) + (r-1)*math.log(s)
    return r*s*h((n-1.0)/(r*s)) - logtau

def C_multipartite(parts):
    parts = tuple(parts); n = sum(parts); k = len(parts)
    if k < 2: return 0.0
    logtau = (k-2)*math.log(n) + sum((a-1)*math.log(n-a) for a in parts if a > 1)
    s = 0.0
    for i in range(k):
        for j in range(i+1, k):
            a, b = parts[i], parts[j]
            R = (1-1.0/a)/(n-a) + (1-1.0/b)/(n-b) + (1.0/a + 1.0/b)/n
            s += a*b*h(R)
    return s - logtau

def C_cycle(n):
    return (n-1)*math.log(n/(n-1.0))

def stage_formulas():
    """Cross-check every closed formula against the direct computation."""
    rng = random.Random(7)
    worst = 0.0
    for _ in range(25):
        k = rng.randint(2, 5)
        parts = [rng.randint(1, 6) for _ in range(k)]
        if sum(parts) < 4 or all(a == 1 for a in parts): continue
        G = nx.complete_multipartite_graph(*parts)
        worst = max(worst, abs(C_multipartite(parts) - C_direct(G)))
    for n, r in [(8,3),(10,2),(12,5),(15,4)]:
        G = nx.complete_multipartite_graph(*([n-r] + [1]*r))
        worst = max(worst, abs(C_split(n, r) - C_direct(G)))
        worst = max(worst, abs(C_bip(n, r) - C_direct(nx.complete_bipartite_graph(r, n-r))))
    for n in (4, 7, 12, 30):
        worst = max(worst, abs(C_cycle(n) - C_direct(nx.cycle_graph(n))))
    print(f"[formulas] multipartite/split/bipartite/cycle closed forms vs direct: max |err| = {worst:.2e}")
    print(f"[numbers ] C(K_2,15) = {C_bip(17,2):.12f}   C(K_3,14) = {C_bip(17,3):.12f}"
          f"   (bundle: 8.315588550473, 8.350120011590)")

# ---------- exhaustive atlas ----------

def stage_atlas():
    from networkx.generators.atlas import graph_atlas_g
    atlas = [g for g in graph_atlas_g()[1:] if g.number_of_nodes() >= 3 and nx.is_connected(g)]
    for n in range(4, 8):
        best, bestG = -1, None
        minbr, minbrG = 1e18, None
        cnt = 0
        for g in atlas:
            if g.number_of_nodes() != n: continue
            cnt += 1
            c = C_direct(g)
            if c > best: best, bestG = c, g
            if not any(nx.bridges(g)):
                if c < minbr - 1e-12: minbr, minbrG = c, g
        # identify the maximizer: is it a complete split graph?
        split_best = max((C_split(n, r), r) for r in range(1, n))
        is_split = any(nx.is_isomorphic(bestG, nx.complete_multipartite_graph(*([n-r]+[1]*r)))
                       for r in range(1, n)) or nx.is_isomorphic(bestG, nx.complete_graph(n))
        cyc_ok = nx.is_isomorphic(minbrG, nx.cycle_graph(n)) and abs(minbr - C_cycle(n)) < 1e-9
        print(f"[atlas n={n}] {cnt} graphs; max C = {best:.6f} split-graph max = {split_best[0]:.6f} "
              f"(r={split_best[1]}) maximizer-is-split: {is_split}; bridgeless min == C_{n}: {cyc_ok}")

# ---------- exhaustive n=8 via geng if available ----------

def stage_geng(n=8):
    import shutil, subprocess
    exe = shutil.which("geng") or shutil.which("nauty-geng")
    if not exe:
        print(f"[geng n={n}] geng unavailable; skipped (atlas covers n<=7)")
        return
    out = subprocess.run([exe, "-c", "-q", str(n)], capture_output=True, text=True).stdout
    best, bestG, minbr, minbrG, cnt = -1, None, 1e18, None, 0
    for line in out.splitlines():
        g = nx.from_graph6_bytes(line.strip().encode())
        cnt += 1
        c = C_direct(g)
        if c > best: best, bestG = c, g
        if not any(nx.bridges(g)) and c < minbr - 1e-12:
            minbr, minbrG = c, g
    split_best = max((C_split(n, r), r) for r in range(1, n))
    is_split = any(nx.is_isomorphic(bestG, nx.complete_multipartite_graph(*([n-r]+[1]*r)))
                   for r in range(1, n)) or nx.is_isomorphic(bestG, nx.complete_graph(n))
    cyc_ok = nx.is_isomorphic(minbrG, nx.cycle_graph(n)) and abs(minbr - C_cycle(n)) < 1e-9
    print(f"[geng n={n}] {cnt} connected graphs; max C = {best:.6f} split max = {split_best[0]:.6f} "
          f"(r={split_best[1]}) maximizer-is-split: {is_split}; bridgeless min == C_{n}: {cyc_ok}")

# ---------- conjecture 10: multipartite partitions ----------

def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, mx), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest

def stage_partitions(nmax=45):
    for n in range(6, nmax+1):
        best, argb = -1, None
        cnt = 0
        for parts in partitions(n):
            if len(parts) < 2: continue
            cnt += 1
            c = C_multipartite(parts)
            if c > best: best, argb = c, parts
        issplit = (len([a for a in argb if a > 1]) <= 1)
        if n % 5 == 0 or not issplit:
            print(f"[partitions n={n}] {cnt} partitions; best = {argb if len(argb)<12 else (argb[0],'1^'+str(len(argb)-1))}"
                  f" C={best:.6f} split-form: {issplit}")
        if not issplit:
            print(f"  *** CONJECTURE 10 COUNTEREXAMPLE at n={n}: {argb}")

# ---------- conjecture 8 adversaries ----------

def theta_graph(i, j, k):
    """Two hubs joined by three paths with i,j,k internal vertices (at most one zero)."""
    G = nx.Graph()
    hub = [0, 1]
    nxt = 2
    for length in (i, j, k):
        prev = 0
        for t in range(length):
            G.add_edge(prev, nxt); prev = nxt; nxt += 1
        G.add_edge(prev, 1)
    return G

def stage_bridgeless_families():
    viol = 0
    # theta graphs up to n = 40
    for n in range(4, 41):
        for i in range(0, n-1):
            for j in range(max(i,1), n-1):
                k = (n-2) - i - j
                if k < j or (i == 0 and j == 0): continue
                if [i,j,k].count(0) > 1: continue
                G = theta_graph(i, j, k)
                if G.number_of_nodes() != n: continue
                c = C_direct(G)
                if c <= C_cycle(n) + 1e-10:
                    viol += 1; print(f"  *** theta({i},{j},{k}) n={n}: C={c:.6f} <= cycle {C_cycle(n):.6f}")
    print(f"[theta] all theta graphs n<=40: violations {viol}")
    # cycle plus one chord across all positions, n<=60 (subset of theta but explicit)
    # prisms, moebius ladders, wheels, K4 subdivisions, complete bipartite K_{2,m}, K_{3,m}, hypercube, random cubic
    viol = 0; tested = 0
    fams = []
    for n in range(3, 31):
        fams.append(("prism", nx.circular_ladder_graph(n)))
        fams.append(("moebius", nx.moebius_kantor_graph() if n == 8 else None))
        fams.append(("wheel", nx.wheel_graph(n+1)))
    for m in range(2, 40):
        fams.append((f"K2{m}", nx.complete_bipartite_graph(2, m)))
    for m in range(3, 25):
        fams.append((f"K3{m}", nx.complete_bipartite_graph(3, m)))
    fams.append(("Q3", nx.hypercube_graph(3)))
    fams.append(("Q4", nx.hypercube_graph(4)))
    fams.append(("petersen", nx.petersen_graph()))
    rng = random.Random(11)
    for i in range(60):
        n = rng.choice(range(6, 61, 2))
        try:
            G = nx.random_regular_graph(3, n, seed=rng.randint(0, 10**6))
            if nx.is_connected(G) and not any(nx.bridges(G)):
                fams.append((f"cubic{n}", G))
        except Exception:
            pass
    for name, G in fams:
        if G is None: continue
        G = nx.convert_node_labels_to_integers(G)
        n = G.number_of_nodes()
        if not nx.is_connected(G) or any(nx.bridges(G)): continue
        tested += 1
        c = C_direct(G)
        if c <= C_cycle(n) + 1e-10 and not nx.is_isomorphic(G, nx.cycle_graph(n)):
            viol += 1; print(f"  *** {name} n={n}: C={c:.6f} <= cycle {C_cycle(n):.6f}")
    print(f"[bridgeless fams] {tested} structured/random bridgeless graphs: violations {viol}")

# ---------- conjecture 6/7 adversaries ----------

def stage_adversaries():
    rng = random.Random(23)
    # (a) split-graph perturbations at n = 40: does anything beat the best split graph?
    for n in (30, 40):
        bestC, bestr = max((C_split(n, r), r) for r in range(2, n-1))
        worst_excess = -1e9
        base = nx.complete_multipartite_graph(*([n-bestr] + [1]*bestr))
        base = nx.convert_node_labels_to_integers(base)
        # core density sweep: remove random core edges
        core = [(u,v) for u,v in base.edges() if base.degree(u) == n-1 and base.degree(v) == n-1]
        for frac in (0.2, 0.5, 0.8, 1.0):
            for _ in range(4):
                G = base.copy()
                for e in rng.sample(core, int(frac*len(core))): G.remove_edge(*e)
                if nx.is_connected(G):
                    worst_excess = max(worst_excess, C_direct(G) - bestC)
        # periphery matchings
        periph = [v for v in base if base.degree(v) == bestr]
        for kk in (1, 3, 6, len(periph)//2):
            G = base.copy()
            pp = rng.sample(periph, 2*kk)
            for t in range(kk): G.add_edge(pp[2*t], pp[2*t+1])
            worst_excess = max(worst_excess, C_direct(G) - bestC)
        # two mesoscopic cores
        r2 = max(2, bestr//2)
        G = nx.Graph()
        A = list(range(r2)); B = list(range(r2, 2*r2)); P = list(range(2*r2, n))
        for u, v in itertools.combinations(A, 2): G.add_edge(u, v)
        for u, v in itertools.combinations(B, 2): G.add_edge(u, v)
        half = len(P)//2
        for v in P[:half]:
            for u in A: G.add_edge(u, v)
        for v in P[half:]:
            for u in B: G.add_edge(u, v)
        G.add_edge(A[0], B[0])
        worst_excess = max(worst_excess, C_direct(G) - bestC)
        print(f"[adv6 n={n}] best split C={bestC:.6f} (r={bestr}); "
              f"max structured-perturbation excess = {worst_excess:.6f} (negative = split wins)")
    # (b) hill climb from random starts, n = 12, 16: does anything beat best split?
    for n in (12, 16):
        bestC, bestr = max((C_split(n, r), r) for r in range(2, n-1))
        record = -1e9
        for trial in range(6):
            G = nx.gnp_random_graph(n, 0.5, seed=rng.randint(0, 10**6))
            while not nx.is_connected(G):
                G = nx.gnp_random_graph(n, 0.5, seed=rng.randint(0, 10**6))
            cur = C_direct(G)
            improved = True
            it = 0
            while improved and it < 400:
                improved = False; it += 1
                pairs = list(itertools.combinations(range(n), 2)); rng.shuffle(pairs)
                for u, v in pairs:
                    H = G.copy()
                    if H.has_edge(u, v):
                        H.remove_edge(u, v)
                        if not nx.is_connected(H): continue
                    else: H.add_edge(u, v)
                    c2 = C_direct(H)
                    if c2 > cur + 1e-12:
                        G, cur, improved = H, c2, True
                        break
            record = max(record, cur)
        print(f"[adv6 climb n={n}] best split={bestC:.6f}; best hill-climb from random starts={record:.6f} "
              f"(<= split expected)")
    # (c) triangle-free adversaries: C5 blowups, Petersen, incomplete bipartite, subdivided splits
    print("[adv7] triangle-free adversaries vs best complete bipartite:")
    for n in (10, 15, 20, 25, 30):
        bestB = max(C_bip(n, r) for r in range(2, n//2+1))
        cands = []
        if n % 5 == 0:
            b = n//5
            cands.append(("C5blowup", nx.complete_multipartite_graph(b,b,b,b,b)))
            # C5 blowup = 5 parts arranged in cycle adjacency
            G = nx.Graph()
            parts = [list(range(i*b, (i+1)*b)) for i in range(5)]
            for i in range(5):
                for u in parts[i]:
                    for v in parts[(i+1) % 5]: G.add_edge(u, v)
            cands.append(("C5blow_cyc", G))
        if n == 10: cands.append(("petersen", nx.petersen_graph()))
        best_r = max(range(2, n//2+1), key=lambda r: C_bip(n, r))
        Kb = nx.complete_bipartite_graph(best_r, n-best_r)
        for frac in (0.05, 0.15):
            G = Kb.copy()
            ee = list(G.edges())
            for e in rng.sample(ee, max(1, int(frac*len(ee)))):
                G.remove_edge(*e)
            if nx.is_connected(G): cands.append((f"Kbip-{frac}", G))
        worst = -1e9; who = ""
        for name, G in cands:
            G = nx.convert_node_labels_to_integers(G)
            if not nx.is_connected(G): continue
            # triangle-free check
            if any(len(set(G[u]) & set(G[v])) > 0 for u, v in G.edges()): continue
            ex = C_direct(G) - bestB
            if ex > worst: worst, who = ex, name
        print(f"   n={n}: best K_r,s = {bestB:.6f}; max adversary excess = {worst:.6f} ({who})")

# ---------- asymptotics ----------

def stage_asymptotics():
    print("[asym] split-family exact optimum vs predicted scales:")
    for n in (10**4, 10**5, 10**6, 10**7):
        lo, hi = 2, int(8*math.sqrt(n/math.log(n))) + 50
        # ternary-ish search then local scan (C_split unimodal in r empirically)
        rs = range(lo, hi)
        bestr = max(rs, key=lambda r: C_split(n, r))
        bestC = C_split(n, bestr)
        scale = math.sqrt(n/math.log(n))
        deficit = n - bestC
        print(f"   n=1e{int(math.log10(n))}: r*={bestr}  r*/sqrt(n/ln n)={bestr/scale:.4f}  "
              f"deficit/(sqrt(n ln n))={deficit/math.sqrt(n*math.log(n)):.4f}")
        approx = bestr*math.log(n/bestr) + n/(2*bestr)
        print(f"        two-term model deficit={approx:.1f} true={deficit:.1f} ratio={approx/deficit:.4f}")
    # bipartite family: same for conjecture 7 + r=2->3 crossover at n=17
    for n in (16, 17, 18):
        vals = [(C_bip(n, r), r) for r in range(2, n//2+1)]
        c, r = max(vals)
        print(f"[bip n={n}] best r = {r} (C={c:.6f})  [expect switch 2->3 at n=17]")
    for n in (10**5, 10**6):
        bestr = max(range(2, int(8*math.sqrt(n/math.log(n)))+50), key=lambda r: C_bip(n, r))
        print(f"[bip n=1e{int(math.log10(n))}] r*={bestr} r*/sqrt(n/ln n)={bestr/math.sqrt(n/math.log(n)):.4f} "
              f"split-minus-bip at opt = {C_split(n,max(2,bestr)) - C_bip(n,bestr):.4f}")

if __name__ == "__main__":
    import time
    t0 = time.time()
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "a"):
        stage_formulas(); stage_atlas(); stage_geng(8)
    if which in ("all", "b"):
        stage_partitions(45); stage_asymptotics()
    if which in ("all", "c"):
        stage_bridgeless_families()
    if which in ("all", "d"):
        stage_adversaries()
    print(f"done in {time.time()-t0:.1f}s")
