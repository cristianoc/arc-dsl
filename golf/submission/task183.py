def p(j):
	A=range;c=len(j);E=c//2-2;k=[];W=[j[0][0],j[0][-1],j[-1][0],j[-1][-1]]
	for l in A(2,c-2):
		J=[]
		for a in A(2,c-2):
			C=j[l][a]
			if C==8:e=(l-2)//E;K=(a-2)//E;C=W[e*2+K]
			J.append(C)
		k.append(J)
	return k

def solve_77fdfe62(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

