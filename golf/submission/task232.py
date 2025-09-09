def p(j,A=enumerate):
 for c,E in A(j):
  k,W,l=0,[],0
  for J,a in A(E):
   if a>0:W=[a,5]*20;l=1
   if l:j[c][J]=W[k];k+=1
 return j

def solve_97999447(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

