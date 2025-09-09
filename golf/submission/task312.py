def p(j):
 for A in j:
  for c in A:
   if c and c-5:A[:]=[c*(x==5)+x*(x!=5)for x in A];break
 return j

def solve_c9f8e694(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

