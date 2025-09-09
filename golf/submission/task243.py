def p(g,L=len,R=range):
 h,w=L(g),L(g[0])
 for z in R(25):
  for r in R(h):
   for c in R(w):
    if g[r][c]==0:
     if c+1<w:
      if g[r][c+1]==1:g[r][c]=1
     if r+1<h:
      if g[r+1][c]==1:g[r][c]=1
     if c-1>=0:
      if g[r][c-1]==1:g[r][c]=1
     if r-1>=0:
      if g[r-1][c]==1:g[r][c]=1
 return g

def solve_9edfc990(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

