# Naive Solution
def count(n):
    res = 0
    while n!=0:
        # if n&1 == 1:
        #     c+=1
        res += n&1
        n >>= 1

    return res

# Brian Kernigam's Algo
# if n = 40: 101000
# then (n-1) = 39: 100111
# n&(n-1 = 32 : 100000
# All the bits after first set bit becomes 1 
def count(n):
    res = 0
    while n:
        n = n&(n-1)
        res += 1
    
    return res

print(count(10))
