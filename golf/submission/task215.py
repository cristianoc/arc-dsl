p=lambda j:[[r for j,r in enumerate(j)if sum(r)and j%3==i%3][0]for i in range(len(j))]

def solve_8eb1be9a(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

