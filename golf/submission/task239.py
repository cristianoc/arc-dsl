from collections import*
def p(j,A=range):
 c=Counter([x for r in j for x in r]).most_common(9);E,k=c[0][1],len(c);j=[[0 for _ in A(k)]for _ in A(E)]
 for W in A(k):
  for l in A(c[W][1]):j[l][W]=c[W][0]
 return j

def solve_9af7a82c(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

