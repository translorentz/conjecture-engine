#!/usr/bin/env python3
"""Companion paper (paper/conjectures_promise.tex): sub-lemma and mechanism
checks for the twelve promise-class electronic-structure conjectures.

IMPORTANT SCOPE.  Unlike the other verify scripts in this repository, this one
does NOT verify any of the twelve conjectural structural laws.  It re-derives
the standard shared lemmas the reasoning uses (Rayleigh continuity, gap-to-
infidelity, Krylov row leverage, occupation-tail freezing, Feshbach fixed-point
perturbation, the CMI-to-trace inequality, and the treewidth-to-polynomial
identity) and three auxiliary bounds used by Conjectures p5, p8, p12 (block
spectral lower bound, determinant sign-gap nonnegativity, block-Gershgorin
lower-bound architecture).  A PASS certifies an ingredient of the reasoning, not
that any promise-class law holds.

Adapted, with attribution, from the source research package
`math_audit.py`/`fermion_utils.py`; rewritten self-contained in the house
verify style.
"""
import math
import sys

import numpy as np
import scipy.linalg as la

rng = np.random.default_rng(20260821)
PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))


def rand_herm(n):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (A + A.conj().T) / 2


def unit(v):
    return v / la.norm(v)


print("== Shared lemmas (Section 2 of the companion paper)")

# Lemma 1: Rayleigh continuity.
viol = 0.0
for _ in range(500):
    H = rand_herm(8)
    x = unit(rng.normal(size=8) + 1j * rng.normal(size=8))
    y = unit(rng.normal(size=8) + 1j * rng.normal(size=8))
    viol = max(viol, abs(np.vdot(x, H @ x) - np.vdot(y, H @ y)) - 2 * la.norm(H, 2) * la.norm(x - y))
check("Lemma 1 Rayleigh continuity", viol <= 2e-12, f"max violation {viol:.1e}")

# Lemma 2: energy-to-fidelity under a gap.
viol = 0.0
for _ in range(500):
    vals = np.sort(rng.uniform(-2, 4, size=8))
    vals[1:] = np.maximum(vals[1:], vals[0] + 0.2)
    U, _ = la.qr(rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)))
    H = U @ np.diag(vals) @ U.conj().T
    psi0 = U[:, 0]
    phi = unit(rng.normal(size=8) + 1j * rng.normal(size=8))
    lhs = float(np.real(np.vdot(phi, H @ phi)) - vals[0])
    rhs = (vals[1] - vals[0]) * (1 - abs(np.vdot(psi0, phi)) ** 2)
    viol = max(viol, rhs - lhs)
check("Lemma 2 gap-to-infidelity", viol <= 2e-12, f"max violation {viol:.1e}")

# Lemma 3: Krylov row-leverage support bound.
viol = 0.0
for _ in range(500):
    Z = rng.normal(size=(30, 6)) + 1j * rng.normal(size=(30, 6))
    U, _ = la.qr(Z, mode="economic")
    lev = np.sum(abs(U) ** 2, axis=1)
    x = U @ unit(rng.normal(size=6) + 1j * rng.normal(size=6))
    keep = rng.choice(30, size=rng.integers(1, 29), replace=False)
    mask = np.ones(30, dtype=bool)
    mask[keep] = False
    viol = max(viol, float(np.sum(abs(x[mask]) ** 2) - np.sum(lev[mask])))
check("Lemma 3 Krylov row-leverage bound", viol <= 2e-12, f"max violation {viol:.1e}")

# Lemma 4: occupation-defect union bound + normalized projection distance.
viol = 0.0
for _ in range(500):
    dim = 32
    psi = unit(rng.normal(size=dim) + 1j * rng.normal(size=dim))
    probs = abs(psi) ** 2
    frozen = rng.choice(5, size=rng.integers(1, 6), replace=False)
    targets = {int(p): int(rng.integers(0, 2)) for p in frozen}
    T = 0.0
    keep = np.ones(dim, dtype=bool)
    for p, t in targets.items():
        occ = float(sum(probs[s] for s in range(dim) if ((s >> p) & 1) == 1))
        T += (1 - occ) if t else occ
        keep &= np.array([((s >> p) & 1) == t for s in range(dim)])
    pkeep = float(np.sum(probs[keep]))
    q = 1 - pkeep
    viol = max(viol, q - T)
    if pkeep > 1e-14:
        phi = np.zeros(dim, dtype=complex)
        phi[keep] = psi[keep] / math.sqrt(pkeep)
        d2 = float(la.norm(phi - psi) ** 2)
        viol = max(viol, d2 - 2 * q, d2 - 2 * T)
check("Lemma 4 occupation-tail leakage/distance", viol <= 3e-12, f"max violation {viol:.1e}")

# Lemma 5: scalar Feshbach fixed-point perturbation.
viol = 0.0
for _ in range(300):
    A = float(rng.uniform(-1, 1))
    d = float(rng.uniform(3, 7))
    b = float(rng.uniform(0.05, 0.7))
    eta = float(rng.uniform(-1e-3, 1e-3))
    E = float(np.min(np.roots([1, -(A + d), A * d - b * b]).real))
    Er = float(np.min(np.roots([1, -(A - eta + d), (A - eta) * d - b * b]).real))
    lo, hi = min(E, Er) - 0.1, max(E, Er) + 0.1
    L = max(b * b / (d - lo) ** 2, b * b / (d - hi) ** 2)
    if L >= 1:
        continue
    viol = max(viol, abs(E - Er) - abs(eta) / (1 - L))
check("Lemma 5 Feshbach fixed-point perturbation", viol <= 2e-10, f"max violation {viol:.1e}")

# Lemma 6: CMI-to-trace algebra, sqrt(1-exp(-I)) <= sqrt(I).
xs = np.logspace(-12, 3, 500)
viol = float(np.max(np.sqrt(-np.expm1(-xs)) - np.sqrt(xs)))
check("Lemma 6 CMI-to-trace algebra", viol <= 2e-15, f"max violation {max(0.0, viol):.1e}")

# Lemma 7: logarithmic treewidth implies polynomial exp(O(t)).
viol = 0.0
for n in (10, 100, 10_000, 10 ** 6):
    for eps in (1e-1, 1e-3, 1e-6):
        t = 2.5 * math.log(n / eps)
        viol = max(viol, abs(math.exp(1.7 * t) - (n / eps) ** (2.5 * 1.7)) / max((n / eps) ** (2.5 * 1.7), 1e-300))
check("Lemma 7 log-treewidth implies polynomial exp(O(t))", viol < 1e-12, f"max violation {viol:.1e}")

print("== Auxiliary bounds (Conjectures p5, p8, p12)")

# p5 auxiliary: block spectral lower bounds.
viol = 0.0
for _ in range(300):
    A = rand_herm(3)
    D = rand_herm(4) + 6 * np.eye(4)
    B = (rng.normal(size=(3, 4)) + 1j * rng.normal(size=(3, 4))) * 0.2
    H = np.block([[A, B], [B.conj().T, D]])
    E = float(la.eigvalsh(H)[0])
    U0, d0, b0 = float(la.eigvalsh(A)[0]), float(la.eigvalsh(D)[0]), float(la.norm(B, 2))
    if d0 <= U0:
        continue
    low = (U0 + d0 - math.sqrt((d0 - U0) ** 2 + 4 * b0 * b0)) / 2
    weak = U0 - b0 * b0 / (d0 - U0)
    viol = max(viol, low - E, weak - E)
check("p5: block spectral lower bounds", viol <= 2e-12, f"max violation {viol:.1e}")

# p8 auxiliary: determinant sign-gap nonnegativity E0(H) >= E0(H_abs).
viol = 0.0
for _ in range(300):
    H = np.real(rand_herm(12))
    off = H - np.diag(np.diag(H))
    Habs = np.diag(np.diag(H)) - np.abs(off)
    viol = max(viol, -(float(la.eigvalsh(H)[0] - la.eigvalsh(Habs)[0])))
check("p8: determinant sign-gap nonnegativity", viol <= 2e-12, f"max violation {viol:.1e}")


# p12 auxiliary: block-Gershgorin lower bound architecture (self-contained).
def block_gershgorin_lower_bound(H, blocks):
    lo = math.inf
    for j, bj in enumerate(blocks):
        Hjj = H[np.ix_(bj, bj)]
        radius = sum(la.norm(H[np.ix_(bj, bk)], 2) for k, bk in enumerate(blocks) if k != j)
        lo = min(lo, float(la.eigvalsh(Hjj)[0]) - radius)
    return lo


def contiguous_blocks(n, w):
    return [list(range(i, min(i + w, n))) for i in range(0, n, w)]


viol = 0.0
for _ in range(200):
    H = np.real(rand_herm(30))
    lb = block_gershgorin_lower_bound(H, contiguous_blocks(30, int(rng.integers(1, 8))))
    viol = max(viol, lb - float(la.eigvalsh(H)[0]))
check("p12: block-Gershgorin proxy is a lower bound", viol <= 2e-11, f"max violation {viol:.1e}")

n_ok = sum(PASS)
print(f"\n{n_ok}/{len(PASS)} sub-lemma/auxiliary checks passed"
      " (ingredients only; not evidence for the conjectural laws).")
sys.exit(0 if all(PASS) else 1)
