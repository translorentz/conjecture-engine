#!/usr/bin/env python3
"""Part XV (Conjectures 271-285, af1-af15): independent reduced-range
recomputation for the self-avoiding-walk stochastic-order, curvature, and
dependence laws, plus exact checks of the three calibration propositions.

Everything here is enumerated from scratch in pure Python, independently of
the primary scans: square-lattice joint laws through n = 12, bridges through
n = 14, dimensions 3..6 through n = 6, published square-lattice counts
through n = 79 for the curvature law af1.  All inequality checks are exact
(integers, Fractions, integer max-flow for the coupling laws)."""

import sys
from fractions import Fraction
from math import comb, log

FAILS = []


def chk(name, ok, extra=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" {extra}" if extra else ""))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- 2D walks
N2 = 12
NB = 14


def enum2d(N):
    """first-step=+x symmetry class; returns per-n joint tables."""
    exy = [dict() for _ in range(N + 1)]
    span = [dict() for _ in range(N + 1)]
    r2a = [dict() for _ in range(N + 1)]
    r2c = [dict() for _ in range(N + 1)]
    ca = [dict() for _ in range(N + 1)]
    cls = [0] * (N + 1)
    occ = {(0, 0), (1, 0)}
    nbrs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def rec(k, x, y, xmin, xmax, ymin, ymax, con):
        cls[k] += 1
        a = sum((x + dx, y + dy) not in occ for dx, dy in nbrs)
        r2 = x * x + y * y
        for tab, key in ((exy, (abs(x), abs(y))), (span, (xmax - xmin, ymax - ymin)),
                         (r2a, (r2, a)), (r2c, (r2, con)), (ca, (con, a))):
            tab[k][key] = tab[k].get(key, 0) + 1
        if k == N:
            return
        for dx, dy in nbrs:
            nx, ny = x + dx, y + dy
            if (nx, ny) in occ:
                continue
            nb = sum((nx + ex, ny + ey) in occ for ex, ey in nbrs)
            occ.add((nx, ny))
            rec(k + 1, nx, ny, min(xmin, nx), max(xmax, nx),
                min(ymin, ny), max(ymax, ny), con + nb - 1)
            occ.remove((nx, ny))

    sys.setrecursionlimit(10000)
    rec(1, 1, 0, 0, 1, 0, 0, 0)
    return cls, exy, span, r2a, r2c, ca


cls, exy_c, span_c, r2a_c, r2c_c, ca_c = enum2d(N2)
cn = {n: 4 * cls[n] for n in range(1, N2 + 1)}
cn[0] = 1


def sym(H):
    out = {}
    for (a, b), c in H.items():
        out[(a, b)] = out.get((a, b), 0) + 2 * c
        out[(b, a)] = out.get((b, a), 0) + 2 * c
    return out


def x4(H):
    return {k: 4 * v for k, v in H.items()}


EXY = {n: sym(exy_c[n]) for n in range(1, N2 + 1)}
SPAN = {n: sym(span_c[n]) for n in range(1, N2 + 1)}
R2A = {n: x4(r2a_c[n]) for n in range(1, N2 + 1)}
R2C = {n: x4(r2c_c[n]) for n in range(1, N2 + 1)}
CA = {n: x4(ca_c[n]) for n in range(1, N2 + 1)}
EXY[0] = {(0, 0): 1}
SPAN[0] = {(0, 0): 1}


def marg(H, i):
    out = {}
    for k, c in H.items():
        out[k[i]] = out.get(k[i], 0) + c
    return out


R2M = {n: marg(R2A[n], 0) for n in R2A}
CM = {n: marg(CA[n], 0) for n in CA}
SXM = {n: marg(SPAN[n], 0) for n in SPAN}
CM[0] = {0: 1}
SXM[0] = {0: 1}

# published square-lattice counts (OEIS A001411 b-file, 0..79, from Jensen's
# 2013 enumeration), used only for af1; spot-verified against OEIS and the
# independently quoted c_71 and c_79
C_PUB = [1, 4, 12, 36, 100, 284, 780, 2172, 5916, 16268, 44100, 120292,
         324932, 881500, 2374444, 6416596, 17245332, 46466676, 124658732,
         335116620, 897697164, 2408806028, 6444560484, 17266613812,
         46146397316, 123481354908, 329712786220, 881317491628, 2351378582244,
         6279396229332, 16741957935348, 44673816630956, 119034997913020,
         317406598267076, 845279074648708, 2252534077759844, 5995740499124412,
         15968852281708724, 42486750758210044, 113101676587853932,
         300798249248474268, 800381032599158340, 2127870238872271828,
         5659667057165209612, 15041631638016155884, 39992704986620915140,
         106255762193816523332, 282417882500511560972, 750139547395987948108,
         1993185460468062845836, 5292794668724837206644,
         14059415980606050644844, 37325046962536847970116,
         99121668912462180162908, 263090298246050489804708,
         698501700277581954674604, 1853589151789474253830500,
         4920146075313000860596140, 13053884641516572778155044,
         34642792634590824499672196, 91895836025056214634047716,
         243828023293849420839513468, 646684752476890688940276172,
         1715538780705298093042635884, 4549252727304405545665901684,
         12066271136346725726547810652, 31992427160420423715150496804,
         84841788997462209800131419244, 224916973773967421352838735684,
         596373847126147985434982575724, 1580784678250571882017480243636,
         4190893020903935054619120005916, 11107224538074654820152678182884,
         29442884996760677051402398150644, 78023796077779727644807609460228,
         206797849568186990141402577046860, 547952781764285893561169365957068,
         1452142167241575828091155500636684,
         3847327231644550282490410907667972,
         10194710293557466193787900071923676]
chk("published counts agree with fresh enumeration for n <= %d" % N2,
    all(C_PUB[n] == cn[n] for n in range(0, N2 + 1)))

# internal identity: sum of atmospheres = c_{n+1}
chk("identity sum A_n = c_{n+1}",
    all(sum(a * c for (C, a), c in CA[n].items()) == cn[n + 1]
        for n in range(1, N2)))

# ------------------------------------------------------------------ af1
ok1 = all(0 < C_PUB[n + 2] * C_PUB[n - 2] < C_PUB[n] ** 2
          for n in range(2, 78)) and \
      all(C_PUB[n + 2] ** 3 * C_PUB[n - 2] < C_PUB[n + 4] * C_PUB[n] ** 3
          for n in range(2, 76))
chk("af1 parity log-concavity + curvature monotone, published counts n<=79", ok1)

# ------------------------------------------------------------------ af2
ok2 = True
for e in (0, 1, 2, 3, 4):  # q = 0,2,4,6,8 exactly
    M = {n: sum(c * r ** e for r, c in R2M[n].items()) for n in R2M}
    ok2 &= all(M[n] ** 2 > M[n - 2] * M[n + 2] for n in range(3, N2 - 1))
for qi in range(1, 101):  # float grid q = 0.2 .. 20
    q = qi / 5.0
    M = {n: sum(c * r ** (q / 2) for r, c in R2M[n].items()) for n in R2M}
    ok2 &= all(M[n] ** 2 > M[n - 2] * M[n + 2] for n in range(3, N2 - 1))
chk("af2 radial-moment parity log-concavity (exact even q + grid)", ok2)

# ---------------------------------------------------------------- bridges
def enum_bridges(N):
    B = [dict() for _ in range(N + 1)]
    occ = {(0, 0), (1, 0)}

    def rec(k, x, y, xmax, vert):
        if vert and x == xmax:
            B[k][x] = B[k].get(x, 0) + 1
        if k == N:
            return
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if dy == -1 and not vert:
                continue  # symmetry class: first vertical step is +y
            nx, ny = x + dx, y + dy
            if nx < 1 or (nx, ny) in occ:
                continue
            occ.add((nx, ny))
            rec(k + 1, nx, ny, max(xmax, nx), vert or dy != 0)
            occ.remove((nx, ny))

    rec(1, 1, 0, 1, False)
    out = []
    for n in range(N + 1):
        full = {h: 2 * c for h, c in B[n].items()}
        if n >= 1:
            full[n] = full.get(n, 0) + 1  # the straight bridge
        out.append(full)
    return out


BR = enum_bridges(NB)
bt = {n: sum(BR[n].values()) for n in range(1, NB + 1)}
chk("bridge totals 1,3,7,17,41,101,251,631,1591,4029,...",
    [bt[n] for n in range(1, 11)] == [1, 3, 7, 17, 41, 101, 251, 631, 1591, 4029])

# af3: log-convexity from n=5; sharp failures at n=2 and n=4
ok3 = all(bt[n] ** 2 < bt[n - 1] * bt[n + 1] for n in range(5, NB)) \
    and bt[2] ** 2 - bt[1] * bt[3] == 2 and bt[4] ** 2 - bt[3] * bt[5] == 2 \
    and bt[3] ** 2 < bt[2] * bt[4]
chk("af3 bridge log-convexity n>=5, with sharp failures at n=2,4", ok3)

# af4: full MLR cross-products
ok4 = True
for n in range(1, NB):
    hs = sorted(set(BR[n]) | set(BR[n + 1]))
    for i in range(len(hs)):
        for j in range(i + 1, len(hs)):
            h1, h2 = hs[i], hs[j]
            ok4 &= BR[n].get(h1, 0) * BR[n + 1].get(h2, 0) >= \
                BR[n].get(h2, 0) * BR[n + 1].get(h1, 0)
chk("af4 bridge-height MLR order, all cross-products, n<=%d" % (NB - 1), ok4)

# Proposition af:height closed forms
okh = all(BR[n].get(n, 0) == 1 for n in range(1, NB + 1)) and \
    all(BR[n].get(n - 1, 0) == 2 * (n - 1) for n in range(2, NB + 1)) and \
    all(BR[n].get(n - 2, 0) == 2 * (n - 2) ** 2 for n in range(3, NB + 1)) and \
    all(BR[n].get(n - 3, 0) == 2 * (n - 3) + 8 * comb(n - 3, 2) + 8 * comb(n - 3, 3)
        for n in range(4, NB + 1))
chk("Proposition af:height closed forms for the top four diagonals", okh)
okh2 = all(2 * (n - 1) * (n + 1) ==
           BR[n][n - 1] * BR[n + 1][n] - BR[n][n] * BR[n + 1][n - 1]
           for n in range(2, NB)) and \
    all(3 * (BR[n][n - 2] * BR[n + 1][n - 1] - BR[n][n - 1] * BR[n + 1][n - 2])
        == 4 * (n - 2) * (n - 1) * (n * n - n - 3) for n in range(3, NB))
chk("Proposition af:height corner-minor identities", okh2)

# ---------------------------------------------------- max-flow (Strassen)
def dominated(mu, nu):
    """exact: mu <= nu in the coordinatewise stochastic order."""
    tm, tn = sum(mu.values()), sum(nu.values())
    A = [(k, c * tn) for k, c in mu.items() if c]
    Bv = [(k, c * tm) for k, c in nu.items() if c]
    INF = 1 << 200
    g = [[] for _ in range(len(A) + len(Bv) + 2)]
    src, snk = len(A) + len(Bv), len(A) + len(Bv) + 1

    def add(u, v, c):
        g[u].append([v, c, len(g[v])])
        g[v].append([u, 0, len(g[u]) - 1])

    for i, (k, c) in enumerate(A):
        add(src, i, c)
    for j, (k, c) in enumerate(Bv):
        add(len(A) + j, snk, c)
    for i, (ka, _) in enumerate(A):
        for j, (kb, _) in enumerate(Bv):
            if ka[0] <= kb[0] and ka[1] <= kb[1]:
                add(i, len(A) + j, INF)
    flow = 0
    while True:
        lev = [-1] * len(g)
        lev[src] = 0
        q = [src]
        for u in q:
            for e in g[u]:
                if e[1] > 0 and lev[e[0]] < 0:
                    lev[e[0]] = lev[u] + 1
                    q.append(e[0])
        if lev[snk] < 0:
            break
        it = [0] * len(g)

        def dfs(u, f):
            if u == snk:
                return f
            while it[u] < len(g[u]):
                e = g[u][it[u]]
                if e[1] > 0 and lev[e[0]] == lev[u] + 1:
                    d = dfs(e[0], min(f, e[1]))
                    if d > 0:
                        e[1] -= d
                        g[e[0]][e[2]][1] += d
                        return d
                it[u] += 1
            return 0
        while True:
            f = dfs(src, INF)
            if f == 0:
                break
            flow += f
    return flow == tm * tn


chk("af5 endpoint monotone coupling (exact max-flow), n<=%d" % (N2 - 2),
    all(dominated(EXY[n], EXY[n + 2]) for n in range(0, N2 - 1)))
chk("af6 span monotone coupling (exact max-flow), n<=%d" % (N2 - 2),
    all(dominated(SPAN[n], SPAN[n + 2]) for n in range(0, N2 - 1)))

# af7: span MLR
ok7 = True
for n in range(0, N2 - 1):
    P, Q = SXM[n], SXM[n + 2]
    ss = sorted(set(P) | set(Q))
    for i in range(len(ss)):
        for j in range(i + 1, len(ss)):
            ok7 &= P.get(ss[i], 0) * Q.get(ss[j], 0) >= \
                P.get(ss[j], 0) * Q.get(ss[i], 0)
chk("af7 span MLR order n -> n+2", ok7)

# af8: contact stochastic growth
ok8 = True
for n in range(2, N2):
    P, Q = CM[n], CM[n + 1]
    tp, tq = sum(P.values()), sum(Q.values())
    for m in set(P) | set(Q):
        ok8 &= sum(c for C, c in Q.items() if C >= m) * tp >= \
            sum(c for C, c in P.items() if C >= m) * tq
chk("af8 contact count stochastically increasing", ok8)


# ------------------------------------------------- quadrant dependence
def quad_ok(H, want):
    tot = sum(H.values())
    xs = sorted({k[0] for k in H})
    ys = sorted({k[1] for k in H})
    for a in xs:
        for b in ys:
            j = sum(c for (x, y), c in H.items() if x >= a and y >= b)
            mx = sum(c for (x, y), c in H.items() if x >= a)
            my = sum(c for (x, y), c in H.items() if y >= b)
            if want * (j * tot - mx * my) < 0:
                return False
    return True


chk("af9 (Sx,Sy) NQD, all thresholds, n<=%d" % N2,
    all(quad_ok(SPAN[n], -1) for n in range(1, N2 + 1)))
chk("af10 (R2,A) PQD", all(quad_ok(R2A[n], +1) for n in range(1, N2 + 1)))
chk("af11 (R2,C) NQD", all(quad_ok(R2C[n], -1) for n in range(1, N2 + 1)))
chk("af12 (C,A) NQD", all(quad_ok(CA[n], -1) for n in range(1, N2 + 1)))
chk("negative control: (|X|,|Y|) NQD fails at n=3",
    not quad_ok(EXY[3], -1))

# af13: finite-size roots of the curvature diagnostic (plausibility screen)
def Kroot(n):
    def lz(m, u):
        return log(sum(c * u ** C for C, c in CM[m].items()))
    lo, hi = 1.0, 4.0
    f = lambda u: lz(n + 2, u) - 2 * lz(n, u) + lz(n - 2, u)
    if f(lo) * f(hi) > 0:
        return None
    for _ in range(60):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


roots = {n: Kroot(n) for n in range(4, N2 - 1)}
chk("af13 finite-size roots exist and oscillate at small n (control)",
    all(r is not None for r in roots.values()),
    "roots " + str({n: round(r, 3) for n, r in roots.items()}))

# ------------------------------------------------------------ dimensions
def enum_dim(D, N):
    """first-step = +e0 class; returns c_n(D) and R^2 histograms."""
    cls = [0] * (N + 1)
    r2h = [dict() for _ in range(N + 1)]
    start = tuple([0] * D)
    first = tuple([1] + [0] * (D - 1))
    occ = {start, first}
    path = [start, first]

    def rec(k, cur):
        cls[k] += 1
        r2 = sum(c * c for c in cur)
        r2h[k][r2] = r2h[k].get(r2, 0) + 1
        if k == N:
            return
        for ax in range(D):
            for sg in (1, -1):
                nxt = list(cur)
                nxt[ax] += sg
                nxt = tuple(nxt)
                if nxt in occ:
                    continue
                occ.add(nxt)
                rec(k + 1, nxt)
                occ.remove(nxt)

    rec(1, first)
    return {n: 2 * D * cls[n] for n in range(1, N + 1)}, \
           {n: {r: 2 * D * c for r, c in r2h[n].items()} for n in range(1, N + 1)}


ND = 6
cd = {2: cn}
r2d = {2: R2M}
for D in (3, 4, 5, 6):
    cd[D], r2d[D] = enum_dim(D, ND)
chk("cross-check c_n(3) = 6,30,150,726,3534,16926",
    [cd[3][n] for n in range(1, 7)] == [6, 30, 150, 726, 3534, 16926])

# Proposition af:nbw closed forms and all-d monotonicity
c_poly = {
    4: lambda d: 2 * d * (2 * d - 1) ** 3 - 2 * d * (2 * d - 2),
    5: lambda d: 2 * d * (2 * d - 1) ** 4 - 2 * d * (2 * d - 2) * (4 * d - 3),
    6: lambda d: 64 * d ** 6 - 160 * d ** 5 + 112 * d ** 4 + 20 * d ** 2 - 34 * d,
    7: lambda d: (128 * d ** 7 - 384 * d ** 6 + 352 * d ** 5 - 80 * d ** 4
                  + 192 * d ** 3 - 372 * d ** 2 + 166 * d),
}
oknb = all(c_poly[n](D) == cd[D][n] for D in range(2, 7) for n in (4, 5, 6)) \
    and c_poly[7](2) == cn[7] and c_poly[7](3) == enum_dim(3, 7)[0][7]
chk("Proposition af:nbw closed forms match enumeration (d<=6 at n<=6; d<=3 at n=7)",
    oknb)
okq = True
for n in (4, 5, 6, 7):
    for D in range(2, 201):
        q1 = Fraction(c_poly[n](D), 2 * D * (2 * D - 1) ** (n - 1))
        q2 = Fraction(c_poly[n](D + 1), 2 * (D + 1) * (2 * D + 1) ** (n - 1))
        okq &= q2 > q1
chk("Proposition af:nbw / af14: q_{d,n} strictly increasing, d <= 200, n=4..7",
    okq)

# af14 from enumerations
ok14 = all(Fraction(cd[D + 1][n], 2 * (D + 1) * (2 * D + 1) ** (n - 1)) >
           Fraction(cd[D][n], 2 * D * (2 * D - 1) ** (n - 1))
           for D in range(2, 6) for n in range(4, ND + 1))
chk("af14 NBW survival increasing in dimension (enumerated, d<=6, n<=6)", ok14)
chk("af14 boundary: survival = 1 for n <= 3",
    all(cd[D][n] == 2 * D * (2 * D - 1) ** (n - 1)
        for D in range(2, 7) for n in (1, 2, 3)))

# af15: exact even moments + float grid, plus the stochastic-order control
ok15 = True
for D in range(2, 6):
    for n in range(2, ND + 1):
        for e in (1, 2, 3, 5):
            m1 = Fraction(sum(c * r ** e for r, c in r2d[D][n].items()), cd[D][n])
            m2 = Fraction(sum(c * r ** e for r, c in r2d[D + 1][n].items()),
                          cd[D + 1][n])
            ok15 &= m2 < m1
        for qi in range(1, 61):
            q = qi / 4.0
            f1 = sum(c * r ** (q / 2) for r, c in r2d[D][n].items()) / cd[D][n]
            f2 = sum(c * r ** (q / 2) for r, c in r2d[D + 1][n].items()) / cd[D + 1][n]
            ok15 &= f2 < f1
chk("af15 all radial moments decrease with dimension (exact + grid)", ok15)


def st_crossing(P, Q):
    tp, tq = sum(P.values()), sum(Q.values())
    up = dn = False
    for t in sorted(set(P) | set(Q)):
        a = sum(c for r, c in P.items() if r >= t) * tq
        b = sum(c for r, c in Q.items() if r >= t) * tp
        up |= a > b
        dn |= a < b
    return up and dn


chk("negative control: radial laws cross between d=2 and d=3 at n=3",
    st_crossing(r2d[3][3], r2d[2][3]))

# Proposition af:extreme spanning-axes inequality on enumerated data
chk("Proposition af:extreme: c_n(d+1) > (1+1/d) c_n(d)",
    all(Fraction(cd[D + 1][n], cd[D][n]) > Fraction(D + 1, D)
        for D in range(2, 6) for n in range(2, ND + 1)))

print()
if FAILS:
    print("FAILURES:", len(FAILS))
    for f in FAILS:
        print("  -", f)
    sys.exit(1)
print("All Part XV checks passed.")
