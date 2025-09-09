j=lambda A:[[A[J][x]for J in range(len(A))]for x in range(len(A[0]))]
def p(A):
 c,E=len(A),len(A[0])
 if E>c:return j(p(j(A)))
 k,W,l=0,c,0
 for J,a in enumerate(A):
  if a[0]==2:k=J
  if any(i==3 for i in a):W,l=min(W,J),J
 if W<k:return p(A[::-1])[::-1]
 return A[:k+1]+A[W:l+1]+[[8]*E]+[[0]*E]*(c-k+W-l-3)

def solve_56dc2b01(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

