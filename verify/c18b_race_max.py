"""C18' -- the Darling-Erdos running-maximum law for balanced races.

For a driftless (balanced) prime-pattern race D(t), the Lamperti
reduction in logarithmic time is a stationary Ornstein-Uhlenbeck
process, so the running maximum of the studentized race obeys the
Darling-Erdos scale:

    M(x) = max_{t<=x} |D(t)| / sqrt(count(t)) = sqrt(2 log log x) (1+o(1)),

with Gumbel-type fluctuations after the classical centering.  This is
an EXTREME-VALUE law for prime races in the logarithmic clock -- the
statistic is new even though each race is already conjectured
driftless.  Tested here on four balanced control races at 10^9:
  twins:   classes 2 vs 4 (mod 5)   and 3 vs 5 (mod 8);
  cousins: classes 2 vs 3 (mod 5)   and 3 vs 5 (mod 8).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import *

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9

RACES = [("twin 2v4 mod5", 2, 5, 2, 4), ("twin 3v5 mod8", 2, 8, 3, 5),
         ("cousin 2v3 mod5", 4, 5, 2, 3), ("cousin 3v5 mod8", 4, 8, 3, 5)]
state = {name: {"D": 0, "cnt": 0, "max": 0.0} for name, *_ in RACES}
carry = np.zeros(4, dtype=bool)
carry_lo = 0
with Timer("sweep"):
    for lo, hi, seg in seg_sieve(X + 5, seg_size=1 << 22):
        comb = np.concatenate([carry, seg]) if lo else seg
        base = carry_lo if lo else 0
        for name, d, m, a, b in RACES:
            starts = np.nonzero(comb[:-d] & comb[d:])[0] + base
            starts = starts[starts > 7]
            r = starts % m
            ia, ib = r == a, r == b
            sel = ia | ib
            if not sel.any():
                continue
            step = np.where(ia[sel], 1, -1)
            st = state[name]
            D = np.cumsum(step) + st["D"]
            cnt = np.arange(1, len(step) + 1) + st["cnt"]
            st["max"] = max(st["max"], float(np.max(np.abs(D) / np.sqrt(cnt))))
            st["D"] = int(D[-1]); st["cnt"] = int(cnt[-1])
            # step autocorrelation accumulators (diffusivity diagnosis)
            st.setdefault("s1", 0.0); st.setdefault("s2", 0.0)
            st.setdefault("n1", 0)
            if len(step) > 3:
                st["s1"] += float(np.dot(step[:-1], step[1:]))
                st["s2"] += float(np.dot(step[:-2], step[2:]))
                st["n1"] += len(step) - 1
        carry, carry_lo = seg[-4:].copy(), hi - 4

de = math.sqrt(2 * math.log(math.log(X)))
print("Darling-Erdos scale sqrt(2 loglog x) at %.0e: %.3f" % (X, de))

# finite-x null via simulation: the studentized race in log time is an
# OU-type process with covariance e^{-|u|/2}; simulate max |Z| over the
# actual observation span S = log(count range) with AR(1) steps.
with Timer("null simulation"):
    rng = np.random.default_rng(20260728)
    S = math.log(math.log(X))  # not used directly; use event-count span
    # span in OU time: s = log(event count), from ~log 10 to log(cnt)
    spans = {name: math.log(max(state[name]["cnt"], 100)) - math.log(10)
             for name, *_ in RACES}
    Smax = max(spans.values())
    dt = 0.01
    n = int(Smax / dt) + 1
    rho = math.exp(-dt / 2)
    sig = math.sqrt(1 - rho * rho)
    NP = 4000
    Z = rng.standard_normal(NP)
    M = np.abs(Z.copy())
    grid = {}
    marks = sorted(set(int(s / dt) for s in spans.values()))
    for k in range(1, n):
        Z = rho * Z + sig * rng.standard_normal(NP)
        np.maximum(M, np.abs(Z), out=M)
        if k in marks:
            grid[k] = M.copy()
out = {}
for name, *_ in RACES:
    st = state[name]
    k = int(spans[name] / dt)
    k = min(grid.keys(), key=lambda kk: abs(kk - k))
    null = grid[k]
    quant = float(np.mean(null <= st["max"]))
    rho1 = st["s1"] / st["n1"]
    rho2 = st["s2"] / st["n1"]
    sig_eff = math.sqrt(max(1 + 2 * rho1 + 2 * rho2, 0.05))
    quant_c = float(np.mean(null <= st["max"] / sig_eff))
    print("%-16s  M(x)=%.3f  null q=%.2f  step rho1=%+.4f rho2=%+.4f  "
          "sigma_eff=%.3f  corrected q=%.2f"
          % (name, st["max"], quant, rho1, rho2, sig_eff, quant_c))
    out[name] = {"final_D": st["D"], "count": st["cnt"],
                 "runmax": st["max"], "ratio_to_DE": st["max"] / de,
                 "null_quantile": quant, "rho1": rho1, "rho2": rho2,
                 "sigma_eff": sig_eff, "corrected_quantile": quant_c}
print("simulated null median max over the span: %.3f  (asymptote %.3f approached slowly)"
      % (float(np.median(grid[max(grid)])), de))
save_result("c18b", {"conjecture": "Darling-Erdos running-max law for balanced races: "
                                   "max |D|/sqrt(count) ~ sqrt(2 loglog x); finite-x null "
                                   "from OU simulation",
                     "X": X, "DE_scale": de,
                     "null_median": float(np.median(grid[max(grid)])),
                     "races": out})
