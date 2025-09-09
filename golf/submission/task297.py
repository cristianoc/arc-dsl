def p(j):
 A,c=len(j),len(j[0]);E=j[0]*20
 for k in range(2,A):j[k]=[E[k-2]for _ in range(c)]
 return j

def solve_bd4472b8(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

