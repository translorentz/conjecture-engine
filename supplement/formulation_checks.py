#!/usr/bin/env python3
"""Deterministic formulation checks for the verified 25-conjecture collection.

These checks validate exact algebraic identities and corrected normalizations only.
They are not evidence that any asymptotic conjecture is true or novel.
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Iterable

import numpy as np
from sympy import primerange, sqrt_mod

HERE = Path(__file__).resolve().parent
TEX = HERE.parent / "paper" / "supplement_conjectures.tex"
OUT = HERE / "formulation_check_results.json"


def is_admissible(H: Iterable[int], prime_limit: int = 100) -> bool:
    H = set(H)
    for p in primerange(2, prime_limit + 1):
        if len({h % p for h in H}) == p:
            return False
    return True


def overlap_profile(H: tuple[int, ...], shift_bound: int = 50) -> dict:
    Hs = set(H)
    candidates = []
    for t in range(-shift_bound, shift_bound + 1):
        if t == 0:
            continue
        Ht = {h + t for h in H}
        shared = len(Hs & Ht)
        if shared == 0:
            continue
        union = Hs | Ht
        if is_admissible(union):
            candidates.append({
                "shift": t,
                "shared_constraints": shared,
                "anchored_codimension": len(union) - len(Hs),
            })
    delta = min((x["anchored_codimension"] for x in candidates), default=None)
    minimizers = [x for x in candidates if x["anchored_codimension"] == delta]
    return {
        "motif": list(H),
        "size": len(H),
        "admissible": is_admissible(H),
        "delta": delta,
        "minimizing_overlaps": minimizers,
    }


def primitive_root(q: int) -> int:
    phi = q - 1
    factors = []
    n = phi
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    for g in range(2, q):
        if all(pow(g, phi // r, q) != 1 for r in factors):
            return g
    raise RuntimeError("no primitive root")


def gauss_transport_check(q: int, seed: int = 0) -> dict:
    rng = np.random.default_rng(seed + q)
    a = np.arange(q)
    xi = np.arange(q)
    A_mat = np.exp(-2j * np.pi * np.outer(xi, a) / q) / math.sqrt(q)

    g = primitive_root(q)
    logs = {}
    x = 1
    for j in range(q - 1):
        logs[x] = j
        x = (x * g) % q

    B_mat = np.zeros((q, q), dtype=complex)
    B_mat[0, 0] = 1.0  # recorded value at zero
    for m in range(q - 1):
        for aval in range(1, q):
            chi = np.exp(2j * np.pi * m * logs[aval] / (q - 1))
            B_mat[m + 1, aval] = np.conjugate(chi) / math.sqrt(q - 1)

    U = B_mat @ np.linalg.inv(A_mat)
    f = rng.normal(size=q)
    f -= np.mean(f)
    Avec = A_mat @ f
    Mvec = B_mat @ f
    vector_error = float(np.max(np.abs(Mvec - U @ Avec)))

    U2 = np.kron(U, U)
    phi = rng.normal(size=q * q) + 1j * rng.normal(size=q * q)
    psi = np.linalg.solve(U2.conj().T, phi)
    X = np.vdot(phi, np.kron(Avec, Avec))
    Y = np.vdot(psi, np.kron(Mvec, Mvec))
    scalar_tensor_error = float(abs(X - Y))
    return {
        "q": q,
        "primitive_root": g,
        "vector_transport_max_error": vector_error,
        "quadratic_test_transport_error": scalar_tensor_error,
    }


def fermat_quotient_mod_p(a: int, p: int) -> int:
    return ((pow(a, p - 1, p * p) - 1) // p) % p


def quadratic_unit_relation_check(prime_limit: int = 100) -> list[dict]:
    rows = []
    for p in primerange(3, prime_limit + 1):
        if pow(2, (p - 1) // 2, p) != 1:
            continue
        roots = sqrt_mod(2, p * p, all_roots=True)
        if not roots:
            continue
        r = int(roots[0])
        a = (1 + r) % (p * p)
        b = (1 - r) % (p * p)
        qa = fermat_quotient_mod_p(a, p)
        qb = fermat_quotient_mod_p(b, p)
        rows.append({
            "p": int(p),
            "root_mod_p2": r,
            "product_mod_p2": int((a * b) % (p * p)),
            "expected_product_mod_p2": p * p - 1,
            "relation_sum_mod_p": int((qa + qb) % p),
        })
    return rows


def smooth_local_factor_check() -> list[dict]:
    rows = []
    s = 1.7
    for p in [2, 3, 5, 7, 11]:
        # Exact valuation law for a Haar random p-adic integer: P(v=k)=(1-1/p)p^{-k}.
        approx = sum((1 - 1 / p) * p ** (-k) * p ** (-(s - 1) * k) for k in range(100))
        z_inf = 1 - 1 / p
        normalized = approx / z_inf
        target = 1 / (1 - p ** (-s))
        rows.append({
            "p": p,
            "normalized_partition": normalized,
            "truncated_zeta_factor": target,
            "absolute_error": abs(normalized - target),
        })
    return rows


def source_audit() -> dict:
    text = TEX.read_text()
    labels = re.findall(r"\\label\{(c\d+)\}", text)
    return {
        "conjecture_environment_count": text.count(r"\begin{conjecture}"),
        "labels": labels,
        "unique_label_count": len(set(labels)),
        "contains_old_universal_polymer_scale": "theta_X(H)=1-\\frac{c(H)}{\\log X}" in text,
        "contains_deterministic_vector_cumulant": "Cum}_r(\\mathbf M_q)" in text,
        "contains_global_regulator_lattice": r"\mathcal R_\Gamma" in text,
        "contains_arboreal_connected_tier": "Connected tier" in text,
        "contains_dynatomic_complexity": r"\mathfrak H_n" in text,
        "contains_perron_amplitude": r"\frac{ds_i}{s_i}" in text,
    }


def main() -> None:
    results = {
        "metadata": {
            "purpose": "formulation and exact-identity checks only",
            "not_evidence_of_truth_or_priority": True,
        },
        "source_audit": source_audit(),
        "C4_anchored_polymer_profiles": [
            overlap_profile((0, 6)),
            overlap_profile((0, 2, 6)),
            overlap_profile((0, 2, 6, 8)),
        ],
        "C7_Gauss_transport": [gauss_transport_check(q) for q in (7, 11, 13)],
        "C14_global_relation_Qsqrt2": quadratic_unit_relation_check(),
        "C24_one_variable_local_calibration": smooth_local_factor_check(),
    }
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True))
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
