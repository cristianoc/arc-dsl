def p(j):A=lambda c:[*map(list,zip(*c[::-1]))];return[c+y for c,y in zip(j,A(j))]+[c+y for c,y in zip(A(A(A(j))),A(A(j)))]

def solve_46442a0e(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

