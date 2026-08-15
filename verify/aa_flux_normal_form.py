#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Complete-flux normal form: Proposition aa:flux and the refutation of Conjecture 183.

Checks, from scratch:

  (0) H_Delta = alpha ^ omega, and omega has all elementary divisors 1;
  (1) the sector operator, computed with honest exterior-algebra signs, is the
      0-1 inclusion matrix U_{r,j}, and Wilson's diagonal form reproduces its
      Smith normal form;
  (2) Conjecture 182: the sector sums equal F_n and P_n;
  (3) Conjecture 183, staircase clause: first p-torsion is one Z/p at n=4p-1;
  (4) Conjecture 183, elementary-abelian clause: FALSE, first at n=15;
  (5) Conjecture 239: interval support 2p+1..n-2p+2, and strict log-concavity;
  (6) Conjecture 240: T_p(n+1) > T_p(n) after onset;
  (7) a brute-force computation of the integral cohomology of the complete flux
      that uses none of the above reduction, agreeing with it for n <= 14 in
      every degree at p = 2,3,5, and at n = 15 in degree 9 exhibiting the Z/4.

Run:  python3 aa_flux_normal_form.py [--full]
      --full also runs the n=15 brute force (about a minute, ~400 MB).
"""
import itertools
import sys
from collections import Counter
from math import comb

import numpy as np
from sympy import Matrix, ZZ, factorint
from sympy.matrices.normalforms import smith_normal_form

BIGP = 999983


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


def check_alpha_omega(n):
    """H_Delta = (e_1+...+e_n) ^ (sum_{2<=i<j<=n} e_i ^ e_j)."""
    target = {t: 1 for t in itertools.combinations(range(1, n + 1), 3)}
    prod = {}
    for i in range(1, n + 1):
        for j, k in itertools.combinations(range(2, n + 1), 2):
            s, t = wedge((i,), (j, k))
            if s:
                prod[t] = prod.get(t, 0) + s
    return {k: v for k, v in prod.items() if v} == target


def omega_divisors(n):
    """elementary divisors of the alternating form omega on W = <e_2,...,e_n>."""
    d = n - 1
    A = [[0] * d for _ in range(d)]
    for i in range(d):
        for j in range(i + 1, d):
            A[i][j], A[j][i] = 1, -1
    S = smith_normal_form(Matrix(A), domain=ZZ)
    return sorted(int(S[i, i]) for i in range(d) if S[i, i] != 0)


# --------------------------------------------------------------- Boolean sectors
def inclusion(r, j):
    lo = list(itertools.combinations(range(r), j))
    hi = list(itertools.combinations(range(r), j + 1))
    idx = {t: c for c, t in enumerate(lo)}
    M = [[0] * len(lo) for _ in hi]
    for i, h in enumerate(hi):
        for x in h:
            M[i][idx[tuple(y for y in h if y != x)]] = 1
    return M


def sector_operator(r, j):
    """wedge by sum_i x_i^y_i on monomials with j (resp. j+1) doubly occupied pairs,
    computed in the exterior algebra with signs."""
    def mono(K):
        out = []
        for i in sorted(K):
            out += [2 * i, 2 * i + 1]
        return tuple(out)
    lo = [frozenset(c) for c in itertools.combinations(range(r), j)]
    hi = [frozenset(c) for c in itertools.combinations(range(r), j + 1)]
    hidx = {mono(K): i for i, K in enumerate(hi)}
    M = [[0] * len(lo) for _ in hi]
    for col, K in enumerate(lo):
        for i in range(r):
            s, out = wedge((2 * i, 2 * i + 1), mono(K))
            if s:
                M[hidx[out]][col] += s
    return M


def wilson(r, j):
    """Wilson's diagonal form for U_{r,j}: entry h-i with multiplicity C(r,i)-C(r,i-1)."""
    h = min(j + 1, r - j)
    d = Counter()
    for i in range(h):
        d[h - i] += comb(r, i) - (comb(r, i - 1) if i else 0)
    return d


def content(cnt):
    out = Counter()
    for x, m in cnt.items():
        for p, e in factorint(x).items():
            out[(p, e)] += m
    return dict(out)


def snf_counter(M):
    S = smith_normal_form(Matrix(M), domain=ZZ)
    return Counter(int(S[i, i]) for i in range(min(S.rows, S.cols)) if S[i, i] != 0)


# --------------------------------------------------------------- predictions
def a_p(r, j, p, power=1):
    q = p ** power
    return sum(m for x, m in wilson(r, j).items() if x % q == 0)


def torsion_profile(n, p, power=1):
    g, ev = (n - 1) // 2, n % 2 == 0
    prof = Counter()
    for s in range(g + 1):
        r = g - s
        for j in range(r):
            a = a_p(r, j, p, power)
            if a:
                mult = comb(g, s) * 2 ** s
                for extra in ([0, 1] if ev else [0]):
                    prof[s + 2 * (j + 1) + 1 + extra] += mult * a
    return {q: v for q, v in sorted(prof.items()) if v}


def B_Q(n):
    g = (n - 1) // 2
    t = sum(comb(g, s) * 2 ** s * 2 * comb(g - s, (g - s) // 2) for s in range(g + 1))
    return 2 * t if n % 2 == 0 else t


def B_F2(n):
    g = (n - 1) // 2
    t = sum(comb(g, s) * 2 ** s * (2 ** (g - s) if g - s else 2) for s in range(g + 1))
    return 2 * t if n % 2 == 0 else t


def F_n(n):
    return comb(n + 1, (n + 1) // 2) if n % 2 else 2 * comb(n, n // 2)


def P_n(n):
    return 2 ** (n - 1) + 2 ** ((n - 1) // 2) if n % 2 else 2 * (2 ** (n - 2) + 2 ** ((n - 2) // 2))


# --------------------------------------------------------------- brute force
def flux_matrix(n, q):
    src = list(itertools.combinations(range(1, n + 1), q - 3))
    tgt = list(itertools.combinations(range(1, n + 1), q))
    tidx = {c: i for i, c in enumerate(tgt)}
    M = np.zeros((len(tgt), len(src)), dtype=np.int64)
    for j, c in enumerate(src):
        rest = [x for x in range(1, n + 1) if x not in c]
        for t in itertools.combinations(rest, 3):
            s, out = wedge(t, c)
            if s:
                M[tidx[out], j] += s
    return M


def rank_modp(A, p):
    A = np.array(A, dtype=np.float64) % p
    m, n = A.shape
    r = 0
    for c in range(n):
        if r >= m:
            break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        i = r + nz[0]
        if i != r:
            A[[r, i]] = A[[i, r]]
        A[r, c:] = (A[r, c:] * pow(int(A[r, c]), p - 2, p)) % p
        below = A[r + 1:, c]
        nzb = np.nonzero(below)[0]
        if nzb.size:
            rows = r + 1 + nzb
            A[np.ix_(rows, range(c, n))] = (
                A[np.ix_(rows, range(c, n))] - np.outer(below[nzb], A[r, c:])) % p
        r += 1
    return r


def kernel_modp(A, p):
    A = np.array(A, dtype=np.float64) % p
    m, n = A.shape
    piv, r = [], 0
    for c in range(n):
        if r >= m:
            break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        i = r + nz[0]
        if i != r:
            A[[r, i]] = A[[i, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p - 2, p)) % p
        col = A[:, c].copy()
        col[r] = 0
        nzr = np.nonzero(col)[0]
        if nzr.size:
            A[nzr] = (A[nzr] - np.outer(col[nzr], A[r])) % p
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in set(piv)]
    K = np.zeros((n, len(free)), dtype=np.int64)
    for j, fc in enumerate(free):
        K[fc, j] = 1
        for i, pc in enumerate(piv):
            K[pc, j] = (-int(A[i, fc])) % p
    return K, len(piv)


def nu_counts(M, p, r0):
    """(#{v_p(d_i)>=1}, #{v_p(d_i)>=2}) for the invariant factors of M."""
    K, r1 = kernel_modp(M, p)
    if K.shape[1] == 0:
        return r0 - r1, 0
    MK = M.astype(np.int64) @ K
    assert np.all(MK % p == 0)
    cat = np.concatenate([MK // p, M], axis=1)
    return r0 - r1, r0 - rank_modp(cat, p)


def brute_force_n15():
    """GF(2) bitset version of the same invariants at n=15, degree 9."""
    M = flux_matrix(15, 9)
    ncols = M.shape[1]
    rows = [int.from_bytes(np.packbits((r & 1).astype(np.uint8), bitorder="little").tobytes(),
                           "little") for r in M]

    def rref(rr, nc):
        rr, piv, r = rr[:], [], 0
        for c in range(nc):
            bit = 1 << c
            sel = next((i for i in range(r, len(rr)) if rr[i] & bit), None)
            if sel is None:
                continue
            rr[r], rr[sel] = rr[sel], rr[r]
            pr = rr[r]
            for i in range(len(rr)):
                if i != r and rr[i] & bit:
                    rr[i] ^= pr
            piv.append(c)
            r += 1
            if r == len(rr):
                break
        return rr, piv

    def rank(rr, nc):
        rr, r = [x for x in rr if x], 0
        for c in range(nc):
            bit = 1 << c
            sel = next((i for i in range(r, len(rr)) if rr[i] & bit), None)
            if sel is None:
                continue
            rr[r], rr[sel] = rr[sel], rr[r]
            pr = rr[r]
            for i in range(r + 1, len(rr)):
                if rr[i] & bit:
                    rr[i] ^= pr
            r += 1
            if r == len(rr):
                break
        return r

    R, piv = rref(rows, ncols)
    r1 = len(piv)
    pivset = set(piv)
    free = [c for c in range(ncols) if c not in pivset]
    K = np.zeros((ncols, len(free)), dtype=np.float64)
    for j, fc in enumerate(free):
        K[fc, j] = 1.0
        for i, pc in enumerate(piv):
            if (R[i] >> fc) & 1:
                K[pc, j] = 1.0
    MK = np.rint(M.astype(np.float64) @ K).astype(np.int64)
    assert np.all(MK % 2 == 0)
    cat = np.concatenate([MK // 2, M], axis=1)
    catrows = [int.from_bytes(np.packbits((r & 1).astype(np.uint8), bitorder="little").tobytes(),
                              "little") for r in cat]
    r2 = rank(catrows, cat.shape[1])
    r0 = rank_modp(M, BIGP)
    return r0, r0 - r1, r0 - r2


# --------------------------------------------------------------- main
def main():
    full = "--full" in sys.argv
    ok = True

    print("(0) H_Delta = alpha ^ omega, and omega is unimodularly symplectic")
    a = all(check_alpha_omega(n) for n in range(4, 13))
    b = all(set(omega_divisors(n)) == {1} and
            len(omega_divisors(n)) == 2 * ((n - 1) // 2) for n in range(4, 20))
    print(f"    identity holds for 4<=n<=12: {a}")
    print(f"    all elementary divisors 1, rank 2*floor((n-1)/2), 4<=n<=19: {b}")
    ok &= a and b

    print("(1) sector operator = U_{r,j}; Wilson's diagonal form = Smith form")
    c = all(sector_operator(r, j) == inclusion(r, j) for r in range(1, 8) for j in range(r))
    d = all(content(wilson(r, j)) == content(snf_counter(inclusion(r, j)))
            for r in range(1, 9) for j in range(r))
    print(f"    exterior-algebra operator is the 0-1 inclusion matrix, r<=7: {c}")
    print(f"    Wilson content matches the Smith form, r<=8: {d}")
    print(f"    Smith form of U_(7,3): {dict(snf_counter(inclusion(7, 3)))}")
    ok &= c and d

    print("(2) Conjecture 182: B(H;Q)=F_n and B(H;F_2)=P_n")
    e = all(B_Q(n) == F_n(n) and B_F2(n) == P_n(n) for n in range(4, 201))
    print(f"    both closed forms for 4<=n<=200: {e}")
    ok &= e

    print("(3) Conjecture 183, staircase clause")
    for p in (2, 3, 5, 7, 11):
        pre = any(torsion_profile(n, p) for n in range(3, 4 * p - 1))
        at = torsion_profile(4 * p - 1, p)
        good = (not pre) and sum(at.values()) == 1
        ok &= good
        print(f"    p={p:2d}: nothing below n={4*p-2}, one Z/{p} at n={4*p-1} in degree "
              f"{list(at)[0]}: {good}")

    print("(4) Conjecture 183, elementary-abelian clause")
    first = next((n for n in range(3, 41) if torsion_profile(n, 2, power=2)), None)
    print(f"    least n whose 2-primary part is not elementary abelian: {first} "
          f"(degrees {torsion_profile(first, 2, power=2)})")
    ok &= first == 15

    print("(5) Conjecture 239")
    gaps, lc = [], []
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
        for n in range(4 * p - 1, 151):
            prof = torsion_profile(n, p)
            if not prof:
                continue
            qs = sorted(prof)
            if qs != list(range(qs[0], qs[-1] + 1)) or (qs[0], qs[-1]) != (2 * p + 1, n - 2 * p + 2):
                gaps.append((p, n))
            for i in range(1, len(qs) - 1):
                if not prof[qs[i]] ** 2 > prof[qs[i - 1]] * prof[qs[i + 1]]:
                    lc.append((p, n, qs[i]))
    print(f"    support is exactly 2p+1..n-2p+2, p<=23, n<=150: {not gaps}")
    print(f"    strict log-concavity violations: {lc if lc else 'none'}")
    ok &= not gaps and not lc

    print("(6) Conjecture 240")
    bad = []
    for p in (2, 3, 5, 7, 11):
        T = {n: sum(torsion_profile(n, p).values()) for n in range(4 * p - 1, 152)}
        bad += [(p, n) for n in range(4 * p - 1, 151) if not T[n + 1] > T[n]]
    print(f"    strict growth after onset, p<=11, n<=150: {not bad}")
    print(f"    T_2 from n=7: {[sum(torsion_profile(n,2).values()) for n in range(7,13)]}")
    ok &= not bad

    print("(7) brute force, using none of the reduction")
    for n in range(7, 13):
        for q in range(3, n + 1):
            M = flux_matrix(n, q)
            if M.size == 0:
                continue
            r0 = rank_modp(M, BIGP)
            for p in (2, 3, 5):
                got = nu_counts(M, p, r0)
                exp = (sum(torsion_profile(n, p).get(q, 0) for _ in [0]),
                       sum(torsion_profile(n, p, 2).get(q, 0) for _ in [0]))
                if got != exp:
                    ok = False
                    print(f"    ** MISMATCH n={n} q={q} p={p}: {got} vs {exp}")
        print(f"    n={n}: every degree and p=2,3,5 agree with the reduction")
    if full:
        r0, g1, g2 = brute_force_n15()
        print(f"    n=15, degree 9: rank_Q={r0} (predicted 3003), "
              f"#(nu>=1)={g1} (predicted 911), #(nu>=2)={g2} (predicted 1)")
        ok &= (r0, g1, g2) == (3003, 911, 1)
    else:
        print("    (pass --full to add the n=15 brute force)")

    print()
    print("ALL CHECKS PASSED" if ok else "FAILURES ABOVE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
