def p(j):A=[i for s in j for i in s];A=[c for c in set(A)if c not in[0,5]][0];j=[[A if C==5 else 0 for C in R]for R in j];return j

def solve_f76d97a5(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

