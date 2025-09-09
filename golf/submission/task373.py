p=lambda g:[[[g[i][j],g[1-i][j]][j%2]for j in range(6)]for i in range(2)]

def solve_e9afcf9a(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

