j=lambda A,c:sum(sum(i==c for i in r)for r in A)
def p(A):E=max(j([r],8)for r in A);k=(j(A,5)-E-2)/2-j(A,8)/E;return[[8*(k>0),8*(k>1),8*(k>2)],[0,0,8*(k>3)],[0,0,0]]

def solve_b0c4d837(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

