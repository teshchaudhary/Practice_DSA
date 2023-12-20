def findWinner(self, n, A):
    xor = 0
    for i in A:
        xor ^= i
    
    if xor == 0:
        return 1
    
    else:
        if len(A)%2 == 0:
            return 1
        
        else:
            return 2
