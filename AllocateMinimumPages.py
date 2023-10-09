# Recursive Solution
def minPages(arr,n,k):
    
    # Sum up till the first partition
    if k == 1:
        return sum(arr[0:n])
    
    # Extra case
    if n == 1:
        return arr[0]
    
    res = float('inf')
    
    # Check for each partitions possible
    for i in range(1, n):
        res = min(res,max(minPages(arr,i,k-1),sum(arr[i:n])))
        
    return res
