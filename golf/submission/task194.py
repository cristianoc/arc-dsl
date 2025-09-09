j=lambda A:[[*i]for i in zip(*A[::-1])]
p=lambda c:[a+b for a,b in zip(c,j(c))]+[a+b for a,b in zip(j(j(j(c))),j(j(c)))]

def solve_7fe24cdd(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

