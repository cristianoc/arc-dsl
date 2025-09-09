p=lambda j:[[[2,4,3][r.index(5)]]*3for r in j]

def solve_a85d4709(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

