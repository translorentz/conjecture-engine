"""Run the full verification suite with production bounds, then rebuild
RESULTS.md.  Individual scripts can be run standalone with custom bounds."""
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))

JOBS = [
    ("c01_quadratic_twin_pair.py", ["1e7"]),
    ("c02_cubic_shift.py", ["1e7"]),
    ("c03_prime_ap_chain.py", ["3e8"]),
    ("c04_quintuplet.py", ["1e9"]),
    ("c05_shifted_quadratic_pair.py", ["1e7"]),
    ("c06_cyclotomic_germain.py", ["1e7"]),
    ("c07_psquared_minus2.py", ["1e7"]),
    ("c08_quadratic_triple.py", ["1e7"]),
    ("c09_fibonacci_primes.py", ["1e4"]),
    ("c10_primorial_primes.py", ["4000"]),
    ("c11_n2_plus_2n.py", ["4200"]),
    ("c12_factorial_primes.py", ["700"]),
    ("c13_prime_plus_cube.py", ["1e8"]),
    ("c14_stern_2k2.py", ["1e8"]),
    ("c15_goldbach_mod4.py", ["1e8"]),
    ("c16_uniform_depolignac.py", ["1e8", "2000"]),
    ("c17_twin_goldbach.py", ["1e8"]),
    ("c18_twin_gap_records.py", ["1e9"]),
    ("c19_gap_first_occurrence.py", ["1e9"]),
    ("c20_poisson_intervals.py", ["1e9", "2e8"]),
    ("c21_twin_race_mod5.py", ["1e9"]),
    ("c22_least_prime_ap.py", ["3000", "5e6"]),
    ("c23_fermat_quotients.py", ["1e7", "1e8"]),
    ("c24_hl_family_F.py", ["1e6", "199"]),
    ("c25_consecutive_mod3.py", ["1e9"]),
]


def main():
    t0 = time.time()
    failed = []
    for script, args in JOBS:
        print("\n===== %s %s =====" % (script, " ".join(args)))
        rc = subprocess.call([sys.executable,
                              os.path.join(ROOT, "verify", script)] + args)
        if rc != 0:
            failed.append(script)
    subprocess.call([sys.executable, os.path.join(ROOT, "compile_results.py")])
    print("\nSuite done in %.0fs; failures: %s" % (time.time() - t0, failed or "none"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
