# def allDivisors(n):
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             print(i)

#             if (i != n/i):
#                 print(n//i)

#         i += 1


# allDivisors(12)


# Prints in ascending order
def allDivisorsSorted(n):
    i = 1

    while i*i < n:
        if n % i == 0:
            print(i)

        i += 1

    while i >= 1:
        if n % i == 0:
            print(n//i)

        i -= 1


allDivisorsSorted(12)
