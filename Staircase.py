def staircase(n):
    if n == 0:
        return 1

    if n<0:
        return 0
    
    return staircase(n-1)+staircase(n-2)+staircase(n-3)

print(staircase(5))