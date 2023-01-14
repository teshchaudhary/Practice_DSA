def peakElement(arr, n):
    si = 0
    ei = n-1

    while si <= ei:
        mid = (si+ei)//2
        if (mid == 0 or arr[mid] >= arr[mid-1]) and (mid == n-1 or arr[mid] >= arr[mid+1]):
            return mid
        elif arr[mid] < arr[mid+1]:
            si = mid+1

        else:
            ei = mid - 1


print(peakElement([17, 19, 9, 5, 3, 6, 17, 7, 18, 16, 18, 11, 3, 15, 2], 15))