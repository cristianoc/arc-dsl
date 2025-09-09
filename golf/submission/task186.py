p=lambda j,A=[2]*3,c=[0]*3:[[A,[0,2,0],c],[A,c,c],[[2,2,0],c,c],[[2,0,0],c,c]][4-sum(r.count(1)for r in j)]

def solve_794b24be(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

