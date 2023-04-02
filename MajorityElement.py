# An element is considered a majority element if the element comes more than the half of the length of the array (freq(n) > length(arr)/2)
# Return the index of such element

# Naive Solution
# O(n^2)

def func1(arr):
    l = len(arr)
    threshold = l//2

    for i in range(len(arr)):
        count = 1

        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count > threshold:
            return i

    return -1
