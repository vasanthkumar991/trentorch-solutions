def product(f, lo, hi):
    if hi<lo:
        return 1
    mul=1
    for i in range(lo,hi+1):
        mul*=f(i)
    return mul
    pass
