def isSubset( a1, a2, n, m):
    d = dict()
    for i in a1:
        if i in d:
            d[i] += 1
        
        else:
            d[i] = 1
    
    for i in a2:
        if i not in d or d[i]==0:
            return "No"
        
        d[i] -= 1
    
    
    return "Yes"
    
