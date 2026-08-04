"""Conjecture 55 stress test: adversarial search for the worst TV^2 / entropy-defect ratio
over small finite abelian groups, plus interval and discretized-Gaussian families on Z/p.
The observed supremum approaches 2/log 2, the conjectured sharp constant."""
"""Stress test for Conjecture 9 (sec 10): inf_{H,a} TV(mu, u_{a+H})^2 <= C * (H(mu*mu)-H(mu)).

Search for the WORST (largest) ratio  R(mu) = minTV^2 / Delta(mu)
over small finite abelian groups.
"""
import numpy as np
import itertools, sys

rng = np.random.default_rng(20260804)

def make_group(dims):
    """Return group data for Z/d1 x Z/d2 x ...: element list, index maps."""
    dims = tuple(dims)
    elems = list(itertools.product(*[range(d) for d in dims]))
    idx = {e: i for i, e in enumerate(elems)}
    return dims, elems, idx

def convolve(p, dims):
    """Self-convolution mu*mu on product of cyclic groups via FFT."""
    a = p.reshape(dims)
    fa = np.fft.fftn(a)
    c = np.fft.ifftn(fa * fa).real
    c = np.clip(c, 0.0, None)
    c = c / c.sum()
    return c.reshape(-1)

def entropy(p):
    q = p[p > 1e-300]
    return -np.sum(q * np.log(q))

def delta(p, dims):
    return entropy(convolve(p, dims)) - entropy(p)

def subgroups(dims, elems, idx):
    """All subgroups, as sorted tuples of element-indices. Generate closures of <=3 generators."""
    n = len(elems)
    dims_arr = np.array(dims)
    def add(i, j):
        e = tuple((np.array(elems[i]) + np.array(elems[j])) % dims_arr)
        return idx[e]
    # addition table
    table = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            table[i, j] = add(i, j)
    subs = set()
    zero = idx[tuple([0]*len(dims))]
    def closure(gens):
        S = {zero}
        frontier = set(gens) | {zero}
        S |= frontier
        changed = True
        while changed:
            changed = False
            new = set()
            for a in S:
                for b in S:
                    c = table[a, b]
                    if c not in S:
                        new.add(c)
            if new:
                S |= new
                changed = True
        return frozenset(S)
    subs.add(frozenset({zero}))
    els = list(range(n))
    for r in range(1, 4):
        for gens in itertools.combinations(els, r):
            subs.add(closure(gens))
    return [sorted(s) for s in subs], table

def coset_uniforms(dims, elems, idx, subs, table):
    """Return list of uniform-on-coset probability vectors (as arrays)."""
    n = len(elems)
    out = []
    for H in subs:
        seen = set()
        for a in range(n):
            coset = frozenset(table[a, h] for h in H)
            if coset in seen:
                continue
            seen.add(coset)
            u = np.zeros(n)
            u[list(coset)] = 1.0/len(coset)
            out.append(u)
    return np.array(out)

def min_tv(p, cosets):
    return 0.5*np.min(np.abs(cosets - p[None, :]).sum(axis=1))

def ratio(p, dims, cosets, dmin=1e-12):
    d = delta(p, dims)
    if d < dmin:
        return -1.0, d
    t = min_tv(p, cosets)
    return t*t/d, d

def softmax(x):
    y = np.exp(x - x.max())
    return y/y.sum()

def grad_ascent(x0, dims, cosets, steps=400, lr=0.5):
    """Maximize log-ratio over softmax parametrization, numeric gradient."""
    x = x0.copy()
    n = len(x)
    best_r, _ = ratio(softmax(x), dims, cosets)
    best_x = x.copy()
    h = 1e-5
    for it in range(steps):
        p = softmax(x)
        r0, d0 = ratio(p, dims, cosets)
        if r0 < 0:
            break
        g = np.zeros(n)
        for i in range(n):
            xi = x.copy(); xi[i] += h
            r1, _ = ratio(softmax(xi), dims, cosets)
            g[i] = (r1 - r0)/h
        gn = np.linalg.norm(g)
        if gn < 1e-12:
            break
        x = x + lr*g/gn
        r2, _ = ratio(softmax(x), dims, cosets)
        if r2 > best_r:
            best_r = r2; best_x = x.copy()
        elif r2 < r0 - 1e-9:
            lr *= 0.7
            if lr < 1e-4: break
    return best_r, softmax(best_x)

def describe(p, k=8):
    ii = np.argsort(-p)[:k]
    return ", ".join(f"{i}:{p[i]:.3f}" for i in ii if p[i] > 1e-4)

def run_group(dims, n_random=300, n_grad=25, verbose=True):
    dims, elems, idx = make_group(dims)
    subs, table = subgroups(dims, elems, idx)
    cosets = coset_uniforms(dims, elems, idx, subs, table)
    n = len(elems)
    results = []

    # 1. random Dirichlet measures at several concentrations
    for conc in [0.05, 0.2, 1.0, 5.0]:
        for _ in range(n_random):
            p = rng.dirichlet(np.full(n, conc))
            r, d = ratio(p, dims, cosets)
            results.append((r, d, p, f"dirichlet({conc})"))

    # 2. sparse supports
    for k in range(2, min(n, 13)):
        for _ in range(60):
            S = rng.choice(n, size=k, replace=False)
            w = rng.dirichlet(np.ones(k))
            p = np.zeros(n); p[S] = w
            r, d = ratio(p, dims, cosets)
            results.append((r, d, p, f"sparse(k={k})"))

    # 3. intervals / APs (in the first cyclic factor if rank>1, else in Z/n)
    if len(dims) == 1:
        N = dims[0]
        for step in range(1, N):
            for m in range(2, N):
                for start in range(0, N, max(1, N//6)):
                    S = [(start + step*i) % N for i in range(m)]
                    if len(set(S)) < m: continue
                    p = np.zeros(n); p[[idx[(s,)] for s in S]] = 1.0/m
                    r, d = ratio(p, dims, cosets)
                    results.append((r, d, p, f"AP(step={step},m={m})"))

    # 4. near-coset perturbations: u_{a+H} + eps*perturbation
    for ci in range(len(cosets)):
        u = cosets[ci]
        for eps in [1e-3, 1e-2, 0.05, 0.15, 0.3]:
            for _ in range(25):
                f = rng.standard_normal(n)
                q = u + eps*f/np.abs(f).sum()
                q = np.clip(q, 0, None); s = q.sum()
                if s <= 0: continue
                q /= s
                r, d = ratio(q, dims, cosets)
                results.append((r, d, q, f"near-coset(eps={eps})"))

    # 5. mixtures of two coset uniforms
    for _ in range(400):
        i, j = rng.choice(len(cosets), size=2, replace=False)
        lam = rng.uniform(0.01, 0.5)
        q = (1-lam)*cosets[i] + lam*cosets[j]
        r, d = ratio(q, dims, cosets)
        results.append((r, d, q, f"coset-mixture(lam={lam:.2f})"))

    results = [t for t in results if t[0] > 0]
    results.sort(key=lambda t: -t[0])

    # 6. gradient ascent from best seeds + random seeds
    seeds = [np.log(np.clip(t[2], 1e-9, None)) for t in results[:n_grad]]
    seeds += [rng.standard_normal(n)*2 for _ in range(n_grad)]
    best = results[0][0] if results else 0.0
    best_p = results[0][2] if results else None
    best_tag = results[0][3] if results else ""
    for x0 in seeds:
        r, p = grad_ascent(x0, dims, cosets, steps=250)
        if r > best:
            best, best_p, best_tag = r, p, "grad-ascent"
    d = delta(best_p, dims)
    t = min_tv(best_p, cosets)
    if verbose:
        print(f"G={'x'.join('Z/%d'%d_ for d_ in dims)}  worst ratio={best:.4f}  "
              f"(TV={t:.4f}, Delta={d:.5f}, from {best_tag})")
        print(f"   worst mu (top atoms): {describe(best_p)}")
    return best, best_p, best_tag

if __name__ == "__main__":
    groups = [ (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (11,), (12,),
               (13,), (14,), (15,), (16,), (17,), (18,), (19,), (20,), (21,), (22,), (23,), (24,),
               (2,2), (2,4), (3,3), (2,2,2), (2,6), (2,8), (2,10), (4,4), (2,12), (3,6) ]
    overall = 0.0; overall_g = None
    for g in groups:
        b, p, tag = run_group(g)
        if b > overall:
            overall = b; overall_g = g
    print(f"\nOVERALL worst ratio found: {overall:.4f} on {overall_g}")
