# Method 1
import heapq as hq
def kthSmallest(arr,k):

    hq.heapify(arr)

    for _ in range(k):
        res = hq.heappop(arr)

    return res

# Method 2
def lomuto(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthsmallest(arr, k) :
    l = 0 
    r = len(arr) - 1 
    while l <= r :
        p = lomuto(arr,l,r) 
        if p == k-1 :
            return arr[p] 
                
        elif p > k-1 :
            r = p - 1 
                
        else :
            l = p + 1 
    return [-1]
