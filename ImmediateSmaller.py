def immediateSmaller(arr, x):
    res = 0
    for i in arr:
        if res < i < x:
            res = i

    if res == 0:
        return -1
    return res

print(immediateSmaller([1,2,3,4,5,6], 4))