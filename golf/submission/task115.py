def p(j):
 def u(A):
  c=[]
  for E in A:
   if E not in c:c.append(E)
  return c
 k=[u(c)for c in j]
 if all(k[0]==c for c in k):return[k[0]]
 return[[E]for E in u([E for c in j for E in c])]

def solve_4be741c5(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

