import math
# Wychoff's Game

def func(A,B):
    if (A>B):
        A,B = B,A
    
    diff = (B-A)
    goldenRatio = (1+math.sqrt(5))//2

    checkBy = goldenRatio * diff

    if checkBy == A:
        return False
    
    else:
        return True
