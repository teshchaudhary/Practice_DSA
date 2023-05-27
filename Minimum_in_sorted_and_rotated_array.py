def minNumber(arr, low, high):

    if arr[low] < arr[high]:
        return arr[low]

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < arr[high]:
            high = mid
        else:
            low = mid + 1

    return arr[low]
