def count(n):
    c = 0
    while n!=0:
        if n&1 == 1:
            c+=1
    
        n>>=1

    return c

print(count(10))
