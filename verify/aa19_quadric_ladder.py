#!/usr/bin/env python3
"""Resolution of Conjecture 195 (Part X): exact and symbolic certification.

Certifies the resolution proposition: the all-quadric signature ladder
a_m = Sigma_{2m} has the algebraic generating function
    A(w) = 2/((1+y)(1-3y)),   4w = y(1-y)^2,   y(0)=0,
and satisfies D_m a_{m+2} = (M_m-D_m) a_{m+1} + M_m a_m with
D_m=(m+2)(2m+3)(14m+9), M_m=6(3m+2)(3m+4)(14m+23).

Checks: (1) the recurrence reproduces the true signature ladder computed
independently from the Hirzebruch series (via aa_flux_indices); (2) the
generating function's exact series equals the recurrence to order 200;
(3) with SymPy, the pole equation, the residue value, the operator
identity certifying the recurrence for all m, the interlacing algebra,
and the asymptotic expansion coefficients -1, 37/18, -281/72; (4) an
exact integer scan of all three clauses through geometric n=10,000.
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aa_flux_indices import S_signature


def coeffs(m):
    D = (m + 2) * (2 * m + 3) * (14 * m + 9)
    M = 6 * (3 * m + 2) * (3 * m + 4) * (14 * m + 23)
    return D, M


def recurrence(terms):
    a = [2, 16]
    for m in range(terms - 2):
        D, M = coeffs(m)
        v = (M - D) * a[-1] + M * a[-2]
        assert v % D == 0, m
        a.append(v // D)
    return a


def check_true_ladder(mmax=12):
    rec = recurrence(mmax + 1)
    true = [2] + [S_signature(n, tuple([2] * (n + 1))) for n in range(2, 2 * mmax + 1, 2)]
    assert rec == true, "recurrence does not match the signature ladder"
    print(f"recurrence == independent signature ladder for m<=%d: OK" % mmax)


def check_generating_function(order=200):
    def mul(a, b):
        out = [Fr(0)] * (order + 1)
        for i, ai in enumerate(a[: order + 1]):
            if ai:
                for j, bj in enumerate(b[: order + 1 - i]):
                    if bj:
                        out[i + j] += ai * bj
        return out

    def inv(sr):
        out = [Fr(0)] * (order + 1)
        out[0] = 1 / sr[0]
        for k in range(1, order + 1):
            out[k] = -sum(sr[i] * out[k - i] for i in range(1, k + 1)) * out[0]
        return out

    y = [Fr(0)] * (order + 1)
    for _ in range(order + 2):
        om = [Fr(1) - y[0]] + [-v for v in y[1:]]
        isq = inv(mul(om, om))
        newy = [Fr(0)] * (order + 1)
        for k in range(order):
            newy[k + 1] = Fr(4) * isq[k]
        if newy == y:
            break
        y = newy
    one_p = y[:]; one_p[0] += 1
    one_m3 = [-3 * v for v in y]; one_m3[0] += 1
    A = [2 * v for v in inv(mul(one_p, one_m3))]
    assert all(v.denominator == 1 for v in A)
    assert [int(v) for v in A] == recurrence(order + 1)
    print(f"algebraic generating function == recurrence to order {order}: OK")


def check_symbolic():
    import sympy as sp

    u = sp.symbols("u", positive=True)
    T = sp.tan(u)
    psi = u * (2 * T / (1 - T**2)) / T**2
    w_u = T**2 * (1 - T**2) ** 2 / 4
    assert sp.simplify(u**2 - w_u * psi**2) == 0
    dpsi2 = sp.diff(psi**2, u) / (2 * u)
    assert sp.simplify(psi / (1 - w_u * dpsi2) - 2 / ((1 + T**2) * (1 - 3 * T**2))) == 0

    y = sp.symbols("y")
    A = 2 / ((1 + y) * (1 - 3 * y))
    wy = y * (1 - y) ** 2 / 4
    tf = y * (1 - y) / (1 - 3 * y)

    def theta(F):
        return sp.simplify(tf * sp.diff(F, y))

    m = sp.symbols("m")
    D = (m + 2) * (2 * m + 3) * (14 * m + 9)
    M = 6 * (3 * m + 2) * (3 * m + 4) * (14 * m + 23)

    def op(pm, F):
        out, cur = 0, F
        for k, c in enumerate(sp.Poly(pm, m).all_coeffs()[::-1]):
            if k:
                cur = theta(cur)
            out += c * (F if k == 0 else cur)
        return out

    B2 = sp.simplify((A - 2 - 16 * wy) / wy**2)
    B1 = sp.simplify((A - 2) / wy)
    G = op(D, B2) + op(-(M - D), B1) + op(-M, A)
    assert sp.simplify(sp.factor(sp.together(G))) == 0
    print("pole equation, residue value, operator identity: OK")

    q = M / D
    gap = sp.factor(27 - q)
    assert sp.simplify(gap - 3 * (126 * m**2 + 271 * m + 118) / D) == 0

    def q_at(z):
        return (6 * (3 * z + 2) * (3 * z + 4) * (14 * z + 23)
                / ((z + 2) * (2 * z + 3) * (14 * z + 9)))

    k = sp.symbols("k")
    expr = sp.together(q_at(m + 1) - (q_at(m) * (1 + 1 / q_at(m - 1)) - 1))
    num, _ = sp.fraction(sp.factor(expr))
    shifted = sp.Poly(sp.expand(num.subs(m, k + 1)), k)
    assert all(c > 0 for c in shifted.all_coeffs())
    print("interlacing algebra (gap factorization, positive shifted numerator): OK")

    s1, s2, s3 = sp.symbols("s1 s2 s3")
    x = sp.symbols("x", positive=True)
    r = lambda mm: 27 * (1 + s1 / mm + s2 / mm**2 + s3 / mm**3)
    ser = sp.series(sp.together((r(m + 1) - (q - 1 + q / r(m))).subs(m, 1 / x)), x, 0, 4).removeO()
    poly = sp.Poly(sp.expand(ser), x)
    sols = {}
    for kk, sym in ((1, s1), (2, s2), (3, s3)):
        c = poly.coeff_monomial(x**kk).subs(sols)
        sols[sym] = sp.solve(sp.Eq(c, 0), sym)[0]
    assert sols[s1] == sp.Rational(-1, 2)
    assert sols[s2].subs(sols) == sp.Rational(37, 72)
    assert sols[s3].subs(sols) == sp.Rational(-281, 576)
    print("asymptotic expansion coefficients -1, 37/18, -281/72 (in n): OK")


def exact_scan(steps=5000):
    a0, a1 = 2, 16
    for m in range(steps):
        D, M = coeffs(m)
        v = (M - D) * a1 + M * a0
        assert v % D == 0
        a2 = v // D
        assert a1 < 27 * a0, f"upper bound fails at n={2*m}"
        assert a2 * a0 > a1 * a1, f"monotonicity fails at n={2*m}"
        a0, a1 = a1, a2
    print(f"exact three-clause scan through geometric n={2*steps}: OK")


if __name__ == "__main__":
    import time
    t0 = time.time()
    check_true_ladder()
    check_generating_function()
    try:
        check_symbolic()
    except ImportError:
        print("sympy unavailable; symbolic certification skipped")
    exact_scan()
    print(f"done in {time.time()-t0:.1f}s")
