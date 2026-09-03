"""Independent verification for Part XXX (Conjectures 425-439): quantum algebras of
graphs and their modules, the algebraic layer of Proposition au:basic.

Exact checks (no floating point):
  1. Normal form in the quantum algebra A_q(Gamma): rewriting to ordered monomials is
     confluent (associativity of the product on random triples) for random graphs.
  2. Commutation rule x_v x^a = (-1)^{sum_{u E v} a_u} x^a x_v and the centre criterion
     for q = -1: a monomial is central iff its exponent vector lies in the kernel of
     the adjacency matrix modulo 2; odd-order graphs always have such vectors beyond
     the squares, since an alternating form of odd dimension is singular.
  3. Extension property: for random graphs on n vertices and random finite S with a
     marked vertex u, the frequency of a vertex adjacent to u and to no other
     element of S, approaching one as n grows (the mechanism of the trivial centre
     of the random graph).
  4. Odd powers of adjacent generators never commute, even powers are central.
  5. Fixed-scalar span formulas are stable: no half-graph pattern of length three for
     'w in span(b1, b2)' in finite modules over the quantum algebra of a small graph,
     by exact rank computation over the rationals.
  6. Squares of generators are central for q = -1.
  7. The two-vertex mechanism of Proposition au:basic(v): for distinct vertices a, c the
     equation x_a x_c = -x_v x_{v'} has a solution (v, v') iff a and c are adjacent (and then
     only (v, v') = (c, a)), so the formula 'exists v, v' (w = x_v x_{v'} u)' evaluates the
     edge relation on the line through a vector.
  8. The lemma behind the stability of the one-vertex formula 'exists v (w = x_v u)':
     +-x_s x_{t'} = x_{s'} x_t forces {s, t'} = {s', t} as multisets.
  9. The explicit exponent vectors giving an order pattern of length three for the
     relation alpha + beta in {2e_v + e_{v'}} (the formula with exponents two and one) on
     six pairwise non-adjacent vertices.

Run:  python3 verify/au_quantum_modules.py
"""
import sys, random, itertools
from fractions import Fraction
import numpy as np
import sympy as sp

PASS = []
def check(name, ok, detail=""):
    PASS.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
random.seed(20260903)

def random_graph(n, p=0.5):
    return {(i, j) for i in range(n) for j in range(i + 1, n) if random.random() < p}
def adjacent(G, u, v):
    return (min(u, v), max(u, v)) in G

class QAlg:
    """Quantum algebra of a graph with q = -1: elements are dicts word-tuple -> Fraction,
    with words kept in normal (sorted) form."""
    def __init__(self, G, n, q):
        self.G, self.n, self.q = G, n, Fraction(q)
    def normal_word(self, word):
        """Sort a word by bubble sort, tracking the q-factor from each adjacent swap."""
        w = list(word); coef = Fraction(1)
        changed = True
        while changed:
            changed = False
            for i in range(len(w) - 1):
                if w[i] > w[i + 1]:
                    # x_a x_b with a > b: x_a x_b = q^{-1} x_b x_a if adjacent (since x_b x_a = q x_a x_b when b<a? use symmetric rule)
                    a, b = w[i], w[i + 1]
                    if adjacent(self.G, a, b):
                        # relation: x_b x_a = q x_a x_b for b<a would break symmetry; we use x_u x_v = q x_v x_u for u E v with u < v.
                        # Here a > b, so x_a x_b = q^{-1} x_b x_a? From x_b x_a = q x_a x_b (b<a): x_a x_b = q^{-1} x_b x_a.
                        coef /= self.q
                    w[i], w[i + 1] = b, a; changed = True
        return tuple(w), coef
    def mul(self, A, B):
        out = {}
        for wa, ca in A.items():
            for wb, cb in B.items():
                w, c = self.normal_word(wa + wb)
                out[w] = out.get(w, Fraction(0)) + ca * cb * c
        return {w: c for w, c in out.items() if c != 0}
    def gen(self, v): return {(v,): Fraction(1)}
    def rand_elem(self, terms=3, deg=3):
        e = {}
        for _ in range(terms):
            w = tuple(sorted(random.randrange(self.n) for _ in range(random.randint(0, deg))))
            e[w] = e.get(w, Fraction(0)) + Fraction(random.randint(-3, 3))
        return {w: c for w, c in e.items() if c != 0}

# 1. confluence / associativity
ok = True
for trial in range(40):
    n = random.randint(3, 8); G = random_graph(n); A = QAlg(G, n, -1)
    a, b, c = A.rand_elem(), A.rand_elem(), A.rand_elem()
    if A.mul(A.mul(a, b), c) != A.mul(a, A.mul(b, c)): ok = False; break
check("normal form is associative on random triples (40 random graphs, q=-1)", ok)
# also check the defining relation in normal form: x_u x_v = q x_v x_u for u E v, u<v, and commute otherwise
ok = True
for trial in range(40):
    n = random.randint(2, 8); G = random_graph(n); A = QAlg(G, n, -1)
    u, v = sorted(random.sample(range(n), 2))
    lhs = A.mul(A.gen(u), A.gen(v)); rhs = A.mul(A.gen(v), A.gen(u))
    rhs = {w: c * (-1 if adjacent(G, u, v) else 1) for w, c in rhs.items()}
    if lhs != rhs: ok = False; break
check("defining relations hold in normal form", ok)

# 2. commutation rule and centre criterion
ok_rule = True; ok_centre = True
for trial in range(60):
    n = random.randint(2, 8); G = random_graph(n); A = QAlg(G, n, -1)
    a = [random.randint(0, 3) for _ in range(n)]
    word = tuple(itertools.chain.from_iterable([v] * a[v] for v in range(n)))
    xa = {word: Fraction(1)}; v = random.randrange(n)
    left = A.mul(A.gen(v), xa); right = A.mul(xa, A.gen(v))
    e = sum(a[u] for u in range(n) if u != v and adjacent(G, u, v))
    pred = {w: c * Fraction(-1) ** e for w, c in right.items()}
    if left != pred: ok_rule = False
    central = all(A.mul(A.gen(u), xa) == A.mul(xa, A.gen(u)) for u in range(n))
    Adj = np.array([[1 if adjacent(G, i, j) else 0 for j in range(n)] for i in range(n)])
    in_kernel = not np.any((Adj @ np.array(a)) % 2)
    if central != in_kernel: ok_centre = False
check("commutation rule x_v x^a = (-1)^{sum_{uEv} a_u} x^a x_v on random monomials", ok_rule)
check("monomial is central iff exponent vector lies in the kernel of the adjacency matrix mod 2", ok_centre)
# even n: the adjacency form mod 2 is nonsingular with positive frequency (then the centre is generated by squares)
for n in (6, 8):
    cnt = 0; T = 300
    for _ in range(T):
        G = random_graph(n); Adj = sp.Matrix([[1 if adjacent(G, i, j) else 0 for j in range(n)] for i in range(n)])
        if Adj.rank(iszerofunc=lambda x: x % 2 == 0) == n: cnt += 1
    check(f"random graphs on {n} vertices: adjacency form nonsingular mod 2 with positive frequency", 0.2 < cnt / T < 0.8, f"fraction {cnt/T:.2f}")
# odd n: adjacency matrix mod 2 is alternating, so always singular over F_2; over Q it may be nonsingular
n = 7; cnt = 0
for _ in range(200):
    G = random_graph(n); Adj = sp.Matrix([[1 if adjacent(G, i, j) else 0 for j in range(n)] for i in range(n)])
    if (Adj.applyfunc(lambda t: t % 2)).rank(iszerofunc=lambda x: x % 2 == 0) < n: cnt += 1
check("odd order: adjacency matrix is singular modulo 2 (alternating form), 200 graphs", cnt == 200, f"{cnt}/200")

# 3. extension property frequency
for n in (10, 20, 40):
    hits = 0; T = 400
    for _ in range(T):
        G = random_graph(n); S = random.sample(range(n), 3); u = S[0]
        if any(w not in S and adjacent(G, u, w) and not any(adjacent(G, w, s) for s in S if s != u) for w in range(n)): hits += 1
    check(f"extension witness (adjacent to u, to no other of |S|=3) exists in random graph on {n} vertices with frequency > 0.{'5' if n==10 else '85'}", hits / T > (0.5 if n == 10 else 0.85), f"frequency {hits/T:.3f}")

# 4. unbounded-degree noncommutation for graphs with an edge
ok = True
for trial in range(20):
    n = random.randint(2, 6); G = random_graph(n)
    if not G: continue
    (u, v) = next(iter(G)); A = QAlg(G, n, -1)
    for d in (1, 5, 9):
        xu = {tuple([u] * d): Fraction(1)}; xv = {tuple([v] * d): Fraction(1)}
        if A.mul(xu, xv) == A.mul(xv, xu): ok = False
    for d in (2, 4):
        xu = {tuple([u] * d): Fraction(1)}; xv = {tuple([v] * d): Fraction(1)}
        if A.mul(xu, xv) != A.mul(xv, xu): ok = False
check("odd powers of adjacent generators anticommute and even powers commute, q=-1", ok)

# 5. no half-graph of length 3 for w in span(b1,b2): exact rank over Q in a finite module
# Model: free module of rank r over the truncated algebra; represent vectors by coefficient
# dicts (basis index, word) -> Fraction; span over the algebra truncated at degree <= D is a Q-space.
def span_contains(A, basis_vecs, w, D):
    """Is w in the A-span of basis_vecs, using scalars of degree <= D? Exact linear algebra over Q."""
    words = [()] + [tuple(sorted(t)) for d in range(1, D + 1) for t in itertools.combinations_with_replacement(range(A.n), d)]
    words = sorted(set(words))
    gens = []
    for b in basis_vecs:
        for wd in words:
            s = {wd: Fraction(1)}
            vec = {}
            for (idx, bw), c in b.items():
                prod = A.mul(s, {bw: c})
                for pw, pc in prod.items():
                    vec[(idx, pw)] = vec.get((idx, pw), Fraction(0)) + pc
            gens.append(vec)
    keys = sorted(set(k for g in gens for k in g) | set(w))
    M = sp.Matrix([[g.get(k, 0) for k in keys] for g in gens])
    target = sp.Matrix([[w.get(k, 0) for k in keys]])
    return M.col_join(target).rank() == M.rank() if gens else all(v == 0 for v in w.values())
n = 3; G = {(0, 1), (1, 2)}; A = QAlg(G, n, -1)
# vectors in a free module of rank 4: e_i = {(i,()):1}
def e(i): return {(i, ()): Fraction(1)}
def xv(v, vec):
    out = {}
    for (i, wd), c in vec.items():
        for pw, pc in A.mul({(v,): Fraction(1)}, {wd: c}).items():
            out[(i, pw)] = out.get((i, pw), Fraction(0)) + pc
    return out
def add(*vs):
    out = {}
    for v in vs:
        for k, c in v.items(): out[k] = out.get(k, Fraction(0)) + c
    return {k: c for k, c in out.items() if c != 0}
# search for a half-graph of length 3: rows w_1,w_2,w_3 and columns (b1_j,b2_j), j=1..3, with w_i in span(b_j) iff i <= j
found = False
pool = [e(0), e(1), e(2), e(3), add(e(0), e(1)), xv(0, e(0)), xv(1, e(1)), add(e(0), xv(2, e(1))), add(xv(0, e(2)), e(3)), add(e(1), e(2), e(3))]
random.shuffle(pool)
for trial in range(150):
    ws = random.sample(pool, 3); cols = [tuple(random.sample(pool, 2)) for _ in range(3)]
    pattern = [[span_contains(A, list(cols[j]), ws[i], 1) for j in range(3)] for i in range(3)]
    if all(pattern[i][j] == (i <= j) for i in range(3) for j in range(3)): found = True; break
check("no half-graph of length three among 150 random configurations for 'w in span(b1,b2)' (fixed scalars of degree <= 1)", not found)
# dimension argument: a length-three half graph would need a 2-generated span to contain 3 independent vectors; verify independence of the pool triples used
# 6. squares are central for q = -1
ok = True
for trial in range(20):
    n = random.randint(2, 6); G = random_graph(n); A = QAlg(G, n, -1)
    if not G: continue
    u, v = next(iter(G)); sq = {(u, u): Fraction(1)}
    if any(A.mul(A.gen(w), sq) != A.mul(sq, A.gen(w)) for w in range(n)): ok = False
check("squares of generators are central for q = -1", ok)

# 7. two-vertex sign mechanism: x_a x_c = -x_v x_v' solvable iff a E c
ok = True; adj_cases = 0
for trial in range(30):
    n = random.randint(3, 7); G = random_graph(n); A = QAlg(G, n, -1)
    for a in range(n):
        for c in range(n):
            if a == c: continue
            lhs = A.mul(A.gen(a), A.gen(c))
            sols = [(v, vp) for v in range(n) for vp in range(n)
                    if A.mul({(): Fraction(-1)}, A.mul(A.gen(v), A.gen(vp))) == lhs]
            if adjacent(G, a, c):
                adj_cases += 1
                if sols != [(c, a)]: ok = False
            elif sols: ok = False
check("x_a x_c = -x_v x_v' has a solution iff a E c, and then only (v,v') = (c,a)", ok and adj_cases > 0, f"{adj_cases} adjacent pairs")
# 8. lemma: +-x_s x_t' = x_s' x_t forces {s,t'} = {s',t}
ok = True
for trial in range(30):
    n = random.randint(2, 6); G = random_graph(n); A = QAlg(G, n, -1)
    for s_, t, sp_, tp_ in itertools.product(range(n), repeat=4):
        l = A.mul(A.gen(s_), A.gen(tp_)); r = A.mul(A.gen(sp_), A.gen(t))
        if l == r or A.mul({(): Fraction(-1)}, l) == r:
            if sorted([s_, tp_]) != sorted([sp_, t]): ok = False
check("+-x_s x_t' = x_s' x_t only when {s,t'} = {s',t} (lemma for the one-vertex formula)", ok)
# 9. order pattern of length three for alpha + beta in Shape = {2e_v + e_v'} (exponents two and one)
a, p, b1, b2, b3, s_ = range(6)
def vec(**kw):
    out = [0] * 6
    for k, val in kw.items(): out[{'a': a, 'p': p, 'b1': b1, 'b2': b2, 'b3': b3, 's': s_}[k]] += val
    return out
alpha = [vec(a=2, b1=1), vec(a=2, b3=1, b2=-1, b1=1), vec(a=4, s=1, p=-2, b2=-1, b1=1)]
beta = [vec(), vec(b2=1, b1=-1), vec(p=2, b2=1, a=-2, b1=-1)]
def in_shape(v):
    return sorted(v) == [0, 0, 0, 0, 1, 2]
ok = all(in_shape([x + y for x, y in zip(alpha[i], beta[j])]) == (i <= j) for i in range(3) for j in range(3))
check("explicit order pattern of length three for alpha + beta in {2e_v + e_v'} on six non-adjacent vertices", ok)

print(f"\n{sum(PASS)}/{len(PASS)} checks passed")
sys.exit(0 if all(PASS) else 1)
