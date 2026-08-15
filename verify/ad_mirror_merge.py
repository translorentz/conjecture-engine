#!/usr/bin/env python3
"""Independent verification of the GV/mirror programme (C5-C8, C10).

From-scratch hypergeometric mirror symmetry for one-parameter projective CICYs:
w0 = sum A_m z^m, A_m = prod (d_i m)! / (m!)^k, k = |P| + 1 = sum d_i,
mirror map q = z exp(f/w0), Yukawa K = D/((1-Lambda z) w0^2) (Jz/z)^3,
GV via K(q) = D + sum N_b b^3 q^b/(1-q^b).
Exact rationals to moderate order; mpmath high-precision beyond.
"""
import sys
from fractions import Fraction as Fr
from math import comb, factorial

EDGES = [((2,2,2,2),(3,2,2)), ((3,2,2),(3,3)), ((3,2,2),(4,2)),
         ((3,3),(5,)), ((4,2),(5,))]
FIVE = [(5,), (4,2), (3,3), (3,2,2), (2,2,2,2)]

def series_mul(a, b, M):
    out = [Fr(0)]*(M+1)
    for i, ai in enumerate(a[:M+1]):
        if ai:
            for j, bj in enumerate(b[:M+1-i]):
                if bj: out[i+j] += ai*bj
    return out

def series_inv(a, M):
    out = [Fr(0)]*(M+1); out[0] = 1/a[0]
    for m in range(1, M+1):
        out[m] = -sum(a[i]*out[m-i] for i in range(1, m+1))*out[0]
    return out

def series_exp(a, M):
    assert a[0] == 0
    out = [Fr(0)]*(M+1); out[0] = Fr(1)
    # out' = a' out
    for m in range(1, M+1):
        out[m] = sum(Fr(i)*a[i]*out[m-i] for i in range(1, m+1))/m
    return out

def periods(d, M):
    k = sum(d)
    A = [Fr(1)]
    for m in range(1, M+1):
        num = Fr(1)
        for di in d:
            for t in range(di*(m-1)+1, di*m+1): num *= t
        den = Fr(m)**k
        A.append(A[-1]*num/den**1 / Fr(1))
    # fix: A_m = prod (d_i m)! / (m!)^k computed incrementally
    A = [Fr(1)]*(M+1)
    for m in range(1, M+1):
        val = A[m-1]
        for di in d:
            for t in range(di*(m-1)+1, di*m+1): val *= t
        val /= Fr(factorial(m))**k * Fr(1)/Fr(factorial(m-1))**k
        A[m] = val
    # simplest robust: direct
    A = [Fr(1)]
    for m in range(1, M+1):
        num = 1
        for di in d: num *= factorial(di*m)
        A.append(Fr(num, factorial(m)**k))
    H = [Fr(0)]*(max(di*M for di in d)+2)
    for t in range(1, len(H)): H[t] = H[t-1] + Fr(1, t)
    B = [Fr(0)]
    for m in range(1, M+1):
        B.append(sum(di*H[di*m] for di in d) - k*H[m])
    f = [Fr(0)] + [A[m]*B[m] for m in range(1, M+1)]
    return A, f

def mirror_map(d, M):
    """q(z) = z exp(f/w0) as series in z; returns list c with q = sum c_m z^m."""
    w0, f = periods(d, M)
    g = series_mul(f, series_inv(w0, M), M)
    e = series_exp(g, M)
    return [Fr(0)] + e[:M]  # q = z * e -> coefficient shift

def invert_series(c, M):
    """Given q = sum_{m>=1} c_m z^m with c_1=1, return z as series in q."""
    z = [Fr(0), Fr(1)] + [Fr(0)]*(M-1)
    for m in range(2, M+1):
        # coefficient of q^m in q(z(q)) must vanish
        comp = [Fr(0)]*(M+1)
        pw = [Fr(0), Fr(1)] + [Fr(0)]*(M-1)  # z^1
        comp = [Fr(0)]*(M+1)
        pw = z[:]
        for j in range(1, M+1):
            if j > 1: pw = series_mul(pw, z, M)
            cj = c[j] if j < len(c) else Fr(0)
            if cj:
                for t in range(M+1): comp[t] += cj*pw[t]
        z[m] -= comp[m]
    return z

def gv(d, M):
    """Genus-zero GV invariants N_1..N_{M-1} exactly."""
    D = 1
    for di in d: D *= di
    Lam = 1
    for di in d: Lam *= di**di
    w0, f = periods(d, M)
    c = mirror_map(d, M)
    z_of_q = invert_series(c, M)
    # w0(z(q)), (1 - Lam z(q)), Jz/z = (q/z) dz/dq
    def compose(a):
        out = [Fr(0)]*(M+1); pw = [Fr(1)] + [Fr(0)]*M
        for j in range(0, M+1):
            if j: pw = series_mul(pw, z_of_q, M)
            if j < len(a) and a[j]:
                for t in range(M+1): out[t] += a[j]*pw[t]
        return out
    w0q = compose(w0)
    onemz = [Fr(1)] + [Fr(0)]*M
    for t in range(M+1): onemz[t] -= Lam*z_of_q[t] if t else 0
    onemz[0] = Fr(1)
    dzdq = [Fr(m)*z_of_q[m] for m in range(M+1)]  # q dz/dq coefficients: m*z_m q^m
    # (q dz/dq)/z as series: divide by z (z has valuation 1)
    zs = z_of_q[1:]; ds = dzdq[1:]
    ratio = series_mul(ds + [Fr(0)], series_inv(zs + [Fr(0)], M-1), M-1)
    r3 = series_mul(series_mul(ratio, ratio, M-1), ratio, M-1)
    Kq = series_mul(series_mul(r3 + [Fr(0)], series_inv(onemz, M), M), series_inv(series_mul(w0q, w0q, M), M), M)
    Kq = [D*x for x in Kq]
    # K = D + sum_b N_b b^3 q^b/(1-q^b): coeff of q^m (m>=1): sum_{b|m} b^3 N_b
    N = {}
    for m in range(1, M):
        s = Kq[m]
        for b in range(1, m):
            if m % b == 0 and b in N: s -= Fr(b**3)*N[b]
        N[m] = s/Fr(m**3)
        assert N[m].denominator == 1, (d, m)
        N[m] = int(N[m])
    return N

def stage_exact(M=26):
    known = {(5,): 2875, (4,2): 1280, (3,3): 1053, (3,2,2): 720, (2,2,2,2): 512}
    NV = {}
    for d in FIVE:
        N = gv(d, M)
        NV[d] = N
        print(f"  {d}: N1={N[1]} (known {known[d]})  N2={N[2]}  N3={N[3]}")
        assert N[1] == known[d], d
    # C7 log-convexity (strict) on 1..M-2
    for d in FIVE:
        N = NV[d]
        viol = [b for b in range(2, M-1) if not N[b]*N[b] < N[b-1]*N[b+1]]
        print(f"  C7 log-convex {d}: violations {viol}")
        assert not viol
    # C6 amplification monotone in beta on the five edges
    for (a, b) in EDGES:
        Na, Nb = NV[a], NV[b]
        rats = [Fr(Nb[be], Na[be]) for be in range(1, M-1)]
        ok = all(rats[i] < rats[i+1] for i in range(len(rats)-1))
        print(f"  C6 edge {a}->{b}: A_1={float(rats[0]):.4f} A_{M-2}={float(rats[-1]):.3e} increasing={ok}")
        assert ok
    return NV

def stage_conifold():
    from mpmath import mp, mpf, exp, log, psi
    mp.dps = 60
    out = {}
    for d in FIVE:
        k = sum(d); D = 1; Lam = 1
        for di in d: D *= di; Lam *= di**di
        zc = mpf(1)/Lam
        # w0, f at zc by term recurrence
        w0 = mpf(1); f = mpf(0); term = mpf(1); Hm = mpf(0); Hd = [mpf(0)]*len(d)
        for m in range(1, 12001):
            fac = mpf(1)
            for di in d:
                for t in range(di*(m-1)+1, di*m+1): fac *= t
            term *= fac * zc / (mpf(m)**k)
            Hm += mpf(1)/m
            Bm = -k*Hm
            for i, di in enumerate(d):
                for t in range(di*(m-1)+1, di*m+1): Hd[i] += mpf(1)/t
                Bm += di*Hd[i]
            w0 += term
            f += term*Bm
            if abs(term)*max(1, abs(Bm)) < mpf(10)**(-40) * abs(w0): break
        qc = zc*exp(f/w0)
        out[d] = (float(qc), float(1/qc))
        print(f"  {d}: q_c={float(qc):.8e}  1/q_c={float(1/qc):.4f}  (terms {m})")
    # C8: q_c decreasing along each edge
    for (a, b) in EDGES:
        assert out[b][0] < out[a][0], (a, b)
    print("  C8: q_c strictly decreases along all five merge edges: OK")
    return out

def stage_yukawa(NV, qcs, M=26):
    """C10 on a grid using available exact GV terms (tail warning at high x)."""
    for (a, b) in EDGES:
        Da = 1; Db = 1
        for di in a: Da *= di
        for di in b: Db *= di
        ok = True; worst = None
        for xi in range(1, 20):
            x = xi/20
            def K(d, N, qc, D):
                s = float(D)
                for be in range(1, M-1):
                    qb = (x*qc)**be
                    s += N[be]*be**3*qb/(1-qb)
                return s
            va = K(a, NV[a], qcs[a][0], Da)/Da
            vb = K(b, NV[b], qcs[b][0], Db)/Db
            if not vb > va:
                ok = False; worst = x
        print(f"  C10 edge {a}->{b}: normalized Yukawa larger on target at all x<=0.95: {ok}"
              + (f" (first failure x={worst})" if not ok else ""))

if __name__ == "__main__":
    import time
    t0 = time.time()
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "a"):
        NV = stage_exact(26)
        qcs = stage_conifold()
        stage_yukawa(NV, qcs, 26)
    print(f"done in {time.time()-t0:.1f}s")

def configs(n):
    """All multidegree configurations for CY n-folds: sum(d_i-1)=n+1, d_i>=2."""
    out = []
    def rec(rem, mx, cur):
        if rem == 0: out.append(tuple(cur)); return
        for d in range(min(mx, rem+1), 1, -1):
            if d-1 <= rem: rec(rem-(d-1), d, cur+[d])
    rec(n+1, n+2, [])
    return out

def stage_c5(M=8):
    """C5: normalized mirror map coefficient contraction under merges, dims 3-5."""
    tot = viol = 0
    for n in (3, 4, 5):
        cfgs = configs(n)
        maps = {}
        for d in cfgs:
            Lam = 1
            for di in d: Lam *= di**di
            c = mirror_map(d, M)
            # qhat(x) = Lam * q(x/Lam): coefficient m: c_m * Lam^{1-m}
            maps[d] = [c[m]*Fr(Lam)**(1-m) if m < len(c) else Fr(0) for m in range(M+1)]
        for d in cfgs:
            for i in range(len(d)):
                for j in range(i+1, len(d)):
                    dd = sorted(list(d[:i]) + list(d[i+1:j]) + list(d[j+1:]) + [d[i]+d[j]-1], reverse=True)
                    dd = tuple(dd)
                    for m in range(2, M+1):
                        tot += 1
                        cm_s, cm_t = maps[d][m], maps[dd][m]
                        if m == 2:
                            ok = cm_t <= cm_s
                        else:
                            ok = cm_t < cm_s
                        if not ok:
                            viol += 1
                            print(f"  C5 VIOL n={n} {d}->{dd} m={m}")
    print(f"  C5 dims 3-5, all merges, m<={M}: {tot} comparisons, {viol} violations")

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "c5":
    stage_c5(8)
