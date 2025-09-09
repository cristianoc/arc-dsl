p=lambda j:[[x for x in sum(j,[])if x]]

def solve_d631b094(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

