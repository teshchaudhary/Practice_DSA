def helper(arr):
    d = {}
    for a in arr:
        d[a] = d.get(a, 0) + 1
    
    return d
    
def check(A,B,N):
    d = helper(A)
        
    for b in B:
        if b not in d:
            return False
        
        d[b] -= 1
        
        
        if d[b] != 0:
            return False

    return True
