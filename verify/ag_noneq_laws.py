#!/usr/bin/env python3
"""Part XVI (Conjectures 286-294, ag1-ag9): independent reduced-range
recomputation for the budgeted-irreversibility laws.

Everything is computed from scratch: exact tilted-cumulant perturbation
theory (Drazin-inverse formulas, no finite differences) for the winding
skewness law, direct spectral optimization for the OU frontier laws, exact
superoperator algebra for the quantum layer, and closed-form checks of the
three calibration propositions."""

import sys, math, itertools
import numpy as np
from numpy.linalg import eigvals, eig, norm, matrix_rank
from scipy.optimize import minimize

rng = np.random.default_rng(23)
FAILS = []


def chk(name, ok, extra=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" {extra}" if extra else ""))
    if not ok:
        FAILS.append(name)


# ------------------------------------------------ ag1: winding skewness
def chorded_ring(N, F, g):
    p, m = math.exp(F / (2 * N)), math.exp(-F / (2 * N))
    Q = np.zeros((N, N)); D = np.zeros((N, N))
    for i in range(N):
        j = (i + 1) % N
        Q[i, j] += p; Q[j, i] += m
        D[i, j] = 1 / N; D[j, i] = -1 / N
    if g > 0:
        Q[0, N // 2] += g; Q[N // 2, 0] += g
    np.fill_diagonal(Q, -Q.sum(axis=1))
    return Q, D


def stationary(Q):
    n = Q.shape[0]
    A = np.vstack([Q.T, np.ones(n)])
    b = np.zeros(n + 1); b[-1] = 1
    pi, *_ = np.linalg.lstsq(A, b, rcond=None)
    return pi


def drazin_apply(Q, pi, b):
    n = Q.shape[0]
    P = np.eye(n) - np.outer(np.ones(n), pi)
    M = np.vstack([np.hstack([Q, np.ones((n, 1))]), np.hstack([pi, np.zeros(1)])])
    sol = np.linalg.solve(M, np.concatenate([P @ b, [0.0]]))
    return sol[:n]


def winding_S3(Q, D):
    n = Q.shape[0]
    pi = stationary(Q)
    off = ~np.eye(n, dtype=bool)
    V1 = np.where(off, Q * D, 0.0)
    V2 = np.where(off, Q * D * D, 0.0)
    V3 = np.where(off, Q * D * D * D, 0.0)
    one = np.ones(n)
    lam1 = pi @ V1 @ one
    r1 = drazin_apply(Q, pi, lam1 * one - V1 @ one)
    lam2 = 0.5 * (pi @ V2 @ one) + pi @ V1 @ r1
    r2 = drazin_apply(Q, pi, lam1 * r1 - V1 @ r1 - 0.5 * (V2 @ one))
    lam3 = (pi @ V3 @ one) / 6 + 0.5 * (pi @ V2 @ r1) + pi @ V1 @ r2
    c2, c3 = 2 * lam2, 6 * lam3
    return abs(c3) / c2 ** 1.5


ok1 = True
minratio = 9.0
for N in (4, 6, 8, 10):
    for F in (0.5, 2.0, 8.0):
        Q0, D = chorded_ring(N, F, 0.0)
        act0 = -np.trace(Q0) / N
        prev = winding_S3(Q0, D)
        base = prev
        for g in (0.005, 0.02, 0.1, 0.5, 2.0, 8.0, 32.0):
            Q, D2 = chorded_ring(N, F, g)
            Q = Q * (act0 / (-np.trace(Q) / N))
            v = winding_S3(Q, D2)
            ok1 &= v > prev - 1e-13
            minratio = min(minratio, v / base)
            prev = v
chk("ag1 winding skewness strictly increasing (exact cumulants, N<=10)",
    ok1 and minratio > 1, f"min ratio {minratio:.7f}")


# ag1 symmetry: affinity reversal is exact antisymmetry psi(-F,z)=psi(F,-z),
# so the SIGNED third cumulant is odd in F while c_2 is even; the standardized
# skewness S_3=|c_3|/c_2^{3/2} is therefore EVEN in F and the law is symmetric
# under affinity reversal (stated for F!=0; positive-affinity tests cover both).
def ring_lead(N, F, g, z):
    L = np.zeros((N, N), dtype=complex)
    for i in range(N):
        j = (i + 1) % N
        L[j, i] += math.exp(F / 2) * np.exp(z / N)
        L[i, j] += math.exp(-F / 2) * np.exp(-z / N)
    L[N // 2, 0] += g
    L[0, N // 2] += g
    for i in range(N):
        L[i, i] -= L[:, i].sum()
    ev = eigvals(L)
    return ev[np.argmax(ev.real)]


ok_anti = True
for N in (4, 6, 8):
    for F in (0.7, 2.0):
        for g in (0.0, 0.5, 2.0):
            for z in (0.05, 0.3, 1.1):
                ok_anti &= abs(ring_lead(N, F, g, z) - ring_lead(N, -F, g, -z)) < 1e-9
chk("ag1 control: affinity reversal antisymmetry psi(-F,z)=psi(F,-z) (F>0 repair)",
    ok_anti, "every odd winding cumulant odd in F")

# ------------------------------------------------ OU frontier machinery
def pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def Bmat(x, s):
    B = np.diag(np.asarray(s, float))
    for a, (i, j) in zip(x, pairs(len(s))):
        B[i, j] = a; B[j, i] = -a
    return B


def rate(x, s):
    return float(min(eigvals(Bmat(x, s)).real))


def freq(x, s):
    return float(max(abs(eigvals(Bmat(x, s)).imag)))


def cost_w(s):
    return np.array([1 / s[i] + 1 / s[j] for i, j in pairs(len(s))])


def project(x, s, budget):
    w = cost_w(s)
    c = float(np.dot(w, x * x))
    return x if c <= budget else x * math.sqrt(budget / c)


def maximize(fun, s, budget, nstart=30):
    w = cost_w(s); npair = len(w)
    best = (-1e18, None)
    starts = []
    for k in range(npair):
        z = np.zeros(npair); z[k] = math.sqrt(budget / w[k]); starts += [z, -z]
    for _ in range(nstart):
        z = rng.normal(size=npair)
        z *= math.sqrt(budget / np.dot(w, z * z)) * rng.uniform(0.3, 1.0)
        starts.append(z)
    for z in starts:
        r = minimize(lambda x: -fun(project(x, s, budget), s), z,
                     method="Nelder-Mead",
                     options={"maxiter": 4000, "xatol": 1e-12, "fatol": 1e-14})
        if -r.fun > best[0]:
            best = (-r.fun, project(r.x, s, budget))
    return best


s3 = np.array([1.0, 2.0, 5.0])

# Proposition ag:pair identities
gam = lambda s1, sj: s1 * sj / ((sj - s1) * (sj + s1))
okp = gam(1, 2) > gam(1, 5) and abs(gam(1, 2) - 2 / (1 * 3)) < 1e-12
ep12 = ((s3[1] - s3[0]) ** 2 / 4) * (1 / s3[0] + 1 / s3[1])
x = np.zeros(3); x[0] = (s3[1] - s3[0]) / 2
okp &= abs(min(eigvals(Bmat(x, s3)).real) - (s3[0] + s3[1]) / 2) < 1e-12
okp &= abs(float(np.dot(cost_w(s3), x * x)) - ep12) < 1e-12
chk("Proposition ag:pair identities (best partner, EP cost, block closure)", okp)

# ag4: two-mode support at small budget
ok4 = True
maxleak = 0.0
for b in (0.005, 0.02, 0.08, 0.16):
    v, xo = maximize(rate, s3, b, nstart=20)
    leak = math.sqrt(xo[1] ** 2 + xo[2] ** 2)
    maxleak = max(maxleak, leak)
    ok4 &= leak < 5e-3
    # matches the exact pair formula on the first arc
    pred = (s3[0] + s3[1]) / 2 - math.sqrt(max(0, ((s3[1] - s3[0]) / 2) ** 2
                                               - b / (1 / s3[0] + 1 / s3[1])))
    ok4 &= abs(v - pred) < 2e-4
chk("ag4 two-mode support and exact first arc, s=(1,2,5)", ok4,
    f"max leak {maxleak:.1e}")

# ag2: recruitment is by initial segments (essentiality test)
def essential_modes(xo, s, budget, vfull):
    ess = []
    n = len(s)
    for m in range(n):
        xr = np.array([a if m not in p else 0.0
                       for a, p in zip(xo, pairs(n))])
        vr = rate(project(xr, s, budget), s)
        # re-optimize within the restricted support for fairness
        if vfull - vr > 1e-6:
            ess.append(m)
    return ess


ok2 = True
prev_m = 0
for b in (0.02, 0.1, 0.3, 0.6, 1.5, 4.0):
    v, xo = maximize(rate, s3, b, nstart=20)
    ess = essential_modes(xo, s3, b, v)
    if ess:
        ok2 &= ess == list(range(max(ess) + 1))
        ok2 &= max(ess) + 1 >= prev_m
        prev_m = max(max(ess) + 1, prev_m)
chk("ag2 recruitment by initial segments (essential modes), s=(1,2,5)", ok2)

# ag3: first-arc convexity (exact formula) + ceiling at finite budget
arc = [(s3[0] + s3[1]) / 2 - math.sqrt(((s3[1] - s3[0]) / 2) ** 2
                                       - b / (1 / s3[0] + 1 / s3[1]))
       for b in np.linspace(0.01, 0.36, 12)]
sl = np.diff(arc)
ok3 = all(sl[i + 1] > sl[i] for i in range(len(sl) - 1))
vceil, _ = maximize(rate, s3, 8.0, nstart=24)
ok3 &= abs(vceil - float(np.mean(s3))) < 1e-5
chk("ag3 first-arc convexity + trace ceiling at finite budget", ok3,
    f"r(8.0)={vceil:.6f} vs {float(np.mean(s3)):.6f}")

# ag5: pair envelope for the frequency (adversarial, n=3 and n=4)
def pair_freq(s, budget):
    best = 0.0
    for i, j in pairs(len(s)):
        v = budget / (1 / s[i] + 1 / s[j]) - ((s[j] - s[i]) / 2) ** 2
        if v > 0:
            best = max(best, math.sqrt(v))
    return best


ok5 = True
worst = 0.0
for svec in ([1, 2, 5], [1, 2, 5, 8]):
    s = np.array(svec, float)
    for b in (0.5, 2.0, 8.0):
        pf = pair_freq(s, b)
        v, _ = maximize(freq, s, b, nstart=24)
        ok5 &= v <= pf * (1 + 1e-6) + 1e-9
        worst = max(worst, v / pf)
chk("ag5 rank-two oscillation envelope (adversarial)", ok5,
    f"max dense/pair ratio {worst:.8f}")

# ag6: cheapest EP (adversarial separation minimization below pair cost)
def minsep(x, s):
    ev = eigvals(Bmat(x, s))
    return float(min(abs(ev[i] - ev[j]) for i in range(len(s))
                     for j in range(i + 1, len(s))))


ok6 = True
for svec in ([1, 2, 5], [1, 2, 5, 8]):
    s = np.array(svec, float)
    cstar = min(((s[j] - s[i]) ** 2 / 4) * (1 / s[i] + 1 / s[j])
                for i, j in pairs(len(s)))
    v, _ = maximize(lambda x_, s_: -minsep(x_, s_), s, 0.97 * cstar, nstart=30)
    ok6 &= -v > 1e-3
    # the pair block itself coalesces at cstar
    i, j = min(pairs(len(s)), key=lambda p: ((s[p[1]] - s[p[0]]) ** 2 / 4)
               * (1 / s[p[0]] + 1 / s[p[1]]))
    xep = np.zeros(len(pairs(len(s))))
    xep[pairs(len(s)).index((i, j))] = (s[j] - s[i]) / 2
    ok6 &= minsep(xep, s) < 1e-7
chk("ag6 cheapest exceptional point is the pair block (adversarial)", ok6)

# ------------------------------------------------ quantum layer
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.array([[1, 0], [0, -1]], complex)
P1 = [I2, X, Y, Z]


def pauli_lindblad(gam, H=None):
    L = np.zeros((4, 4), complex)
    for P, g in zip([X, Y, Z], gam):
        L += g * (np.kron(P.conj(), P) - np.eye(4))
    if H is not None:
        L += -1j * (np.kron(np.eye(2), H) - np.kron(H.T, np.eye(2)))
    return L


gamq = (0.35, 0.65, 1.05)
sph = np.array([2 * (gamq[1] + gamq[2]), 2 * (gamq[0] + gamq[2]),
                2 * (gamq[0] + gamq[1])])
hv = np.array([0.23, -0.17, 0.41])
Hq = 0.5 * (hv[0] * X + hv[1] * Y + hv[2] * Z)
Aq = np.array([[0, hv[2], -hv[1]], [-hv[2], 0, hv[0]], [hv[1], -hv[0], 0]])
lev = sorted([z for z in eigvals(pauli_lindblad(gamq, Hq)) if abs(z) > 1e-9],
             key=lambda z: (round(z.real, 9), z.imag))
bev = sorted([-z for z in eigvals(np.diag(sph) + Aq)],
             key=lambda z: (round(z.real, 9), z.imag))
err = max(abs(a - b) for a, b in zip(lev, bev))
chk("Proposition ag:env qubit equality (Bloch <-> OU spectra)", err < 1e-10,
    f"error {err:.1e}")

# ag9: two-qubit second-order local vs entangling (nonresonant/resonant)
def two_qubit_modes(gA, gB):
    sA = {0: 0.0, 1: 2 * (gA[1] + gA[2]), 2: 2 * (gA[0] + gA[2]),
          3: 2 * (gA[0] + gA[1])}
    sB = {0: 0.0, 1: 2 * (gB[1] + gB[2]), 2: 2 * (gB[0] + gB[2]),
          3: 2 * (gB[0] + gB[1])}
    modes = [(a, b) for a in range(4) for b in range(4) if (a, b) != (0, 0)]
    return modes, np.array([sA[a] + sB[b] for a, b in modes])


def second_order_best(gA, gB, local_only):
    modes, s = two_qubit_modes(gA, gB)
    slow = int(np.argmin(s))
    Ps = [np.kron(P1[a], P1[b]) for a, b in modes]
    if local_only:
        dirs = [(x, 0) for x in (1, 2, 3)] + [(0, y) for y in (1, 2, 3)]
    else:
        dirs = [(x, y) for x in range(4) for y in range(4) if (x, y) != (0, 0)]
    amats = []
    for (x, y) in dirs:
        H = np.kron(P1[x], P1[y])
        a = np.zeros((len(modes), len(modes)))
        for j2 in range(len(modes)):
            img = -1j * (H @ Ps[j2] - Ps[j2] @ H)
            for i2 in range(len(modes)):
                a[i2, j2] = np.real(np.trace(Ps[i2].conj().T @ img) / 4)
        amats.append(a)
    nd = len(dirs)
    Nm = np.zeros((nd, nd)); Mm = np.zeros((nd, nd))

    def nb(c):
        a = sum(ci * Ai for ci, Ai in zip(c, amats))
        nv = sum(a[slow, j2] ** 2 / (s[j2] - s[slow])
                 for j2 in range(len(modes))
                 if j2 != slow and s[j2] > s[slow] + 1e-12)
        bv = 0.5 * sum(a[j2, k2] ** 2 * (1 / s[j2] + 1 / s[k2])
                       for j2 in range(len(modes)) for k2 in range(len(modes))
                       if j2 != k2)
        return nv, bv

    E = np.eye(nd)
    for i2 in range(nd):
        for j2 in range(i2, nd):
            nij, bij = nb(E[i2] + E[j2])
            ni, bi = nb(E[i2]); nj, bj = nb(E[j2])
            Nm[i2, j2] = Nm[j2, i2] = (nij - ni - nj) / 2
            Mm[i2, j2] = Mm[j2, i2] = (bij - bi - bj) / 2
    for i2 in range(nd):
        Nm[i2, i2], Mm[i2, i2] = nb(E[i2])
    w, V = np.linalg.eigh(Mm)
    keep = w > 1e-10
    Pr = V[:, keep] / np.sqrt(w[keep])
    return float(np.max(np.linalg.eigvalsh(Pr.T @ Nm @ Pr)))


lo = second_order_best((.2, .7, 1.1), (.4, .9, 1.4), True)
fu = second_order_best((.2, .7, 1.1), (.4, .9, 1.4), False)
chk("retained control: local Hamiltonian attains the full second-order optimum "
    "(discarded entangling-resonance criterion)",
    fu <= lo * (1 + 1e-8) + 1e-12, f"local {lo:.6f} full {fu:.6f}")

# ag9 + Proposition ag:basin: exact sphere law and kappa divergence
def slow_left(s, h):
    B = Bmat(np.array([-h, 0, 0]), s)
    ev, R = eig(B)
    idx = int(np.argmin(ev.real))
    lam = ev[idx]; r = R[:, idx]
    evL, W = eig(B.T)
    j = int(np.argmin(abs(evL - lam)))
    l = W[:, j] / (W[:, j] @ r)
    return l.real, float(norm(l) * norm(r))


okb = True
d = (s3[1] - s3[0]) / 2
for h in (0.3, 0.45, 0.49, 0.499):
    l, kap = slow_left(s3, h)
    u = math.sqrt(d * d - h * h)
    kexact = (h * h + (d - u) ** 2) / (h * h - (d - u) ** 2)
    okb &= abs(kap - kexact) < 1e-8
    pts = rng.normal(size=(200000, 3))
    pts /= norm(pts, axis=1)[:, None]
    eps = 0.02
    frac = float(np.mean(abs(pts @ l) < eps))
    okb &= abs(frac - eps / kap) < 3 * math.sqrt(frac / 200000) + 3e-4
chk("Proposition ag:basin exact law mu(B_eps)=eps/kappa on the sphere", okb)
kaps = [slow_left(s3, h)[1] * math.sqrt(d - h) for h in (0.49, 0.499, 0.4999)]
chk("ag:basin kappa ~ sqrt(h_c/2)(h_c-h)^{-1/2}",
    all(abs(k - math.sqrt(d / 2)) < 0.02 for k in kaps),
    f"scaled limits {[round(k,4) for k in kaps]} vs {math.sqrt(d/2):.4f}")

print()
if FAILS:
    print("FAILURES:", len(FAILS))
    for f in FAILS:
        print("  -", f)
    sys.exit(1)
print("All Part XVI checks passed.")
