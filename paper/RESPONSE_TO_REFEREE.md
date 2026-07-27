# Response to the referee report

The full report is committed verbatim as `paper/REFEREE_REPORT.md`.
Verdict was MINOR REVISION with no conjecture refuted. Actions taken:

## Fix 1 — numerical errors (all accepted)
* sqrt(e^gamma/2): 0.94358 -> **0.943682** (C19, abstract). Fixed.
* 1/(2C2): 0.75735 -> **0.757390** (C18). Fixed.
* C(41): replaced our truncated 6.64092 with **Cohen's 6.6395463**, cited;
  the A=41 verification line updated to pred 261,017.6, z = +0.12; a
  paragraph added acknowledging the truncation lesson and stating that
  quoted digits of all conditionally convergent constants are limited by
  the stated wobble. The verifier `c24_hl_family_F.py` cutoff was raised.
* C9 count "25 should be 24": **rebutted with evidence**. Our hit list
  contains only prime indices (machine-checked: 25 entries, all prime,
  index 4 absent; F_3 = 2 is prime so p = 3 legitimately counts). The
  referee likely compared against OEIS A001605, which includes the
  non-prime index 4 (26 terms up to 9677). No change.

## Fix 2 — Theorem 1 corollary (accepted)
Restated: the unconditional content is that the non-representable *cubes*
have counting function ~ x^(1/3); the asymptotic for the full exceptional
set is now explicitly conditional on Conjecture 13(i). The proof's
density-one sentence now cites the Chebyshev-bound reason.

## Fix 3 — attribution (all accepted)
* C20: cited Sanchis-Lozano (arXiv:1804.07659); abstract demotes C20 from
  the flagship list to "sharpened instance with numerical precedent".
* C21: cited Sahoo (arXiv:2111.09053) and arXiv:1807.00406 as twin-bias
  prior art; the "twin patterns containing a prime square" wording was
  replaced with the precise weighted-count formulation.
* C19: cited Wolf / Kourbatov-Wolf (arXiv:2002.02115) as the slope-1
  competitors, and added the referee's observation that our limit implies
  a liminf strengthening of Granville's limsup, in tension with
  Firoozbakht-supported numerics.
* C22: part (i) relabeled (a) with Fiori (arXiv:2404.02329) added; part
  (ii) remains (b).
* C16: added the visible secondary-term caveat (mean z_d ~ -0.3 at 10^8).
