#!/usr/bin/env python3
"""Independent verification for Part XIX (Conjectures 320-334, aj1-aj15):
lag irreversibility of non-equilibrium dynamics.

Central observable: for an irreducible bidirected CTMC with generator Q,
stationary pi, and P_t=exp(tQ), the two-time endpoint law F_t(i,j)=pi_i P_t(i,j)
has lag irreversibility L(t)=KL(F_t||F_t^T); with entropy-production rate sigma
the temporal sampling efficiency is eta(t)=L(t)/(sigma t) in [0,1].

Checks (fresh implementation, no reuse of the source package):
  aj1  RESOLVED FALSE: the homogeneous 10-ring has non-monotone eta(t)
  aj2  gamma * t_*  <= 2         (t_* the L-maximizer, gamma the reversible gap)
  aj3  gamma^2 (int L)/sigma <= 2
  aj4  -log L(t)/(2t) -> alpha_irr   (doubling law: matched to slope of ||A_t||)
  aj8  RESOLVED FALSE: the same homogeneous ring refutes strict monotonicity
  aj9  RESOLVED FALSE: an explicit near-decomposable 7-ring has gamma*L/sigma>1/2
  aj13 RESOLVED FALSE: an explicit 5D Jordan-block OU (g_A=1) has g_A t_* > 1
  aj14 RESOLVED FALSE: the same OU has g_A^2 (int L)/sigma > 1
  aj15 OU doubling law -log L_OU/(2t) -> alpha_H (surviving)
  aj10 wrapped-Brownian scaling limit eta_N(t_N) -> E(A,tau)

Runs in a couple of minutes.  Random search cannot prove the surviving laws;
a PASS means no counterexample was found in the sampled ensembles, except for
aj1, aj8, aj9, aj13, aj14, which are exhibited counterexamples to the deposited
statements.
"""
import numpy as np
from scipy.linalg import expm, eigvals, solve_lyapunov, solve

rng = np.random.default_rng(20260822)
PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))


def stationary(Q):
    n = Q.shape[0]
    A = np.vstack([Q.T, np.ones(n)])
    b = np.zeros(n + 1); b[-1] = 1
    return np.linalg.lstsq(A, b, rcond=None)[0]


def sigma_ep(Q, pi):
    n = len(pi); s = 0.0
    for i in range(n):
        for j in range(n):
            if i != j and Q[i, j] > 0 and Q[j, i] > 0:
                s += pi[i] * Q[i, j] * np.log(pi[i] * Q[i, j] / (pi[j] * Q[j, i]))
    return s


def L_of_t(Q, pi, t):
    P = expm(t * Q); F = pi[:, None] * P; Ft = F.T
    m = (F > 1e-300) & (Ft > 1e-300)
    return float(np.sum(F[m] * np.log(F[m] / Ft[m])))


def rev_gap(Q, pi):
    n = Q.shape[0]; Qs = np.zeros_like(Q)
    for i in range(n):
        for j in range(n):
            if i != j:
                Qs[i, j] = pi[j] * Q[j, i] / pi[i]
    for i in range(n):
        Qs[i, i] = -Qs[i].sum()
    Qbar = 0.5 * (Q + Qs); d = np.sqrt(pi)
    S = -(d[:, None] * Qbar) / d[None, :]; S = 0.5 * (S + S.T)
    return float(np.sort(np.linalg.eigvalsh(S))[1])


def spec_gap(Q):
    re = np.sort(-eigvals(Q).real)
    return float(re[re > 1e-9][0])


def rand_chain(n, dense, lo, hi, biased):
    Q = np.zeros((n, n)); E = set()
    for i in range(n):
        E.add((i, (i + 1) % n)); E.add(((i + 1) % n, i))
    for i in range(n):
        for j in range(n):
            if i != j and (i, j) not in E and rng.random() < dense:
                E.add((i, j)); E.add((j, i))
    for (i, j) in E:
        Q[i, j] = np.exp(rng.uniform(lo, hi))
    if biased:
        b = np.exp(rng.uniform(0.5, 3))
        for i in range(n):
            Q[i, (i + 1) % n] *= b
    for i in range(n):
        Q[i, i] = -Q[i].sum()
    return Q


import mpmath as mp
mp.mp.dps = 80


def eta_homog_ring(N, a, u):
    """Exact eta(t)=L(t)/(sigma t) on the homogeneous N-cycle with clockwise
    rate p=e^{a/2}, counterclockwise q=e^{-a/2}, at reduced lag u=(p-q)t/N,
    by 80-digit Fourier diagonalization of the circulant generator."""
    a = mp.mpf(a)
    p = mp.e ** (a / 2); q = mp.e ** (-a / 2); v = p - q; sigma = (p - q) * a
    w = mp.e ** (2j * mp.pi / N)
    lam = [p * (w ** m - 1) + q * (w ** (-m) - 1) for m in range(N)]
    t = u * N / v
    P = [(mp.mpf(1) / N) * sum(mp.e ** (lam[m] * t) * w ** (-m * k)
                               for m in range(N)) for k in range(N)]
    Lt = mp.mpf(0)
    for k in range(N):
        pk = P[k].real; pmk = P[(-k) % N].real
        if pk > 0 and pmk > 0:
            Lt += pk * mp.log(pk / pmk)
    return Lt / (sigma * t)


print("== aj1 RESOLVED FALSE: homogeneous 10-ring has non-monotone eta(t)")
# The deposited conjecture asserts eta(t)=L/(sigma t) is non-increasing.  It is
# false already on the homogeneous ring, where winding aliasing collapses eta
# near half a winding and then revives it before diffusion mixes the cycle.
eta54 = eta_homog_ring(10, 1, mp.mpf("0.54"))
eta68 = eta_homog_ring(10, 1, mp.mpf("0.68"))
check("aj1 eta revives on the homogeneous 10-ring (monotonicity refuted)",
      eta68 > eta54 * 100,
      f"eta(u=0.54)={mp.nstr(eta54,4)} -> eta(u=0.68)={mp.nstr(eta68,4)}, "
      f"factor {mp.nstr(eta68/eta54,4)}")

print("== aj2 (gamma t_* <= 2), aj3 (gamma^2 area/sigma <= 2)")
m2 = m3 = 0.0
for _ in range(800):
    n = int(rng.integers(3, 9))
    Q = rand_chain(n, rng.uniform(0, 0.5), rng.uniform(-8, -3), rng.uniform(1, 3), rng.random() < 0.6)
    pi = stationary(Q)
    if pi.min() < 1e-12:
        continue
    sig = sigma_ep(Q, pi)
    if sig < 1e-8:
        continue
    g = spec_gap(Q); tmax = 40 / g; ts = np.linspace(tmax / 400, tmax, 400)
    Ls = np.array([L_of_t(Q, pi, t) for t in ts])
    gam = rev_gap(Q, pi)
    m2 = max(m2, gam * ts[np.argmax(Ls)]); m3 = max(m3, gam ** 2 * np.trapezoid(Ls, ts) / sig)
check("aj2 gamma t_* <= 2", m2 <= 2.0, f"max {m2:.3f}")
check("aj3 gamma^2 area/sigma <= 2", m3 <= 2.0, f"max {m3:.3f}")

print("== aj4: doubling law  -log L/(2t) -> alpha_irr  (matched to ||A_t|| slope)")
def At_norm(Q, pi, t):
    P = expm(t * Q); A = pi[:, None] * P - (pi[:, None] * P).T
    return np.linalg.norm(A)
rat = []
for _ in range(60):
    n = int(rng.integers(3, 7))
    Q = rand_chain(n, 0.35, -1, 1.5, False)
    pi = stationary(Q)
    if pi.min() < 1e-8:
        continue
    g = spec_gap(Q); ts = np.linspace(6 / g, 14 / g, 40)
    Ls = np.array([L_of_t(Q, pi, t) for t in ts]); As = np.array([At_norm(Q, pi, t) for t in ts])
    m = (Ls > 1e-250) & (As > 1e-250)
    if m.sum() < 10:
        continue
    rat.append(np.polyfit(ts[m], np.log(Ls[m]), 1)[0] / (2 * np.polyfit(ts[m], np.log(As[m]), 1)[0]))
check("aj4 KL exponent = 2 * antisymmetric-flux exponent", abs(np.median(rat) - 1) < 0.02,
      f"median ratio {np.median(rat):.4f}")


def ring(n, cw, ccw):
    Q = np.zeros((n, n))
    for i in range(n):
        Q[i, (i + 1) % n] = cw[i]; Q[i, (i - 1) % n] = ccw[i]
    for i in range(n):
        Q[i, i] = -Q[i].sum()
    return Q


print("== aj8 RESOLVED FALSE: the homogeneous ring is a strictly monotone-failing cycle")
# The unicyclic strengthening asserts eta'(t)<0 for every driven cycle.  The
# homogeneous 10-ring above is a driven cycle on which eta revives, so aj8 fails
# for the same reason as aj1; the revival is genuine at 80 digits, not the
# finite-precision cancellation once supposed.  We confirm the interior rise on
# a fine reduced-lag grid.
etas8 = [eta_homog_ring(10, 1, mp.mpf(u) / 100) for u in range(50, 71, 2)]
rises8 = max(float(etas8[i + 1] - etas8[i]) for i in range(len(etas8) - 1))
check("aj8 eta strictly-decreasing fails on the homogeneous cycle",
      rises8 > 0,
      f"largest interior increment on u in [0.50,0.70]: +{rises8:.3e}")

print("== aj9 RESOLVED FALSE: explicit near-decomposable 7-ring with gamma L/sigma > 1/2")
# explicit reproducible counterexample to the deposited constant 1/2
cw = np.array([0.226384, 0.210311, 6.271519, 3.188855, 2.030301, 3.934932, 0.001413])
ccw = np.array([1.09928, 1.797104, 0.289091, 2.825231, 0.675518, 1.295227, 0.003263])
Q9 = ring(7, cw, ccw); pi9 = stationary(Q9); sig9 = sigma_ep(Q9, pi9); gam9 = rev_gap(Q9, pi9)
g9 = spec_gap(Q9); ts = np.linspace(0.02 / g9, 40 / g9, 800)
Lmax9 = max(L_of_t(Q9, pi9, t) for t in ts)
ratio9 = gam9 * Lmax9 / sig9
check("aj9 gamma*L/sigma exceeds 1/2 (constant refuted)", ratio9 > 0.5,
      f"gamma*Lmax/sigma = {ratio9:.4f} > 1/2")

print("== aj13/aj14 RESOLVED FALSE (explicit nonnormal Jordan-block OU); aj15 surviving")
def ou_L(A, D, t, C):
    d = A.shape[0]; eAt = expm(A * t)
    Sig = np.block([[C, C @ eAt.T], [eAt @ C, C]])
    SigR = np.block([[C, eAt @ C], [C @ eAt.T, C]])
    return max(0.5 * (np.trace(solve(SigR, Sig)) - 2 * d), 0.0)
def Hnorm(A, t, C):
    eAt = expm(A * t); return np.linalg.norm(eAt @ C - C @ eAt.T)

# Explicit counterexample to aj13 and aj14: A = -I + 2*(superdiagonal nilpotent),
# D = I.  All eigenvalues are -1 so g_A = 1, but the strong nonnormal transient of a
# single large Jordan block pushes the lag-KL peak past one drift-relaxation time and
# the integrated budget past sigma/g_A^2.  The deposited random search sampled only
# drifts with negative-definite symmetric part and so never reached this regime.
d0 = 5
A0 = -np.eye(d0) + 2 * np.diag(np.ones(d0 - 1), 1)
D0 = np.eye(d0)
C0 = solve_lyapunov(A0, -2 * D0)
assert np.max(np.abs(A0 @ C0 + C0 @ A0.T + 2 * D0)) < 1e-9      # exact Lyapunov solution
gA0 = -np.max(eigvals(A0).real)                                 # = 1
Airr0 = A0 + D0 @ np.linalg.inv(C0)
sig0 = np.trace(Airr0.T @ np.linalg.inv(D0) @ Airr0 @ C0)       # entropy production
ts0 = np.linspace(1e-3, 8.0, 16000)
Ls0 = np.array([ou_L(A0, D0, t, C0) for t in ts0])
gAt0 = gA0 * ts0[np.argmax(Ls0)]
tt0 = np.linspace(1e-4, 50.0, 80000)
area0 = np.trapezoid([ou_L(A0, D0, t, C0) for t in tt0], tt0)
narea0 = gA0 ** 2 * area0 / sig0
check("aj13 RESOLVED FALSE: explicit Jordan-block OU has g_A t_* > 1",
      gAt0 > 1.0, f"g_A t_* = {gAt0:.4f} (sigma_OU = {sig0:.1f})")
check("aj14 RESOLVED FALSE: explicit Jordan-block OU has g_A^2 area/sigma > 1",
      narea0 > 1.0, f"g_A^2 (int L)/sigma = {narea0:.4f}")

# aj15 doubling law still surviving: sampled over nonnormal Hurwitz drifts
r15 = []
for _ in range(700):
    d = int(rng.integers(2, 6)); M = rng.normal(size=(d, d))
    A = M - (abs(np.max(eigvals(M).real)) + rng.uniform(0.3, 1.8)) * np.eye(d)
    if rng.random() < 0.5:
        A = A + np.triu(rng.normal(size=(d, d)) * rng.uniform(1, 5), 1)
    if np.max(eigvals(A).real) >= -1e-6:
        continue
    B = rng.normal(size=(d, d)); D = B @ B.T + 0.05 * np.eye(d)
    C = solve_lyapunov(A, -2 * D)
    if np.min(np.linalg.eigvalsh(C)) < 1e-9:
        continue
    gA = -np.max(eigvals(A).real)
    tt = np.linspace(5 / gA, 12 / gA, 40)
    Ls2 = np.array([ou_L(A, D, t, C) for t in tt]); Hs = np.array([Hnorm(A, t, C) for t in tt])
    mm = (Ls2 > 1e-250) & (Hs > 1e-250)
    if mm.sum() >= 10:
        r15.append(np.polyfit(tt[mm], np.log(Ls2[mm]), 1)[0] / (2 * np.polyfit(tt[mm], np.log(Hs[mm]), 1)[0]))
check("aj15 OU doubling law (exponent ratio -> 1)", abs(np.median(r15) - 1) < 0.03,
      f"median ratio {np.median(r15):.4f}")

print("== aj10: wrapped-Brownian limit eta_N(t_N) -> E(A,tau)")
def eta_ring(N, Aaff, tau):
    a = Aaff / N; p = np.exp(a / 2); q = np.exp(-a / 2)
    k = np.arange(N); lam = p * (np.exp(-2j * np.pi * k / N) - 1) + q * (np.exp(2j * np.pi * k / N) - 1)
    t = N * N * tau / (p + q)
    dist = np.fft.ifft(np.exp(lam * t)).real; dist = np.maximum(dist, 0); dist /= dist.sum()
    L = sum(dist[dd] * np.log(dist[dd] / dist[(-dd) % N])
            for dd in range(N) if dist[dd] > 1e-300 and dist[(-dd) % N] > 1e-300)
    return L / (Aaff ** 2 * tau / 2)
def wrapped(Aaff, tau):
    xs = np.linspace(0, 1, 2000, endpoint=False)
    w = lambda s: sum(np.exp(-(xs + k - s * Aaff * tau / 2) ** 2 / (2 * tau)) / np.sqrt(2 * np.pi * tau)
                      for k in range(-6, 7))
    wp, wm = w(1), w(-1)
    return 2 / (Aaff ** 2 * tau) * np.trapezoid(wp * np.log(wp / wm), xs)
err = 0.0
for Aaff in (1.0, 2.0, 4.0):
    for tau in (0.08, 0.2):
        err = max(err, abs(eta_ring(128, Aaff, tau) - wrapped(Aaff, tau)))
check("aj10 ring eta_N(N=128) matches wrapped-Brownian E(A,tau)", err < 5e-3, f"max abs error {err:.2e}")

n_ok = sum(PASS)
print(f"\n{n_ok}/{len(PASS)} checks passed "
      "(surviving laws: no counterexample in sampled ensembles; "
      "aj1, aj8, aj9, aj13, aj14: exhibited counterexamples).")
import sys
sys.exit(0 if all(PASS) else 1)
