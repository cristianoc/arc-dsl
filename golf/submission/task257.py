def p(g,L=len,R=range):
 h,w=L(g),L(g[0])
 for r in R(4):
  for c in R(4):
   if g[r][c]==0:
    if g[r][c+5]>0:g[r][c]=g[r][c+5]
   if g[r][c]==0:
    if g[r+5][c]>0:g[r][c]=g[r+5][c]
   if g[r][c]==0:
    if g[r+5][c+5]>0:g[r][c]=g[r+5][c+5]
 return [r[:4] for r in g[:4]]

def solve_a68b268e(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

