p=lambda j,A=range(4):[[j[x][y+4]or j[x+4][y]or j[x+4][y+4]or j[x][y]for y in A]for x in A]

def solve_75b8110e(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

