# Verification results

Auto-generated from `results/*.json` (the committed record of the actual
runs).  Regenerate with `python3 compile_results.py` after re-running any
verifier.


## C01 — uniform quadratic de Polignac: (n^2+1, n^2+1+d) ~ C(d) I(N) uniformly over admissible even d

* **correlation** = 0.9998
* **slope** = 1.002
* **z_mean** = 0.2415
* **z_sd** = 0.8421
* **z_max_abs** = 2.28

## C01B — distribution of C(d): derived Euler-product moments match the empirical family


## C02 — n^3+2 prime

* **constant_C** = 1.298
* **constant_wobble** = 0.0002509
* **first_solutions**: 1, 3, 5, 29, 45, 63, 65, 69, 71, 83

**table**

| N | obs | pred | ratio | z |
|---|---|---|---|---|
| 1000 | 74 | 77.2 | 0.9586 | -0.36 |
| 10000 | 520 | 539.7 | 0.9636 | -0.85 |
| 100000 | 4059 | 4168 | 0.9738 | -1.69 |
| 1000000 | 33795 | 3.403e+04 | 0.9931 | -1.28 |
| 10000000 | 287956 | 2.878e+05 | 1.001 | 0.32 |

## C02B — cubic family: C(a) has a limiting distribution with derived Euler-product moments; count uniform over a

* **z_mean** = 0.09285
* **z_sd** = 0.7199

## C03 — p, 2p-1, 3p-2 all prime (AP chain)

* **constant_C** = 2.858
* **constant_wobble** = 2.982e-06
* **first_solutions**: 3, 7, 37, 211, 271, 307, 331, 337, 601, 727

**table**

| N | obs | pred | ratio | z |
|---|---|---|---|---|
| 100 | 3 | 5.4 | 0.5598 | -1.02 |
| 1000 | 10 | 14.2 | 0.7043 | -1.11 |
| 10000 | 46 | 49.9 | 0.9225 | -0.55 |
| 100000 | 229 | 228.6 | 1.002 | 0.03 |
| 1000000 | 1259 | 1250 | 1.008 | 0.27 |
| 10000000 | 7597 | 7626 | 0.9962 | -0.33 |
| 100000000 | 50193 | 5.01e+04 | 1.002 | 0.43 |
| 300000000 | 125379 | 1.254e+05 | 0.9996 | -0.14 |

## C03B — triplet (0,2,6) race mod 5: class 1 leads via the (q^2-2, q^2, q^2+4) doubly-thinned configuration


## C04 — power-obstruction ladder (corrected): composite k impossible (thm); prime-k lanes follow Bateman-Horn for D_k


## C05 — cyclotomic twin bases: Phi_k(n), Phi_k(n+1) both prime for k in {3,6}; k=4 branch dead by parity (only (2,5))


## C06 — alternating cyclotomic chain p, Phi3(p), Phi6(Phi3(p)) all prime

* **constant_C** = 3.614
* **constant_wobble** = 0.01081
* **first_solutions**: 2, 3, 59, 101, 1847, 1973, 3041, 3671, 3989, 4721

**table**

| N | obs | pred | ratio | z |
|---|---|---|---|---|
| 1000 | 4 | 3.3 | 1.223 | 0.4 |
| 10000 | 11 | 10.2 | 1.079 | 0.25 |
| 100000 | 41 | 43.4 | 0.945 | -0.36 |
| 1000000 | 224 | 227.8 | 0.9833 | -0.25 |
| 10000000 | 1362 | 1357 | 1.004 | 0.13 |

## C07 — p and p^2-2 both prime

* **constant_C** = 3.383
* **constant_wobble** = 0.0007611
* **first_solutions**: 2, 3, 5, 7, 13, 19, 29, 37, 43, 47

**table**

| N | obs | pred | ratio | z |
|---|---|---|---|---|
| 1000 | 52 | 56.7 | 0.9175 | -0.62 |
| 10000 | 259 | 272.4 | 0.9506 | -0.81 |
| 100000 | 1595 | 1598 | 0.9982 | -0.07 |
| 1000000 | 10548 | 1.057e+04 | 0.9983 | -0.17 |
| 10000000 | 74914 | 7.527e+04 | 0.9952 | -1.31 |

## C07B — sexy-pair contamination matrix: two surviving orientations, drift components T_A (class 3 mod 5 / 3 mod 8) and T_B (class 1 mod 5 / 1 mod 8), class 2 mod 5 and 5,7 mod 8 clean


## C08 — null-mechanism race: quadratic twin pairs have no square contamination; class race n=1 vs n=4 (mod 5) is driftless


## C09 — #{p<=x: F_p prime} ~ (e^gamma/log phi) log x

* **slope_predicted** = 3.701
* **hits**: 3, 5, 7, 11, 13, 17, 23, 29, 43, 47, 83, 131, 137, 359, 431, 433, 449, 509, 569, 571, 2971, 4723, 5387, 9311, 9677

**table**

| x | obs | pred | ratio | z |
|---|---|---|---|---|
| 100 | 11 | 17 | 0.645 | -1.46 |
| 1000 | 20 | 25.6 | 0.782 | -1.1 |
| 10000 | 25 | 34.1 | 0.733 | -1.56 |

## C09B — finitely many p with F_p and L_p both prime; disjoint rank pools (p vs 2p) justify joint independence


## C10 — n=3 is the only factorial twin (n!-1, n!+1 both prime)


## C11 — infinitely many primes n^2+2^n; count ~ E(N)

* **kappa** = 4.273
* **hits**: 3, 9, 15, 21, 33, 2007, 2127, 3759

**table**

| N | obs | pred | z |
|---|---|---|---|
| 100 | 5 | 4.37 | 0.3 |
| 1000 | 5 | 6.71 | -0.66 |
| 4200 | 8 | 8.19 | -0.07 |

## C11B — n^2+2^n: CRT-exact kappa_S net converges; count ~ E(N)

* **hits**: 3, 9, 15, 21, 33, 2007, 2127, 3759

**table**

| N | obs | pred | z |
|---|---|---|---|
| 1000 | 5 | 6.71 | -0.66 |
| 4200 | 8 | 8.19 | -0.07 |
| 6000 | 8 | 8.55 | -0.19 |

## C12 — #{n<=N: n!+1 prime} ~ e^gamma log N

* **slope_predicted** = 1.781
* **hits**: 1, 2, 3, 11, 27, 37, 41, 73, 77, 116, 154, 320, 340, 399, 427

**table**

| N | obs | pred | ratio | z |
|---|---|---|---|---|
| 100 | 9 | 8.2 | 1.097 | 0.28 |
| 700 | 15 | 11.7 | 1.286 | 0.98 |

## C12B — pair-level MS law: pinned 4-tuple average G(H) = -(beta2/2) log^2 H + O(log H); Var/E = 1 + 2 S(2) G(H)/log^2 x


## C13 — RESTATED: non-cube exceptions of n=p+k^3 finite; cube k^3 exceptional iff 3k^2-3k+1 composite (thm); cube lane follows BH


## C13B — boundary-factorization principle: collapse to the boundary lane + dead-parity/dead-3adic/BH trichotomy for x^3+cx


## C14 — 5993 is the largest odd n not of form p+2k^2 (k>=1)

* **largest_exception** = 5993
* **exceptions**: 1, 3, 17, 137, 227, 977, 1187, 1493, 5777, 5993

## C14B — Stern lane race: k-parity drift = norm-form contamination, classes 1,3 (mod 8) contaminated (opposite lanes), 5,7 null


## C15 — every n=2(4)>=6 is a sum of two primes =3(4); R3(n) ~ (1/2)S(n)*I(n)

* **exceptions**: 

**samples**

| n | obs | pred | ratio |
|---|---|---|---|
| 1000002 | 8236 | 8128 | 1.013 |
| 1000006 | 4832 | 4877 | 0.9908 |
| 10000002 | 59648 | 5.951e+04 | 1.002 |
| 10000006 | 29740 | 2.98e+04 | 0.9979 |
| 99999994 | 219360 | 2.19e+05 | 1.002 |
| 99999998 | 275046 | 2.751e+05 | 0.9998 |

## C15B — least Goldbach summand: U => Exp(1); canonical ordering deficit Theta_G > 0 (sibling of C22(ii))

* **KS** = 0.0877

## C16 — pi_d(x) ~ S(d) Li2(x) uniformly in d

* **correlation** = 1
* **slope** = 0.9997
* **z_mean** = -0.2674
* **z_sd** = 0.5186
* **z_max_abs** = 1.799

**worst**

| d | obs | pred | z |
|---|---|---|---|
| 1832 | 441111 | 4.423e+05 | -1.8 |
| 1480 | 602615 | 6.039e+05 | -1.7 |
| 1054 | 484754 | 4.859e+05 | -1.68 |
| 804 | 892753 | 8.943e+05 | -1.62 |
| 960 | 1172603 | 1.174e+06 | -1.58 |
* **drift** = [-0.2864915835029418, -0.24827897183404862]

## C16B — covariance kernel of z_d profile from HL triple constants


## C16C — moving-window pair-count field: empirical correlation matrix matches HL triple-constant kernel


## C17 — every even n>=4210 is a sum of two twin-pair members

* **largest_exception** = 4208
* **exceptions**: 4, 94, 96, 98, 400, 402, 404, 514, 516, 518, 784, 786, 788, 904, 906, 908, 1114, 1116, 1118, 1144, 1146, 1148, 1264, 1266, 1268, 1354, 1356, 1358, 3244, 3246, 3248, 4204, 4206, 4208

## C17B — quantitative twin-member Goldbach: R_T(n) ~ [sum of 4 orientation S4(n)] J(n)

* **z_mean** = -11.09
* **z_sd** = 8.746

## C18 — limsup G_twin(x)/log^3 x = 1/(2C2)

* **model_constant** = 0.7574

**checkpoints**

| x | record | ratio_log3 |
|---|---|---|
| 100000 | 630 | 0.4128 |
| 1000000 | 1452 | 0.5506 |
| 10000000 | 1722 | 0.4112 |
| 100000000 | 2868 | 0.4588 |
| 1000000000 | 4770 | 0.536 |

**records** (gap, after): (2190 @ 17382479), (2256 @ 30752231), (2832 @ 32822369), (2868 @ 96894041), (3012 @ 136283429), (3102 @ 234966929), (3180 @ 248641037), (3480 @ 255949949), (3804 @ 390817727), (4770 @ 698542487)

## C18B — Darling-Erdos running-max law for balanced races: max |D|/sqrt(count) ~ sqrt(2 loglog x); finite-x null from OU simulation


## C19 — log p(g)/sqrt(g) -> sqrt(e^gamma/2) = 0.9436

* **slope_measured_g_ge_100** = 1.307
* **slope_cramer** = 1
* **slope_granville** = 0.9437
* **missing_even_gaps**: 254, 256, 258, 262, 264, 266, 268, 270, 272, 274, 278, 280

**table**

| g | p | log_p_over_sqrt_g |
|---|---|---|
| 30 | 4297 | 1.527 |
| 60 | 43331 | 1.378 |
| 90 | 404851 | 1.361 |
| 120 | 1895359 | 1.319 |
| 150 | 13626257 | 1.341 |
| 180 | 17051707 | 1.241 |
| 210 | 20831323 | 1.163 |
| 240 | 391995431 | 1.277 |
| 282 | 436273009 | 1.185 |

## C19B — second-order S*(g) dependence of first occurrences: log p(g) = sqrt g + (1/2)log g - (1/2)log S*(g) + O(1)


## C20 — Var/mean = 1 - (log h + gamma + log 2pi - 1)/log x

* **second_order_constant** = 1.415

**table**

| lambda | windows | mean | var | var_over_mean | predicted | naive_poisson | z_vs_pred |
|---|---|---|---|---|---|---|---|
| 0.5 | 19301976 | 0.4977 | 0.4102 | 0.8241 | 0.8189 | 1 | 16.04 |
| 1 | 9650988 | 0.9955 | 0.7874 | 0.791 | 0.7854 | 1 | 12.27 |
| 2 | 4825494 | 1.991 | 1.498 | 0.7527 | 0.752 | 1 | 1.02 |
| 4 | 2412747 | 3.982 | 2.867 | 0.7201 | 0.7185 | 1 | 1.67 |

## C21 — class 1 leads twin race mod 5 via q^2-2 mechanism; classes 2,4 symmetric; bias/noise ~ 1/log x

* **lead_density_D1_positive** = 0.8473
* **lead_density_D24_positive** = 0.9981

**table**

| x | D1 | D1_predicted | D24_control | noise_scale |
|---|---|---|---|---|
| 1.258e+07 | 163 | 20.9 | 252 | 189.8 |
| 1.007e+08 | 97.5 | 47.9 | 443 | 470.6 |
| 4.027e+08 | -77.5 | 87 | 269 | 870.8 |
| 1e+09 | -426.5 | 127.2 | 969 | 1308 |
* **final_counts** = {"1": 1141217, "2": 1142128, "4": 1141159}

## C21B — mod-8 twin race: entire square-contamination on class 7; 1,3,5 symmetric


**table**

| x | D7 | T_predicted | noise_scale |
|---|---|---|---|
| 1.258e+07 | 27 | 41.9 | 155 |
| 1.007e+08 | 549 | 95.8 | 384 |
| 4.027e+08 | 693 | 174 | 711 |
| 1e+09 | 212 | 254.3 | 1068 |
* **final_counts** = {"1": 856684, "3": 855807, "5": 856046, "7": 855967}

## C21C — contamination calculus, fresh instance: cousin races (n,n+4) mod 5 (class-4 deficit) and mod 8 (class-1 deficit)


**table**

| x | D5 | D8 | T_pred | noise | ctrl23 | ctrl35 |
|---|---|---|---|---|---|---|
| 9.647e+07 | 251 | 140 | 66.7 | 653 | 214 | 387 |
| 3.985e+08 | 803 | 2 | 118.4 | 1226 | 172 | 799 |
| 1e+09 | -20.5 | -319.3 | 163.6 | 1851 | 17 | 198 |

## C22 — tail of Li(p(a,q))/phi is Exp(1); max ~ H_phi + Gumbel

* **tail_slope** = -1.545
* **gumbel_mean** = -2.454
* **gumbel_sd** = 0.7982
* **gumbel_sd_model** = 1.283
* **mean_U_overall** = 0.761

**mean_U_by_band**

| q_band_lo | mean_U | theta |
|---|---|---|
| 2.2 | 0.8507 | 0.172 |
| 4.6 | 0.9633 | 0.07 |
| 10 | 0.9008 | 0.266 |
| 21.5 | 0.8046 | 0.675 |
| 46.4 | 0.76 | 1.013 |
| 100 | 0.7405 | 1.294 |
| 215.4 | 0.7368 | 1.515 |
| 464.2 | 0.7428 | 1.678 |
| 1000 | 0.7537 | 1.796 |
| 2154 | 0.7621 | 1.917 |

## C22B — theta decomposition with defined Bernoulli control; theta_corr persistence on prime moduli differentiates from smooth-q effects


**rows**

| stratum | n_q | theta_disc_mean | theta_disc_se | theta_corr_mean | theta_corr_se |
|---|---|---|---|---|---|
| prime | 40 | 0.8469 | 8.801e-06 | 0.8243 | 0.009135 |
| smooth | 40 | 4.322 | 0.2218 | -2.321 | 0.2204 |

## C22C — injective no-collision baseline for C22: Theta_inj = (1+o(1))/(2 log q), an order of magnitude below measured theta_corr = 0.824


## C23 — Fermat quotients equidistribute; Wieferich count ~ loglog x

* **KS** = 0.0006425
* **sqrt_n_KS** = 0.5238
* **mean_u** = 0.4999
* **small_quotient_obs** = 156
* **small_quotient_pred** = 147.9
* **wieferich_expected** = 2.675
* **wieferich**: 1093, 3511

## C23B — multibase Fermat quotients: exact homomorphism; joint equidistribution for independent bases; simultaneous Wieferich finiteness (empirical list empty)

* **correlation** = 0.002333

## C24 — Q_A(N) ~ C(A) I_A(N) uniformly over odd A

* **correlation** = 1
* **rank_correlation** = 0.9999
* **mean_ratio** = 1.001
* **sd_ratio** = 0.002721
* **max_abs_z** = 1.92

**rows**

| A | C | obs | pred | ratio | z |
|---|---|---|---|---|---|
| 1 | 2.241 | 88118 | 8.809e+04 | 1 | 0.09 |
| 11 | 3.259 | 128170 | 1.281e+05 | 1 | 0.17 |
| 21 | 0.9702 | 38207 | 3.814e+04 | 1.002 | 0.33 |
| 31 | 2.484 | 97181 | 9.765e+04 | 0.9952 | -1.49 |
| 41 | 6.641 | 261080 | 2.611e+05 | 1 | 0.02 |
| 51 | 1.184 | 46814 | 4.655e+04 | 1.006 | 1.21 |
| 61 | 2.241 | 87768 | 8.809e+04 | 0.9964 | -1.08 |
| 71 | 2.678 | 105388 | 1.053e+05 | 1.001 | 0.31 |
| 81 | 1.539 | 60571 | 6.048e+04 | 1.001 | 0.36 |
| 91 | 2.037 | 79982 | 8.008e+04 | 0.9988 | -0.34 |
| 101 | 5.102 | 200584 | 2.006e+05 | 1 | 0.06 |
| 111 | 1.428 | 56401 | 5.615e+04 | 1.004 | 1.04 |
| 121 | 2.423 | 95254 | 9.525e+04 | 1 | 0.03 |
| 131 | 2.15 | 84371 | 8.452e+04 | 0.9983 | -0.5 |
| 141 | 0.8309 | 32809 | 3.266e+04 | 1.004 | 0.81 |
| 151 | 2.783 | 109591 | 1.094e+05 | 1.002 | 0.55 |
| 161 | 4.165 | 163440 | 1.637e+05 | 0.9982 | -0.73 |
| 171 | 1.799 | 70667 | 7.071e+04 | 0.9993 | -0.18 |
| 181 | 3.024 | 118762 | 1.189e+05 | 0.999 | -0.36 |
| 191 | 3.417 | 134314 | 1.343e+05 | 0.9998 | -0.07 |

## C24B — Conjecture-F family covariance kernel from pair singular series


## C25 — Goldbach lane race: R3-R1 ~ square contamination D_sys on average; (3,3) lane leads


## C25B — HL-weighted drift, sign-density constant, and internal null lane n=1(3) for the Goldbach lane race

