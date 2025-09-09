p=lambda g:[[g[i%5][j%6]for j in range(len(g[0])*2)]for i in range(len(g)*1)]

def solve_963e52fc(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

