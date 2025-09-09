def p(g,L=len,R=range):
 h=L(g)
 w=L(g[0])
 C=g[h//2][:w//2]
 C={C[i]:C[-(i+1)] for i in R(L(C))}
 for r in R(h):
  for c in R(w):g[r][c]=C[g[r][c]]
 return g

def solve_85c4e7cd(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

