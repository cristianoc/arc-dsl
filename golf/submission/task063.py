def p(j):
 A=range
 c=len(j)
 E=[o[:]for o in j]
 for k in range(c):
  if j[1][k]==0and j[c-2][k]==0and sum(j[W][k]for W in A(1,c-1))==0:
   for W in A(1,c-1):E[W][k]=3
 for W in range(c):
  if j[W][1]==0and j[W][c-2]==0and sum(j[W][k]for k in A(1,c-1))==0:
   for k in A(1,c-1):
    if E[W][k]==0:E[W][k]=3
 return E

def solve_2bee17df(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

