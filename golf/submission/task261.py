def p(j):j=[j[-1]]+j[:len(j)-1];j=[[2 if C==8 else C for C in R]for R in j];return j

def solve_a79310a0(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

