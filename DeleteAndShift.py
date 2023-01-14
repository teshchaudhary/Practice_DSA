def deleteFromArray(arr, n, idx):  # Last element will be 0
    for i in range(idx, n-1):
        arr[i] = arr[i+1]

    arr[n-1] = 0
    return arr


print(deleteFromArray([1, 2, 3, 4, 5], 5, 3))

# Delete and shift by an element(First Occurence) in list
def das(arr, ele):
    i = 0
    l = len(arr)
    while i < l:
        if arr[i] == ele:
            for j in range(i, l-1):
                arr[j] = arr[j+1]
            arr[l-1] = 0
        i += 1

    return arr


print(das([1, 2, 3, 4, 5], 3))
