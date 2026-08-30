#!/usr/bin/env python3
"""Exact and seeded checks for the calibration behind Conjecture 394.

The conjecture concerns Floer barcode entropy for a noncommuting random
Hamiltonian cocycle, which this script cannot compute.  It instead verifies
the exact combinatorial step in Proposition ar:basic for the in-model lazy
walk mu=(1-p)delta_id+p delta_phi: every deterministic iterate through the
current endpoint occurs among the prefixes.  A seeded Bernoulli experiment
then checks the only probabilistic input, S_n/n -> p.

This is deliberately not an SL(2,Z) proxy and makes no LQG claim.
"""

from __future__ import annotations

import itertools
import math
import random


def exhaustive_prefix_check(max_n: int = 16) -> tuple[bool, int]:
    """Check every zero-one word through max_n for the no-skipped-iterate law."""
    checked = 0
    for n in range(max_n + 1):
        for word in itertools.product((0, 1), repeat=n):
            counts = [0]
            for step in word:
                counts.append(counts[-1] + step)
            if set(counts) != set(range(counts[-1] + 1)):
                return False, checked
            checked += 1
    return True, checked


def bernoulli_rate_check(
    p: float = 0.37, n: int = 200_000, samples: int = 24, seed: int = 394
) -> tuple[bool, float, float]:
    """Seeded strong-law calibration with a conservative finite tolerance."""
    rng = random.Random(seed)
    rates = []
    for _ in range(samples):
        total = sum(rng.random() < p for _ in range(n))
        rates.append(total / n)
    max_error = max(abs(rate - p) for rate in rates)
    rms_error = math.sqrt(sum((rate - p) ** 2 for rate in rates) / samples)
    # About six binomial standard deviations; intended to catch coding errors,
    # not to serve as evidence for the strong law.
    tolerance = 6.0 * math.sqrt(p * (1.0 - p) / n)
    return max_error < tolerance, max_error, rms_error


def main() -> None:
    prefix_ok, words = exhaustive_prefix_check()
    rate_ok, max_error, rms_error = bernoulli_rate_check()

    print("Conjecture 394: lazy Hamiltonian-walk calibration")
    print(f"  zero-one words checked through length 16: {words}")
    print(f"  no-skipped-iterate identity: {'PASS' if prefix_ok else 'FAIL'}")
    print(f"  Bernoulli rate maximum error: {max_error:.6f}")
    print(f"  Bernoulli rate RMS error:     {rms_error:.6f}")
    print(f"  seeded S_n/n calibration: {'PASS' if rate_ok else 'FAIL'}")
    print("Scope: exact lazy-walk reduction only; no Floer barcode is computed.")

    if not (prefix_ok and rate_ok):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
