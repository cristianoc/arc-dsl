def p(j,A=range):
	c,E=len(j),len(j[0]);k=[]
	for W in A(c-1):
		for l in A(E-1):
			J=j[W][l],j[W][l+1],j[W+1][l],j[W+1][l+1]
			if all(J):k+=[(W,l,len(set(J)))]
	for(W,l,a)in k:
		for C in A(a):
			e=W+2+C
			if e<c:j[e][l]=j[e][l+1]=3
	return j

def solve_fcc82909(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

