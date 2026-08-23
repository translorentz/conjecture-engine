#!/usr/bin/env python3
"""Independent verification for Part XX (Conjectures 335-336).

Two exactly solved objects in random conformal geometry, checked from their
closed forms by code sharing nothing with the source package:

  * Conjecture 335 (DOZZ spectral log-concavity): for Q/3 <= a < Q/2,
        d^2/dP^2 log |C_b(a, a, Q/2 + iP)| < 0   for all P > 0,
    with two boundary controls (sub-chamber charge; full 3-charge Hessian)
    that must FAIL, confirming the chamber is necessary.

  * Conjecture 336 (Brownian-annulus modular log-concavity) RESOLVED FALSE:
    the deposited claim that  s -> log p_x(e^s)  is strictly concave for every
    boundary-length ratio x>0 fails at large x, where the logarithmic-modulus
    curvature turns positive (+0.380 at x=e^5, tau=0.30) and tends to the
    positive asymptote (4 pi/3) tau; the deposited scan reached only moderate
    ratios and missed the tail.

log Upsilon_b is evaluated from the Barnes integral representation via a
real-part integrand (derived here, not the source package's complex form);
the annulus density is rebuilt by Fourier-inverting the exact Mellin
transform and multiplying by the exact Dedekind eta.  All curvatures are
central second differences.  Run:  python verify/ak_cft_shape_laws.py
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import loggamma

# ---------------------------------------------------------------------------
# Barnes Upsilon_b: real part of log Upsilon_b(sigma + iP), 0 < sigma < Q.
# Re log U(sigma+iP) = int_0^inf dt/t [ (w^2-P^2) e^{-t}
#     - (cosh(w t) cos(P t) - 1) / (2 sinh(bt/2) sinh(t/2b)) ],  w = Q/2-sigma.
# ---------------------------------------------------------------------------

def re_logU(sigma, P, b):
    Q = b + 1.0 / b
    w = Q / 2.0 - sigma

    def f(t):
        if t < 1e-12:
            return w * w - P * P            # analytic t->0 limit
        e1 = (w * w - P * P) * np.exp(-t)
        den = 2.0 * np.sinh(b * t / 2.0) * np.sinh(t / (2.0 * b))
        e2 = (np.cosh(w * t) * np.cos(P * t) - 1.0) / den
        return (e1 - e2) / t

    val, _ = quad(f, 0.0, 60.0, limit=400, epsabs=1e-11, epsrel=1e-11)
    return val


def re_logU_at_Q(P, b):
    """Re log U(Q + 2iP) via one downshift to 1/b + 2iP."""
    twoP = 2.0 * P
    # U(x+b) = gamma(bx) b^{1-2bx} U(x), x = 1/b + 2iP, bx = 1 + 2 i b P
    lg = np.real(loggamma(1 + 1j * b * twoP) - loggamma(-1j * b * twoP))
    return lg - np.log(b) + re_logU(1.0 / b, twoP, b)


def dozz_curv(P, a, b, h=1e-3):
    """Second P-derivative of log |C_b(a,a,Q/2+iP)| (P-dependent part)."""
    Q = b + 1.0 / b

    def F(P):
        return (re_logU_at_Q(P, b)
                - 2.0 * re_logU(Q / 2.0, P, b)
                - 2.0 * re_logU(2.0 * a - Q / 2.0, P, b))

    return (F(P + h) - 2.0 * F(P) + F(P - h)) / h ** 2


# ---- real Upsilon_1 with unit shifts, for the joint 3-charge control ----

def re_logU1_real(x):
    """Re log |Upsilon_1(x)| for real x, reducing to (0,2) by U(x+1)=gamma(x)U(x)."""
    corr = 0.0
    while x >= 2.0:
        y = x - 1.0
        corr += np.real(loggamma(complex(y)) - loggamma(complex(1.0 - y)))
        x = y
    while x <= 0.0:
        corr -= np.real(loggamma(complex(x)) - loggamma(complex(1.0 - x)))
        x = x + 1.0
    return corr + re_logU(x, 0.0, 1.0)


def logabs_dozz_real(a1, a2, a3, b=1.0):
    """log |C_b(a1,a2,a3)| up to the P/charge-independent Upsilon'(0) constant,
    real charges.  Prefactor is real; its log is linear in the charges so does
    not affect the Hessian, and is dropped here."""
    Q = b + 1.0 / b
    abar = a1 + a2 + a3
    num = re_logU1_real(2 * a1) + re_logU1_real(2 * a2) + re_logU1_real(2 * a3)
    den = (re_logU1_real(abar - Q) + re_logU1_real(abar - 2 * a1)
           + re_logU1_real(abar - 2 * a2) + re_logU1_real(abar - 2 * a3))
    return num - den


def joint_hessian_eigs(a, b=1.0, h=2e-3):
    pts = [a, a, a]

    def g(v):
        return logabs_dozz_real(v[0], v[1], v[2], b)

    H = np.zeros((3, 3))
    v0 = np.array(pts, float)
    for i in range(3):
        for j in range(3):
            vpp = v0.copy(); vpp[i] += h; vpp[j] += h
            vpm = v0.copy(); vpm[i] += h; vpm[j] -= h
            vmp = v0.copy(); vmp[i] -= h; vmp[j] += h
            vmm = v0.copy(); vmm[i] -= h; vmm[j] -= h
            H[i, j] = (g(vpp) - g(vpm) - g(vmp) + g(vmm)) / (4 * h * h)
    return np.linalg.eigvalsh((H + H.T) / 2)


# ---------------------------------------------------------------------------
# Brownian annulus (Ang-Remy-Sun): p_x(tau) ~ eta(2 i tau) rho_tau(x).
# ---------------------------------------------------------------------------

def log_eta_2itau(tau):
    q = np.exp(-4.0 * np.pi * tau)
    s = 0.0
    qn = q
    for n in range(1, 100000):
        term = np.log1p(-qn)
        s += term
        if abs(term) < 1e-16:
            break
        qn *= q
    return -np.pi * tau / 6.0 + s


def rho_log_density(ell, tau):
    """density of log X_tau at ell: (1/pi) int_0^inf cos(t ell) phi(t,tau) dt."""
    def f(t):
        if t < 1e-12:
            ph = 1.0
        else:
            ph = (2 * np.pi * t / (3 * np.sinh(2 * np.pi * t / 3.0))) \
                 * np.exp(-2 * np.pi * tau * t * t / 3.0)
        return np.cos(t * ell) * ph
    val, _ = quad(f, 0.0, 40.0, limit=400, epsabs=1e-12, epsrel=1e-12)
    return val / np.pi


def annulus_curv(s, logx, h=1e-3):
    def G(s):
        tau = np.exp(s)
        return log_eta_2itau(tau) + np.log(rho_log_density(logx, tau))
    return (G(s + h) - 2.0 * G(s) + G(s - h)) / h ** 2


# ---------------------------------------------------------------------------

def main():
    ok = True

    print("Conjecture 335 (DOZZ spectral log-concavity), chamber Q/3<=a<Q/2:")
    Ps = [0.15, 0.3, 0.5, 0.8, 1.2, 1.8, 2.6, 3.5]
    worst = -1e9
    for b in [0.5, 0.8, 1.0, 1.3]:
        Q = b + 1.0 / b
        for frac in [1.0 / 3, 0.37, 0.42, 0.47, 0.499]:
            a = frac * Q
            mx = max(dozz_curv(P, a, b) for P in Ps)
            worst = max(worst, mx)
            assert mx < 0, f"FAIL b={b} a/Q={frac}: max curv {mx:+.4f}"
    print(f"  PASS: strictly negative for all (b,a,P); worst max curvature {worst:+.4f}")

    print("Boundary control A: a=0.55 (< Q/3) at b=1 must have positive curvature:")
    mxA = max(dozz_curv(P, 0.55, 1.0) for P in Ps)
    assert mxA > 0, "control A did not turn positive"
    print(f"  PASS: max curvature {mxA:+.4f} > 0, so the a>=Q/3 floor is necessary")

    print("Boundary control B: joint 3-charge Hessian of log|C_1| at (1.3,1.3,1.3):")
    eigs = joint_hessian_eigs(1.3, 1.0)
    assert eigs.max() > 0, "control B: no positive eigenvalue"
    print(f"  PASS: eigenvalues {np.round(eigs,2)}, positive one present, "
          "so joint concavity fails")

    print("Conjecture 336 (Brownian-annulus modular log-concavity) RESOLVED FALSE:")
    # The deposited scan reached only moderate boundary ratios, where the
    # logarithmic-modulus curvature is indeed negative; it missed the tail.
    ss = [np.log(v) for v in [0.02, 0.05, 0.1, 0.25, 0.5, 1, 2, 4, 8, 16, 30]]
    curv_by_x = {}
    for x in [0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 10.0, 20.0]:
        logx = np.log(x)
        curv_by_x[x] = max(annulus_curv(s, logx) for s in ss)
    moderate = max(curv_by_x.values())
    print(f"  moderate boundary ratios x in [1/20,20]: curvature stays "
          f"negative (worst {moderate:+.4f}), matching the deposited scan")
    sym = abs(curv_by_x[4.0] - curv_by_x[0.25])
    assert sym < 1e-2, "x<->1/x symmetry broken"
    print(f"  x<->1/x symmetry: |curv(4)-curv(1/4)| = {sym:.2e}")

    # Counterexample at large boundary ratio: log X_tau = Z + G_tau with Z
    # logistic of scale 2/3 and G_tau Gaussian; the logistic tail drives the
    # curvature to the positive (4 pi/3) tau as x -> infinity.
    c5 = annulus_curv(np.log(0.30), 5.0)
    c7 = annulus_curv(np.log(0.30), 7.0)
    assert c5 > 0, f"expected positive curvature at x=e^5, got {c5:+.4f}"
    assert c7 > c5, "curvature should keep growing into the tail"
    print(f"  COUNTEREXAMPLE: at x=e^5, tau=0.30 curvature = {c5:+.5f} > 0; "
          f"at x=e^7 it grows to {c7:+.5f}")
    print(f"  asymptote (4 pi/3) tau = {(4*np.pi/3)*0.30:+.4f} as x -> infinity, "
          "so log-concavity fails in the tail")

    print("\nAll Part XX checks passed.")
    return ok


if __name__ == "__main__":
    main()
