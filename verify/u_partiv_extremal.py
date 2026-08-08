#!/usr/bin/env python3
"""Part IV extremal reductions, verified from scratch.

Two proved results integrated from the independent audit are reverified here with an
implementation that builds rho_G(S) directly from closed neighbourhoods and component
counts, using exact rational arithmetic for the distributions.

(1) Reduction of the star majorization (Conjecture 73). For a tree T on n>=3 vertices and a
    prime power q, the decreasingly ordered adjoint-rank distribution of the star K_{1,n-1}
    majorizes that of T iff  max_r pi_{T,q}(r) <= 1 - 1/q.  We check the equivalence directly
    over all trees and confirm both sides hold for n>=5 and both fail at (n,q)=(4,2).

(2) Forward equality halves of Conjectures 75 and 76. s(P_n)=n and s(K_{1,n-1})=3 (n>=3),
    each equal to n-leaf+2 and diam+1, so path and star attain equality in both bounds.
"""
from fractions import Fraction as Fr
from itertools import combinations
import networkx as nx


def rho(G, S):
    NS = set(S)
    for v in S:
        NS |= set(G[v])
    c = nx.number_connected_components(G.subgraph(S)) if S else 0
    return len(NS) - c


def rank_dist(G, q):
    n = G.number_of_nodes()
    nodes = list(G.nodes())
    dist = {}
    for k in range(n + 1):
        for S in combinations(nodes, k):
            r = rho(G, list(S))
            dist[r] = dist.get(r, Fr(0)) + Fr((q - 1) ** k, q ** n)
    return dist


def s_count(G):
    n = G.number_of_nodes()
    nodes = list(G.nodes())
    vals = set()
    for k in range(n + 1):
        for S in combinations(nodes, k):
            vals.add(rho(G, list(S)))
    return len(vals)


def path(n):
    return nx.path_graph(n)


def star(n):
    G = nx.Graph()
    G.add_node(0)
    for i in range(1, n):
        G.add_edge(0, i)
    return G


def majorizes(g, f):
    gs = sorted(g, reverse=True)
    fs = sorted(f, reverse=True)
    L = max(len(gs), len(fs))
    gs += [Fr(0)] * (L - len(gs))
    fs += [Fr(0)] * (L - len(fs))
    sg = sf = Fr(0)
    for i in range(L):
        sg += gs[i]
        sf += fs[i]
        if sg < sf:
            return False
    return True


def main():
    # (1) reduction equivalence, all trees through n=10, q in {2,3,4,5}
    for q in (2, 3, 4, 5):
        for n in range(3, 11):
            sd = list(rank_dist(star(n), q).values())
            for T in nx.nonisomorphic_trees(n):
                td = rank_dist(T, q)
                maj = majorizes(sd, list(td.values()))
                red = max(td.values()) <= 1 - Fr(1, q)
                assert maj == red, (q, n, "equivalence fails")
                if n >= 5:
                    assert maj and red, (q, n, "n>=5 should hold")
    # sharpness at (4,2): star does NOT majorize the path, and max atom exceeds 1-1/q
    sd4 = list(rank_dist(star(4), 2).values())
    pd4 = rank_dist(path(4), 2)
    assert not majorizes(sd4, list(pd4.values()))
    assert max(pd4.values()) > 1 - Fr(1, 2)
    print("C73 reduction: majorization <=> max-atom<=1-1/q verified (trees n<=10, q in 2,3,4,5);")
    print("             both hold for n>=5, both fail at (n,q)=(4,2)")

    # (2) forward equality: s(P_n)=n, s(star)=3, matching n-leaf+2 and diam+1
    for n in range(2, 12):
        P = path(n)
        lp = sum(1 for v in P if P.degree(v) == 1)
        assert s_count(P) == n == (n - lp + 2) == (nx.diameter(P) + 1)
        if n >= 3:
            K = star(n)
            lk = sum(1 for v in K if K.degree(v) == 1)
            assert s_count(K) == 3 == (n - lk + 2) == (nx.diameter(K) + 1)
    print("C75/C76 forward halves: s(P_n)=n and s(star)=3 attain both bounds (n<=11)")


if __name__ == "__main__":
    main()
