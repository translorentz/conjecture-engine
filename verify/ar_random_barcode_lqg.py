#!/usr/bin/env python3
"""Independent calibration checks for Conjectures 394--395.

These computations test exact normalizations and a decategorified toral
proxy.  They do not numerically test either asymptotic conjecture.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.linalg import eigh


Matrix = tuple[int, int, int, int]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    a, b, c, d = left
    e, f, g, h = right
    return (a * e + b * g, a * f + b * h,
            c * e + d * g, c * f + d * h)


def random_positive_sl2_product(rng: np.random.Generator, n: int) -> Matrix:
    generators: tuple[Matrix, ...] = ((2, 1, 1, 1), (1, 1, 1, 2))
    product: Matrix = (1, 0, 0, 1)
    for index in rng.integers(0, len(generators), size=n):
        product = matmul(generators[int(index)], product)
    return product


def toral_proxy_check() -> tuple[bool, list[tuple[int, float, float]]]:
    """Compare fixed-point and spectral-radius exponents for SL(2,Z) products."""
    rng = np.random.default_rng(394)
    rows: list[tuple[int, float, float]] = []
    for n in (20, 40, 80, 160):
        gaps = []
        for _ in range(200):
            a, b, c, d = random_positive_sl2_product(rng, n)
            trace = a + d
            # det(M-I)=2-tr(M) for det(M)=1.  Computing through the trace
            # avoids overflowing a floating determinant.
            fixed_exponent = math.log(abs(trace - 2)) / n
            spectral_exponent = math.acosh(trace / 2) / n
            gaps.append(abs(fixed_exponent - spectral_exponent))
        rows.append((n, float(np.mean(gaps)), float(np.max(gaps))))
    passed = rows[-1][1] < rows[0][1] / 3 and rows[-1][2] < 0.02
    return passed, rows


@dataclass(frozen=True)
class ScalingResult:
    max_product_error: float
    max_eigenvalue_error: float
    exponent_identity_error: float


def lqg_scaling_check() -> tuple[bool, ScalingResult]:
    """Check field-shift covariance on a random weighted Dirichlet form."""
    rng = np.random.default_rng(395)
    side = 7
    size = side * side
    stiffness = np.zeros((size, size), dtype=float)

    def vertex(i: int, j: int) -> int:
        return i * side + j

    for i in range(side):
        for j in range(side):
            v = vertex(i, j)
            stiffness[v, v] = 4.0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < side and 0 <= nj < side:
                    stiffness[v, vertex(ni, nj)] = -1.0

    gamma = 1.3
    field_shift = 0.7
    mass_weights = np.exp(gamma * rng.normal(size=size))
    mass = np.diag(mass_weights)
    scale = math.exp(gamma * field_shift)
    shifted_mass = scale * mass

    eigenvalues = eigh(stiffness, mass, subset_by_index=(0, 5),
                       eigvals_only=True)
    shifted_eigenvalues = eigh(stiffness, shifted_mass,
                               subset_by_index=(0, 5), eigvals_only=True)
    area = float(mass_weights.sum())
    shifted_area = scale * area

    product_error = float(np.max(np.abs(
        shifted_area * shifted_eigenvalues - area * eigenvalues
    ) / (area * eigenvalues)))
    eigenvalue_error = float(np.max(np.abs(
        shifted_eigenvalues - eigenvalues / scale
    ) / (eigenvalues / scale)))

    d_gamma = 4.81
    xi = gamma / d_gamma
    exponent_error = abs(gamma / xi - d_gamma)
    result = ScalingResult(product_error, eigenvalue_error, exponent_error)
    passed = max(product_error, eigenvalue_error, exponent_error) < 1e-11
    return passed, result


def main() -> None:
    toral_ok, toral_rows = toral_proxy_check()
    scaling_ok, scaling = lqg_scaling_check()

    print("Conjecture 394: decategorified hyperbolic-toral proxy")
    print(" n    mean exponent gap    maximum gap")
    for n, mean_gap, max_gap in toral_rows:
        print(f"{n:3d}   {mean_gap:17.6e}   {max_gap:11.6e}")
    print("  scope: proxy only; no Floer barcode was computed")
    print(f"  calibration: {'PASS' if toral_ok else 'FAIL'}")

    print("Conjecture 395: field-shift normalization")
    print(f"  max area-times-eigenvalue relative error: "
          f"{scaling.max_product_error:.3e}")
    print(f"  max inverse eigenvalue scaling error:      "
          f"{scaling.max_eigenvalue_error:.3e}")
    print(f"  gamma/xi=d_gamma identity error:           "
          f"{scaling.exponent_identity_error:.3e}")
    print("  scope: exact discrete scaling calibration; no LQG limit was computed")
    print(f"  calibration: {'PASS' if scaling_ok else 'FAIL'}")

    if not (toral_ok and scaling_ok):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
