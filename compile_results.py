"""Rebuild RESULTS.md from results/*.json."""
import glob
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

HEAD = """# Verification results

Auto-generated from `results/*.json` (the committed record of the actual
runs).  Regenerate with `python3 compile_results.py` after re-running any
verifier.

"""


def fmt(v):
    if isinstance(v, float):
        return "%.4g" % v
    return str(v)


def table(rows, cols):
    out = ["| " + " | ".join(cols) + " |",
           "|" + "|".join("---" for _ in cols) + "|"]
    for r in rows:
        out.append("| " + " | ".join(fmt(r.get(c, "")) for c in cols) + " |")
    return "\n".join(out)


def main():
    parts = [HEAD]
    for path in sorted(glob.glob(os.path.join(ROOT, "results", "c*.json"))):
        name = os.path.basename(path)[:-5]
        data = json.load(open(path))
        parts.append("## %s — %s\n" % (name.upper(), data.get("conjecture", "")))
        for key in ("constant_C", "constant_wobble", "slope_predicted", "kappa",
                    "model_constant", "second_order_constant", "correlation",
                    "rank_correlation", "slope", "mean_ratio", "sd_ratio",
                    "max_abs_z", "z_mean", "z_sd", "z_max_abs",
                    "largest_exception", "n_exceptions",
                    "slope_measured_g_ge_100", "slope_cramer", "slope_granville",
                    "tail_slope", "gumbel_mean", "gumbel_sd", "gumbel_sd_model",
                    "mean_U_overall", "KS", "sqrt_n_KS", "mean_u",
                    "small_quotient_obs", "small_quotient_pred",
                    "wieferich_expected", "lead_density_D1_positive",
                    "lead_density_D24_positive", "expected_more_in_next_decade"):
            if key in data:
                parts.append("* **%s** = %s" % (key, fmt(data[key])))
        for key in ("first_solutions", "hits", "exceptions", "wieferich",
                    "missing_even_gaps"):
            if key in data:
                v = data[key]
                s = ", ".join(str(x) for x in v[:40])
                if len(v) > 40:
                    s += ", ... (%d total)" % len(v)
                parts.append("* **%s**: %s" % (key, s))
        if "by_digits" in data:
            parts.append("* **exceptions by digit count**: %s" % data["by_digits"])
        for tkey in ("table", "checkpoints", "samples", "rows", "worst",
                     "records", "mean_U_by_band", "bands"):
            if tkey in data and isinstance(data[tkey], list) and data[tkey]:
                rows = data[tkey]
                if isinstance(rows[0], dict):
                    cols = list(rows[0].keys())
                    if tkey == "rows" and len(rows) > 25:
                        rows = rows[::5]
                    parts.append("\n**%s**\n\n%s" % (tkey, table(rows, cols)))
                elif tkey == "records":
                    parts.append("\n**records** (gap, after): %s" %
                                 ", ".join("(%d @ %d)" % (g, p) for g, p in rows[-10:]))
        for k, v in data.items():
            if k.startswith("lambda_") or k in ("final_counts", "counts", "drift"):
                parts.append("* **%s** = %s" % (k, json.dumps(v)))
        parts.append("")
    out = "\n".join(parts)
    with open(os.path.join(ROOT, "RESULTS.md"), "w") as fh:
        fh.write(out)
    print("RESULTS.md written (%d bytes)" % len(out))


if __name__ == "__main__":
    main()
