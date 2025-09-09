def p(j,A=range):
 c=len(j);E=len(j[0]);p=[J[:]for J in j]
 for k in A(E):
  W=[J for J in A(c)if j[J][k]];l=len(W)//2
  for J in A(l):p[W[-1-J]][k]=8
 return p

def solve_ce9e57f2(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

