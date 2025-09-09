p=lambda j:[[8*(not A|B)for(A,B)in zip(A,A[4:])]for A in j]

def solve_1b2d62fb(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

