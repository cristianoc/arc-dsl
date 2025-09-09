def p(j,A=enumerate):c,E=zip(*[(i,j)for i,r in A(j)for j,x in A(r)if x]);return[r[min(E):max(E)+1]for r in j[min(c):max(c)+1]]

def solve_1cf80156(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

