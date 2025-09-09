p=lambda j:[[1if[j[i][0]for i in range(3)]==[j[i][2]for i in range(3)]else 7]]

def solve_44f52bb0(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

