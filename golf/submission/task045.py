def p(j):
	for A in j:
		for c in{*A}-{0}:
			E=A.index(c);k=len(A)-A[::-1].index(c)
			for W in range(E,k):
				if~A[W]:A[W]=c
	return j

def solve_22eb0ac0(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

