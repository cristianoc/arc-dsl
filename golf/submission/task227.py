p=lambda g:[[2*(g[i][j]==0==g[i+4][j])for j in range(4)]for i in range(4)]

def solve_94f9d214(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

