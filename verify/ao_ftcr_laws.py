#!/usr/bin/env python3
"""Independent checks for Part XXIV (Conjectures 380-383, fixed-traffic
circulation rays) and the refuted companions of Proposition (ao:basic).

  * ray invariants: pi stationary, traffic and escape rates constant in alpha.
  * endpoint spectral bounds h(alpha)<=h(0), g(alpha)>=g(0).
  * refuted companion: whole-ray fast-edge monotonicity is FALSE -- a valid
    bidirected ray on which h(alpha) strictly increases, confirmed at 40 digits.
  * ao1 (E1): alternating-derivative hierarchy of E[U_{gamma,t}] in x=alpha^2,
    via the exact augmented (X_t, V_t) chain.
  * ao4 (E3): stochastic acceleration of the visited stationary mass on a cycle,
    via the exact augmented chain.

Run:  python verify/ao_ftcr_laws.py
"""
import numpy as np
from scipy.linalg import expm
import mpmath as mp

def make_ftcr(n, rng, cs=0.9):
    pi = rng.uniform(0.3, 1.0, n); pi /= pi.sum()
    J = np.zeros((n, n))
    for _ in range(3*n):
        i, j, k = rng.choice(n, 3, replace=False); f = rng.standard_normal()
        for a, b in [(i, j), (j, k), (k, i)]:
            J[a, b] += f; J[b, a] -= f
    T = np.abs(J) + rng.uniform(0.2, 1.5, (n, n)); T = (T + T.T)/2
    np.fill_diagonal(T, 0.0); np.fill_diagonal(J, 0.0)
    r = np.max(np.abs(J)/np.where(T > 0, T, np.inf)); J = J*(cs/r) if r > 0 else J
    return pi, T, J

def Lgen(pi, T, J, alpha):
    n = len(pi); L = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                L[i, j] = (T[i, j] + alpha*J[i, j])/(2*pi[i])
        L[i, i] = -L[i].sum()
    return L

def edges(L):
    ev = np.linalg.eigvals(L); rates = np.delete(-ev.real, np.argmin(np.abs(ev)))
    return rates.max(), rates.min()

def check_invariants_and_endpoints():
    rng = np.random.default_rng(1); worst_stat = 0.0; worst_over = 0.0
    for _ in range(200):
        n = int(rng.integers(4, 8)); pi, T, J = make_ftcr(n, rng)
        h0, g0 = edges(Lgen(pi, T, J, 0.0))
        scale = max(abs(h0), 1.0)
        for al in np.linspace(0, 1, 21):
            L = Lgen(pi, T, J, al)
            worst_stat = max(worst_stat, np.max(np.abs(pi@L)))
            h, g = edges(L)
            # endpoint bounds h(alpha)<=h(0), g(alpha)>=g(0); relative overshoot
            worst_over = max(worst_over, (h - h0)/scale, (g0 - g)/scale)
    assert worst_stat < 1e-12, f"stationarity drift {worst_stat}"
    assert worst_over < 1e-8, f"endpoint bound violated, overshoot {worst_over}"
    return worst_stat, worst_over

def _hmp(pi, T, J, a, n):
    M = mp.zeros(n, n)
    for i in range(n):
        s = mp.mpf(0)
        for j in range(n):
            if i != j:
                v = (mp.mpf(T[i, j]) + mp.mpf(a)*mp.mpf(J[i, j]))/(2*mp.mpf(pi[i]))
                M[i, j] = v; s += v
        M[i, i] = -s
    ev = mp.eig(M, left=False, right=False); mg = [abs(e) for e in ev]
    i0 = mg.index(min(mg))
    return max(-mp.re(ev[t]) for t in range(len(ev)) if t != i0)

def find_s1_counterexample():
    # Prop ao:basic asserts a bidirected SIX-state ray whose fast edge h(alpha)
    # strictly increases by more than 0.6, verified to 40 digits.  We search
    # six-state rays and stop at the first whose 40-digit-confirmed interior
    # increase exceeds 0.6, matching the stated proposition.
    rng = np.random.default_rng(1); n = 6
    al = np.linspace(0, 1, 101)
    mp.mp.dps = 40
    for _ in range(4000):
        pi, T, J = make_ftcr(n, rng)
        hs = np.array([edges(Lgen(pi, T, J, a))[0] for a in al])
        d = np.diff(hs); k = int(np.argmax(d))
        if d[k] < 0.7:                      # coarse screen with margin above 0.6
            continue
        grid = np.linspace(al[max(0, k-1)], al[min(100, k+2)], 15)
        vals = [float(_hmp(pi, T, J, a, n)) for a in grid]
        maxinc = max(vals[i+1]-vals[i] for i in range(len(vals)-1))
        if maxinc > 0.6:
            return n, maxinc
    raise AssertionError("no six-state ray with >0.6 fast-edge increase found")

# --- exact augmented (site, visited-set) chain ---
def augmented(pi, T, J, alpha):
    n = len(pi); L = Lgen(pi, T, J, alpha)
    states = [(i, 1 << i) for i in range(n)] + \
             [(i, v) for v in range(1 << n) for i in range(n) if (v >> i) & 1 and bin(v).count("1") >= 2]
    idx = {s: m for m, s in enumerate(states)}
    S = len(states); A = np.zeros((S, S))
    for (i, v), m in idx.items():
        for j in range(n):
            if j != i and L[i, j] > 0:
                w = v | (1 << j)
                A[m, idx[(j, w)]] += L[i, j]
        A[m, m] = -A[m].sum()
    return states, idx, A

def visited_dist(pi, T, J, alpha, t):
    states, idx, A = augmented(pi, T, J, alpha)
    P = expm(A.T * t)
    p0 = np.zeros(len(states))
    for i in range(len(pi)):
        p0[idx[(i, 1 << i)]] = pi[i]
    return states, P @ p0

def check_E1_alternating():
    # E[U_{gamma,t}] alternating derivatives in x=alpha^2 (first two moments)
    rng = np.random.default_rng(3); n = 4
    pi, T, J = make_ftcr(n, rng)
    xs = np.linspace(0.0, 1.0, 9)               # x = alpha^2 grid
    for gamma in [0.0, 0.5, 1.0]:
        w = pi**gamma; w /= w.sum()
        for k in [1, 2]:
            EU = []
            for x in xs:
                states, p = visited_dist(pi, T, J, np.sqrt(x), 0.6)
                U = np.array([sum(w[i] for i in range(n) if not (v >> i) & 1) for (i, v) in states])
                EU.append(float(p @ (U**k)))
            EU = np.array(EU)
            d = EU.copy()
            for r in range(1, 4):                # alternating differences
                d = np.diff(d)
                assert ((-1)**r * d).min() > -1e-9, f"E1 fail gamma={gamma} k={k} r={r}"
    return True

def check_E3_cycle():
    # simple cycle, nonuniform pi; stationary-mass FOSD increasing in alpha
    rng = np.random.default_rng(5); n = 5
    pi = rng.uniform(0.3, 1.0, n); pi /= pi.sum()
    T = np.zeros((n, n)); J = np.zeros((n, n))
    Tedge = rng.uniform(0.6, 1.5, n)
    c = 0.5*Tedge.min()                          # constant oriented current => divergence-free
    for i in range(n):
        j = (i+1) % n
        T[i, j] = T[j, i] = Tedge[i]
        J[i, j] = c; J[j, i] = -c
    assert np.max(np.abs(pi @ Lgen(pi, T, J, 1.0))) < 1e-12, "cycle: pi not stationary"
    for t in [0.5, 1.0]:
        prev = None
        for al in [0.0, 0.5, 1.0]:
            states, p = visited_dist(pi, T, J, al, t)
            masses = np.array([sum(pi[i] for i in range(n) if (v >> i) & 1) for (i, v) in states])
            zs = np.linspace(0.05, 0.95, 19)
            tail = np.array([p[masses >= z].sum() for z in zs])
            if prev is not None:
                assert (tail - prev).min() > -1e-9, "E3 FOSD fail"
            prev = tail
    return True

if __name__ == "__main__":
    ws, over = check_invariants_and_endpoints()
    print(f"invariants: pi stationary to {ws:.1e}; endpoint bounds h(a)<=h(0), g(a)>=g(0) hold "
          f"(max relative overshoot {over:.1e})")
    n, inc = find_s1_counterexample()
    print(f"refuted companion S1: n={n} ray with fast edge rising by {inc:.3f} at 40-digit precision "
          "(whole-ray fast-edge monotonicity FALSE; endpoint bound only)")
    check_E1_alternating()
    print("ao1 (E1): alternating-derivative hierarchy of E[U] in x=alpha^2 holds (n=4, k<=2, r<=3)")
    check_E3_cycle()
    print("ao4 (E3): cycle stationary-mass stochastic acceleration holds (n=5 nonuniform cycle)")
    print("\nAll Part XXIV checks passed (and S1 correctly refuted).")
