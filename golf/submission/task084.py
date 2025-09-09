def p(j):
 A=len(j)
 for c in range(1,len(j[0])):j[A-1][c]=4;j[A-c-1][c]=2
 return j

def solve_3bd67248(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

