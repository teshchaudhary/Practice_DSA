# This will give -1 in case if array is not sorted and rotated as well
# Eg: arr = [10, 20, 40, 6, 5, 8]
# In this case string is not rotated and sorted properly so for searching element 6 it will give -1

def func(arr, ele):
    si = 0
    ei = len(arr) - 1

    while si <= ei:
        mid = (si + ei) // 2

        if arr[mid] == ele:
            return mid
        
        if arr[si] < arr[mid]:
            if arr[si] <= ele < arr[mid]:
                ei = mid - 1
            
            else:
                si = mid + 1
        
        else:
            if arr[mid] < ele <= arr[ei]:
                si = mid + 1
                
            else:
                ei = mid - 1
    return -1

arr = [10, 20, 40, 5, 6, 8]
print(func(arr, 6))
