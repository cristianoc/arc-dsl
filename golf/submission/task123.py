def p(g,R=range):
 g=[[x for x in r if x>0] for r in g if r.count(0)<2]
 g=[[r[0]]*10 for r in g+g+g]
 for r in R(10):
  for c in R(10):g[r][c]=g[c][r]
 return g[:10]

def solve_539a4f51(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

