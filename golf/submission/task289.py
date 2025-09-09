p=lambda j:(A:=len(set(sum(j,[]))-{0}),[[x for x in r for _ in range(A)]for r in j for _ in range(A)])[1]

def solve_b91ae062(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

