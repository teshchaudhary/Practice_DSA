# Given a sorted array of positive integers rearrange the array elements in a way that first element should be max value,
# second should be min value, third should be second max, fourth should be second min and so on.
# Modify the original array itself. Do it without using any extra space. You do not have to return anything

def rearrange(arr, n):
    si, ei = 0, n-1

    maxi = arr[ei]+1

    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[ei] % maxi)*maxi
            ei -= 1

        else:
            arr[i] += (arr[si] % maxi)*maxi
            si += 1

    for i in range(n):
        arr[i] = arr[i]//maxi
