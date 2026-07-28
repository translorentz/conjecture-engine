"""C22 upgrade -- the differentiating experiment: prime vs smooth moduli,
with theta_disc DEFINED by an explicit Bernoulli control model.

Control model (named): candidates a, a+q, a+2q, ... are independently
prime with hazard h_i = w/log(a+iq) where w = q/phi(q) for candidates
coprime to the fixed small primes dividing 2q's radical... simplified to
the parity-aware Cramer control: h_i = (q/phi(q)) * s_i / log(v_i), with
s_i = 2 if v_i odd else 0 (odd q: parity alternates; even q: fixed).
E_model[U] is computed exactly from these hazards; the DISCRETENESS
deficit is theta_disc(q) = (1 - E_model[U]) log q.  The ordering term is
theta_corr(q) = (1 - E_measured[U]) log q - theta_disc(q).

If theta_corr persists for PRIME moduli q (no smooth-modulus structure),
the ordering anomaly is differentiated from Leung's smooth-q
singular-series discrepancies.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

PLIM = int(float(sys.argv[1])) if len(sys.argv) > 1 else 2 * 10**7

with Timer("primes"):
    primes = primes_up_to(PLIM).astype(np.int64)
grid = np.linspace(2.0, float(PLIM), 2_000_001)
lig = np.concatenate([[0.0], np.cumsum(np.diff(grid) / np.log(grid[:-1] + np.diff(grid) / 2))])
def Li(x): return np.interp(x, grid, lig)

# strata: prime q in [1500, 6000]; smooth q (7-smooth) in same range
prime_qs = [int(q) for q in primes_up_to(6000) if q > 1500][:40]
smooth_qs = sorted({2**a * 3**b * 5**c * 7**d
                    for a in range(0, 13) for b in range(0, 8)
                    for c in range(0, 6) for d in range(0, 5)
                    if 1500 <= 2**a * 3**b * 5**c * 7**d <= 6000})[:40]

def measured_meanU(q):
    r = primes % q
    cl, fi = np.unique(r, return_index=True)
    keep = np.gcd(cl, q) == 1
    phi = int(np.count_nonzero(np.gcd(np.arange(1, q + 1), q) == 1))
    if int(keep.sum()) != phi:
        return None, phi
    return float(np.mean(Li(primes[fi[keep]].astype(float)) / phi)), phi

def model_meanU(q, phi, L=4000):
    """Exact E[U] under the parity-aware Cramer control, averaged over classes."""
    a = np.arange(1, q + 1)
    a = a[np.gcd(a, q) == 1].astype(np.float64)          # phi classes
    i = np.arange(L, dtype=np.float64)
    V = a[:, None] + i[None, :] * q                       # candidate values
    odd = (V % 2) == 1
    h = np.where(odd, (q / phi) * 2.0 / np.log(np.maximum(V, 3.0)), 0.0)
    h = np.clip(h, 0.0, 0.97)
    surv = np.cumprod(1.0 - h, axis=1)
    pfirst = h * np.concatenate([np.ones((len(a), 1)), surv[:, :-1]], axis=1)
    U = Li(V) / phi
    EU = (pfirst * U).sum(axis=1) + (1 - pfirst.sum(axis=1)) * U[:, -1]
    return float(EU.mean())

rows = []
for label, qs in (("prime", prime_qs), ("smooth", smooth_qs)):
    th_d, th_c = [], []
    for q in qs:
        mu, phi = measured_meanU(q)
        if mu is None:
            continue
        mm = model_meanU(q, phi)
        lg = math.log(q)
        th_d.append((1 - mm) * lg)
        th_c.append((1 - mu) * lg - (1 - mm) * lg)
    th_d, th_c = np.array(th_d), np.array(th_c)
    rows.append({"stratum": label, "n_q": len(th_d),
                 "theta_disc_mean": float(th_d.mean()), "theta_disc_se": float(th_d.std()/math.sqrt(len(th_d))),
                 "theta_corr_mean": float(th_c.mean()), "theta_corr_se": float(th_c.std()/math.sqrt(len(th_c)))})
    print("%s moduli (n=%d): theta_disc = %.3f +- %.3f ; theta_corr = %.3f +- %.3f"
          % (label, len(th_d), th_d.mean(), th_d.std()/math.sqrt(len(th_d)),
             th_c.mean(), th_c.std()/math.sqrt(len(th_c))))
save_result("c22b", {"conjecture": "theta decomposition with defined Bernoulli control; "
                                   "theta_corr persistence on prime moduli differentiates from smooth-q effects",
                     "PLIM": PLIM, "rows": rows})
