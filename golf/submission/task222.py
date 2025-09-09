def p(g,L=len,R=range):
 h,w=L(g),L(g[0])
 n=[[0 for _ in R(w)]]
 g=n+g+n
 g=[[0]+r+[0] for r in g]
 for r in R(1,h+1):
  for c in R(1,w+1):
   C=g[r-1][c-1:c+2]+g[r][c-1:c+2]+g[r+1][c-1:c+2]
   if C.count(g[r][c])<4:g[r][c]=0
 return [r[1:-1] for r in g[1:-1]]

def solve_91714a58(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

