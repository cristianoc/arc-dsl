def p(j):A=tuple(0if v==0else 1for v in j[0]);return[[{(1,1,0):1,(1,0,1):2,(0,1,1):3,(0,1,0):6}[A]]]

def solve_27a28665(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

