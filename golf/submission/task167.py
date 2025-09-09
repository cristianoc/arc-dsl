p=lambda j:[[[5,5,5],[0,0,0],[0,0,0]],[[5,0,0],[0,5,0],[0,0,5]],[[0,0,5],[0,5,0],[5,0,0]]][len(set(v for r in j for v in r))-1]

def solve_6e02f1e3(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

