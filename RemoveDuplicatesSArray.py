# Remove duplicates from sorted array

def rem(arr):
    res = 1
    for i in range(1,len(arr)):
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res += 1
    return arr[:res]
