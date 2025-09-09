def p(g,L=len,R=range):
 h,w,x,y,b=L(g),L(g[0]),[],[],[]
 for r in R(h):
  for c in R(w):
   C=g[r][c]
   if C==2:x+=[c];g[r][c]=0
   if C==4:y+=[c];g[r][c]=0
   if C==1:b+=[c]
 for r in R(h):
  for c in R(w):
   if g[r][c]==1:g[r][c+(min(y)-min(b))]=4;g[r][c+(min(x)-min(b))]=2
 return g

def solve_1caeab9d(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

