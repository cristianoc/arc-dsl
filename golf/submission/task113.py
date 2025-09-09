p=lambda j:j[:5]+j[:5][::-1]

def solve_496994bd(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

