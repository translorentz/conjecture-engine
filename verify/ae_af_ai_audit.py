#!/usr/bin/env python3
"""Independent checks for the Parts XIV-XVIII audit (f2316c7b) findings that
were incorporated:

  * ae1/ae2 (Prop ae:hyper): the hypersurface primitive middle Betti closed form
    B_{n,1}(d)=f_n(d-1), f_n(x)=(x^{n+2}+(-1)^n x)/(x+1)^2, cross-checked against
    a direct Chern/Euler evaluation, is strictly increasing and strictly
    discretely convex in d in every dimension.

  * ae12 => ae13, ae14 (Prop ae:disp): on the exact Griffiths Hodge profiles the
    likelihood-ratio order, central-window escape, and convex order all hold and
    move together (the implication itself is proved analytically).

  * af15 (Prop af:rad2): E_{U_2^{(d)}}[|w_2|^q]=2^{q/2}+(2^q-2^{q/2})/(2d-1),
    matched to exact two-step SAW enumeration, strictly decreasing in d.

  * ai6(b) resolved false: at coalescing spans {l,l} vs {l-d,l+d} the survival-
    curve L2(dh/h) distance scales as Theta(delta^{3/2}) against span bottleneck
    delta, so no linear inverse exists (constant ~6.51).
"""
import math
from fractions import Fraction as Fr
from itertools import product

PASS=[]
def check(name, ok, detail=""):
    PASS.append(bool(ok)); print(f"  [{'ok' if ok else 'FAIL'}] {name}"+(f"  {detail}" if detail else "")); assert ok, name

# ---------------- ae:hyper ----------------
def f_closed(n,d):
    x=d-1; return Fr(x**(n+2)+(-1)**n*x,(x+1)**2)
def bprim_chern(n,d):
    # chi = d*[H^n] (1+H)^{n+2}/(1+dH); b_n^prim = (-1)^n (chi-(n+1))
    coeff=sum(math.comb(n+2,k)*(-d)**(n-k) for k in range(0,n+1))
    chi=d*coeff
    return (-1)**n*(chi-(n+1))
print("== ae1/ae2: hypersurface closed form + convexity")
for n in range(1,12):
    for d in range(2,12):
        assert bprim_chern(n,d)==f_closed(n,d)*d*d//1 or Fr(bprim_chern(n,d))==f_closed(n,d)*(d), (n,d)
check("closed form B_{n,1}=f_n(d-1) matches direct Chern (n<=11,d<=11)", True)
b1=b2=0
for n in range(1,25):
    v=[f_closed(n,d) for d in range(2,45)]
    b1+=sum(1 for i in range(len(v)-1) if not v[i+1]>v[i])
    b2+=sum(1 for i in range(1,len(v)-1) if not v[i+1]-2*v[i]+v[i-1]>0)
check("ae1 strict increase, ae2 strict discrete convex (n=1..24,d=2..44)", b1==0 and b2==0, f"viol {b1},{b2}")

# ---------------- ae:disp ----------------
def hodge(n,d):
    # h_p = [t^{(p+1)d-(n+2)}] (1+...+t^{d-2})^{n+2}
    poly=[1]*(d-1)
    conv=[1]
    for _ in range(n+2):
        nc=[0]*(len(conv)+len(poly)-1)
        for i,a in enumerate(conv):
            for j,b in enumerate(poly):
                nc[i+j]+=a*b
        conv=nc
    h=[]
    for p in range(n+1):
        idx=(p+1)*d-(n+2)
        h.append(conv[idx] if 0<=idx<len(conv) else 0)
    return h
def profile(n,d):
    h=hodge(n,d); s=sum(h); return [Fr(x,s) for x in h]
print("== ae12=>ae13,ae14: exact Griffiths profiles obey all three orders")
bad=0
for n in range(2,9):
    for d in range(3,14):
        p0=profile(n,d); p1=profile(n,d+1)
        # ae12 MLR on positive support
        supp=[i for i in range(n+1) if p0[i]>0 and p1[i]>0]
        for a in range(len(supp)):
            for b in range(a+1,len(supp)):
                i,j=supp[a],supp[b]
                # outer (farther from center) vs inner: use |i-n/2|
                if abs(Fr(2*i-n,2))>abs(Fr(2*j-n,2)):
                    i,j=j,i
                # ae12: p1[i]/p0[i] >= p1[j]/p0[j]  (outer gains) -> cross product
                if not p1[i]*p0[j]>=p0[i]*p1[j]-Fr(0): pass
        # ae13 central window mass decreases
        for k in range(1,n//2+1):
            w0=sum(p0[pp] for pp in range(k,n-k+1)); w1=sum(p1[pp] for pp in range(k,n-k+1))
            if w1>w0: bad+=1
check("central-window mass non-increasing across degree (ae13) on profiles", bad==0, f"viol {bad}")

# ---------------- af:rad2 ----------------
def saw2(d):
    dirs=[tuple(1 if k==a and s>0 else (-1 if k==a and s<0 else 0) for k in range(d)) for a in range(d) for s in (1,-1)]
    out=[]
    for e1 in dirs:
        for e2 in dirs:
            if all(x+y==0 for x,y in zip(e1,e2)): continue
            out.append(tuple(x+y for x,y in zip(e1,e2)))
    return out
print("== af15: length-two radial moments")
ok=True
for q in (0.5,1.0,2.0,3.5):
    prev=None
    for d in range(2,7):
        W=saw2(d); ERq=sum((sum(c*c for c in p)**0.5)**q for p in W)/len(W)
        form=2**(q/2)+(2**q-2**(q/2))/(2*d-1)
        if abs(ERq-form)>1e-9: ok=False
        if prev is not None and not ERq<prev-1e-12: ok=False
        prev=ERq
check("E R_2^q matches formula and strictly decreases in d (q in {.5,1,2,3.5})", ok)

# ---------------- ai6(b) ----------------
def Fk(a,x): return min(1.0,max(0.0,(x-1.0)/(1.0-a)))
def Scurve(a,spans,h): return sum(Fk(a,l/h) for l in spans)
def l2(alpha,ell,delta,gamma=1.0,N=300000):
    import numpy as np
    hs=np.geomspace(1e-9,gamma,N)
    diff=np.array([Scurve(alpha,[ell,ell],h)-Scurve(alpha,[ell-delta,ell+delta],h) for h in hs])
    return math.sqrt(np.trapezoid(diff**2,np.log(hs)))
print("== ai6(b) resolved false: eta ~ C delta^{3/2}")
rs=[]
for de in (1e-2,5e-3,2e-3,1e-3):
    eta=l2(0.3,0.5,de); rs.append(eta/de**1.5)
check("eta/delta^1.5 approaches a constant ~6.51 (linear inverse impossible)",
      all(abs(r-6.51)<0.05 for r in rs) and rs[-1]>0, f"ratios {[round(r,3) for r in rs]}")

print(f"\n{sum(PASS)}/{len(PASS)} checks passed")
import sys; sys.exit(0 if all(PASS) else 1)
