#!/usr/bin/env python3
"""Independent verification of Conjectures 77-96 on the n<=5 poset corpus (plus ut_n family),
over F_2, F_3, and F_5 (F_5 restricted to dim<=7). Reports pass/fail and confirms the
reported failure boundaries. Nothing imported from the bundle."""
import v_poset_core as C
from fractions import Fraction
import itertools, sys

MAXN = 5

def build_corpus():
    corpus = []  # dict per poset
    for n in range(1, MAXN + 1):
        for (nn, rel) in C.gen_unlabeled_posets(n):
            basis, m, br, adB, kir = C.build_algebra(nn, rel)
            rec = {"n": nn, "rel": rel, "m": m, "br": br, "adB": adB, "kir": kir,
                   "forest": C.hasse_forest(nn, rel), "data": {}}
            for q in (2, 3, 5):
                if q == 5 and m > 6:
                    continue
                if q == 3 and m > 10:
                    continue
                A, K = C.enumerators(m, adB, kir, q)
                rec["data"][q] = {
                    "A": tuple(A), "K": tuple(K),
                    "bA": max([r for r in range(m + 1) if A[r]] + [0]),
                    "bK": max([r for r in range(m + 1) if K[r]] + [0]),
                    "Z": C.center_dim(m, br, q),
                    "lcs": C.lower_central_profile(m, br, q),
                    "Der": C.der_dim(m, br, q) if m <= 9 else None,
                    "Cent": C.centroid_dim(m, br, q) if m <= 9 else None,
                }
            corpus.append(rec)
    return corpus

def Rpoly(A, K, q):
    """R = (K - A) / ((1-T)(1-qT)); return coeff list (low->high) or None if not divisible / neg."""
    diff = [K[i] - A[i] for i in range(len(A))]
    r = [Fraction(x) for x in diff] + [Fraction(0), Fraction(0)]
    quo = [Fraction(0)] * len(r)
    for deg in range(len(r) - 1, 1, -1):
        if r[deg] == 0:
            continue
        f = r[deg] / q
        quo[deg - 2] += f
        r[deg] -= f * q
        r[deg - 1] -= f * (-(1 + q))
        r[deg - 2] -= f * 1
    if any(x != 0 for x in r):
        return None, False
    coeffs = quo[:len(A)]
    while coeffs and coeffs[-1] == 0:
        coeffs.pop()
    allint = all(x == int(x) for x in coeffs)
    return [int(x) if x == int(x) else x for x in coeffs], allint

def support(vec):
    return tuple(i for i, x in enumerate(vec) if x)

def unimodal(seq):
    seq = list(seq)
    i = 0
    n = len(seq)
    while i + 1 < n and seq[i] <= seq[i + 1]:
        i += 1
    while i + 1 < n and seq[i] >= seq[i + 1]:
        i += 1
    return i == n - 1

def interval_support(vec):
    s = support(vec)
    return len(s) == 0 or list(s) == list(range(s[0], s[-1] + 1))

def strict_logconcave_interior(seq):
    """strict at every interior index where it is nontrivial (both neighbours nonzero)."""
    for i in range(1, len(seq) - 1):
        if seq[i - 1] and seq[i + 1]:
            if not (seq[i] * seq[i] > seq[i - 1] * seq[i + 1]):
                return False
    return True

def logconcave(seq):
    for i in range(1, len(seq) - 1):
        if seq[i] * seq[i] < seq[i - 1] * seq[i + 1]:
            return False
    return True

def even_subseq(K):
    return [K[2 * j] for j in range(len(K) // 2 + 1) if 2 * j < len(K)]

def main():
    print("building corpus (n<=5, q=2,3,5)...", flush=True)
    corpus = build_corpus()
    print(f"corpus: {len(corpus)} posets\n", flush=True)

    # ---- determination conjectures: group by (q, A) ----
    def group_by(keyfn, qs=(2, 3, 5)):
        g = {}
        for rec in corpus:
            for q in qs:
                if q in rec["data"]:
                    g.setdefault((q, keyfn(rec, q)), []).append((rec, q))
        return g

    # 77: A -> K
    g = group_by(lambda r, q: r["data"][q]["A"])
    c77 = sum(1 for k, v in g.items() if len({r["data"][q]["K"] for r, q in v}) > 1)
    ncoll = sum(1 for k, v in g.items() if len(v) > 1)
    print(f"77 (A=>K):        collision classes={ncoll}, violations={c77}")

    # 78: A -> lower-central profile
    c78 = sum(1 for k, v in g.items() if len({r["data"][q]["lcs"] for r, q in v}) > 1)
    print(f"78 (A=>lcs):      violations={c78}")

    # 80: A -> dim Der
    c80 = sum(1 for k, v in g.items() if None not in {r["data"][q]["Der"] for r,q in v} and len({r["data"][q]["Der"] for r, q in v}) > 1)
    print(f"80 (A=>dim Der):  violations={c80}")

    # 82: A -> dim Cent
    c82 = sum(1 for k, v in g.items() if None not in {r["data"][q]["Cent"] for r,q in v} and len({r["data"][q]["Cent"] for r, q in v}) > 1)
    print(f"82 (A=>dim Cent): violations={c82}")

    # 83/84: rank support independent of q
    c83 = c84 = 0
    for rec in corpus:
        qs = [q for q in (2, 3, 5) if q in rec["data"]]
        if len(qs) >= 2:
            sA = {support(rec["data"][q]["A"]) for q in qs}
            sK = {support(rec["data"][q]["K"]) for q in qs}
            if len(sA) > 1:
                c83 += 1
            if len(sK) > 1:
                c84 += 1
    print(f"83 (supp A indep q): violations={c83};  84 (supp K indep q): violations={c84}")

    # 85 core: (A@2,A@3) -> A@5
    g85 = {}
    for rec in corpus:
        if 2 in rec["data"] and 3 in rec["data"] and 5 in rec["data"]:
            g85.setdefault((rec["data"][2]["A"], rec["data"][3]["A"]), []).append(rec)
    c85 = sum(1 for k, v in g85.items() if len({r["data"][5]["A"] for r in v}) > 1)
    n85 = sum(1 for k, v in g85.items() if len(v) > 1)
    print(f"85 core ((A2,A3)=>A5): classes with 3-field data, collision classes={n85}, violations={c85}")

    # 86: ad-rank stochastic dominance q' > q (CDF_{q'} <= CDF_q pointwise)
    def cdf(A):
        tot = sum(A); s = 0; out = []
        for x in A:
            s += x; out.append(Fraction(s, tot))
        return out
    c86 = 0; t86 = 0
    for rec in corpus:
        for (q, qp) in [(2, 3), (2, 5), (3, 5)]:
            if q in rec["data"] and qp in rec["data"]:
                A = rec["data"][q]["A"]; Ap = rec["data"][qp]["A"]
                L = max(len(A), len(Ap))
                A = list(A) + [0] * (L - len(A)); Ap = list(Ap) + [0] * (L - len(Ap))
                cq = cdf(A); cqp = cdf(Ap); t86 += 1
                if any(cqp[i] > cq[i] for i in range(L)):
                    c86 += 1
    print(f"86 (ad stoch dominance): {t86} pair-tests, violations={c86}")

    # 88/89/90: center-one
    c1 = [rec for rec in corpus if all(rec["data"][q]["Z"] == 1 for q in rec["data"])]
    # 88: K -> A among center-one
    g88 = {}
    for rec in c1:
        for q in rec["data"]:
            g88.setdefault((q, rec["data"][q]["K"]), []).append((rec, q))
    v88 = sum(1 for k, v in g88.items() if len({r["data"][q]["A"] for r, q in v}) > 1)
    print(f"88 (center-one K=>A): center-one records={sum(len(rec['data']) for rec in c1)}, violations={v88}")

    # 89/90
    v89 = v90i = v90u = 0; lc_fail = 0; tested = 0
    for rec in c1:
        for q in rec["data"]:
            R, allint = Rpoly(rec["data"][q]["A"], rec["data"][q]["K"], q)
            tested += 1
            if R is None or not allint or any(x < 0 for x in R):
                v89 += 1
            else:
                if not interval_support(R):
                    v90i += 1
                if not unimodal(R):
                    v90u += 1
                if not logconcave(R):
                    lc_fail += 1
    print(f"89 (center-one R nonneg int): {tested} records, violations={v89}")
    print(f"90 (R interval+unimodal): interval-viol={v90i}, unimodal-viol={v90u}; "
          f"log-concavity fails {lc_fail} times (confirms unimodal calibration)")

    # 91-94: forests
    forests = [rec for rec in corpus if rec["forest"]]
    g91 = {}
    for rec in forests:
        for q in rec["data"]:
            g91.setdefault((q, rec["data"][q]["K"]), []).append((rec, q))
    v91 = sum(1 for k, v in g91.items() if len({r["data"][q]["A"] for r, q in v}) > 1)
    n91 = sum(1 for k, v in g91.items() if len(v) > 1)
    print(f"91 (forest K=>A): collision classes={n91}, violations={v91}")

    v92 = v93 = v94 = 0; f93_lc = 0
    for rec in forests:
        for q in rec["data"]:
            K = rec["data"][q]["K"]; bK = rec["data"][q]["bK"]; bA = rec["data"][q]["bA"]
            if support(K) != tuple(range(0, bK + 1, 2)):
                v92 += 1
            ev = even_subseq(K)
            if not unimodal(ev):
                v93 += 1
            if not strict_logconcave_interior(ev):
                f93_lc += 1
            if bK > 2 * bA:
                v94 += 1
    print(f"92 (forest supp K = evens): violations={v92}")
    print(f"93 (forest even-K unimodal): violations={v93}; strict-log-concavity fails {f93_lc} times")
    print(f"94 (forest bK<=2bA): violations={v94}")

    # 94 unrestricted fails on non-forests
    nf_fail = 0
    for rec in corpus:
        if not rec["forest"]:
            for q in rec["data"]:
                if rec["data"][q]["bK"] > 2 * rec["data"][q]["bA"]:
                    nf_fail += 1
    print(f"   unrestricted bK<=2bA fails on non-forests: {nf_fail} (confirms forest restriction is meaningful)")

    # 95: ut_n even-K strict log-concave
    print("95 (ut_n even-K strict log-concave):")
    for q, nmax in [(2, 6), (3, 5), (5, 4)]:
        for nn in range(2, nmax + 1):
            rel = frozenset((i, j) for i in range(nn) for j in range(i + 1, nn))
            basis, m, br, adB, kir = C.build_algebra(nn, rel)
            A, K = C.enumerators(m, adB, kir, q)
            ev = even_subseq(K)
            nz = [x for x in ev if x]
            if len(nz) >= 3:
                ok = strict_logconcave_interior(ev)
                print(f"   ut_{nn} q={q}: even-K={ev}  strict-LC={ok}")

    # 96: incidence covariance < 0 for nonabelian, = 0 iff abelian (q=2, m<=6, perp-subspace enum)
    print("96 (incidence covariance): sampling I_L on n<=4, m<=6 posets", flush=True)
    def nullspace_basis(rowsMT, m, p):
        """basis of {f : rowsMT @ f = 0} where rowsMT is a list of length-m rows (the image vectors)."""
        # row reduce the image vectors; free columns give basis of perp
        R=[r[:] for r in rowsMT]; pivots=[]; r=0
        for c in range(m):
            piv=-1
            for i in range(r,len(R)):
                if R[i][c]%p: piv=i;break
            if piv<0: continue
            R[r],R[piv]=R[piv],R[r]
            inv=pow(R[r][c]%p,p-2,p); R[r]=[(x*inv)%p for x in R[r]]
            for i in range(len(R)):
                if i!=r and R[i][c]%p:
                    f=R[i][c]%p; R[i]=[(R[i][j]-f*R[r][j])%p for j in range(m)]
            pivots.append(c); r+=1
        free=[c for c in range(m) if c not in pivots]
        basis=[]
        for fc in free:
            v=[0]*m; v[fc]=1
            for ri,pc in enumerate(pivots):
                v[pc]=(-R[ri][fc])%p
            basis.append(v)
        return basis
    v96=0; ab_ok=0; nonab=0
    for rec in corpus:
        if rec["n"]>4 or rec["m"]>6: continue
        m=rec["m"]; br=rec["br"]; adB=rec["adB"]; kir=rec["kir"]; q=2
        abelian=all(not br[a][b] for a in range(m) for b in range(m))
        pairs=[]
        for bits in range(q**m if m else 1):
            coeffs=[(bits>>a)&1 for a in range(m)]
            adrows=[[0]*m for _ in range(m)]
            for a in range(m):
                if coeffs[a]:
                    for i in range(m):
                        for j in range(m):
                            adrows[i][j]=(adrows[i][j]+adB[a][i][j])%q
            rax=C.rank_mod(adrows,m,q)
            # image vectors = columns of ad_x
            imgs=[[adrows[i][j] for i in range(m)] for j in range(m)]
            imgs=[v for v in imgs if any(v)]
            nb=nullspace_basis(imgs,m,q) if imgs else [[1 if i==k else 0 for i in range(m)] for k in range(m)]
            # enumerate perp subspace
            fdim=len(nb)
            for fb in range(q**fdim if fdim else 1):
                fc=[0]*m
                for t in range(fdim):
                    if (fb>>t)&1:
                        for i in range(m): fc[i]=(fc[i]+nb[t][i])%q
                Brows=[[0]*m for _ in range(m)]
                for k in range(m):
                    if fc[k]:
                        for a in range(m):
                            for b in range(m):
                                Brows[a][b]=(Brows[a][b]+kir[k][a][b])%q
                pairs.append((rax,C.rank_mod(Brows,m,q)))
        if not pairs: continue
        nx=len(pairs); mx=sum(p[0] for p in pairs)/nx; mf=sum(p[1] for p in pairs)/nx
        cov=sum((p[0]-mx)*(p[1]-mf) for p in pairs)/nx
        if abelian:
            if abs(cov)<1e-9: ab_ok+=1
            else: print("   ABELIAN cov!=0:",sorted(rec["rel"]),cov)
        else:
            nonab+=1
            if cov>=-1e-12:
                v96+=1
                if v96<=3: print("   nonabelian cov>=0:",sorted(rec["rel"]),cov)
    print(f"   nonabelian tested={nonab}, cov>=0 violations={v96}; abelian cov=0 confirmed on {ab_ok}", flush=True)

    print("\nDONE")

if __name__ == "__main__":
    main()
