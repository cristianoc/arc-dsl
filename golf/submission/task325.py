def p(j,A=range):
 c,E=len(j),len(j[0]);k=0
 def f(W,l):
  j[W][l]=0
  for J,a in(1,0),(-1,0),(0,1),(0,-1):
   C,e=W+J,l+a
   if 0<=C<c and 0<=e<E and j[C][e]:f(C,e)
 for K in A(c):
  for w in A(E):
   if j[K][w]:k+=1;f(K,w)
 return[[8*(K==w)for w in A(k)]for K in A(k)]

def solve_d0f5fe59(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

