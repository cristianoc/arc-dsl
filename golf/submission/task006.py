p=lambda j:[[a and b and 2 for a,b in zip(r[:3],r[4:7])]for r in j[:3]]

def solve_0520fde7(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

