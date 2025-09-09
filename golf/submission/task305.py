def p(j):
	A=len(j);c=[A for c in j for A in c if A]
	if not c:return j
	E=sorted(set(c));k=len(E);W=[[0]*A for c in[0]*A]
	for l in range(A):
		for J in range(A):W[l][J]=E[(l+J)%k]
	return W

def solve_c3f564a4(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

