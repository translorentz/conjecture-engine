#!/usr/bin/env python3
"""Conjecture 71 resolution: the interval-support-at-fixed-rank claim is false.

Reconstructed from scratch. rho_G(S) = |N[S]| - c(G[S]); for each attainable rank the set of
support sizes K_r(G) is checked for interior gaps. The connected eight-vertex graph below has
K_5 = {1,3,4,5,6}, a gap at size two. An exhaustive scan of all 12,346 unlabelled graphs on
eight vertices (McKay's census) finds exactly two violations, both connected, and none on
seven or fewer vertices. The failure does not reach Conjecture 70: the shifted rank slices
A_{G,r}(Z) = (1+Z)^{|E|-r} B_{G,r}(Z) stay strictly log-concave on the refuting graphs,
because the binomial factor fills the raw-support gap.

Requires the graph8 census (evidence/graph8.g6) only for the exhaustive count; the single
witness and the C70 survival are checked without it.
"""
import os
from itertools import combinations
from collections import defaultdict
from math import comb
import networkx as nx

WITNESS = [(0, 3), (0, 6), (0, 7), (1, 4), (1, 6), (1, 7), (2, 5),
           (2, 6), (3, 6), (3, 7), (4, 6), (4, 7), (5, 7)]


def rho(G, S):
    NS = set(S)
    for v in S:
        NS |= set(G[v])
    c = nx.number_connected_components(G.subgraph(S)) if S else 0
    return len(NS) - c


def gap_ranks(G):
    nodes = list(G.nodes())
    rs = defaultdict(set)
    for k in range(len(nodes) + 1):
        for S in combinations(nodes, k):
            rs[rho(G, list(S))].add(k)
    out = []
    for r, sz in rs.items():
        s = sorted(sz)
        if s != list(range(s[0], s[-1] + 1)):
            out.append((r, s))
    return out


def polymul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def strict_logconcave(c):
    for i in range(1, len(c) - 1):
        if c[i - 1] > 0 and c[i + 1] > 0 and c[i] > 0:
            if not c[i] * c[i] > c[i - 1] * c[i + 1]:
                return False
    return True


def main():
    G = nx.Graph(WITNESS)
    n, m = G.number_of_nodes(), G.number_of_edges()
    assert n == 8 and nx.is_connected(G)
    gaps = gap_ranks(G)
    assert gaps == [(5, [1, 3, 4, 5, 6])], gaps
    print("C71 witness GCOfuw: K_5 =", gaps[0][1], "-> interior gap at size 2, connected")

    # C70 survives on the witness: raw B_{G,5} has a gap, shifted slice A_{G,5} does not.
    Braw = defaultdict(lambda: defaultdict(int))
    for k in range(n + 1):
        for S in combinations(range(n), k):
            Braw[rho(G, list(S))][k] += 1
    B5 = [Braw[5].get(k, 0) for k in range(n + 1)]
    assert B5[2] == 0 and B5[1] and B5[3], "raw B_{G,5} should gap at size 2"
    allok = True
    for r in Braw:
        A = polymul([comb(m - r, i) for i in range(m - r + 1)],
                    [Braw[r].get(k, 0) for k in range(n + 1)])
        if sum(1 for x in A if x) > 1 and not strict_logconcave(A):
            allok = False
    assert allok
    print("C70 survives: every shifted rank slice of the witness is strictly log-concave")

    # minimality: no violation on <= 7 vertices
    for nn in range(1, 8):
        v = sum(1 for H in nx.graph_atlas_g()
                if H.number_of_nodes() == nn and gap_ranks(H))
        assert v == 0, (nn, v)
    print("no violation on 7 or fewer vertices (graph atlas)")

    # exhaustive count over all 8-vertex graphs, if the census is present
    for cand in ("evidence/graph8.g6",
                 os.path.join(os.path.dirname(__file__), "graph8.g6")):
        if os.path.exists(cand):
            viol = []
            with open(cand, "rb") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    H = nx.from_graph6_bytes(line)
                    if gap_ranks(H):
                        viol.append((nx.to_graph6_bytes(H, header=False).strip().decode(),
                                     nx.is_connected(H)))
            assert len(viol) == 2 and all(c for _, c in viol), viol
            print("exhaustive 8-vertex scan: exactly two violations, both connected:",
                  [g for g, _ in viol])
            break
    else:
        print("(graph8 census not present; skipped the exhaustive count)")


if __name__ == "__main__":
    main()
