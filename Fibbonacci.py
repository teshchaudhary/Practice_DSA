# Starting point is zero

def generator(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    return generator(n-1)+generator(n-2)


print(generator(6))