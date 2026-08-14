#!/usr/bin/env python3
"""Exact entropy of G(n, W) for the threshold graphon W(x,y)=1{x+y>=1}, n<=7.

The sampled labeled graph is a deterministic function of (pi, s): pi the
ascending order of y_i=|x_i-1/2| (uniform permutation) and s the sign pattern
(x_i>1/2), uniform on {0,1}^n, independent.  Adjacency: i~j iff both signs +,
or exactly one + and the +-signed vertex has the larger y.
Checks the Conjecture-18 negative control: H(G(n,W)) <= n log n - (1-log2) n + O(log n),
versus the naive quantization prediction H ~ n log n + o(n).
"""
import math, itertools
from collections import defaultdict

def exact_entropy(n):
    prob = defaultdict(float)
    labels = list(range(n))
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    w = 1.0/(math.factorial(n)*2**n)
    for order in itertools.permutations(labels):
        rank = [0]*n
        for pos, v in enumerate(order): rank[v] = pos
        for smask in range(2**n):
            key = 0
            for b, (i, j) in enumerate(pairs):
                si = (smask >> i) & 1; sj = (smask >> j) & 1
                if si and sj: key |= 1 << b
                elif si != sj:
                    plus, minus = (i, j) if si else (j, i)
                    if rank[plus] > rank[minus]: key |= 1 << b
            prob[key] += w
    Hn = -sum(p*math.log(p) for p in prob.values())
    return Hn, len(prob)

for n in range(2, 8):
    Hn, supp = exact_entropy(n)
    bound = math.log(math.factorial(n)) + (n-1)*math.log(2)
    lin = (Hn - n*math.log(n))/n
    print(f"n={n}: H={Hn:.5f}  support={supp}  log(n! 2^(n-1))={bound:.5f}  "
          f"(H - n log n)/n = {lin:+.5f}  [-(1-log2) = {-(1-math.log(2)):.5f}]")
