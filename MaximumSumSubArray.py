# A sub array is an array of contiguous element picked from an array
# Sub Array of {1,2,3} will be
# {1}, {2}, {3}, {1,2}, {2,3}, {1,2,3}
# {1,3} will not be an subarray as it is not contiguous

# O(n^2)
# Make every possible sum and checks if the value is increasing, if it increases then update the res otherwise no change as it will return the maximum of current value of curr and res.

def func1(arr):
    res = arr[0]
    l = len(arr)

    for i in range(l):
        curr = 0
        for j in range(i,l):
            curr += arr[j]
            res = max(res, curr)
    
    return res

arr = [1, -2, 3, -1, 2]
print(func1(arr))
