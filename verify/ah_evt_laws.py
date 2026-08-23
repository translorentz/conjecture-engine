#!/usr/bin/env python3
"""Independent verification for Part XVII (Conjectures 295-307, ah1-ah13).

Re-derives, with fresh implementations, the computational claims of the part:
the tilted Gaussian-orthant formula for Husler-Reiss extremal coefficients and
the isoperimetry, closure, elasticity, monotonicity, and curvature laws built
on it; the cluster thinning algebra, the Bloom-pair occupancy refutation, and
the occupancy census behind the repaired tomography conjecture; process-level
thinning spectroscopy on a moving-maximum process; the Hausdorff and
persistence checks of the angular-topology programme (own F2 Vietoris-Rips);
the integer/fractional tomography dichotomy and its stability spectra; the
sparse-tomography threshold; and the Poissonization and factorial-cumulant
ladder for randomized blocks.  Runs in a few minutes; every check asserts.
"""
import itertools
import math
from collections import Counter

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import multivariate_normal, norm

rng = np.random.default_rng(20260819)
PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    assert ok, name


# ---------------------------------------------------------------- HR layer
def theta_from_gamma(G):
    m = G.shape[0]
    tot = 0.0
    for i in range(m):
        idx = [j for j in range(m) if j != i]
        mu = np.array([G[i, j] / 2 for j in idx])
        S = np.array([[(G[i, j] + G[i, k] - G[j, k]) / 2 for k in idx] for j in idx])
        tot += multivariate_normal(mean=np.zeros(m - 1), cov=S + 1e-12 * np.eye(m - 1),
                                   allow_singular=True).cdf(mu)
    return tot


def gamma_from_points(X):
    m = X.shape[0]
    return np.array([[np.dot(X[i] - X[j], X[i] - X[j]) for j in range(m)]
                     for i in range(m)])


def simplex_points(m, scale=1.0):
    X = np.eye(m) - 1.0 / m
    U, s, _ = np.linalg.svd(X, full_matrices=False)
    X = (U * s)[:, :m - 1]
    return X / math.sqrt(np.dot(X[0] - X[1], X[0] - X[1])) * scale


print("== Proposition ah:hr and Conjectures ah1-ah4 (HR geometry)")
# (ah:hr i) formula agrees with the pairwise closed form
errs = [abs(theta_from_gamma(np.array([[0.0, g], [g, 0.0]])) - 2 * norm.cdf(math.sqrt(g) / 2))
        for g in (0.04, 0.5, 2.0, 9.0)]
check("orthant formula reproduces 2*Phi(sqrt(Gamma)/2) at m=2", max(errs) < 1e-9,
      f"max err {max(errs):.1e}")

# (ah:hr ii) pairwise elasticity bound
xs = np.linspace(1e-4, 12, 4000)
el2 = xs * norm.pdf(xs) / (2 * norm.cdf(xs))
check("pairwise elasticity sup = 0.1473 < 1/2", abs(el2.max() - 0.14726) < 2e-3,
      f"sup {el2.max():.4f}")

# (ah1) random fixed-energy perturbations never beat the simplex
for m in (3, 4):
    Xeq = simplex_points(m, 1.0)
    S0 = sum(np.dot(Xeq[i] - Xeq[j], Xeq[i] - Xeq[j])
             for i in range(m) for j in range(i + 1, m))
    th_eq = theta_from_gamma(gamma_from_points(Xeq))
    worst = -1e9
    for _ in range(120):
        X = Xeq + rng.normal(0, 0.35, Xeq.shape)
        X -= X.mean(axis=0)
        e = sum(np.dot(X[i] - X[j], X[i] - X[j]) for i in range(m) for j in range(i + 1, m))
        X = X * math.sqrt(S0 / e)
        worst = max(worst, theta_from_gamma(gamma_from_points(X)))
    check(f"ah1 m={m}: perturbed theta <= simplex theta", worst <= th_eq + 1e-7,
          f"simplex {th_eq:.6f} best perturbed {worst:.6f}")

# (ah1b) proved refutation side: triangle+centers beats simplex at small scale
def e_iid(k):
    from scipy.integrate import quad
    return quad(lambda x: x * k * norm.pdf(x) * norm.cdf(x) ** (k - 1), -12, 12)[0]


fvals = {k: e_iid(k) / math.sqrt(k - 1) for k in (2, 3, 4, 5, 6)}
check("ah1b: e_k/sqrt(k-1) peaks at k=3",
      fvals[3] > max(v for k, v in fvals.items() if k != 3),
      f"{ {k: round(v, 5) for k, v in fvals.items()} }")
def kactive(m, k, S0):
    X = np.zeros((k + 1, max(k - 1, 1)))
    T = simplex_points(k, 1.0)
    X[:k] = T / np.linalg.norm(T[0]) * math.sqrt(S0 / (m * k))
    return X


for m, scale in ((4, 0.08), (5, 0.2)):
    S0 = m * (m - 1) / 2 * scale ** 2
    ts = theta_from_gamma(gamma_from_points(simplex_points(m, scale)))
    tt = theta_from_gamma(gamma_from_points(kactive(m, 3, S0)))
    check(f"ah1b: triangle+centers beats simplex at m={m}, scale={scale}",
          tt > ts + 1e-6, f"triangle {tt:.6f} vs simplex {ts:.6f}")
S0 = 10 * 0.35 ** 2
t4 = theta_from_gamma(gamma_from_points(kactive(5, 4, S0)))
t5 = theta_from_gamma(gamma_from_points(simplex_points(5, 0.35)))
t3 = theta_from_gamma(gamma_from_points(kactive(5, 3, S0)))
check("ah1b: four-active phase at m=5, scale 0.35",
      t4 > t5 + 1e-4 and t4 > t3 + 1e-4,
      f"k=3: {t3:.6f}, k=4: {t4:.6f}, k=5: {t5:.6f}")

# (ah2) deficit ratio approaches one from below
X = rng.normal(size=(3, 2)); X -= X.mean(axis=0)
G = gamma_from_points(X); G /= G[G > 0].min()
ratios = []
for t in (6.0, 24.0, 96.0):
    th = theta_from_gamma(t * G)
    dsum = sum(2 * (1 - norm.cdf(math.sqrt(t * G[i, j]) / 2))
               for i in range(3) for j in range(i + 1, 3))
    ratios.append((3 - th) / dsum)
check("ah2: deficit ratio rises toward 1", ratios[0] < ratios[1] < ratios[2] <= 1.0 + 1e-9,
      f"ratios {['%.4f' % r for r in ratios]}")

# (ah3a) elasticity stays below 1/2 on a grid of geometries
worst_el = 0.0
for _ in range(10):
    m = int(rng.integers(3, 5))
    X = rng.normal(size=(m, m - 1)); X -= X.mean(axis=0)
    G = gamma_from_points(X); G /= G[G > 0].max()
    for t in np.geomspace(0.05, 30, 8):
        h = 0.02
        e = (math.log(theta_from_gamma(math.exp(math.log(t) + h) * G))
             - math.log(theta_from_gamma(math.exp(math.log(t) - h) * G))) / (2 * h)
        worst_el = max(worst_el, e)
check("ah3a: sampled elasticity < 1/2", worst_el < 0.5, f"max {worst_el:.4f}")

# (ah3b) entrywise monotonicity on admissible pairs
def admissible(G):
    m = G.shape[0]
    J = np.eye(m) - np.ones((m, m)) / m
    return np.linalg.eigvalsh(-0.5 * J @ G @ J).min() > -1e-10


mono_tested = 0
for _ in range(400):
    m = int(rng.integers(3, 5))
    X = rng.normal(size=(m, m - 1)); X -= X.mean(axis=0)
    G = gamma_from_points(X)
    H = rng.uniform(0, 0.5, size=(m, m)); H = (H + H.T) / 2; np.fill_diagonal(H, 0)
    G2 = G * (1 + H)
    if not admissible(G2):
        continue
    mono_tested += 1
    assert theta_from_gamma(G2) >= theta_from_gamma(G) - 1e-8
    if mono_tested >= 40:
        break
check("ah3b: theta monotone on admissible entrywise increases", mono_tested >= 30,
      f"{mono_tested} pairs")

# (ah4) collinear q = 0; random q >= 0; m=2 expansion has no t-term
Z = rng.normal(size=(400000, 2))
col = np.array([[0.0, 0.0], [0.4, 0.0], [1.0, 0.0]]); col -= col.mean(axis=0)
Gv = Z @ col.T; I = np.argmax(Gv, axis=1)
Mv = Gv[np.arange(len(Z)), I]
q = 0.5 * (Mv ** 2 - (col ** 2).sum(axis=1)[I])
check("ah4: collinear q = 0", abs(q.mean()) < 4 * q.std() / math.sqrt(len(Z)),
      f"q = {q.mean():+.5f}")
PHIQ = np.linspace(0, 2 * math.pi, 200_000, endpoint=False)
UQ = np.stack([np.cos(PHIQ), np.sin(PHIQ)], axis=1)


def q_exact(X):
    V = UQ @ X.T
    Iq = np.argmax(V, axis=1)
    g = V[np.arange(len(PHIQ)), Iq]
    return 0.5 * (2.0 * (g ** 2).mean() - (X ** 2).sum(axis=1)[Iq].mean())


qmin = 1e9
for _ in range(40):
    X = rng.normal(size=(3, 2)); X -= X.mean(axis=0)
    X /= math.sqrt((X ** 2).sum())
    qmin = min(qmin, q_exact(X))
thin = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, 0.01]]); thin -= thin.mean(axis=0)
qmin = min(qmin, q_exact(thin / math.sqrt((thin ** 2).sum())))
check("ah4: exact planar q >= 0 (incl. thin triangle)", qmin > -1e-9, f"min {qmin:.2e}")
u = np.array([1e-3, 1e-2, 5e-2])
resid = 2 * norm.cdf(u) - 1 - 2 * norm.pdf(0) * u
check("ah4: m=2 expansion has vanishing t-coefficient", np.all(np.abs(resid) < u ** 3),
      "2Phi(u)-1-sqrt(2/pi)u = O(u^3)")

# ------------------------------------------------- cluster thinning algebra
print("== Proposition ah:thin and Conjectures ah5-ah6 (cluster tomography)")


def occ_multiset(S, m):
    return tuple(sorted(Counter(x % m for x in S).values()))


def occ_data(S, top):
    return tuple(occ_multiset(S, m) for m in range(2, top + 1))


def diff_multiset(S):
    return tuple(sorted(b - a for a, b in itertools.combinations(sorted(S), 2)))


# (ah:thin iii) recover occupancy multiset from Q_{m,S}(p) samples
S = (0, 2, 3, 7, 11)
m = 4
counts = Counter(x % m for x in S)
ps = np.linspace(0.05, 0.95, 12)
Q = np.array([sum(1 - (1 - p) ** counts.get(r, 0) for r in range(m)) / m for p in ps])
A = np.array([[(1 - (1 - p) ** k) / m for k in range(1, len(S) + 1)] for p in ps])
coef, *_ = np.linalg.lstsq(A, Q, rcond=None)
rec = {k + 1: int(round(c)) for k, c in enumerate(coef) if round(c) > 0}
check("ah:thin iii: occupancy multiset recovered from response",
      rec == dict(Counter(counts.values())), f"{rec}")

# (ah:thin iv) Moebius recovery of the difference multiset
ok_moeb = True
def mobius(n):
    out, nn, p = 1, n, 2
    while p * p <= nn:
        if nn % p == 0:
            nn //= p
            if nn % p == 0:
                return 0
            out = -out
        p += 1
    return -out if nn > 1 else out


for _ in range(120):
    k = int(rng.integers(3, 7))
    S = tuple(sorted(rng.choice(50, size=k, replace=False).tolist()))
    D = max(S) - min(S)
    g = {mm: sum(math.comb(c, 2) for c in Counter(x % mm for x in S).values())
         for mm in range(1, D + 1)}
    cd = Counter(diff_multiset(S))
    for delta in range(1, D + 1):
        c_rec = sum(mobius(j) * g.get(j * delta, 0) for j in range(1, D // delta + 1))
        if c_rec != cd.get(delta, 0):
            ok_moeb = False
check("ah:thin iv: Moebius inversion recovers difference multiset", ok_moeb)

# (ah:thin v) dilation identity
ok_dil = True
for _ in range(60):
    k = int(rng.integers(3, 6))
    S = tuple(sorted(rng.choice(30, size=k, replace=False).tolist()))
    t = int(rng.integers(2, 7))
    for mm in range(2, 40):
        m1 = mm // math.gcd(t, mm)
        lhs = occ_multiset(tuple(t * x for x in S), mm)
        rhs = occ_multiset(S, m1) if m1 >= 2 else (len(S),)
        if lhs != rhs:
            ok_dil = False
check("ah:thin v: dilation identity for occupancy data", ok_dil)

# Bloom pair: occupancy-equivalent, homometric, not congruent
B1, B2 = (0, 1, 4, 10, 12, 17), (0, 1, 8, 11, 13, 17)
check("Bloom pair shares occupancy data (all m <= 60)",
      occ_data(B1, 60) == occ_data(B2, 60))
check("Bloom pair homometric, non-congruent",
      diff_multiset(B1) == diff_multiset(B2)
      and B2 != tuple(17 - x for x in reversed(B1)) and B1 != B2)
P1, P2 = (0, 1, 3, 8, 10, 14), (0, 1, 7, 9, 11, 14)
check("occupancy data strictly refines homometry",
      diff_multiset(P1) == diff_multiset(P2) and occ_data(P1, 15) != occ_data(P2, 15))

# census: size <= 5 clean through diameter 30; size-6 collisions all homometric
def canon(S):
    S = tuple(sorted(S)); S0 = tuple(x - S[0] for x in S)
    return min(S0, tuple(sorted(S0[-1] - x for x in S0)))


seen = {}
coll5 = 0
for k in (3, 4, 5):
    for D in range(k - 1, 31):
        for mid in itertools.combinations(range(1, D), k - 2):
            S = (0,) + mid + (D,)
            if canon(S) != S:
                continue
            key = (k, D, occ_data(S, 31))
            if key in seen and seen[key] != S:
                coll5 += 1
            seen[key] = S
check("ah6a: no occupancy collisions for size <= 5, diameter <= 30", coll5 == 0,
      f"{len(seen)} canonical sets")
seen6 = {}
coll6 = []
for D in range(5, 19):
    for mid in itertools.combinations(range(1, D), 4):
        S = (0,) + mid + (D,)
        if canon(S) != S:
            continue
        key = (D, occ_data(S, 19))
        if key in seen6 and seen6[key] != S:
            coll6.append((seen6[key], S))
        seen6[key] = S
check("ah6b: all size-6 occupancy collisions (diam <= 18) are homometric pairs",
      len(coll6) == 4 and all(diff_multiset(a) == diff_multiset(b) for a, b in coll6),
      f"{len(coll6)} collisions")

# (ah5) process-level Bernoulli thinning on a moving-maximum process
a = np.array([0.5, 0.2, 0.3])
n = 2_000_000
Zf = 1.0 / -np.log(rng.uniform(size=n + 3))
Xp = np.max(np.stack([a[j] * Zf[3 - j:3 - j + n] for j in range(3)]), axis=0)
srt = np.sort(a)[::-1]
tail = srt / srt[0]
pk = tail - np.append(tail[1:], 0.0)
theta_true = 1.0 / sum((k + 1) * w for k, w in enumerate(pk))
for p in (1.0, 0.5):
    Y = Xp[rng.uniform(size=n) < p]
    u = np.quantile(Y, 1 - 3e-4)
    nb = len(Y) // 200
    Yb = Y[:nb * 200].reshape(nb, 200)
    th_hat = (Yb.max(axis=1) > u).sum() / (Y[:nb * 200] > u).sum()
    GN = sum(w * (1 - p) ** (k + 1) for k, w in enumerate(pk))
    th_pred = theta_true * (1 - GN) / p
    check(f"ah5: thinning response at p={p}", abs(th_hat / th_pred - 1) < 0.08,
          f"est {th_hat:.4f} formula {th_pred:.4f}")

# --------------------------------------------------- angular topology layer
print("== Conjectures ah7-ah8 (angular topology, own F2 Vietoris-Rips)")
C0 = np.array([1, 1, 1]) / 3.0
E1 = np.array([1.0, -1.0, 0.0]) / math.sqrt(2)
E2 = np.array([1.0, 1.0, -2.0]) / math.sqrt(6)
RHO = 0.18


def vr_h1(X, rmax):
    npt = len(X)
    D = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
    edges = sorted((D[i, j], i, j) for i in range(npt) for j in range(i + 1, npt)
                   if D[i, j] <= rmax)
    eidx = {(i, j): r for r, (f, i, j) in enumerate(edges)}
    parent = list(range(npt))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    positive = [False] * len(edges)
    for r, (f, i, j) in enumerate(edges):
        ra, rb = find(i), find(j)
        if ra == rb:
            positive[r] = True
        else:
            parent[ra] = rb
    tris = sorted((max(D[i, j], D[i, k], D[j, k]), i, j, k)
                  for i in range(npt) for j in range(i + 1, npt) for k in range(j + 1, npt)
                  if max(D[i, j], D[i, k], D[j, k]) <= rmax)
    pivot, bars = {}, []
    for f, i, j, k in tris:
        col = {eidx[(i, j)], eidx[(i, k)], eidx[(j, k)]}
        while col:
            low = max(col)
            if low in pivot:
                col ^= pivot[low]
            else:
                pivot[low] = col
                if f > edges[low][0] + 1e-12:
                    bars.append((edges[low][0], f))
                break
    for r in range(len(edges)):
        if positive[r] and r not in pivot:
            bars.append((edges[r][0], rmax))
    return sorted(bars, key=lambda b: b[0] - b[1])


nn = 500_000
R = 1.0 / rng.uniform(size=nn)
PHI = rng.uniform(0, 2 * math.pi, size=nn)
rho_eff = RHO * (1 + 5.0 / R)
W = C0 + rho_eff[:, None] * (np.cos(PHI)[:, None] * E1 + np.sin(PHI)[:, None] * E2)
order = np.argsort(-R)
phig = np.linspace(0, 2 * math.pi, 2000, endpoint=False)
MG = C0 + RHO * (np.cos(phig)[:, None] * E1 + np.sin(phig)[:, None] * E2)
for k in (200, 800):
    A = W[order[:k]]
    P = A - C0
    u1, u2 = P @ E1, P @ E2
    d1 = np.abs(np.hypot(u1, u2) - RHO).max()
    d2 = np.sqrt(((MG[:, None, :] - A[None, :, :]) ** 2).sum(-1)).min(axis=1).max()
    dH = max(d1, d2)
    predict = RHO * 5.0 * k / nn + (math.log(k) / k) * math.pi * RHO
    check(f"ah7: Hausdorff rate at k={k}", dH < 3 * predict,
          f"d_H {dH:.5f} predicted scale {predict:.5f}")
bars = vr_h1(W[order[:60]], 0.40)
death_true = math.sqrt(3) * RHO
check("ah7: one dominant loop with the analytic death",
      len(bars) >= 1 and abs(bars[0][1] - death_true) < 0.02
      and (len(bars) < 2 or (bars[1][1] - bars[1][0]) < 0.4 * (bars[0][1] - bars[0][0])),
      f"bar {bars[0][0]:.3f}->{bars[0][1]:.3f} vs sqrt(3)rho={death_true:.4f}")

nh = 2_000_000
R0 = 1.0 / rng.uniform(size=nh)
R1 = 1.0 / np.sqrt(rng.uniform(size=nh))
J = rng.integers(0, 3, size=nh)
PHIh = rng.uniform(0, 2 * math.pi, size=nh)
WR = C0 + RHO * (np.cos(PHIh)[:, None] * E1 + np.sin(PHIh)[:, None] * E2)
for eta, expect_good in ((0.0, True), (0.45, False)):
    W0 = (1 - eta) * np.eye(3)[J] + eta * rng.dirichlet(np.ones(3), size=nh)
    Xh = R0[:, None] * W0 + R1[:, None] * WR
    Wang = Xh / Xh.sum(axis=1)[:, None]
    keep = (1 - Wang.max(axis=1)) > 0.25
    kk = np.argsort(-Xh.sum(axis=1)[keep])[:120]
    bars = vr_h1(Wang[keep][kk], 0.40)
    dom = bars[0] if bars else (0, 0)
    err = max(abs(dom[0]), abs(dom[1] - death_true)) if bars else death_true / 2
    err = min(err, death_true / 2)
    good = err < 0.12
    check(f"ah8: filtered recovery at eta={eta} is {'good' if expect_good else 'poor'}",
          good == expect_good, f"d_B-proxy {err:.3f}")

# ------------------------------------------------------- tomography layer
print("== Proposition ah:moment and Conjectures ah9-ah10 (tail tomography)")
H1 = [(0.5, 0.2), (0.5, 0.8)]
H2 = [(0.28125, 0.1), (0.4375, 0.5), (0.28125, 0.9)]


def T(H, alpha, av, bv):
    return sum(p * (av * w + bv * (1 - w)) ** alpha for p, w in H)


d2max = max(abs(T(H1, 2.0, av, 3.3 - av) - T(H2, 2.0, av, 3.3 - av))
            for av in np.linspace(0.3, 3.0, 50))
d15max = max(abs(T(H1, 1.5, av, 3.3 - av) - T(H2, 1.5, av, 3.3 - av))
             for av in np.linspace(0.3, 3.0, 50))
check("ah:moment: T_2 blind, T_1.5 separates", d2max < 1e-12 and d15max > 1e-4,
      f"{d2max:.1e} vs {d15max:.1e}")
ws = np.linspace(0.005, 0.995, 80)
avs = np.linspace(0.3, 3.0, 80)
for alpha, lo, hi in ((2.0, 3, 3), (1.5, 8, 40)):
    Mm = np.array([[(av * w + (3.3 - av) * (1 - w)) ** alpha for w in ws] for av in avs])
    sv = np.linalg.svd(Mm, compute_uv=False); sv /= sv[0]
    rank8 = int((sv > 1e-8).sum())
    check(f"ah9: effective rank at alpha={alpha}", lo <= rank8 <= hi, f"rank(1e-8) = {rank8}")

alpha = 1.37
d, s = 3, 2
p = s * (d - 1) + (s - 1)


def forward(x, dirs):
    atoms = x[:s * (d - 1)].reshape(s, d - 1)
    Wm = np.column_stack([atoms, 1 - atoms.sum(axis=1)])
    pis = np.append(x[s * (d - 1):], 1 - x[s * (d - 1):].sum())
    return np.array([sum(pis[r] * max(dirs[j] @ Wm[r], 1e-12) ** alpha for r in range(s))
                     for j in range(len(dirs))])


r2 = np.random.default_rng(7)
while True:
    W0 = r2.dirichlet(np.ones(d), size=s)
    if np.abs(W0[0] - W0[1]).max() > 0.25 and W0.min() > 0.05:
        break
pi0 = r2.dirichlet(np.ones(s))
for m, want_many in ((p - 1, True), (p, False)):
    dirs = r2.uniform(0.3, 2.0, size=(m, d))
    y0 = np.array([sum(pi0[r] * (dirs[j] @ W0[r]) ** alpha for r in range(s))
                   for j in range(m)])
    sols = set()
    for _ in range(60):
        x0 = np.concatenate([r2.dirichlet(np.ones(d), size=s)[:, :d - 1].reshape(-1),
                             r2.dirichlet(np.ones(s))[:s - 1]])
        res = least_squares(lambda x: forward(x, dirs) - y0, x0, method="trf",
                            xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        if np.sum(res.fun ** 2) < 1e-18:
            atoms = res.x[:s * (d - 1)].reshape(s, d - 1)
            pis = np.append(res.x[s * (d - 1):], 1 - res.x[s * (d - 1):].sum())
            if np.any(pis < 1e-6) or np.any(atoms < -1e-6) or np.any(atoms.sum(axis=1) > 1):
                continue
            sols.add(tuple(sorted(tuple(np.round(np.append(atoms[r], pis[r]), 4))
                                  for r in range(s))))
    if want_many:
        check("ah10: continuum below the threshold m=p-1", len(sols) >= 5, f"{len(sols)} solutions")
    else:
        check("ah10: unique solution at the threshold m=p", len(sols) == 1, f"{len(sols)} solution")

# ---------------------------------------------------------- blocks layer
print("== Proposition ah:block and Conjectures ah11-ah13 (block designs)")
al = 2.0
xs = np.linspace(0.7, 5.0, 200)
ns = [64, 256, 1024, 4096, 16384]


def slope(errs):
    return float(np.polyfit(np.log(ns), np.log(errs), 1)[0])


e_fixed = [np.max(np.abs(np.exp(n * np.log1p(-xs ** -al / n)) - np.exp(-xs ** -al)))
           for n in ns]
q0 = xs ** -al / 64
check("ah:block i: Poissonization exact for Pareto",
      np.max(np.abs(np.exp(-64 * q0) - np.exp(-xs ** -al))) < 1e-15)
check("ah12: fixed blocks slope -1", abs(slope(e_fixed) + 1) < 0.05, f"{slope(e_fixed):.3f}")
e2 = []
for n in ns:
    sq = int(round(math.sqrt(n)))
    q = xs ** -al / n
    F = 0.5 * np.exp((n - sq) * np.log1p(-q)) + 0.5 * np.exp((n + sq) * np.log1p(-q))
    e2.append(np.max(np.abs(F - np.exp(-xs ** -al))))
check("ah12: two-point law slope -2", abs(slope(e2) + 2) < 0.05, f"{slope(e2):.3f}")
ladders = {3: ((0, 1, 3), (1 / 3, 1 / 2, 1 / 6)),
           4: ((0, 1, 2, 4), (3 / 8, 1 / 3, 1 / 4, 1 / 24))}
for r, (support, pr) in ladders.items():
    mus = [sum(p * x ** k for p, x in zip(pr, support)) for k in range(1, r + 1)]
    poisson_mus = [1, 2, 5, 15][:r]
    check(f"ah:block iii: r={r} law matches Poisson(1) moments",
          max(abs(a - b) for a, b in zip(mus, poisson_mus)) < 1e-12,
          f"support {support} weights {[f'{v:.4f}' for v in pr]}")
    er = []
    for n in ns[:3]:
        q = xs ** -al / n
        Pxi = sum(pi * (1 - q) ** x for pi, x in zip(pr, support))
        er.append(np.max(np.abs(Pxi ** n - np.exp(-xs ** -al))))
    # slopes fitted on the pre-floor range (errors reach 1e-12 at large n)
    ratio = er[0] / er[1]
    check(f"ah12: r={r} ladder error falls like n^-{r}",
          4 ** r * 0.7 < ratio < 4 ** r * 1.4,
          f"per-4x ratio {ratio:.1f} vs 4^{r}={4 ** r}")

beta = 0.8
us = np.geomspace(5, 500, 30)
sl_gen = float(np.polyfit(np.log(us),
                          np.log(0.5 * us ** -beta + 0.5 * us ** (-2 * beta)), 1)[0])
sl_can = float(np.polyfit(np.log(us), np.log(0.5 * us ** (-2 * beta)), 1)[0])
check("ah13: exponent doubling at cancellation",
      abs(sl_can + 2 * beta) < 1e-6 and -beta - 0.1 < sl_gen < -beta + 0.02,
      f"slopes {sl_gen:.3f} vs {sl_can:.3f}")
rats = []
for n in (1e3, 1e6, 1e9):
    kcan = n ** (4 * beta / (al + 4 * beta))
    ccrit = 0.5 * (n / kcan) ** (-beta / al)
    rats.append(ccrit / n ** (-beta / (al + 4 * beta)))
check("ah13: critical window tracks n^{-beta/(alpha+4beta)}",
      max(rats) / min(rats) < 1.0001, f"constant ratio {rats[0]:.3f}")

print(f"\nAll {len(PASS)} checks passed." if all(PASS) else "FAILURES PRESENT")
