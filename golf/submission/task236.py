def p(j,A=range(4)):
 for c in A:
  for E in A:
   j[c][E]+=j[c+5][E]
   if j[c][E]==3:j[c][E]=0
   elif j[c][E]>0:j[c][E]=3
 return j[:4]

def solve_99b1bc43(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

