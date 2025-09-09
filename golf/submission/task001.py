p=lambda j,A=range(9):[[j[r//3][c//3]and j[r%3][c%3]for c in A]for r in A]

def solve_007bbfb7(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

