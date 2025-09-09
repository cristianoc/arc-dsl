def p(j):
	A=range;c=[A[:]for A in j];E=j[5][0];k=[[j[l+1][A+1]for A in A(3)]for l in A(3)]
	for W in[(0,6),(0,12),(6,0),(6,6),(6,12),(12,0),(12,6),(12,12)]:
		for l in A(3):
			for J in A(3):a,C=W[0]+l+1,W[1]+J+1;c[a][C]=j[a][C]if k[l][J]==j[a][C]else E if k[l][J]else 0
	return c

def solve_1e32b0e9(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

