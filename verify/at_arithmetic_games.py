"""Independent verification for Part XXIX (Conjectures 410-424): arithmetic games,
prime continuants and Hessian shadows.

Checks the proved anchors of Proposition at:basic and the finite calibrations quoted
in the Significance paragraphs, with code written independently of the source
diagnostics.  Exact rational arithmetic is used for the Legendre game certificates
and the character-sum identity; simulations are seeded.

  1. Local laws of continuants modulo p (density 1/(p+1); lag-two density g_p/(p+1)).
  2. Prime-continuant constant 2 log 2 and the lag-one pair factor 6/pi^2.
  3. Squarefree proxy density prod (1-1/(p(p+1))).
  4. Progression digit-set dimension: four-term expansion with the digamma term.
  5. Continuant avoidance dimension for p=7 (transfer operator on [0,1] x P^1(F_p)).
  6. Exact unit values of the Legendre half-box games (rational certificates).
  7. Circulant and antisymmetric game values (LP).
  8. Character-sum divisibility q | sum chi(F(P)) and |t| <= 7 for smooth quartics.
  9. Dual-curve identity #C^vee = #C - b_split + b_conj by counting tangent lines.
 10. Scale separation: Hankel sign games have sqrt(m) v of order one, full games do not.
 11. Quarter-box positivity for p = 3 mod 4 and half-box smallness; the half-box sign is
     asserted only in the class 7 mod 8 (calibration on four primes, not a sign theorem).
 12. Exact rational minimax certificate for the half box at p = 547 (class 3 mod 8): the
     value is positive, refuting the sign clause of Conjecture at15 as first deposited.
     The certificate (verify/data/at15_p547_certificate.json) is checked without any
     optimizer: the Legendre matrix is rebuilt and every primal and dual inequality is
     verified in exact arithmetic.

Run:  python3 verify/at_arithmetic_games.py
"""
import math, random, sys, itertools
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import eigvals
from scipy.optimize import brentq
import mpmath as mp
import sympy as sp

PASS = []
def check(name, ok, detail=""):
    PASS.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

random.seed(20260902); rng = np.random.default_rng(20260902)
try:
    import gmpy2
    def isprime(n): return bool(gmpy2.is_prime(n, 12))
except ImportError:
    def isprime(n): return sp.isprime(n)

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

# ---------------------------------------------------------------- 1-3: continuants
def continuants(bits, nmax):
    """Continuants q_1..q_nmax of a uniformly random dyadic rational with `bits` bits."""
    u = random.getrandbits(bits); v = 1 << bits
    q0, q1 = 1, 0; qs = []
    while len(qs) < nmax and u:
        d = v // u; v, u = u, v - d * u
        q0, q1 = d * q0 + q1, q0; qs.append(q0)
    return qs if len(qs) == nmax else None

M, NMAX = 2500, 150
SP = primes_upto(10000); PRIM = 1
for p in SP: PRIM *= p
div = {p: 0 for p in (2, 3, 5)}; div2 = {p: 0 for p in (2, 3, 5)}; tot = 0
cnt_prime = [0] * (NMAX + 1); cnt_pair = [0] * (NMAX + 1); sqf = 0; sqf_tot = 0
for _ in range(M):
    qs = continuants(int(3.7 * NMAX) + 200, NMAX)
    if qs is None: continue
    prev = False
    for k, q in enumerate(qs, start=1):
        if k >= 20:
            tot += 1
            for p in div:
                if q % p == 0:
                    div[p] += 1
                    if k + 2 <= NMAX and qs[k + 1] % p == 0: div2[p] += 1
        if 40 <= k <= NMAX:
            pr = isprime(q); cnt_prime[k] += pr
            if pr and prev: cnt_pair[k] += 1
            prev = pr
            g = math.gcd(q, PRIM); sqf_tot += 1
            if math.gcd(q // g, g) == 1: sqf += 1
        elif k < 40:
            prev = isprime(q) if k == 39 else False
for p in div:
    d = div[p] / tot
    check(f"local law P(p|q_n)=1/(p+1), p={p}", abs(d - 1 / (p + 1)) < 0.02, f"observed {d:.4f}")
gp = {p: sum(math.log2(1 + 1 / (j * p * (j * p + 2))) for j in range(1, 200000)) for p in (2, 3, 5)}
for p in (2, 3):
    d = div2[p] / tot; pred = gp[p] / (p + 1)
    check(f"lag-two law P(p|q_n, p|q_n+2)=g_p/(p+1), p={p}", abs(d / pred - 1) < 0.08, f"observed {d:.4f} predicted {pred:.4f}")
ks = range(40, NMAX + 1)
obs = sum(cnt_prime[k] for k in ks) / M; pred = sum(2 * math.log(2) / k for k in ks)
check("prime continuant constant 2 log 2 (40<=n<=150)", abs(obs / pred - 1) < 0.08, f"observed {obs:.4f} predicted {pred:.4f}")
obsp = sum(cnt_pair[k] for k in ks) / M; predp = sum(24 * math.log(2) ** 2 / math.pi ** 2 / (k * (k - 1)) for k in ks)
check("lag-one prime pairs follow the 6/pi^2 law (loose)", abs(obsp / predp - 1) < 0.35, f"observed {obsp:.5f} predicted {predp:.5f}")
prod = 1.0
for p in SP: prod *= 1 - 1 / (p * (p + 1))
check("squarefree proxy density = prod(1-1/(p(p+1)))", abs(sqf / sqf_tot - prod) < 0.01 and abs(sqf / sqf_tot - 6 / math.pi ** 2) > 0.05, f"observed {sqf/sqf_tot:.4f} predicted {prod:.4f}")

# ---------------------------------------------------------------- 4-5: dimensions
def cheb_nodes(N, a, b):
    k = np.arange(N); return (a + b) / 2 + (b - a) / 2 * np.cos(np.pi * (k + 0.5) / N)
def bary(Y, nodes):
    N = len(nodes); k = np.arange(N); w = (-1.0) ** k * np.sin(np.pi * (k + 0.5) / N)
    d = Y[..., None] - nodes; small = np.abs(d) < 1e-14; d = np.where(small, 1.0, d)
    t = w / d; P = t / t.sum(axis=-1, keepdims=True)
    return np.where(small.any(axis=-1)[..., None], small.astype(float), P)
def rho_prog(s, m, a, N=36, K=5000):
    hi = 1.0 / a; nodes = cheb_nodes(N, 0, hi); n = a + m * np.arange(K)
    Y = 1.0 / (n[:, None] + nodes[None, :]); W = (n[:, None] + nodes[None, :]) ** (-2 * s)
    L = np.einsum('kn,knj->nj', W, bary(Y, nodes))
    tail = np.array([float(m ** (-2 * s) * mp.zeta(2 * s, (a + m * K + x) / m)) for x in nodes])
    L += tail[:, None] * bary(np.zeros(N), nodes)
    return max(abs(eigvals(L)))
def dim_prog(m, a): return brentq(lambda s: math.log(rho_prog(s, m, a)), 0.5 + 1e-9, 1.0, xtol=1e-11)
d_even = dim_prog(2, 2)
check("transfer operator reproduces the even-digit dimension 0.7195 (control)", abs(d_even - 0.7195) < 5e-4, f"{d_even:.6f}")
for (m, a) in ((16, 16), (16, 8), (32, 8)):
    d = dim_prog(m, a)
    pred4 = 0.5 + 1 / (2 * m) - math.log(m) / (2 * m * m) - float(mp.digamma(a / m)) / (2 * m * m)
    pred3 = 0.5 + 1 / (2 * m) - math.log(m) / (2 * m * m)
    check(f"progression digit set dim E_{{{a},{m}}}: four-term expansion", abs(d - pred4) * m * m < 0.2, f"dim={d:.8f} resid*m^2={ (d-pred4)*m*m:.4f}, without digamma {(d-pred3)*m*m:.4f}")
def rho_avoid(s, p, N=26, A=2500):
    nodes = cheb_nodes(N, 0, 1.0); S = p + 1
    inv = lambda r: p if r == 0 else (0 if r == p else pow(r, -1, p))
    L = np.zeros((S * N, S * N)); digits = np.arange(1, A + 1)
    Y = 1.0 / (digits[:, None] + nodes[None, :]); W = (digits[:, None] + nodes[None, :]) ** (-2 * s); P = bary(Y, nodes)
    P0 = bary(np.zeros(N), nodes); blocks = {}
    for c in range(p):
        idx = np.nonzero(digits % p == c)[0]; Lc = np.einsum('kn,knj->nj', W[idx], P[idx])
        nxt = digits[idx][-1] + p
        tail = np.array([float(p ** (-2 * s) * mp.zeta(2 * s, (nxt + x) / p)) for x in nodes])
        blocks[c] = Lc + tail[:, None] * P0
    for r in range(1, S):
        ir = inv(r)
        for c in range(p):
            rp = p if ir == p else (c + ir) % p
            if rp == 0: continue
            L[r * N:(r + 1) * N, rp * N:(rp + 1) * N] += blocks[c]
    return max(abs(eigvals(L)))
d7 = brentq(lambda s: math.log(rho_avoid(s, 7)), 0.6, 0.999999, xtol=1e-9)
check("avoidance dimension p=7 equals 0.92735 and (1-dim)(p+1) lies between 0.42 and 0.62", abs(d7 - 0.927353) < 2e-4 and 0.42 < (1 - d7) * 8 < 0.62, f"dim={d7:.6f} (1-dim)(p+1)={(1-d7)*8:.4f}")

# ---------------------------------------------------------------- 6: exact Legendre certificates
def legendre_table(p):
    t = [0] + [-1] * (p - 1)
    for a in range(1, p): t[a * a % p] = 1
    return t
def fund_unit(p):
    y = 1
    while True:
        for den, target in ((1, -1), (2, -4)):
            t = p * y * y + target
            if t > 0 and math.isqrt(t) ** 2 == t:
                x = math.isqrt(t)
                if den == 2 and (x % 2 != y % 2): continue
                return x, y, den
        y += 1
def unit_power(fu, p, e):
    x, y, d = fu; X, Y = 1, 0
    for _ in range(e): X, Y = X * x + Y * y * p, X * y + Y * x
    D = d ** e; g = math.gcd(math.gcd(X, Y), D); return X // g, Y // g, D // g
def solve_exact(A, k):
    """Solve sum_i x_i A[i][j] = v (j<k), sum x_i = 1 over the rationals; return (v, x)."""
    m = len(A); n = k + 1
    Mx = [[Fraction(A[i][j]) for i in range(k)] + [Fraction(-1)] + [Fraction(0)] for j in range(k)]
    Mx.append([Fraction(1)] * k + [Fraction(0)] + [Fraction(1)])
    for col in range(n):
        piv = next(r for r in range(col, n) if Mx[r][col] != 0)
        Mx[col], Mx[piv] = Mx[piv], Mx[col]
        pv = Mx[col][col]; Mx[col] = [t / pv for t in Mx[col]]
        for r in range(n):
            if r != col and Mx[r][col] != 0:
                f = Mx[r][col]; Mx[r] = [a - f * b for a, b in zip(Mx[r], Mx[col])]
    sol = [Mx[r][n] for r in range(n)]
    return sol[k], sol[:k] + [Fraction(0)] * (m - k)
for which, plist, expo in (("hankel", (17, 41, 73, 89, 97, 113), 1), ("toeplitz", (13, 29, 37, 61), 3)):
    for p in plist:
        chi = legendre_table(p); m = (p - 1) // 2
        A = [[chi[(i + j) % p] if which == "hankel" else chi[(i - j) % p] for j in range(1, m + 1)] for i in range(1, m + 1)]
        v, x = solve_exact(A, m - 1 if which == "hankel" else m)
        pay = [sum(x[i] * A[i][j] for i in range(m)) for j in range(m)]
        fu = fund_unit(p); X, Y, D = unit_power(fu, p, expo)
        target = Fraction(-Y, X) if which == "hankel" else Fraction(Y, X)
        ok = all(t >= 0 for t in x) and all(t == v for t in pay) and v == target and D == 1 and X * X - p * Y * Y == -1
        check(f"exact value of the {which} half box p={p} is {'-' if which=='hankel' else '+'}y/x for the unit eps^{expo}", ok, f"v={v}")

# ---------------------------------------------------------------- 7: LP values
def value(A):
    m, n = A.shape; c = np.zeros(m + 1); c[-1] = -1
    r = linprog(c, A_ub=np.hstack([-A.T, np.ones((n, 1))]), b_ub=np.zeros(n),
                A_eq=np.hstack([np.ones((1, m)), np.zeros((1, 1))]), b_eq=[1],
                bounds=[(0, None)] * m + [(None, None)], method="highs")
    x = np.maximum(r.x[:m], 0); x /= x.sum(); low = (x @ A).min()
    c2 = np.zeros(n + 1); c2[-1] = 1
    r2 = linprog(c2, A_ub=np.hstack([A, -np.ones((m, 1))]), b_ub=np.zeros(m),
                 A_eq=np.hstack([np.ones((1, n)), np.zeros((1, 1))]), b_eq=[1],
                 bounds=[(0, None)] * n + [(None, None)], method="highs")
    y = np.maximum(r2.x[:n], 0); y /= y.sum(); high = (A @ y).max()
    assert high - low < 1e-7
    return (low + high) / 2
c = rng.choice([-1.0, 1.0], size=13); i = np.arange(13); C = c[(i[:, None] - i[None, :]) % 13]
check("circulant game value equals the mean entry", abs(value(C) - c.mean()) < 1e-8, f"{value(C):.6f} vs {c.mean():.6f}")
B = rng.standard_normal((15, 15)); B = B - B.T
check("antisymmetric game has value zero", abs(value(B)) < 1e-8, f"{value(B):.2e}")

# ---------------------------------------------------------------- 8-9: quartics over F_q
def points(q):
    return [(1, y, z) for y in range(q) for z in range(q)] + [(0, 1, z) for z in range(q)] + [(0, 0, 1)]
MON4 = [(a, b, 4 - a - b) for a in range(5) for b in range(5 - a)]
def ev(F, P, q):
    x, y, z = P; return sum(c * pow(x, a, q) * pow(y, b, q) * pow(z, cc, q) for c, (a, b, cc) in zip(F, MON4)) % q
def grad_zero(F, P, q):
    for k in range(3):
        g = 0
        for c, mon in zip(F, MON4):
            if mon[k] > 0:
                mm = list(mon); mm[k] -= 1
                g += c * mon[k] * pow(P[0], mm[0], q) * pow(P[1], mm[1], q) * pow(P[2], mm[2], q)
        if g % q: return False
    return True
def line_pts(l, q, P):
    a, b, c = l; return [Q for Q in P if (a * Q[0] + b * Q[1] + c * Q[2]) % q == 0]
def tangent_line(coef, q):
    """True if the binary quartic with coefficients coef[k] of s^k has a repeated root over the closure."""
    s_ = sp.symbols('s')
    f = sp.Poly(sum(int(coef[k]) * s_ ** k for k in range(5)), s_, modulus=q)
    return sp.gcd(f, f.diff(s_)).degree() >= 1
q = 13; P = points(q); chi = legendre_table(q); V = sp.Matrix([[t ** k for k in range(5)] for t in range(5)]); Vinv = V.inv_mod(q)
n_curves = 0; div_ok = 0; dual_ok = 0; dual_tested = 0
while n_curves < 12:
    F = [int(t) for t in rng.integers(0, q, size=15)]
    on = [Q for Q in P if ev(F, Q, q) == 0]
    if any(grad_zero(F, Q, q) for Q in on): continue
    n_curves += 1
    S = sum(chi[ev(F, Q, q)] for Q in P)
    if S % q == 0 and abs(S // q) <= 7: div_ok += 1
    # tangent lines and bitangent tangency types
    ntan = 0; bs = bc = 0; hyper = False
    for l in P:
        lp = line_pts(l, q, P); good = [Q for Q in lp if ev(F, Q, q) != 0]
        P0, P1 = good[0], good[1]
        vals = [ev(F, tuple((P0[t] + s * P1[t]) % q for t in range(3)), q) for s in range(5)]
        coef = [int(t) % q for t in (Vinv * sp.Matrix(vals))]  # f(s) = sum coef[k] s^k
        if tangent_line(coef, q): ntan += 1
        c0 = coef[0]; ic0 = pow(c0, -1, q); inv2 = pow(2, -1, q)
        al = coef[1] * ic0 * inv2 % q; be = (coef[2] * ic0 - al * al) * inv2 % q
        if (2 * al * be * c0 - coef[3]) % q == 0 and (c0 * be * be - coef[4]) % q == 0:
            disc = (al * al - 4 * be) % q
            if disc == 0: hyper = True
            elif chi[disc] == 1: bs += 1
            else: bc += 1
    if not hyper:
        dual_tested += 1
        if ntan == len(on) - bs + bc: dual_ok += 1
check("character sum of a smooth quartic is q times an integer of modulus at most 7 (12 curves, q=13)", div_ok == n_curves, f"{div_ok}/{n_curves}")
check("dual-curve identity #C^v = #C - b_split + b_conj on curves without hyperflex", dual_tested > 0 and dual_ok == dual_tested, f"{dual_ok}/{dual_tested}")

# ---------------------------------------------------------------- 10: scale separation of random games
m = 60; hk = []; full = []
for _ in range(40):
    h = rng.choice([-1.0, 1.0], size=2 * m - 1); i = np.arange(m); hk.append(value(h[i[:, None] + i[None, :]]))
    full.append(value(rng.choice([-1.0, 1.0], size=(m, m))))
sh = np.std(hk) * math.sqrt(m); sf = np.std(full) * math.sqrt(m)
check("Hankel sign games: sqrt(m) v has spread of order one; full games are smaller", 0.5 < sh < 1.3 and sf < 0.45 and sh > 2 * sf, f"hankel {sh:.3f} full {sf:.3f}")

# ---------------------------------------------------------------- 11: quarter and half boxes
for p in (103, 107, 127, 131):
    chi = legendre_table(p); mq = p // 4; i = np.arange(1, mq + 1)
    Q = np.array(chi, dtype=float)[(i[:, None] + i[None, :]) % p]; vq = value(Q)
    mh = (p - 1) // 2; j = np.arange(1, mh + 1); Hm = np.array(chi, dtype=float)[(j[:, None] + j[None, :]) % p]; vh = value(Hm)
    if p % 8 == 7:
        check(f"p={p} (7 mod 8): quarter box positive, half box nonpositive with |v|<1/p", vq > 0 and vh < 1e-12 and abs(vh) < 1 / p, f"quarter {vq:.5f} half {vh:.2e}")
    else:
        check(f"p={p} (3 mod 8): quarter box positive, half box |v|<1/p (sign not asserted)", vq > 0 and abs(vh) < 1 / p, f"quarter {vq:.5f} half {vh:.2e}")

# ---------------------------------------------------------------- 12: exact certificate at p = 547
import json, os
cert_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "at15_p547_certificate.json")
obj = json.load(open(cert_path)); p = int(obj["p"]); m = (p - 1) // 2; v = Fraction(obj["value"])
x = [Fraction(0)] * m; y = [Fraction(0)] * m
for it in obj["row_strategy"]: x[int(it["index_1based"]) - 1] = Fraction(it["weight"])
for it in obj["column_strategy"]: y[int(it["index_1based"]) - 1] = Fraction(it["weight"])
chi = legendre_table(p)
ok = p == 547 and p % 8 == 3 and sum(x) == 1 and sum(y) == 1 and min(x) >= 0 and min(y) >= 0 and v > 0
col = [sum(x[i] * chi[(i + j + 2) % p] for i in range(m)) for j in range(m)]   # entry (i+1)+(j+1)
row = [sum(y[j] * chi[(i + j + 2) % p] for j in range(m)) for i in range(m)]
ok = ok and min(col) >= v and max(row) <= v
check("p=547: exact rational certificate, row guarantee >= v and column guarantee <= v with v > 0 (half box positive)", ok, f"v={float(v):.6e}, p^1.5 v={float(v)*p**1.5:.3f}, supports {sum(t>0 for t in x)}/{sum(t>0 for t in y)}")

print(f"\n{sum(PASS)}/{len(PASS)} checks passed")
sys.exit(0 if all(PASS) else 1)
