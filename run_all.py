"""Run the full verification suite with production bounds, then rebuild
RESULTS.md.  Individual scripts can be run standalone with custom bounds."""
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))

JOBS = [
    # main statements (v6 roster)
    ("c01_quadratic_depolignac_family.py", ["1e6", "300"]),
    ("c01b_family_moments.py", ["1e5", "300"]),
    ("c01_quadratic_twin_pair.py", ["1e7"]),          # d = 2 instance
    ("c02_cubic_shift.py", ["1e7"]),
    ("c02b_cubic_family.py", ["1e5", "300", "60", "2e5"]),
    ("c03_prime_ap_chain.py", ["3e8"]),
    ("c03b_triplet_race.py", ["1e9"]),
    ("c04_power_ladder.py", ["1e8", "1e6", "8e5"]),
    ("c05_cyclotomic_twin_family.py", ["1e7"]),
    ("c06_repunit_chain.py", ["1e7"]),
    ("c07_psquared_minus2.py", ["1e7"]),
    ("c07b_sexy_matrix.py", ["1e9"]),
    ("c08_null_race.py", ["1e7"]),
    ("c09_fibonacci_primes.py", ["1e4"]),
    ("c09b_fib_lucas_twins.py", ["10000"]),
    ("c10_factorial_twins.py", ["700"]),
    ("c11_n2_plus_2n.py", ["4200"]),
    ("c11b_crt_kappa.py", ["6000"]),
    ("c12_factorial_primes.py", ["700"]),
    ("c12b_pair_ms.py", ["3000", "20000"]),
    ("c13_prime_plus_cube.py", ["1e8"]),
    ("c13b_boundary.py", ["1e6"]),
    ("c14_stern_2k2.py", ["1e8"]),
    ("c14b_stern_lane_race.py", ["1e8", "2500"]),
    ("c15_goldbach_mod4.py", ["1e8"]),
    ("c15b_least_goldbach.py", ["1e8", "2000"]),
    ("c16_uniform_depolignac.py", ["1e8", "2000"]),
    ("c16b_covariance_kernel.py", ["1e8", "60"]),
    ("c16c_window_field.py", ["1e8", "1e5", "2000", "40"]),
    ("c17_twin_goldbach.py", ["1e8"]),
    ("c17b_twin_member_goldbach.py", ["1e8", "150", "30000"]),
    ("c18_twin_gap_records.py", ["1e9"]),
    ("c18b_race_max.py", ["1e9"]),
    ("c19_gap_first_occurrence.py", ["1e9"]),
    ("c19b_waiting_refinement.py", ["1e9", "60", "500"]),
    ("c20_poisson_intervals.py", ["1e9", "2e8"]),
    ("c21_twin_race_mod5.py", ["1e9"]),
    ("c21b_twin_race_mod8.py", ["1e9"]),
    ("c21c_cousin_races.py", ["1e9"]),
    ("c22_least_prime_ap.py", ["3000", "5e6"]),
    ("c22b_stratified.py", ["2e7"]),
    ("c22c_injective_baseline.py", ["400"]),
    ("c23_fermat_quotients.py", ["1e7", "1e8"]),
    ("c23b_multibase.py", ["1e7", "100"]),
    ("c24_hl_family_F.py", ["1e6", "199"]),
    ("c24b_family_kernel.py", ["1e6", "99"]),
    ("c25_goldbach_lane_race.py", ["1e8", "500"]),
    ("c25b_weighted_drift.py", ["1e8", "400"]),
    # retained calibration benchmarks (retired slot occupants)
    ("c05_twin_cyclotomic.py", ["1e7"]),
    ("c06_cyclotomic_germain.py", ["1e7"]),
    ("c08_quadratic_triple.py", ["1e7"]),
    ("c10_primorial_twins.py", ["4000"]),
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
