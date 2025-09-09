p=lambda j:list(map(list,zip(*[[0]*c.count(0)+[x for x in c if x]for c in zip(*j)])))

def solve_1e0a9b12(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

