p=lambda j:j+j[::-1]

def solve_8be77c9e(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

