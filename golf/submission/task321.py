def p(j):
 for A in range(4):
  for c in range(4):
   if j[A][c+5]>0:j[A][c+10]=j[A][c+5]
   if j[A][c]>0:j[A][c+10]=j[A][c]
 return[R[10:]for R in j]

def solve_cf98881b(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

