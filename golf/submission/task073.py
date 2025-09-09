def p(j):
 A=[o[:]for o in j]
 for c in range(5):
  for E in range(5):
   if j[E][c]==1:A[E][c]=0;A[4][c]=1
 return A

def solve_3618c87e(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

