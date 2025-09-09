p=lambda j,A=range(9):[[j[r%3][c%3]*(j[r//3][c//3]==2)for c in A]for r in A]

def solve_cce03e0d(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

