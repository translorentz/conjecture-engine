# Referee Report: "Twenty-five conjectures from a local–global random model"

*Independent clean-context referee (Claude Fable 5); reviewed the paper
source only — no repository memos, code, or results consulted. All
computations were the referee's own, run from the bare statements.
Committed verbatim; the authors' actions are in `RESPONSE_TO_REFEREE.md`.*

---

## PART 1 — ORIGINALITY / NOVELTY

I spot-checked 14 of the 25 statements against the literature (2–3 searches each for routine items; 4–5 searches each for the six claimed-most-novel: C5, C8, C19, C20, C21, C22). Every bibliography entry I checked is real (Grantham–Granville arXiv:2307.07894; Martin arXiv:1806.00946, Exp. Math. 31 (2022); Haddad–Leung–Sabuncu arXiv:2408.11781; Kourbatov 1301.2242/1309.4053; Montgomery–Soundararajan CMP 252; Lemke Oliver–Soundararajan; Caldwell–Gallot; CDP; Jacobson–Williams; Wagstaff; Shanks; Gallagher). No fabricated references detected. OEIS attributions checked where reachable (A188596, A060003, A064539, A007534, A001605, A080149-by-context) are correct.

**Hard-target findings:**

- **C5 (pair n²+n+1, n²+n+7), label (b) "no prior trace":** 3 searches (polynomial pair, OEIS, Bateman–Horn quadratic pairs) found nothing. Label **credible**.
- **C8 (triple n²+1, n²+3, n²+7), label (b):** 4 searches. The *pair* (n²+1, n²+3) is known (A080149, "twin quadratic primes" problem literature — correctly credited in C1); the triple has no trace. Label **credible**.
- **C19 (first-occurrence gaps, sqrt(e^γ/2)), label (b):** 4 searches. Prior art: Shanks 1964 (limit 1, cited), Wolf's refinement p(g) ~ √g·e^√g (limit still 1 — **uncited**), Kourbatov–Wolf JIS 23 (2020) / arXiv:2002.02115 (first occurrences in residue classes, p ≈ √d·exp(√(d/φ(q))), constant 1). No prior statement of the competing constant sqrt(e^γ/2) found. Label **credible**; but cite Wolf and Kourbatov–Wolf 2020 as the competing prior conjectures.
- **C20 (finite-x variance law), label (b):** 4 searches. The statement is an essentially mechanical transcription of Montgomery's ∑_{d≤h}𝔖(d)(h−d) second-order term (which the paper credits) into Gallagher's regime. More importantly, **prior art missed**: Sanchis-Lozano, arXiv:1804.07659, is a numerical/heuristic study at x ~ 10^8 fitting exactly this normalized-variance shape w = 1 − b(h)/log N in support of Montgomery–Soundararajan. The abstract's billing of C20 as one of the four "most notably" new results **oversells**; the instance-packaging is at best marginally novel. **Attribution issue.**
- **C21 (twin race mod 5), label (b) "apparently new":** 5 searches. The quantified mod-5 statement with the (q²−2, q²) mechanism and the C7 constant appears genuinely new. However, the *family* — Chebyshev-type races/biases for twin primes in residue classes — has uncited prior art: Sahoo, arXiv:2111.09053 (twin-prime biases incl. the mod-4 race, where twins lean opposite to primes), and arXiv:1807.00406 (statistical bias in prime pairs). "Apparently new" should be narrowed to the quantified mod-5 instance. **Minor attribution issue.**
- **C22 (least primes in progressions), label (b), part (i) cf. HLS:** 4 searches. Part (i)'s Exp(1) limit is prior art (stated as known in the cited HLS paper itself); the Gumbel form is a routine order-statistics corollary of (i); Fiori arXiv:2404.02329 (2024) updates Wagstaff's numerics and is uncited. Part (ii)'s measured θ(q)/log q deficit: no prior trace found; **credible** and, I agree, the most interesting new number here. Label (b) is fair for (ii), but (i) is (a)-grade and should be labeled so.

**Routine spot-checks (labels confirmed):** C1 (A080149 ✓), C3 (Dubner 2002 tabulated Chernick counts ✓), C6 (A188596 = 1.5217315... ✓, paper transparent), C9 (Grantham–Granville really do conjecture c·log N for Fibonacci primes ✓), C15 (Martin's Exp. Math. paper covers exactly this refinement family ✓), C14/C17 (classical, correctly credited).

**Attribution section overall:** honest in structure and unusually candid (records its own refuted conjecture). Fair to the literature on the 15 (a)-items. Gaps: Sanchis-Lozano (C20), Sahoo / twin-bias literature (C21), Wolf's first-occurrence law (C19), Fiori (C22), Cohen's high-precision Hardy–Littlewood constants (C24, see below). The claim "C21 and C22(ii) are the most genuinely new" — I concur after searching.

---

## PART 2 — DISPROOF ATTEMPTS

### (i) Congruence/admissibility claims — all verified by script, none refuted

- **C21:** 3 | q²+2 for all primes 3 < q < 10^5 ✓ (trivial: q² ≡ 1 mod 3). (q²−2) mod 5 ∈ {2,4}, never 1, for all primes q ≠ 5 below 10^5 ✓. Twin starts >5 lie in {1,2,4} mod 5 ✓. Wording bug: a "twin pattern containing a prime square" is not a twin-*prime* pattern (q² is composite); the intended Chebyshev-bias mechanism (prime-power pairs in the weighted count) should be stated explicitly.
- **C11:** n even ⇒ value even; n odd, 3∤n ⇒ 3 | n²+2^n (since 2^n ≡ −1). So primality forces n ≡ 3 (mod 6) — proved, and verified: only hits in [2,400] are {3,9,15,21,33}, all ≡ 3 (6); n = 2007 and 2127 hits reconfirmed by Miller–Rabin (605-digit numbers). Note OEIS A064539 already records the mod-6 constraint; only κ is new.
- **Theorem 1:** the factorization proof is correct; verified as an iff for all k ≤ 215 (139 non-representable cubes below 10^7 = exactly the k with 3k²−3k+1 composite). **Gap:** the corollary "the set of integers not representable as p+k³ ... of counting function ∼ x^{1/3}" is **not a theorem as stated**: unconditionally one gets infinitude and the lower bound ~x^{1/3} (composite values of 3k²−3k+1 have density 1 by a standard sieve bound), but the asymptotic *equality* for the full non-representable set assumes the non-cube exceptional set is o(x^{1/3}) — i.e., assumes Conjecture 13(i). The theorem should claim ~x^{1/3} for the *cube* part only.
- **C15:** parity claim correct (p+q ≡ 2 mod 4 with p,q odd forces p ≡ q mod 4); no (3,3)-exception for any n ≡ 2 (4), 6 ≤ n ≤ 10^6 ✓.
- **C4 quintuplet (0,2,6,12,14):** admissible — ω(p) = 1,2,4,4,5,5 at p = 2,3,5,7,11,13, all < p ✓; realized at n = 5 (5,7,11,17,19) ✓.

### (ii) Constants recomputed independently (9 of them + 2 derived)

| Constant | Paper | Referee (cutoff 2·10^6) | Verdict |
|---|---|---|---|
| C1 | 2.954014 | 2.954014 | match |
| C2* | 1.298435 | 1.298435 | match |
| C3 | 2.858249 | 2.858249 | match |
| C4 | 15.19770 | 15.197697 | match |
| C5 | 5.928477 | 5.928477 | match |
| C7 | 3.383216 | 3.383216 | match (but see below) |
| C8 | 10.64599 | 10.645985 | match |
| κ (C11) | 4.2734 | 4.2733 (p ≤ 3000) | match |
| γ+log2π−1 | 1.41509 | 1.415093 | match |
| **sqrt(e^γ/2)** (C19) | **0.94358** | **0.943682** | **wrong 4th decimal** |
| **1/(2C₂)** (C18) | **0.75735** | **0.757390** | **wrong 5th digit** |
| **C(41)** (C24) | **6.64092** | 6.640922 @2·10^5 → 6.640512 @2·10^6 → 6.639726 @3.2·10^7 | **truncation artifact** |

The C(41) case is diagnostic: the paper's 6.64092 is *exactly* the partial product at cutoff 2·10^5 (not the claimed 2·10^6), and the true value is Cohen's high-precision **6.6395463...** — the paper's 4th significant decimal is wrong by 1.4·10^-3. The conditionally convergent constants (C1, C5, C6, C7, C8, C24 family) are all quoted to 7 digits with genuine accuracy of only ~10^-4–10^-3 (my C7 still moves at the 5th decimal between cutoffs 2·10^6 and 3.2·10^7). Not fatal to any conjecture (with the true C(41), the paper's A=41 verification becomes z ≈ +0.12 instead of +0.02), but precision is systematically overstated.

### (iii) Independent numerical sanity tests (11 conjectures re-tested with the referee's own code)

- **C5:** count to 10^6: obs 9295 vs C5·I = 9257.1, z = +0.39 ✓.
- **C14:** exhaustive to 10^5: exceptions exactly {1, 3, 17, 137, 227, 977, 1187, 1493, 5777, 5993} ✓.
- **C20 at x = 10^8** (5.4·10^5 windows): Var/E = 0.7694 vs predicted 0.7650 (λ=1); 0.7306 vs 0.7274 (λ=2). Naive Poisson (ratio 1) refuted by 23%; residual +0.004 of the anticipated O(1/log²x) size ✓.
- **C4:** decade counts at 1.2·10^8: z = −0.79 on [10^6,10^7), z = +0.19 on [10^7,10^8); confirms both the constant and the "phantom mass below 10^5" caveat ✓.
- **C21 at 10^8:** classes (1,2,4) = (172474, 172754, 172130); D₁ = +32 vs systematic prediction +48, noise 719 ✓ consistent.
- **C25:** ĉ = 0.404 (10^7), 0.387 (10^8) vs paper's 0.400, 0.375-at-10^9 — consistent drift ✓; #(1,1)/#(2,2) = 0.99967 at 10^8 ✓.
- **C16 at 10^7,** all 1000 even d ≤ 2000: corr 0.999991, slope 0.998, max|z| = 2.07 ✓. (Observed sd(z) ≈ 0.5 with mean −0.46 at this height — the "mean-zero, unit-order" description is loose at smaller x; secondary terms visible.)
- **C17:** exhaustive to 10^7: 34 exceptions ≥ 4, largest 4208; with n = 2 this is A007534's 35 ✓.
- **C13:** exhaustive to 10^7: non-cube exceptions per decade [4, 27, 168, 763, 2011, 2808, 1181] — decaying past 10^6 ✓; 78,526,384 confirmed non-cube and non-representable ✓.
- **C22:** mean U = 0.751 / 0.783 / 0.795 at q = 211 / 1009 / 2999 — deficit and recovery confirmed ✓.
- **C23 to 3·10^5:** √n·KS = 1.02 (bounded ✓); census K=100: 132 vs 123.3 ✓; Wieferich = {1093, 3511} ✓. **C10:** exactly 11 primorial primes p ≤ 4000 ✓ vs predicted 14.8.

### (iv) Logical-gap hunt

- No covering-congruence or algebraic-identity refutation found for any of the 25. The engine's own admissibility discipline (e.g., rejecting n²+n+3 at p=3) checks out.
- **Theorem 1 corollary** is the one real logical overreach (see (i)).
- **C19** is bolder than advertised: limit sqrt(e^γ/2) implies the CSG ratio g/log²p(g) → 2e^{-γ} ≈ 1.123 for *all* large g (a liminf statement), strictly stronger than Granville's limsup, and contradicting Firoozbakht-type bounds that current numerics support (slope 1.30 at 4·10^9 is still 38% above the claimed limit). Legitimate as a registered competing constant, but the text should state this tension.
- **C9 data nit:** "25 Fibonacci prime indices ≤ 10^4" counts index 4 (F₄ = 3), which is not prime; the conjecture's count over primes p is **24**. This slightly *deepens* the deficit the paper already flags (z ≈ −1.7, not −1.6). *(Authors' note: rebutted with evidence — see RESPONSE_TO_REFEREE.md; the hit list contains only prime indices.)*
- **C22(i)** conflates a limit theorem-shape with a heuristic; fine as conjecture, but part (i) is not novel.

---

## VERDICT

| # | Verdict |
|---|---|
| C1 | SOUND |
| C2 | SOUND |
| C3 | SOUND |
| C4 | SOUND |
| C5 | SOUND (novelty label credible) |
| C6 | SOUND |
| C7 | SOUND (precision overstated: 5th decimal still drifting at cutoff 3·10^7) |
| C8 | SOUND (novelty label credible) |
| C9 | SOUND-BUT: count should be 24, not 25; constant already self-flagged as suspect |
| C10 | SOUND (verified exactly) |
| C11 | SOUND (mod-6 congruence is in OEIS; novelty = κ only) |
| C12 | SOUND |
| Thm 1 | SUSPECT-MATH (proof of the iff correct; the "∼ x^{1/3}" corollary for the full exceptional set is conditional on C13(i), not a theorem) |
| C13 | SOUND |
| C14 | SOUND (reproduced exactly) |
| C15 | SOUND (parity claim verified) |
| C16 | SOUND |
| C17 | SOUND (reproduced exactly) |
| C18 | SOUND-BUT: 1/(2C₂) = 0.757390, not 0.75735 |
| C19 | SOUND-BUT: sqrt(e^γ/2) = 0.943682, not 0.94358; cite Wolf/Kourbatov–Wolf; state the Firoozbakht tension |
| C20 | SOUND-BUT-ATTRIBUTION-ISSUE: verified at 10^8, but it is an MS corollary with uncited numerical precedent (Sanchis-Lozano arXiv:1804.07659); demote from "most notable" |
| C21 | SOUND (all congruences verified; quantified instance appears new; cite twin-race prior art: Sahoo arXiv:2111.09053, arXiv:1807.00406; fix "prime square" wording) |
| C22 | SOUND (part (i) is prior art and should be (a); part (ii) novelty credible and verified) |
| C23 | SOUND |
| C24 | SOUND-BUT: C(41) = 6.64092 is a truncation artifact (true value 6.6395463, Cohen); cite Cohen's high-precision computations |
| C25 | SOUND (reproduced) |

**No conjecture refuted.** Every checkable identity, congruence, exception list, and admissibility claim I tested is correct; 9 constants reproduce; 11 conjectures re-verified numerically with independent code.

## RECOMMENDATION: MINOR REVISION

1. **Fix the three numerical errors and add error bars.** C(41) → 6.639546 (and recheck every conditionally convergent constant against a larger cutoff or Cohen-style acceleration; state truncation uncertainty per constant); 0.94358 → 0.943682 (C19); 0.75735 → 0.757390 (C18). Also 25 → 24 in Remark 2 (C9).
2. **Restate Theorem 1's corollary.** Unconditional content: the non-representable *cubes* have counting function ∼ x^{1/3}; the asymptotic for the full exceptional set is conditional on C13(i). As printed, a conjecture is smuggled into a theorem.
3. **Repair attribution for the novelty flagships.** Cite Sanchis-Lozano (arXiv:1804.07659) at C20 and soften the abstract's claim for it; cite Sahoo (arXiv:2111.09053) and arXiv:1807.00406 at C21; cite Wolf's p(g) ∼ √g·e^√g and Kourbatov–Wolf (2020) at C19, and note C19's implied liminf-CSG = 2e^{-γ} conflicts with Firoozbakht-supported numerics; relabel C22(i) as (a) (exponential limit is stated as known in the cited HLS paper; also cite Fiori arXiv:2404.02329).
