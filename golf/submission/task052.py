p=lambda j:[[5]*3if len(set(r))==1else[0]*3for r in j]

def solve_25d8a9c8(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

