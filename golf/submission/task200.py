def p(j):
 A,c,E,k=10,enumerate,range,0
 for W,l in c(j):
  for J,a in c(l):
   if a%5:
    for C in E(J,A,2):
     for e in E(W+1):j[e][C]=a
    for C in E(J+1,A,2):j[k*(A-1)][C]=5;k^=1
    return j

def solve_8403a5d5(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

