def p(g):a=[i for i,r in enumerate(g)if any(r)];b=[j for j in range(len(g[0]))if any(r[j]for r in g)];return[r[b[0]:b[-1]+1][::-1]for r in g[a[0]:a[-1]+1]]

def solve_7468f01a(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

