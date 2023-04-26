# Find the number of distinct ordered pairs (p, q) of prime numbers that satisfy the equation N = p + 2q.

def isPrime(n):
    if n == 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i*i <= n:
        if n % i == 0 or n % i+2 == 0:
            return False

        i += 1

    return True

def func(N):
    res = 0
    for p in range(3, N, 2):
        if isPrime(p):
            if isPrime((N - p) // 2):
                res += 1
    
    return res

print(func(int(input())))
