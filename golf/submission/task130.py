def solve_5614dbcf(I):
    A=tuple(tuple(0 if v==5 else v for v in r) for r in I)
    O=tuple(tuple(r[::3]) for r in A[::3])
    return O

p=solve_5614dbcf

