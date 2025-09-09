p=lambda g:[[3if g[i][j]==5and(len(g[0])-1-j)%2==0else g[i][j]for j in range(len(g[0]))]for i in range(3)]

def solve_d406998b(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

