def p(j):j=[R[::-1]+R for R in j];A=[j[2],j[1],j[0]];return A+j+A

def solve_8d5021e8(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

