def p(j):
 A,c,E=j;k=6,4,0,0,0,1,3,1,0,0,0,4
 for W in range(len(A)):
  l=k[W%12]
  if l&1:A[W]=4
  if l&2:c[W]=4
  if l&4:E[W]=4
 return j

def solve_7447852a(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

