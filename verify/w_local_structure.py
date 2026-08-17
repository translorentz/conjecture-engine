#!/usr/bin/env python3
"""Part VI (Conjectures 97-116) independent reproduction, from scratch.

Reproduces the four proved propositions and a representative finite sample of the twenty
conjectures, with implementations sharing no code with the deposited scans.  Ranges are kept
modest so the script runs in seconds.  The deposited evidence reaches much further.
"""
from itertools import combinations, permutations
from collections import defaultdict
from fractions import Fraction as Fr
from math import comb, log, isqrt
import numpy as np


def omega(n, spf):
    c = 0
    while n > 1:
        p = spf[n]
        while n % p == 0:
            n //= p
            c += 1
    return c


def sieves(N):
    spf = np.zeros(N + 1, dtype=np.int64)
    for p in range(2, N + 1):
        if spf[p] == 0:
            spf[p::p][spf[p::p] == 0] = p
    return spf


def main():
    # ---- Proposition w:jump: exact factorial-ratio jump identities ----
    spf_small = sieves(200000)
    Om = lambda n: omega(int(n), spf_small)

    def omega_binom(k, n):
        # Omega(C(kn,n)) by Legendre; every prime factor is <= kn, no huge factorization
        top = k * n
        total = 0
        for p in range(2, top + 1):
            if spf_small[p] != p:
                continue
            pk = p
            while pk <= top:
                total += top // pk - n // pk - (k - 1) * n // pk
                pk *= p
        return total

    for k in range(2, 9):
        for n in range(1, 60):
            J = omega_binom(k, n + 1) - omega_binom(k, n)
            rhs = sum(Om(k * n + j) for j in range(1, k + 1)) - Om(n + 1) \
                - sum(Om((k - 1) * n + j) for j in range(1, k))
            assert J == rhs, (k, n, J, rhs)
    # central-binomial specialization
    for n in range(1, 60):
        assert omega_binom(2, n + 1) - omega_binom(2, n) == 1 + Om(2 * n + 1) - Om(n + 1)
    print("Prop w:jump: factorial-ratio jump identities exact (k<=8, n<60)")

    # ---- Proposition w:k2slope: finite exact regression for its jump formula ----
    k2_values = []
    for m in range(2, 17):
        n = 2 ** m - 1
        direct = omega_binom(2, n + 1) - omega_binom(2, n)
        formula = 1 - m + Om(2 ** (m + 1) - 1)
        assert direct == formula, (m, direct, formula)
        k2_values.append(direct)
    print(f"Prop w:k2slope: exact dyadic jump formula checked for 2<=m<=16, last jump {k2_values[-1]}")

    # ---- radical ratio R(n)=rad(n)/n; window order patterns ----
    # Pattern densities are conditional on no ties (delta_pi normalized among untied
    # windows, as in the paper's definitions): ties have positive density (adjacent
    # squarefree pairs already tie at R=1), so the chi-square below uses the strict
    # window count as its total, which is exactly the conditional normalization.
    N = 1_000_000
    rad = np.ones(N + 1, dtype=np.float64)
    isc = np.zeros(N + 1, dtype=bool)
    for p in range(2, N + 1):
        if not isc[p]:
            if p * p <= N:
                isc[p * p::p] = True
            rad[p::p] *= p
    R = np.zeros(N + 1)
    R[1:] = rad[1:] / np.arange(1, N + 1)

    def rankword_chi(d):
        cnt = defaultdict(int)
        for n in range(1, N - d + 1):
            w = R[n:n + d]
            if len(set(w.tolist())) < d:
                continue
            cnt[tuple(int(x) for x in np.argsort(w))] += 1
        tot = sum(cnt.values())
        k = 1
        for i in range(1, d + 1):
            k *= i
        exp = tot / k
        chi = sum((v - exp) ** 2 / exp for v in cnt.values()) + (k - len(cnt)) * exp
        return chi, cnt, tot

    for d in (3, 4):
        chi, _, _ = rankword_chi(d)
        assert chi < 30, (d, chi)          # Prop w:radunif: uniform through length 4
    chi5, cnt5, _ = rankword_chi(5)
    assert chi5 > 1000                     # C103: nonuniform at length 5
    ratio = cnt5[tuple(int(c) for c in "30241")] / cnt5[tuple(int(c) for c in "13240")]
    assert ratio > 12                      # C104: dominant/suppressed word ratio
    print(f"Prop w:radunif + C103/104: uniform d<=4, chi5={chi5:.0f}, word ratio={ratio:.2f}")

    # ---- abundancy / totient monotone-triple densities and totient barrier ----
    M = 2_000_000
    sigma = np.zeros(M + 1, dtype=np.int64)
    for d in range(1, M + 1):
        sigma[d::d] += d
    phi = np.arange(M + 1, dtype=np.int64)
    for p in range(2, M + 1):
        if phi[p] == p:
            phi[p::p] -= phi[p::p] // p
    ab = sigma[1:] / np.arange(1, M + 1)
    to = phi[1:] / np.arange(1, M + 1)

    def mono_density(a):
        x, y, z = a[:-2], a[1:-1], a[2:]
        strict = (x != y) & (y != z) & (x != z)
        mono = ((x < y) & (y < z)) | ((x > y) & (y > z))
        return mono.sum() / strict.sum()

    dab, dto = mono_density(ab), mono_density(to)
    assert 0.094 < dab < 0.098 and 0.019 < dto < 0.022      # C105, C106
    # C107 (resolved false): the proposed five-term totient barrier is refuted in general
    # by Martin's simultaneous-inequality theorem, which yields strictly monotone runs of
    # phi(n)/n of every length on positive lower density.  The runs are astronomically rare
    # (none below 4e9), so within this modest range the empirical maximum run is still <= 4;
    # we record that finite fact, not the (false) universal barrier.
    best_i = best_d = 1
    ci = cd = 1
    for i in range(1, len(to)):
        ci = ci + 1 if to[i] > to[i - 1] else 1
        cd = cd + 1 if to[i] < to[i - 1] else 1
        best_i = max(best_i, ci)
        best_d = max(best_d, cd)
    assert best_i <= 4 and best_d <= 4
    print(f"C105/106: densities {dab:.4f}, {dto:.4f}; C107: max totient run {max(best_i, best_d)}")

    # ---- C110/111: two-sided binomial-slice shocks (signs of extremes) ----
    for k in (3, 5):
        js = []
        for n in range(1, 4000):
            J = (sum(Om(k * n + j) for j in range(1, k + 1)) - Om(n + 1)
                 - sum(Om((k - 1) * n + j) for j in range(1, k)))
            js.append(J)
        assert min(js) < -6 and max(js) > 6                 # unbounded both sides (indicative)
    print("C110/111: binomial-slice jumps range widely both signs")

    # ---- C116: prime-gap boundary means, mod-6 sign pattern ----
    P = 3_000_000
    Omv = np.zeros(P + 3, dtype=np.int32)
    sc = np.zeros(P + 3, dtype=bool)
    for p in range(2, P + 3):
        if not sc[p]:
            if p * p < P + 3:
                sc[p * p::p] = True
            pk = p
            while pk < P + 3:
                Omv[pk::pk] += 1
                if pk > (P + 3) // p:
                    break
                pk *= p
    isp = np.ones(P + 1, dtype=bool)
    isp[:2] = False
    for p in range(2, isqrt(P) + 1):
        if isp[p]:
            isp[p * p::p] = False
    pr = np.nonzero(isp)[0]
    sums = defaultdict(float)
    cnts = defaultdict(int)
    for i in range(1, len(pr) - 1):
        p, q = int(pr[i]), int(pr[i + 1])
        if q + 1 > P:
            break
        g = q - p
        sums[g] += Omv[p + 1] + Omv[q - 1] - Omv[p - 1] - Omv[q + 1]
        cnts[g] += 1
    m2, m4, m6 = sums[2] / cnts[2], sums[4] / cnts[4], sums[6] / cnts[6]
    assert m2 > 1 and m4 < -1 and abs(m6) < 0.6            # gap=2 up, gap=4 down, 6|gap ~0
    print(f"C116: boundary means gap2={m2:+.2f} gap4={m4:+.2f} gap6={m6:+.2f} (mod-6 wave)")

    print("Part VI representative checks passed")


if __name__ == "__main__":
    main()
