#!/usr/bin/env python3
"""Conjectures 87 and 90 resolution: verify the two refuting seven-point posets, and
correct the Conjecture 82 illustration of the unitriangular centroid dimension.

Independent of any deposited or externally supplied code: the pattern Lie algebras,
their rank enumerators, centres, and centroids are built from scratch in v_poset_core.

Conjecture 87 (Kirillov likelihood-ratio field monotonicity) asserts that the
normalized even-rank Kirillov distribution over the larger field dominates the smaller
in monotone likelihood-ratio order. The seven-point poset P87 below already refutes it
at q=2 versus q'=3: the ratio of even-rank counts K_3/K_2 rises then falls.

Conjecture 90 (Centre-one quotient shape) asserts that, for a line centre, the incidence
quotient R has interval support and is unimodal. The seven-point poset P90 has a line
centre and an R that is nonnegative with interval support but carries a strict interior
valley, so unimodality fails while positivity and interval support survive.

Conjecture 82 states that the adjoint enumerator determines dim Cent(L_P); that claim is
untouched. Only its illustrative sentence about the chain is corrected here: the centroid
of ut_n has dimension n, not one.
"""
import v_poset_core as V


def closure(n, covers):
    rel = set(covers)
    changed = True
    while changed:
        changed = False
        for (a, b) in list(rel):
            for (c, d) in list(rel):
                if b == c and (a, d) not in rel:
                    rel.add((a, d))
                    changed = True
    return rel


def build(n, covers):
    rel = closure(n, covers)
    return V.build_algebra(n, rel)


def quotient_R(A, K, q):
    """R = (K - A) / ((1 - T)(1 - qT)) by synthetic division; assert exact."""
    deg = max(len(A), len(K)) - 1
    num = [(K[i] if i < len(K) else 0) - (A[i] if i < len(A) else 0) for i in range(deg + 1)]
    out, r1, r2 = [], 0, 0
    for i, val in enumerate(num):
        cur = val + (1 + q) * r1 - q * r2
        if i <= deg - 2:
            out.append(cur)
        else:
            assert cur == 0, "division not exact"
        r2, r1 = r1, cur
    while out and out[-1] == 0:
        out.pop()
    return out


def main():
    # ---- Conjecture 87 ----
    P87 = [(0, 1), (1, 2), (1, 3), (0, 4), (4, 6), (0, 5), (5, 6)]  # 0-indexed covers
    _, m, _, adB, kir = build(7, P87)
    assert m == 10
    ev = {}
    for q in (2, 3):
        A, K = V.enumerators(m, adB, kir, q)
        ev[q] = [K[r] for r in range(0, m + 1, 2) if r < len(K)]
    # nonzero even ranks are 0,2,4,6
    K2 = [c for c in ev[2] if c]
    K3 = [c for c in ev[3] if c]
    assert K2 == [128, 384, 128, 384], K2
    assert K3 == [2187, 17496, 4374, 34992], K3
    ratios = [b / a for a, b in zip(K2, K3)]
    # monotone likelihood ratio requires ratios nondecreasing; it dips at rank 4
    assert ratios[1] > ratios[2], ratios
    assert not all(ratios[i] <= ratios[i + 1] for i in range(len(ratios) - 1))
    print("C87 refuted: K_2 even =", K2, " K_3 even =", K3)
    print("           K_3/K_2 =", [round(r, 1) for r in ratios], "-> not monotone (dips at rank 4)")

    # ---- Conjecture 90 ----
    P90 = [(0, 1), (1, 2), (1, 3), (2, 5), (3, 4), (4, 5), (5, 6)]
    _, m, br, adB, kir = build(7, P90)
    assert m == 19
    assert V.center_dim(m, br, 2) == 1
    A, K = V.enumerators(m, adB, kir, 2)
    R = quotient_R(A, K, 2)
    assert all(c >= 0 for c in R), "positivity fails"
    nz = [i for i, c in enumerate(R) if c]
    assert nz == list(range(nz[0], nz[-1] + 1)), "support not an interval"
    # strict interior valley at degrees 8,9,10
    assert R[8] > R[9] < R[10] and R[8] < R[10], (R[8], R[9], R[10])
    unimodal = all(R[i] <= R[i + 1] for i in range(len(R) - 1)) or \
        any(all(R[i] <= R[i + 1] for i in range(k)) and
            all(R[i] >= R[i + 1] for i in range(k, len(R) - 1)) for k in range(len(R)))
    assert not unimodal, "sequence is unexpectedly unimodal"
    print("C90 refuted: line centre, R nonnegative with interval support but not unimodal")
    print("           R[8..10] =", R[8:11], "(strict interior valley)")

    # ---- Conjecture 82 illustration: dim Cent(ut_n) = n for n >= 3 ----
    # ut_2 is abelian and one-dimensional, so its centroid is the full gl_1, dimension 1;
    # for n >= 3 the centre is a proper subspace and dim Cent(ut_n) = n exactly.
    _, m, br, _, _ = build(2, [(0, 1)])
    assert V.centroid_dim(m, br, 2) == 1 and V.centroid_dim(m, br, 3) == 1
    for n in range(3, 8):
        _, m, br, _, _ = build(n, [(i, i + 1) for i in range(n - 1)])
        for q in (2, 3):
            d = V.centroid_dim(m, br, q)
            assert d == n, (n, q, d)
    print("C82 illustration corrected: dim Cent(ut_n) = n for n = 3..7 (ut_2 degenerate, dim 1)")


if __name__ == "__main__":
    main()
