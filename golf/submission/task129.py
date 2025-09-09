p=lambda j:[[max(sum(j,[]),key=sum(j,[]).count)]*3]*3

def solve_5582e5ca(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

