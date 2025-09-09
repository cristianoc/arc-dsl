p=lambda g:[[3if g[i][j]+g[i+7][j]==2else 0for j in range(5)]for i in range(6)]

def solve_3428a4f5(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

