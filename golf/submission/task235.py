p=lambda j:[[(45-j[2][x]-2*j[2][x+1]-4*j[1][x+1])//5]*3 for x in range(0,15,5)]

def solve_995c5fa3(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

