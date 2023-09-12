# Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number. Return 1 if the number is Perfect otherwise return 0.

def divisors(N):
    res = []
    i = 1
    while i*i <= N:
        if N%i == 0:
            res.append(i)
        i += 1
    
    i -= 1
    while i > 0:
        if N % i == 0:
            res.append(N//i)
        i -= 1
    
    return res


class Solution:
    def isPerfectNumber(self, N):
        
        if N == 1:
            return 0
            
        l = divisors(N)
        if sum(l) - N == N:
            return 1
        
        return 0
