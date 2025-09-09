def p(j):A=(j[3][3]<1)*6;[j[r].__setitem__(slice(A,A+3),j[r][3:6][::-1])for r in range(3)];return j

def solve_760b3cac(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

