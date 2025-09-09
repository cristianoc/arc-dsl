p=lambda g:[[3if g[i][j]==0and g[i+5][j]==0else 0for j in range(4)]for i in range(4)]

def solve_6430c8c4(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

