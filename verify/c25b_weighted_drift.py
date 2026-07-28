"""C25 upgrade -- the singular-series-weighted drift and the sign-density
constant of the Goldbach lane race.

The fourth external review noted that the expected mean of D_sys must
average the Hardy-Littlewood local densities of n - q^2 (they vary
with n), not treat each n - q^2 as a generic integer.  The variation
is drastic: for n = 1 (mod 3), q^2 = 1 (mod 3) for every prime q > 3,
so 3 | n - q^2 ALWAYS and the contamination collapses to the single
q = 3 term -- a finite local collapse an Euler product cannot
represent (its p = 3 factor vanishes).  We therefore use the exact
presieve + Mertens form: with P = 1000 and
prodOdd = prod_{2 < p <= P} (1 - 1/p) computed exactly,

  P(n - q^2 prime) = [2 / (log(n-q^2) * prodOdd)]
                       * 1{n - q^2 has no prime factor <= P},

(the 2 is parity: n - q^2 is always odd), which incorporates every
local condition -- quadratic residues, p | n bonuses, the mod-3
collapse -- through the actual trial division of each n - q^2.  Model:

    Dsys_model(n) = (4 / (lbar(n) * prodOdd)) *
                    sum_{q alive} log q  +  exact small-prime terms,

with lbar(n) the ANALYTIC lane mean (n-6)/J(n),
J(n) = int_3^{n-3} dt/(log t log(n-t)).  The noise scale is
sigma(n) = sqrt(S_G(n) J(n)) (total ordered representations across
both lanes), giving the drift-to-noise constant kappa(n) =
Dsys_model(n)/sigma(n) and the predicted limiting sign density
Phi(kappa) -- a CONSTANT in (1/2, 1), unlike the twin race where
drift/noise -> 0.  This script computes, on the same seeded sample as
the c25 run: mean Dsys_model vs mean empirical Dsys (recomputed with
the analytic lbar), mean kappa, and mean Phi(kappa) vs the observed
sign fraction 0.592.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
NSAMP = int(sys.argv[2]) if len(sys.argv) > 2 else 400
PLOC = 1000
TWO_C2 = 1.3203236316

with Timer("sieve"):
    P = sieve_bool(X)
P1 = np.zeros_like(P)
P1[5::4] = P[5::4]
P3 = np.zeros_like(P)
P3[3::4] = P[3::4]
p1_list = np.nonzero(P1)[0].astype(np.int64)
p3_list = np.nonzero(P3)[0].astype(np.int64)
qs = np.array([int(q) for q in primes_up_to(int(math.isqrt(X)) + 1) if q > 2],
              dtype=np.int64)
logqs = np.log(qs.astype(float))
locp = [int(p) for p in primes_up_to(PLOC) if p > 2]
prod_odd = 1.0
for p in locp:
    prod_odd *= 1 - 1.0 / p

rng = np.random.default_rng(20260727)
lo, hi = 10**6, X
samples = np.unique((np.exp(rng.uniform(math.log(lo), math.log(hi), NSAMP)) // 4)
                    .astype(np.int64) * 4 + 2)


def J_int(n):
    t = np.exp(np.linspace(math.log(3.0), math.log(n - 3.0), 4001))
    f = 1.0 / (np.log(t) * np.log(n - t))
    return float(np.trapezoid(f, t))


def model_drift(n, lbar):
    """Presieve+Mertens expected value of 2*sum log q log(n-q^2) P(prime)/lbar."""
    v = n - qs * qs
    ok = v >= 3
    v = v[ok]
    lq = logqs[ok]
    alive = np.ones(len(v), dtype=bool)
    exact = 0.0
    for p in locp:
        hit = v % p == 0
        small = hit & (v == p)  # n - q^2 IS the small prime p: prime with prob 1
        if small.any():
            exact += float(np.sum(2.0 * lq[small] * np.log(v[small]) / lbar))
        alive &= ~hit
    return exact + 4.0 / (lbar * prod_odd) * float(np.sum(lq[alive]))


def SG(n):
    s = TWO_C2
    m = n
    for p in (3, 5, 7, 11, 13):
        if m % p == 0:
            s *= (p - 1) / (p - 2)
    # larger odd prime factors of n
    m = n // 2
    d = 3
    mm = m
    while d * d <= mm:
        if mm % d == 0:
            if d > 13:
                s *= (d - 1) / (d - 2)
            while mm % d == 0:
                mm //= d
        d += 2
    if mm > 13 and mm > 1:
        s *= (mm - 1) / (mm - 2)
    return s


Phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))

rows = []
with Timer("weighted drift over %d samples" % len(samples)):
    for n in samples:
        n = int(n)
        J = J_int(n)
        lbar = (n - 6) / J
        v = n - qs * qs
        ok = v >= 3
        vv = v[ok]
        hit = P[vv]
        de = 2.0 * float(np.sum(logqs[ok][hit] * np.log(vv[hit].astype(float)))) / lbar
        dm = model_drift(n, lbar)
        sig = math.sqrt(max(SG(n) * J, 1e-12))
        i3 = np.searchsorted(p3_list, n - 2)
        R3 = int(np.count_nonzero(P3[n - p3_list[:i3]]))
        i1 = np.searchsorted(p1_list, n - 2)
        R1 = int(np.count_nonzero(P1[n - p1_list[:i1]]))
        rows.append((n, dm, de, dm / sig, R3 - R1))

nn = np.array([r[0] for r in rows])
dm = np.array([r[1] for r in rows])
de = np.array([r[2] for r in rows])
ka = np.array([r[3] for r in rows])
DD = np.array([r[4] for r in rows], dtype=float)
phis = np.array([Phi(k) for k in ka])
print("samples: %d" % len(rows))
print("mean Dsys_model (HL-weighted) = %.2f" % dm.mean())
print("mean Dsys_empirical (analytic lbar) = %.2f" % de.mean())
print("model/empirical ratio = %.3f" % (dm.mean() / de.mean()))
print("mean D (recounted) = %.2f" % DD.mean())
print("mean kappa (drift/noise) = %.3f  (range %.3f .. %.3f)"
      % (ka.mean(), ka.min(), ka.max()))
print("predicted sign density mean Phi(kappa) = %.3f   observed frac{D>0} = %.3f"
      % (phis.mean(), (DD > 0).mean()))
print("-- internal null lane: n = 1 (mod 3), i.e. n = 10 (mod 12) --")
strata = {}
for label, sel in (("null n=1(3)", nn % 3 == 1), ("live n=0,2(3)", nn % 3 != 1)):
    k = int(sel.sum())
    se = DD[sel].std() / math.sqrt(k)
    strata[label] = {"n": k, "mean_D": float(DD[sel].mean()), "se": float(se),
                     "mean_Dsys_model": float(dm[sel].mean()),
                     "mean_Dsys_emp": float(de[sel].mean()),
                     "sign_frac": float((DD[sel] > 0).mean())}
    print("%s: n=%d  mean D = %.1f +- %.1f  model Dsys = %.1f  emp Dsys = %.1f  "
          "frac{D>0} = %.3f"
          % (label, k, DD[sel].mean(), se, dm[sel].mean(), de[sel].mean(),
             (DD[sel] > 0).mean()))
save_result("c25b", {"conjecture": "HL-weighted drift, sign-density constant, and internal "
                                   "null lane n=1(3) for the Goldbach lane race",
                     "X": X, "n_samples": len(rows),
                     "mean_Dsys_model": float(dm.mean()),
                     "mean_Dsys_empirical_analytic_lbar": float(de.mean()),
                     "mean_D": float(DD.mean()),
                     "mean_kappa": float(ka.mean()),
                     "pred_sign_density": float(phis.mean()),
                     "obs_sign_frac": float((DD > 0).mean()),
                     "strata": strata})
