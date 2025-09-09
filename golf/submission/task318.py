def p(j):return[[3 if j[r][c]or j[r+5][c]else 0 for c in range(4)]for r in range(4)]

def solve_ce4f8723(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

