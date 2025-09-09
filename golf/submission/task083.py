def p(j):A=[r+r[::-1]for r in j];return A+A[::-1]

def solve_3af2c5a8(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

