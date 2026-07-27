"""
ntlib.py -- shared number-theory machinery for the conjecture engine.

Provides:
  * dense and segmented sieves (numpy)
  * deterministic Miller-Rabin (n < 3.317e24) and BPSW for big integers
  * Legendre symbol, Tonelli-Shanks square roots mod p
  * Bateman-Horn singular series for systems of integer polynomials
  * Hardy-Littlewood k-tuple constants, twin singular series S(d)
  * logarithmic integrals  int dt / prod log|f_i(t)|
  * result persistence (results/*.json)

All heuristic constants are computed from first principles here; the
verification scripts compare raw counts against these predictions.
"""

import json
import math
import os
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(ROOT, "results")

TWIN_C2 = 0.6601618158468695739278121100145557784326  # Hardy-Littlewood C2
TWIN_2C2 = 2 * TWIN_C2
EULER_GAMMA = 0.5772156649015328606065120900824024310422


# ----------------------------------------------------------------------
# sieves
# ----------------------------------------------------------------------

def sieve_bool(n):
    """Boolean array s of length n+1 with s[i] = True iff i is prime."""
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p:: p] = False
    return s


def primes_up_to(n):
    return np.nonzero(sieve_bool(n))[0]


def seg_sieve(limit, seg_size=1 << 23, start=0):
    """Yield (lo, hi, seg) with seg[i] = True iff lo+i is prime, covering
    [start, limit)."""
    base = primes_up_to(int(limit ** 0.5) + 1)
    lo = start
    while lo < limit:
        hi = min(lo + seg_size, limit)
        seg = np.ones(hi - lo, dtype=bool)
        if lo == 0:
            seg[:2] = False
        elif lo == 1:
            seg[:1] = False
        for p in base:
            p = int(p)
            first = max(p * p, ((lo + p - 1) // p) * p)
            if first < hi:
                seg[first - lo:: p] = False
        yield lo, hi, seg
        lo = hi


# ----------------------------------------------------------------------
# primality for individual integers
# ----------------------------------------------------------------------

_DET_MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
_DET_MR_LIMIT = 3317044064679887385961981  # deterministic below this


def _mr_witness(a, d, n, r):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(r - 1):
        x = x * x % n
        if x == n - 1:
            return False
    return True


def _miller_rabin(n, bases):
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in bases:
        if a % n == 0:
            continue
        if _mr_witness(a, d, n, r):
            return False
    return True


def _jacobi(a, n):
    a %= n
    t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


def _strong_lucas(n):
    """Strong Lucas probable-prime test with Selfridge parameters."""
    D = 5
    while True:
        j = _jacobi(D, n)
        if j == -1:
            break
        if j == 0 and abs(D) != n:
            return False
        D = -D - 2 if D > 0 else -D + 2
        if D == 13 and int(math.isqrt(n)) ** 2 == n:
            return False
    P, Q = 1, (1 - D) // 4
    d, s = n + 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # compute U_d, V_d via binary chain
    U, V, Qk = 1, P, Q % n
    for bit in bin(d)[3:]:
        U, V = U * V % n, (V * V - 2 * Qk) % n
        Qk = Qk * Qk % n
        if bit == "1":
            U, V = (P * U + V) % n, (D * U + P * V) % n
            if U % 2:
                U += n
            if V % 2:
                V += n
            U, V = U // 2 % n, V // 2 % n
            Qk = Qk * Q % n
    if U == 0 or V == 0:
        return True
    for _ in range(s - 1):
        V = (V * V - 2 * Qk) % n
        if V == 0:
            return True
        Qk = Qk * Qk % n
    return False


def is_prime(n):
    """Deterministic for n < 3.317e24, BPSW beyond (no known counterexample)."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    if n < _DET_MR_LIMIT:
        return _miller_rabin(n, _DET_MR_BASES)
    return _miller_rabin(n, (2,)) and _strong_lucas(n)


# ----------------------------------------------------------------------
# modular helpers
# ----------------------------------------------------------------------

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    t = pow(a, (p - 1) // 2, p)
    return 1 if t == 1 else -1


def sqrt_mod(a, p):
    """Tonelli-Shanks: x with x^2 = a (mod p), or None. p odd prime."""
    a %= p
    if a == 0:
        return 0
    if legendre(a, p) != 1:
        return None
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while legendre(z, p) != -1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t, r = t * c % p, r * b % p
    return r


# ----------------------------------------------------------------------
# polynomials:  coefficient lists in ASCENDING order, e.g. n^2+1 -> [1,0,1]
# ----------------------------------------------------------------------

def poly_eval_mod(coeffs, n, p):
    """Evaluate poly at numpy array n modulo p."""
    acc = np.zeros_like(n)
    for c in reversed(coeffs):
        acc = (acc * n + (c % p)) % p
    return acc


def poly_eval_int(coeffs, n):
    acc = 0
    for c in reversed(coeffs):
        acc = acc * n + c
    return acc


def _analytic_root_count(coeffs, p):
    """Number of roots mod p, valid when p exceeds every coefficient.
    Supports degree 1, degree 2, and pure cubics x^3 + c."""
    deg = len(coeffs) - 1
    if deg == 1:
        return 1
    if deg == 2:
        c, b, a = coeffs[0], coeffs[1], coeffs[2]
        disc = (b * b - 4 * a * c) % p
        if disc == 0:
            return 1
        return 1 + legendre(disc, p)
    if deg == 3 and coeffs[1] == 0 and coeffs[2] == 0:
        c = coeffs[0]
        if p % 3 == 2:
            return 1
        # p = 1 mod 3: x^3 = -c has 3 roots iff -c is a cubic residue
        return 3 if pow(-c % p, (p - 1) // 3, p) == 1 else 0
    raise NotImplementedError("root count for degree %d" % deg)


def omega_brute(polys, p):
    """#{n mod p : p | prod f_i(n)} by direct enumeration."""
    n = np.arange(p, dtype=np.int64)
    bad = np.zeros(p, dtype=bool)
    for coeffs in polys:
        bad |= poly_eval_mod(coeffs, n, p) == 0
    return int(bad.sum())


def bateman_horn_constant(polys, pmax=1_000_000, brute_below=5000):
    """C = prod_p (1 - omega(p)/p) / (1 - 1/p)^k  over p <= pmax.

    Beyond `brute_below` the roots of distinct polynomials are assumed
    disjoint mod p (valid once p exceeds all pairwise resultants; our
    systems have tiny resultants, and everything below `brute_below`
    is enumerated directly).  Returns (C, C_at_pmax_over_10) so callers
    can report a truncation error estimate.
    """
    k = len(polys)
    logC = 0.0
    logC_early = None
    ps = primes_up_to(pmax)
    cut = pmax // 10
    for p in ps:
        p = int(p)
        if p < brute_below:
            w = omega_brute(polys, p)
        else:
            w = sum(_analytic_root_count(c, p) for c in polys)
        if w >= p:
            raise ValueError("inadmissible: omega(%d) = %d" % (p, w))
        logC += math.log1p(-w / p) - k * math.log1p(-1.0 / p)
        if logC_early is None and p > cut:
            logC_early = logC
    return math.exp(logC), math.exp(logC_early if logC_early is not None else logC)


def hl_tuple_constant(offsets, pmax=1_000_000):
    """Hardy-Littlewood constant for the k-tuple n + h, h in offsets."""
    k = len(offsets)
    span = max(offsets) - min(offsets)
    logC = 0.0
    for p in primes_up_to(pmax):
        p = int(p)
        w = len(set(h % p for h in offsets)) if p <= span else k
        if w >= p:
            raise ValueError("inadmissible tuple at p=%d" % p)
        logC += math.log1p(-w / p) - k * math.log1p(-1.0 / p)
    return math.exp(logC)


def twin_S(d):
    """Singular series for the pair (n, n+d), d even: S(d)=2C2*prod (p-1)/(p-2)."""
    assert d % 2 == 0 and d > 0
    s = TWIN_2C2
    m = d
    while m % 2 == 0:
        m //= 2
    p = 3
    while p * p <= m:
        if m % p == 0:
            s *= (p - 1) / (p - 2)
            while m % p == 0:
                m //= p
        p += 2
    if m > 1:
        s *= (m - 1) / (m - 2)
    return s


def inv_mod(a, p):
    return pow(a, -1, p)


def poly_roots_mod(coeffs, p):
    """All roots of the polynomial mod p.  Fast paths for degree 1/2 and
    pure cubics with p = 2 mod 3; brute force otherwise (small p or the
    p = 1 mod 3 cubic case, which is rare enough not to matter)."""
    deg = len(coeffs) - 1
    if p <= max(64, *[abs(c) for c in coeffs]):
        n = np.arange(p, dtype=np.int64)
        return [int(r) for r in n[poly_eval_mod(coeffs, n, p) == 0]]
    if deg == 1:
        return [(-coeffs[0]) * inv_mod(coeffs[1], p) % p]
    if deg == 2:
        c, b, a = coeffs
        disc = (b * b - 4 * a * c) % p
        s = sqrt_mod(disc, p)
        if s is None:
            return []
        i2a = inv_mod(2 * a, p)
        r1, r2 = (-b + s) * i2a % p, (-b - s) * i2a % p
        return [r1] if r1 == r2 else [r1, r2]
    if deg == 3 and coeffs[1] == 0 and coeffs[2] == 0:
        c = -coeffs[0] % p
        if p % 3 == 2:
            return [pow(c, (2 * p - 1) // 3, p)]
        if pow(c, (p - 1) // 3, p) != 1:
            return []
        n = np.arange(p, dtype=np.int64)
        return [int(r) for r in n[poly_eval_mod(coeffs, n, p) == 0]]
    raise NotImplementedError


def count_poly_primes(polys, N, presieve_to=100_000, checkpoints=()):
    """#{1 <= n <= N : every f_i(n) is prime}, by sieving out n for which
    some f_i(n) has a prime factor <= presieve_to (with f_i(n) bigger than
    that factor), then applying deterministic Miller-Rabin to survivors.

    Returns dict with 'total', 'at' (checkpoint -> count), 'n_tested',
    'first' (first 10 solutions).
    """
    # small n handled directly so 'f(n) == p' edge cases never arise
    n0 = 1
    while min(poly_eval_int(c, n0) for c in polys) <= presieve_to:
        n0 += 1
    alive = np.ones(N + 1, dtype=bool)
    alive[:n0] = False
    for p in primes_up_to(presieve_to):
        p = int(p)
        for c in polys:
            for r in poly_roots_mod(c, p):
                start = r if r >= n0 else r + ((n0 - r + p - 1) // p) * p
                alive[start:: p] = False
    small = [n for n in range(1, n0)
             if all(is_prime(poly_eval_int(c, n)) for c in polys)]
    cand = np.nonzero(alive)[0]
    sols = list(small)
    for n in cand:
        n = int(n)
        if all(is_prime(poly_eval_int(c, n)) for c in polys):
            sols.append(n)
    sols.sort()
    arr = np.array(sols, dtype=np.int64)
    return {
        "total": len(sols),
        "at": {int(x): int((arr <= x).sum()) for x in checkpoints},
        "n_tested": int(len(cand)) + len(small),
        "first": sols[:10],
    }


def zscore(obs, pred):
    """Poisson-normalized deviation (the residual should look like noise
    of size sqrt(main term) -- criterion III.9b)."""
    return (obs - pred) / math.sqrt(max(pred, 1.0))


# ----------------------------------------------------------------------
# logarithmic integrals
# ----------------------------------------------------------------------

def bh_integral(polys, N, lo=None, npts=200_001):
    """int_{lo}^{N} dt / prod_i log f_i(t), the Bateman-Horn main term
    (already includes the 1/(d1*...*dk) via using log f_i rather than
    deg*log t).  Starts at the smallest t where every f_i(t) >= 3.
    Integrated in u = log t for accuracy over many decades."""
    if lo is None:
        t = 1.0
        while any(poly_eval_int(c, t) < 3 for c in polys):
            t += 1
        lo = t
    u = np.linspace(math.log(lo), math.log(float(N)), npts)
    t = np.exp(u)
    vals = np.ones_like(t)
    for c in polys:
        f = np.polyval(list(reversed(c)), t)
        vals *= np.log(f)
    return float(np.trapezoid(t / vals, u))


def li_k(x, k, lo=2.0, npts=200_001):
    """int_lo^x dt / (log t)^k, integrated in u = log t."""
    u = np.linspace(math.log(lo), math.log(float(x)), npts)
    return float(np.trapezoid(np.exp(u) * u ** (-k), u))


# ----------------------------------------------------------------------
# result persistence
# ----------------------------------------------------------------------

def save_result(name, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    payload = dict(payload)
    payload["_generated_unix"] = int(time.time())
    path = os.path.join(RESULTS_DIR, name + ".json")
    with open(path, "w") as fh:
        json.dump(payload, fh, indent=2, default=_json_default)
    print("\n[saved -> %s]" % os.path.relpath(path, ROOT))


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(type(o))


class Timer:
    def __init__(self, label=""):
        self.label = label

    def __enter__(self):
        self.t0 = time.time()
        return self

    def __exit__(self, *exc):
        self.dt = time.time() - self.t0
        if self.label:
            print("  [%s: %.1fs]" % (self.label, self.dt))
