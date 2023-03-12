def isSparse(n):
    return n & (n >> 1) == 0
