#!/usr/bin/env python3
"""Part X (Conjectures 177-196) independent reproduction, from scratch.

Reimplements both programmes with no code shared with the deposited scans:
the flux programme with bitmask exterior algebra, own sign rule, packed-bitset
and vectorized F_p elimination, and an own Smith normal form; the CICY
programme with the scaled Hirzebruch characteristic series, the signature
recovered as chi_{y=1} rather than by a separate L-genus route, and exact
Fraction arithmetic.  Ranges are kept modest so the script runs in a few
minutes; the deposited evidence and the full review scans reach further."""

import random
from itertools import combinations
from math import comb

# ---------- exterior algebra with bitmask bases ----------
def subsets_bit(n, k):
    return [sum(1 << i for i in c) for c in combinations(range(n), k)]

def sign_merge(tri_mask, s_mask, tri_elems):
    # sign of e_T wedge e_S: (-1)^{#{(t,s): t in T, s in S, s < t}}
    inv = 0
    for t in tri_elems:
        inv += bin(s_mask & ((1 << t) - 1)).count("1")
    return -1 if inv & 1 else 1

def dH_matrix(n, flux, k):
    """Matrix of alpha -> H ^ alpha from Lambda^k to Lambda^{k+3}; rows=codomain."""
    dom = subsets_bit(n, k)
    cod = subsets_bit(n, k + 3)
    cindex = {m: i for i, m in enumerate(cod)}
    M = [[0] * len(dom) for _ in range(len(cod))]
    fl = [(sum(1 << i for i in t), t, c) for t, c in flux.items() if c]
    for j, s in enumerate(dom):
        for tmask, telems, c in fl:
            if tmask & s:
                continue
            M[cindex[tmask | s]][j] += c * sign_merge(tmask, s, telems)
    return M

import numpy as _np

def rank_mod_p(M, p):
    if not M or not M[0]:
        return 0
    if p == 2:
        # packed bitset elimination
        rows = [int("".join("1" if x & 1 else "0" for x in row[::-1]), 2) if any(x & 1 for x in row) else 0 for row in M]
        rows = [r for r in rows if r]
        r = 0
        pivots = []
        for row in rows:
            cur = row
            for pb, pr in pivots:
                if cur >> pb & 1:
                    cur ^= pr
            if cur:
                pivots.append((cur.bit_length() - 1, cur))
        return len(pivots)
    A = _np.array(M, dtype=_np.int64) % p
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        nz = _np.flatnonzero(A[r:, c])
        if nz.size == 0:
            continue
        piv = r + int(nz[0])
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        A[r] = A[r] * pow(int(A[r, c]), -1, p) % p
        col = A[:, c].copy()
        col[r] = 0
        A = (A - _np.outer(col, A[r])) % p
        r += 1
        if r == rows:
            break
    return r

PRIMES = [1_000_003, 999_999_937, 2_147_483_647]

def betti(n, flux, p):
    ranks = [rank_mod_p(dH_matrix(n, flux, k), p) for k in range(n - 2)]
    prof = []
    for k in range(n + 1):
        b = comb(n, k)
        if k >= 3:
            b -= ranks[k - 3]
        if k <= n - 3:
            b -= ranks[k]
        prof.append(b)
    return tuple(prof)

def total(n, flux, p):
    return sum(betti(n, flux, p))

# ---------- Smith normal form over Z (own implementation) ----------
def snf_divisors(M):
    """Nonzero elementary divisors of integer matrix M (list)."""
    A = [row[:] for row in M]
    if not A or not A[0]:
        return []
    rows, cols = len(A), len(A[0])
    divs = []
    top = 0
    left = 0
    while top < rows and left < cols:
        # find smallest nonzero pivot in submatrix
        best = None
        for i in range(top, rows):
            for j in range(left, cols):
                v = A[i][j]
                if v and (best is None or abs(v) < abs(A[best[0]][best[1]])):
                    best = (i, j)
        if best is None:
            break
        bi, bj = best
        A[top], A[bi] = A[bi], A[top]
        for row in A:
            row[left], row[bj] = row[bj], row[left]
        while True:
            # clear column
            again = False
            for i in range(top + 1, rows):
                if A[i][left]:
                    q = A[i][left] // A[top][left]
                    if q:
                        A[i] = [a - q * b for a, b in zip(A[i], A[top])]
                    if A[i][left]:
                        A[top], A[i] = A[i], A[top]
                        again = True
            # clear row
            for j in range(left + 1, cols):
                if A[top][j]:
                    q = A[top][j] // A[top][left]
                    if q:
                        for i in range(top, rows):
                            A[i][j] -= q * A[i][left]
                    if A[top][j]:
                        for i in range(top, rows):
                            A[i][left], A[i][j] = A[i][j], A[i][left]
                        again = True
            if not again:
                col_clear = all(A[i][left] == 0 for i in range(top + 1, rows))
                row_clear = all(A[top][j] == 0 for j in range(left + 1, cols))
                if col_clear and row_clear:
                    break
        divs.append(abs(A[top][left]))
        top += 1
        left += 1
    # enforce divisibility chain
    changed = True
    while changed:
        changed = False
        for i in range(len(divs) - 1):
            a, b = divs[i], divs[i + 1]
            if b % a:
                from math import gcd
                g = gcd(a, b)
                divs[i], divs[i + 1] = g, a * b // g
                changed = True
    return divs

def integral_invariants(n, flux):
    """Per-degree free rank and torsion elementary divisors of H^k."""
    mats = [dH_matrix(n, flux, k) for k in range(n - 2)]
    snfs = [snf_divisors(M) for M in mats]
    out = []
    for k in range(n + 1):
        rk_in = len(snfs[k - 3]) if k >= 3 else 0     # rank of d into degree k
        rk_out = len(snfs[k]) if k <= n - 3 else 0
        free = comb(n, k) - rk_in - rk_out
        tors = [d for d in (snfs[k - 3] if k >= 3 else []) if d > 1]
        out.append((free, tors))
    return out

# ---------- targets ----------
def g_profile(n):
    prof = [0] * (n + 1)
    if n % 2 == 0:
        m = n // 2
        v = 3 ** (m - 1)
        prof[m - 1], prof[m], prof[m + 1] = v, 2 * v, v
    elif n % 4 == 3:
        m = (n - 1) // 2
        prof[m] = prof[m + 1] = 3 ** m
    else:
        m = (n - 1) // 2
        outer = 3 if n == 9 else 1
        prof[m - 1], prof[m], prof[m + 1], prof[m + 2] = outer, 3 ** m, 3 ** m, outer
    return tuple(prof)

def F_n(n):
    return comb(n + 1, (n + 1) // 2) if n % 2 else 2 * comb(n, n // 2)

def P_n(n):
    if n % 2:
        return 2 ** (n - 1) + 2 ** ((n - 1) // 2)
    return 2 * (2 ** (n - 2) + 2 ** ((n - 2) // 2))

def complete_flux(n):
    return {t: 1 for t in combinations(range(n), 3)}

# ---------- checks ----------
def check_d_squared():
    rng = random.Random(7)
    for n in (6, 8):
        flux = {t: rng.choice((-2, -1, 1, 3)) for t in combinations(range(n), 3)}
        for k in range(n - 5):
            A = dH_matrix(n, flux, k + 3)
            B = dH_matrix(n, flux, k)
            prod = [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))]
                    for i in range(len(A))]
            assert all(all(x == 0 for x in row) for row in prod), (n, k)
    print("d_H^2 = 0: OK (n=6,8 random integer flux)")

def profile_from_ranks(n, ranks):
    prof = []
    for k in range(n + 1):
        b = comb(n, k)
        if k >= 3:
            b -= ranks[k - 3]
        if k <= n - 3:
            b -= ranks[k]
        prof.append(b)
    return tuple(prof)

def check_C6_C7_complete(max_n=13, snf_max=9):
    print("== C6/C7 complete flux (matrices built once per n) ==")
    for n in range(4, max_n + 1):
        f = complete_flux(n)
        mats = [dH_matrix(n, f, k) for k in range(n - 2)]
        def tot_p(p):
            return sum(profile_from_ranks(n, [rank_mod_p(M, p) for M in mats]))
        b2 = tot_p(2)
        bq = [tot_p(p) for p in PRIMES[:2]]
        ok2 = b2 == P_n(n)
        okq = all(x == F_n(n) for x in bq)
        line = f"n={n:2d}  B(F2)={b2} (P_n={P_n(n)}) {'OK' if ok2 else 'FAIL'}   B(Q-proxy)={bq[0]} (F_n={F_n(n)}) {'OK' if okq else 'FAIL'}"
        # odd prime scan
        res = []
        for p in (3, 5, 7):
            bp = tot_p(p)
            if bp != F_n(n):
                res.append((p, bp - F_n(n)))
        line += f"  odd-prime excesses: {res if res else 'none'}"
        print(line)
    for n in range(4, snf_max + 1):
        inv = integral_invariants(n, complete_flux(n))
        tors = [d for _, t in inv for d in t]
        t2 = sum(1 for d in tors if d % 2 == 0)
        elem = all(d == 2 for d in tors)
        pred = (P_n(n) - F_n(n)) // 2
        freetot = sum(fr for fr, _ in inv)
        print(f"SNF n={n}: free total={freetot} (F_n={F_n(n)}) t2={t2} (pred {pred}) "
              f"all divisors=2: {elem} {'OK' if t2 == pred and freetot == F_n(n) else 'FAIL'}")

def check_C1_dense(trials_per_n=8):
    print("== C1 dense sign flux ==")
    rng = random.Random(20260812)
    hits = tot = 0
    for n in range(3, 12):
        for _ in range(trials_per_n):
            flux = {t: rng.choice((-1, 1)) for t in combinations(range(n), 3)}
            prof = betti(n, flux, PRIMES[0])
            tot += 1
            hits += prof == g_profile(n)
    print(f"dense +-1 trials: {hits}/{tot} hit g_n")

WITNESSES = {
 3: {(0,1,2): 1},
 4: {(0,1,2): 1},
 5: {(0,2,4): -1, (1,2,3): -1},
 6: {(0,3,4): 1, (1,2,5): -1},
 7: {(0,2,4): -1, (0,3,6): -1, (1,2,5): 1, (1,4,6): -1, (3,4,5): 1},
 8: {(0,2,3): -1, (0,5,7): 1, (1,3,6): 1, (2,4,7): -1, (4,5,6): 1},
 9: {(0,1,7): -1, (0,2,6): 1, (0,3,5): 1, (1,2,5): 1, (1,6,8): 1, (2,3,4): 1, (4,6,8): -1, (5,7,8): -1},
}

def check_C3_witnesses(_unused=None):
    print("== C3 witnesses (embedded from the deposited bundle) ==")
    from collections import Counter
    for n, flux in WITNESSES.items():
        prof = betti(n, flux, PRIMES[1])
        ok = prof == g_profile(n)
        pc = Counter(p for t in flux for p in combinations(t, 2))
        print(f"n={n}: support {len(flux)}, saturates {'OK' if ok else 'FAIL'}, "
              f"linear={max(pc.values()) <= 1}")

def check_C3_minimality():
    print("== C3 minimality (exhaustive n=5,6; claimed mu=2,2) ==")
    for n in (5, 6):
        found1 = False
        for t in combinations(range(n), 3):
            prof = betti(n, {t: 1}, PRIMES[0])
            if prof == g_profile(n):
                found1 = True
        print(f"n={n}: single-triple saturation possible: {found1} (claim: needs 2)")

def check_C8_snf_trials(trials=8):
    print("== C8 random sign-flux torsion counts ==")
    rng = random.Random(99)
    for _ in range(trials):
        n = rng.randint(5, 8)
        flux = {t: rng.choice((-1, 1)) for t in combinations(range(n), 3)}
        prof = betti(n, flux, PRIMES[0])
        if prof != g_profile(n):
            print(f"n={n}: profile off-generic, skipped")
            continue
        inv = integral_invariants(n, flux)
        tors = [d for _, t in inv for d in t]
        t2 = sum(1 for d in tors if d % 2 == 0)
        pred = (P_n(n) - sum(g_profile(n))) // 2
        odd = [d for d in tors if d % 2]
        print(f"n={n}: t2={t2} pred={pred} {'OK' if t2 == pred else 'FAIL'}"
              f"  divisors={sorted(set(tors))} odd-torsion={odd if odd else 'none'}")

def check_C2_sparse():
    print("== C2 sparse threshold (qualitative) ==")
    from math import log
    rng = random.Random(4242)
    for c in (1, 4, 10):
        hits = tot = 0
        for n in (8, 9, 10):
            p_edge = min(1.0, c * log(n) / n**2)
            for _ in range(12):
                flux = {t: rng.choice((-1, 1)) for t in combinations(range(n), 3)
                        if rng.random() < p_edge}
                prof = betti(n, flux, PRIMES[0])
                tot += 1
                hits += prof == g_profile(n)
        print(f"c={c}: hit rate {hits}/{tot}")


# ========================== CICY programme ==========================

import sys, json, time
from fractions import Fraction as Fr
from functools import lru_cache
from itertools import combinations
from math import comb, factorial, gcd, prod

def bernoulli_plus(m):
    """B_0..B_m with B_1=+1/2, via the defining recursion of x/(1-e^-x)."""
    B = [Fr(1)]
    for k in range(1, m + 1):
        # sum_{j=0}^{k} C(k+1,j) B_j^- = 0 with B^- convention; use B^+ = (-1)^k B^-
        s = Fr(0)
        for j in range(k):
            s += Fr(comb(k + 1, j)) * B[j] * (-1) ** (k - j)
        B.append(s / (k + 1) * (-1) ** (k + 1) if False else -s / (k + 1) * (-1) ** k)
    # safer: build from zeta-free recursion below instead
    return B

def bernoulli_series(order):
    """Coefficients c_k with x/(1-e^{-x}) = sum c_k x^k, exact."""
    # 1 - e^{-x} = sum_{k>=1} (-1)^{k+1} x^k / k!; divide x by it.
    den = [Fr((-1) ** (k + 1), factorial(k)) for k in range(1, order + 2)]
    c = [Fr(0)] * (order + 1)
    c[0] = 1 / den[0]
    for k in range(1, order + 1):
        c[k] = -sum(den[i] * c[k - i] for i in range(1, k + 1)) / den[0]
    return c

def mul(a, b, order):
    out = [Fr(0)] * (order + 1)
    for i, ai in enumerate(a[: order + 1]):
        if ai:
            for j, bj in enumerate(b[: order + 1 - i]):
                if bj:
                    out[i + j] += ai * bj
    return out

def inv(a, order):
    out = [Fr(0)] * (order + 1)
    out[0] = 1 / a[0]
    for k in range(1, order + 1):
        out[k] = -sum(a[i] * out[k - i] for i in range(1, k + 1)) * out[0]
    return out

def powser(a, e, order):
    out = [Fr(1)] + [Fr(0)] * order
    b = list(a[: order + 1])
    while e:
        if e & 1:
            out = mul(out, b, order)
        e >>= 1
        if e:
            b = mul(b, b, order)
    return out

@lru_cache(maxsize=None)
def Qxy_at(y, order):
    """Series of Q(x;y) at rational y: sum_k c_k (1+y)^k x^k - x y."""
    c = bernoulli_series(order)
    yy = Fr(y)
    q = [c[k] * (1 + yy) ** k for k in range(order + 1)]
    if order >= 1:
        q[1] -= yy
    return tuple(q)

@lru_cache(maxsize=None)
def genus_at(n, degrees, y):
    N = n + len(degrees)
    Q = list(Qxy_at(y, N))
    ser = powser(Q, N + 1, N)
    for d in degrees:
        Qd = [Q[k] * Fr(d) ** k for k in range(N + 1)]  # Q(d x)
        ser = mul(ser, inv(Qd, N), N)
        # multiply by d*x: shift by one, scale by d
        ser = [Fr(0)] + [Fr(d) * v for v in ser[:N]]
    return ser[N]

@lru_cache(maxsize=None)
def chi_y_coeffs(n, degrees):
    """(chi^0,...,chi^n) by evaluation at y=0..n + my own Newton interpolation."""
    ys = list(range(n + 1))
    vals = [genus_at(n, degrees, y) for y in ys]
    # Newton forward differences on integer nodes
    diffs = []
    row = vals[:]
    while row:
        diffs.append(row[0])
        row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    coeffs = [Fr(0)] * (n + 1)
    basis = [Fr(1)]  # falling factorial y(y-1)...(y-k+1) in monomial coeffs
    for k, dk in enumerate(diffs):
        if k:
            new = [Fr(0)] * (len(basis) + 1)
            for i, b in enumerate(basis):
                new[i + 1] += b
                new[i] += b * Fr(-(k - 1))
            basis = new
        w = dk / factorial(k)
        for i, b in enumerate(basis):
            coeffs[i] += w * b
    assert all(c.denominator == 1 for c in coeffs), (n, degrees)
    return tuple(int(c) for c in coeffs)

def a_coeffs(n, degrees):
    ch = chi_y_coeffs(n, degrees)
    return tuple((-1) ** (n - p) * ch[p] for p in range(n + 1))

@lru_cache(maxsize=None)
def S_signature(n, degrees):
    """S = (-1)^{n/2} sigma with sigma = chi_{y=1}."""
    v = genus_at(n, degrees, 1)
    assert v.denominator == 1
    return (-1) ** (n // 2) * int(v)

def configs(n):
    """All CY multidegrees (sorted tuples, d_i>=2) for complex dimension n."""
    out = []
    def rec(remaining, minpart, acc):
        if remaining == 0:
            out.append(tuple(acc))
            return
        for d in range(minpart, remaining + 1):
            # parts d>=2 with sum = n+r+1 <=> (d_i - 1) partition n+1
            rec(remaining - d, d, acc + [d])
    # sum (d_i - 1) = n + 1
    def rec2(remaining, minpart, acc):
        if remaining == 0:
            out.append(tuple(v + 1 for v in acc))
            return
        for d in range(minpart, remaining + 1):
            rec2(remaining - d, d, acc + [d])
    rec2(n + 1, 1, [])
    return out

def merges_of(d):
    seen = set()
    for i, j in combinations(range(len(d)), 2):
        m = tuple(sorted([v for k, v in enumerate(d) if k not in (i, j)] + [d[i] + d[j] - 1]))
        seen.add((m, d[i], d[j]))
    return seen

# ---------------- checks ----------------
def calibrations():
    a_k3 = a_coeffs(2, (4,))
    assert a_k3 == (2, 20, 2), a_k3
    a5 = a_coeffs(3, (5,))
    assert a5 == (0, 100, 100, 0), a5
    assert S_signature(2, (4,)) == 16
    assert S_signature(2, (2, 2, 2)) == 16
    assert S_signature(2, (2, 3)) == 16
    # Euler char cross-check: chi = sum (-1)^p chi^p at y=-1 equals classical
    ch = chi_y_coeffs(3, (5,))
    euler = sum((-1) ** p * c for p, c in enumerate(ch))
    assert euler == -200, euler
    print("calibrations OK: K3 (2,20,2) S=16 all three dim-2 configs; quintic (0,100,100,0), chi=-200")

def check_chi_y(nmax=14):
    print(f"== C9-C15 chi_y programme through n={nmax} ==")
    t9 = t10 = t11 = t13 = 0
    v9 = v10 = v11 = v13 = 0
    nconf = 0
    for n in range(2, nmax + 1):
        cfgs = configs(n)
        nconf += len(cfgs)
        A = {c: a_coeffs(n, c) for c in cfgs}
        D = {c: prod(c) for c in cfgs}
        Q = tuple([2] * (n + 1)); Y = (n + 2,)
        for c in cfgs:
            for p in range(1, n):
                t9 += 2
                if not (A[Q][p] <= A[c][p] <= A[Y][p]):
                    v9 += 1
                    print(f"C9 VIOLATION n={n} {c} p={p}")
            # C13 ultra-log-concavity on positive triples
            for p in range(1, n):
                x0, x1, x2 = A[c][p - 1], A[c][p], A[c][p + 1]
                if x0 > 0 and x1 > 0 and x2 > 0:
                    t13 += 1
                    lhs = Fr(x1, comb(n, p)) ** 2
                    rhs = Fr(x0, comb(n, p - 1)) * Fr(x2, comb(n, p + 1))
                    if not lhs > rhs:
                        v13 += 1
                        print(f"C13 VIOLATION n={n} {c} p={p}")
            for m, di, dj in merges_of(c):
                for p in range(1, n):
                    t10 += 1
                    if not Fr(A[m][p], D[m]) > Fr(A[c][p], D[c]):
                        v10 += 1
                        print(f"C10 VIOLATION n={n} {c}->{m} p={p}")
                if n >= 3 and max(di, dj) == max(c):
                    for p in range(1, n):
                        t11 += 1
                        if not A[m][p] > A[c][p]:
                            v11 += 1
                            print(f"C11 VIOLATION n={n} {c}->{m} p={p}")
        print(f"  n={n}: {len(cfgs)} configs done", flush=True)
    print(f"configs total {nconf}; C9 {t9} comps {v9} viol; C10 {t10}/{v10}; C11 {t11}/{v11}; C13 {t13}/{v13}")

def check_roots(nmax=12):
    import numpy as np
    print(f"== C12/C14/C15 numerical root programme through n={nmax} ==")
    bad12 = bad14 = bad15 = 0; t12 = t14 = t15 = 0
    for n in range(2, nmax + 1):
        cfgs = configs(n)
        A = {c: a_coeffs(n, c) for c in cfgs}
        D = {c: prod(c) for c in cfgs}
        def reduced(c):
            a = list(A[c])
            if n % 2 == 1:
                assert a[0] == 0 and a[-1] == 0
                a = a[1:-1] if a[-1] == 0 else a[1:]
                # strip single forced factor y: a_0=0 for odd n
            while a and a[-1] == 0:
                a.pop()
            return a
        def roots(c):
            a = reduced(c)
            return np.roots(np.array(a[::-1], dtype=float) / max(map(abs, a)))
        def mahler(c):
            a = reduced(c)
            r = roots(c)
            return abs(a[-1]) * np.prod(np.maximum(1.0, np.abs(r)))
        for c in cfgs:
            r = roots(c)
            t12 += 1
            if np.max(np.abs(r.imag)) > 1e-6 * (1 + np.max(np.abs(r))) or np.max(r.real) > -1e-12:
                bad12 += 1
                print(f"C12 VIOLATION n={n} {c}: roots {sorted(r)[:4]}...")
            for m, di, dj in merges_of(c):
                t14 += 1
                if not mahler(m) / D[m] > mahler(c) / D[c]:
                    bad14 += 1
                    print(f"C14 VIOLATION n={n} {c}->{m}")
                if max(di, dj) == max(c):
                    t15 += 1
                    rho_m, rho_c = np.max(np.abs(roots(m))), np.max(np.abs(roots(c)))
                    strict_dims = n not in (2, 3, 5)
                    if strict_dims and not rho_m > rho_c * (1 + 1e-9):
                        bad15 += 1
                        print(f"C15 strictness VIOLATION n={n} {c}->{m}: {rho_c} -> {rho_m}")
                    if not strict_dims and abs(rho_m - rho_c) > 1e-6 * rho_c:
                        bad15 += 1
                        print(f"C15 equality VIOLATION n={n} {c}->{m}: {rho_c} -> {rho_m}")
        print(f"  n={n} done", flush=True)
    print(f"C12 {t12}/{bad12}; C14 {t14}/{bad14}; C15 {t15}/{bad15}")

def check_signature(nmax=26):
    print(f"== C16-C18, C20 signature programme through n={nmax} ==")
    t16 = v16 = t17 = v17 = t18 = v18 = 0
    nconf = 0
    for n in range(2, nmax + 1, 2):
        cfgs = configs(n)
        nconf += len(cfgs)
        S = {c: S_signature(n, c) for c in cfgs}
        D = {c: prod(c) for c in cfgs}
        Q = tuple([2] * (n + 1)); Y = (n + 2,)
        g = 0
        for c in cfgs:
            g = gcd(g, S[c])
            if n >= 4:
                t16 += 1
                inside = S[Q] <= S[c] <= S[Y]
                eqQ = S[c] == S[Q] and c != Q
                eqY = S[c] == S[Y] and c != Y
                if not inside or eqQ or eqY:
                    v16 += 1
                    print(f"C16 VIOLATION n={n} {c}")
            for m, di, dj in merges_of(c):
                t17 += 1
                if not Fr(S[m], D[m]) > Fr(S[c], D[c]):
                    v17 += 1
                    print(f"C17 VIOLATION n={n} {c}->{m}")
                if n >= 4 and max(di, dj) == max(c):
                    t18 += 1
                    if not S[m] > S[c]:
                        v18 += 1
                        print(f"C18 VIOLATION n={n} {c}->{m}")
        pred = 2 if n % 4 == 0 else 2 ** max(4, 1 + (((n + 2) & -(n + 2)).bit_length() - 1))
        ok = g == pred
        print(f"  n={n}: {len(cfgs)} cfgs, gcd={g} (pred {pred}) {'OK' if ok else 'FAIL C20'}", flush=True)
    print(f"configs {nconf}; C16 {t16}/{v16}; C17 {t17}/{v17}; C18 {t18}/{v18}")

def check_C19(nmax=60):
    print(f"== C19 all-quadric ratios through n={nmax} ==")
    prev = None
    prev_ratio = None
    rows = []
    for n in range(2, nmax + 1, 2):
        q = S_signature(n, tuple([2] * (n + 1)))
        if prev is not None:
            r = Fr(q, prev)
            mono = prev_ratio is None or r > prev_ratio
            below = r < 27
            rows.append((n, float(r), mono, below))
            prev_ratio = r
        prev = q
        print(f"  n={n}: S={q}" + (f" ratio={float(prev_ratio):.8f}" if prev_ratio else ""), flush=True)
    ok = all(m and b for _, _, m, b in rows)
    last_n, last_r, _, _ = rows[-1]
    print(f"C19: monotone+below-27 {'OK' if ok else 'FAIL'}; last ratio R_{last_n-2}={last_r:.8f}, gap={27-last_r:.8f}, 27/{last_n}={27/last_n:.8f}")


if __name__ == "__main__":
    import time
    t0 = time.time()
    check_d_squared()
    check_C6_C7_complete(max_n=12, snf_max=0)
    for n in range(4, 9):
        invs = integral_invariants(n, complete_flux(n))
        tors = [d for _, t in invs for d in t]
        t2 = sum(1 for d in tors if d % 2 == 0)
        pred = (P_n(n) - F_n(n)) // 2
        freetot = sum(fr for fr, _ in invs)
        print(f"SNF n={n}: free={freetot} (F_n={F_n(n)}) t2={t2} (pred {pred}) "
              f"elementary={all(d == 2 for d in tors)} {'OK' if t2 == pred and freetot == F_n(n) else 'FAIL'}")
    check_C1_dense(trials_per_n=4)
    check_C3_witnesses()
    check_C3_minimality()
    calibrations()
    check_chi_y(10)
    check_roots(9)
    check_signature(18)
    check_C19(40)
    print(f"all done in {time.time()-t0:.1f}s")
