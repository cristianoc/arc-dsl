def p(j):A={2:[[5,5,5],[0,5,0],[0,5,0]],1:[[0,5,0],[5,5,5],[0,5,0]],3:[[0,0,5],[0,0,5],[5,5,5]]};c=[i for s in j for i in s];return A[max(c)]

def solve_d4469b4b(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

