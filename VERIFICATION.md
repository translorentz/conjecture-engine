# Independent verification: novelty audit + adversarial testing

Three independent layers were run against the 25 conjectures after the
primary verification suite:

1. **Novelty audit** — five search agents combed OEIS, arXiv, MathWorld,
   PrimePages and the literature for prior art, one batch of five
   conjectures each.
2. **Adversarial battery** (`adversarial/battery.py`) — scripted refutation
   attempts pushing every falsifiable-by-instance conjecture a decade or
   more past its original bound (exception hunts in (10^8, 10^9], the
   statistical laws re-tested at 4·10^9, uniformity stressed at 3x the
   d-range and 2x the q-range).  Machine-readable outcomes in
   `results/adversarial.json`.
3. **Clean-context adversarial agents** — five independent agents (Opus),
   given only the bare statements and told to refute them with their own
   code.  All five were killed mid-run by a session usage limit, but their
   working artifacts (independent sieves, constants, exception lists)
   survive and are summarized below where they reached conclusions.

## Headline outcomes

* **C13 was REFUTED as originally stated — by our own battery.** Every
  exception it found in (10^8, 10^9] is a perfect cube: n = k^3 escapes
  only through n − (k−1)^3, since n − j^3 factors as
  (k−j)(k^2+kj+j^2), so k^3 is representable iff 3k^2−3k+1 is prime.
  The exception set is therefore infinite (~x^{1/3}).  The conjecture was
  restated for non-cube n (memo C13), the cube criterion is now
  machine-checked as a theorem in-range, and the cube lane yields a fresh
  Bateman–Horn instance.  The original overreach and its correction are
  kept on record.
* **One memo claim was falsified by the novelty audit**: C14's ten-term
  exception list for p + 2k^2 (k ≥ 1) is OEIS A060003 verbatim, and 1493
  is the well-known largest Stern prime — the memo's novelty note said
  otherwise and has been corrected.
* **No other conjecture was refuted** by any layer.

## Novelty verdicts

(a) = previously stated essentially verbatim; (b) = classical family, this
quantified instance apparently unstated; no (c)/(d) verdicts occurred.

| # | Verdict | Prior art found |
|---|---|---|
| C01 | (a) | OEIS A080149 (with Cloitre's c≈2.9 asymptotic); Carella arXiv:1710.07827 (unrefereed) has the BH form |
| C02 | (b) | A067200/A144953 bare sequences; constant unpublished |
| C03 | (a) | A174734; for p ≥ 5 this is Chernick's Carmichael triple (6m+1)(12m+1)(18m+1): Dubner, J. Integer Seq. 5 (2002) quantifies it |
| C04 | (b) | A078946 (consecutive-primes variant) bare; constant unpublished |
| C05 | (b) | no OEIS entry, no literature trace found — the cleanest instance-novelty in the suite |
| C06 | (a) | A053182 + **A188596 is literally our constant** (1.5217315...); our 1.52166 ± 4e-4 matches |
| C07 | (b) | A062326 bare sequence; constant 3.3832 unpublished |
| C08 | (b) | no OEIS entry, no constant found |
| C09 | (a) | Grantham–Granville arXiv:2307.07894 (Lucas-sequence e^γ log-count heuristics); Wagstaff's Mersenne analogue |
| C10 | (a) | Caldwell–Gallot, Math. Comp. 71 (2002): e^γ log N for p#±1 |
| C11 | (b) | A064539 has the sequence and the n ≡ 3 (mod 6) note; the κ-quantified count is unstated |
| C12 | (a) | Caldwell–Gallot 2002, verbatim for n!±1 |
| C13 | (a)-core | finiteness for non-cubes is Hardy–Littlewood (Partitio Numerorum III, E_3(X) = O(1)); our census + decay quantification unstated; **as first stated, false — see above** |
| C14 | (a) | OEIS A060003 verbatim (k ≥ 1, ten terms); Stern primes A042978 |
| C15 | (a) | Kimball Martin, Exp. Math. 31 (2022), arXiv:1806.00946: the (3,3) mod-4 lane, incl. exceptionless threshold |
| C16 | (a)-core | uniform HL-B is standard (Goldston–Ledoan); Brent 1975, Korevaar–te Riele 2010 did profile verifications; our fixed-x Gaussian z-profile packaging is new |
| C17 | (a) | **Dubner's conjecture (2000)**; A007534, verified by Dubner to ~2·10^10 |
| C18 | (a) | Kourbatov arXiv:1309.4053 etc.: same constant 1/(2C2) ≈ 0.76, richer corrections, larger tables |
| C19 | (b) | Shanks/Wolf/Nicely endorse limit slope 1; our Granville-corrected 0.9436 appears unstated — a genuinely different constant on the books |
| C20 | (b) | constant γ+log 2π−1 is Montgomery–Soundararajan (mesoscopic); the microscopic finite-x Var/mean law + test appears unstated |
| C21 | (b) | no prior twin-race-mod-5 statement or q²−2 mechanism found (closest: arXiv:2111.09053; Brent's "twins more random") |
| C22 | (b) | Exp(1) limit is Haddad–Leung–Sabuncu arXiv:2408.11781; Wagstaff 1979/Fiori 2404.02329 for the max; the 1/log q deficit law and ordering anomaly appear unstated |
| C23 | (a) | Crandall–Dilcher–Pomerance 1997; Dorais–Klyve 2011 (incl. tail-uniformity census) |
| C24 | (a) | Hardy–Littlewood Conjecture F (1923); Fung–Williams 1990, Jacobson–Williams 2003 run the same constants-predict-density program |
| C25 | (a) | Lemke Oliver–Soundararajan arXiv:1603.03720 (as credited in the memo from the start) |

Net: 10 of 25 carry instance-level novelty (C02, C04, C05, C07, C08, C11,
C19, C20, C21, C22), with C05, C08, C19, C20, C21, C22 the strongest
claims to new content; 15 are re-derivations/verifications of statements
already on the record — which the criteria document counts as a feature
(family membership) but which we now attribute explicitly.

## Adversarial battery outcomes (results/adversarial.json)

| Target | Test | Outcome |
|---|---|---|
| C13 | exception census (10^8, 10^9] | **REFUTED as stated** — 412 new exceptions, all cubes; conjecture restated |
| C14 | hunt for an 11th exception to 10^9 | none — 5993 stands a decade past the original bound |
| C15 | hunt for a (3,3)-lane Goldbach failure to 10^9 | none |
| C17 | hunt for a 36th Dubner exception to 10^9 | none (independently re-verified by a dead agent's sumset code — same 35-element list) |
| C16 | uniformity at d ≤ 6000, x = 10^8 | holds; max |z| = 2.01 over 3000 values of d |
| C18 | records to 4·10^9 | new record gap 5292 after twin 2,466,641,069; G/log³x = 0.49, order intact |
| C19 | first occurrences to 4·10^9 | slope 1.307 → 1.297, falling as required; 11 of 12 previously-missing gaps filled |
| C20 | variance law at 4·10^9 | Var/mean = 0.7998 vs predicted 0.7960 (λ=1); 0.7670 vs 0.7646 (λ=2) |
| C21 | race to 4·10^9 | D1 = −2196 vs noise 2444: no persistent leader, exactly as conjectured (bias/noise ~ 1/log x) |
| C22 | mean U at q ∈ (3000, 6000] | 0.7707 → 0.7758: recovery toward 1 continues; θ ≈ 1.92 |
| C25 | ĉ at 4·10^9 | ĉ = 0.3703 (from 0.3752 at 10^9): slow drift, consistent with o(1) term; symmetry 0.99989 |
| C04 | count at 4·10^9 | obs 15236 vs pred 15230.3 — ratio 1.0004, z = +0.05 |

## Salvaged clean-agent evidence (agents killed by session limits)

* **C06/C07/C08**: independent singular-series computation with primes to
  10^9 gave 1.521730 / 3.383227 / 10.647706 (ours: 1.52166 / 3.38322 /
  10.64599, each within stated truncation wobble; C06 agrees with OEIS
  A188596 to 6 digits).  Independent presieve+MR counts to 3·10^7:
  final ratios 0.9962 / 0.9965 / 1.0059, all |z| < 1.6.  (The agent first
  got z ≈ −22 from a bug in its own sieve — every prime n ≤ Q was killed
  by its own modulus — diagnosed and fixed by the agent itself; the
  corrected run agrees with ours.)
* **C09**: independent fast-doubling + BPSW scan reproduced exactly our 25
  Fibonacci prime exponents ≤ 10^4 and the persistent ~27% deficit against
  e^γ/log φ (z ≈ −1.5 at every scale — consistent with Grantham–Granville's
  warning that the naive constant needs O(1) corrections).
* **C11**: independent congruence sweep to n = 3000: zero primes off the
  n ≡ 3 (mod 6) lane, hits {3,9,15,21,33,2007,2127} as ours.
* **C12**: independent scan to n = 500: 15 hits, z ≤ +1.2 against e^γ log N.
* **C17**: independent sumset algorithm to 10^9: identical 35 exceptions.
* **C19**: independent first-occurrence table to 10^9 matches ours
  (e.g. p(282) = 436,273,009).
* **C23**: KS at x = 10^5, 10^6, 10^7, 10^8: √N·KS = 0.82, 0.82, 0.52,
  0.63 — bounded with no drift (square-root discrepancy confirmed at four
  scales); Wieferich = {1093, 3511} at 10^8; small-quotient census
  K=100: 169 obs vs 161.2 model, K=1000: 1133 vs 1143.9.
* **C24**: independent two-method constants (Euler product vs direct)
  agree to 4-5 digits; spot ratios at N = 10^6 within 0.3% of 1.
* **C22**: independent per-q statistics for q ≤ 300 reproduce the mean-U
  anomaly (0.71–0.82, fraction of classes with U < 1 ≈ 0.73).

## What remains open / flagged

* C09's constant: data sit ~27% below e^γ/log φ at two independent scans;
  the memo's humility clause is now a quantified flag — the mod-5
  divisor-structure correction is the suite's most concrete "needs a
  Granville patch" candidate.
* C25's ĉ drifts slowly (0.40 → 0.37 over three decades): the leading-order
  form survives, but a secondary term is visible; the constant should be
  treated as ĉ(∞) ∈ [0.30, 0.40] until the LOS secondary terms are put in.
* C22's θ is measured (≈1.9 and slowly rising at q ~ 6000), not derived —
  the deepest unexplained number produced by the suite.

## Twin-citation gate (bibliography certification)

Protocol: two independent Opus verifiers must unanimously agree every
reference (1) exists, (2) has correct authors, titles, venue data and
DOI; any flag fails the gate, references are remediated, and the gate is
re-run with a FRESH pair until a unanimous pass is obtained on the final
text.

* **Round 1** (verifiers A, B — 27 entries): both independently found the
  same three failures — HLS author initials (corrected to T. Haddad,
  S.-K. Leung, C. Sabuncu), PairBias missing author (W. Puszkarz), Fiori
  paraphrased title (replaced by arXiv's literal metadata, typo marked
  [sic]).  A additionally could not verify Dubner2000's page range; B
  confirmed it via the OEIS-hosted article.  Remediation: 3 fixes, 2
  cosmetic title normalizations, DOIs added to every entry possessing one.
* **Round 2** (fresh verifiers C, D): zero FAILs; both independently
  flagged only Dubner2000's page range as unverifiable (non-indexed
  journal).  Remediation: unverifiable pages dropped, leaving only
  fields positively confirmed by prior verifiers.
* **Round 3** (fresh verifiers E, F): **27/27 PASS from both, zero FAIL,
  zero UNVERIFIED — gate passed unanimously on the final text.**

The gated bibliography (27 entries, 20 with DOIs verified to resolve to
the exact works, 5 verified to legitimately lack DOIs, plus 2 arXiv
companion pointers) is identical in `paper/conjectures.tex` and the
provenance-stripped `paper/conjectures_blind.tex`.
