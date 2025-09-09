def p(g):q=range;c=sum(all(g[i+k][j+l]==1for k in q(2)for l in q(2))for i in q(8)for j in q(8));return[[1if i<c else 0for i in q(5)]]

def solve_1fad071e(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

