def p(j):A=lambda c:list(map(all,c)).index(1);E,k=A(j),A(zip(*j));j[E-1][k-1:k+2]=j[E+1][k-1:k+2]=[4]*3;j[E][k-1]=j[E][k+1]=4;return j

def solve_67a423a3(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

