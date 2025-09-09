p=lambda j:(A:=sum(c>0for r in j for c in r),[sum(([x]*A for x in r),[])for r in j for _ in range(A)])[1]

def solve_ac0a08a4(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

