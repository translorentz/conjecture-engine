#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Support obstructions and coefficient rescaling: Propositions aa:support and
ad:cover, and the boundary control retained with Conjecture 180.

Checks, from scratch and in exact arithmetic:

  (0) the tensor factorisation: an unused coordinate multiplies the Betti
      polynomial by (1+t);
  (1) for the deposited generic profile, the largest u with g_n = (1+t)^u g_{n-u}
      is 1, attained exactly at n = 0 mod 4 -- this is what bounds the number of
      unused coordinates a saturating form may have, and hence gives
      mu_n >= (n-1)/3 and the subcritical direction of Conjecture 178;
  (2) the rescaling criterion: rank_{F_2}(A) = |S| implies the rational profile
      depends only on the support S, exhaustively over small spanning supports;
  (3) the retained boundary control for Conjecture 180: the four-triple support
      {012,013,024,034} on five coordinates is coefficient-sensitive, the two
      profiles are separated exactly by the vanishing of a Pfaffian, and the
      probability of the degenerate branch depends on the coefficient set;
  (4) that this control, as a fixed circuit, is subcritical in the window; and
  (5) that the criterion is nevertheless vacuous for a typical support in that
      window, since |S| = Theta(n log n) exceeds the n columns of A -- so the
      argument localizes the mechanism but does not prove Conjecture 180.

Run:  python3 aa_support_obstructions.py
"""
import itertools
import sys
from collections import Counter
from fractions import Fraction
from math import comb


# --------------------------------------------------------------- exterior algebra
def wedge(a, b):
    c = list(a) + list(b)
    if len(set(c)) != len(c):
        return 0, None
    sign, arr = 1, c[:]
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                sign = -sign
    return sign, tuple(arr)


def rank_Q(M):
    A = [[Fraction(x) for x in row] for row in M]
    rows, cols = len(A), (len(A[0]) if A else 0)
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(r + 1, rows):
            if A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        r += 1
        if r == rows:
            break
    return r


def profile(n, support, coeffs):
    """rational Betti profile of (Lambda* Q^n, H ^ -) for H = sum c_t e_t."""
    ranks = {}
    for k in range(n + 1):
        if k + 3 > n:
            ranks[k] = 0
            continue
        dom = list(itertools.combinations(range(n), k))
        cod = list(itertools.combinations(range(n), k + 3))
        ci = {t: i for i, t in enumerate(cod)}
        M = [[0] * len(dom) for _ in cod]
        for j, b in enumerate(dom):
            for t, c in zip(support, coeffs):
                sg, u = wedge(t, b)
                if sg:
                    M[ci[u]][j] += sg * c
        ranks[k] = rank_Q(M)
    return tuple(comb(n, k) - ranks.get(k, 0) - ranks.get(k - 3, 0) for k in range(n + 1))


def rank_F2(rows, ncols):
    rows = [sum(1 << i for i in range(ncols) if r[i] % 2) for r in rows]
    rk = 0
    for c in range(ncols):
        bit = 1 << c
        sel = next((i for i in range(rk, len(rows)) if rows[i] & bit), None)
        if sel is None:
            continue
        rows[rk], rows[sel] = rows[sel], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i] & bit:
                rows[i] ^= rows[rk]
        rk += 1
    return rk


def incidence(n, supp):
    return [[1 if i in t else 0 for i in range(n)] for t in supp]


# --------------------------------------------------------------- deposited profile
def g(n):
    if n % 2 == 0:
        m = n // 2
        return {m - 1: 3 ** (m - 1), m: 2 * 3 ** (m - 1), m + 1: 3 ** (m - 1)}
    k = (n - 1) // 2
    if n % 4 == 3:
        return {k: 3 ** k, k + 1: 3 ** k}
    o = 3 if n == 9 else 1
    return {k - 1: o, k: 3 ** k, k + 1: 3 ** k, k + 2: o}


def vec(n):
    d = g(n)
    return [d.get(k, 0) for k in range(n + 2)]


def mul(v, u):
    for _ in range(u):
        v = [(v[k] if k < len(v) else 0) + (v[k - 1] if k >= 1 else 0) for k in range(len(v) + 1)]
    return v


def trim(v):
    v = list(v)
    while v and v[-1] == 0:
        v.pop()
    return v


def main():
    ok = True

    print("(0) unused coordinate multiplies the Betti polynomial by (1+t)")
    supp5 = ((0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4))
    for cf in ([1, 1, 1, 1], [1, 2, -2, -2]):
        p5 = profile(5, supp5, cf)
        p6 = profile(6, supp5, cf)          # same support, one spare coordinate
        lift = trim(mul(list(p5), 1))
        good = trim(list(p6)) == lift
        ok &= good
        print(f"    coeffs {cf}: 5-var {p5}, 6-var {p6}, (1+t)*5-var matches: {good}")

    print("(1) largest u with g_n = (1+t)^u g_(n-u), deposited profile")
    maxu = {}
    for n in range(6, 121):
        best = 0
        for u in range(1, 5):
            if n - u < 4:
                break
            if trim(vec(n)) == trim(mul(vec(n - u), u)):
                best = u
        maxu[n] = best
    ones = sorted(n for n, u in maxu.items() if u == 1)
    ok &= max(maxu.values()) == 1 and all(n % 4 == 0 for n in ones)
    print(f"    max u over 6<=n<=120 is {max(maxu.values())}; attained exactly at "
          f"n = 0 mod 4: {all(n % 4 == 0 for n in ones)}")
    print(f"    hence a saturating support of s triples has n - 3s <= 1, i.e. mu_n >= (n-1)/3")

    print("(2) rescaling criterion: rank_F2(A) = |S| implies the profile depends only on S")
    viol = tested = 0
    for n in (4, 5, 6):
        triples = list(itertools.combinations(range(n), 3))
        for e in range(2, {4: 5, 5: 5, 6: 3}[n] + 1):
            for supp in itertools.combinations(triples, e):
                if sorted(set(i for t in supp for i in t)) != list(range(n)):
                    continue
                tested += 1
                if rank_F2(incidence(n, supp), n) != e:
                    continue
                profs = set()
                for cf in itertools.product([1, -1, 2, -2], repeat=e):
                    profs.add(profile(n, supp, list(cf)))
                    if len(profs) > 1:
                        break
                if len(profs) > 1:
                    viol += 1
                    print(f"    ** VIOLATION n={n} supp={supp}")
    ok &= viol == 0
    print(f"    {tested} spanning supports tested; violations: {viol}")

    print("(3) the Conjecture 180 boundary control")
    seen = Counter()
    for cf in itertools.product([1, -1, 2, -2], repeat=4):
        seen[profile(5, supp5, list(cf))] += 1
    print(f"    profiles on {supp5}: {dict(seen)}")
    ok &= len(seen) == 2 and set(seen) == {(0, 3, 9, 9, 3, 0), (0, 1, 9, 9, 1, 0)}

    def pf(cf):
        """Pfaffian of omega, where H = e_0 ^ omega on {1,2,3,4}."""
        m = {}
        for t, c in zip(supp5, cf):
            s = tuple(x for x in t if x != 0)
            sg, _ = wedge((0,), s)
            m[s] = c * sg
        gg = lambda i, j: m.get((i, j), 0)
        return gg(1, 2) * gg(3, 4) - gg(1, 3) * gg(2, 4) + gg(1, 4) * gg(2, 3)

    split = {}
    for cf in itertools.product([1, -1, 2, -2], repeat=4):
        split.setdefault(profile(5, supp5, list(cf)), set()).add(pf(list(cf)) == 0)
    clean = all(len(v) == 1 for v in split.values())
    ok &= clean
    print(f"    profile determined by whether the Pfaffian vanishes: {clean}")
    for V, lab in [([1, -1], "{+-1}"), ([1, -1, 2, -2], "{+-1,+-2}")]:
        z = sum(1 for cf in itertools.product(V, repeat=4) if pf(list(cf)) == 0)
        print(f"    V = {lab:12s}: Pr[degenerate branch] = {z}/{len(V)**4}")

    print("(4) subcriticality of a FIXED coefficient-sensitive circuit")
    cov = Counter(i for t in supp5 for i in t)
    ok &= all(v % 2 == 0 for v in cov.values())
    print(f"    the control covers every coordinate evenly: {dict(sorted(cov.items()))}")
    print(f"    |V| = {len(cov)} <= 3|S|/2 = {3*len(supp5)/2}; expected copies at "
          f"p = c log n / n^2 are ~ n^({len(cov)-2*len(supp5)}) (log n)^{len(supp5)} -> 0")

    print("(5) but the criterion is VACUOUS in the window: |S| exceeds n there")
    from math import log
    print(f"    {'n':>7} {'c':>5} {'E|S| = C(n,3)p':>16} {'E|S| > n':>9}")
    exceeds = True
    for c in (1.0, 4.0):
        for n in (100, 1000, 10000, 100000):
            ES = comb(n, 3) * c * log(n) / n ** 2
            if n >= 1000:
                exceeds &= ES > n
            print(f"    {n:>7} {c:>5} {ES:>16.1f} {'yes' if ES > n else 'no':>9}")
    ok &= exceeds
    print("    rank_F2(A) <= n, so rank_F2(A) = |S| is impossible once |S| > n;")
    print("    dim ker(A^T) >= |S| - n = Theta(n log n), so even circuits are forced.")
    print("    The fixed-circuit bound in (4) therefore localizes the mechanism but")
    print("    cannot be summed over the >= 2^(|S|-n) circuits a typical support carries.")

    print()
    print("ALL CHECKS PASSED" if ok else "FAILURES ABOVE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
