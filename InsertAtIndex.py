def insertAtIndex(arr, sizeOfArray, index, element):
    arr.append(0)

    i = sizeOfArray

    while i > index-1:
        arr[i] = arr[i-1]
        i -= 1
    arr[index] = element
    return arr

print(insertAtIndex([1,2,3,4,5],6,5,90))