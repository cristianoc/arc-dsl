def p(g,E=enumerate):Z={c for R in g for c,v in E(R)if v==2};return[[1 if 1 in R else 3 if 3 in R else 2 if v<1and c in Z else v for c,v in E(R)]for R in g]

def solve_178fcbfb(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

