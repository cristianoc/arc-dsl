def p(g):
 g=[g[0]]+g+[g[-1]]
 g=[[R[0]]+R+[R[-1]]for R in g]
 for r,c in[[0,0],[0,-1],[-1,0],[-1,-1]]:g[r][c]=0
 return g

def solve_49d1d64f(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

