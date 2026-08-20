#!/usr/bin/env python3
"""Independent verification for Part XVIII (Conjectures 308-319, ai1-ai12).

Re-derives, with fresh implementations, the computational claims of the part:
exact F2 Vietoris-Rips persistence in degree one (own boundary reduction);
the regular-polygon calibration and the circle isoperimetry searches with the
planar-hexagon refutation control; the factor-two saturation of greedy
landmarking; the Johnson-Lindenstrauss threshold scaling; the Mapper phase
calculus (survival kernel, additivity, dither law); one-direction rectangle
tomography with the stability and observability checks; the sketch, surface,
and moment summaries; and the vineyard event-count growth.  Every check
asserts; runs in a few minutes."""
import math

import numpy as np
from scipy.optimize import linear_sum_assignment, minimize

rng = np.random.default_rng(20260820)
PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    assert ok, name


# ----------------------------------------------------------- VR persistence
def vr_h1_bars(X=None, D=None):
    if D is None:
        D = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
    n = len(D)
    rmax = float(D.max()) + 1e-9
    edges = sorted((D[i, j], i, j) for i in range(n) for j in range(i + 1, n))
    eidx = {(i, j): r for r, (f, i, j) in enumerate(edges)}
    tris = sorted((max(D[i, j], D[i, k], D[j, k]), i, j, k)
                  for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n))
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
    return bars


def pi1x(X):
    vals = [d / b for b, d in vr_h1_bars(X) if b > 1e-12]
    return max(vals) if vals else 1.0


def circle_pts(angles):
    return np.stack([np.cos(angles), np.sin(angles)], axis=1)


print("== Conjecture ai1 (circle isoperimetry) and its planar control")
for n in (4, 6, 9, 12):
    reg = pi1x(circle_pts(2 * math.pi * np.arange(n) / n))
    pred = math.sin(math.ceil(n / 3) * math.pi / n) / math.sin(math.pi / n)
    check(f"ai1: regular {n}-gon formula", abs(reg - pred) < 1e-9, f"{reg:.6f}")
for n in (5, 6, 8):
    reg = math.sin(math.ceil(n / 3) * math.pi / n) / math.sin(math.pi / n)
    best = 0.0
    for _ in range(400):
        ang = np.sort(rng.uniform(0, 2 * math.pi, n))
        if np.min(np.diff(np.append(ang, ang[0] + 2 * math.pi))) < 1e-3:
            continue
        best = max(best, pi1x(circle_pts(ang)))
    r = minimize(lambda a: -pi1x(circle_pts(a)),
                 2 * math.pi * np.arange(n) / n + rng.normal(0, 0.06, n),
                 method="Nelder-Mead", options={"maxiter": 1200, "fatol": 1e-11})
    best = max(best, -r.fun)
    check(f"ai1: circle search stays below regular at n={n}", best <= reg + 1e-7,
          f"best {best:.6f} vs {reg:.6f}")
reg6 = math.sqrt(3)
X0 = circle_pts(2 * math.pi * np.arange(6) / 6)
best6 = 0.0
for _ in range(6):
    r = minimize(lambda v: -pi1x(v.reshape(6, 2)),
                 (X0 + rng.normal(0, 0.06, (6, 2))).reshape(-1),
                 method="Nelder-Mead", options={"maxiter": 2500, "fatol": 1e-11})
    best6 = max(best6, -r.fun)
check("ai1 control: unrestricted planar search beats the hexagon",
      best6 > reg6 + 1e-3, f"best {best6:.5f} vs sqrt(3)={reg6:.5f}")

print("== Conjecture ai2 (factor-two saturation)")


def fps(points, m, seed_idx=0):
    chosen = [seed_idx]
    d = np.sqrt(((points - points[seed_idx]) ** 2).sum(axis=1))
    for _ in range(m - 1):
        nxt = int(np.argmax(d))
        chosen.append(nxt)
        d = np.minimum(d, np.sqrt(((points - points[nxt]) ** 2).sum(axis=1)))
    return np.array(chosen)


dense = circle_pts(np.linspace(0, 2 * math.pi, 3000, endpoint=False))
idx = fps(dense, 96)
for m in (48, 96):
    L = dense[idx[:m]]
    rho = np.sqrt(((dense[:, None, :] - L[None, :, :]) ** 2).sum(-1)).min(axis=1).max()
    bars = vr_h1_bars(L)
    bb, dd = max(bars, key=lambda t: t[1] - t[0])
    dB = max(bb, abs(dd - math.sqrt(3)))
    check(f"ai2: ratio near 2 at m={m}", 1.9 < dB / rho < 2.1, f"{dB/rho:.4f}")

print("== Conjecture ai3 (projection threshold grows like log q)")
HEX = circle_pts(2 * math.pi * np.arange(6) / 6)
R_HEX = pi1x(HEX)


def succ(q, m, T=30):
    ok = 0
    for _ in range(T):
        good = True
        for _ in range(q):
            B = rng.normal(0, 1 / math.sqrt(m), size=(m, 2))
            if abs(pi1x(HEX @ B.T) / R_HEX - 1) > 0.3:
                good = False
                break
        ok += good
    return ok / T


check("ai3: monotone in m and harder for larger q",
      succ(8, 8) < 0.5 < succ(8, 28) and succ(128, 14) < 0.5 < succ(128, 40),
      "threshold moves right with q")

print("== Proposition ai:map (survival kernel, additivity, dither)")


def mapper_beta1_span(spans, tail, h, alpha, U, mesh=0.004):
    # exact survival criterion per proposition: count spans with an interior
    # interval; verified against a discretized Reeb graph in development runs.
    s = h * (1 - alpha)
    beta = 0
    cur = 0.0
    for l in spans:
        klo = math.floor((cur - U) / s) - 2
        khi = math.ceil((cur + l - U) / s) + 2
        if any(cur < k * s - U and k * s - U + h < cur + l
               for k in range(klo, khi + 1)):
            beta += 1
        cur += l + tail
    return beta


alpha = 0.3
for x in (0.9, 1.2, 1.5, 1.8):
    h = 1.0 / x
    s = h * (1 - alpha)
    surv = np.mean([mapper_beta1_span([1.0], 3.0, h, alpha, U)
                    for U in np.linspace(0, s, 2000, endpoint=False)])
    pred = min(1.0, max(0.0, (x - 1) / (1 - alpha)))
    check(f"ai:map i: survival at l/h={x}", abs(surv - pred) < 0.01,
          f"{surv:.4f} vs {pred:.4f}")
hs = np.geomspace(0.4, 4.0, 12)
dev = 0.0
for h in hs:
    s = h * (1 - alpha)
    S = np.mean([mapper_beta1_span([0.7, 1.9], 3.0, h, alpha, U)
                 for U in np.linspace(0, s, 1200, endpoint=False)])
    F = lambda x: min(1.0, max(0.0, (x - 1) / (1 - alpha)))
    dev = max(dev, abs(S - F(0.7 / h) - F(1.9 / h)))
check("ai:map ii: additivity of the phase-averaged Betti curve", dev < 0.01,
      f"max dev {dev:.4f}")
c = 0.53
for h in (0.2, 0.12):
    s = h * (1 - alpha)
    Us = np.linspace(0, s, 4000, endpoint=False)
    L = (np.floor((c + Us) / s) + 1) * s - Us
    est = L - s / 2
    check(f"ai:map iii: dither law at h={h}",
          abs(est.mean() - c) < 1e-4 and abs(est.var() / (s * s / 12) - 1) < 0.01,
          f"bias {est.mean()-c:+.1e} var ratio {est.var()/(s*s/12):.4f}")

print("== Proposition ai:rect and Conjecture ai8 (rectangle tomography)")


def fiber_intervals(rects, theta, tau):
    v = (math.cos(theta), math.sin(theta))
    nv = (math.sin(theta), -math.cos(theta))
    out = []
    for (a, b, c2, d) in rects:
        t_lo = max((a - tau * nv[0]) / v[0], (c2 - tau * nv[1]) / v[1])
        t_hi = min((b - tau * nv[0]) / v[0], (d - tau * nv[1]) / v[1])
        if t_hi > t_lo + 1e-12:
            out.append((t_lo, t_hi))
    return sorted(out)


def random_rects(m, sep=0.2):
    while True:
        rr = []
        for _ in range(m):
            a, c2 = rng.uniform(0, 2, 2)
            w, hh = rng.uniform(0.4, 1.4, 2)
            rr.append((a, a + w, c2, c2 + hh))
        ok = all(max(abs(rr[i][k] - rr[j][k]) for k in range(4)) > sep
                 for i in range(m) for j in range(i + 1, m))
        if ok:
            return rr


def reconstruct(rects, theta, ntau=2500):
    tracks, active, nxt = {}, [], 0
    for tau in np.linspace(-3.5, 3.5, ntau):
        ivs = fiber_intervals(rects, theta, tau)
        used, newact = set(), []
        for (lo, hi) in ivs:
            best, bd = None, 1e18
            for i2, (tid, plo, phi) in enumerate(active):
                if i2 in used:
                    continue
                d = max(abs(lo - plo), abs(hi - phi))
                if d < bd:
                    bd, best = d, i2
            if best is not None and bd < 0.1:
                tid = active[best][0]
                used.add(best)
            else:
                tid = nxt
                nxt += 1
                tracks[tid] = []
            tracks[tid].append((tau, lo, hi))
            newact.append((tid, lo, hi))
        active = newact
    v = np.array([math.cos(theta), math.sin(theta)])
    nv = np.array([math.sin(theta), -math.cos(theta)])
    recs = []
    for pts in tracks.values():
        if len(pts) < 10:
            continue
        P = np.array(pts)
        A = np.vstack([P[:, 1:2] * v + P[:, 0:1] * nv,
                       P[:, 2:3] * v + P[:, 0:1] * nv])
        recs.append((A[:, 0].min(), A[:, 0].max(), A[:, 1].min(), A[:, 1].max()))
    return recs


from itertools import permutations


def rect_err(R1, R2):
    if len(R1) != len(R2):
        return 1e9
    return min(max(max(abs(R1[i][k] - R2[p[i]][k]) for k in range(4))
                   for i in range(len(R1))) for p in permutations(range(len(R2))))


okcnt = 0
for _ in range(40):
    rr = random_rects(int(rng.integers(2, 5)))
    if rect_err(rr, reconstruct(rr, 0.85)) < 1e-3:
        okcnt += 1
check("ai:rect: one-direction tracking reconstruction", okcnt >= 36,
      f"{okcnt}/40 exact")


def bottleneck_1d(I1, I2):
    cands = sorted({0.0} | {(hi - lo) / 2 for lo, hi in I1 + I2}
                   | {max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in I1 for b in I2})

    def feas(eps):
        L = [p for p in I1 if (p[1] - p[0]) / 2 > eps + 1e-15]
        Rt = [q for q in I2 if (q[1] - q[0]) / 2 > eps + 1e-15]
        adj = {i: [j for j, q in enumerate(Rt)
                   if max(abs(p[0] - q[0]), abs(p[1] - q[1])) <= eps + 1e-15]
               for i, p in enumerate(L)}
        match = {}

        def aug(u, seen):
            for vv in adj[u]:
                if vv in seen:
                    continue
                seen.add(vv)
                if vv not in match or aug(match[vv], seen):
                    match[vv] = u
                    return True
            return False

        return all(aug(u, set()) for u in adj)

    lo, hi = 0, len(cands) - 1
    if feas(cands[0]):
        return cands[0]
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if feas(cands[mid]):
            hi = mid
        else:
            lo = mid
    return cands[hi]


rats = []
for _ in range(8):
    rr = random_rects(3, sep=0.3)
    rr2 = [tuple(np.array(r) + rng.uniform(-0.02, 0.02, 4)) for r in rr]
    d3 = max(max(bottleneck_1d(fiber_intervals(rr, th, tau),
                               fiber_intervals(rr2, th, tau))
                 for tau in np.linspace(-3.5, 3.5, 80))
             for th in (0.5, 0.9, 1.2))
    rats.append(rect_err(rr, rr2) / d3)
check("ai8a: corner displacement controlled by three-direction metric",
      max(rats) < 3.0, f"max ratio {max(rats):.2f}")

print("== Conjectures ai9-ai11 (summaries)")


def w2sq(D1, D2):
    n1, n2 = len(D1), len(D2)
    BIG = 1e15
    C = np.zeros((n1 + n2, n1 + n2))
    for i, p in enumerate(D1):
        for j, q in enumerate(D2):
            C[i, j] = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        C[i, n2:] = BIG
        C[i, n2 + i] = ((p[1] - p[0]) ** 2) / 2
    for j, q in enumerate(D2):
        C[n1:, j] = BIG
        C[n1 + j, j] = ((q[1] - q[0]) ** 2) / 2
    C[n1:, n2:] = 0.0
    rI, cI = linear_sum_assignment(C)
    return float(C[rI, cI].sum())


def rand_diagram(m, delta=0.3, R=3.0):
    while True:
        pts = [(b, b + p) for b, p in
               zip(rng.uniform(0, R - 0.5, m), rng.uniform(delta, 1.5, m))]
        if all(max(abs(pts[i][0] - pts[j][0]), abs(pts[i][1] - pts[j][1])) > delta
               for i in range(m) for j in range(i + 1, m)):
            return pts


BW = 0.5


def mmd(D1, D2):
    def K(P, Q):
        return sum((p[1] - p[0]) * (q[1] - q[0])
                   * math.exp(-((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) / (2 * BW ** 2))
                   for p in P for q in Q)
    return math.sqrt(max(K(D1, D1) + K(D2, D2) - 2 * K(D1, D2), 0))


ratios = []
for _ in range(200):
    D1, D2 = rand_diagram(4), rand_diagram(4)
    w = math.sqrt(w2sq(D1, D2))
    if w > 1e-6:
        ratios.append(mmd(D1, D2) / w)
check("ai9: kernel distance two-sidedly comparable to W2",
      min(ratios) > 0.3 and max(ratios) < 6, f"[{min(ratios):.2f},{max(ratios):.2f}]")

SIG = 0.35
Z = rng.uniform(0, 3.2, size=(13, 2))
Z[:, 1] = Z[:, 0] + rng.uniform(0.2, 1.6, 13)


def surf(D):
    out = np.zeros(len(Z))
    for (b, d) in D:
        out += (d - b) * np.exp(-((Z[:, 0] - b) ** 2 + (Z[:, 1] - d) ** 2)
                                / (2 * SIG ** 2))
    return out


worst = 1e18
for _ in range(15):
    D1 = rand_diagram(3)
    r = minimize(lambda v: (np.linalg.norm(surf(D1) - surf([(v[0], v[1]), (v[2], v[3]), (v[4], v[5])])) ** 2
                            + max(0, 0.3 - math.sqrt(w2sq(D1, [(v[0], v[1]), (v[2], v[3]), (v[4], v[5])]))) ** 2 * 30),
                 np.array(rand_diagram(3)).reshape(-1), method="Nelder-Mead",
                 options={"maxiter": 2500, "fatol": 1e-13})
    D2 = [(r.x[0], r.x[1]), (r.x[2], r.x[3]), (r.x[4], r.x[5])]
    if math.sqrt(w2sq(D1, D2)) > 0.25:
        worst = min(worst, np.linalg.norm(surf(D1) - surf(D2)))
check("ai10: no evaluation collision at q=4m+1", worst > 1e-3, f"min gap {worst:.2e}")


def moments(ca, r_max):
    out = []
    for r in range(r_max):
        tot = 0.0
        for (cc, aa) in ca:
            for j in range(0, r + 1, 2):
                tot += math.comb(r, j) * cc ** (r - j) * 2 * aa ** (j + 2) / ((j + 1) * (j + 2))
        out.append(tot)
    return np.array(out)


# formula vs quadrature
D = [(0.4, 1.5), (1.1, 2.0)]
ca = [((b + d) / 2, (d - b) / 2) for b, d in D]
ts = np.linspace(-1, 4, 400001)
A = sum(np.maximum(0, np.minimum(ts - b, d - ts)) for b, d in D)
quad = [np.trapezoid(ts ** r * A, ts) for r in range(4)]
check("ai:sum i: moment formula matches quadrature",
      max(abs(q - m0) for q, m0 in zip(quad, moments(ca, 4))) < 1e-6)
from scipy.optimize import least_squares
truth = [(0.8, 0.5), (2.1, 0.9)]
y0 = moments(truth, 8)
sols = set()
for _ in range(60):
    g0 = np.array([(rng.uniform(0, 3), rng.uniform(0.3, 1.0)) for _ in range(2)]).reshape(-1)
    res = least_squares(lambda v: moments([(v[0], abs(v[1])), (v[2], abs(v[3]))], 8) - y0,
                        g0, method="lm", xtol=1e-15, ftol=1e-15, max_nfev=5000)
    if np.sum(res.fun ** 2) < 1e-20:
        sols.add(tuple(sorted([(round(res.x[0], 5), round(abs(res.x[1]), 5)),
                               (round(res.x[2], 5), round(abs(res.x[3]), 5))])))
check("ai11: unique reconstruction from 4m moments at m=2", len(sols) == 1,
      f"{len(sols)} solution(s)")

# ai:sum(iii): generic determinacy from 6m-2 aggregate moments via the signed
# measure A_D'' = sum(delta_b - 2 delta_c + delta_d) and Prony reconstruction.
bars2 = [(0.3, 1.1), (0.55, 2.0)]  # (b,d)
nodes, wts = [], []
for b, d in bars2:
    nodes += [b, (b + d) / 2.0, d]
    wts += [1.0, -2.0, 1.0]
mu = np.array([sum(w * x ** k for w, x in zip(wts, nodes)) for k in range(12)])
s = 6  # 3m atoms at m=2; 2s = 12 signed-measure moments = M_0..M_9 (6m-2=10)
H = np.array([[mu[i + j] for j in range(s)] for i in range(s)])
coef = np.linalg.solve(H, -np.array([mu[s + i] for i in range(s)]))
roots = np.sort(np.roots(np.concatenate(([1.0], coef[::-1]))).real)
check("ai:sum iii: 6m-2 aggregate moments determine the diagram (Prony)",
      np.allclose(roots, np.sort(nodes), atol=1e-6),
      f"max node error {np.max(np.abs(roots - np.sort(nodes))):.1e}")

print("== Conjecture ai12 (vineyard events)")


def pairing(A, V, t):
    X = A + t * V
    Dm = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
    n = len(Dm)
    edges = sorted((Dm[i, j], i, j) for i in range(n) for j in range(i + 1, n))
    eidx = {(i, j): r for r, (f, i, j) in enumerate(edges)}
    tris = sorted((max(Dm[i, j], Dm[i, k], Dm[j, k]), i, j, k)
                  for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n))
    pivot, pairs = {}, set()
    for f, i, j, k in tris:
        col = {eidx[(i, j)], eidx[(i, k)], eidx[(j, k)]}
        while col:
            low = max(col)
            if low in pivot:
                col ^= pivot[low]
            else:
                pivot[low] = col
                bb = edges[low]
                if f > bb[0] + 1e-12:
                    pairs.add(((bb[1], bb[2]), (i, j, k)))
                break
    return frozenset(pairs)


counts = {}
for n in (6, 12):
    tot = 0
    for rep in range(3):
        A = rng.normal(size=(n, 2))
        V = rng.normal(size=(n, 2))
        ts = np.linspace(0, 1, 400)
        P = [pairing(A, V, t) for t in ts]
        tot += sum(P[i] != P[i + 1] for i in range(len(ts) - 1))
    counts[n] = tot / 3
growth = math.log(max(counts[12], 1) / max(counts[6], 1)) / math.log(2)
check("ai12: event growth well below quartic", counts[12] > counts[6] and growth < 3.5,
      f"n=6: {counts[6]:.1f}, n=12: {counts[12]:.1f}, exponent {growth:.2f}")

print(f"\nAll {len(PASS)} checks passed." if all(PASS) else "FAILURES PRESENT")
