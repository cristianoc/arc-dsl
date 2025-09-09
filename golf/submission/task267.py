def p(j):A=j[6][0];c=[[r and A for r in X]for X in j];c[6][0]=0;return c

def solve_aabf363d(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

