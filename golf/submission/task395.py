def p(g):t,b=g[:3],g[3:];return[[2if t[r][c]==b[r][c]==0else 0for c in range(3)]for r in range(3)]

def solve_fafffa47(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

