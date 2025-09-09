p=lambda g:[[g[i][j]or g[i][8-j]if g[i][j]*g[i][8-j]==0 else g[i][j]for j in range(4)]for i in range(len(g))]

def solve_e3497940(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

