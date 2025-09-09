p=lambda g,R=range(1,8):(G:=[[0]*9for _ in g],[G[i+a].__setitem__(j+b,(1,5)[a*b])for i in R for j in R if g[i][j]for a in(-1,0,1)for b in(-1,0,1)if a|b])[0]

def solve_b60334d2(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

