def p(j,A=range(18)):
 for c in A:
  E,k,W=j[c:c+3]
  for l in A:
   J=l+3
   if sum(E[l:J]+k[l:J]+W[l:J])==0:E[l:J]=k[l:J]=W[l:J]=[1]*3
 return j

def solve_6cf79266(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

