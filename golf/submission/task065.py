def p(j):
	A=range;c=(len(j)-1)//2
	if c==1:
		E=[j[0][0],j[0][2],j[2][0],j[2][2]]
		for k in E:
			if E.count(k)==1:return[[k]]
	for(W,l)in[(0,0),(0,c+1),(c+1,0),(c+1,c+1)]:
		J=[[j[W+k][l+c]for c in A(c)]for k in A(c)];k=[J[k][E]for k in A(c)for E in A(c)]
		if len(set(k))>1:return J

def solve_2dc579da(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

