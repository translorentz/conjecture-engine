# The 25 Conjectures

Each entry states the conjecture at the maximum strength the local–global
random model supports, derives its constant, checks local admissibility,
places it in the standard hierarchy (Hardy–Littlewood k-tuples ⊂ Schinzel H
⊂ Bateman–Horn; Cramér/Granville; Borel–Cantelli accounting), and names its
verification script.  Numerical outcomes live in `RESULTS.md` and
`results/*.json`.

Notation: `BH(f1,...,fk)` is the Bateman–Horn singular series
`C = prod_p (1 - omega(p)/p) / (1 - 1/p)^k` with `omega(p) = #{n mod p : p | f1(n)...fk(n)}`;
`I(N)` is the matching main term `int dt / prod_i log f_i(t)`;
`Li_k(x) = int_2^x dt/(log t)^k`; `S(d)` is the twin singular series
`2 C2 prod_{p|d, p>2} (p-1)/(p-2)`, `2 C2 = 1.3203236...`;
`gamma` is Euler's constant, `e^gamma = 1.7810724...`.

---

## C01 — Quadratic twin pairs

**Conjecture.** There are infinitely many n with `n^2+1` and `n^2+3` both
prime; precisely,

    #{n <= N : n^2+1, n^2+3 prime} = C01 * int_2^N dt/(log(t^2+1) log(t^2+3)) * (1+o(1)),

with `C01 = BH(x^2+1, x^2+3)` (computed in `results/c01.json`, truncation
wobble reported).

**Admissibility.** n must be even (else both values even); n ≢ 0 (mod 3)
(else 3 | n^2+3); at every p, `omega(p) <= 4 < p` for p ≥ 5 — the constant
computation *asserts* `omega(p) < p` for every p up to 2·10^6, so the
singular series is provably nonzero over that range and provably convergent.

**Hierarchy.** This is the intersection of two Hardy–Littlewood Conjecture-E
style statements and a special case of Schinzel's Hypothesis H with the
Bateman–Horn quantification.  It implies infinitely many twin pairs of the
form (m+1, m+3) with m a perfect square — a de Polignac refinement.

**Why the negation is costly.** The values n^2+1 and n^2+3 share no
algebraic factor (resultant 4); a failure would mean the primes conspire
against a quadratic sequence in a way no known obstruction (congruence,
size, algebraic factorization) explains.

**Verification.** `verify/c01_quadratic_twin_pair.py` counts to N = 10^7
(values to 10^14, deterministic Miller–Rabin) and compares count, ratio and
Poisson-normalized z at every decade.

---

## C02 — The cubic shift n^3 + 2

**Conjecture.** `#{n <= N : n^3+2 prime} = C02 * int_2^N dt/log(t^3+2) * (1+o(1))`,
`C02 = BH(x^3+2)`.

**Admissibility.** omega(2) = 1 (n even kills it), omega(3) = 1 (n ≡ 1 mod 3
gives 3 | n^3+2); for p ≡ 2 (mod 3) the cube map is a bijection so omega = 1
exactly; for p ≡ 1 (mod 3), omega ∈ {0,3} according as -2 is a cubic residue.
The p ≡ 1 fluctuation makes the singular series converge only conditionally —
the script reports the wobble between cutoffs as an error bar.

**Hierarchy.** Bateman–Horn for a single cubic; the cubic analogue of the
classical `n^2+1` conjecture (Landau's problem quantified by Hardy–Littlewood
Conjecture E).  No cubic case is known to hold; the closest theorem is
Heath-Brown's x^3 + 2y^3 primes — which is exactly the "partial-result
tractability" (criterion 16) neighbor of this statement.

**Verification.** `verify/c02_cubic_shift.py`, N = 10^7 (values to 10^21,
still inside the deterministic Miller–Rabin range).

---

## C03 — The AP chain p, 2p−1, 3p−2

**Conjecture.** There are infinitely many primes p such that p, 2p−1, 3p−2
are all prime — a 3-term arithmetic progression with common difference p−1
whose first term is its own index; quantitatively

    #{p <= x} = C03 * int_2^x dt/(log t * log(2t-1) * log(3t-2)) * (1+o(1)),

`C03 = BH(x, 2x-1, 3x-2)`.  First chain: (3, 5, 7).

**Admissibility.** mod 2: p odd makes all three odd (omega(2)=1); mod 3:
p ≡ 2 kills 2p−1, p ≡ 0 forces p = 3, so omega(3) = 2 < 3; all linear, so
omega(p) <= 3 < p beyond.

**Hierarchy.** A Bateman–Horn system of three linear forms — sibling of
Sophie Germain (p, 2p+1) and of Cunningham chains, but tied to APs: it
produces 3-term prime APs (p, 2p−1, 3p−2) whose common difference p−1 is
determined by the prime itself.

**Verification.** `verify/c03_prime_ap_chain.py`, x = 3·10^8 by direct sieve
to 9·10^8.

---

## C04 — The quintuplet (0, 2, 6, 12, 14)

**Conjecture (Hardy–Littlewood instance).**
`#{n <= x : n, n+2, n+6, n+12, n+14 all prime} = C04 * Li_5(x) * (1+o(1))`,
with C04 the HL constant of the pattern.  (This admissible pattern is
distinct from the two classical diameter-12 quintuplets (0,2,6,8,12) and
(0,4,6,10,12); it has diameter 14 and contains two twin pairs 2 apart plus
a middle prime.)

**Admissibility.** Residues mod 5 are {0,1,2,4} — class 3 is free — so
omega(5) = 4 < 5; smaller primes checked the same way; the tuple is
admissible (asserted programmatically for all p).

**Goldilocks note.** For 5-tuples the counting function converges slowly
(the integral from 2 contains phantom mass where no quintuplet can live);
the verification therefore also reports per-decade *increments*, where the
model must — and does — match without small-x contamination.  This is
criterion III.9 in action: shape of agreement, not raw range.

**Verification.** `verify/c04_quintuplet.py`, segmented sweep to 10^9.

---

## C05 — The shifted pair n^2+n+1, n^2+n+7

**Conjecture.** Infinitely many n make `n^2+n+1` and `n^2+n+7`
simultaneously prime, with counting function `C05 * int dt/(log f1 log f2)`,
`C05 = BH(x^2+x+1, x^2+x+7)`.

**Admissibility.** n^2+n is always even, so both forms are always odd —
no parity loss at all (omega(2) = 0, local factor 4).  mod 3 both forms
vanish only at n ≡ 1; mod 7 the joint omega is 4 < 7.  Note the
near-miss: the "natural" pair (n^2+n+1, n^2+n+3) is *inadmissible* —
3 divides one of them for every n ≢ 1 (mod 3) and the other at n ≡ 1.  The
+7 companion is the nearest admissible relative; the engine rejects the +3
pair automatically (singular series = 0).  This is criterion I.1 doing
real work.

**Verification.** `verify/c05_shifted_quadratic_pair.py`, N = 10^7.

---

## C06 — Cyclotomic Sophie Germain pairs

**Conjecture.** Infinitely many primes p have `Phi_3(p) = p^2+p+1` prime,
with `#{p <= x} = C06 * int_2^x dt/(log t * log(t^2+t+1)) * (1+o(1))`,
`C06 = BH(x, x^2+x+1)`.

**Admissibility.** 3 | p^2+p+1 iff p ≡ 1 (mod 3), so half the primes are
locally barred at 3 — the constant absorbs this.  For q ≡ 1 (mod 3) the
quadratic has two roots (the primitive cube roots of unity), else none.

**Downward fecundity.** If p and q = p^2+p+1 are both prime then
q | p^3 − 1, so ord_q(p) = 3 and the repunit-like integer 111 base p is
prime: these are exactly the primes of the form (p^3−1)/(p−1).  The
conjecture thus quantifies "infinitely many base-p repunit primes of
length 3 with prime base", tying it to the (base-independent!) repunit
family that contains Mersenne primes (base 2).

**Verification.** `verify/c06_cyclotomic_germain.py`, x = 10^7.

---

## C07 — The downward companion p, p^2 − 2

**Conjecture.** Infinitely many primes p have p^2 − 2 prime;
`#{p <= x} = C07 * int_2^x dt/(log t log(t^2-2)) * (1+o(1))`,
`C07 = BH(x, x^2-2)`.

**Admissibility.** p odd makes p^2−2 odd; 3 ∤ p^2−2 always (squares are
0,1 mod 3); for q > 3 the quadratic contributes 1 + legendre(2, q) roots.

**Position in the web.** Beyond Bateman–Horn membership, C07 is the exact
input the twin-race conjecture C21 consumes: the pairs (p^2−2, p^2) are the
only square-contaminated twin patterns mod 3 (see C21), so C07's constant
*is* the bias constant of C21.  Refuting C07 (finitely many p^2−2 primes)
would erase the predicted twin-race bias — the two stand or fall together
(criterion V.15).

**Verification.** `verify/c07_psquared_minus2.py`, x = 10^7.

---

## C08 — The quadratic triple n^2+1, n^2+3, n^2+7

**Conjecture.** Infinitely many n make all of n^2+1, n^2+3, n^2+7 prime;
`#{n <= N} = C08 * int dt/(prod log(t^2+c)) * (1+o(1))`, `C08 = BH` of the
system, c ∈ {1,3,7}.

**Admissibility.** The shift set {1,3,7} must itself be admissible *as a
tuple against the quadratic residues*: mod 7, n^2+7 ≡ n^2 forces n ≢ 0;
n^2+3 forces n ≢ ±2; n^2+1 has no roots mod 7 — total omega(7) = 3 < 7.
(The greedy extension {1,3,7,9} stays admissible but at a price: mod 5 it
forces n ≡ 0 (mod 5), collapsing the candidate set to one lane — the
diameter-7 triple is the natural stopping point before the pattern begins
consuming its own density.)

**Hierarchy.** C08 strictly refines C01 (drop the third form) exactly as
prime quadruplets refine twins; the engine verifies the pair and the triple
with the same machinery, exhibiting the k-tuple-style tower one level up
from Hardy–Littlewood's linear world.

**Verification.** `verify/c08_quadratic_triple.py`, N = 10^7.

---

## C09 — Fibonacci primes (Lenstra–Pomerance–Wagstaff analogue)

**Conjecture.** `#{p <= x : p prime, F_p prime} = (e^gamma / log phi) * log x * (1+o(1))`,
slope `e^gamma/log phi = 3.7010...`, phi the golden ratio.

**Derivation.** Every prime divisor q of F_p (p prime, p ≠ 5) has rank of
apparition exactly p, hence q ≡ ±1 (mod p) — the same divisor screening
that powers the LPW Mersenne heuristic.  Sizes: log F_p = p log phi + O(1).
Replacing log 2 by log phi in the LPW argument gives the slope; the count
through exponent x is (e^gamma/log phi) log x, i.e. expected number of
Fibonacci primes with p in a dyadic block is constant — a log log law in
the size of F_p (criterion II.7: divergent Borel–Cantelli sum, barely).

**Humility clause.** The mod-5 splitting of ranks (q ≡ ±1 mod 5 vs not)
may modify the constant by an O(1) factor the way Granville's factor
corrects Cramér; the verification reports the empirical slope with its
Poisson error precisely to expose this.

**Verification.** `verify/c09_fibonacci_primes.py`: BPSW-tests F_p for all
p ≤ 10^4 (up to 2090 digits).

---

## C10 — Primorial primes p# + 1

**Conjecture.** `#{p <= x : p# + 1 prime} = e^gamma * log x * (1+o(1))`.

**Derivation.** p# + 1 is coprime to every prime q ≤ p by construction, so
its survival odds against trial division are boosted by
`prod_{q<=p} (1-1/q)^{-1} ~ e^gamma log p` (Mertens) relative to a random
integer of size log(p#) = theta(p) ~ p.  Probability per prime:
`e^gamma log p / p`; summing over p ≤ x gives `e^gamma log x` — again a
divergent-but-barely Borel–Cantelli sum, so "infinitely many primorial
primes, with predictable log-density" is the maximal supportable claim.
The same argument gives the same constant for p# − 1 (not run here).

**Verification.** `verify/c10_primorial_primes.py`, p ≤ 4000
(numbers to ~1700 digits, BPSW).

---

## C11 — Primes of the form n^2 + 2^n

**Conjecture.** There are infinitely many primes n^2 + 2^n; necessarily
n ≡ 3 (mod 6), and

    #{n <= N : n^2+2^n prime} = E(N) * (1+o(1)),
    E(N) = sum_{n = 3 (6), n <= N} kappa / log(n^2 + 2^n) ~ (kappa/(6 log 2)) log N,

with the local constant `kappa = prod_p (1 - delta_p)/(1 - 1/p)`, where
delta_p is the exact density of n ≡ 3 (mod 6) with p | n^2 + 2^n, computed
over the period lcm(6, p·ord_p(2)).

**Admissibility (the fun part).** Parity forces n odd; then mod 3, if
n ≢ 0 the value is 1 + 2 ≡ 0 (mod 3).  So the *only* admissible lane is
n ≡ 3 (mod 6) — and there kappa's first two factors are (1-0)/(1-1/2) = 2
and (1-0)/(1-1/3) = 3/2: what looks like a punishing obstruction is
actually a 3x local bonus inside the lane.  Mixed polynomial–exponential
sequences are exactly where hand-waving dies and the computed singular
series earns its keep.

**Verification.** `verify/c11_n2_plus_2n.py`: kappa from local densities
(p ≤ 300), PRP scan n ≤ 4200 (~1270 digits).

---

## C12 — Factorial primes n! + 1

**Conjecture.** `#{n <= N : n! + 1 prime} = e^gamma * log N * (1+o(1))`.

**Derivation.** Identical screening to C10: n!+1 is coprime to all primes
≤ n, boost e^gamma log n against size log n! ~ n log n, probability
e^gamma/n per n, partial sums e^gamma log N.  C10 and C12 share a constant
but not a sequence — a deliberate pairing: if the data track the constant
in both (they do — see RESULTS), the *model* is validated, not a lucky fit
(criterion III.9: it is the shape of agreement across the family that
persuades).

**Verification.** `verify/c12_factorial_primes.py`, n ≤ 700.

---

## C13 — Prime plus a positive cube (restated after self-refutation)

**History, on the record.** The first version claimed the whole exception
set of n = p + k^3 (k ≥ 1) is finite.  Our own adversarial battery
refuted it: every exception it found in (10^8, 10^9] is a perfect cube.
Cause: for n = k^3, n − j^3 = (k−j)(k^2+kj+j^2) factors algebraically, so
a cube is representable only through j = k−1, i.e. iff 3k^2−3k+1 is
prime.  That is an elementary theorem manufacturing an *infinite*,
density-one-in-cubes exceptional family — an algebraic obstruction
(criterion I.2/I.3) the Borel–Cantelli accounting missed because cubes
have density zero.  The failure mode is exactly the one the criteria
document warns about, and we keep it visible rather than papering over
it.

**Conjecture (restated).**
(i) [theorem, machine-checked] For k ≥ 2, k^3 is unrepresentable iff
    3k^2−3k+1 is composite; hence #{exceptions ≤ x} ~ x^{1/3}.
(ii) [conjecture] The set of NON-CUBE integers n ≥ 2 not representable as
    p + k^3 is finite; its per-decade counts decay super-geometrically
    (the largest non-cube exception below 10^8 is 78,526,384).
(iii) [Bateman–Horn corollary] The representable cubes follow
    #{k ≤ K : 3k^2−3k+1 prime} ~ C * int dt/log(3t^2−3t+1) — a fresh BH
    instance born from the refutation.

**Accounting.** Representation chances: ~ n^{1/3} cubes, each hit prime
with the locally-corrected probability m(v)/log v where the local weight
m(v) = prod_{p in {2,3,7}} [p/(p-1) if p ∤ v else 0] (2, 3, 7 are the
moduli where cubes degenerate: k^3 mod 9 ∈ {0,±1}, mod 7 ∈ {0,±1}).
P(n unrepresentable) = prod_k (1 - m/log v) decays like exp(-c_n n^{1/3}/log n);
summing over n converges.  Two model lessons the data taught (see RESULTS):
the *naive* model without local weights underestimates exceptions by an
order of magnitude (the singular series is not optional), and even the
3-prime-corrected model undershoots the last observed decade — the extreme
tail is dominated by worst-case congruence classes that a truncated local
product smooths over.  The conjecture leans on the observed decay rate,
not on the truncated model's tail integral.

**Verification.** `verify/c13_prime_plus_cube.py`: exact exception list to
10^8 by vectorized sieve-shift union; sampled local-model per decade.

---

## C14 — The Stern-type list for p + 2k^2, k ≥ 1

**Conjecture.** Exactly ten odd numbers are not of the form p + 2k^2 with
p prime and k ≥ 1:

    1, 3, 17, 137, 227, 977, 1187, 1493, 5777, 5993

and 5993 is the largest (verified to 10^8; expected further exceptions
beyond, by the C13-style accounting with ~ sqrt(n/2) chances: < 10^-40).

**Attribution (corrected by the novelty audit).** This conjecture is
previously stated, essentially verbatim: OEIS A060003 ("odd numbers not of
the form p + 2x^2, x > 0") lists exactly these ten terms and conjectures
completeness; the prime members 3, 17, 137, 227, 977, 1187, 1493 are the
Stern primes (A042978), with 1493 famously the largest known.  An earlier
draft of this memo wrongly claimed 1493 was absent from the classical
lists — the adversarial audit caught that, and the correction is left on
record deliberately.  Our contribution here is verification machinery and
the Borel–Cantelli tail accounting, not the statement.

**Verification.** `verify/c14_stern_2k2.py`, exhaustive to 10^8.

---

## C15 — Goldbach in the 3 (mod 4) lane

**Conjecture.** (a) Every n ≡ 2 (mod 4) with n ≥ 6 is p + q with
p ≡ q ≡ 3 (mod 4) both prime.  (b) The ordered count obeys

    R3(n) = (1/2) * S(n) * int_3^{n-3} dt/(log t log(n-t)) * (1+o(1)),

S(n) the Goldbach singular series — exactly half of all Goldbach
representations, because p + q ≡ 2 (mod 4) forces p ≡ q (mod 4) and
equidistribution splits the two lanes evenly.

**Why this and not mod-4-class-(1,1)?**  For n ≡ 2 (mod 4) the two lanes
are symmetric asymptotically, but the (3,3) lane never loses its smallest
representations (3 + q), so it admits the clean threshold n ≥ 6 with *no
exceptions at all* — the strongest uniform statement available.  (The
(1,1) lane fails for a sprinkling of small n.)  Choosing the lane with the
exceptionless threshold is the Goldilocks calibration.

**Verification.** `verify/c15_goldbach_mod4.py`: existence swept
exhaustively to 10^8; R3(n) computed exactly at sampled n across two
decades and compared with the singular-series prediction.

---

## C16 — Uniform quantitative de Polignac

**Conjecture.** For every even d, `pi_d(x) = #{p <= x-d : p, p+d prime}`
satisfies `pi_d(x) = S(d) Li_2(x) (1 + o(1))` *uniformly* for
d ≤ (log x)^A: at x = 10^8 the normalized residuals
`z_d = (pi_d - S(d) Li_2)/sqrt(S(d) Li_2)` over all even d ≤ 2000 behave
like a single N(0, sigma^2) sample with sigma = O(1), no trend in d, and
the regression slope of pi_d on S(d) Li_2 equals 1.

**Content.** Individual de Polignac statements (every even d occurs
infinitely often) are subsumed; what is *added* is the uniformity — the
singular series predicts a thousand different constants at once, spanning
a factor ~3 from S(2) to S(2·3·5·7·...), and the data must reproduce the
entire profile with square-root errors.  A conspiracy would need to bend a
1000-dimensional vector, not one number.  This is the strongest form the
random model supports at fixed x (criterion IV.13) and the cleanest
"shape of agreement" exhibit in the suite.

**Verification.** `verify/c16_uniform_depolignac.py`: all even d ≤ 2000 at
x = 10^8, correlation/slope/z-statistics and drift check.

---

## C17 — Goldbach with twin-prime members

**Conjecture.** Every even n ≥ 4210 is t1 + t2 where t1, t2 are members of
twin-prime pairs; the full exception list is

    2, 4, 94, 96, 98, 400, 402, 404, 514, 516, 518, 784, 786, 788,
    904, 906, 908, 1114, 1116, 1118, 1144, 1146, 1148, 1264, 1266, 1268,
    1354, 1356, 1358, 3244, 3246, 3248, 4204, 4206, 4208

(verified complete to 10^8 here).

**Accounting.** Twin members have density ~ 2·S(2)/log^2 x, so expected
representations of n are ~ c(n)·n/log^4 n — divergent enough that the
exception count must be finite; the exceptions' clustering in triples
(consecutive evens) reflects the sparse low-lying twin population, a
structural fingerprint no bare existence claim would show.  Assuming only
Hardy–Littlewood for the pattern set, this refines both Goldbach (weaker
input per prime, stronger structural demand) and twin infinitude (which it
implies).

**Verification.** `verify/c17_twin_goldbach.py`, exhaustive to 10^8.

---

## C18 — Cramér gaps between twin pairs

**Conjecture.** Let G_t(x) be the largest gap between consecutive twin-prime
starts up to x.  Then G_t(x) ≍ log^3 x, and to first order

    limsup_{x} G_t(x) / log^3 x = 1/(2 C2) = 0.75735...

**Derivation.** Twin starts have local density 2C2/log^2 t; a Cramér model
for the thinned process gives record waiting times ~ (log of event count)
x (mean spacing) = log(x) * log^2(x)/(2C2).

**Humility clause (criterion II.6, learned from Mertens/Cramér).**
Granville's lesson applies verbatim: local corrections to a Cramér model
can shift such constants by factors like 2e^{-gamma}; the honest statement
is the order log^3 x with the constant flagged as first-order.  The data
(normalized records ~0.4–0.5 at 10^9, drifting up on a log log clock)
can neither confirm nor refute the exact constant — as the memo predicts
they cannot; what they do confirm is the cube of the logarithm.

**Verification.** `verify/c18_twin_gap_records.py`, records to 10^9.

---

## C19 — First occurrence of a prime gap

**Conjecture.** Let p(g) be the prime starting the first occurrence of a
gap of exactly g.  Then `log p(g) / sqrt(g) -> sqrt(e^gamma/2) = 0.94358...`
(Granville-corrected Shanks; Shanks' original heuristic gives limit 1, the
uncorrected Cramér maximal-gap constant).

**Derivation.** If maximal gaps near x are ~ c log^2 x, the first gap of
size g appears where g = c log^2 p, i.e. log p(g) = sqrt(g/c).  Cramér's
c = 1 gives slope 1; Granville's local-configuration correction
c = 2e^{-gamma} = 1.1229 gives 0.9436.  The two differ by 6% — below the
resolution of any feasible computation (the criteria document's log log
drift warning, quantified) — so the conjecture's value is structural: it
pins the *functional form* log p ~ sqrt(g) and registers a definite,
falsifiable-in-principle constant on the books.

**Verification.** `verify/c19_gap_first_occurrence.py`: all first
occurrences to 10^9, regression slope over g ≥ 100, missing-gap census.

---

## C20 — Microscopic intervals: Poisson with an exact second-order deficit

**Conjecture.** Fix lambda > 0 and let X count primes in [t, t + lambda log x)
for random t ~ x.  Then X converges to Poisson(lambda) (Gallagher), and at
finite x the ratio obeys

    Var(X)/E(X) = 1 - (log(lambda log x) + gamma + log 2pi - 1)/log x + O(1/log^2 x).

The constant `gamma + log 2pi - 1 = 1.41508...` comes from Montgomery's
`sum_{d<=h} S(d)(h-d) = h^2/2 - (h/2)(log h + gamma + log 2pi - 1) + o(h)`.

**Story.** The naive conjecture ("counts are Poisson, Var/mean = 1") is
*refuted* by our data at 5 sigma-equivalents — variance deficits of 20–30%
persist across lambda — while the corrected statement matches to three
decimals at 10^8 and 10^9 with no tuned parameter.  This is the suite's
clearest demonstration of criterion II.6: demand exactly the fluctuation
the model earns, not the one the limit theorem suggests.

**Verification.** `verify/c20_poisson_intervals.py`: 10^7–10^8 disjoint
windows near 10^9, lambda ∈ {1/2, 1, 2, 4}.

---

## C21 — The twin-prime race mod 5

**Setup.** Twin starts p > 5 fall in classes p ≡ 1, 2, 4 (mod 5).  In the
von-Mangoldt-weighted count, square contamination — the engine of
Chebyshev's bias — enters through twin patterns containing a prime square.
Mod 3 kills (q^2, q^2+2) for every q > 3 (3 | q^2+2 always), so the *only*
surviving contamination is (q^2−2, q^2), governed by C07.  Since
q^2 ≡ 1 or 4 (mod 5), the contaminated start q^2−2 lies in class 4 or 2 —
never class 1.

**Conjecture.** (a) pi_t(x;5,1) systematically leads:
`D1(x) = pi_t(x;5,1) − (pi_t(x;5,2)+pi_t(x;5,4))/2` has positive
logarithmic mean, with the mechanism-sized systematic part

    D1_sys(x) = (1/(2 log^2 x)) * sum_{q <= sqrt x, q^2-2 prime} log q * log(q^2-2);

(b) classes 2 and 4 are symmetric (their difference is driftless);
(c) — the structural point — bias/noise decays like 1/log x, so unlike
Chebyshev's classical races the twin race has *no* persistent leader:
leadership log-density tends to a limit strictly between 1/2 and 1.
An initially-plausible alternative ("class 4 trails because both members
are quadratic residues") is *inadmissible* once the mod-3 computation is
done — the engine's first guess was wrong and the local analysis corrected
it before the data did.

**Verification.** `verify/c21_twin_race_mod5.py` to 10^9: D1 vs D1_sys,
the 2–4 control, both leadership densities.

---

## C22 — Least primes in progressions: exponential tail, Gumbel extremes

**Conjecture.** Put U(a,q) = Li(p(a,q))/phi(q), p(a,q) the least prime
≡ a (mod q).  Then:

  (i)  U → Exp(1) in distribution as q → ∞: tail log-slope → −1,
       max_a U − H_{phi(q)} → Gumbel (H_n = sum 1/k) — the Wagstaff-type
       bound max p(a,q) ~ phi(q) log^2 q in exact order-statistics form,
       and E_a[U] → 1;
  (ii) the finite-q deficit is first-order 1/log q:
       `E_a[U] = 1 − theta(q)/log q + o(1/log q)` with theta slowly
       varying (measured theta ≈ 1.6–1.9 across two decades of q; the
       deficit bottoms out near q ~ 200 and then *recovers* — the
       signature of a vanishing correction, not of a limit below 1).

**What the data forced.** The naive claim "U is Exp(1) at finite q" is
refuted decisively: at q ≤ 3000 the whole distribution is ~25% compressed
(mean 0.75, tail slope −1.5, maxima ~2.5 below H_phi).  Controls isolate
the causes: a Cramér pseudo-prime control shows discrete-hazard
finite-size effects (~0.9 at q ~ 2300), and the remaining gap to the real
primes (~0.13) disappears under any reshuffling of the actual prime
residues — the ordering of the primes fills classes faster than any
exchangeable model.  Both corrections scale like 1/log q, which is what
(ii) asserts; the constant theta is left open, honestly, as the deepest
unexplained number in this suite.

**Verification.** `verify/c22_least_prime_ap.py`: all q ≤ 3000, every
admissible class, primes to 5·10^6; per-band theta estimates.

---

## C23 — Fermat quotients: equidistribution and the Wieferich ledger

**Conjecture.** Let q_p = (2^{p−1}−1)/p mod p.  Then
(a) q_p/p equidistributes on [0,1) with square-root discrepancy
    (KS distance ~ pi(x)^{-1/2}, no drift between halves);
(b) tail uniformity: #{p ≤ x : q_p < K} = sum_p min(1, K/p) (1+o(1));
(c) hence #{Wieferich p ≤ x} = log log x + O(1) — Borel–Cantelli on the
    divergent-but-barely sum 1/p — so {1093, 3511} below 10^8, a third
    example expected only near doubly-exponential heights.

**Position.** (a) is strictly stronger than (c) and is what the data can
actually measure well (criterion III.9: verify the model, not the rare
event).  A Wieferich desert (or glut) violating (c) would break (a) first.

**Verification.** `verify/c23_fermat_quotients.py`: KS to 10^7,
small-quotient census, Wieferich sweep to 10^8.

---

## C24 — Hardy–Littlewood Conjecture F as a family: the constants predict the ordering

**Conjecture.** For odd A let Q_A(N) = #{n ≤ N : n^2+n+A prime} and
C(A) = BH(x^2+x+A).  Then uniformly over the family (all odd A ≤ 199,
including Euler's A = 41):

    Q_A(N) = C(A) * int_2^N dt/log(t^2+t+A) * (1 + o(1)),

with residuals jointly of Poisson size — so the computed singular series
alone predicts the full empirical ranking of the hundred polynomials
(rank correlation → 1), and A = 41 is prime-rich for a *reason* that the
engine computes rather than admires.

**Content over the single-A statement.** As with C16, the family-level
claim is what makes the evidence compelling: one hundred constants spanning
a ~6x density range must all land on the same regression line of slope 1.
Description length: the entire data set (10^8 primality bits) compresses to
one product formula per A (criterion IV.11).

**Verification.** `verify/c24_hl_family_F.py`: N = 10^6 per A, polynomial
presieve + deterministic MR; correlation, rank correlation, max |z|.

---

## C25 — Consecutive primes mod 3: the vanishing repulsion law

**Conjecture.** Among consecutive primes p, p' ≤ x (both > 3), the
same-class fraction s(x) = #{p ≡ p' (mod 3)}/#pairs satisfies

    1/2 − s(x) = (c + o(1)) * log log x / log x,   with c ∈ (0, ∞),

(Lemke Oliver–Soundararajan's first-order law at q = 3: the repulsion is
real but *evanescent*, vanishing at the precise rate loglog/log — neither a
constant bias like Chebyshev's nor a square-root artifact), and the deficit
splits symmetrically: #(1,1)/#(2,2) → 1.

**Falsifiability shape.** The verification computes
c_hat(x) = (1/2 − s(x))·log x/loglog x at geometric checkpoints; the
conjecture demands c_hat flat while x traverses two decades (a 10% window
on a quantity that would drift by 50% if the exponent of either log were
wrong by 1/4).  The measured c_hat is reported with its trajectory; the
symmetric split is a second, sharper null.

**Verification.** `verify/c25_consecutive_mod3.py`, all consecutive pairs
to 10^9.
