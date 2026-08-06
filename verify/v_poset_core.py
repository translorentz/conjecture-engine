#!/usr/bin/env python3
"""Part V (Conjectures 77-96) verification core: poset pattern Lie algebras and their
adjoint / Kirillov rank enumerators, reimplemented from scratch.

L_P(F_q) = span{ e_{ij} : i <_P j } with matrix-unit bracket
    [e_{ij}, e_{kl}] = delta_{jk} e_{il} - delta_{li} e_{kj}.
A_{P,q}(T) = sum_{x in L_P} T^{rank ad_x},  K_{P,q}(T) = sum_{f in L_P^*} T^{rank B_f},
B_f(u,v) = f([u,v]).

Nothing here is imported from the uploaded bundle; poset generation is independent.
"""
import itertools
from functools import lru_cache

# ---------- independent poset generation (naturally labelled, then dedup up to iso) ----------
def gen_labelled_posets(n):
    """All transitively closed, irreflexive, antisymmetric relations on [n] using only
    upper-triangular pairs (i<j): these are exactly the naturally labelled posets on n points."""
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    out = []
    # DFS over including/excluding each pair, pruning on transitivity closure
    def closure_ok(rel):
        # rel is a set of (i,j) i<j; check transitively closed
        for (i, j) in rel:
            for (j2, k) in rel:
                if j == j2 and (i, k) not in rel:
                    return False
        return True
    # brute force is fine for n<=5 (2^10 = 1024 subsets at n=5)
    for bits in range(1 << len(pairs)):
        rel = frozenset(pairs[t] for t in range(len(pairs)) if bits >> t & 1)
        if closure_ok(rel):
            out.append(rel)
    return out

def poset_leq_matrix(n, rel):
    """strict-less relation as function i<j (poset order), rel is set of (i,j) i<j numeric with i<_P j."""
    return rel

def canon(n, rel):
    """canonical form of poset under relabelling (min over permutations of the sorted comparability set,
    encoded so that the natural-labelling constraint is dropped)."""
    best = None
    verts = list(range(n))
    # full order relation as set of ordered pairs (a<_P b)
    order = set(rel)  # all (i,j) with i<j numeric and i<_P j; since naturally labelled, i<_P j => i<j numeric
    for perm in itertools.permutations(verts):
        # relabel: vertex v -> perm[v]; a <_P b becomes perm[a] <_P perm[b]
        mapped = frozenset((perm[a], perm[b]) for (a, b) in order)
        # encode as sorted tuple
        key = tuple(sorted(mapped))
        if best is None or key < best:
            best = key
    return best

def gen_unlabeled_posets(n):
    seen = {}
    for rel in gen_labelled_posets(n):
        c = canon(n, rel)
        if c not in seen:
            seen[c] = (n, rel)
    return list(seen.values())

# ---------- Lie algebra construction ----------
def build_algebra(n, rel):
    """basis = list of (i,j); return basis, adB (list of m x m matrices over Z, ad_{e_a}),
    kirstruct[k][a][b] = coeff of e_k in [e_a,e_b]."""
    basis = sorted(rel)  # (i,j) pairs that are order relations
    m = len(basis)
    idx = {p: a for a, p in enumerate(basis)}
    # bracket [e_a,e_b] -> list of (target, coeff)
    br = [[None] * m for _ in range(m)]
    for a in range(m):
        i, j = basis[a]
        for b in range(m):
            k, l = basis[b]
            terms = {}
            if j == k and (i, l) in idx:
                terms[idx[(i, l)]] = terms.get(idx[(i, l)], 0) + 1
            if l == i and (k, j) in idx:
                terms[idx[(k, j)]] = terms.get(idx[(k, j)], 0) - 1
            br[a][b] = terms
    # adB[a] : matrix of ad_{e_a}, column b -> br[a][b]
    adB = []
    for a in range(m):
        M = [[0] * m for _ in range(m)]
        for b in range(m):
            for t, c in br[a][b].items():
                M[t][b] += c
        adB.append(M)
    # kir[k][a][b] = coeff of e_k in [e_a,e_b]
    kir = [[[0] * m for _ in range(m)] for _ in range(m)]
    for a in range(m):
        for b in range(m):
            for t, c in br[a][b].items():
                kir[t][a][b] += c
    return basis, m, br, adB, kir

# ---------- rank over F_p ----------
def rank_mod(rows, m, p):
    rows = [r[:] for r in rows]
    r = 0
    for c in range(m):
        if r >= m:
            break
        piv = -1
        for i in range(r, len(rows)):
            if rows[i][c] % p:
                piv = i
                break
        if piv < 0:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c] % p, p - 2, p)
        rows[r] = [(x * inv) % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % p:
                f = rows[i][c] % p
                rows[i] = [(rows[i][j] - f * rows[r][j]) % p for j in range(m)]
        r += 1
    return r

def rank_f2(rows, m):
    """fast GF(2) rank via bitmask ints; rows given as list of int bitmasks."""
    basis = []
    for v in rows:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
    return len(basis)

# ---------- enumerators ----------
def enumerators(m, adB, kir, p):
    """return A (list len m+1) and K (list len m+1) rank counts, over all p^m elements."""
    A = [0] * (m + 1)
    K = [0] * (m + 1)
    if m == 0:
        A[0] = 1; K[0] = 1
        return A, K
    coeffs = [0] * m
    total = p ** m
    if p == 2:
        # bit-packed rows
        for _ in range(total):
            # ad_x = sum coeffs[a]*adB[a]  (coeffs in {0,1})
            adrows = [0] * m
            kirrows = [0] * m
            for a in range(m):
                if coeffs[a]:
                    Ma = adB[a]
                    Ka = kir[a]
                    for i in range(m):
                        ri = 0
                        Mi = Ma[i]
                        for j in range(m):
                            if Mi[j] & 1:
                                ri |= 1 << j
                        adrows[i] ^= ri
                        rk = 0
                        Ki = Ka[i]
                        for j in range(m):
                            if Ki[j] & 1:
                                rk |= 1 << j
                        kirrows[i] ^= rk
            A[rank_f2(adrows, m)] += 1
            K[rank_f2(kirrows, m)] += 1
            # increment
            pos = 0
            while pos < m:
                coeffs[pos] ^= 1
                if coeffs[pos]:
                    break
                pos += 1
    else:
        for _ in range(total):
            adrows = [[0] * m for _ in range(m)]
            kirrows = [[0] * m for _ in range(m)]
            for a in range(m):
                ca = coeffs[a]
                if ca:
                    Ma = adB[a]; Ka = kir[a]
                    for i in range(m):
                        Mi = Ma[i]; Ki = Ka[i]
                        ar = adrows[i]; kr = kirrows[i]
                        for j in range(m):
                            if Mi[j]:
                                ar[j] = (ar[j] + ca * Mi[j]) % p
                            if Ki[j]:
                                kr[j] = (kr[j] + ca * Ki[j]) % p
            A[rank_mod(adrows, m, p)] += 1
            K[rank_mod(kirrows, m, p)] += 1
            pos = 0
            while pos < m:
                coeffs[pos] += 1
                if coeffs[pos] < p:
                    break
                coeffs[pos] = 0
                pos += 1
    return A, K

# ---------- structural invariants ----------
def lower_central_profile(m, br, p):
    """dims of gamma_i / gamma_{i+1}. gamma_1 = L; gamma_{i+1} = [L, gamma_i]."""
    if m == 0:
        return ()
    import itertools as it
    # represent subspaces by row-reduced basis over F_p
    def rref(rows):
        rows = [r[:] for r in rows]
        piv_cols = []
        r = 0
        for c in range(m):
            piv = -1
            for i in range(r, len(rows)):
                if rows[i][c] % p:
                    piv = i; break
            if piv < 0:
                continue
            rows[r], rows[piv] = rows[piv], rows[r]
            inv = pow(rows[r][c] % p, p - 2, p)
            rows[r] = [(x * inv) % p for x in rows[r]]
            for i in range(len(rows)):
                if i != r and rows[i][c] % p:
                    f = rows[i][c] % p
                    rows[i] = [(rows[i][j] - f * rows[r][j]) % p for j in range(m)]
            piv_cols.append(c); r += 1
        return [row for row in rows[:r]], piv_cols
    full = []
    for a in range(m):
        e = [0] * m; e[a] = 1; full.append(e)
    gamma = full
    dims = [m]
    prof = []
    prev = m
    for _ in range(m + 2):
        # [L, gamma]: brackets of basis e_a with each vector in gamma
        gens = []
        gb, _ = rref(gamma)
        for a in range(m):
            for gv in gb:
                # [e_a, gv] = sum_b gv[b] [e_a,e_b]
                res = [0] * m
                for b in range(m):
                    if gv[b]:
                        for t, c in br[a][b].items():
                            res[t] = (res[t] + gv[b] * c) % p
                if any(res):
                    gens.append(res)
        nb, _ = rref(gens) if gens else ([], [])
        d = len(nb)
        prof.append(prev - d)
        if d == 0:
            break
        gamma = nb
        prev = d
    return tuple(prof)

def solve_dim(constraints, nvars, p):
    """dimension of solution space of homogeneous system (list of rows length nvars) over F_p."""
    if nvars == 0:
        return 0
    r = rank_mod([row[:] for row in constraints], nvars, p) if constraints else 0
    return nvars - r

def der_dim(m, br, p):
    """dim of derivation algebra: D in gl(m), D[e_a,e_b] = [D e_a, e_b] + [e_a, D e_b] for all a<b.
    Variables: D[t][s] (image of e_s has coeff D[t][s] on e_t). nvars = m*m."""
    if m == 0:
        return 0
    nv = m * m
    def var(t, s):
        return t * m + s
    rows = []
    for a in range(m):
        for b in range(m):
            if a >= b:
                continue
            # LHS: D[e_a,e_b] = sum_t br[a][b][t] * D(e_t) = sum_t br[a][b][t] * sum_u D[u][t] e_u
            # RHS: [D e_a, e_b] + [e_a, D e_b]
            #    = sum_u D[u][a] [e_u,e_b] + sum_u D[u][b] [e_a,e_u]
            # each component e_u: collect coefficients into a constraint row per output basis e_c
            coeff = [dict() for _ in range(m)]  # coeff[c][var] = value
            # LHS
            for t, cc in br[a][b].items():
                for u in range(m):
                    coeff[u][var(u, t)] = coeff[u].get(var(u, t), 0) + cc
            # RHS term1: sum_u D[u][a] [e_u,e_b]
            for u in range(m):
                for tc, cc in br[u][b].items():
                    coeff[tc][var(u, a)] = coeff[tc].get(var(u, a), 0) - cc
            # RHS term2: sum_u D[u][b] [e_a,e_u]
            for u in range(m):
                for tc, cc in br[a][u].items():
                    coeff[tc][var(u, b)] = coeff[tc].get(var(u, b), 0) - cc
            for c in range(m):
                if coeff[c]:
                    row = [0] * nv
                    for v, val in coeff[c].items():
                        row[v] = val % p
                    if any(row):
                        rows.append(row)
    return solve_dim(rows, nv, p)

def centroid_dim(m, br, p):
    """dim of centroid: phi in gl(m) with phi[x,y]=[phi x,y]=[x,phi y].
    Enforce phi[e_a,e_b]=[phi e_a,e_b] and phi[e_a,e_b]=[e_a,phi e_b] for all a,b."""
    if m == 0:
        return 0
    nv = m * m
    def var(t, s):
        return t * m + s
    rows = []
    for a in range(m):
        for b in range(m):
            # constraint 1: phi[e_a,e_b] - [phi e_a, e_b] = 0
            coeff = [dict() for _ in range(m)]
            for t, cc in br[a][b].items():
                for u in range(m):
                    coeff[u][var(u, t)] = coeff[u].get(var(u, t), 0) + cc
            for u in range(m):
                for tc, cc in br[u][b].items():
                    coeff[tc][var(u, a)] = coeff[tc].get(var(u, a), 0) - cc
            for c in range(m):
                if coeff[c]:
                    row = [0] * nv
                    for v, val in coeff[c].items():
                        row[v] = val % p
                    if any(row):
                        rows.append(row)
            # constraint 2: phi[e_a,e_b] - [e_a, phi e_b] = 0
            coeff = [dict() for _ in range(m)]
            for t, cc in br[a][b].items():
                for u in range(m):
                    coeff[u][var(u, t)] = coeff[u].get(var(u, t), 0) + cc
            for u in range(m):
                for tc, cc in br[a][u].items():
                    coeff[tc][var(u, b)] = coeff[tc].get(var(u, b), 0) - cc
            for c in range(m):
                if coeff[c]:
                    row = [0] * nv
                    for v, val in coeff[c].items():
                        row[v] = val % p
                    if any(row):
                        rows.append(row)
    return solve_dim(rows, nv, p)

def center_dim(m, br, p):
    """dim Z(L): x with [x, e_b]=0 for all b. Variables x_a. Constraint per output component."""
    if m == 0:
        return 0
    rows = []
    for b in range(m):
        coeff = [dict() for _ in range(m)]
        for a in range(m):
            for t, cc in br[a][b].items():
                coeff[t][a] = coeff[t].get(a, 0) + cc
        for c in range(m):
            if coeff[c]:
                row = [0] * m
                for v, val in coeff[c].items():
                    row[v] = val % p
                if any(row):
                    rows.append(row)
    return solve_dim(rows, m, p)

def hasse_forest(n, rel):
    """cover graph is a forest? covers = relations i<_P j with no k strictly between."""
    order = set(rel)
    covers = []
    for (i, j) in order:
        strictly_between = any((i, k) in order and (k, j) in order for k in range(n))
        if not strictly_between:
            covers.append((i, j))
    # undirected forest check
    import collections
    parent = {v: v for v in range(n)}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    edges = 0
    verts = set()
    for (i, j) in covers:
        verts.add(i); verts.add(j)
        ri, rj = find(i), find(j)
        if ri == rj:
            return False  # cycle
        parent[ri] = rj
        edges += 1
    return True
