p=lambda j:[[k]for k,_ in __import__('collections').Counter(i for r in j for i in r).most_common(5)[2:]]

def solve_f8b3ba0a(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

