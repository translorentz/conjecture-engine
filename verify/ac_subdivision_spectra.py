#!/usr/bin/env python3
"""Independent verification of the subdivision programme (Conjectures 1, 2, 4).

Barycentric subdivision implemented from scratch as the order complex of the
face poset.  Faces are canonical tuples; sd vertices are faces of the parent.
"""
import math, sys, itertools
import numpy as np

def faces_of(maximal):
    F = set()
    for m in maximal:
        for k in range(1, len(m)+1):
            for c in itertools.combinations(sorted(m), k):
                F.add(c)
    return F

def barycentric(maximal):
    """Return maximal simplices of sd(K): maximal chains of the face poset."""
    out = []
    for m in maximal:
        m = tuple(sorted(m))
        d = len(m) - 1
        # chains sigma_0 < sigma_1 < ... < sigma_d ending at m: built from
        # permutations (add one vertex at a time)
        for perm in itertools.permutations(m):
            chain = tuple(tuple(sorted(perm[:i+1])) for i in range(len(m)))
            out.append(chain)
    return out

def relabel(maximal):
    """Relabel vertex names (which are faces) to integers for the next round."""
    verts = {}
    out = []
    for m in maximal:
        nm = []
        for v in m:
            if v not in verts: verts[v] = len(verts)
            nm.append(verts[v])
        out.append(tuple(sorted(nm)))
    return out, len(verts)

def one_skeleton_degrees(maximal):
    E = set()
    V = set()
    for m in maximal:
        for v in m: V.add(v)
        for u, v in itertools.combinations(m, 2):
            E.add((u, v) if u < v else (v, u))
    deg = {}
    for u, v in E:
        deg[u] = deg.get(u, 0) + 1
        deg[v] = deg.get(v, 0) + 1
    return np.array([deg[v] for v in V]), sorted(E), len(V)

def graph_laplacian(maximal):
    deg, E, n = one_skeleton_degrees(maximal)
    L = np.zeros((n, n))
    for u, v in E:
        L[u, v] -= 1; L[v, u] -= 1
        L[u, u] += 1; L[v, v] += 1
    return L

def stage_degree_moments(start, name, mmax=7, alphas=(1.0, 2.0, 2.5849625007, 3.0, 4.0)):
    """Degree moments over m; report per-step growth ratios of M_alpha."""
    print(f"[deg {name}] alpha_c(2) = log6/log2 = {math.log(6)/math.log(2):.6f}")
    maximal = [tuple(sorted(s)) for s in start]
    prev = {}
    for m in range(mmax+1):
        deg, E, nV = one_skeleton_degrees(maximal)
        row = f"  m={m} |V|={nV} dmax={deg.max()}"
        for a in alphas:
            Ma = float(np.mean(deg.astype(float)**a))
            if a in prev: row += f"  r({a:.2f})={Ma/prev[a]:.4f}"
            prev[a] = Ma
        print(row, flush=True)
        if m < mmax:
            maximal, _ = relabel(barycentric(maximal))
    print(f"  [predicted supercritical ratio at alpha=4: 16/6 = {16/6:.4f}; "
          f"alpha=3: 8/6 = {8/6:.4f}; subcritical ratios -> 1]")

def stage_spectral_moments(start, name, mmax=5):
    """Dense spectral moments up to |V| ~ 4000."""
    maximal = [tuple(sorted(s)) for s in start]
    prevM = {}
    ac = math.log(6)/math.log(2)
    for m in range(mmax+1):
        L = graph_laplacian(maximal)
        n = L.shape[0]
        if n > 4200:
            print(f"  m={m}: |V|={n} too large for dense; stop"); break
        ev = np.linalg.eigvalsh(L)
        ev = np.maximum(ev, 0)
        row = f"  m={m} |V|={n} lmax={ev.max():.3f}"
        for a in (2.0, ac, 4.0):
            Ma = float(np.mean(ev**a))
            tag = f"a={a:.2f}"
            if (m, a) != (0, a) and a in prevM:
                row += f"  M[{tag}]={Ma:.4g} r={Ma/prevM[a]:.4f}"
            else:
                row += f"  M[{tag}]={Ma:.4g}"
            prevM[a] = Ma
        # critical-moment linearity probe: M_ac / (m+1)
        Mc = float(np.mean(ev**ac))
        row += f"  M_ac/(m+1)={Mc/(m+1):.4f}"
        print(row, flush=True)
        if m < mmax:
            maximal, _ = relabel(barycentric(maximal))
    print(f"[spec {name}] predicted: r(a=4) -> 16/6 = {16/6:.4f}; r(a=2) -> bounded; "
          f"M_ac ~ linear in m")

def stage_tail_counts(start, name, mmax=5):
    """Conjecture 4 probe (2D, k=0): N_m(theta) = #{lambda >= 2^(theta m)};
    prediction (1/m) log(N/f0) ~ -theta log 6."""
    maximal = [tuple(sorted(s)) for s in start]
    specs = []
    for m in range(mmax+1):
        L = graph_laplacian(maximal)
        if L.shape[0] > 4200: break
        specs.append(np.maximum(np.linalg.eigvalsh(L), 0))
        if m < mmax:
            maximal, _ = relabel(barycentric(maximal))
    for theta in (0.3, 0.5, 0.7):
        row = f"  theta={theta}: rate(m)="
        for m in range(2, len(specs)):
            ev = specs[m]
            N = int((ev >= 2.0**(theta*m)).sum())
            if N == 0: row += "  -inf"
            else: row += f"  {math.log(N/len(ev))/m:+.3f}"
        row += f"   [predicted -> {-theta*math.log(6):+.3f}]"
        print(row, flush=True)

# ---------- Hodge layer ----------

def boundary_matrices(maximal):
    """Full complex from maximal simplices; return faces by dim and boundary ops."""
    allf = faces_of(maximal)
    dmax = max(len(f) for f in allf) - 1
    bydim = [sorted(f for f in allf if len(f) == k+1) for k in range(dmax+1)]
    idx = [{f: i for i, f in enumerate(fs)} for fs in bydim]
    Bs = []
    for k in range(1, dmax+1):
        B = np.zeros((len(bydim[k-1]), len(bydim[k])))
        for j, f in enumerate(bydim[k]):
            for t in range(len(f)):
                sub = f[:t] + f[t+1:]
                B[idx[k-1][sub], j] = (-1)**t
        Bs.append(B)
    return bydim, Bs

def hodge_laplacians(maximal):
    bydim, Bs = boundary_matrices(maximal)
    dmax = len(bydim) - 1
    Ls = []
    for k in range(dmax+1):
        n = len(bydim[k])
        L = np.zeros((n, n))
        if k >= 1: L += Bs[k-1].T @ Bs[k-1]
        if k < dmax: L += Bs[k] @ Bs[k].T
        Ls.append(L)
    return Ls

def stage_hodge_2d(mmax=4):
    """2D: Delta_1 max should double per step (B=2), Delta_2 bounded (B=1)."""
    maximal = [(0,1,2)]
    for m in range(mmax+1):
        Ls = hodge_laplacians(maximal)
        sizes = [L.shape[0] for L in Ls]
        if max(sizes) > 4500:
            print(f"  m={m}: sizes {sizes} too large; stop"); break
        mx = [float(np.linalg.eigvalsh(L)[-1]) for L in Ls]
        print(f"  m={m} sizes={sizes} max eig: k=0 {mx[0]:.3f}  k=1 {mx[1]:.3f}  k=2 {mx[2]:.3f}", flush=True)
        if m < mmax:
            maximal, _ = relabel(barycentric(maximal))
    print("[hodge2d] predicted late growth factors: k=0: x2, k=1: x2, k=2: bounded")

def stage_hodge_3d(mmax=2):
    """Tetrahedron probe; bundle claims maxima 15->75.06 (k=0,1), 10->15.74 (k=2), 7->7.88 (k=3)."""
    maximal = [(0,1,2,3)]
    for m in range(mmax+1):
        Ls = hodge_laplacians(maximal)
        sizes = [L.shape[0] for L in Ls]
        if max(sizes) > 6000:
            print(f"  m={m}: sizes {sizes} too large; stop"); break
        mx = [float(np.linalg.eigvalsh(L)[-1]) for L in Ls]
        print(f"  m={m} sizes={sizes} max eig: " +
              "  ".join(f"k={k} {v:.4f}" for k, v in enumerate(mx)), flush=True)
        if m < mmax:
            maximal, _ = relabel(barycentric(maximal))
    print("[hodge3d] bundle claims m=1->2: k=0,1: 15->75.06; k=2: 10->15.74; k=3: 7->7.88")

if __name__ == "__main__":
    import time
    t0 = time.time()
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    TRI = [(0,1,2)]
    GLUED = [(0,1,2), (1,2,3)]
    BOOK3 = [(0,1,2), (0,1,3), (0,1,4)]  # three triangles sharing an edge
    if which in ("all", "deg"):
        stage_degree_moments(TRI, "triangle", 7)
        stage_degree_moments(GLUED, "glued", 6)
        stage_degree_moments(BOOK3, "book3", 6)
    if which in ("all", "spec"):
        stage_spectral_moments(TRI, "triangle", 5)
        stage_tail_counts(TRI, "triangle", 5)
    if which in ("all", "hodge"):
        stage_hodge_2d(4)
        stage_hodge_3d(2)
    print(f"done in {time.time()-t0:.1f}s")
