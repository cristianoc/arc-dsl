j=len
A=range
def p(c):
	E,k=[],[];W,l=j(c),j(c[0])
	for J in A(W-4):
		for a in A(l-4):
			C=[[c[E+J][C+a]for E in A(5)]for C in A(5)];C=[a for J in C for a in J];C=sum([J for J in C if J==1])
			if C==16:E.append(J+2);k.append(a+2)
	for J in A(W):
		for a in A(l):
			if J in E or a in k:
				if c[J][a]!=1:c[J][a]=6
	return c

def solve_41e4d17e(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

