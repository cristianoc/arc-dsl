def p(j):
 for A in range(4):
  for c in range(3):
   j[A][c]+=j[A][c+4]
   if j[A][c]>0:j[A][c]=0
   else:j[A][c]=3
 return[R[:3]for R in j]

def solve_f2829549(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

