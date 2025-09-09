def p(j):
 A=[o[:]for o in j]
 c,E=len(j),len(j[0])
 for k in range(1,c):
  for W in range(1,E-1):
   if j[k][W]==0and j[k][W-1]and j[k][W+1]and j[k][W-1]==j[k][W+1]and j[k-1][W]==j[k][W-1]:A[c-1][W]=4
 return A

def solve_54d82841(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

