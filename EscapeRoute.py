# Find a way out of the maze (nxm) such that that meets the following requirements:

# > The path starts from a cell (a,b) and ends at cell (c,d), where |a-c| + |b-d| = 1
# > The path traverses every cell in the maze exactly once
# > John can only move in the four directions: up, down, left, and right

def func(n, m):

    if n % 2 == 1 or m % 2 == 1:
        return "No"
    
    if n % 2 == 0 and m % 2 == 0:
        return "Yes"
    
    return "No"
    
n,m = map(int, input().split())
print(func(n,m))
