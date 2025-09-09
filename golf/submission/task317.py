def p(j,A=range):
 c=len(j);E=[[0 for _ in A(c)]for _ in A(c)]
 for k in A(c):
  for W in A(c):
   if j[k][W]==5:
    for l in A(max(0,k-1),min(c,k+2)):
     for J in A(max(0,W-1),min(c,W+2)):E[l][J]=1
 return E

def solve_ce22a75a(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

