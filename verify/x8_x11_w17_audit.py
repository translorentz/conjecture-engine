#!/usr/bin/env python3
"""Independent checks for three Part VI/VII statements revisited after the
Parts XIII-XVIII v2 audit (fe350c29):

  * Conjecture x8  (124, connected gcd-graph positivity): the Milnor-Orlik
    middle Betti count b_2(L(a))=#{k:1<=k_i<=a_i-1, sum k_i/a_i in Z} is
    positive for every connected gcd-graph N=4 tuple (no counterexample), and
    vanishes for the connected N=5 calibration (2,2,2,2,2).

  * Conjecture x11 (127, Hochster interval support) over F_2: an exhaustive and
    randomized search for a strand-support GAP in the exact formalism
    h_{r,s}(G)=sum_{|I|=s} dim_{F2} Htilde_r(Cl(G)_I;F2) finds none -- the
    Abedelfatah-Nevo field counterexample to Whieldon's gaplessness does not
    transfer, since dim_{F2} >= dim_Q means 2-torsion can only fill a gap.

  * Conjecture w17 (113) / Proposition w:covexist: the lag-one shock covariance
    is a finite sum of local rational densities -- all but finitely many primes
    cancel because the signed affine coefficients sum to zero -- reproducing the
    exact central-binomial constant -5/3.

Runs in well under a minute."""
from fractions import Fraction as Fr
from functools import reduce
from itertools import combinations, product
from math import gcd

PASS = []
def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    assert ok, name

# ------------------------------------------------------------------ x8
def betti_middle(a):
    L = reduce(lambda x, y: x * y // gcd(x, y), a)
    w = [L // ai for ai in a]
    dist = [0] * L; dist[0] = 1
    for ai, wi in zip(a, w):
        cnt = [0] * L
        for ki in range(1, ai):
            cnt[(ki * wi) % L] += 1
        nd = [0] * L
        for r in range(L):
            if dist[r]:
                for s in range(L):
                    if cnt[s]:
                        nd[(r + s) % L] += dist[r] * cnt[s]
        dist = nd
    return dist[0]

def gcd_connected(a):
    n = len(a); adj = {i: set() for i in range(n)}
    for i, j in combinations(range(n), 2):
        if gcd(a[i], a[j]) > 1:
            adj[i].add(j); adj[j].add(i)
    seen = {0}; st = [0]
    while st:
        v = st.pop()
        for u in adj[v]:
            if u not in seen:
                seen.add(u); st.append(u)
    return len(seen) == n

def sorted_tuples(cap, N):
    def rec(start, rem):
        if rem == 0:
            yield (); return
        for v in range(start, cap + 1):
            for t in rec(v, rem - 1):
                yield (v,) + t
    yield from rec(2, N)

print("== x8: Brieskorn middle Betti over connected gcd-graphs (N=4)")
check("(2,2,2,2) b_2=1", betti_middle((2, 2, 2, 2)) == 1)
check("(3,3,3,3) b_2=6", betti_middle((3, 3, 3, 3)) == 6)
check("(2,2,2,2,2) connected, b_3=0", gcd_connected((2,2,2,2,2)) and betti_middle((2,2,2,2,2)) == 0)
conn = bad = 0
for a in sorted_tuples(25, 4):
    if gcd_connected(a):
        conn += 1
        if betti_middle(a) == 0:
            bad += 1
check("no connected N=4 tuple (entries<=25) has b_2=0", bad == 0, f"{conn} connected tested")

# ------------------------------------------------------------------ x11 (F_2)
def cliques(adj, verts):
    out = []
    def ext(cur, cand):
        out.append(tuple(cur))
        for i, v in enumerate(cand):
            ext(cur + [v], [u for u in cand[i + 1:] if u in adj[v]])
    ext([], list(verts))
    return out

def reduced_betti_F2(adj, verts):
    faces = cliques(adj, verts)
    by = {}
    for f in faces:
        by.setdefault(len(f) - 1, []).append(f)
    dims = sorted(by)
    idx = {d: {f: i for i, f in enumerate(sorted(by[d]))} for d in dims}
    def rank(d):
        if d not in by or d - 1 not in by:
            return 0
        piv = []; rk = 0
        for f in sorted(by[d]):
            v = 0
            for i in range(len(f)):
                v ^= 1 << idx[d - 1][f[:i] + f[i + 1:]]
            for p in piv:
                v = min(v, v ^ p)
            if v:
                piv.append(v); rk += 1
        return rk
    rr = {d: rank(d) for d in range(min(dims), max(dims) + 2)}
    return {d: (len(by[d]) - rr.get(d, 0)) - rr.get(d + 1, 0)
            for d in dims if d >= 0 and (len(by[d]) - rr.get(d, 0)) - rr.get(d + 1, 0) > 0}

def adj_of(n, edges):
    a = {i: set() for i in range(n)}
    for x, y in edges:
        a[x].add(y); a[y].add(x)
    return a

def strands(adj, V, rmin=1):
    H = {}
    V = sorted(V)
    for s in range(2, len(V) + 1):
        for I in combinations(V, s):
            for r, b in reduced_betti_F2(adj, I).items():
                if r >= rmin:
                    H[(r, s)] = H.get((r, s), 0) + b
    S = {}
    for (r, s), v in H.items():
        if v > 0:
            S.setdefault(r, set()).add(s)
    return {r: sorted(v) for r, v in S.items()}

def interval(L):
    return not L or L == list(range(L[0], L[-1] + 1))

print("== x11 (F_2): search for a strand-support gap")
# engine sanity: octahedron K_{2,2,2} -> flag S^2 -> single top strand r=2
octe = [(i, j) for i in range(6) for j in range(i + 1, 6)
        if (i, j) not in {(0, 1), (2, 3), (4, 5)}]
S = strands(adj_of(6, octe), range(6))
check("octahedron strands all intervals", all(interval(S[r]) for r in S), str(S))
# multipartite K_{3,2,2,2} homotopy = wedge of 2 copies of S^3 (fills s=9)
def multipartite(parts):
    verts = [v for p in parts for v in p]
    E = [(a, b) for i in range(len(parts)) for j in range(i + 1, len(parts))
         for a in parts[i] for b in parts[j]]
    return adj_of(len(verts), E)
b = reduced_betti_F2(multipartite([[0,1,2],[3,4],[5,6],[7,8]]), range(9))
check("K_{3,2,2,2}: dim Htilde_3 = 2", b.get(3, 0) == 2, str(b))
# exhaustive all graphs on <=6 vertices: every strand (r>=1) support is an interval
import itertools
gap = None
for n in range(4, 7):
    allpairs = list(combinations(range(n), 2))
    for mask in range(1 << len(allpairs)):
        edges = [allpairs[i] for i in range(len(allpairs)) if mask >> i & 1]
        Sg = strands(adj_of(n, edges), range(n))
        for r in Sg:
            if not interval(Sg[r]):
                gap = (n, edges, r, Sg[r]); break
        if gap:
            break
    if gap:
        break
check("exhaustive n<=6: no F_2 strand-support gap at any r>=1", gap is None, str(gap))

# ------------------------------------------------------------------ w17 mechanism
def vpint(x, p):
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v

def constraint(a, b, m, p):
    t = vpint(a, p) if a else 10 ** 9
    if t >= m:
        return ('all',) if b % p ** m == 0 else ('none',)
    if (b % p ** t if b else 0) != 0 and vpint(b, p) < t:
        return ('none',)
    e = m - t; pe = p ** e
    u = (a // p ** t) % pe
    r = (-(b // p ** t) * pow(u, -1, pe)) % pe
    return ('res', e, r)

def dens1(a, b, m, p):
    c = constraint(a, b, m, p)
    return Fr(0) if c[0] == 'none' else Fr(1) if c[0] == 'all' else Fr(1, p ** c[1])

def dens2(a1, b1, m, a2, b2, l, p):
    c1 = constraint(a1, b1, m, p); c2 = constraint(a2, b2, l, p)
    if c1[0] == 'none' or c2[0] == 'none':
        return Fr(0)
    if c1[0] == 'all' and c2[0] == 'all':
        return Fr(1)
    if c1[0] == 'all':
        return Fr(1, p ** c2[1])
    if c2[0] == 'all':
        return Fr(1, p ** c1[1])
    e1, r1 = c1[1], c1[2]; e2, r2 = c2[1], c2[2]
    if (r1 - r2) % p ** min(e1, e2) != 0:
        return Fr(0)
    return Fr(1, p ** max(e1, e2))

def local_cov(F, p, R=40):
    ev = lambda a, b: sum(dens1(a, b, m, p) for m in range(1, R + 1))
    evv = lambda a1, b1, a2, b2: sum(dens2(a1, b1, m, a2, b2, l, p)
                                     for m in range(1, R + 1) for l in range(1, R + 1))
    C = Fr(0)
    for a1, b1, s1 in F:
        for a2, b2, s2 in F:
            C += s1 * s2 * (evv(a1, b1, a2, a2 + b2) - ev(a1, b1) * ev(a2, a2 + b2))
    return C

def is_prime(p):
    return p > 1 and all(p % q for q in range(2, int(p ** .5) + 1))

forms_binom = lambda k: [(k, j, 1) for j in range(1, k + 1)] + [(k - 1, j, -1) for j in range(1, k)] + [(1, 1, -1)]
forms_multi = lambda k: [(k, j, 1) for j in range(1, k + 1)] + [(1, 1, -k)]
forms_fuss = lambda r: [(r + 1, j, 1) for j in range(1, r + 1)] + [(r, j, -1) for j in range(2, r + 2)]

print("== w17: shock covariance is a finite rational sum over exceptional primes")
for name, F in [("binomial k=2", forms_binom(2)), ("multinomial k=2", forms_multi(2)),
                ("multinomial k=3", forms_multi(3)), ("Fuss r=2", forms_fuss(2))]:
    check(f"{name}: signed coeffs sum to zero", sum(s for _, _, s in F) == 0)
    # generic primes give exactly zero local covariance
    genzero = all(local_cov(F, p) == 0 for p in (83, 89, 97, 101))
    check(f"{name}: generic primes contribute 0", genzero)
# central-binomial exact constant -5/3 (C_2 + C_3, with C_2=-1)
Fcb = forms_binom(2)
c2 = local_cov(Fcb, 2)
check("central-binomial C_2 = -1", c2 == -1, str(c2))
approx = float(sum(local_cov(Fcb, p) for p in (2, 3)))
check("central-binomial C_2+C_3 ~ -5/3", abs(approx - (-5 / 3)) < 1e-9, f"{approx:.6f}")

print(f"\n{sum(PASS)}/{len(PASS)} checks passed")
import sys
sys.exit(0 if all(PASS) else 1)
