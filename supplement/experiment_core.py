#!/usr/bin/env python3
"""Finite-range stress tests for 25 structural number-theory conjectures.

The computations are diagnostics, not evidence of proof. Every output is tied to a
specific discriminating prediction (relation, scale, sign, kernel, or null case).
The script is deterministic and records all bounds.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.fft import rfft, irfft, next_fast_len
from scipy.special import expi
from scipy.stats import skew, kurtosis, kstest, expon, norm, spearmanr
from sympy import factorint



def is_prime64(x:int)->bool:
    if x<2:return False
    small=(2,3,5,7,11,13,17,19,23,29,31,37)
    for p in small:
        if x%p==0:return x==p
    d=x-1;s=0
    while d%2==0:s+=1;d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%x==0:continue
        y=pow(a,d,x)
        if y in (1,x-1):continue
        for _ in range(s-1):
            y=y*y%x
            if y==x-1:break
        else:return False
    return True


def prime_sieve(n: int) -> np.ndarray:
    a = np.ones(n + 1, dtype=np.bool_)
    a[:2] = False
    if n >= 4:
        a[4::2] = False
    if n >= 2:
        a[2] = True
    for p in range(3, math.isqrt(n) + 1, 2):
        if a[p]:
            a[p * p :: 2 * p] = False
    return a


def li(x: int | float) -> float:
    return float(expi(math.log(float(x)))) if x > 1 else 0.0


def moving_sum(a: np.ndarray, L: int) -> np.ndarray:
    cs = np.concatenate(([0], np.cumsum(a, dtype=np.int64)))
    return cs[L:] - cs[:-L]


def standardized_moments(x: np.ndarray) -> dict:
    x = np.asarray(x, dtype=float)
    if len(x) < 4 or np.std(x) == 0:
        return {"n": int(len(x)), "mean": float(np.mean(x)) if len(x) else None,
                "variance": float(np.var(x)) if len(x) else None,
                "skew": None, "excess_kurtosis": None}
    return {
        "n": int(len(x)), "mean": float(np.mean(x)), "variance": float(np.var(x, ddof=1)),
        "skew": float(skew(x, bias=False)),
        "excess_kurtosis": float(kurtosis(x, fisher=True, bias=False)),
    }


def prime_pattern_suite(isprime: np.ndarray, N: int) -> dict:
    """C1-C5: prime pattern fields, cumulants, transition, extremes, universality."""
    motifs = {
        "pair_2": (0, 2), "pair_4": (0, 4), "pair_6": (0, 6), "pair_10": (0, 10),
        "triplet_026": (0, 2, 6), "triplet_046": (0, 4, 6),
        "triplet_0612": (0, 6, 12), "triplet_0410": (0, 4, 10),
    }
    maxh = max(max(v) for v in motifs.values())
    fields = {}
    for name, H in motifs.items():
        x = np.ones(N - maxh + 1, dtype=np.int8)
        for h in H:
            x &= isprime[h:h + len(x)]
        fields[name] = x

    windows = [400, 1000, 2500, 6000, 15000]
    c1 = {}
    c2 = {}
    c3 = {}
    for L in windows:
        step = max(1, L // 4)
        names = ["pair_2", "pair_4", "pair_6", "pair_10"]
        series=[moving_sum(fields[n], L) for n in names]
        idx=np.arange(N//2, min(len(v) for v in series), step)
        counts = np.column_stack([v[idx] for v in series]).astype(float)
        means = counts.mean(axis=0)
        centered = counts - means
        cov = np.cov(centered, rowvar=False)
        eig = np.linalg.eigvalsh(cov)
        z = centered / np.sqrt(np.diag(cov))
        # Fourth joint cumulant tensor compressed to diagonal and two mixed entries.
        fourth_diag = [float(np.mean(z[:,i]**4)-3.0) for i in range(len(names))]
        mixed = {}
        for i,j in [(0,1),(0,2),(1,2)]:
            mixed[f"{names[i]}__{names[j]}"] = float(np.mean(z[:,i]**2*z[:,j]**2) - 1.0 - 2.0*np.mean(z[:,i]*z[:,j])**2)
        c1[str(L)] = {
            "samples": int(len(counts)), "means": dict(zip(names, map(float, means))),
            "covariance": cov.tolist(), "eigenvalues": eig.tolist(),
            "standardized_fourth_cumulants": dict(zip(names, fourth_diag)),
            "mixed_fourth_connected": mixed,
        }
        # variance hierarchy of covariance eigenmodes
        evals, evecs = np.linalg.eigh(cov)
        c2[str(L)] = {
            "eigenvalue_ratios_to_largest": (evals / evals[-1]).tolist(),
            "condition_number": float(evals[-1]/max(evals[0],1e-12)),
            "eigenvectors_columns": evecs.tolist(),
            "smallest_mode_variance_ratio_to_mean_coordinate": float(evals[0]/np.mean(np.diag(cov))),
        }
        # Poisson to Gaussian diagnostics for twins
        twin = counts[:,0]
        mu = twin.mean()
        c3[str(L)] = {
            "mean": float(mu), "fano": float(twin.var(ddof=1)/mu),
            "skew": float(skew(twin,bias=False)),
            "poisson_skew": float(1/math.sqrt(mu)),
            "excess_kurtosis": float(kurtosis(twin,fisher=True,bias=False)),
            "poisson_excess_kurtosis": float(1/mu),
        }

    # C4: occurrence-gap hazard for twin primes. Use local-rate transform g/log^2(midpoint)
    starts = np.flatnonzero(fields["pair_2"])
    gaps = np.diff(starts)
    mids = starts[:-1] + gaps/2
    hazard = gaps / np.maximum(np.log(np.maximum(mids,10.0))**2, 1.0)
    hazard = hazard[mids > N//10]
    c4 = {
        "occurrences": int(len(starts)), "gap_count": int(len(hazard)),
        "hazard_mean": float(np.mean(hazard)),
        "hazard_cv": float(np.std(hazard,ddof=1)/np.mean(hazard)),
        "exp_ks_stat_after_mean_scaling": float(kstest(hazard/np.mean(hazard), expon.cdf).statistic),
        "max_scaled_gap": float(np.max(hazard)),
        "gumbel_centered_max": float(np.max(hazard)/np.mean(hazard) - math.log(len(hazard))),
    }

    # C5: arithmetic-wavelet stability.  The smallest covariance eigenvector is
    # the empirically optimal balanced combination of the four pair fields.
    ordered = [str(L) for L in windows]
    ref = np.array(c2[ordered[-1]]["eigenvectors_columns"])[:,0]
    wavelet = {}
    for key in ordered:
        vec = np.array(c2[key]["eigenvectors_columns"])[:,0]
        wavelet[key] = {
            "smallest_mode_variance_ratio_to_mean_coordinate": c2[key]["smallest_mode_variance_ratio_to_mean_coordinate"],
            "absolute_alignment_with_largest_window": float(abs(np.dot(vec, ref))),
            "coefficients_up_to_sign": (vec * (1 if np.dot(vec,ref)>=0 else -1)).tolist(),
        }
    c5={"motifs":["pair_2","pair_4","pair_6","pair_10"],"wavelet_modes":wavelet}

    return {"C1_connected_field":c1,"C2_overlap_variance_hierarchy":c2,
            "C3_local_spectral_covariance":c3,"C4_conditioned_cluster_extremes":c4,
            "C5_arithmetic_wavelet_completeness":c5}


def least_prime_occupancy(primes: np.ndarray, q_max: int=1000) -> tuple[dict,list[dict]]:
    rows=[]
    for q0 in primes[(primes>=101)&(primes<q_max)]:
        q=int(q0); least=np.zeros(q,dtype=np.int64); least[0]=q; remaining=q-1
        for p0 in primes:
            p=int(p0)
            if p==q: continue
            a=p%q
            if a and least[a]==0:
                least[a]=p; remaining-=1
                if remaining==0: break
        if remaining: continue
        u=np.array([li(int(x)) for x in least],dtype=float)/(q-1)
        un=u[1:]
        centered=u-u.mean()
        spec=np.abs(np.fft.fft(centered))**2/q
        freq=np.minimum(np.arange(q),q-np.arange(q))
        low=(freq>=1)&(freq<=5); high=freq>=q//4
        # quadratic-character projection
        chi=np.zeros(q)
        for a in range(1,q):
            chi[a]=1.0 if pow(a,(q-1)//2,q)==1 else -1.0
        char_proj=float(np.dot(centered,chi)/math.sqrt(q))
        # L(1,chi) crude finite sum to 20q
        M=20*q
        L1=sum((1.0 if pow(n%q,(q-1)//2,q)==1 else -1.0)/n for n in range(1,M+1) if n%q)
        m=q-1
        terminal=un-math.log(m)
        terminal_sorted=np.sort(terminal)[::-1]
        rows.append({
            "q":q,"mean_u":float(un.mean()),"speedup_scaled":float((1-un.mean())*math.log(q)),
            "cover_shift":float(un.max()-sum(1/j for j in range(1,m+1))),
            "fourier_low_high":float(spec[low].mean()/spec[high].mean()),
            "char_projection":char_proj,"L1_chi_proxy":float(L1),
            "terminal_top5":terminal_sorted[:5].tolist(),
            "tail_counts":{str(s):int(np.sum(terminal>s)) for s in (-1.0,0.0,1.0,2.0)},
        })
    bins=[(101,250),(251,500),(501,900),(901,q_max)]
    summary=[]
    for lo,hi in bins:
        rr=[r for r in rows if lo<=r['q']<hi]
        if not rr: continue
        summary.append({"range":[lo,hi],"count":len(rr),
            "speedup_scaled":float(np.mean([r['speedup_scaled'] for r in rr])),
            "cover_shift":float(np.mean([r['cover_shift'] for r in rr])),
            "fourier_low_high":float(np.mean([r['fourier_low_high'] for r in rr])),
            "terminal_theta":{str(s):float(np.mean([r['tail_counts'][str(s)]/math.exp(-s) for r in rr])) for s in (-1.0,0.0,1.0,2.0)}})
    proj=np.array([r['char_projection'] for r in rows]); L1=np.array([r['L1_chi_proxy'] for r in rows])
    return {"q_count":len(rows),"by_bin":summary,
            "char_projection_L1_spearman":float(spearmanr(np.abs(proj),1/np.maximum(np.abs(L1),1e-9)).statistic)}, rows


def is_fundamental_discriminant(D:int)->bool:
    if D>=0: return False
    if D%4==1:
        n=-D
        # squarefree
        p=2
        while p*p<=n:
            if n%(p*p)==0: return False
            p+=1
        return True
    if D%4==0:
        d=D//4
        if d%4 not in (2,3): return False
        n=-d; p=2
        while p*p<=n:
            if n%(p*p)==0: return False
            p+=1
        return True
    return False


def kronecker_D_p(D:int,p:int)->int:
    if p==2:
        if D%2==0: return 0
        return 1 if D%8 in (1,7) else -1
    a=D%p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1


def class_number_negative(D:int)->int:
    """Count reduced primitive positive definite binary quadratic forms of discr. D."""
    assert D<0 and D%4 in (0,1)
    lim=int(math.sqrt(abs(D)/3))+1
    count=0
    for a in range(1,lim+1):
        parity=D&1
        # b in [-a,a], same parity as D
        start=-a
        if (start-parity)&1: start+=1
        for b in range(start,a+1,2):
            num=b*b-D
            den=4*a
            if num%den: continue
            c=num//den
            if a>c: continue
            if math.gcd(a,math.gcd(abs(b),c))!=1: continue
            if (abs(b)==a or a==c) and b<0: continue
            count+=1
    return count


def class_group_local_independence(Dmax:int=15000)->dict:
    small_primes=(3,5,7,11,13)
    data=[]
    for D in range(-3,-Dmax-1,-1):
        if not is_fundamental_discriminant(D): continue
        h=class_number_negative(D)
        signs=tuple(kronecker_D_p(D,p) for p in small_primes)
        genus_bits=max(0,len(factorint(abs(D)))-1)
        data.append((D,h,signs,genus_bits))
    out={"Dmax":Dmax,"field_count":len(data),"tests":{}}
    for ell in (3,5):
        y=np.array([h%ell==0 for _,h,_,_ in data],dtype=float)
        base=float(y.mean())
        entries=[]
        for j,p in enumerate(small_primes):
            vals={}
            for s in (-1,1):
                yy=[(h%ell==0) for _,h,sg,_ in data if sg[j]==s]
                vals[str(s)]={"n":len(yy),"prob":float(np.mean(yy)) if yy else None}
            entries.append({"p":p,"conditional":vals,
                            "max_abs_shift":max(abs(vals[str(s)]["prob"]-base) for s in (-1,1) if vals[str(s)]["prob"] is not None)})
        # growing prefix signature: compare extreme cells with adequate samples
        sig=defaultdict(list)
        for _,h,sg,g in data:
            sig[(g,sg[:3])].append(h%ell==0)
        cell_probs=[np.mean(v) for v in sig.values() if len(v)>=40]
        out["tests"][str(ell)]={"base_prob":base,"single_prime":entries,
            "genus_plus_first3_cell_sd":float(np.std(cell_probs,ddof=1)) if len(cell_probs)>1 else None,
            "adequate_cells":len(cell_probs)}
    return out


def fermat_quotient(p:int,a:int)->int:
    return ((pow(a,p-1,p*p)-1)//p)%p


def quad_pair_mul(x:tuple[int,int], y:tuple[int,int], mod:int, d:int=2)->tuple[int,int]:
    a,b=x; c,e=y
    return ((a*c+d*b*e)%mod, (a*e+b*c)%mod)


def quad_pair_pow(base:tuple[int,int], exp:int, mod:int, d:int=2)->tuple[int,int]:
    out=(1,0); cur=(base[0]%mod,base[1]%mod)
    while exp:
        if exp&1: out=quad_pair_mul(out,cur,mod,d)
        cur=quad_pair_mul(cur,cur,mod,d); exp//=2
    return out


def toric_fermat_quotient_sqrt2(p:int)->tuple[int,int,int]:
    """Finite logarithm of eta=3+2sqrt(2) on the norm-one torus.

    Returns (tangent coefficient B mod p, scalar coefficient A mod p, chi_2(p)).
    At good primes eta^(p-chi)=1+p(A+B sqrt2) mod p^2 and norm one forces A=0.
    """
    chi = 1 if pow(2,(p-1)//2,p)==1 else -1
    mod=p*p
    a,b=quad_pair_pow((3,2),p-chi,mod,2)
    A=(((a-1)%mod)//p)%p
    B=((b%mod)//p)%p
    return B,A,chi


def fermat_suite(primes:np.ndarray,pmax:int=250000)->dict:
    ps=[int(p) for p in primes if 7<=p<=pmax]
    bases=(2,3,5,6,12)
    qvals={a:[] for a in bases}; plist=[]
    fourier_m=(1,2,3,5,8,13)
    progression=defaultdict(lambda:defaultdict(list))
    near_counts={"rank1_2":Counter(),"rank2_2_3":Counter(),"rank3_2_3_5":Counter()}
    thresholds=(0.02,0.05,0.1)
    exact={"2":[],"3":[],"5":[],"2&3":[]}
    depth2={"2":[]}
    toric_vals=[]; toric_split=defaultdict(list); toric_exact=[]; toric_scalar_errors=[]
    for p in ps:
        if any(p==a for a in bases): continue
        qs={a:fermat_quotient(p,a) for a in bases}
        plist.append(p)
        for a in bases:qvals[a].append(qs[a]/p)
        for mod in (4,8): progression[mod][p%mod].append(qs[2]/p)
        for th in thresholds:
            if min(qs[2],p-qs[2])/p<th: near_counts["rank1_2"][str(th)]+=1
            if max(min(qs[2],p-qs[2]),min(qs[3],p-qs[3]))/p<th: near_counts["rank2_2_3"][str(th)]+=1
            if max(min(qs[a],p-qs[a]) for a in (2,3,5))/p<th: near_counts["rank3_2_3_5"][str(th)]+=1
        for a in (2,3,5):
            if qs[a]==0: exact[str(a)].append(p)
        if qs[2]==0 and qs[3]==0: exact["2&3"].append(p)
        if pow(2,p-1,p**3)==1: depth2["2"].append(p)
        B,A,chi=toric_fermat_quotient_sqrt2(p)
        toric_vals.append(B/p); toric_split[chi].append(B/p); toric_scalar_errors.append(A)
        if B==0: toric_exact.append(p)
    arr={a:np.array(v) for a,v in qvals.items()}
    relation_errors={
        "q6_minus_q2_q3":float(np.max(np.abs(((arr[6]-arr[2]-arr[3]+0.5)%1)-0.5))),
        "q12_minus_2q2_q3":float(np.max(np.abs(((arr[12]-2*arr[2]-arr[3]+0.5)%1)-0.5))),
    }
    fourier={}
    for a in (2,3,5):
        fourier[str(a)]={str(m):float(abs(np.mean(np.exp(2j*math.pi*m*arr[a])))) for m in fourier_m}
    joint={}
    for uv in ((2,3),(2,5),(3,5)):
        joint[str(uv)]={f"{m},{n}":float(abs(np.mean(np.exp(2j*math.pi*(m*arr[uv[0]]+n*arr[uv[1]])))))
                        for m,n in ((1,1),(1,-1),(2,1),(3,-2))}
    prog_summary={}
    for mod,d in progression.items():
        prog_summary[str(mod)]={str(r):{"n":len(v),"mean":float(np.mean(v)),
            "fourier1":float(abs(np.mean(np.exp(2j*math.pi*np.array(v)))))} for r,v in d.items() if v}
    tv=np.array(toric_vals)
    toric={
        "field":"Q(sqrt(2))", "point":"3+2sqrt(2)", "sample":len(toric_vals),
        "max_scalar_tangent_error_mod_p":int(max(toric_scalar_errors) if toric_scalar_errors else 0),
        "fourier":{str(m):float(abs(np.mean(np.exp(2j*math.pi*m*tv)))) for m in fourier_m},
        "split_by_legendre2":{str(k):{"n":len(v),"mean":float(np.mean(v)),
            "fourier1":float(abs(np.mean(np.exp(2j*math.pi*np.array(v)))))} for k,v in toric_split.items()},
        "exact_toric_hits":toric_exact,
    }
    return {"pmax":pmax,"prime_count":len(plist),"relation_errors":relation_errors,
            "marginal_fourier":fourier,"joint_fourier":joint,
            "near_zero_counts":{k:dict(v) for k,v in near_counts.items()},
            "exact_hits":exact,"depth2_hits":depth2,"progressions":prog_summary,
            "C15_toric_finite_logarithm":toric}


def iterate_value(c:int,n:int)->int:
    x=0
    for _ in range(n):x=x*x+c
    return x


def roots_of_iterate_mod_p(c:int,p:int,n:int)->int:
    cnt=0
    for x in range(p):
        y=x
        for _ in range(n): y=(y*y+c)%p
        if y==0:cnt+=1
    return cnt


def simulate_wreath_fixed_leaves(samples:int,n:int,seed:int=1)->list[int]:
    rng=np.random.default_rng(seed+n)
    # recursively generate random element of C2 wr ... wr C2 and number fixed leaves
    def one(level:int)->int:
        if level==0:return 1
        swap=rng.integers(0,2)
        if swap:return 0
        return one(level-1)+one(level-1)
    return [one(n) for _ in range(samples)]


def dynamics_suite(primes:np.ndarray)->dict:
    cs=[-10,-7,-5,-3,1,2,3,5,6,7,10]
    small_ps=[int(p) for p in primes if 7<=p<=499]
    c16={}
    for n in (2,3,4):
        empirical=[]
        for c in cs:
            empirical.extend(roots_of_iterate_mod_p(c,p,n) for p in small_ps if (c == 0 or p % abs(c) != 0))
        sim=simulate_wreath_fixed_leaves(20000,n)
        ec=Counter(empirical); sc=Counter(sim)
        keys=sorted(set(ec)|set(sc))
        tv=0.5*sum(abs(ec[k]/len(empirical)-sc[k]/len(sim)) for k in keys)
        c16[str(n)]={"samples":len(empirical),"empirical_distribution":{str(k):v/len(empirical) for k,v in ec.items()},
                     "wreath_distribution":{str(k):v/len(sim) for k,v in sc.items()},"total_variation":float(tv)}

    # C17 fixed-leaf tail: probability that f_c^n has a root mod p, compared
    # with the fixed-leaf probability in the full binary wreath product.
    c17={}
    for n,entry in c16.items():
        nn=int(n)
        emp=1.0-entry["empirical_distribution"].get("0",0.0)
        wr=1.0-entry["wreath_distribution"].get("0",0.0)
        c17[n]={"empirical_root_probability":emp,"wreath_root_probability":wr,
                "n_times_empirical":nn*emp,"n_times_wreath":nn*wr,
                "predicted_limit":2.0}

    # C18/C19 primitive factor process for c in a moderate family at level 4
    largest=[]; sqfree=[]; components=[]
    for c in range(-80,81):
        if c in (-2,-1,0):continue
        seen=set();
        for n in range(1,4):seen.update(factorint(abs(iterate_value(c,n))).keys())
        v=abs(iterate_value(c,4)); fac=factorint(v)
        prim={p:e for p,e in fac.items() if p not in seen}
        if v<=1 or not prim:continue
        logtot=sum(e*math.log(p) for p,e in prim.items())
        if logtot==0:continue
        largest.append(max(math.log(p)/logtot for p in prim))
        sqfree.append(all(e==1 for e in prim.values()))
        components.append(len(prim))
    c18={"family_size":len(largest),"level":4,"mean_largest_log_share":float(np.mean(largest)),
         "median_largest_log_share":float(np.median(largest)),"random_integer_PD1_benchmark":0.62433,
         "mean_primitive_components":float(np.mean(components))}
    c19={"squarefree_primitive_fraction":float(np.mean(sqfree)),"family_size":len(sqfree),
         "repeated_primitive_count":int(len(sqfree)-sum(sqfree))}

    # C20 gcd kernel, compare independent parameters and same-map shifted levels
    independent=[]; related=[]
    params=[1,2,3,5,6,7,10,11,13]
    for i,c in enumerate(params):
        seq=[abs(iterate_value(c,n)) for n in range(2,7)]
        for d in params[i+1:]:
            seq2=[abs(iterate_value(d,n)) for n in range(2,7)]
            g=max(math.gcd(a,b) for a in seq for b in seq2)
            scale=max(max(seq),max(seq2))
            independent.append(math.log(max(g,1))/math.log(scale))
        related.extend(math.log(math.gcd(seq[j],seq[j+1]))/math.log(seq[j+1]) for j in range(len(seq)-1))
    c20={"independent_pair_mean_max_log_gcd_ratio":float(np.mean(independent)),
         "independent_pair_max":float(np.max(independent)),
         "same_orbit_adjacent_mean_log_gcd_ratio":float(np.mean(related)),
         "same_orbit_adjacent_max":float(np.max(related))}
    return {"C16_growing_arboreal_chebotarev":c16,"C17_entropy_conductor_barrier_subcritical_test":c17,
            "C18_primitive_PD":c18,"C19_primitive_squarefull":c19,"C20_fiber_product_gcd":c20}


def root_count_poly_mod_p(coeffs:list[int],p:int)->int:
    return sum(1 for x in range(p) if sum(c*pow(x,i,p) for i,c in enumerate(coeffs))%p==0)


def largest_prime_factor(fac:dict[int,int])->int:
    return max(fac) if fac else 1


def buchstab_omega(u:float,h:float=0.001)->float:
    if u<1:return 0.0
    if u<=2:return 1/u
    grid=np.arange(1.0,u+h,h); om=np.zeros(len(grid)); g=np.zeros(len(grid))
    for i,x in enumerate(grid):
        if x<=2+h/2:om[i]=1/x;g[i]=1
        else:
            j=max(0,int(round((x-2)/h)))
            g[i]=g[i-1]+h*om[j]
            om[i]=g[i]/x
    return float(om[-1])


def polynomial_suite(primes:np.ndarray,N:int=1200)->dict:
    # C21/C22 for f=x^3-2 (S3); factor values in a sample.
    rows=[]
    for n in range(2,N+1):
        v=n**3-2
        fac=factorint(v)
        lp=largest_prime_factor(fac)
        small=sum(e for p,e in fac.items() if p<=100)
        small_part=1
        for pp,ee in fac.items():
            if pp<=100: small_part*=pp**ee
        residual=max(1,v//small_part)
        # mark largest factor by root count of x^3-2 mod p
        rc=(1 if lp%3==2 else 3) if lp>3 else None
        rows.append((n,v,fac,lp,small,small_part,residual,rc))
    marks=Counter(r[-1] for r in rows if r[-1] is not None)
    c21={"N":N,"largest_factor_root_count_distribution":{str(k):v/sum(marks.values()) for k,v in marks.items()},
         "S3_fixed_point_size_biased_prediction":{"1":0.5,"3":0.5},"sample":sum(marks.values())}
    small=np.array([r[4] for r in rows],dtype=float)
    raw=np.array([math.log(r[3])/math.log(r[1]) for r in rows],dtype=float)
    residual_share=np.array([math.log(r[3])/math.log(r[6]) if r[6]>1 else 1.0 for r in rows],dtype=float)
    c22={"raw_pearson_small_vs_largest_log_share":float(np.corrcoef(small,raw)[0,1]),
         "mass_renormalized_pearson":float(np.corrcoef(small,residual_share)[0,1]),
         "mass_renormalized_spearman":float(spearmanr(small,residual_share).statistic),
         "mean_residual_largest_share":float(np.mean(residual_share))}

    # C23 colored components f=(n^2+1)(n^2+n+1)
    color=[]; cross=[]
    smooth_pairs=[]
    thresholds=(0.35,0.45,0.55)
    smooth_counts={str(t):[0,0,0] for t in thresholds} # joint, first, second
    M=6000
    for n in range(1,M+1):
        a=n*n+1; b=n*n+n+1
        fa=factorint(a); fb=factorint(b)
        la=math.log(largest_prime_factor(fa))/math.log(a)
        lb=math.log(largest_prime_factor(fb))/math.log(b)
        color.append((la,lb))
        cross.append(len(set(fa)&set(fb)))
        for t in thresholds:
            A=la<=t;B=lb<=t
            smooth_counts[str(t)][0]+=A and B
            smooth_counts[str(t)][1]+=A
            smooth_counts[str(t)][2]+=B
    ar=np.array(color)
    c23={"N":M,"component_largest_factor_correlation":float(np.corrcoef(ar[:,0],ar[:,1])[0,1]),
         "fraction_with_common_prime_factor":float(np.mean(np.array(cross)>0)),
         "resultant":1}
    c24={"N":M,"thresholds":{}}
    for t,(j,a,b) in smooth_counts.items():
        pa=a/M;pb=b/M;pj=j/M
        c24["thresholds"][t]={"joint":pj,"product":pa*pb,"ratio":pj/(pa*pb) if pa*pb else None}

    # C25 finite-u roughness and conditional primality for n^2+1.
    lo,hi=60000,140000
    ns=np.arange(lo,hi+1,dtype=np.int64); vals=ns*ns+1
    isprime_vals=np.array([is_prime64(int(v)) for v in vals],dtype=bool)
    c25={"range":[lo,hi],"rows":[]}
    for y in (13,31,71,151,313):
        smallp=[int(p) for p in primes if p<=y]
        survive=np.ones(len(ns),dtype=bool)
        V=1.0
        for p in smallp:
            rho=root_count_poly_mod_p([1,0,1],p)
            V*=1-rho/p
            if rho:
                survive &= (vals%p)!=0
        obs=float(isprime_vals[survive].mean())
        logmid=math.log(float(np.median(vals[survive])))
        u=logmid/math.log(y)
        omega=buchstab_omega(u)
        # rough survivor density heuristic e^-gamma *? V already exact local; finite-u multiplier e^gamma omega(u)
        finite_mult=math.exp(0.5772156649015329)*omega
        pred_survive=V*finite_mult
        obs_survive=float(survive.mean())
        # BH constant approx C=prod (1-rho/p)/(1-1/p)
        C=1.0
        for p0 in primes[primes<=5000]:
            p=int(p0);rho=root_count_poly_mod_p([1,0,1],p)
            C*=(1-rho/p)/(1-1/p)
        pred_prime=C/logmid
        pred_cond=pred_prime/pred_survive
        c25["rows"].append({"y":y,"u":u,"observed_survivor_density":obs_survive,
            "predicted_finite_u_survivor_density":pred_survive,"survivor_ratio":obs_survive/pred_survive,
            "observed_conditional_prime":obs,"predicted_conditional_prime":pred_cond,
            "conditional_ratio":obs/pred_cond})
    return {"C21_frobenius_marked_PD":c21,"C22_small_large_independence":c22,
            "C23_colored_components":c23,"C24_saddle_entanglement":c24,
            "C25_buchstab_BH_bridge":c25}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='research_grade_25_results.json')
    ap.add_argument('--prime-max',type=int,default=3_000_000)
    args=ap.parse_args()
    isprime=prime_sieve(args.prime_max); primes=np.flatnonzero(isprime)
    import time
    t=time.time(); print("program I",flush=True)
    results={"metadata":{"prime_max":args.prime_max,"deterministic":True},
             "program_I":prime_pattern_suite(isprime,args.prime_max-20)}
    print("I sec",time.time()-t,flush=True); t=time.time()
    print("program II occupancy",flush=True)
    occ,rows=least_prime_occupancy(primes)
    print("occupancy sec",time.time()-t,flush=True); t=time.time()
    results["program_II"]={"C6_first_order_occupancy":occ,
                            "C7_dual_spectral_geometry":occ,
                            "C8_conditioned_terminal_process":occ,
                            "C9_exceptional_zero_rank_one":{"q_count":occ['q_count'],"spearman_abs_projection_vs_inverse_L1":occ['char_projection_L1_spearman'],"rows":rows},
                            "C10_class_group_decoupling":class_group_local_independence()}
    print("II sec",time.time()-t,flush=True); t=time.time()
    print("program III",flush=True)
    results["program_III"]=fermat_suite(primes)
    print("III sec",time.time()-t,flush=True); t=time.time()
    print("program IV",flush=True)
    results["program_IV"]=dynamics_suite(primes)
    print("IV sec",time.time()-t,flush=True); t=time.time()
    print("program V",flush=True)
    results["program_V"]=polynomial_suite(primes)
    print("V sec",time.time()-t,flush=True)
    Path(args.out).write_text(json.dumps(results,indent=2))
    print(json.dumps({"out":args.out,"top_keys":list(results)},indent=2))

if __name__=='__main__': main()
