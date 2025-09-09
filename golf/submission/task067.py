p=lambda j:[R[:int(len(j[0])/3)]for R in j]

def solve_2dee498d(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

