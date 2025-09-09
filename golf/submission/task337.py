def solve_d511f180(I):
    O=tuple(tuple(8 if v==5 else 5 if v==8 else v for v in r) for r in I)
    return O

p=solve_d511f180

