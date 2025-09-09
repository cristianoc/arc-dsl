def p(j):A=[i for r in j for i,x in enumerate(r)if x>0];c,E=min(A),max(A)+1;return[r[c:E]*2 for r in j if max(r)>0]

def solve_28bf18c6(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

