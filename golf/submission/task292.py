def p(j):
 for A in j:A[::3]=[6 if v==4 else v for v in A[::3]]
 return j

def solve_ba26e723(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

