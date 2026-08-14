#!/usr/bin/env python3
"""Independent verification of the prime-cyclic programme (Conjectures 11-15).

Own FFT convolution code on Z/pZ; nothing shared with the bundle scripts.
"""
import math, sys
import numpy as np

LOG2 = math.log(2)
FLOOR = 0.5*LOG2

def H(a):
    a = a[a > 1e-300]
    return float(-(a*np.log(a)).sum())

def cyc_pow(a, m):
    z = np.fft.fft(a)
    q = np.fft.ifft(z**m).real
    q = np.clip(q, 0, None)
    return q/q.sum()

def dgauss(p, sigma, center=0):
    x = np.arange(p)
    d = (x - center + p//2) % p - p//2
    a = np.exp(-0.5*(d/sigma)**2)
    return a/a.sum()

def interval(p, L):
    a = np.zeros(p); a[:L] = 1.0/L
    return a

def is_prime(n):
    if n < 2: return False
    for q in range(2, int(n**0.5)+1):
        if n % q == 0: return False
    return True

def next_prime(n):
    while not is_prime(n): n += 1
    return n

def stage_doubling():
    """Conjecture 11 calibration: Gaussian at floor; two-bump pays extra ~ half log 2."""
    print("[doubling] gain - (1/2)log2 for discrete Gaussians (should -> 0):")
    for p in (next_prime(4001), next_prime(16001)):
        for s in (5, 12, 30, 60):
            a = dgauss(p, s)
            g = H(cyc_pow(a, 2)) - H(a)
            print(f"   p={p} sigma={s}: {g - FLOOR:+.6f}")
    print("[two-bump] gain for separated equal bumps (should -> log2 = 2x floor):")
    p = next_prime(16001)
    for s in (8, 20):
        for D in (p//3, p//2 - 100):
            a = 0.5*dgauss(p, s) + 0.5*dgauss(p, s, D)
            g = H(cyc_pow(a, 2)) - H(a)
            print(f"   sigma={s} sep={D}: gain={g:.6f}  vs log2={LOG2:.6f}")

def stage_mcopy():
    """Conjecture 14: H(mu^{*m}) - H(mu) >= (1/2) log m, mesoscopic regime."""
    p = next_prime(20011)
    fams = [("gauss8", dgauss(p, 8)), ("gauss25", dgauss(p, 25)),
            ("interval60", interval(p, 60)),
            ("geom", None), ("skew", None), ("bimix", None)]
    x = np.arange(p)
    d = (x + p//2) % p - p//2
    g = np.exp(-np.abs(d)/9.0); fams[3] = ("dLaplace9", g/g.sum())
    sk = np.exp(-np.where(d >= 0, d/5.0, -d/25.0)); fams[4] = ("skew", sk/sk.sum())
    bi = 0.7*dgauss(p, 10) + 0.3*dgauss(p, 10, 300); fams[5] = ("bimix", bi/bi.sum())
    print("[m-copy] excess gain - (1/2)log m (should be >= 0 up to numeric):")
    worst = 1e9
    for name, a in fams:
        row = f"   {name}:"
        for m in (2, 3, 4, 5, 7, 10):
            ex = H(cyc_pow(a, m)) - H(a) - 0.5*math.log(m)
            worst = min(worst, ex)
            row += f"  m={m}:{ex:+.4f}"
        print(row)
    print(f"   minimum excess across families/m: {worst:+.6f}")
    # adversarial mini-search: 3-parameter mixture minimizing m=3 excess
    rng = np.random.default_rng(3)
    best = 1e9; arg = None
    for _ in range(300):
        s1 = rng.uniform(3, 40); w = rng.uniform(0.05, 0.95); sep = int(rng.uniform(0, 2000))
        a = w*dgauss(p, s1) + (1-w)*dgauss(p, s1, sep)
        ex = H(cyc_pow(a, 3)) - H(a) - 0.5*math.log(3)
        if ex < best: best, arg = ex, (round(s1,1), round(w,2), sep)
    print(f"   adversarial m=3 mixture search (300 draws): min excess {best:+.6f} at (sigma,w,sep)={arg}")

def stage_wrap():
    """Conjecture 13: TV to discretized circle heat kernel + entropy limit."""
    def qpt(p, t):
        j = np.fft.fftfreq(p)*p
        coef = np.exp(-2*math.pi**2*t*j**2)
        q = np.fft.ifft(coef).real
        q = np.clip(q, 0, None)
        return q/q.sum()
    def rel_ent_target(t, N=200001):
        u = np.arange(N)/N
        th = np.zeros(N)
        for j in range(1, 60):
            th += 2*math.exp(-2*math.pi**2*t*j*j)*np.cos(2*math.pi*j*u)
        th += 1.0
        th = np.clip(th, 1e-300, None)
        return float(np.mean(th*np.log(th)))
    print("[wrap] Gaussian input: TV(mu^{*m}, q_{p,t}) and entropy vs target:")
    for t in (0.02, 0.1, 0.5):
        row = f"   t={t}:"
        for p, s in ((1009, 15), (4001, 25), (16001, 40)):
            p = next_prime(p)
            m = max(1, round(t*p*p/s**2))
            teff = m*s*s/p/p
            a = dgauss(p, s)
            conv = cyc_pow(a, m)
            tv = 0.5*float(np.abs(conv - qpt(p, teff)).sum())
            ent_def = math.log(p) - H(conv)
            row += f"  p={p}: TV={tv:.2e} def={ent_def:.5f}/{rel_ent_target(teff):.5f}"
        print(row)
    # non-Gaussian span-1 aperiodic input: lazy +-1 walk step
    print("[wrap] lazy walk input (1/4,1/2,1/4): TV to discretized heat kernel:")
    for p in (next_prime(1009), next_prime(4001)):
        s2 = 0.5  # variance of the step
        for t in (0.05, 0.3):
            m = round(t*p*p/s2)
            a = np.zeros(p); a[0] = 0.5; a[1] = 0.25; a[p-1] = 0.25
            conv = cyc_pow(a, m)
            teff = m*s2/p/p
            tv = 0.5*float(np.abs(conv - qpt(p, teff)).sum())
            print(f"   p={p} t={teff:.3f} (m={m}): TV={tv:.3e}")

def stage_monotone():
    """Conjecture 15: H(mu^{*(m+1)}) - H(mu^{*m}) >= (1/2)log((m+1)/m) - o(1/m),
    log-concave input, pre-wrap."""
    p = 2_000_003
    x = np.arange(p)
    d = (x + p//2) % p - p//2
    fams = []
    g = np.exp(-np.abs(d)/7.0); fams.append(("dLaplace7", g/g.sum(), 98.0))
    g2 = np.exp(-0.5*(d/10.0)**2); fams.append(("gauss10", g2/g2.sum(), 100.0))
    tri = np.clip(15 - np.abs(d), 0, None); fams.append(("triangle15", tri/tri.sum(), 37.5))
    print(f"[monotone] p={p}; margin m*(step - halflog((m+1)/m)); negative = violation-ish:")
    ms = [1, 2, 3, 5, 8, 16, 32, 64, 128, 256, 512, 1000]
    for name, a, var in fams:
        z = np.fft.fft(a)
        Hs = {}
        for m in ms + [m+1 for m in ms]:
            q = np.fft.ifft(z**m).real
            q = np.clip(q, 0, None); q /= q.sum()
            Hs[m] = H(q)
        row = f"   {name} (max wrap ratio {(ms[-1]+1)*var/p**2:.1e}):"
        worst = 1e9
        for m in ms:
            step = Hs[m+1] - Hs[m]
            margin = m*(step - 0.5*math.log((m+1)/m))
            worst = min(worst, margin)
            if m in (1, 8, 64, 512, 1000): row += f"  m={m}:{margin:+.4f}"
        print(row + f"   worst scaled margin: {worst:+.5f}")

if __name__ == "__main__":
    import time
    t0 = time.time()
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "a"): stage_doubling()
    if which in ("all", "b"): stage_mcopy()
    if which in ("all", "c"): stage_wrap()
    if which in ("all", "d"): stage_monotone()
    print(f"done in {time.time()-t0:.1f}s")
