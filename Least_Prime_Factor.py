def prime(n):
    if n%2 == 0: return 2
    if n%3 == 0: return 3
    
    i = 4
    
    while i*i < n+1:
        if n % i == 0:
            return i
        
        i += 1
    
    return n
    
    
def leastPrimeFactor (self, n):
    res = [0, 1, 2, 3, 2]f
    for i in range(5, n+1):
        res.append(prime(i))
    return res
            
