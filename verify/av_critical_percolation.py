"""Independent verification for Part XXXI (Conjectures 440-459): percolation at the
critical point in every dimension.  Calibrations of the proved layer of Proposition
av:basic and of the finite anchors quoted in the Significance paragraphs; nothing here
tests an asymptotic statement.

  1. Proposition av:basic(iv): 1-(1-p_c(d))^{2d} -> 1-1/e using the numerical critical
     points p_c(Z^d) for d = 2..13 and Kesten's asymptotics.
  2. Critical one-arm probabilities pi_d(n) on Z^d for d = 2..5, n <= 4, at the numerical
     critical points (n = 1 exact): dimensional monotonicity (Conjecture av2(i)).
  3. Z^2 at p = 1/2: pi_2(n) for n <= 128 and the effective exponent against 5/48; the
     lower bound pi(n/2) >= (2d p_c |dLambda_n|)^{-1/2} of Proposition av:basic(iii); the
     BK bound tau(0,x) <= pi(|x|/2)^2 and the two-arm ratio tau(0,x)/pi(|x|)^2
     (Conjecture av8).
  4. Z^3 at p_c = 0.24881182: pi_3(n) for n <= 32 and the effective exponent.
  5. Finite-volume curves theta_n(p) on Z^2 for n <= 256: the finite-cluster one-arm
     probability is largest at p = 1/2 (Conjecture av3), with theta approximated from
     above by theta_256.
  6. Finite-size thresholds p_n(eps pi_2(n)) on Z^2 (Proposition av:basic(ii), Conjecture
     av4): below 1/2, increasing towards it with the planar rate n^{-3/4}.
  7. Slab critical points (Conjecture av5): crossing-method estimates of p_c(Z^2 x [0,k])
     for k in {1,2,4,8}, decreasing towards p_c(Z^3).

Run:  python3 verify/av_critical_percolation.py   (a few minutes)
"""
import sys, math, itertools
import numpy as np

PASS = []
def check(name, ok, detail=""):
    PASS.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(20260905)

# numerical critical points of nearest-neighbour bond percolation on Z^d (Mertens-Moore 2018 and earlier)
PC = {2: 0.5, 3: 0.24881182, 4: 0.1601314, 5: 0.118172, 6: 0.0942019, 7: 0.0786752, 8: 0.06770839,
      9: 0.05949601, 10: 0.05309258, 11: 0.04794969, 12: 0.04372386, 13: 0.04018762}

# ---------------------------------------------------------------- percolation on a box via sparse connected components
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

def box_clusters(dims, p):
    """Bond percolation on prod_i {0..dims[i]-1}; returns (labels, coords)."""
    N = int(np.prod(dims)); idx = np.arange(N)
    coords = np.stack(np.unravel_index(idx, dims), axis=1)
    srcs, dsts = [], []
    stride = 1
    for ax in range(len(dims) - 1, -1, -1):
        mask = coords[:, ax] < dims[ax] - 1
        src = idx[mask]; dst = src + stride
        opn = rng.random(src.size) < p
        srcs.append(src[opn]); dsts.append(dst[opn])
        stride *= dims[ax]
    src = np.concatenate(srcs); dst = np.concatenate(dsts)
    g = coo_matrix((np.ones(src.size, dtype=np.int8), (src, dst)), shape=(N, N))
    _, labels = connected_components(g, directed=False)
    return labels, coords

def one_arm_probs(dim, n, p, samples):
    """Estimate P_p(0 <-> dLambda_m) for m = 1..n on the box Lambda_n (side 2n+1)."""
    L = 2 * n + 1; hits = np.zeros(n + 1)
    for _ in range(samples):
        roots, coords = box_clusters((L,) * dim, p)
        c0 = roots[(L ** dim) // 2]
        dist = np.max(np.abs(coords - n), axis=1)
        same = roots == c0
        reach = np.max(dist[same])
        hits[1:reach + 1] += 1
    return hits[1:] / samples

# ---------------------------------------------------------------- 1
vals = [1 - (1 - PC[d]) ** (2 * d) for d in sorted(PC)]
target = 1 - math.exp(-1)
check("Prop (iv): 1-(1-p_c)^{2d} approaches 1-1/e (d=2..13), monotone decreasing",
      all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)) and abs(vals[-1] - target) < 0.03 and vals[-1] > target,
      f"d=2: {vals[0]:.4f}, d=13: {vals[-1]:.4f}, limit {target:.4f}")

# ---------------------------------------------------------------- 2: dimensional monotonicity, n <= 4
pi_small = {}
for d, samples in ((2, 20000), (3, 6000), (4, 1500), (5, 400)):
    pi_small[d] = one_arm_probs(d, 4, PC[d], samples)
    print(f"   pi_{d}(n), n=1..4: " + ", ".join(f"{v:.4f}" for v in pi_small[d]) + f"  (exact n=1: {1-(1-PC[d])**(2*d):.4f})")
ok = True
for n in range(4):
    for d in (2, 3, 4):
        if not pi_small[d][n] > pi_small[d + 1][n] + 0.02: ok = False
check("Conjecture av2(i): pi_{d+1}(n) < pi_d(n) for d=2..4, n=1..4 (margin > 0.02)", ok)

# ---------------------------------------------------------------- 3: Z^2 at 1/2
def arm_and_twopoint_2d(n, p, samples):
    L = 2 * n + 1; N = L * L; hits = np.zeros(n + 1); tp = np.zeros(n + 1); cnt = 0
    for _ in range(samples):
        roots, coords = box_clusters((L, L), p)
        c0 = roots[N // 2]; same = roots == c0
        dist = np.max(np.abs(coords - n), axis=1)
        hits[1:np.max(dist[same]) + 1] += 1
        # two-point function to the axis point (n+m, n) for m = 1..n
        for m in range(1, n + 1):
            tp[m] += same[(n) * L + (n + m)]
    return hits[1:] / samples, tp[1:] / samples
pi2, tau2 = arm_and_twopoint_2d(128, 0.5, 400)
ns = np.array([8, 16, 32, 64, 128]); vals2 = pi2[ns - 1]
slope = -np.polyfit(np.log(ns), np.log(vals2), 1)[0]
check("Z^2, p=1/2: effective one-arm exponent on n in [8,128] within 0.04 of 5/48", abs(slope - 5 / 48) < 0.04, f"slope {slope:.3f}, pi(128)={vals2[-1]:.3f}")
lb = [ (2 * 2 * 0.5 * (2 * (2 * n + 1))) ** -0.5 for n in ns ]   # |dLambda_n| <= 2d(2n+1)^{d-1} with d=2
check("Prop (iii): pi(n/2) >= (2d p_c |dLambda_n|)^{-1/2} on Z^2 data", all(pi2[n // 2 - 1] >= l for n, l in zip(ns, lb)), f"e.g. n=128: pi(64)={pi2[63]:.3f} >= {lb[-1]:.3f}")
bk_ok = all(tau2[m - 1] <= pi2[m // 2 - 1] ** 2 + 0.03 for m in (8, 16, 32, 64))
ratios = [tau2[m - 1] / pi2[m - 1] ** 2 for m in (8, 16, 32, 64)]
check("Prop (iii): tau(0,x) <= pi(|x|/2)^2 on Z^2 data (axis points, tolerance 0.03)", bk_ok, "ratios tau/pi(|x|)^2: " + ", ".join(f"{r:.2f}" for r in ratios))
check("Conjecture av8: two-arm ratio tau(0,x)/pi(|x|)^2 bounded on Z^2 (between 0.1 and 2)", all(0.1 < r < 2 for r in ratios))

# ---------------------------------------------------------------- 4: Z^3
pi3 = one_arm_probs(3, 32, PC[3], 300)
ns3 = np.array([4, 8, 16, 32]); v3 = pi3[ns3 - 1]
slope3 = -np.polyfit(np.log(ns3), np.log(v3), 1)[0]
check("Z^3 at p_c: effective one-arm exponent on n in [4,32] between 0.35 and 0.60", 0.35 < slope3 < 0.60, f"slope {slope3:.3f}, pi_3: " + ", ".join(f"{v:.3f}" for v in v3))
print(f"   pi_2(n): " + ", ".join(f"{pi2[n-1]:.3f}" for n in ns))

# ---------------------------------------------------------------- 5: finite-volume curves on Z^2
def theta_curve(n, ps, samples):
    L = 2 * n + 1; N = L * L; out = []
    for p in ps:
        h = 0
        for _ in range(samples):
            roots, coords = box_clusters((L, L), p)
            c0 = roots[N // 2]
            dist = np.max(np.abs(coords - n), axis=1)
            h += np.max(dist[roots == c0]) == n
        out.append(h / samples)
    return np.array(out)
grid = np.array([0.40, 0.42, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.50, 0.51, 0.52, 0.53, 0.55, 0.58, 0.62, 0.66, 0.70])
curves = {}
for n, s_ in ((8, 3000), (16, 1500), (32, 600), (64, 250), (128, 120), (256, 40)):
    curves[n] = theta_curve(n, grid, s_)
# Conjecture av3(ii): the finite-cluster one-arm probability P_p(0<->dLambda_n, |C|<infinity) is largest at p_c.
# theta_256 approximates theta from above, so theta_n - theta_256 is a lower bound for theta_n - theta; above p = 0.53
# the correlation length is below 60 and the approximation is close.
above = grid >= 0.53
viol = []
for n in (8, 16, 32, 64):
    f = curves[n] - curves[256]
    if np.max(f[above]) >= curves[n][grid == 0.50][0]: viol.append(n)
    print(f"   n={n}: theta_n(1/2)={curves[n][grid==0.50][0]:.3f}, max_(p>=0.53) [theta_n - theta_256] = {np.max(f[above]):.3f} at p={grid[above][np.argmax(f[above])]:.2f}")
check("Conjecture av3(ii): finite-cluster arm probability above p_c (p >= 0.53, theta from the 513-box) stays below theta_n(1/2), n=8..64", not viol, f"violations at n={viol}")
sup_info = []
for n in (8, 16, 32, 64):
    f = curves[n] - curves[256]; i = int(np.argmax(f))
    sup_info.append((n, grid[i], f[i], f[i] / curves[n][grid == 0.50][0]))
print("   argmax_p (theta_n - theta_256): " + "; ".join(f"n={n}: p={pm:.2f}, value {dv:.3f}, ratio to theta_n(1/2) {r:.2f}" for n, pm, dv, r in sup_info))
check("Conjecture av3(i): maximiser of theta_n - theta_256 lies within 0.05 of 1/2 and the value is at most theta_n(1/2)", all(abs(pm - 0.5) <= 0.05 and r <= 1.0 for _, pm, _, r in sup_info))

# ---------------------------------------------------------------- 6: finite-size thresholds at levels scaled with pi_2(n)
def threshold(n, eps):
    c = curves[n]
    for i in range(len(grid) - 1):
        if c[i] < eps <= c[i + 1]:
            return grid[i] + (grid[i + 1] - grid[i]) * (eps - c[i]) / (c[i + 1] - c[i])
    return np.nan
ns6 = [8, 16, 32, 64, 128]
thr = {f: [threshold(n, f * curves[n][grid == 0.50][0]) for n in ns6] for f in (0.5, 0.8)}
print("   p_n(0.5 pi(n)): " + ", ".join(f"{t:.3f}" for t in thr[0.5]) + " ; p_n(0.8 pi(n)): " + ", ".join(f"{t:.3f}" for t in thr[0.8]))
ok6 = all(t < 0.5 for t in thr[0.5] + thr[0.8]) and all(thr[0.5][i] <= thr[0.5][i + 1] + 0.005 for i in range(4)) and all(thr[0.8][i] <= thr[0.8][i + 1] + 0.005 for i in range(4))
check("Prop (ii)/av4(i): thresholds p_n(eps pi_2(n)) lie below 1/2 and increase towards it (eps=0.5,0.8, tolerance 0.005)", ok6)
gaps = [0.5 - t for t in thr[0.5]]
gslope = -np.polyfit(np.log(ns6), np.log(gaps), 1)[0]
check("Conjecture av4(i)/(iii): 1/2 - p_n(0.5 pi(n)) shrinks with an exponent within 0.3 of 3/4", abs(gslope - 0.75) < 0.3, f"gaps {', '.join(f'{g:.3f}' for g in gaps)}, slope {gslope:.2f}")

# ---------------------------------------------------------------- 7: slab critical points Z^2 x [0,k]
def slab_cross_prob(k, L, p, samples):
    """Probability that an open path crosses an L x L x (k+1) slab from x=0 to x=L-1."""
    hits = 0
    for _ in range(samples):
        roots, coords = box_clusters((L, L, k + 1), p)
        left = set(roots[coords[:, 0] == 0].tolist()); right = set(roots[coords[:, 0] == L - 1].tolist())
        hits += bool(left & right)
    return hits / samples
def slab_pc(k, L=32, samples=120):
    lo, hi = 0.24, 0.50
    for _ in range(9):
        mid = (lo + hi) / 2
        if slab_cross_prob(k, L, mid, samples) < 0.5: lo = mid
        else: hi = mid
    return (lo + hi) / 2
slab = {k: slab_pc(k) for k in (1, 2, 4, 8)}
print("   slab p_c estimates: " + ", ".join(f"k={k}: {v:.3f}" for k, v in slab.items()))
scaled = [ (k ** (1 / 0.876)) * (slab[k] - PC[3]) for k in (1, 2, 4, 8) ]
check("Conjecture av5: slab thresholds decrease in k towards p_c(Z^3)=0.2488 and k^{1/nu}(p_c(S_k)-p_c) varies by less than a factor 3",
      slab[1] > slab[2] > slab[4] > slab[8] > PC[3] and max(scaled) / min(scaled) < 3, "scaled: " + ", ".join(f"{s:.3f}" for s in scaled))

print(f"\n{sum(PASS)}/{len(PASS)} checks passed")
sys.exit(0 if all(PASS) else 1)
