def p(j,A=enumerate):
 for c,E in A(j):
  for k,W in A(E):
   if W==5:
    for l in range(c-1,c+2):
     for J in range(k-1,k+2):
      if[l,J]!=[c,k]:j[l][J]=1
 return j

def solve_4258a5f9(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

