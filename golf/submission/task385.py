def p(j,A=enumerate):
 for c,E in A(j):
  for k,W in A(E):
   if c<len(j)//2:j[c][k]=j[-(c+1)][k]
 return j

def solve_f25ffba3(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

