def p(j,A=0):
 for c in j:
  for E,k in enumerate(c):
   if k:A=(not A)*k
   else:c[E]=A
 return j

def solve_22168020(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

