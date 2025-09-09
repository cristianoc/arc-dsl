def p(j,A=enumerate):
 c=len(j)-1
 E=len(j[0])-1
 for k,W in A(j):
  for l,J in A(W):
   if k>0and l<c:
    if j[k][E]==5and j[0][l]==5:j[k][l]=2
 return j

def solve_2281f1f4(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

