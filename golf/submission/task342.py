def p(j,A=enumerate):
 c=lambda E,k:sum([[L,b]for L,r in A(j)for b,v in A(r)if v in E and v not in k],[])
 E,k,W,l,J,a,C,e=c(range(10),[0,8]);K,w=c([8],[])[:2];j[K][w:w+2]=[j[E][k],j[W][l]][::(1,-1)[k>l]];j[K+1][w:w+2]=[j[J][a],j[C][e]][::(1,-1)[a>e]]
 for L,b in(E,k),(W,l),(J,a),(C,e):j[L][b]=0
 return j

def solve_d89b689b(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

