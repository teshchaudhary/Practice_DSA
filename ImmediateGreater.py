def immediateGreater(arr, x):
    diff = None
    res = 0
    for i in arr:
        if i > x:
            if diff is None:
                diff = i-x
                res = i
            elif i-x < diff:
                diff = i-x
                res = i

    if res == 0:
        return -1
    else:
        return res


print(immediateGreater([9, 11, 12, 13], 10))
