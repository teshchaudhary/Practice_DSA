# Kadane
# Get sum of all normal contiguous subarray
def normalMaxSum(arr):
    res = arr[0]
    max_end = arr[0]

    for i in range(len(arr)):
        max_end = max(max_end+arr[i], arr[i])
        res = max(res, max_end)

    return res

# The intution is to find the minmum sum of the subarray
# To get this all we need is to invert all the elements' sign and then get the maximum sum of the subarray


def OverallMaxSum(arr):
    max_normal = normalMaxSum(arr)
    # If each element in the array is negative then the maximum sum will come from this only
    if max_normal < 0:
        return max_normal

    # Circular Sum
    arr_sum = 0

    # This will give the maximum subset sum of the inverted array
    for i in range(len(arr)):
        arr_sum += arr[i]
        arr[i] = -arr[i]

    max_circular = arr_sum + max_normal

    return max(max_circular, max_normal)
