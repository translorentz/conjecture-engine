#!/usr/bin/env python3
"""Independent anchor/reduced-model checks for Part XXI (Conjectures 337-351,
theoretical fluid dynamics).

These are NOT verifications of the singular laws themselves, which are blow-up,
vanishing-viscosity, and asymptotic statements about continuum solutions and lie
beyond any finite computation.  They independently reproduce the exact anchors and
reduced-model reductions of Proposition (al:anchors), sharing no code with the
source derivation:

  * al14 (C14): three-vortex self-similar collapse condition (exact) and core
    contraction of the planar point-vortex ODE from a zero-angular-impulse config.
  * al5  (C05): degenerate one-drift shear enhanced-dissipation exponent m/(m+2).
  * al12 (C12): homogeneity-reduced gSQG neck ODE d' = -d^{1-beta} => d~(T-t)^{1/beta}.
  * al6  (C06): scale-invariance of the total curvature of a space curve.
  * al15 (C15): exact-Beltrami (ABC) Lamb-vector annihilation vs a non-Beltrami field.

Run:  python verify/al_fluid_laws.py
"""
import numpy as np
from scipy.integrate import solve_ivp

def check_vortex_collapse():
    G = np.array([1.0, 1.0, -0.5])
    cond = G[0]*G[1] + G[1]*G[2] + G[2]*G[0]
    assert abs(cond) < 1e-14, f"collapse condition {cond} != 0"

    def rhs(t, y):
        z = y[:3] + 1j*y[3:]
        dz = np.zeros(3, complex)
        for i in range(3):
            s = 0
            for j in range(3):
                if i != j:
                    s += G[j] / np.conj(z[i]-z[j])
            dz[i] = s/(2j*np.pi)
        return np.concatenate([dz.real, dz.imag])

    rng = np.random.default_rng(0)
    best = None
    for _ in range(4000):
        z = rng.standard_normal(3) + 1j*rng.standard_normal(3)
        z = z - (G@z)/G.sum()                     # center of vorticity at 0
        L = float(np.sum(G*np.abs(z)**2))         # angular impulse
        if best is None or abs(L) < best[0]:
            best = (abs(L), z.copy())
    z0 = best[1]
    diam = lambda z: max(abs(z[0]-z[1]), abs(z[1]-z[2]), abs(z[0]-z[2]))
    sol = solve_ivp(rhs, [0, 200], np.concatenate([z0.real, z0.imag]),
                    rtol=1e-10, atol=1e-12, max_step=0.5)
    zs = sol.y[:3] + 1j*sol.y[3:]
    d = np.array([diam(zs[:, k]) for k in range(zs.shape[1])])
    ratio = d.min()/d[0]
    assert ratio < 0.1, f"core did not contract: {ratio}"
    return cond, ratio

def check_shear_exponent():
    import numpy.fft as fft
    def gap(m, k, nu, Ny=192):
        y = np.linspace(0, 2*np.pi, Ny, endpoint=False); dy = y[1]-y[0]
        ky = fft.fftfreq(Ny, d=dy)*2*np.pi
        Lap = np.real(np.fft.ifft((-(ky**2))[:, None]*np.fft.fft(np.eye(Ny), axis=0), axis=0))
        A = np.diag(-1j*k*(y**m)) + nu*(Lap - k**2*np.eye(Ny))
        return -np.max(np.linalg.eigvals(A).real)
    out = {}
    for m in [1, 2, 3]:
        nus = np.array([1e-3, 3e-4, 1e-4, 3e-5])
        g = np.array([gap(m, 1, nu) for nu in nus])
        slope = np.polyfit(np.log(nus), np.log(g), 1)[0]
        out[m] = (slope, m/(m+2))
        assert abs(slope - m/(m+2)) < 0.05, f"m={m}: {slope} vs {m/(m+2)}"
    return out

def check_neck_ode():
    out = {}
    for beta in [0.5, 0.75, 1.0]:
        s = solve_ivp(lambda t, d: -np.maximum(d, 1e-12)**(1-beta), [0, 10], [1.0],
                      rtol=1e-10, atol=1e-12, dense_output=True,
                      events=lambda t, d: d[0]-1e-6)
        T = s.t_events[0][0]
        tt = np.linspace(0.5*T, 0.98*T, 50); dd = s.sol(tt)[0]
        slope = np.polyfit(np.log(T-tt), np.log(dd), 1)[0]
        out[beta] = (slope, 1/beta)
        assert abs(slope - 1/beta) < 0.02, f"beta={beta}: {slope} vs {1/beta}"
    return out

def check_frenet_scale_invariance():
    # dimensionless pair (total curvature K = int kappa ds,
    # torsion variation Tor = int L|d_s tau|/(1+L|tau|) ds) of a modulated helix,
    # both dilation-invariant (Prop al:anchors (iv), significance of al6).
    def invariants(scale):
        t = np.linspace(0, 4*np.pi, 40000); dt = t[1]-t[0]
        a, b = 1.0, 0.3
        r = np.vstack([scale*a*np.cos(t), scale*a*np.sin(t),
                       scale*(b*t + 0.1*np.sin(3*t))]).T
        dr = np.gradient(r, t, axis=0); ddr = np.gradient(dr, t, axis=0)
        dddr = np.gradient(ddr, t, axis=0)
        cross = np.cross(dr, ddr); ncross = np.linalg.norm(cross, axis=1)
        speed = np.linalg.norm(dr, axis=1)
        kappa = ncross/speed**3
        tau = np.einsum('ij,ij->i', cross, dddr)/ncross**2
        ds = speed*dt
        L = np.sum(ds)
        dtau_ds = np.gradient(tau, t)/speed        # d tau/ds
        K = np.sum(kappa*ds)
        # trim endpoints where finite differences of the 3rd derivative are worst
        sl = slice(3, -3)
        Tor = np.sum((L*np.abs(dtau_ds)/(1+L*np.abs(tau)))[sl]*ds[sl])
        return K, Tor
    K1, T1 = invariants(1.0); K2, T2 = invariants(2.5)
    relK = abs(K1-K2)/K1; relT = abs(T1-T2)/abs(T1)
    assert relK < 1e-10, f"total curvature not scale invariant: {relK}"
    assert relT < 1e-3, f"torsion variation not scale invariant: {relT}"
    return K1, relK, T1, relT

def _curl_spectral(u, k):
    # u: (3, n, n, n) real field on a periodic box; k: 1D wavenumbers
    KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
    uh = np.fft.fftn(u, axes=(1, 2, 3))
    wx = np.fft.ifftn(1j*(KY*uh[2] - KZ*uh[1])).real
    wy = np.fft.ifftn(1j*(KZ*uh[0] - KX*uh[2])).real
    wz = np.fft.ifftn(1j*(KX*uh[1] - KY*uh[0])).real
    return np.array([wx, wy, wz])

def check_beltrami_lamb():
    # ABC (Beltrami) vs Taylor-Green (non-Beltrami): compute omega = curl(u)
    # SPECTRALLY (not u x u), confirm the ABC field is Beltrami (omega = u), and
    # check its Lamb vector u x omega vanishes while Taylor-Green's does not.
    n = 32
    x = np.linspace(0, 2*np.pi, n, endpoint=False)
    k = np.fft.fftfreq(n, d=1.0/n)              # integer wavenumbers on [0,2pi)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    A = B = C = 1.0
    uABC = np.array([A*np.sin(Z)+C*np.cos(Y), B*np.sin(X)+A*np.cos(Z), C*np.sin(Y)+B*np.cos(X)])
    wABC = _curl_spectral(uABC, k)
    beltrami_err = np.sqrt(np.mean((wABC - uABC)**2))   # should be ~0: omega = u
    lamb_abc = np.cross(uABC, wABC, axis=0)             # u x curl(u), NOT u x u
    uTG = np.array([np.sin(X)*np.cos(Y)*np.cos(Z), -np.cos(X)*np.sin(Y)*np.cos(Z), 0*X])
    wTG = _curl_spectral(uTG, k)
    lamb_tg = np.cross(uTG, wTG, axis=0)
    rms_abc = np.sqrt(np.mean(lamb_abc**2))
    rms_tg = np.sqrt(np.mean(lamb_tg**2))
    ratio = rms_abc/max(rms_tg, 1e-300)
    assert beltrami_err < 1e-10, f"ABC not Beltrami: curl(u)!=u, err {beltrami_err}"
    assert ratio < 1e-12, f"ABC Lamb not annihilated: {ratio}"
    return rms_abc, rms_tg, ratio, beltrami_err

if __name__ == "__main__":
    cond, ratio = check_vortex_collapse()
    print(f"al14: collapse condition = {cond:.1e} (exact 0); core -> {ratio*100:.1f}% of initial diameter")
    sh = check_shear_exponent()
    print("al5 : shear enhanced-dissipation exponents m/(m+2):",
          ", ".join(f"m={m}: {s:.3f}~{t:.3f}" for m, (s, t) in sh.items()))
    nk = check_neck_ode()
    print("al12: neck ODE d~(T-t)^(1/beta):",
          ", ".join(f"beta={b}: {s:.3f}~{t:.3f}" for b, (s, t) in nk.items()))
    K1, relK, T1, relT = check_frenet_scale_invariance()
    print(f"al6 : (total curvature, torsion variation) dilation-invariant to relative "
          f"{relK:.1e} and {relT:.1e}")
    ra, rt, r, berr = check_beltrami_lamb()
    print(f"al15: ABC is Beltrami (curl(u)-u rms {berr:.1e}); Lamb rms {ra:.1e} vs "
          f"Taylor-Green {rt:.3f}, ratio {r:.1e}")
    print("\nAll Part XXI anchor checks passed.")
