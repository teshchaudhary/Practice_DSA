# def powerOfTwo(n):
#     a = 1
#     while a<=n:
#         if a == n:
#             return True
#         a<<=1
    
#     return False

# def powerOfTwo(n):
#     if n == 0:
#         return False
    
#     while n!=1:
#         if n % 2 != 0:
#             return False
#         n>>=1
    
#     return True

# Tricky Method
def powerOfTwo(n):
    if n == 0:
        return False
    return n&(n-1) == 0 # if number is of the power of two
                        # It will give 0 otherwise some other number

print(powerOfTwo(4))
