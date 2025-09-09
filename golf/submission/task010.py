def p(j):
 A={}
 for c in j:
  for E,k in enumerate(c):
   if k==5:c[E]=A.setdefault(E,len(A)+1)
 return j

def solve_08ed6ac7(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

