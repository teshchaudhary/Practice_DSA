# def computePower(m,n):

#     if n == 0:
#         return 1

#     temp = computePower(m, n//2)

#     if n % 2 == 0:
#         return temp*temp

#     else:
#         return m * computePower(m,n-1)

# print(computePower(5,4))


# Optimized

# def power(m, n):
#     res = 1

#     while n > 0:
#         if n % 2 != 0:  # The bit becomes 1
#             res *= m
#             # No need to do anything for 0
#         m *= m
#         n //= 2

#     return res


# print(power(2, 10))

# when mod is given for bigger powers then

# -> reduce every multiply with the mod k (if mod k is given)

def power(m, n):
    res = 1

    while n > 0:
        if n & 1 != 0:  # The bit is one
            res *= m
            # No need to do anything for 0
        m *= m
        n >>= 1

    return res

# Also Handles the negative powers
def negation_handled_power(m, n):
    res = 1
    negative_exponent = n < 0
    n = abs(n)
    while n:
        if n & 1:
            res *= m
        
        m *= m
        n >>= 1
    
    return 1/res if negative_exponent else res
