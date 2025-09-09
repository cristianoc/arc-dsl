def p(j):
	for A in range(len(j[0])):
		if j[-1][A]==2:
			c=0
			for E in range(len(j)):
				if j[-(E+1)][A+c]==5:c+=1;j[-E][A+c]=2
				j[-(E+1)][A+c]=2
	return j

def solve_d9f24cd1(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

