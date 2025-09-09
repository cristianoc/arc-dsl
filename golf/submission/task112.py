def p(j,h=enumerate):
 A=c=0
 for E,k in h(j):
  for W,l in h(k):A+=E*(l==3);c+=W*(l==3)
 A//=2;c//=2
 for E,k in h(j):
  for W,l in h(k):
   if l==2:
    for J,a in(E,W),(A-E,W),(E,c-W),(A-E,c-W):j[J][a]=2
 return j

def solve_4938f0c2(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

