def p(g):
 g[-1]=g[0]=[8]*len(g[0])
 for r in range(len(g)):g[r][0]=8;g[r][-1]=8
 return g

def solve_6f8cd79b(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

