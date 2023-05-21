def immediateSmaller(arr, x):
    res = 0
    for i in arr:
        if res < i < x:
            res = i

    if res == 0:
        return -1
    return res

def immediateSmaller(self,arr,n,x):
        res = -1
        for i in range(len(arr)):
            if arr[i] < x:
                if res == -1 or res < arr[i]:
                    res = arr[i]
        
        return res
print(immediateSmaller([1,2,3,4,5,6], 4))
