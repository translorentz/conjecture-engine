#!/usr/bin/env python3
"""Targeted finite diagnostics for the research-quality set of 25 conjectures.

The computations are deliberately modest.  They test definitions, exact algebraic
relations, finite structural predictions, null cases, and the direction of proposed
asymptotics.  They are not presented as evidence of proof or certified novelty.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import skew, kurtosis
from scipy.integrate import quad
from sympy import Poly, factor_list, factorint, mobius, symbols

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import experiment_core as core


def singular_series(H: tuple[int, ...], prime_bound: int = 2000) -> float:
    """Truncated Hardy--Littlewood singular series for a finite integer set."""
    H = tuple(sorted(set(H)))
    k = len(H)
    ps = np.flatnonzero(core.prime_sieve(prime_bound))
    value = 1.0
    for p0 in ps:
        p = int(p0)
        nu = len({h % p for h in H})
        if nu == p:
            return 0.0
        value *= (1.0 - nu / p) / ((1.0 - 1.0 / p) ** k)
    return float(value)


def admissible(H: tuple[int, ...]) -> bool:
    H = tuple(sorted(set(H)))
    for p in np.flatnonzero(core.prime_sieve(max(20, len(H) + 5))):
        p = int(p)
        if len({h % p for h in H}) == p:
            return False
    return True


def overlap_size(H: tuple[int, ...], K: tuple[int, ...], t: int) -> int:
    return len(set(H).intersection({x + t for x in K}))


def overlap_matrices(motifs: list[tuple[int, ...]]) -> dict:
    """Exact finite overlap-incidence matrices, weighted by truncated singular series."""
    max_d = max(max(H) - min(H) for H in motifs)
    levels: dict[int, np.ndarray] = {}
    raw_counts: dict[int, np.ndarray] = {}
    for i, H in enumerate(motifs):
        for j, K in enumerate(motifs):
            lo = min(H) - max(K) - max_d
            hi = max(H) - min(K) + max_d
            for t in range(lo, hi + 1):
                r = overlap_size(H, K, t)
                if r <= 0:
                    continue
                U = tuple(sorted(set(H).union({x + t for x in K})))
                levels.setdefault(r, np.zeros((len(motifs), len(motifs))))
                raw_counts.setdefault(r, np.zeros((len(motifs), len(motifs))))
                levels[r][i, j] += singular_series(U, 500)
                raw_counts[r][i, j] += 1
    return {
        str(r): {
            "weighted_matrix": levels[r].tolist(),
            "raw_overlap_count_matrix": raw_counts[r].tolist(),
            "rank": int(np.linalg.matrix_rank(levels[r], tol=1e-9)),
            "eigenvalues": np.linalg.eigvalsh((levels[r] + levels[r].T) / 2).tolist(),
        }
        for r in sorted(levels, reverse=True)
    }


def prime_program(isprime: np.ndarray, N: int) -> dict:
    base = core.prime_pattern_suite(isprime, N)
    motifs = [(0, 2), (0, 4), (0, 6), (0, 10)]

    # C1: connected cumulant diagnostics already computed in core.
    c1 = base["C1_connected_field"]

    # C2: exact overlap levels.
    c2 = {
        "motifs": [list(H) for H in motifs],
        "overlap_levels": overlap_matrices(motifs),
        "empirical_covariance_eigenmodes": base["C2_overlap_variance_hierarchy"],
    }

    # C3: empirical Wiener--Khinchin identity and local singular-series side.
    H = (0, 2)
    field = np.ones(N - max(H), dtype=np.float64)
    for h in H:
        field *= isprime[h:h + len(field)]
    field -= field.mean()
    M = min(300_000, len(field))
    f = field[-M:]
    fft = np.fft.rfft(f)
    spec = (np.abs(fft) ** 2) / M
    ac = np.fft.irfft(np.abs(fft) ** 2, n=M) / M
    recon = np.fft.rfft(ac)
    wk_error = float(np.max(np.abs(recon.real - spec)) / max(1.0, np.max(spec)))
    local_rows = []
    for t in range(1, 101):
        U = tuple(sorted(set(H).union({x + t for x in H})))
        local_rows.append({
            "shift": t,
            "overlap": overlap_size(H, H, t),
            "admissible": admissible(U),
            "truncated_singular_series": singular_series(U, 1000),
        })
    c3 = {
        "wiener_khinchin_relative_error": wk_error,
        "local_connected_input_first_100_shifts": local_rows,
        "warning": "The multiple-zero spectral matching is not computationally tested at this range.",
    }

    # C4: the polymer graph includes chains not seen by the finite difference graph.
    H6 = (0, 6)
    start_sets = []
    for A in itertools.combinations(range(0, 19, 6), 3):
        union = tuple(sorted({h + t for t in A for h in H6}))
        edges = [(u, v) for u, v in itertools.combinations(A, 2)
                 if set(h + u for h in H6).intersection(h + v for h in H6)]
        # connectivity on occurrence starts
        seen = {A[0]}
        changed = True
        while changed:
            changed = False
            for u, v in edges:
                if u in seen and v not in seen:
                    seen.add(v); changed = True
                if v in seen and u not in seen:
                    seen.add(u); changed = True
        if len(seen) == len(A):
            start_sets.append({
                "starts": list(A), "union": list(union), "admissible": admissible(union),
                "truncated_singular_series": singular_series(union, 2000),
            })
    # empirical runs of sexy-prime-pair starts spaced by 6
    starts = np.flatnonzero(isprime[:-6] & isprime[6:])
    sset = set(map(int, starts))
    run_lengths = []
    for s in starts:
        s = int(s)
        if s - 6 in sset:
            continue
        r = 1
        while s + 6 * r in sset:
            r += 1
        run_lengths.append(r)
    c4 = {
        "connected_three_start_polymers": start_sets,
        "empirical_sexy_pair_run_length_counts": dict(Counter(run_lengths)),
        "three_start_chain_polymer_admissible": any(x["starts"] == [0, 6, 12] and x["admissible"] for x in start_sets),
    }

    # C5: first odd cumulants and the Kuperberg-calibrating scale, for prime counts.
    prime_indicator = isprime.astype(float)
    odd = {}
    X = N / 2
    for L in (500, 1500, 5000, 15000):
        counts = core.moving_sum(prime_indicator, L)
        idx = np.arange(N // 3, min(len(counts), N - L), max(1, L // 3))
        z = counts[idx] - counts[idx].mean()
        k3 = float(np.mean(z ** 3))
        k5 = float(np.mean(z ** 5) - 10 * np.mean(z ** 3) * np.mean(z ** 2))
        scale3 = L * (math.log(max(L, 3)) ** 2)
        scale5 = (L ** 2) * (math.log(max(L, 3)) ** 3)
        odd[str(L)] = {
            "samples": int(len(z)), "third_cumulant": k3, "fifth_cumulant": k5,
            "third_over_h_logh2": k3 / scale3,
            "fifth_over_h2_logh3": k5 / scale5,
            "skew": float(skew(z, bias=False)), "excess_kurtosis": float(kurtosis(z, fisher=True, bias=False)),
        }
    c5 = odd
    return {"C1": c1, "C2": c2, "C3": c3, "C4": c4, "C5": c5}


def multiplicative_character_powers(q: int, centered: np.ndarray, max_order: int = 6) -> dict:
    """Powers for characters obtained from a primitive root of prime q."""
    # find primitive root
    factors = list(factorint(q - 1))
    g = next(a for a in range(2, q) if all(pow(a, (q - 1)//r, q) != 1 for r in factors))
    logtab = np.empty(q, dtype=int); x = 1
    for j in range(q - 1):
        logtab[x] = j; x = (x * g) % q
    vals = centered[1:]
    residues = np.arange(1, q)
    out = {}
    for k in range(1, min(max_order, q - 2) + 1):
        chi = np.exp(2j * math.pi * k * logtab[residues] / (q - 1))
        out[str(k)] = float(abs(np.dot(vals, np.conjugate(chi))) ** 2 / (q - 1))
    return out



def operator_projection_diagnostic(centered: np.ndarray, q: int) -> dict:
    """Project f tensor f onto additive-difference and multiplicative-ratio matrix algebras."""
    residues = np.arange(1, q, dtype=np.int64)
    n = q - 1
    R = np.outer(centered[1:], centered[1:])
    y = R.reshape(-1)
    cols = []
    labels = []
    aa = residues[:, None]
    bb = residues[None, :]
    diffs = (aa - bb) % q
    ratios = (aa * np.array([pow(int(b), -1, q) for b in residues])[None, :]) % q
    # Drop one column from each family to reduce exact dependencies; lstsq handles the rest.
    for h in range(q):
        col = (diffs == h).astype(float).reshape(-1)
        norm = np.linalg.norm(col)
        if norm:
            cols.append(col / norm); labels.append(('A', h))
    for r in range(1, q):
        col = (ratios == r).astype(float).reshape(-1)
        norm = np.linalg.norm(col)
        if norm:
            cols.append(col / norm); labels.append(('M', r))
    X = np.column_stack(cols)
    coef, *_ = np.linalg.lstsq(X, y, rcond=1e-10)
    proj = X @ coef
    residual = y - proj
    add_part = X[:, [i for i,l in enumerate(labels) if l[0]=='A']] @ coef[[i for i,l in enumerate(labels) if l[0]=='A']]
    mult_part = X[:, [i for i,l in enumerate(labels) if l[0]=='M']] @ coef[[i for i,l in enumerate(labels) if l[0]=='M']]
    yn = np.linalg.norm(y)
    return {
        'q': q,
        'matrix_dimension': n,
        'relative_residual_hs': float(np.linalg.norm(residual)/yn) if yn else 0.0,
        'additive_component_norm_over_total': float(np.linalg.norm(add_part)/yn) if yn else 0.0,
        'multiplicative_component_norm_over_total': float(np.linalg.norm(mult_part)/yn) if yn else 0.0,
        'design_rank': int(np.linalg.matrix_rank(X, tol=1e-9)),
        'design_columns': int(X.shape[1]),
    }

def occupancy_program(primes: np.ndarray) -> dict:
    occ, rows = core.least_prime_occupancy(primes, q_max=1200)
    # Recompute a smaller detailed sample with multiplicative powers.
    detailed = []
    for row in rows[::max(1, len(rows)//35)]:
        q = row["q"]
        least = np.zeros(q, dtype=np.int64); least[0] = q; remaining = q - 1
        for p0 in primes:
            p = int(p0)
            if p == q: continue
            a = p % q
            if a and least[a] == 0:
                least[a] = p; remaining -= 1
                if remaining == 0: break
        u = np.array([core.li(int(x)) for x in least], dtype=float)/(q - 1)
        centered = u - u.mean()
        add = np.abs(np.fft.fft(centered))**2/q
        mult = multiplicative_character_powers(q, centered)
        detailed.append({
            "q": q,
            "additive_low_power": float(np.mean(add[1:6])),
            "additive_bulk_power": float(np.mean(add[q//4:3*q//4])),
            "multiplicative_powers": mult,
            "terminal_excesses": np.sort(u[1:] - math.log(q - 1))[-8:].tolist(),
        })
    addv = np.array([d["additive_low_power"] for d in detailed])
    multv = np.array([d["multiplicative_powers"].get("1", 0.0) for d in detailed])

    c6 = {
        "compact_time_and_mean_shift_diagnostics": occ,
        "warning": "The data do not distinguish the full connected expansion from a pair-only approximation.",
    }
    transfer_rows=[]
    selected=(53,79,101,127,149)
    for q in selected:
        least=np.zeros(q,dtype=np.int64);least[0]=q;remaining=q-1
        for p0 in primes:
            pp=int(p0)
            if pp==q:continue
            a=pp%q
            if a and least[a]==0:
                least[a]=pp;remaining-=1
                if remaining==0:break
        u=np.array([core.li(int(x)) for x in least],dtype=float)/(q-1)
        f=u-u.mean()
        A=np.fft.fft(f)/math.sqrt(q)
        factors=list(factorint(q-1))
        g=next(a for a in range(2,q) if all(pow(a,(q-1)//r,q)!=1 for r in factors))
        logtab=np.empty(q,dtype=int);x=1
        for j in range(q-1):logtab[x]=j;x=(x*g)%q
        residues=np.arange(1,q)
        errs=[];energies={}
        for k in range(1,min(6,q-2)+1):
            chi=np.exp(2j*math.pi*k*logtab[residues]/(q-1))
            M=np.dot(f[1:],np.conjugate(chi))/math.sqrt(q-1)
            tau=np.sum(np.conjugate(chi)*np.exp(2j*math.pi*residues/q))
            rhs=tau/math.sqrt(q*(q-1))*np.sum(A[1:]*np.exp(2j*math.pi*k*logtab[residues]/(q-1)))
            errs.append(abs(M-rhs)/max(1.0,abs(M)))
            energies[str(k)]=float(abs(M)**2)
        ac={str(h):float(np.mean(f*np.roll(f,-h))) for h in range(1,11)}
        transfer_rows.append({"q":q,"gauss_transfer_max_relative_error":float(max(errs)),
                              "additive_autocorrelation_lags_1_10":ac,
                              "multiplicative_character_energies":energies})
    projection_rows=[]
    for q in selected:
        least=np.zeros(q,dtype=np.int64);least[0]=q;remaining=q-1
        for p0 in primes:
            pp=int(p0)
            if pp==q:continue
            a=pp%q
            if a and least[a]==0:
                least[a]=pp;remaining-=1
                if remaining==0:break
        u=np.array([core.li(int(x)) for x in least],dtype=float)/(q-1)
        projection_rows.append(operator_projection_diagnostic(u-u.mean(),q))
    c7 = {
        "sampled_moduli": detailed,
        "gauss_transfer_and_autocorrelation_rows": transfer_rows,
        "operator_projection": projection_rows,
        "cross_correlation_low_additive_vs_first_multiplicative_power": float(np.corrcoef(addv, multv)[0,1]) if len(detailed)>2 else None,
        "warning": "The exact Gauss identity is checked; the arithmetic asymptotics of the two autocorrelation families remain untested.",
    }
    # Terminal exceedance counts after empirical common centering by log(q-1).
    thresholds = (-1.0, 0.0, 1.0)
    c8 = {str(x): {} for x in thresholds}
    for x in thresholds:
        counts = np.array([sum(v > x for v in d["terminal_excesses"]) for d in detailed], dtype=float)
        c8[str(x)] = {"mean": float(counts.mean()), "variance": float(counts.var(ddof=1)),
                      "poisson_target_e_minus_x": math.exp(-x), "sample_moduli": len(counts)}
    # C9: null diagnostic; no exceptional-zero ensemble is claimed.
    c9 = {
        "quadratic_projection_L1_proxy_spearman": occ["char_projection_L1_spearman"],
        "interpretation": "No exceptional conductor occurs in the range; this is intentionally a null diagnostic.",
    }
    # C10 class-group conditioning: only genus rank, not exact discriminant factors.
    c10 = core.class_group_local_independence(18000)
    return {"C6": c6, "C7": c7, "C8": c8, "C9": c9, "C10": c10}


def finite_log_large_sieve(ps: list[int], base: int, Ms=(4, 8, 16, 32, 64)) -> dict:
    q = np.array([core.fermat_quotient(p, base)/p for p in ps])
    out = {}
    N = len(ps)
    for M in Ms:
        sums = np.array([abs(np.sum(np.exp(2j*math.pi*m*q)))**2 for m in range(1, M+1)])
        out[str(M)] = {
            "frequency_energy": float(sums.sum()),
            "large_sieve_shape_M_plus_N_times_N": float((M + N) * N),
            "ratio": float(sums.sum()/((M+N)*N)),
            "max_single_frequency_over_N": float(np.sqrt(sums.max())/N),
        }
    return out


def family_wieferich(H: int = 3000, tuple_samples: int = 500, seed: int = 7) -> dict:
    rng = np.random.default_rng(seed)
    primes = [int(p) for p in np.flatnonzero(core.prime_sieve(int(H**0.45))) if p >= 3]
    out = {}
    for r in (1, 2):
        counts = []
        for _ in range(tuple_samples):
            aa = [int(rng.integers(2, H+1)) for _ in range(r)]
            count = 0
            for p in primes:
                if any(a % p == 0 for a in aa):
                    continue
                if all(pow(a, p-1, p*p) == 1 for a in aa):
                    count += 1
            counts.append(count)
        lam = sum(((1-1/p)**r)*p**(-r) for p in primes)
        out[str(r)] = {
            "sample_size": tuple_samples, "prime_max": max(primes),
            "mean_count": float(np.mean(counts)), "variance": float(np.var(counts, ddof=1)),
            "poisson_mean_sum_p_minus_r": float(lam), "histogram": dict(Counter(counts)),
        }
    return out


def toric_functoriality(ps: list[int]) -> dict:
    # Split-torus morphism phi(x,y)=x^2 y^3; corrected logarithm is -q_p on G_m.
    errors = []
    norm_errors = []
    power_errors = []
    for p in ps:
        if p in (2,3,5): continue
        l2 = (-core.fermat_quotient(p, 2)) % p
        l3 = (-core.fermat_quotient(p, 3)) % p
        phi = (2**2)*(3**3)
        lp = (-core.fermat_quotient(p, phi)) % p
        errors.append((lp - (2*l2 + 3*l3)) % p)
        B, A, chi = core.toric_fermat_quotient_sqrt2(p)
        norm_errors.append(A)
        # Power morphism on norm-one torus: ell(P^2)=2ell(P).
        mod = p*p
        eta2 = core.quad_pair_mul((3,2),(3,2),mod,2)
        a,b = core.quad_pair_pow(eta2,p-chi,mod,2)
        B2=((b%mod)//p)%p
        power_errors.append((B2-2*B)%p)
    return {
        "split_torus_morphism_max_error": int(max(errors) if errors else 0),
        "norm_relation_max_scalar_error": int(max(norm_errors) if norm_errors else 0),
        "norm_one_power_morphism_max_error": int(max(power_errors) if power_errors else 0),
    }


def finite_log_program(primes: np.ndarray) -> dict:
    base = core.fermat_suite(primes, pmax=120000)
    ps = [int(p) for p in primes if 7 <= p <= 120000]
    c11 = {
        "relation_errors": base["relation_errors"],
        "marginal_fourier": base["marginal_fourier"],
        "joint_fourier": base["joint_fourier"],
    }
    c12 = finite_log_large_sieve(ps, 2)
    harmonic = {"rank1_sum": sum(1/p for p in ps), "rank2_sum": sum(1/(p*p) for p in ps)}
    shrink={}
    for alpha in (0.4,0.6,0.8):
        B=1.0
        obs1=obs2=0
        pred1=pred2=0.0
        for p in ps:
            w=int(B*(p**(1-alpha)))
            q2=core.fermat_quotient(p,2);q3=core.fermat_quotient(p,3)
            d2=min(q2,p-q2);d3=min(q3,p-q3)
            obs1+=int(d2<=w);obs2+=int(d2<=w and d3<=w)
            mass=(2*w+1)/p
            pred1+=mass;pred2+=mass*mass
        shrink[str(alpha)]={"rank1_observed":obs1,"rank1_haar_sum":pred1,
                            "rank2_observed":obs2,"rank2_haar_sum":pred2}
    exact_logtimes={str(a):[math.log(math.log(p)) for p in hits] for a,hits in base["exact_hits"].items()}
    c13 = {"exact_hits": base["exact_hits"], "exact_hit_loglog_times":exact_logtimes,
           "heuristic_sums": harmonic,"shrinking_box_counts":shrink,
           "near_zero_counts": base["near_zero_counts"]}
    c14 = family_wieferich()
    c15 = {"functoriality_checks": toric_functoriality(ps[:5000]),
           "equidistribution_checks": base["C15_toric_finite_logarithm"]}
    return {"C11": c11, "C12": c12, "C13": c13, "C14": c14, "C15": c15}


def critical_orbit_polys(max_n: int = 5):
    c = symbols('c')
    v = {0: Poly(0, c, domain='ZZ')}
    expr = 0
    for n in range(1, max_n+1):
        expr = expr**2 + c
        v[n] = Poly(expr, c, domain='ZZ')
    psi = {}
    for n in range(1, max_n+1):
        num = Poly(1, c, domain='ZZ')
        den = Poly(1, c, domain='ZZ')
        for d in range(1, n+1):
            if n % d: continue
            mu = int(mobius(n//d))
            if mu == 1: num *= v[d]
            elif mu == -1: den *= v[d]
        q, r = divmod(num, den)
        if not r.is_zero:
            raise ArithmeticError(f"dynatomic division failed at n={n}")
        psi[n] = q
    return c, v, psi


def eval_poly_mod(poly: Poly, x: int, mod: int) -> int:
    val = 0
    for coeff in poly.all_coeffs():
        val = (val*x + int(coeff)) % mod
    return val


def squarefree_local_product(poly: Poly, prime_bound: int = 47, earlier: list[Poly] | None = None) -> tuple[float, dict]:
    prod = 1.0; rows = {}
    earlier = earlier or []
    for p in np.flatnonzero(core.prime_sieve(prime_bound)):
        p = int(p); mod = p*p
        rho = sum(eval_poly_mod(poly, a, mod) == 0
                  and all(eval_poly_mod(v, a, p) != 0 for v in earlier)
                  for a in range(mod))
        delta = rho/mod
        prod *= 1-delta
        rows[str(p)] = {"rho_mod_p2": rho, "delta": delta}
    return prod, rows


def factor_value_by_components(polys: list[Poly], cval: int) -> list[dict[int,int]]:
    return [factorint(abs(int(poly.eval(cval)))) if abs(int(poly.eval(cval))) > 1 else {} for poly in polys]



def binary_wreath_parity_distribution(level: int) -> tuple[dict[int,float],dict[int,float]]:
    """Fixed-leaf distributions in full C2-wreath group and its total-swap-parity kernel."""
    joint={(0,1):1.0}  # (parity, fixed leaves) at level 0
    for _ in range(level):
        nxt=defaultdict(float)
        items=list(joint.items())
        for (pl,kl),vl in items:
            for (pr,kr),vr in items:
                for root_swap in (0,1):
                    par=root_swap^pl^pr
                    fixed=0 if root_swap else kl+kr
                    nxt[(par,fixed)]+=0.5*vl*vr
        joint=dict(nxt)
    full=defaultdict(float);even=defaultdict(float)
    peven=sum(v for (p,k),v in joint.items() if p==0)
    for (par,k),v in joint.items():
        full[k]+=v
        if par==0: even[k]+=v/peven
    return dict(full),dict(even)

def sampling_proxy(mu: dict[int,float], N: int) -> float:
    return 0.5*sum(min(x, math.sqrt(x/N)) for x in mu.values())

def arboreal_program(primes: np.ndarray) -> dict:
    old = core.dynamics_suite(primes)
    # C16 finite-index universality diagnostic on a coarse fixed-leaf quotient.
    c16 = {"empirical_fixed_level": old["C16_growing_arboreal_chebotarev"], "full_vs_index2": {}}
    for level in (2,3,4,5,6):
        full,even=binary_wreath_parity_distribution(level)
        grid=[10,30,100,300,1000,3000,10000,30000,100000]
        crit_full=next((N for N in grid if sampling_proxy(full,N)<=0.1),None)
        crit_even=next((N for N in grid if sampling_proxy(even,N)<=0.1),None)
        c16["full_vs_index2"][str(level)]={"full_distribution":full,"even_subgroup_distribution":even,
            "collision_effective_full":1/sum(x*x for x in full.values()),
            "collision_effective_even":1/sum(x*x for x in even.values()),
            "proxy_critical_sample_full":crit_full,"proxy_critical_sample_even":crit_even}

    # C17 exact iid sampling functional for the observed finite state laws.
    c17 = {}
    for n, row in old["C16_growing_arboreal_chebotarev"].items():
        mu = np.array(list(row["wreath_distribution"].values()), dtype=float)
        for sample_n in (50, 200, 1000):
            sampling_bound = 0.5*sum(min(x, math.sqrt(x/sample_n)) for x in mu)
            missing_mass = sum(x*math.exp(-sample_n*x) for x in mu)
            c17.setdefault(n, {})[str(sample_n)] = {
                "sampling_L1_functional": float(sampling_bound),
                "poissonized_expected_missing_mass": float(missing_mass),
            }

    c, v, psi = critical_orbit_polys(4)
    # C18 coloured dynatomic components at level 4.
    facs = [Poly(f, c, domain='ZZ') for f, _ in factor_list(psi[4].as_expr())[1]]
    color_stats = []
    for cv in range(-45, 46):
        if cv in (-2,-1,0): continue
        comps = factor_value_by_components(facs, cv)
        if not comps or any(not ff for ff in comps): continue
        masses = []
        for ff in comps:
            total = sum(e*math.log(p) for p,e in ff.items())
            masses.append(max((math.log(p)/total for p in ff), default=0.0))
        color_stats.append(masses)
    c18 = {
        "level": 4, "dynatomic_degree": psi[4].degree(),
        "irreducible_component_degrees": [f.degree() for f in facs],
        "samples": len(color_stats),
        "mean_largest_share_by_component": np.mean(np.array(color_stats), axis=0).tolist() if color_stats else [],
    }

    # C19 level-dependent local Euler product; no false stabilization in n.
    c19 = {}
    for n in (2,3,4):
        poly = psi[n]
        local_prod, rows = squarefree_local_product(poly, 43, earlier=[v[m] for m in range(1, n)])
        vals=[]
        for cv in range(-120,121):
            if cv in (-2,-1,0): continue
            val=abs(int(poly.eval(cv)))
            if val<=1: continue
            vals.append(all(e==1 for e in factorint(val).values()))
        c19[str(n)] = {
            "degree": poly.degree(), "empirical_squarefree_fraction": float(np.mean(vals)),
            "truncated_local_product_p_le_43": local_prod,
            "local_rows": rows,
        }

    # C20 synchronized divisor-sensitive gcd examples.
    unrelated=[]; diagonal=[]
    for a in range(2,15):
        for b in range(a+1,16):
            xa, xb = a, b
            for n in range(1,7):
                xa=xa*xa+1; xb=xb*xb+2
            unrelated.append(math.log(math.gcd(xa,xb))/max(math.log(xa),math.log(xb)))
        x=a
        for n in range(1,7): x=x*x+1
        diagonal.append(1.0)  # gcd(x,x)=x, exact divisor-compatible periodic diagonal
    c20 = {"unrelated_mean_normalized_gcd":float(np.mean(unrelated)),
           "unrelated_max_normalized_gcd":float(np.max(unrelated)),
           "divisor_compatible_diagonal_ratio":1.0}
    return {"C16": c16, "C17": c17, "C18": c18, "C19": c19, "C20": c20}


def exact_local_states(polys: list[list[int]], p: int) -> dict:
    counts=Counter()
    for a in range(p):
        state=[]
        for coeffs in polys:
            val=sum(c*pow(a,i,p) for i,c in enumerate(coeffs))%p
            state.append(int(val==0))
        counts[tuple(state)] += 1
    return {''.join(map(str,k)):v for k,v in sorted(counts.items())}




def buchstab_component(u: float, j: int) -> float:
    """Generalized Buchstab component from the ordered-factor simplex formula."""
    if j < 1 or u < j:
        return 0.0
    if j == 1:
        return 1.0/u
    def J(k: int, s: float) -> float:
        if k == 0:
            return 1.0
        if s < k:
            return 0.0
        val,_=quad(lambda tt: J(k-1,s-tt)/tt,1.0,s-k+1,epsabs=1e-8,epsrel=1e-8,limit=100)
        return val/k
    return J(j-1,u-1)/u

def factor_count_flow_sample(lo: int=70000, count: int=3000, seed: int=17) -> dict:
    """Compare y-rough factor-count profiles for n^2+1 with uniform integers of similar size."""
    rng=np.random.default_rng(seed)
    ns=np.arange(lo,lo+count,dtype=np.int64)
    poly_vals=[int(n*n+1) for n in ns]
    low=min(poly_vals);high=max(poly_vals)
    random_vals=[int(x) for x in rng.integers(low,high+1,size=count)]
    poly_fac=[factorint(v) for v in poly_vals]
    random_fac=[factorint(v) for v in random_vals]
    rows={}
    for y in (31,71,151,313):
        def dist(facs):
            ctr=Counter();surv=0
            for ff in facs:
                if min(ff)<=y: continue
                surv+=1;ctr[sum(ff.values())]+=1
            return {str(k):v/surv for k,v in sorted(ctr.items())} if surv else {},surv
        pd,pn=dist(poly_fac);rd,rn=dist(random_fac)
        mean_u=float(np.mean([math.log(v)/math.log(y) for v in poly_vals]))
        comps={j:buchstab_component(mean_u,j) for j in range(1,int(mean_u)+2)}
        total=sum(comps.values())
        pred={str(j):v/total for j,v in comps.items() if v>1e-12}
        rows[str(y)]={"mean_u":mean_u,"polynomial_survivors":pn,"random_integer_survivors":rn,
                      "polynomial_conditional_Omega":pd,"random_conditional_Omega":rd,
                      "buchstab_component_prediction_at_mean_u":pred,
                      "component_sum":total,"buchstab_omega":core.buchstab_omega(mean_u)}
    endpoint_y=math.isqrt(max(poly_vals))+1
    endpoint_composites=sum(1 for v,ff in zip(poly_vals,poly_fac) if min(ff)>endpoint_y and sum(ff.values())>1)
    return {"interval":[lo,lo+count-1],"rows":rows,"endpoint_y":endpoint_y,
            "endpoint_rough_composites":endpoint_composites}

def factorization_program(primes: np.ndarray) -> dict:
    old = core.polynomial_suite(primes, N=1600)
    c21=old["C21_frobenius_marked_PD"]
    c22=old["C22_small_large_independence"]
    # C23 exact local states and conditioned residual correlations.
    polys=[[1,0,1],[1,1,1]]
    local={str(p):exact_local_states(polys,p) for p in (2,3,5,7,11,13)}
    M=5000; groups=defaultdict(list)
    for n in range(1,M+1):
        a=n*n+1; b=n*n+n+1
        small_state=tuple((a%p==0,b%p==0) for p in (2,3,5,7))
        fa=factorint(a);fb=factorint(b)
        la=math.log(max(fa))/math.log(a);lb=math.log(max(fb))/math.log(b)
        groups[small_state].append((la,lb))
    cors=[]
    for vals in groups.values():
        if len(vals)>=80:
            ar=np.array(vals)
            cors.append(float(np.corrcoef(ar[:,0],ar[:,1])[0,1]))
    c23={"exact_local_state_counts":local,"adequate_conditioning_cells":len(cors),
         "mean_conditioned_largest_factor_correlation":float(np.mean(cors)) if cors else None,
         "unconditioned":old["C23_colored_components"]}

    # C24 uses true smoothness (largest prime <= y), not largest-share proxies.
    ys=(251,501,1001,2003)
    joint={}
    vals=[]
    for n in range(1,8001):
        a=n*n+1;b=n*n+n+1
        fa=factorint(a);fb=factorint(b)
        vals.append((max(fa),max(fb)))
    for y in ys:
        A=np.array([x<=y for x,_ in vals]);B=np.array([z<=y for _,z in vals])
        pa=float(A.mean());pb=float(B.mean());pj=float((A&B).mean())
        joint[str(y)]={"marginal_1":pa,"marginal_2":pb,"joint":pj,
                       "joint_over_product":pj/(pa*pb) if pa*pb else None}
    c24={"true_smoothness_thresholds":joint,"exact_local_states":local}

    # C25 dyadic interval calculation.
    lo,hi=70000,140000
    ns=np.arange(lo,hi+1,dtype=np.int64);vals_arr=ns*ns+1
    isprime_vals=np.array([core.is_prime64(int(v)) for v in vals_arr])
    rows=[]
    C=1.0
    for p0 in primes[primes<=7000]:
        p=int(p0);rho=core.root_count_poly_mod_p([1,0,1],p)
        C*=(1-rho/p)/(1-1/p)
    for y in (13,31,71,151,313):
        survive=np.ones(len(ns),dtype=bool);V=1.0
        for p0 in primes[primes<=y]:
            p=int(p0);rho=core.root_count_poly_mod_p([1,0,1],p)
            V*=1-rho/p
            if rho:survive &= vals_arr%p!=0
        log_scale=float(np.mean(np.log(vals_arr)))
        u=log_scale/math.log(y);pred_rough=V*math.exp(0.5772156649015329)*core.buchstab_omega(u)
        obs_rough=float(survive.mean());obs_cond=float(isprime_vals[survive].mean())
        pred_prime=C/log_scale;pred_cond=pred_prime/pred_rough
        rows.append({"y":y,"u_dyadic_mean":u,"observed_rough":obs_rough,"predicted_rough":pred_rough,
                     "rough_ratio":obs_rough/pred_rough,"observed_conditional_prime":obs_cond,
                     "predicted_conditional_prime":pred_cond,"conditional_ratio":obs_cond/pred_cond})
    c25={"dyadic_interval":[lo,hi],"roughness_rows":rows,
          "factor_count_flow":factor_count_flow_sample()}
    return {"C21":c21,"C22":c22,"C23":c23,"C24":c24,"C25":c25}


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--out', default=str(HERE/'research_quality_25_results.json'))
    ap.add_argument('--prime-max', type=int, default=3_000_000)
    args=ap.parse_args()
    started=time.perf_counter()
    isprime=core.prime_sieve(args.prime_max)
    primes=np.flatnonzero(isprime)
    results={
        "metadata":{"prime_max":args.prime_max,"deterministic":True,
                    "warning":"Finite diagnostics only; not evidence of proof or priority."},
        "program_I":prime_program(isprime,args.prime_max-30),
        "program_II":occupancy_program(primes),
        "program_III":finite_log_program(primes),
        "program_IV":arboreal_program(primes),
        "program_V":factorization_program(primes),
    }
    results["metadata"]["runtime_seconds"]=time.perf_counter()-started
    Path(args.out).write_text(json.dumps(results,indent=2,sort_keys=True))
    print(args.out)

if __name__=='__main__':
    main()
