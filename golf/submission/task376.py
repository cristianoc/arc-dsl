p=lambda j:(j+j[-2:0:-1])*2+j[:1]

def solve_eb281b96(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

