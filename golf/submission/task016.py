p=lambda j,A=[0,5,6,4,3,1,2,7,9,8]:[[A[x]for x in r]for r in j]

def solve_0d3d703e(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

