def p(j):
	from collections import Counter as D;A=[c for l in j for c in l if c];c=dict(D(A).most_common());E=len(j[0]);k=[[0]*E for c in range(len(j))]
	for(W,l)in enumerate(sorted(c,key=c.get,reverse=True)):k[-1-W][-c[l]:]=[l]*c[l]
	return k

def solve_beb8660c(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

