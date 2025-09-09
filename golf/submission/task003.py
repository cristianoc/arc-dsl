p=lambda j:[[c*2 for c in r]for r in j+(j[:3],j[2:5])[j[1]!=j[4]]]

def solve_017c7c7b(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

