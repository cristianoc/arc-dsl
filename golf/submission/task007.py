def p(g):R=range;L=len;d={(i+j)%3:c for i in R(L(g))for j in R(L(g[0]))for c in[g[i][j]]if c};return[[d.get((i+j)%3,0)for j in R(L(g[0]))]for i in R(L(g))]

def solve_05269061(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

