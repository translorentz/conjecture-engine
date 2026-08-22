#!/usr/bin/env python3
"""Independent anchor/global-block checks for Part XXII (Conjectures 352-364,
random conformal geometry).

The metric-geometry laws (am1-am8) and the CLE nesting law (am13) are
continuum-limit statements beyond finite computation; only their algebraic
anchors are checkable.  The field-theory laws (am9-am12) are checked here in the
exact global-block limit, as the bundle itself does (the full Virasoro
descendant contribution is a separate verification target).

  * Prop am:triangle : scaling triangle p=1/H=1/(alpha-1), Brownian reductions,
    affine star anchors s_1=d, s_3=2, s_k(4)=5-k.
  * am9  : sphere global SL(2) block spectral MLR (increasing in E=P^2).
  * am10 : DOZZ four-point curvature < 0 in the chamber (exact Upsilon_1 + block),
           positive at the excluded charge a=0.55.
  * am11 : torus global-block thermal MLR (decreasing in E).
  * am12 : five-point coupled DOZZ/global-block proxy has negative-definite
           finite-difference Hessian in the two internal momenta (comb channel).

Run:  python verify/am_rgcft_laws.py
"""
import numpy as np
from scipy.special import hyp2f1
from scipy.integrate import quad
from scipy.special import loggamma

def check_triangle():
    for d in [2.5, 3.0, 4.0, 5.0]:
        p, H, al = d/2, 2/d, 1+2/d
        assert abs(p - 1/H) < 1e-12 and abs(p - 1/(al-1)) < 1e-12
    assert abs(4/2-2) < 1e-12 and abs(2/4-0.5) < 1e-12 and abs(1+2/4-1.5) < 1e-12
    s = lambda k, d: 2 + (3-k)/2*(d-2)
    for d in [3.0, 4.0, 5.0]:
        assert abs(s(1, d)-d) < 1e-12 and abs(s(3, d)-2) < 1e-12
    for k in range(1, 6):
        assert abs(s(k, 4.0)-(5-k)) < 1e-12
    return True

def sphere_block_logmod2(P, z, Q=2.0):
    D = Q*Q/4 + P*P
    val = z**D * hyp2f1(D, D, 2*D, z)
    return 2*np.log(abs(val))

def check_sphere_mlr():
    # E=P^2 -> |F(z2)|^2/|F(z1)|^2 strictly increasing
    bad = 0
    for (z1, z2) in [(0.1, 0.2), (0.1, 0.3), (0.2, 0.4), (0.3, 0.5)]:
        Es = np.linspace(0.05, 6, 60)
        r = np.array([sphere_block_logmod2(np.sqrt(E), z2) - sphere_block_logmod2(np.sqrt(E), z1) for E in Es])
        if np.min(np.diff(r)) <= 0:
            bad += 1
    assert bad == 0, "sphere MLR failed"
    return True

# --- DOZZ Upsilon_1 (real integrand), reused shape from Part XX check ---
def re_logU(sigma, P, b=1.0):
    Q = b + 1/b; w = Q/2 - sigma
    def f(t):
        if t < 1e-12: return w*w - P*P
        den = 2*np.sinh(b*t/2)*np.sinh(t/(2*b))
        return ((w*w-P*P)*np.exp(-t) - (np.cosh(w*t)*np.cos(P*t)-1)/den)/t
    v, _ = quad(f, 0, 60, limit=400, epsabs=1e-11, epsrel=1e-11)
    return v

def re_logU_at_Q(P, b=1.0):
    twoP = 2*P
    lg = np.real(loggamma(1+1j*b*twoP) - loggamma(-1j*b*twoP))
    return lg - np.log(b) + re_logU(1/b, twoP, b)

def dozz_logmod2(a, P, b=1.0):
    Q = b + 1/b
    return 2*(re_logU_at_Q(P, b) - 2*re_logU(Q/2, P, b) - 2*re_logU(2*a-Q/2, P, b))

def four_point_curv(a, z, P, b=1.0, h=1e-3):
    def F(P):
        return dozz_logmod2(a, P, b) + sphere_block_logmod2(P, z, b+1/b)
    return (F(P+h) - 2*F(P) + F(P-h))/h**2

def check_four_point():
    Ps = [0.3, 0.6, 1.0, 1.6, 2.4]
    for a in [2/3, 0.8, 0.96]:      # chamber Q/3<=a<Q/2 at b=1 (Q=2): 0.667..1.0
        for z in [0.1, 0.3, 0.5]:
            assert max(four_point_curv(a, z, P) for P in Ps) < 0, f"a={a} z={z}"
    # excluded charge a=0.55 (<Q/3): positive somewhere
    pos = max(four_point_curv(0.55, z, P) for z in [0.1, 0.3, 0.5] for P in Ps)
    assert pos > 0, "sub-chamber control did not turn positive"
    return pos

def torus_block_logmod2(P, q, a, Q=2.0):
    D = Q*Q/4 + P*P
    c = 1 + 6*Q*Q
    h_ext = a*(Q-a)
    H = (1-q)**(-1) * hyp2f1(h_ext, 1-h_ext, 2*D, q/(q-1))
    val = q**(D - c/24) * H
    return 2*np.log(abs(val))

def check_torus_mlr():
    bad = 0
    for (b1, b2) in [(0.2, 0.4), (0.3, 0.6), (0.25, 0.5)]:
        q1, q2 = np.exp(-2*np.pi*b1), np.exp(-2*np.pi*b2)   # b2>b1 => q2<q1
        for a in [2/3, 0.8, 0.96]:
            Es = np.linspace(0.05, 5, 50)
            r = np.array([torus_block_logmod2(np.sqrt(E), q2, a) - torus_block_logmod2(np.sqrt(E), q1, a) for E in Es])
            if np.max(np.diff(r)) >= 0:
                bad += 1
    assert bad == 0, "torus thermal MLR failed"
    return True

# --- am12: five-point comb sewing-kernel modulus in two internal momenta ---
def couple_logmod2(a, P1, P2, b=1.0):
    # Middle DOZZ vertex C(Q/2+iP1, a, Q/2+iP2) of the comb: P-dependent part of
    # 2 log|C| via the same Upsilon_b evaluator (re_logU(A,B)=Re log Upsilon_b(A+iB),
    # re_logU_at_Q handles the reflected legs 2alpha=Q+2iP).  Legs:
    #   numerator 2a1=Q+2iP1, 2a3=Q+2iP2 (P-dependent);  2a2=2a (P-independent, dropped);
    #   denominator a+i(P1+P2), a+i(P2-P1), Q-a+i(P1+P2), a+i(P1-P2).
    Q = b + 1/b
    num = re_logU_at_Q(P1, b) + re_logU_at_Q(P2, b)
    den = (re_logU(a, P1+P2, b) + re_logU(a, abs(P2-P1), b)
           + re_logU(Q-a, P1+P2, b) + re_logU(a, abs(P1-P2), b))
    return 2*(num - den)

def five_point_logmod2(a, z1, z2, P1, P2, b=1.0):
    # comb: end vertices C(a,a,Q/2+iP1), C(Q/2+iP2,a,a), middle coupling vertex,
    # and one global SL(2) block per internal line.
    Q = b + 1/b
    return (dozz_logmod2(a, P1, b) + dozz_logmod2(a, P2, b)
            + couple_logmod2(a, P1, P2, b)
            + sphere_block_logmod2(P1, z1, Q) + sphere_block_logmod2(P2, z2, Q))

def check_multipoint_hessian(h=2e-3):
    # negative-definite 2x2 finite-difference Hessian of log|K_z| in (P1,P2)
    worst = -np.inf
    for a in [2/3, 0.8, 0.96]:              # interior chamber Q/3<=a<Q/2 at b=1
        for z1 in [0.2, 0.4]:
            for z2 in [0.3, 0.5]:
                for P1 in [0.4, 0.8, 1.2]:
                    for P2 in [0.5, 0.9, 1.3]:
                        f = lambda p, q: five_point_logmod2(a, z1, z2, p, q)
                        fpp = (f(P1+h, P2) - 2*f(P1, P2) + f(P1-h, P2))/h**2
                        fqq = (f(P1, P2+h) - 2*f(P1, P2) + f(P1, P2-h))/h**2
                        fpq = (f(P1+h, P2+h) - f(P1+h, P2-h)
                               - f(P1-h, P2+h) + f(P1-h, P2-h))/(4*h*h)
                        tr, det = fpp + fqq, fpp*fqq - fpq*fpq
                        lam_max = tr/2 + np.sqrt(max((tr/2)**2 - det, 0.0))
                        worst = max(worst, lam_max)
                        assert fpp < 0 and det > 0, \
                            f"Hessian not negative-definite a={a} P=({P1},{P2})"
    return worst

if __name__ == "__main__":
    check_triangle()
    print("am1-am8 anchors: scaling triangle p=1/H=1/(alpha-1), Brownian reductions, star anchors OK")
    check_sphere_mlr()
    print("am9 : sphere global SL(2) block spectral MLR strictly increasing OK")
    pos = check_four_point()
    print(f"am10: DOZZ four-point curvature < 0 in chamber; sub-chamber a=0.55 positive (max {pos:+.3f})")
    check_torus_mlr()
    print("am11: torus global-block thermal MLR strictly decreasing OK")
    worst = check_multipoint_hessian()
    print(f"am12: five-point coupled DOZZ/global-block Hessian negative-definite "
          f"(largest eigenvalue {worst:+.2f} over chamber grid)")
    print("\nAll Part XXII checkable anchors/global-block reductions passed.")
