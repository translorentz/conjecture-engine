#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Proposition w:shock and Proposition x:landau: the two-sided shock forcing
and the Landau floor for minimal mapping-torus cohomology.

Checks, from scratch and in exact arithmetic:

  (1) the binomial-slice and Fuss--Catalan jump identities, against direct
      factorization of the binomials;
  (2) nonproportionality of the form families for all small parameters;
  (3) the Chinese-remainder forcing of Proposition w:shock in practice:
      six primes per form drive J_{3,n} <= -20, J_{4,n} <= -30, and
      J_{3,n} >= +21, beyond every corpus extreme;
  (4) the character-average orbit formula P = (1/m) sum_j det(I + A^j)
      against direct enumeration of signed subset orbits with wedge
      reordering signs, over every orientation-preserving signed cycle
      type through dimension 9;
  (5) the exact minima M_d for d = 4..13, reproducing the deposited law
      2^floor((d+3)/2) through d = 11, the value 160 at d = 12, and 320
      at d = 13, each argmin respecting the Landau floor 2^(d+1)/ord(A);
  (6) the torsion budget x20 (N <= 2P) on every type through d = 13; and
  (7) the divergence of the floor 2^d/g(d) past (sqrt 2)^d, with the
      near-coincidence log2 g(d) ~ d/2 across the tested range d <= 21
      that explains the square-root illusion.

Run:  python3 wx_shock_landau.py
"""
import itertools
import sys
from math import gcd, isqrt, prod


# ------------------------------------------------------------------ arithmetic
def lcm(a, b):
    return a * b // gcd(a, b)


def Om(n):
    """Omega with multiplicity; sympy's factorint handles the large forced
    values (heights up to ~1e35) that trial division cannot."""
    from sympy import factorint
    return sum(factorint(int(n)).values())


def binom(n, k):
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


def primes_from(start, count):
    ps, p = [], max(start, 2)
    def isp(x):
        if x < 2:
            return False
        for q in range(2, isqrt(x) + 1):
            if x % q == 0:
                return False
        return True
    while len(ps) < count:
        p += 1
        if isp(p):
            ps.append(p)
    return ps


def crt(rems, mods):
    r, m = 0, 1
    for ri, mi in zip(rems, mods):
        g = gcd(m, mi)
        assert g == 1
        r = (r + m * ((ri - r) * pow(m, -1, mi) % mi)) % (m * mi)
        m *= mi
    return r, m


# ------------------------------------------------------------- signed orbits
def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def signed_types(d):
    for part in partitions(d):
        for signs in itertools.product((1, -1), repeat=len(part)):
            det = 1
            for L, s in zip(part, signs):
                det *= (-1) ** (L - 1) * s
            if det == 1:
                yield part, signs


def orbit_counts_formula(part, signs):
    """P, N, ord(A) by character average and unsigned Burnside."""
    m = 1
    for L, s in zip(part, signs):
        m = lcm(m, L if s == 1 else 2 * L)
    tot = 0
    for j in range(m):
        det = 1
        for L, s in zip(part, signs):
            if j == 0:
                det *= 2 ** L
                continue
            g = gcd(j, L)
            Lp = L // g
            hol = s ** (j // g)
            f = 1 - (-1) ** Lp * hol
            det *= f ** g
            if det == 0:
                break
        tot += det
    assert tot % m == 0
    P = tot // m
    ms = 1
    for L in part:
        ms = lcm(ms, L)
    tot2 = 0
    for j in range(ms):
        c = sum(gcd(j, L) if j else L for L in part)
        tot2 += 2 ** c
    assert tot2 % ms == 0
    return P, tot2 // ms - P, m


def orbit_counts_direct(part, signs):
    """Gold standard: enumerate subsets, track entry signs AND wedge
    reordering signs around each orbit."""
    d = sum(part)
    sigma = [0] * d
    esign = [1] * d
    base = 0
    for L, s in zip(part, signs):
        for j in range(L):
            sigma[base + j] = base + (j + 1) % L
        esign[base + L - 1] = s
        base += L

    def step(T):
        elems = [p for p in range(d) if T >> p & 1]
        imgs = [sigma[p] for p in elems]
        sg = 1
        for p in elems:
            sg *= esign[p]
        inv = sum(1 for i in range(len(imgs)) for j in range(i + 1, len(imgs))
                  if imgs[i] > imgs[j])
        if inv % 2:
            sg = -sg
        U = 0
        for q in imgs:
            U |= 1 << q
        return U, sg

    P = N = 0
    seen = bytearray(1 << d)
    for S in range(1 << d):
        if seen[S]:
            continue
        T, hol = S, 1
        while True:
            seen[T] = 1
            T, sg = step(T)
            hol *= sg
            if T == S:
                break
        if hol == 1:
            P += 1
        else:
            N += 1
    return P, N


def landau(n):
    best = [1] * (n + 1)
    sieve = list(range(n + 1))
    for i in range(2, isqrt(n) + 1):
        if sieve[i] == i:
            for j in range(i * i, n + 1, i):
                if sieve[j] == j:
                    sieve[j] = i
    for p in [i for i in range(2, n + 1) if sieve[i] == i]:
        q = p
        while q <= n:
            for tot in range(n, q - 1, -1):
                cand = best[tot - q] * q
                if cand > best[tot]:
                    best[tot] = cand
            q *= p
    return best[n]


def main():
    ok = True

    print("(1) jump identities against direct factorization")
    bad = 0
    for k in (2, 3, 4, 5):
        for n in (3, 7, 12, 20):
            lhs = Om(binom(k * (n + 1), n + 1)) - Om(binom(k * n, n))
            rhs = Om(k) + sum(Om(k * n + j) - Om((k - 1) * n + j) for j in range(1, k))
            bad += lhs != rhs
    for r in (1, 2, 3, 4):
        for n in (3, 7, 12, 20):
            F = lambda m: binom((r + 1) * m, m) // (r * m + 1)
            lhs = Om(F(n + 1)) - Om(F(n))
            rhs = (Om(r + 1) + sum(Om((r + 1) * n + j) for j in range(1, r + 1))
                   - Om(r * n + r + 1) - sum(Om(r * n + j) for j in range(2, r + 1)))
            bad += lhs != rhs
    ok &= bad == 0
    print(f"    32 parameter pairs, mismatches: {bad}")

    print("(2) nonproportionality of the form families")
    viol = 0
    for k in range(2, 40):
        for j in range(1, k):
            for jp in range(1, k):
                if k * jp == (k - 1) * j:
                    viol += 1
    for r in range(1, 40):
        for j in range(1, r + 1):
            for jp in range(2, r + 2):
                if (r + 1) * jp == r * j:
                    viol += 1
    ok &= viol == 0
    print(f"    parameters through 39, proportional pairs: {viol}")

    print("(3) six-prime forcing witnesses")
    for k, target in ((3, -20), (4, -30)):
        mods, rems = [], []
        p0 = 2 * k * k
        for j in range(1, k):
            ps = primes_from(p0, 6)
            p0 = ps[-1]
            q = prod(ps)
            mods.append(q)
            rems.append((-j * pow(k - 1, -1, q)) % q)
        r0, Q = crt(rems, mods)
        best = None
        for t in range(200):
            n = r0 + t * Q
            if n < 2:
                continue
            J = Om(k) + sum(Om(k * n + j) - Om((k - 1) * n + j) for j in range(1, k))
            best = J if best is None else min(best, J)
        ok &= best <= target
        print(f"    k={k}: min J over 200 progression steps = {best} (target {target})")
    mods, rems = [], []
    p0 = 18
    for j in range(1, 3):
        ps = primes_from(p0, 6)
        p0 = ps[-1]
        q = prod(ps)
        mods.append(q)
        rems.append((-j * pow(3, -1, q)) % q)
    r0, Q = crt(rems, mods)
    best = None
    for t in range(200):
        n = r0 + t * Q
        if n < 2:
            continue
        J = Om(3) + sum(Om(3 * n + j) - Om(2 * n + j) for j in range(1, 3))
        best = J if best is None else max(best, J)
    ok &= best >= 21
    print(f"    k=3 positive side: max J = +{best} (target +21)")

    print("(4) character-average formula vs direct wedge-sign enumeration, d<=9")
    bad = tested = 0
    for d in range(1, 10):
        for part, sg in signed_types(d):
            tested += 1
            a = orbit_counts_direct(part, sg)
            b = orbit_counts_formula(part, sg)[:2]
            if a != b:
                bad += 1
    ok &= bad == 0
    print(f"    {tested} orientation-preserving types, mismatches: {bad}")

    print("(5) exact minima and the Landau floor, d = 4..13")
    expected = {4: 8, 5: 16, 6: 16, 7: 32, 8: 32, 9: 64, 10: 64, 11: 128, 12: 160, 13: 320}
    for d in range(4, 14):
        best = floor_ok = None
        x20ok = True
        for part, sg in signed_types(d):
            P, N, m = orbit_counts_formula(part, sg)
            B = 2 * P
            if N > 2 * P:
                x20ok = False
            if B * m < 2 ** (d + 1):
                floor_ok = False
            if best is None or B < best:
                best = B
        ok &= best == expected[d] and x20ok and floor_ok is None
        print(f"    d={d:>2}: M_d = {best:>4} (expected {expected[d]:>4}); "
              f"x20 holds: {x20ok}; every type obeys 2P >= 2^(d+1)/ord(A): {floor_ok is None}")

    print("(6) floor 2^d/g(d) vs (sqrt2)^d, and the small-d coincidence")
    for d in (12, 21, 30, 50, 100):
        g = landau(d)
        lb = 2 ** d / g
        halfd = 2 ** (d / 2)
        note = f"log2 g({d}) = {g.bit_length() - 1 + (g / 2**(g.bit_length()-1) > 1.414):.0f}~"
        print(f"    d={d:>3}: g(d)={g:>15}  2^d/g(d)={lb:>12.3e}  (sqrt2)^d={halfd:>12.3e}"
              f"  ratio={lb/halfd:>10.2e}")
    ok &= 2 ** 50 / landau(50) > 2 ** 25 and 2 ** 100 / landau(100) > 2 ** 50

    print()
    print("ALL CHECKS PASSED" if ok else "FAILURES ABOVE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
