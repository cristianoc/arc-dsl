p=lambda j:[r[3%len(r):]+r[:3%len(r)]for r in j[2:]+j[:2]]

def solve_25ff71a9(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

