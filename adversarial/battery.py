"""Adversarial battery: attempts to REFUTE the conjectures by pushing the
falsifiable-by-instance ones far beyond their original verification bounds.

Any line printed with the prefix 'REFUTED' is a counterexample report.
Results are appended to results/adversarial.json.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import numpy as np
from ntlib import (sieve_bool, seg_sieve, primes_up_to, twin_S, li_k,
                   hl_tuple_constant, TWIN_2C2, EULER_GAMMA, Timer, is_prime)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = {}


def report(key, payload):
    OUT[key] = payload
    print("[%s] %s" % (key, json.dumps(payload)[:600]))


# ----------------------------------------------------------------- C14
def attack_c14(lo=10**8, hi=10**9):
    """Hunt for odd n in (lo, hi] not representable as p + 2k^2, k>=1.
    Any hit refutes 'the ten exceptions are all / 5993 largest'."""
    with Timer("c14 sieve"):
        P = sieve_bool(hi)
        Podd = P[1::2].copy()
        del P
    found = []
    seg = 4 * 10**7
    with Timer("c14 hunt"):
        start = lo + 1 if (lo + 1) % 2 else lo + 2
        for s in range(start, hi, seg):
            e = min(s + seg, hi + 1)
            todo = np.arange(s, e, 2, dtype=np.int64)
            k = 1
            while len(todo) and 2 * k * k < e:
                v = todo - 2 * k * k
                alive = v >= 3
                surv = todo[alive]
                v = v[alive]
                hit = Podd[(v - 1) >> 1]
                found.extend(int(x) for x in todo[~alive])
                todo = surv[~hit]
                k += 1
            found.extend(int(x) for x in todo)
    for n in found:
        print("REFUTED c14: %d not representable as p+2k^2" % n)
    report("c14", {"range": [lo, hi], "new_exceptions": found})
    del Podd


# ----------------------------------------------------------------- C15
def attack_c15(lo=10**8, hi=10**9):
    """Hunt for n = 2 (mod 4) in (lo, hi] with no p+q, p=q=3 (mod 4)."""
    with Timer("c15 sieve"):
        P = sieve_bool(hi)
        P3 = np.zeros_like(P)
        P3[3::4] = P[3::4]
        p3 = np.nonzero(P3)[0].astype(np.int64)
        del P
    found = []
    seg = 4 * 10**7
    with Timer("c15 hunt"):
        start = lo + 2
        while start % 4 != 2:
            start += 1
        for s in range(start, hi, seg):
            e = min(s + seg, hi + 1)
            todo = np.arange(s, e, 4, dtype=np.int64)
            i = 0
            while len(todo) and i < len(p3):
                t = int(p3[i])
                v = todo - t
                dead = v < 3
                found.extend(int(x) for x in todo[dead])
                hit = ~dead & P3[np.clip(v, 0, hi)]
                todo = todo[~hit & ~dead]
                i += 1
            found.extend(int(x) for x in todo)
    for n in found:
        print("REFUTED c15: %d has no 3mod4+3mod4 Goldbach partition" % n)
    report("c15", {"range": [lo, hi], "new_exceptions": found})


# ----------------------------------------------------------------- C17
def attack_c17(lo=10**8, hi=10**9):
    """Hunt for even n in (lo, hi] not a sum of two twin-pair members."""
    with Timer("c17 sieve"):
        P = sieve_bool(hi + 2)
        T = np.zeros(hi + 1, dtype=bool)
        T[: hi + 1] = P[: hi + 1]
        m = np.zeros(hi + 1, dtype=bool)
        m[: hi - 1] = P[2: hi + 1]
        m[2: hi + 1] |= P[: hi - 1]
        T &= m
        del P, m
        t_list = np.nonzero(T)[0].astype(np.int64)
    found = []
    seg = 2 * 10**7
    with Timer("c17 hunt"):
        for s in range(lo + 2, hi, seg):
            e = min(s + seg, hi + 1)
            todo = np.arange(s, e, 2, dtype=np.int64)
            i = 0
            while len(todo) and i < len(t_list):
                t = int(t_list[i])
                v = todo - t
                dead = v < 3
                found.extend(int(x) for x in todo[dead])
                hit = ~dead & T[np.clip(v, 0, hi)]
                todo = todo[~hit & ~dead]
                i += 1
            found.extend(int(x) for x in todo)
    for n in found:
        print("REFUTED c17: %d not a sum of two twin members" % n)
    report("c17", {"range": [lo, hi], "new_exceptions": found})
    del T


# ----------------------------------------------------------------- C13
def attack_c13(lo=10**8, hi=10**9):
    """Extend the p + k^3 exception census a decade: the conjecture needs
    the per-decade count to keep collapsing (observed 273 in (1e7,1e8])."""
    with Timer("c13 sieve+union"):
        P = sieve_bool(hi)
        rep = np.zeros(hi + 1, dtype=bool)
        k = 1
        while k ** 3 < hi:
            c = k ** 3
            rep[c:] |= P[: hi + 1 - c]
            k += 1
        del P
    exc = np.nonzero(~rep[lo + 1:])[0] + lo + 1
    exc = [int(x) for x in exc]
    report("c13", {"range": [lo, hi], "new_exceptions_count": len(exc),
                   "sample": exc[:30], "largest": exc[-1] if exc else None,
                   "verdict": ("decay continues" if len(exc) < 273 else
                               "REFUTED-decay: count did not fall")})
    del rep


# ----------------------------------------------------------------- C16
def attack_c16(x=10**8, dmax=6000):
    """Stress uniformity at 3x the original d-range."""
    with Timer("c16 sieve"):
        P = sieve_bool(x)
    LI2 = li_k(x, 2)
    zs = []
    worst = (0, 0.0, 0, 0.0)
    with Timer("c16 scan"):
        for d in range(2, dmax + 1, 2):
            c = int(np.count_nonzero(P[: x + 1 - d] & P[d:]))
            pr = twin_S(d) * LI2
            z = (c - pr) / math.sqrt(pr)
            zs.append(z)
            if abs(z) > abs(worst[1]):
                worst = (d, z, c, pr)
    zs = np.array(zs)
    half = len(zs) // 2
    report("c16", {"x": x, "dmax": dmax, "z_mean": float(zs.mean()),
                   "z_sd": float(zs.std()), "z_max_abs": float(np.abs(zs).max()),
                   "worst_d": worst[0], "worst_z": round(worst[1], 2),
                   "drift_halves": [float(zs[:half].mean()), float(zs[half:].mean())],
                   "verdict": "REFUTED-uniformity" if np.abs(zs).max() > 5 else "holds"})
    del P


# ----------------------------------------------------------------- combined 4e9 sweep
def attack_sweep(X=4 * 10**9):
    """One segmented pass to 4e9 testing C19 (missing gaps + slope),
    C25 (c-hat stability), C21 (twin race trajectory), C18 (records),
    C04 (quintuplet count)."""
    H = (0, 2, 6, 12, 14)
    span = max(H)
    first = {}
    last_prime = None
    last_r = None
    pair_counts = np.zeros(4, dtype=np.int64)
    tw = {1: 0, 2: 0, 4: 0}
    twin_best, twin_records = 0, []
    last_twin = None
    quint = 0
    carry = np.zeros(span, dtype=bool)
    carry_lo = 0
    with Timer("4e9 sweep"):
        for lo, hi, seg in seg_sieve(X + span + 1, seg_size=1 << 24):
            pos = np.nonzero(seg)[0].astype(np.int64) + lo
            # C19 gaps
            pp = pos if last_prime is None else np.concatenate([[last_prime], pos])
            if len(pp) > 1:
                gaps = np.diff(pp)
                for g in np.unique(gaps):
                    g = int(g)
                    if g not in first:
                        first[g] = int(pp[int(np.argmax(gaps == g))])
                last_prime = int(pp[-1])
            # C25 mod 3
            p3 = pos[pos > 3]
            r = (p3 % 3).astype(np.int64)
            rr = r if last_r is None else np.concatenate([[last_r], r])
            if len(rr) > 1:
                idx = 2 * (rr[:-1] - 1) + (rr[1:] - 1)
                pair_counts += np.bincount(idx, minlength=4)
                last_r = int(rr[-1])
            # twins / quintuplets on carry-joined array
            comb = np.concatenate([carry, seg]) if lo else seg
            base = carry_lo if lo else 0
            starts = np.nonzero(comb[:-2] & comb[2:])[0] + base
            st5 = starts[starts > 5]
            rm = st5 % 5
            for cls in (1, 2, 4):
                tw[cls] += int(np.count_nonzero(rm == cls))
            spp = starts if last_twin is None else np.concatenate([[last_twin], starts])
            if len(spp) > 1:
                tg = np.diff(spp)
                big = np.nonzero(tg > twin_best)[0]
                for i in big:
                    if tg[i] > twin_best:
                        twin_best = int(tg[i])
                        twin_records.append((twin_best, int(spp[i])))
                last_twin = int(spp[-1])
            m = np.ones(len(comb) - span, dtype=bool)
            for h in H:
                m &= comb[h: len(comb) - span + h]
            qidx = np.nonzero(m)[0] + base
            quint += int(np.count_nonzero(qidx <= X))
            carry, carry_lo = seg[-span:].copy(), hi - span

    # C19 verdicts
    gs = sorted(first)
    missing = [g for g in range(2, max(gs), 2) if g not in first]
    fit_g = [g for g in gs if g >= 100]
    sq = np.array([math.sqrt(g) for g in fit_g])
    lp = np.array([math.log(first[g]) for g in fit_g])
    slope = float(np.sum(sq * lp) / np.sum(sq * sq))
    old_missing = {254, 256, 258, 262, 264, 266, 268, 270, 272, 274, 278, 280}
    filled = sorted(old_missing - set(missing))
    report("c19", {"X": X, "slope_g_ge_100": round(slope, 4),
                   "largest_gap": gs[-1], "missing_even_gaps": missing,
                   "gaps_filled_since_1e9": filled,
                   "verdict": "slope must keep falling toward ~0.94-1.0; got %.3f" % slope})
    n11, n12, n21, n22 = (int(v) for v in pair_counts)
    tot = n11 + n12 + n21 + n22
    s = (n11 + n22) / tot
    chat = (0.5 - s) * math.log(X) / math.log(math.log(X))
    report("c25", {"X": X, "same_fraction": round(s, 5), "c_hat": round(chat, 4),
                   "n11_over_n22": round(n11 / n22, 5),
                   "verdict": "c_hat should stay ~0.37-0.40; symmetric ratio ~1"})
    report("c21", {"X": X, "counts": tw,
                   "D1": tw[1] - (tw[2] + tw[4]) / 2.0,
                   "noise_scale": round(math.sqrt(tw[1] + (tw[2] + tw[4]) / 4.0), 0)})
    report("c18", {"X": X, "record": twin_best,
                   "record_over_log3": round(twin_best / math.log(X) ** 3, 4),
                   "records_tail": twin_records[-5:]})
    C4 = hl_tuple_constant(H, pmax=2_000_000)
    pred = C4 * li_k(X, 5)
    z = (quint - pred) / math.sqrt(pred)
    report("c04", {"X": X, "obs": quint, "pred": round(pred, 1),
                   "ratio": round(quint / pred, 4), "z": round(z, 2),
                   "verdict": "REFUTED-asymptotic" if abs(z) > 5 else "holds"})


# ----------------------------------------------------------------- C20 at 4e9
def attack_c20(x0=4 * 10**9, width=2 * 10**8):
    CDEF = EULER_GAMMA + math.log(2 * math.pi) - 1
    pos = []
    with Timer("c20 window sieve"):
        for lo, hi, seg in seg_sieve(x0 + width, seg_size=1 << 24, start=x0):
            pos.append(np.nonzero(seg)[0].astype(np.int64) + lo)
    pos = np.concatenate(pos)
    logx = math.log(x0)
    rows = []
    for lam in (1.0, 2.0):
        h = lam * logx
        edges = np.arange(x0, x0 + width, h)
        counts, _ = np.histogram(pos, bins=edges)
        ratio = float(counts.var() / counts.mean())
        pred = 1 - (math.log(h) + CDEF) / logx
        rows.append({"lambda": lam, "var_over_mean": round(ratio, 4),
                     "predicted": round(pred, 4),
                     "gap": round(ratio - pred, 4)})
    report("c20", {"x0": x0, "rows": rows,
                   "verdict": "prediction must be closer than naive 1.0"})


# ----------------------------------------------------------------- C22 larger q
def attack_c22(qlo=3000, qhi=6000, plim=2 * 10**7):
    with Timer("c22 primes"):
        primes = primes_up_to(plim).astype(np.int64)
    grid = np.linspace(2.0, float(plim), 2_000_001)
    lig = np.concatenate([[0.0], np.cumsum(np.diff(grid) /
                                           np.log(grid[:-1] + np.diff(grid) / 2))])
    means = []
    with Timer("c22 scan"):
        for q in range(qlo + 1, qhi + 1, 7):  # sample every 7th q
            r = primes % q
            cl, fi = np.unique(r, return_index=True)
            keep = np.gcd(cl, q) == 1
            phi = int(np.count_nonzero(np.gcd(np.arange(1, q + 1), q) == 1))
            if int(keep.sum()) != phi:
                continue
            U = np.interp(primes[fi[keep]].astype(float), grid, lig) / phi
            means.append((q, float(U.mean())))
    qs = np.array([m[0] for m in means], dtype=float)
    us = np.array([m[1] for m in means])
    lo_m = float(us[qs < (qlo + qhi) / 2].mean())
    hi_m = float(us[qs >= (qlo + qhi) / 2].mean())
    report("c22", {"q_range": [qlo, qhi], "n_q": len(means),
                   "mean_U_lower_half": round(lo_m, 4),
                   "mean_U_upper_half": round(hi_m, 4),
                   "theta_upper": round((1 - hi_m) * math.log((qlo + 3 * qhi) / 4), 3),
                   "verdict": "recovery toward 1 must continue (upper >= lower)"})


ATTACKS = {"c14": attack_c14, "c15": attack_c15, "c17": attack_c17,
           "c13": attack_c13, "c16": attack_c16, "sweep": attack_sweep,
           "c20": attack_c20, "c22": attack_c22}

if __name__ == "__main__":
    which = sys.argv[1:] or list(ATTACKS)
    for name in which:
        print("\n########## attack %s" % name)
        try:
            ATTACKS[name]()
        except Exception as exc:  # keep the battery going
            report(name, {"ERROR": repr(exc)})
    path = os.path.join(ROOT, "results", "adversarial.json")
    old = {}
    if os.path.exists(path):
        old = json.load(open(path))
    old.update(OUT)
    with open(path, "w") as fh:
        json.dump(old, fh, indent=2)
    print("\n[saved -> results/adversarial.json]")
