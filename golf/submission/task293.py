j=lambda A:[A[0]]*len(A)if A[0]else A
c=lambda E:[[E[y][x]for y in range(len(E))]for x in range(len(E[0]))]
k=lambda E:[j(A)for A in E]
p=lambda E:c(k(c(E)))if k(E)==E else k(E)

def solve_ba97ae07(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

