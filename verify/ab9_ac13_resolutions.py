#!/usr/bin/env python3
"""Certification of the resolutions of Conjectures 205 (ab9) and 229 (ac13).

205: the 14-vertex tree with a degree-five hub, five leaves, diameter ten has
normalized distance-signless-Laplacian Shannon entropy strictly below P_14.
229: the lazy-walk-plus-rare-jump family satisfies the deposited hypotheses
while its wrap limit carries a compound-Poisson factor; mode three separates.
"""
import math
import numpy as np

def check_205():
    from mpmath import mp, mpf, matrix, eigsy, log
    mp.dps = 60
    def HQ1(edges, n):
        adj = {i: [] for i in range(n)}
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        D = [[0]*n for _ in range(n)]
        for s0 in range(n):
            dist = {s0: 0}; q = [s0]
            while q:
                nq = []
                for x in q:
                    for y in adj[x]:
                        if y not in dist: dist[y] = dist[x]+1; nq.append(y)
                q = nq
            for j in range(n): D[s0][j] = dist[j]
        t = [sum(r) for r in D]; W2 = sum(t)
        Q = matrix(n, n)
        for i in range(n):
            for j in range(n):
                Q[i, j] = mpf(D[i][j]) + (mpf(t[i]) if i == j else 0)
        H = mpf(0)
        for lam in eigsy(Q, eigvals_only=True):
            p = lam/W2
            if p > mpf(10)**-50: H -= p*log(p)
        return H
    T = [(0,1),(0,2),(1,6),(1,11),(1,12),(1,13),(2,3),(3,4),(4,5),(6,7),(7,8),(8,9),(9,10)]
    P = [(i, i+1) for i in range(13)]
    hT, hP = HQ1(T, 14), HQ1(P, 14)
    assert hT < hP and abs(float(hT-hP) + 3.1535496e-5) < 1e-11
    print(f"205: counterexample tree beats path by {float(hP-hT):.6e}: resolved false confirmed")

def check_229(p=10007, t=0.1):
    L = int(math.isqrt(p)); a = p//3; eps = L/a**2
    step = np.zeros(p); step[0] = 0.5; step[1] = 0.25; step[p-1] = 0.25
    Y = np.fft.ifft(np.fft.fft(step)**L).real; Y = np.clip(Y, 0, None); Y /= Y.sum()
    Z = np.zeros(p); Z[0] = 1-eps; Z[a] = eps/2; Z[p-a] = eps/2
    X = np.fft.ifft(np.fft.fft(Y)*np.fft.fft(Z)).real; X = np.clip(X, 0, None); X /= X.sum()
    xs = np.arange(p); d = (xs+p//2) % p - p//2
    var = float((X*d**2).sum())
    m = int(round(t*p*p/var)); teff = m*var/p/p
    conv = np.fft.ifft(np.fft.fft(X)**m).real; conv = np.clip(conv, 0, None); conv /= conv.sum()
    phic = np.fft.fft(conv)
    j = 3
    actual = abs(phic[j])
    heat = math.exp(-2*math.pi**2*teff*j*j)
    pred = math.exp(-(2*math.pi**2*teff/3)*j*j)*math.exp(m*eps*(math.cos(2*math.pi*j*a/p)-1))
    assert abs(actual-pred) < 1e-4 and actual > 10*heat
    print(f"229: mode-3 coefficient {actual:.6f} matches jump prediction {pred:.6f}, "
          f"separated from heat kernel {heat:.2e}: resolved false confirmed")

if __name__ == "__main__":
    check_205(); check_229()
