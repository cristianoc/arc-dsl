def p(j):
	A=range;c=[[[j[D+c*3][A+E*3]for A in A(3)]for D in A(3)]for c in A(len(j)//3)for E in A(len(j[0])//3)]
	for E in c:
		if[tuple(tuple(c[E][A]==0 for A in A(3))for E in A(3))for c in c].count(tuple(tuple(E[c][A]==0 for A in A(3))for c in A(3)))==1:return E

def solve_a87f7484(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

