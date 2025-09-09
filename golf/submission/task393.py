p=lambda j:[[k]for k,_ in __import__('collections').Counter(i for r in j for i in r).most_common(4)[1:]]

def solve_f8ff0b80(I):
    L=[list(r) for r in I]
    R=p(L)
    return tuple(tuple(r) for r in R)

