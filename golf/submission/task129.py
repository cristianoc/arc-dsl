def solve_5582e5ca(I):
    flat=[v for r in I for v in r]
    c=max(set(flat), key=flat.count)
    O=tuple((c,)*3 for _ in range(3))
    return O

p=solve_5582e5ca

