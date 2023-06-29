#For a given non-negative integer N, find the next smallest Happy Number. A number is called Happy if it leads to 1 after a sequence of steps. Wherein at each step the number is replaced by the sum of squares of its digits that is, if we start with Happy Number and keep replacing it with sum of squares of its digits, we reach 1 at some point.

def func(n):
    if n == 1 or n == 7 or n == 10:
        return True
    
    if n < 10:
        return False
    
    res = 0
    while n:
        res += (n%10)**2
        n//=10
    
    if func(res):
        return True
    
    return False

def nextHappy (N):
        
    N += 1
    
    while N != 100000:
        if func(N):
            return N
        
        else:
            N += 1
    
    return -1
