def p(j,A=enumerate):
 for c,E in A(j):
  for k,W in A(E):
   for l,J in(c+1,k),(c-1,k),(c,k+1),(c,k-1):
    if W==2and 0<=l<len(j)and 0<=J<len(E)and j[l][J]==3:j[c][k]=0;j[l][J]=8
 return j

def solve_d90796e8(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

