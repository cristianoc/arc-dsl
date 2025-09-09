def p(g,L=len,E=enumerate):
 for C in set(sum(g,[])):
  P=[[x,y] for y,r in E(g) for x,c in E(r) if c==C]
  f=sum(P,[]);x=f[::2];y=f[1::2]
  X=g[min(y):max(y)]
  X=[r[min(x)+1:max(x)][:] for r in X]
  if X[0].count(C)==L(X[0]):
   return X[1:]
 return g

def solve_1c786137(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

