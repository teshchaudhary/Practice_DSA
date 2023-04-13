# O(3^n)

def cutRope(n, a, b, c):
    if n == 0:
        return 0

    if n < 0:
        return -1

    res = max(cutRope(n-a, a, b, c),
              cutRope(n-b, a, b, c),
              cutRope(n-c, a, b, c),)

    return -1 if res == -1 else res + 1


print(cutRope(5, 2, 5, 1))
