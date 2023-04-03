def func(arr, k):
    res = float('-inf')
    l = len(arr)
    i = 0

    while (i+k-1 < l): # To get elements such that there are k elements after the curr index
        curr_sum = 0
        for j in range(k):
            curr_sum += arr[i+j] # to sum k elements from each index possible

        res = max(res, curr_sum)
        i += 1
    
    return res

# print(func([10,5,-2,20,1],3))
