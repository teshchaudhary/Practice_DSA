# A frog jumps either 1, 2, or 3 steps to go to the top. In how many ways can it reach the top of Nth step. As the answer will be large find the answer modulo 1000000007.

# The pattern will be making a tribionacci series with 1, 2, 4 as initial terms
def countWays(n):
        
    a, b, c = 1,2,4
    
    if n == 1:
        return a
    
    elif n == 2:
        return b
    
    elif n == 3:
        return c
    
    else:
        for i in range(3,n):
            s = a + b + c
            a, b, c = b, c, s%((10**9)+7)
        
        return c
