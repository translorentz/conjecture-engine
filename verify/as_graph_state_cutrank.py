#!/usr/bin/env python3
"""Independent finite checks for Conjectures 395--409.

The script reproduces exact calibrations, finite shape tests, explicit
negative controls, small rank-width computations, and seeded LC-orbit data.
It is a falsification suite: no finite run proves an asymptotic conjecture.
"""

from __future__ import annotations

import itertools
import math
from collections import Counter, defaultdict, deque
from fractions import Fraction

import networkx as nx
import numpy as np


def gf2_rank(rows: list[int]) -> int:
    """Rank of bit-packed rows over F_2."""
    rows = [row for row in rows if row]
    rank = 0
    while rows:
        pivot = max(rows)
        if pivot == 0:
            break
        rows.remove(pivot)
        bit = 1 << (pivot.bit_length() - 1)
        rows = [row ^ pivot if row & bit else row for row in rows]
        rank += 1
    return rank


def graph_rows(graph: nx.Graph) -> list[int]:
    graph = nx.convert_node_labels_to_integers(graph, ordering="sorted")
    rows = [0] * graph.number_of_nodes()
    for u, v in graph.edges():
        rows[u] |= 1 << v
        rows[v] |= 1 << u
    return rows


def cut_rank(rows: list[int], subset: int) -> int:
    outside = ((1 << len(rows)) - 1) ^ subset
    return gf2_rank([rows[v] & outside for v in range(len(rows))
                     if subset >> v & 1])


def cut_signature(rows: list[int]) -> tuple[int, ...]:
    return tuple(cut_rank(rows, subset) for subset in range(1 << len(rows)))


def z_signature(graph: nx.Graph) -> tuple[tuple[int, int, int], ...]:
    rows = graph_rows(graph)
    counts: Counter[tuple[int, int]] = Counter()
    for subset in range(1 << len(rows)):
        counts[(subset.bit_count(), cut_rank(rows, subset))] += 1
    return tuple((size, rank, count) for (size, rank), count
                 in sorted(counts.items()))


def edge_mask_to_rows(n: int, mask: int) -> list[int]:
    rows = [0] * n
    bit = 0
    for u in range(n):
        for v in range(u + 1, n):
            if mask >> bit & 1:
                rows[u] |= 1 << v
                rows[v] |= 1 << u
            bit += 1
    return rows


def rows_to_edge_mask(rows: list[int]) -> int:
    mask = 0
    bit = 0
    for u in range(len(rows)):
        for v in range(u + 1, len(rows)):
            if rows[u] >> v & 1:
                mask |= 1 << bit
            bit += 1
    return mask


def local_complement(rows: list[int], vertex: int) -> list[int]:
    out = rows.copy()
    neighbours = [v for v in range(len(rows)) if rows[vertex] >> v & 1]
    for i, u in enumerate(neighbours):
        for v in neighbours[i + 1:]:
            out[u] ^= 1 << v
            out[v] ^= 1 << u
    return out


def lc_orbit(rows: list[int]) -> set[int]:
    start = rows_to_edge_mask(rows)
    seen = {start}
    queue = deque([rows])
    while queue:
        current = queue.popleft()
        for vertex in range(len(rows)):
            nxt = local_complement(current, vertex)
            code = rows_to_edge_mask(nxt)
            if code not in seen:
                seen.add(code)
                queue.append(nxt)
    return seen


def rectangular_rank_count(q: int, m: int, n: int, rank: int) -> int:
    numerator = math.prod((q**m - q**i) * (q**n - q**i)
                          for i in range(rank))
    denominator = math.prod(q**rank - q**i for i in range(rank))
    return numerator // denominator


def matrix_calibration() -> bool:
    q, m, n = 2, 3, 4
    exact = Counter()
    for bits in range(1 << (m * n)):
        rows = [((bits >> (i * n)) & ((1 << n) - 1)) for i in range(m)]
        exact[gf2_rank(rows)] += 1
    formula = {r: rectangular_rank_count(q, m, n, r)
               for r in range(min(m, n) + 1)}
    return dict(exact) == formula and sum(formula.values()) == q ** (m * n)


def distance_mean_identity_check(max_n: int = 20) -> bool:
    """Check the two exact formulas for Lambda_n(ell) in Conjecture 397."""
    for n in range(1, max_n + 1):
        for ell in range(1, n + 1):
            subset_sum = Fraction(0)
            for a in range(1, ell + 1):
                binomial_tail = sum(math.comb(n - a, j)
                                    for j in range(ell - a + 1))
                subset_sum += Fraction(math.comb(n, a) * binomial_tail,
                                       2 ** (n - a))
            code_sum = Fraction(
                sum(math.comb(n, w) * (3 ** w - 1)
                    for w in range(1, ell + 1)),
                2 ** n,
            )
            if subset_sum != code_sum:
                return False
    return True


def labelled_cutrank_lc_check(max_n: int = 6) -> tuple[bool, list[tuple[int, int]]]:
    rows_out = []
    for n in range(1, max_n + 1):
        edge_count = n * (n - 1) // 2
        visited: set[int] = set()
        fibre_owner: dict[tuple[int, ...], int] = {}
        orbits = 0
        for code in range(1 << edge_count):
            if code in visited:
                continue
            rows = edge_mask_to_rows(n, code)
            orbit = lc_orbit(rows)
            visited.update(orbit)
            signatures = {cut_signature(edge_mask_to_rows(n, item))
                          for item in orbit}
            if len(signatures) != 1:
                return False, rows_out
            signature = signatures.pop()
            if signature in fibre_owner:
                return False, rows_out
            fibre_owner[signature] = code
            orbits += 1
        rows_out.append((n, orbits))
    return True, rows_out


def tree_matching_number(n: int, edges: list[tuple[int, int]], mask: int) -> int:
    adjacency = [[] for _ in range(n)]
    for index, (u, v) in enumerate(edges):
        if mask >> index & 1:
            adjacency[u].append(v)
            adjacency[v].append(u)

    seen = [False] * n
    total = 0

    def visit(vertex: int, parent: int) -> tuple[int, int]:
        # free: best below vertex when it is not matched to its parent;
        # blocked: best when it is already matched to its parent.
        base = 0
        gains = []
        for child in adjacency[vertex]:
            if child == parent:
                continue
            child_free, child_blocked = visit(child, vertex)
            base += child_free
            gains.append(1 + child_blocked - child_free)
        return base + max([0] + gains), base

    for root in range(n):
        if seen[root]:
            continue
        # Mark this retained-edge component; visit itself does the DP.
        stack = [root]
        seen[root] = True
        while stack:
            v = stack.pop()
            for w in adjacency[v]:
                if not seen[w]:
                    seen[w] = True
                    stack.append(w)
        total += visit(root, -1)[0]
    return total


def percolated_profile(tree: nx.Graph) -> tuple[int, ...]:
    graph = nx.convert_node_labels_to_integers(tree, ordering="sorted")
    edges = list(graph.edges())
    counts = Counter(tree_matching_number(len(graph), edges, mask)
                     for mask in range(1 << len(edges)))
    return tuple(counts[j] for j in range(max(counts) + 1))


def log_concave(values: tuple[int, ...]) -> bool:
    return all(values[i] ** 2 >= values[i - 1] * values[i + 1]
               for i in range(1, len(values) - 1))


def ultra_log_concave(values: tuple[int, ...]) -> bool:
    degree = len(values) - 1
    scaled = [values[i] / math.comb(degree, i) for i in range(degree + 1)]
    return all(scaled[i] ** 2 + 1e-12 >= scaled[i - 1] * scaled[i + 1]
               for i in range(1, degree))


def forest_shape_checks(max_n: int = 12) -> tuple[bool, int, float]:
    checked = 0
    max_real_part = -math.inf
    for n in range(3, max_n + 1):
        for tree in nx.generators.nonisomorphic_trees(n):
            profile = percolated_profile(tree)
            if not log_concave(profile):
                return False, checked, max_real_part
            roots = np.roots(list(reversed(profile)))
            if len(roots):
                max_real_part = max(max_real_part,
                                    float(np.max(np.real(roots))))
                if np.max(np.real(roots)) >= 1e-8:
                    return False, checked, max_real_part
            checked += 1
    return True, checked, max_real_part


def forest_negative_controls() -> tuple[bool, tuple[int, ...], tuple[int, ...]]:
    ulc_tree = nx.from_graph6_bytes(b"LqD?I?@O??g??@")
    ulc_profile = percolated_profile(ulc_tree)
    target = (1, 13, 30, 20)
    real_root_failure = any(np.max(np.abs(np.imag(np.roots(list(reversed(
        percolated_profile(tree))))))) > 1e-7
        and percolated_profile(tree) == target
        for tree in nx.generators.nonisomorphic_trees(7))
    return (not ultra_log_concave(ulc_profile) and real_root_failure,
            ulc_profile, target)


def bernstein_tail_counts(tree: nx.Graph) -> dict[tuple[int, int], int]:
    graph = nx.convert_node_labels_to_integers(tree, ordering="sorted")
    edges = list(graph.edges())
    out: Counter[tuple[int, int]] = Counter()
    for mask in range(1 << len(edges)):
        matching = tree_matching_number(len(graph), edges, mask)
        retained = mask.bit_count()
        for threshold in range(1, matching + 1):
            out[(threshold, retained)] += 1
    return dict(out)


def coefficientwise_leq(left: dict[tuple[int, int], int],
                        right: dict[tuple[int, int], int],
                        edge_count: int) -> bool:
    for threshold in range(1, edge_count + 2):
        for retained in range(edge_count + 1):
            if left.get((threshold, retained), 0) > right.get(
                    (threshold, retained), 0):
                return False
    return True


def broom_graph(n: int, leaves: int) -> nx.Graph:
    graph = nx.star_graph(leaves)
    old_leaf = 1
    previous = 0
    graph.remove_edge(0, old_leaf)
    for vertex in range(leaves + 1, n):
        graph.add_edge(previous, vertex)
        previous = vertex
    graph.add_edge(previous, old_leaf)
    return nx.convert_node_labels_to_integers(graph)


def tree_extremal_checks(max_n: int = 11) -> tuple[bool, int]:
    checked = 0
    for n in range(3, max_n + 1):
        star = bernstein_tail_counts(nx.star_graph(n - 1))
        path = bernstein_tail_counts(nx.path_graph(n))
        brooms = {leaves: bernstein_tail_counts(broom_graph(n, leaves))
                  for leaves in range(2, n)}
        for tree in nx.generators.nonisomorphic_trees(n):
            profile = bernstein_tail_counts(tree)
            if not (coefficientwise_leq(star, profile, n - 1)
                    and coefficientwise_leq(profile, path, n - 1)):
                return False, checked
            leaves = sum(tree.degree(v) == 1 for v in tree)
            if not coefficientwise_leq(brooms[leaves], profile, n - 1):
                return False, checked
            checked += 1
    return True, checked


def tree_collision_check() -> tuple[bool, int]:
    first = nx.from_graph6_bytes(b"NpCa?C@?a??@?@O???G")
    second = nx.from_graph6_bytes(b"NpCc?D??G?_@O???g??")
    return (not nx.is_isomorphic(first, second)
            and z_signature(first) == z_signature(second),
            len(z_signature(first)))


def positive_tail_atlas_check() -> tuple[bool, int]:
    checked = 0
    for graph in nx.graph_atlas_g():
        if len(graph) == 0:
            continue
        rows = graph_rows(graph)
        counts = Counter(cut_rank(rows, subset)
                         for subset in range(1 << len(rows)))
        tail = tuple(counts[r] for r in range(1, max(counts) + 1))
        if not log_concave(tail):
            return False, checked
        checked += 1
    return True, checked


def rank_one_counterexample_check() -> tuple[bool, tuple[int, ...]]:
    """Verify the explicit sharp boundary for positive-tail log-concavity."""
    graph = nx.from_graph6_bytes(b"LG??XrL?[A?KCW")
    rows = graph_rows(graph)
    counts = Counter(cut_rank(rows, subset)
                     for subset in range(1 << len(rows)))
    profile = tuple(counts[r] for r in range(max(counts) + 1))
    target = (2, 28, 410, 1896, 3296, 2208, 352)
    passed = (nx.is_connected(graph) and graph.number_of_edges() == 20
              and profile == target
              and profile[1] ** 2 < profile[0] * profile[2])
    return passed, profile


def exact_rank_width(graph: nx.Graph) -> int:
    rows = graph_rows(graph)
    n = len(rows)
    full = (1 << n) - 1
    rho = [cut_rank(rows, subset) for subset in range(1 << n)]
    dp = [0] * (1 << n)
    for size in range(2, n + 1):
        for subset in (s for s in range(1, full + 1)
                       if s.bit_count() == size):
            anchor = subset & -subset
            best = n
            part = (subset - 1) & subset
            while part:
                if part & anchor:
                    other = subset ^ part
                    candidate = max(dp[part], dp[other], rho[part], rho[other])
                    best = min(best, candidate)
                part = (part - 1) & subset
            dp[subset] = best
    return dp[full]


def cubic_width_calibration() -> tuple[bool, list[tuple[int, float]]]:
    rng = np.random.default_rng(406)
    rows = []
    for n, samples in ((8, 4), (10, 4), (12, 3)):
        widths = []
        for _ in range(samples):
            seed = int(rng.integers(0, 2**31 - 1))
            widths.append(exact_rank_width(nx.random_regular_graph(3, n,
                                                                   seed=seed)))
        rows.append((n, float(np.mean(widths))))
    return all(value > 0 for _, value in rows), rows


def orbit_entropy_calibration() -> tuple[bool, list[tuple[int, float, float]]]:
    rng = np.random.default_rng(409)
    rows_out = []
    for n in (7, 8, 9):
        values = []
        for _ in range(5):
            graph = nx.gnp_random_graph(n, 0.5,
                                        seed=int(rng.integers(0, 2**31 - 1)))
            size = len(lc_orbit(graph_rows(graph)))
            values.append(math.log2(size) / n)
        rows_out.append((n, float(np.mean(values)), float(max(values))))
    return all(0 < mean <= math.log2(3) + 1e-12
               for _, mean, _ in rows_out), rows_out


def main() -> None:
    matrix_ok = matrix_calibration()
    distance_mean_ok = distance_mean_identity_check()
    lc_ok, lc_rows = labelled_cutrank_lc_check()
    atlas_ok, atlas_count = positive_tail_atlas_check()
    rank_one_ok, rank_one_profile = rank_one_counterexample_check()
    forest_ok, forest_count, max_root = forest_shape_checks()
    controls_ok, ulc_profile, root_profile = forest_negative_controls()
    extremal_ok, extremal_count = tree_extremal_checks()
    collision_ok, z_terms = tree_collision_check()
    cubic_ok, cubic_rows = cubic_width_calibration()
    orbit_ok, orbit_rows = orbit_entropy_calibration()

    print("Conjectures 395--396: finite-field rank calibration")
    print(f"  rectangular rank count: {'PASS' if matrix_ok else 'FAIL'}")
    print("Conjecture 397: graph-state distance mean identity")
    print(f"  exact identity through n=20: {'PASS' if distance_mean_ok else 'FAIL'}")
    print("Conjecture 398: labelled cut-rank fibres versus LC orbits")
    for n, orbits in lc_rows:
        print(f"  n={n}: {orbits} fibres/orbits")
    print(f"  exact partition check: {'PASS' if lc_ok else 'FAIL'}")
    print("Conjecture 399: positive-rank-tail log-concavity")
    print(f"  nonempty graph-atlas graphs checked: {atlas_count}")
    print(f"  result: {'PASS' if atlas_ok else 'FAIL'}")
    print(f"  rank-one counterexample profile: {rank_one_profile}")
    print(f"  sharp-boundary certificate: {'PASS' if rank_one_ok else 'FAIL'}")
    print("Conjectures 400--401: forest shape laws")
    print(f"  unlabelled trees through order 12: {forest_count}")
    print(f"  largest computed root real part: {max_root:.6g}")
    print(f"  log-concavity/Hurwitz checks: {'PASS' if forest_ok else 'FAIL'}")
    print(f"  ULC counterexample profile: {ulc_profile}")
    print(f"  non-real-root control profile: {root_profile}")
    print(f"  negative controls: {'PASS' if controls_ok else 'FAIL'}")
    print("Conjectures 402--403: coefficientwise tree extremality")
    print(f"  unlabelled trees through order 11: {extremal_count}")
    print(f"  result: {'PASS' if extremal_ok else 'FAIL'}")
    print("Conjecture 404: exact order-15 reconstruction collision")
    print(f"  equal nonzero Z-terms: {z_terms}")
    print(f"  collision check: {'PASS' if collision_ok else 'FAIL'}")
    print("Conjecture 405: small cubic rank-width calibration")
    for n, mean in cubic_rows:
        print(f"  n={n}: mean exact rank-width {mean:.3f}")
    print(f"  calibration: {'PASS' if cubic_ok else 'FAIL'}")
    print("Conjecture 408: seeded LC-orbit entropy calibration")
    for n, mean, maximum in orbit_rows:
        print(f"  n={n}: mean={mean:.3f}, max={maximum:.3f}")
    print(f"  universal-bound calibration: {'PASS' if orbit_ok else 'FAIL'}")
    print("Scope: finite falsification checks only; no asymptotic law is proved.")

    if not all((matrix_ok, distance_mean_ok, lc_ok, atlas_ok, rank_one_ok,
                forest_ok, controls_ok,
                extremal_ok, collision_ok, cubic_ok, orbit_ok)):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
