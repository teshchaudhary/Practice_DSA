# Stock Prices are listed
# We need to maximize the profit


# Naive Solution
# Idea is to check all the pairs such that for a pair (xi, xj)
# j > i and xj > xi
# Profit will be (xj - xi) + maxProfit(0, i-1) + maxProfit(j+1, n-1)

def Func(arr, si, ei):
    if si > ei:
        return 0
    
    res = 0
    for i in range(si, ei):
        for j in range(i+1, ei+1):
            if (arr[j] > arr[i]):
                curr = arr[j] - arr[i] + Func(arr, 0, si-1) + Func(arr,j+1, len(arr) -1)
                res = max(curr, res)
    
    return res
