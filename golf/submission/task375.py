def p(j):
 for A in range(len(j)):j[A][A]=j[-A-1][A]=0
 return j

def solve_ea786f4a(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

