def func(arr):
    arr.sort(key= lambda x: x[0])

    res = 0

    for i in range(1,len(arr)):
        if arr[res][1] >= arr[i][0]:
            arr[res][1] = max(arr[res][1], arr[i][1])
        
        else:
            res += 1
            arr[res] = arr[i]
    
    for i in range(res+1):
        yield arr[i]


arr = [[5,10],[3,15],[18,30],[2,7]]
a = func(arr)
print(a)
