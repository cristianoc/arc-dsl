def p(j,A=range):
 c=len(j)
 for E in A(1,c-1):
  k=W=0
  for l in A(c):
   J=j[E][l];k=[k,1][k<1and J>1]
   if k==1and J<1:k=2;W=[W,l][~W]
   if k>1and J>1:
    for a in A(W,l):j[E][a]=9;k=1;W=0
 return j

def solve_ef135b50(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

