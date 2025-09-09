p=lambda g,R=range:[[[g[k+i][j]for j in R(3)]for i in R(3)]for k in R(0,9,3)if[[g[k+i][j]for j in R(3)]for i in R(3)]!=[[g[k+j][i]for j in R(3)]for i in R(3)]][0]

def solve_662c240a(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

