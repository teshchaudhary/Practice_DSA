def minValue(a, b, n):
    res = 0
    a.sort()
    b.sort()

    for i in range(n):
        res += a[i]*b[n-i-1]

    return res
