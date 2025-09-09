def p(g,L=len,R=range):
 h,w=L(g),L(g[0])
 f=sum(g,[]);C=sorted([[f.count(k),k] for k in set(f)])[0][1]
 P=[[0,1],[0,-1],[-1,0],[1,0]]
 for r in R(h):
  for c in R(w):
   if g[r][c]==C:
    m=[]
    for y,x in P:
     if r+y>=0 and c+x>=0 and r+y<h and c+x<w:
      m+=[g[r+y][c+x]]
    if sum(m)/L(m)<max(m)/2:
     g[r][c]=0
    else: g[r][c]=max(m)
 return g

def solve_7e0986d6(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

