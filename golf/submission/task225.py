def p(g,L=len,R=range):
 h,w=L(g),L(g[0])
 r=[r for r in R(h) if L(set(g[r]))>1][0]
 c=[c for c in R(w) if g[r][c]>0][0]
 P=[[-2,-2,g[r+1][c+1]],[2,-2,g[r][c+1]],[-2,2,g[r+1][c]],[2,2,g[r][c]]]
 for i in R(r,r+2):
  for j in R(c,c+2):
   for y,x,C in P:
    if 0<=y+i<h and 0<=x+j<w:
     g[y+i][x+j]=C
 return g

def solve_93b581b8(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

