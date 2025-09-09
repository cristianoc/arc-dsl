p=lambda g:[[g[i][j]or g[i+6][j]for j in range(11)]for i in range(5)]

def solve_e98196ab(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

