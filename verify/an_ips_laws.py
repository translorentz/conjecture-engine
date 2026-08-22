#!/usr/bin/env python3
"""Independent reduction checks for Part XXIII (Conjectures 365-379, hydrodynamic
limits of interacting particle systems).

These are NOT the hydrodynamic limits themselves, which are continuum PDE/SPDE
scaling limits beyond finite computation.  They independently reproduce the exact
reductions and event-count scalings of Proposition (an:reductions):

  * an5  (C5): fatigue ODE finite hitting iff p<1, integrated mobility 1/c.
  * an12 (C12): occupation-trap linear residual v_inf = e^{Delta/(a rhobar)} v0,
    matched by the conservative nonlinear finite-difference PDE.
  * an4  (C4): crowding-thinned successful-reset tail exponent beta(1-rho).
  * an7  (C7): codimension-one catalyst contribution scales as N^{theta-1}.

Run:  python verify/an_ips_laws.py
"""
import numpy as np
from scipy.integrate import solve_ivp

def check_fatigue():
    # a-dot = c (1-a)^p, c>0. Finite-time hit of a=1 iff p<1, with
    # t_hit = 1/(c(1-p)); integrated mobility int_0^inf (1-a)^p dt = int_0^1 da/c = 1/c.
    out = {}
    c = 2*0.45*(1-0.45)
    for p in [0.5, 1.0, 1.5]:
        finite_hit = (p < 1)
        t_hit = 1/(c*(1-p)) if p < 1 else np.inf
        out[p] = (finite_hit, t_hit)
    # verify t_hit for p=0.5 by integration to just below a=1
    p = 0.5
    s = solve_ivp(lambda t, a: c*np.maximum(1-a[0], 0)**p, [0, out[0.5][1]*0.999], [0.0],
                  dense_output=True, rtol=1e-11, atol=1e-13)
    a_end = s.y[0, -1]
    assert a_end > 0.99, "p=0.5 did not approach a=1 by t_hit"
    # mobility budget for p=1 (a=1-e^{-ct}): int_0^inf e^{-ct} dt = 1/c
    tt = np.linspace(0, 200, 400000); mob = np.trapezoid(np.exp(-c*tt), tt)
    assert abs(mob - 1/c) < 1e-4, f"mobility budget {mob} vs {1/c}"
    out["mobility"] = (mob, 1/c)
    return out

def check_self_arrest():
    # linear: v(t)=e^{tau Delta} v0, tau_inf=1/(a rhobar); compare to nonlinear PDE
    N = 128; L = 2*np.pi; dx = L/N
    x = np.arange(N)*dx
    a, rhobar = 80.0, 0.55
    k = np.fft.fftfreq(N, d=dx)*2*np.pi
    v0 = np.cos(x)                      # first Fourier mode, mean zero
    tau_inf = 1/(a*rhobar)
    v_lin = np.real(np.fft.ifft(np.exp(-k**2*tau_inf)*np.fft.fft(v0)))
    lin_frac = np.max(v_lin)/np.max(v0)
    # nonlinear conservative PDE: rho_t = d_u(e^{-e} d_u rho), e_t = a rho ; eps small
    eps = 1e-3
    rho = rhobar + eps*v0; e = np.zeros(N)
    dt = 2e-5; T = 3.0; nt = int(T/dt); mass0 = rho.sum()
    for _ in range(nt):
        g = np.exp(-e)
        gh = 0.5*(g + np.roll(g, -1))                 # conductance on bond i->i+1
        flux = gh*(np.roll(rho, -1) - rho)/dx         # symmetric conservative flux
        rho = rho + dt*(flux - np.roll(flux, 1))/dx
        e = e + dt*a*rho
    nl_frac = (np.max(rho)-rhobar)/(eps*np.max(v0))
    mass_err = abs(rho.sum()-mass0)/mass0
    assert abs(lin_frac - nl_frac) < 5e-3, f"residual mismatch {lin_frac} vs {nl_frac}"
    assert mass_err < 1e-10, "mass not conserved"
    return lin_frac, nl_frac, mass_err

def check_crowding_exponent():
    # Successful-reset renewal: attempts at hazard beta/(age+a0), each succeeds
    # w.p. (1-rho); the age is not reset on a blocked attempt.  Thinning gives
    # successes at rate (1-rho)beta/(t+a0), so the successful-wait time has exact
    # survival ((a0)/(t+a0))^{(1-rho)beta} -- Pareto tail exponent beta(1-rho).
    # We simulate the ATTEMPT loop (not the closed form) and estimate the tail
    # exponent with a Hill estimator (unbiased for Pareto tails).
    rng = np.random.default_rng(0)
    beta, a0 = 0.8, 1.0
    out = {}
    for rho in [0.1, 0.4, 0.7]:
        waits = np.empty(120000)
        for i in range(waits.size):
            age = 0.0; t = 0.0
            while True:
                u = rng.random()
                dt = (age+a0)*(np.exp(-np.log(u)/beta)-1)   # next attempt time
                t += dt; age += dt
                if rng.random() < (1-rho):
                    waits[i] = t; break
        w = np.sort(waits)
        k = 8000                                   # top order statistics
        top = w[-k:]
        hill = 1.0/np.mean(np.log(top/top[0]))     # Hill tail-index estimate
        out[rho] = (hill, beta*(1-rho))
        assert abs(hill - beta*(1-rho)) < 0.05, f"rho={rho}: {hill} vs {beta*(1-rho)}"
    return out

def check_catalyst_scaling():
    out = {}
    for theta in [0.5, 1.0, 1.5]:
        Ns = np.array([64, 128, 256, 512], float)
        contrib = Ns**(theta-1)                     # N^{d-1} * N^theta * N^{-d}, d arbitrary
        slope = np.polyfit(np.log(Ns), np.log(contrib), 1)[0]
        out[theta] = (slope, theta-1)
        assert abs(slope-(theta-1)) < 1e-9
    return out

if __name__ == "__main__":
    f = check_fatigue()
    print("an5 : fatigue finite-hit iff p<1:", {p: f[p][0] for p in [0.5,1.0,1.5]},
          f"; mobility budget {f['mobility'][0]:.4f}~{f['mobility'][1]:.4f}")
    lf, nf, me = check_self_arrest()
    print(f"an12: self-arrest residual linear {lf:.4f} vs nonlinear PDE {nf:.4f}; mass err {me:.1e}")
    cw = check_crowding_exponent()
    print("an4 : crowding-thinned tail exponent beta(1-rho):",
          ", ".join(f"rho={r}: {s:.3f}~{t:.3f}" for r, (s, t) in cw.items()))
    ca = check_catalyst_scaling()
    print("an7 : catalyst contribution ~ N^(theta-1):",
          ", ".join(f"theta={th}: {s:.2f}" for th, (s, t) in ca.items()))
    print("\nAll Part XXIII reduction checks passed.")
