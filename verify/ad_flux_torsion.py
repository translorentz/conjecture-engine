#!/usr/bin/env python3
"""Independent verification of C3 (torsion shape) and C4 (post-onset persistence).

t_{p,k}(n) = number of p-primary cyclic summands of H^k(Lambda^* Z^n, H_Delta ^ -)
           = rank_Q(D_{k-3}) - rank_{F_p}(D_{k-3}),
where D_j : Lambda^j -> Lambda^{j+3} is wedge with the complete 3-form.
Own code; nothing shared with the bundle.
"""
import itertools, sys
from math import comb

def wedge_matrix(n, k):
    """Matrix of H_Delta ^ - : Lambda^k -> Lambda^{k+3} over Z (rows: (k+3)-sets)."""
    rows = list(itertools.combinations(range(n), k+3))
    cols = list(itertools.combinations(range(n), k))
    ridx = {S: i for i, S in enumerate(rows)}
    M = [[0]*len(cols) for _ in rows]
    for j, S in enumerate(cols):
        Sset = set(S)
        rest = [x for x in range(n) if x not in Sset]
        for T in itertools.combinations(rest, 3):
            # sign of merging sorted T into sorted S: sign of permutation sorting T+S
            merged = sorted(T + S)
            # count inversions: for e_T ^ e_S with T,S sorted ascending
            sgn = 1
            seq = list(T) + list(S)
            inv = sum(1 for a in range(len(seq)) for b in range(a+1, len(seq)) if seq[a] > seq[b])
            sgn = -1 if inv % 2 else 1
            M[ridx[tuple(merged)]][j] += sgn
    return M

def rank_mod(M, p):
    """Gaussian elimination rank over F_p (p large prime approximates Q-rank)."""
    A = [row[:] for row in M]
    if not A or not A[0]: return 0
    R, C = len(A), len(A[0])
    for i in range(R):
        for j in range(C):
            A[i][j] %= p
    r = 0
    for c in range(C):
        piv = next((i for i in range(r, R) if A[i][c]), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], p-2, p)
        A[r] = [(x*inv) % p for x in A[r]]
        for i in range(R):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][j] - f*A[r][j]) % p for j in range(C)]
        r += 1
        if r == R: break
    return r

BIGP = 1_000_000_007

def torsion_profile(n, p):
    """t_{p,k}(n) for k = 3..n (torsion in H^k comes from D_{k-3})."""
    prof = {}
    for k3 in range(0, n-2):
        M = wedge_matrix(n, k3)
        rq = rank_mod(M, BIGP)
        rp = rank_mod(M, p)
        t = rq - rp
        if t: prof[k3+3] = t
    return prof

def main(nmax=12):
    print("torsion profiles t_{p,k}(n) (only nonzero):")
    T = {}
    for n in range(5, nmax+1):
        for p in (2, 3, 5):
            prof = torsion_profile(n, p)
            T[(n, p)] = sum(prof.values())
            if prof:
                ks = sorted(prof)
                vals = [prof[k] for k in ks]
                # C3 checks
                interval = ks == list(range(ks[0], ks[-1]+1))
                dual = all(prof.get(k, 0) == prof.get(n+3-k, 0) for k in range(0, n+4))
                slc = all(vals[i]**2 > vals[i-1]*vals[i+1] for i in range(1, len(vals)-1))
                print(f"  n={n} p={p}: k={ks[0]}..{ks[-1]} t={vals}  T={sum(vals)}"
                      f"  interval={interval} duality={dual} strictLC={slc}")
                assert interval and dual and slc, (n, p)
    # C4: persistence
    print("C4 persistence T_p(n+1) > T_p(n) after onset:")
    for p in (2, 3):
        onset = 4*p - 1
        seq = [(n, T.get((n, p), 0)) for n in range(5, nmax+1)]
        print(f"  p={p}: T = {seq}")
        for n in range(onset, nmax):
            if (n, p) in T and (n+1, p) in T:
                assert T[(n+1, p)] > T[(n, p)], (p, n)
        # onset check: zero before 4p-1, one at 4p-1
        for n in range(5, min(onset, nmax+1)):
            assert T.get((n, p), 0) == 0, (p, n)
        if (onset, p) in T:
            assert T[(onset, p)] == 1, p
    print("C3+C4 verified on the computed range")
    # closed-form T_2 check and long-range monotonicity of (P_n - F_n)/2
    def F(n): return comb(n+1, (n+1)//2) if n % 2 else 2*comb(n, n//2)
    def P(n): return 2**(n-1) + 2**((n-1)//2) if n % 2 else 2*(2**(n-2) + 2**((n-2)//2))
    t2 = {n: (P(n)-F(n))//2 for n in range(3, 201)}
    print("  T_2 from closed forms (n=7..12):", [t2[n] for n in range(7, 13)])
    assert all(t2[n+1] > t2[n] for n in range(7, 200))
    print("  closed-form T_2 strictly increasing for 7 <= n <= 200: OK")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 12)
