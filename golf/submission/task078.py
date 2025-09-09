def p(j,A=range):
	c,E=len(j),len(j[0]);k=[[0]*E for W in A(c)]
	for W in A(E):
		l=[j[c][W]for c in A(c)if j[c][W]!=0]
		for(J,a)in enumerate(l):k[J][W]=a
	return k

def solve_3906de3d(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

