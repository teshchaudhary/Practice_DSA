def count(n):
    res = 0
    while n!=0:
        # if n&1 == 1:
        #     c+=1
        res += n&1
        n >>= 1

    return res

print(count(10))
