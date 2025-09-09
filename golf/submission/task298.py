def p(j):A=len(j)//2;c=[j[i][i]for i in range(A)];E={c[i]:c[i-1]for i in range(A)};return[[E[i]for i in r]for r in j]

def solve_bda2d7a6(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

