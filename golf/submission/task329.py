def p(j):
	A=len(j[0])//2;c=[[0 for A in A]for A in j]
	for E in range(len(j)):c[E][A]=j[E][A]
	return c

def solve_d23f8c26(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

