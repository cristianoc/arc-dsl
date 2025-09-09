def p(j):
 A=sum(j,[]).index(2);c,E=divmod(A,5);j[c][E]=0
 if c*E:j[c-1][E-1]=3
 if c<2and E:j[c+1][E-1]=8
 if E<4and c:j[c-1][E+1]=6
 if c<2and E<4:j[c+1][E+1]=7
 return j

def solve_a9f96cdd(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

