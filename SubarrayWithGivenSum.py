def func1(arr, k):
    for i in range(len(arr)):
        curr = 0

        for j in range(i, len(arr)):
            curr += arr[j]
            if curr == k:
                return True

    return False

# arr = [3,2,0,4,7]
# print(func1(arr,6))
