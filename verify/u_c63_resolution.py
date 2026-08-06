#!/usr/bin/env python3
"""Conjecture 63 resolution: verify the refuting seven-vertex unicyclic pair and its uniqueness.

The pair was communicated in external review. This script confirms, with the
independent implementation, that the two connected unicyclic graphs share
C(2,Y) while their class-counting polynomials differ, and that this is the
unique violating class among all trees and connected unicyclic graphs through
nine vertices. The tree case is verified exhaustively through fourteen vertices
in u_boundary_collisions-style sweeps (see run below).
"""
import u_core_atlas as V
from u_boundary_collisions import tree_N
import networkx as nx

EA = [(0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (3, 6), (4, 5)]
EB = [(0, 1), (0, 3), (0, 4), (1, 2), (2, 5), (2, 6), (5, 6)]


def Nkey(N):
    return tuple(sorted(N.items()))


def main():
    n = 7
    NA, NB = V.count_matrix(n, EA), V.count_matrix(n, EB)
    GA, GB = nx.Graph(EA), nx.Graph(EB)
    assert nx.is_connected(GA) and nx.is_connected(GB)
    assert GA.number_of_edges() == GB.number_of_edges() == 7
    assert not nx.is_isomorphic(GA, GB)
    assert V.Cq_vec(NA, 2) == V.Cq_vec(NB, 2) == (1, 3, 7, 29, 32, 40, 16)
    assert Nkey(NA) != Nkey(NB)
    assert V.Cq_vec(NA, 3) != V.Cq_vec(NB, 3)
    assert nx.is_bipartite(GA) and not nx.is_chordal(GA)
    assert nx.is_chordal(GB) and not nx.is_bipartite(GB)
    print("refuting pair confirmed: shared C(2,Y), distinct C, distinct C(3,Y),")
    print("one bipartite non-chordal member and one chordal non-bipartite member")

    # uniqueness through nine vertices
    for m in range(4, 10):
        graphs = []
        for T in nx.nonisomorphic_trees(m):
            mp = {v: i for i, v in enumerate(T.nodes())}
            te = [tuple(sorted((mp[a], mp[b]))) for a, b in T.edges()]
            graphs.append(tuple(sorted(te)))
            es = set(te)
            for a in range(m):
                for b in range(a + 1, m):
                    if (a, b) not in es:
                        graphs.append(tuple(sorted(es | {(a, b)})))
        buckets = {}
        for e in graphs:
            N = V.count_matrix(m, e)
            buckets.setdefault(V.Cq_vec(N, 2), {}).setdefault(Nkey(N), []).append(e)
        viol = [d for d in buckets.values() if len(d) > 1]
        expect = 1 if m == 7 else 0
        assert len(viol) == expect, (m, len(viol))
        print(f"connected pseudoforests n={m}: violating binary classes = {len(viol)}")

    # tree case exhaustively through fourteen vertices
    for m in range(4, 15):
        buckets = {}
        for T in nx.nonisomorphic_trees(m):
            mp = {v: i for i, v in enumerate(T.nodes())}
            te = [(mp[a], mp[b]) for a, b in T.edges()]
            N = tree_N(m, te)
            buckets.setdefault(V.Cq_vec(N, 2), set()).add(Nkey(N))
        assert all(len(s) == 1 for s in buckets.values()), m
        print(f"trees n={m}: binary rigidity holds")


if __name__ == "__main__":
    main()
