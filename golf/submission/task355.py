def p(g,L=len,R=range):
 #values are overcounted - fix by changin once counted
 f=sum(g,[]);Z=sorted([[f.count(k),k] for k in set(f)])[0][1]
 h,w=L(g),L(g[0])
 P=[0 for _ in range(10)]
 for r in R(1,h-1):
  for c in R(1,w-1):
   C=g[r-1][c-1:c+2]+g[r][c-1:c+2]+g[r+1][c-1:c+2]
   if C.count(Z)>0 and L(set(C))==2:
     for T in set(C):
      if T!=Z:P[T]+=1
 return [[P.index(max(P))]]

def solve_de1cd16c(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

