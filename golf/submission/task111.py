p=lambda g:next([g[i+k][j-1:j+2]for k in(1,2,3)]for i,r in enumerate(g)for j,x in enumerate(r)if x==5)

def solve_48d8fb45(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

