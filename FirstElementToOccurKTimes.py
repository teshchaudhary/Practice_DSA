def firstElementKTime(a, k):
    d = dict()
        
    for i in a:
        d[i] = d.get(i,0)+1
            
        if d[i] == k:
            return i
                
    return -1 
