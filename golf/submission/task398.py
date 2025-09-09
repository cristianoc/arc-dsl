def p(g,L=len,R=range):
 s=R(L([x for x in set(g[0])if x>0])*5)
 X=[[0 for x in s]for y in s]
 g=g[0]
 T=0
 for r in s:
  for c in R(5):
   try:X[-(r+1)][c+T]=g[c]
   except:pass
  T+=1
 return X

def solve_feca6190(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

