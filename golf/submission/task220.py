def p(j,A=enumerate):
 c={8:4,2:1,3:6};E=[[J for a,J in A(W)]for W in j]
 for k,W in A(j):
  for l,J in A(W):
   if J:
    for a in range(-1,2):
     for C in range(-1,2):
      try:
       if[a,C]!=[0,0]:E[k+a][l+C]=c[J]
      except:0
 return E

def solve_913fb3ed(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

