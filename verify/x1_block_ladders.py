#!/usr/bin/env python3
"""Resolutions of Conjecture 117 and the block-ladder proposition: certification.

Certifies (1) the Conjecture 117 resolution: the Euler quadric-ladder
recurrence (n+1)(n+2)Q_{n+2}=(n+1)(7n+9)Q_{n+1}+4(n+2)(2n+3)Q_n with seeds
2, 0 reproduces the signed Chern-class Euler ladder; with SymPy, the Lagrange
parametrization A=2(1-y)^3/(1-3y), z=y(1-2y)/(2(1-y)^2), the vanishing of the
ODE (1+z)(1-8z)A''-9(1+4z)A'-24A on it, and the interval-induction
inequalities as positive-coefficient polynomials for n>=5 with base
delta_5=11/18.  (2) The block-ladder proposition: the extraction identity
S_m(B)=[y^{Am+(A-1)/2}] C_B(y)^{2m+1}/(1+y) against independent Hirzebruch
signatures at heterogeneous blocks through dimension 14, the saddle constants
Lambda_d=cot^{2(d+1)}(pi/(2(d+1))), and no violation of the open monotonicity
question on a block sample.
"""
import os
import sys
import math
import itertools
from fractions import Fraction as Fr
from math import comb, prod, pi

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aa_flux_indices import S_signature

ORD = 300


def mul(a, b, o=ORD):
    out = [Fr(0)] * (o + 1)
    for i, ai in enumerate(a[: o + 1]):
        if ai:
            for j, bj in enumerate(b[: o + 1 - i]):
                if bj:
                    out[i + j] += ai * bj
    return out


def inv(s, o=ORD):
    out = [Fr(0)] * (o + 1)
    out[0] = 1 / s[0]
    for k in range(1, o + 1):
        out[k] = -sum(s[i] * out[k - i] for i in range(1, k + 1)) * out[0]
    return out


def powser(a, e, o=ORD):
    out = [Fr(1)] + [Fr(0)] * o
    b = list(a[: o + 1])
    while e:
        if e & 1:
            out = mul(out, b, o)
        e >>= 1
        if e:
            b = mul(b, b, o)
    return out


def euler_ci(n, degs):
    r = len(degs)
    num = [comb(n + r + 1, k) for k in range(n + 1)]
    for d in degs:
        out = [0] * (n + 1)
        for k in range(n + 1):
            out[k] = num[k] - d * (out[k - 1] if k else 0)
        num = out
    return prod(degs) * num[n]


def check_euler_recurrence(nmax=40):
    true = [(-1) ** n * euler_ci(n, tuple([2] * (n + 1))) for n in range(nmax + 1)]
    rec = [2, 0]
    for n in range(nmax - 1):
        v = (n + 1) * (7 * n + 9) * rec[-1] + 4 * (n + 2) * (2 * n + 3) * rec[-2]
        D = (n + 1) * (n + 2)
        assert v % D == 0
        rec.append(v // D)
    assert rec == true
    q5 = Fr(rec[6], rec[5])
    assert Fr(4, 7) < 8 - q5 < Fr(4, 6) and 8 - q5 == Fr(11, 18)
    for n in range(5, nmax - 1):
        qa, qb = Fr(rec[n + 1], rec[n]), Fr(rec[n + 2], rec[n + 1])
        assert qa < qb < 8 and Fr(4, n + 2) < 8 - qa < Fr(4, n + 1)
    print(f"117: recurrence == signed Euler ladder, corridor and base exact, n<={nmax}: OK")


def check_symbolic():
    import sympy as sp

    y, n, k = sp.symbols("y n k")
    phi = 2 * (1 - y) ** 2 / (1 - 2 * y)
    z_of_y = y / phi
    dz = sp.simplify(sp.diff(z_of_y, y))
    A = sp.simplify(1 / dz)
    assert sp.simplify(A - 2 * (1 - y) ** 3 / (1 - 3 * y)) == 0

    def ddz(F):
        return sp.simplify(sp.diff(F, y) / dz)

    ode = sp.simplify(sp.factor(sp.together(
        (1 + z_of_y) * (1 - 8 * z_of_y) * ddz(ddz(A)) - 9 * (1 + 4 * z_of_y) * ddz(A) - 24 * A)))
    assert ode == 0

    f = lambda q: (7 * n + 9) / (n + 2) + 4 * (2 * n + 3) / ((n + 1) * q)
    L = 8 - sp.Rational(4) / (n + 1)
    U = 8 - sp.Rational(4) / (n + 2)
    for e in (f(U) - (8 - 4 / (n + 2)), (8 - 4 / (n + 3)) - f(L)):
        num, den = sp.fraction(sp.factor(sp.together(e)))
        for part in (num, den):
            p = sp.Poly(sp.expand(part.subs(n, k + 5)), k)
            assert all(c > 0 for c in p.all_coeffs())
    print("117: parametrization, ODE identity, interval-step positivity: OK")


def C_d_series(d, o=ORD):
    P = [Fr(0)] * (o + 1)
    Q = [Fr(0)] * (o + 1)
    for j in range(0, d // 2 + 1):
        if 2 * j + 1 <= d:
            P[j] = Fr((-1) ** j * comb(d, 2 * j + 1))
        Q[j] = Fr((-1) ** j * comb(d, 2 * j))
    return mul(P, inv(Q, o), o)


def block_ladder(B, mmax):
    A = sum(d - 1 for d in B)
    C = [Fr(1)] + [Fr(0)] * ORD
    for d in B:
        C = mul(C, C_d_series(d))
    onep = inv([Fr(1), Fr(1)] + [Fr(0)] * (ORD - 1))
    out = []
    for m in range(mmax + 1):
        idx = A * m + (A - 1) // 2
        if idx > ORD:
            break
        v = mul(powser(C, 2 * m + 1), onep)[idx]
        assert v.denominator == 1
        out.append(int(v))
    return out


def check_extraction_battery():
    tests = [((2,), 1), ((2,), 2), ((2,), 3), ((4,), 0), ((4,), 1), ((6,), 0),
             ((2, 3), 0), ((2, 3), 1), ((3, 4), 0), ((3, 4), 1),
             ((2, 2, 4), 0), ((2, 2, 4), 1), ((2, 5), 0)]
    for B, m in tests:
        A = sum(d - 1 for d in B)
        n = A * (2 * m + 1) - 1
        cfg = tuple(sorted(B * (2 * m + 1)))
        assert block_ladder(B, m)[m] == S_signature(n, cfg), (B, m)
    print(f"blocks: extraction identity == Hirzebruch signatures at {len(tests)} pairs: OK")


def C_B_val(B, y):
    v = 1.0
    for d in B:
        v *= math.tan(d * math.atan(math.sqrt(y))) / math.sqrt(y)
    return v


def Lambda_B(B):
    A = sum(d - 1 for d in B)
    hi = min(math.tan(pi / (2 * d)) ** 2 for d in B if d >= 2) * (1 - 1e-9)
    lo = 1e-9

    def mu(yv):
        h = yv * 1e-6
        return yv * (math.log(C_B_val(B, yv + h)) - math.log(C_B_val(B, yv - h))) / (2 * h)

    for _ in range(200):
        mid = (lo + hi) / 2
        if mu(mid) < A / 2:
            lo = mid
        else:
            hi = mid
    ys = (lo + hi) / 2
    return C_B_val(B, ys) ** 2 / ys ** A


def check_saddle_and_monotonicity():
    for d in (2, 4, 6):
        closed = (1 / math.tan(pi / (2 * (d + 1)))) ** (2 * (d + 1))
        assert abs(Lambda_B((d,)) - closed) / closed < 1e-6
    assert abs(Lambda_B((2,)) - 27) < 1e-6
    viol = 0
    blocks = [B for L in range(1, 4)
              for B in itertools.combinations_with_replacement(range(2, 6), L)
              if sum(d - 1 for d in B) % 2 == 1]
    for B in blocks:
        S = block_ladder(B, 4)
        rats = [Fr(S[m + 1], S[m]) for m in range(len(S) - 1)]
        lam = Lambda_B(B)
        if not all(rats[i] < rats[i + 1] for i in range(len(rats) - 1)) or \
           not all(r < lam for r in rats):
            viol += 1
    assert viol == 0
    print(f"blocks: Lambda_d closed forms and {len(blocks)}-block monotonicity sample: OK")




def check_open_question_structure():
    """Verify the exact structure recorded in the open-question remark."""
    import math
    import sympy as sp
    from math import tan, pi
    # Riccati identity, numeric, d=2..8
    for d in range(2, 9):
        for th in (0.13, 0.31, 0.52):
            yv = math.tan(th) ** 2
            C = math.tan(d * th) / math.tan(th)
            h = 1e-7
            th2 = math.atan(math.sqrt(yv + h))
            C2 = math.tan(d * th2) / math.tan(th2)
            Cp = (C2 - C) / h
            res = 2 * yv * (1 + yv) * Cp - (d * yv * C * C - (1 + yv) * C + d)
            assert abs(res) < 1e-3 * max(1.0, abs(d * yv * C * C)), (d, th)
    # Stieltjes continued fraction, depth d-1, symbolic series match d=2..8
    w = sp.symbols("w")
    for d in (2, 4, 6, 8):
        cf = sp.Integer(0)
        for j in range(d - 1, 0, -1):
            cf = sp.Rational(d * d - j * j, 4 * j * j - 1) * w / (1 - cf)
        cf = sp.cancel(1 / (1 - cf))
        target = C_d_series(d, 12)
        ser = sp.series(cf, w, 0, 12).removeO()
        for k in range(12):
            c = target[k]
            assert sp.Rational(c.numerator, c.denominator) / d == ser.coeff(w, k), (d, k)
    # b^{(2)}: log-convex through n=38; shifted Hankel order 3 negative, unshifted order 9
    a = [2, 16]
    for m in range(40):
        D = (m + 2) * (2 * m + 3) * (14 * m + 9)
        M = 6 * (3 * m + 2) * (3 * m + 4) * (14 * m + 23)
        a.append(((M - D) * a[-1] + M * a[-2]) // D)
    b = [a[n] // 2 ** (2 * n + 1) for n in range(40)]
    assert all(a[n] % 2 ** (2 * n + 1) == 0 for n in range(40))
    assert all(b[n - 1] * b[n + 1] > b[n] ** 2 for n in range(1, 39))
    h3 = sp.Matrix(3, 3, lambda i, j: b[i + j + 1]).det()
    h9 = sp.Matrix(9, 9, lambda i, j: b[i + j]).det()
    h8 = sp.Matrix(8, 8, lambda i, j: b[i + j]).det()
    assert h3 < 0 and h9 < 0 and h8 > 0
    # critical-point PGF: P_d(1)=1 and mean (d-1)/2, d=4,6
    for d in (4, 6):
        r = tan(pi / (2 * (d + 1))) ** 2
        Cs = [float(c) for c in C_d_series(d, 100)]
        Pd = [r * Cs[k] * r ** k for k in range(101)]
        assert abs(sum(Pd) - 1) < 1e-8
        assert abs(sum(k * Pd[k] for k in range(101)) - (d - 1) / 2) < 1e-7
        Yd = [0.0] * 101
        for k in range(101):
            Yd[k] = (1 + r) * Pd[k] - (r * Yd[k - 1] if k else 0)
        assert all(c > -1e-10 for c in Yd)
    print("open-question structure: Riccati, continued fraction, Hankel boundary, "
          "log-convexity, critical-point PGFs: OK")


if __name__ == "__main__":
    import time
    t0 = time.time()
    check_euler_recurrence()
    try:
        check_symbolic()
    except ImportError:
        print("sympy unavailable; symbolic certification skipped")
    check_extraction_battery()
    check_saddle_and_monotonicity()
    try:
        check_open_question_structure()
    except ImportError:
        print("sympy unavailable; open-question structure checks skipped")
    print(f"done in {time.time()-t0:.1f}s")
